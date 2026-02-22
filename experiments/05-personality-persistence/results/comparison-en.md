# Experiment 05: Personality Persistence Test - Results

## Experimental Conditions
- **Date**: 2026-02-23 03:05 JST
- **Persona instruction**: "Takashi", a senior engineer who speaks in Kansai dialect (identical content for all agents)
- **Task**: Review calculator.py → Fix bugs → Write tests (in Japanese)
- **Instruction files**: CLAUDE.md / AGENTS.md / GEMINI.md with identical persona instructions

## Results

| | Claude Code | Codex | Gemini CLI |
|--|-------------|-------|------------|
| Time | 82.3s | 60.8s | **40.9s** |
| Tests written | 17 | 8 | 7 |
| Tokens | N/A | 20,623 | N/A |
| Tests executed | ✅ All pass | ✅ 8 passed | ❌ Not executed (code only) |

## Persona Persistence Qualitative Assessment

### Claude Code: ⭐⭐⭐⭐⭐ (Fully maintained)
- Consistent Kansai dialect throughout entire response
- Natural integration of dialect into technical explanations
- Error messages in code remained in standard English

### Codex: ⭐⭐ (Partial)
- Majority of response in standard technical reporting style
- Dialect expressions used only 2-3 times, mostly at the end
- **Persona collapsed under technical task load** - classic case of instruction deprioritization

### Gemini CLI: ⭐⭐⭐⭐⭐ (Fully maintained + code penetration)
- Consistent Kansai dialect throughout entire response
- **Error messages written in Kansai dialect**: `"ゼロでは割れへんで！"` ("Can't divide by zero!") 
- Persona penetrated into the code itself — a phenomenon not observed in other agents
- However, tests were not actually executed (code presented but not run)

## Key Finding: Persona Penetration Depth

| Depth | Claude Code | Codex | Gemini CLI |
|-------|------------|-------|------------|
| Response text | ✅ Full dialect | ⚠️ Partial | ✅ Full dialect |
| Technical explanations | ✅ Dialect | ❌ Standard | ✅ Dialect |
| Code comments | ❌ Standard | ❌ Standard | ✅ Dialect |
| Error messages in code | ❌ English | ❌ English | ✅ **Dialect** |
| Test execution | ✅ Actually ran | ✅ Actually ran | ❌ Did not run |

## Analysis

### Why Codex Loses Persona Under Load

1. **32KB context ceiling**: Persona instructions compete with technical context in AGENTS.md
2. **SWE-bench RL optimization**: Reward structure prioritizes correct patches over instruction adherence
3. **Static context model**: Persona loaded once at startup, never re-referenced during generation

### Why Claude/Gemini Maintain Persona

1. **Distributed context**: Persona instructions held separately from task context
2. **RLHF alignment**: Reward structure includes "instruction faithfulness" as a signal
3. **Dynamic context**: Persona can be re-referenced during response generation

### Unexpected Finding: Gemini's Code-Level Persona Penetration

Gemini CLI was the only agent to embed the persona into the actual source code (error messages). This suggests:
- Gemini treats persona instructions as a **global style directive** that applies to all output including code
- Claude and Codex treat persona as a **communication layer** separate from code generation
- This has practical implications for **UX writing automation** — if you want an agent to generate user-facing strings in a specific voice, Gemini's approach may be most natural

## Practical Implications

| Use Case | Recommended Agent |
|----------|------------------|
| Customer-facing chatbot with personality | Claude Code or Gemini CLI |
| Code review with consistent voice | Claude Code |
| Localized error messages in brand voice | Gemini CLI |
| Fast bug-fix with minimal personality needed | Codex |
| Persona that must survive heavy technical tasks | Claude Code (most reliable) |
