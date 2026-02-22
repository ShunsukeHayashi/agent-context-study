# Agent Context Study

**Comparative study of context understanding models in AI coding agents**

## Overview

An experimental investigation into how major AI coding agents — Claude Code, OpenAI Codex CLI, Gemini CLI, and Cursor — understand and utilize project context. Through controlled experiments with identical codebases and prompts, we reveal fundamental architectural differences that explain why developers prefer different agents for different tasks.

## Key Findings

### 1. Context Discovery Model (Experiment 02)
> Claude Code autonomously discovers and reads documentation files. Codex only reads files explicitly mentioned in prompts.

- Claude Code: Read `docs/overview.md` without being told → traced bug info back to documentation source
- Codex: Recognized file existed but did not read it → found bugs through direct code analysis only

### 2. Speed vs Depth Trade-off (Experiment 03)
> Codex is 1.7x faster on linear CLI tasks. Context-integration tasks are roughly equal.

| Task Type | Claude Code | Codex | Winner |
|-----------|------------|-------|--------|
| CLI-linear (pytest fix) | 42.3s | **24.4s** | Codex (1.7x) |
| Context-integration (ADR review) | **41.4s** | 45.2s | ~Equal |

### 3. Personality Persistence (Experiment 05)
> Claude Code and Gemini CLI maintain persona through heavy technical tasks. Codex persona collapses under load.

| Agent | Persona Maintenance | Persona in Code |
|-------|-------------------|-----------------|
| Claude Code | ⭐⭐⭐⭐⭐ Full | ❌ Standard |
| Codex | ⭐⭐ Partial (collapsed) | ❌ Standard |
| Gemini CLI | ⭐⭐⭐⭐⭐ Full | ✅ **In error messages** |

### 4. Content Creation (Experiment 4C-1)
> Claude Code reflects author voice/style. Codex produces well-structured but voice-neutral content.

- Claude: Used casual first-person ("僕"), ended with reader question — matched author profile
- Codex: Used formal first-person ("私"), conclusion-first structure — clean but less personal

## Architecture Comparison

| Feature | Claude Code | Codex CLI | Gemini CLI | Cursor |
|---------|------------|-----------|------------|--------|
| Context files | CLAUDE.md | AGENTS.md | GEMINI.md | .cursor/rules/*.mdc |
| Loading | Hierarchical + on-demand | **Single pass, static** | Bidirectional scan + import | Glob-match + AI-select |
| Size limit | Effectively none | **32KB hard cap** | None documented | Per-rule |
| Subdirectory discovery | ✅ On-demand | ❌ | ✅ Scans below CWD | ✅ Glob patterns |
| Dynamic reload | ✅ During session | ❌ Startup only | ✅ /memory refresh | ✅ Agent-requested |
| File imports | ❌ | ❌ | ✅ @file.md syntax | ❌ |
| OSS | ❌ | ✅ | ✅ | ❌ |

**Key insight: Codex CLI is the only agent with a static, single-entry, explicit-reference-only context model.** All other agents implement some form of dynamic, distributed, implicit discovery.

## Evidence Base

All hypotheses are grounded in official documentation:
- Claude Code: [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) — 6-layer hierarchical memory
- Codex CLI: [developers.openai.com/codex/guides/agents-md/](https://developers.openai.com/codex/guides/agents-md/) — Single chain with 32KB cap
- Gemini CLI: [google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html](https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html) — Bidirectional scan + imports
- External benchmarks: Terminal-Bench 2.0 (Codex 75.1% vs Claude 65.4%), OSWorld (Claude 72.7% vs Codex 64.7%)

## Repository Structure

```
agent-context-study/
├── README.md                          # Japanese overview
├── README-en.md                       # English overview (this file)
├── hypotheses.md                      # Hypotheses with predictions
├── experiments/
│   ├── 02-implicit-bug-discovery/     # Context chain hypothesis test
│   ├── 03-speed-vs-context/           # Speed vs depth comparison
│   │   ├── 3a-cli-linear/            # CLI-linear task (Codex advantage)
│   │   └── 3b-context-integration/    # Context-integration task
│   ├── 04-task-taxonomy/              # Task classification experiments
│   │   └── 4c1-blog-draft/           # Content creation comparison
│   └── 05-personality-persistence/    # 3-agent persona test
└── analysis/
    └── architecture-comparison.md     # 4-agent architecture analysis
```

## Implications for Agent Design

1. **For speed-critical linear tasks**: Use Codex — it's objectively faster
2. **For context-heavy exploration**: Use Claude Code — it discovers relevant files autonomously
3. **For personality-rich applications**: Use Claude Code or Gemini CLI — persona survives technical load
4. **For Codex with context**: Explicitly list all reference files in prompts — it reads what you tell it
5. **For multi-agent orchestration**: Use Claude as orchestrator (context-aware routing) + Codex as executor (fast patches)

## Author

- Hayashi Shunsuke — Prompt Engineer
- GitHub: [@ShunsukeHayashi](https://github.com/ShunsukeHayashi)
- Tools: OpenClaw (multi-agent orchestration platform)

## License

MIT
