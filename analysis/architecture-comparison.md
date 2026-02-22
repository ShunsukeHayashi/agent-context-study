# AIコーディングエージェント コンテキストアーキテクチャ比較

## 調査対象（2026年2月時点）

| エージェント | 提供元 | OSS | 指示ファイル名 |
|-------------|--------|-----|---------------|
| Claude Code | Anthropic | ❌ プロプライエタリ | CLAUDE.md |
| Codex CLI | OpenAI | ✅ (github.com/openai/codex) | AGENTS.md |
| Gemini CLI | Google | ✅ (github.com/google-gemini/gemini-cli) | GEMINI.md |
| Cursor | Anysphere | ❌ プロプライエタリ | .cursor/rules/*.mdc |

---

## コンテキストロードモデルの比較

### Claude Code: 階層的オンデマンドロード
```
出典: code.claude.com/docs/en/memory

ロード順序:
1. Managed policy (/Library/Application Support/ClaudeCode/CLAUDE.md)
2. Project memory (./CLAUDE.md)
3. Project rules (./.claude/rules/*.md)
4. User memory (~/.claude/CLAUDE.md)
5. Project local (./CLAUDE.local.md)
6. Auto memory (~/.claude/projects/<project>/memory/)

特徴:
- 親ディレクトリのCLAUDE.md → 起動時に全文ロード
- 子ディレクトリのCLAUDE.md → オンデマンドロード（アクセス時）
- Auto memory: MEMORY.md をインデックスとしてトピックファイルへ自動参照
- 動的: セッション中もファイル探索が発生する
- 上限: 実質なし（動的ロードで分散）
```

### Codex CLI: 単一チェーン逐次連結
```
出典: developers.openai.com/codex/guides/agents-md/

ロード順序:
1. Global (~/.codex/AGENTS.override.md > AGENTS.md)
2. Project root → current dir まで下方向ウォーク
   各ディレクトリで: AGENTS.override.md > AGENTS.md > fallback names
   1ファイル/ディレクトリ

特徴:
- 起動時に1回だけ構築（セッション中の動的ロードなし）
- 各ディレクトリで1ファイルのみ
- 合計 32KB 上限 (project_doc_max_bytes)
- 超過分は無言切り捨て（ユーザー通知なし）
- 静的: 一度構築したら変更なし
```

### Gemini CLI: 階層的 + 双方向スキャン + インポート
```
出典: google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html
ソース: github.com/google-gemini/gemini-cli (OSS)

ロード順序:
1. Global (~/.gemini/GEMINI.md)
2. CWD → project root (上方向スキャン、.gitで停止)
3. CWD配下のサブディレクトリ（下方向スキャン、.gitignore/.geminiignore尊重）

特徴:
- 上方向 + 下方向の双方向スキャン
- @file.md 構文でインポート（モジュール化）可能
- /memory コマンドで実行中にコンテキストを追加・確認
- ファイル名カスタマイズ可能（AGENTS.md やカスタム名に変更可）
- 全ファイル連結してモデルに送信
```

### Cursor: ルールベース + グロブマッチ
```
出典: design.dev/guides/cursor-rules/, cursor公式docs

ロード順序:
1. User Rules (settings内、グローバル適用)
2. Project Rules (.cursor/rules/*.mdc, git管理)
3. Legacy .cursorrules (非推奨だが動作)

特徴:
- .mdcファイルにfrontmatter（description, globs）を記述
- globsでファイルパターンに応じて自動適用（例: *.tsx → React rules）
- 「関連性に基づく自動選択」= Claudeの探索型に近い
- Agent-requested rules: AIが自分で必要なルールを選ぶモード
- IDE統合なので、開いているファイルのコンテキストが自動注入
```

---

## 設計思想の分類

### 軸1: 静的 vs 動的

| 静的（起動時固定） | 動的（セッション中変化） |
|------------------|----------------------|
| **Codex CLI** | **Claude Code** |
| 1回構築、以後不変 | オンデマンドロード、Auto memory |
| | **Gemini CLI** |
| | /memory refresh, サブディレクトリスキャン |
| | **Cursor** |
| | Agent-requested rules |

### 軸2: 単一エントリ vs 分散エントリ

| 単一エントリポイント | 分散エントリポイント |
|-------------------|-------------------|
| **Codex CLI** | **Claude Code** (6層) |
| AGENTS.md → 32KB上限 | 複数CLAUDE.md + rules + auto memory |
| | **Gemini CLI** (双方向+import) |
| | **Cursor** (ルールファイル群) |

### 軸3: 暗黙的探索 vs 明示的参照

| 暗黙的探索（自発的発見） | 明示的参照のみ |
|----------------------|-------------|
| **Claude Code** (子dir自動ロード) | **Codex CLI** |
| **Gemini CLI** (サブdir下方向スキャン) | |
| **Cursor** (glob+AI選択) | |

---

## 核心的発見

**Codex CLIだけが「静的・単一エントリ・明示的参照のみ」の設計。**

他の3つ（Claude Code, Gemini CLI, Cursor）は全て動的・分散・暗黙的探索を何らかの形で実装している。

これは偶然ではなく、設計思想の違い：
- **Codex**: SWEベンチ最適化。タスクを最短経路で解くためにコンテキストを絞る
- **Claude/Gemini/Cursor**: 開発者体験最適化。文脈を広く拾ってrelevantな情報を見つける

### ユーザー体験への影響

この設計差が「Claude好き vs Codex好き」のユーザー分岐を生む構造的要因：
- 文脈を自動で拾ってほしい人 → Claude/Gemini/Cursor
- 指示したことだけ高速にやってほしい人 → Codex
- 両方必要な人 → タスク特性に応じた使い分け（本研究の提案）
