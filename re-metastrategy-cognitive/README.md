# re-metastrategy-cognitive

A reverse engineering meta-cognitive skill focused on **attention management**, **task-mode routing**, **object typing**, **hypothesis branching**, **mental model rotation**, and **convergence control**.

It is intentionally **tool-agnostic**. It does not tell the agent which RE tool to use. It tells the agent **how to think** when doing reverse engineering.

## What changed in this version

This revised version upgrades the skill from a strict abstraction-and-trigger protocol into a fuller **reverse-engineering cognitive controller**.

### Key improvements

- Added **Task Mode Router**
  - classify
  - localize
  - explain
  - recover
  - bypass
  - compare
  - validate
  - attribute

- Split abstraction into two axes
  - **Mechanism Abstraction**
  - **Business Abstraction**

- Added **Object Typing Protocol**
  - business logic
  - dispatcher
  - VM handler
  - decoder/decryptor
  - environment probe
  - anti-debug gate
  - bridge/glue
  - and more

- Added **Attention Budget Protocol**
  - high / medium / low
  - plus a **parking lot** mechanism for low-value or currently irrelevant complexity

- Added **Hypothesis Pool Protocol**
  - multiple candidate explanations
  - discriminators
  - falsifiers
  - reduced single-hypothesis lock-in

- Added explicit **Mental Model Library**
  - state machine
  - transform pipeline
  - trust chain
  - boundary crossing
  - temporal delta
  - deception surface
  - and more

- Added explicit **Deception Check**
  - to resist control-flow theater, naming traps, and pseudo-complexity

- Replaced one-size-fits-all convergence with **task-mode-based termination**

## Why this matters

Many RE agents are good at reading code but weak at:

- knowing where attention should go
- managing ambiguity without collapsing too early
- switching between cognitive models, not just viewpoints
- separating mechanism understanding from business understanding
- avoiding attractive but low-value complexity

This version is designed to improve those failure modes directly.

## Files

- `skills/re-metastrategy-cognitive/SKILL.md`

## Suggested use cases

Use this skill when the agent needs meta-level control during:

- binary reverse engineering
- malware analysis
- VM / packer analysis
- anti-debugging reasoning
- obfuscation deconstruction
- protocol or format recovery
- exploit surface reasoning
- mechanism vs business intent separation

## Notes

- This is a **thinking framework**, not a tool driver.
- It is especially useful when an agent is stuck, drifting, overfitting to one narrative, or spending too much attention on noise.
