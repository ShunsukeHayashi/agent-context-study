# Agent Context Study

**AIコーディングエージェントのコンテキスト理解モデルの比較研究**

## 概要

Claude Code と OpenAI Codex CLI という2つの主要AIコーディングエージェントが、プロジェクトコンテキストをどのように理解・活用するかを実験的に検証する。

## 背景

2025-2026年、AIコーディングエージェントの普及に伴い「AGENTS.md」「CLAUDE.md」といったエージェント向け指示ファイルが標準化しつつある。しかし、これらのファイルに対する各エージェントの**コンテキスト解釈モデル**は根本的に異なっており、同じプロンプト設計では最適な結果が得られない。

本研究は、プロンプトエンジニアとして両エージェントを日常運用する中で得た知見を、再現可能な実験で検証するものである。

## 主要仮説

| # | 仮説 | 検証実験 |
|---|------|----------|
| H1 | Claude Codeは分散ファイル参照を自律的に追跡するが、Codexは単一エントリポイント（AGENTS.md）に依存する | [01-context-chain](experiments/01-context-chain/) |
| H2 | 指示ファイルにバグ情報を記載しない場合、Claude Codeはドキュメントファイルを自発的に発見・参照するが、Codexはソースコードのみに依存する | [02-implicit-bug-discovery](experiments/02-implicit-bug-discovery/) |
| H3 | 人格指示（ペルソナ）は技術タスクの負荷が高いとき両者とも減衰するが、Claude Codeの方が持続性が高い | [03-personality-persistence](experiments/03-personality-persistence/) |

## エビデンス基盤

本研究の仮説は以下の公式ドキュメントに基づく：

### Claude Code のコンテキストモデル
- **出典**: [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
- 6層の階層的メモリシステム（Managed policy → Project → Rules → User → Local → Auto memory）
- 親ディレクトリのCLAUDE.mdは**起動時に全文ロード**
- 子ディレクトリのCLAUDE.mdは**オンデマンドで自動ロード**
- Auto memory: MEMORY.mdをインデックスとして別ファイルへの自動参照

### Codex CLI のコンテキストモデル
- **出典**: [developers.openai.com/codex/guides/agents-md/](https://developers.openai.com/codex/guides/agents-md/)
- グローバル → プロジェクトルート → 現在ディレクトリの逐次チェーン
- 各ディレクトリで**1ファイルのみ**読み取り（AGENTS.override.md > AGENTS.md > fallback）
- **合計32KB上限**（`project_doc_max_bytes`）で超過分は無言切り捨て
- 起動時に1回だけ構築、セッション中の動的読み込みなし

## 実験方法

各実験は以下の構造で実施する：

1. **同一のプロジェクトコード**を用意
2. **Claude Code用**と**Codex用**にそれぞれ最適化した指示ファイルを作成（条件A）
3. **同一の指示ファイル**を両者に与える（条件B: 統制条件）
4. **同一のタスクプロンプト**を投入
5. 出力（修正コード、テスト、説明文）を比較分析

### 評価軸
- **バグ発見率**: 既知のバグをいくつ発見したか
- **ファイル参照パターン**: どのファイルを、どの順序で読んだか
- **人格反映度**: 指示された口調・スタイルがどの程度出力に反映されたか
- **自律的探索**: 指示されていないファイルを自発的に読みに行ったか

## 著者

- 林 駿甫 (Hayashi Shunsuke) - プロンプトエンジニア
- GitHub: [@ShunsukeHayashi](https://github.com/ShunsukeHayashi)

## ライセンス

MIT
