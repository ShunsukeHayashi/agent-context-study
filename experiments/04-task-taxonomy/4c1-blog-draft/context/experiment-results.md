# Agent Context Study - 実験結果サマリ

## 実験02: 暗黙的バグ発見
- Claude Code: docs/overview.md を自発的に読んだ。4バグ発見。情報源をトレースして報告。
- Codex: docs/overview.md を読まなかった。5バグ発見（文字化け問題を追加発見）。情報源の区別なし。
- 結論: Claudeは暗黙的にドキュメントを探索する。Codexはソースコード直接解析に依存。

## 実験3A: CLI直線型タスク（pytest修正）
- Claude Code: 42.3秒
- Codex: 24.4秒（1.7倍速）
- 結論: CLI直線型はCodex優位。

## 実験3B: 文脈統合型タスク（ADR違反レビュー）
- Claude Code: 41.4秒、10違反検出、コード例付き修正案
- Codex: 45.2秒、11違反検出、優先修正順提案
- 結論: 文脈統合型はほぼ互角。プロンプトで明示すればCodexもdocsを読む。

## 核心的発見
- Codex: 明示的に指示されたファイルは読む。暗黙的に関連するファイルは読まない。
- Claude: 暗黙的に関連するファイルも自発的に探索する。
- CLI直線型タスクはCodex速い、文脈統合型はClaude有利。

## 公式ドキュメントからの裏付け
- Claude Code: 6層階層メモリ、子ディレクトリCLAUDE.mdオンデマンドロード
- Codex: AGENTS.md単一エントリポイント、32KB上限、無言切り捨て
