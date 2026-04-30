---
name: qinghuan-lp-agent-skills
description: Repository-level routing index for the qinghuan-lp-agent-skills collection. Use when deciding which bundled skill to activate across this repo. Route complex general decisions to FOUDF, engineering and architecture analysis to DevTrace, and reverse engineering, malware, obfuscation, anti-debugging, protocol recovery, or high-noise binary analysis to re-metastrategy-cognitive.
---

# Agent Skills Index

这是仓库级入口索引，用于在多个 skills 之间做快速路由。

## Routing Rules

- 遇到**通用复杂决策**、策略判断、关系分析、约束权衡、博弈分析时，调用 **FOUDF**
- 遇到**工程分析**、架构评估、重构取舍、技术选型、复杂系统依赖分析时，调用 **DevTrace**
- 遇到**逆向工程**、二进制分析、恶意代码分析、混淆/反调试、协议恢复、漏洞面推理，或目标信息**噪声很高、需要注意力控制与去噪**时，调用 **re-metastrategy-cognitive**

## Quick Map

| 场景 | 调用 skill |
| --- | --- |
| 复杂局势判断、策略选择 | `FOUDF` |
| 技术系统理解、架构分析 | `DevTrace` |
| 逆向分析、去噪、前瞻观测 | `re-metastrategy-cognitive` |

## Minimal Guidance

优先做**正确路由**，再进入对应 skill 的详细规则。

如果问题横跨多个领域：
- 先用 `FOUDF` 做全局结构化判断
- 再进入 `DevTrace` 或 `re-metastrategy-cognitive` 做领域内深挖
