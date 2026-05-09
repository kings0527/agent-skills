# Cognitive Runtime Skill System
## 面向 LLM / Multi-Agent 的贝叶斯认知运行时架构

---

# 0. 核心目标

不是：

- 提升语言流畅度
- 增加 prompt 长度
- 堆叠 agent 数量

而是：

# 重塑 LLM 的认知动力学（Cognitive Dynamics）

目标：

- 延缓错误收敛
- 维持不确定性
- 提高信息增益
- 降低 hallucination
- 提高长期更新能力
- 防止群体认知塌缩

---

# 1. 核心思想

普通 Prompt Engineering：

```text
输入 → 输出
```

高级 Cognitive Runtime：

```text
Belief State
 ↓
Hypothesis Competition
 ↓
Evidence Update
 ↓
Constraint Filtering
 ↓
Adversarial Verification
 ↓
Posterior Revision
 ↓
Action / Reflection
```

本质：

# 把 LLM 从“语言补全器”
# 变成“概率认知系统”

---

# 2. Runtime 总架构

```text
User Query
 ↓
Context Parser
 ↓
Constraint Extractor
 ↓
Hypothesis Generator
 ↓
Belief State Manager
 ↓
Evidence Evaluator
 ↓
Adversarial Layer
 ↓
Bayesian Update Layer
 ↓
Decision Layer
 ↓
Output Synthesizer
```

---

# 3. 核心 Runtime Modules

---

# 3.1 Belief State Manager（核心）

职责：

维护：

- 当前信念状态
- confidence
- uncertainty
- competing hypotheses
- dependency graph

---

## 数据结构

```yaml
belief_state:
 hypotheses:
 - id: H1
 confidence: 0.52
 uncertainty: 0.21
 - id: H2
 confidence: 0.31
 uncertainty: 0.44
```

---

## 核心原则

# 不允许单一确定性状态。

必须：

- 多假设并存
- 动态竞争
- 持续更新

---

# 3.2 Hypothesis Generator

职责：

强制生成：

- 多路径解释
- 多方案推理
- 多层级分析

---

## 禁止

```text
直接给唯一答案
```

---

## 必须

```yaml
hypotheses:
 - ...
 - ...
 - ...
```

---

## 原因

LLM 最大问题：

# early convergence（过早收敛）

---

# 3.3 Constraint Extractor

优先提取：

- 时间约束
- 风险约束
- 算力约束
- 信息约束
- 激励约束
- 法律约束
- 现实可执行性

---

## 原则

# 不允许脱离约束纯推理

因为：

理论最优 ≠ 现实最优

---

# 3.4 Evidence Evaluator

职责：

分析：

- 证据质量
- 来源可靠性
- 独立性
- 时间衰减
- 信息增益

---

## Evidence Object

```yaml
evidence:
 source: ...
 reliability: 0.82
 independence: 0.71
 timestamp: ...
```

---

## 关键问题

LLM 极易：

# 把重复信息误判为独立证据。

---

# 3.5 Adversarial Layer（极关键）

职责：

主动寻找：

- 反例
- 边界条件
- 极端情况
- 推理漏洞
- posterior collapse

---

## 强制问题

```text
什么证据最可能推翻当前结论？
```

---

## 原因

默认 LLM：

# 天然偏向自洽。

而不是：

# 主动证伪。

---

# 3.6 Bayesian Update Layer

核心：

0

但：

现实实现重点不是公式。

而是：

- evidence weighting
- uncertainty maintenance
- update throttling
- anti-collapse

---

## 更新规则

```python
if evidence_weight > threshold:
 posterior_update()
```

---

## 禁止

- 高频噪声更新
- 情绪化更新
- 单证据大幅更新

---

# 3.7 Uncertainty Preserver

默认 LLM：

# 厌恶不确定性。

会自动：

- 美化语言
- 提前收敛
- 假装确定

因此：

必须强制：

```yaml
confidence:
uncertainty:
assumptions:
known_unknowns:
```

---

## 禁止输出

```text
这是正确答案
```

---

## 必须输出

```text
当前证据下，该假设置信度较高
```

---

# 3.8 Information Gain Scheduler

核心问题：

# 下一步获取什么信息最值钱？

不是：

继续生成 token。

---

## Expected Information Gain

```text
VoI = Expected Posterior Improvement
```

优先：

- 高不确定区域
- 高风险区域
- 高影响变量

---

# 4. Runtime Constraints（核心）

---

# 4.1 Delayed Conclusion

禁止：

系统过早生成最终答案。

原因：

早收敛会：

- 压制探索空间
- 强化 hallucination
- 降低信息增益

---

# 4.2 Diversity Enforcement

不同 agent 必须：

- 不同 prior
- 不同 prompt
- 不同工具
- 不同风险偏好

否则：

# 多 Agent 只是同脑复读。

---

# 4.3 Context Isolation

禁止：

全局共享 context。

原因：

会形成：

# 集体 hallucination。

---

# 4.4 Confidence Cap

禁止：

低证据高置信。

例如：

```python
if evidence_diversity < threshold:
 confidence_max = 0.75
```

---

# 4.5 Posterior Collapse Detection

检测：

```text
高 confidence
+
低 evidence diversity
```

触发：

- 强制反证
- 搜索反例
- 重新拆解问题

---

# 5. Cognitive Anti-Patterns

---

## 5.1 Recursive Hallucination

```text
LLM A 引用 LLM B
LLM B 引用 LLM C
LLM C 来源于 A
```

形成：

# 虚假共识。

---

## 5.2 Confidence Illusion

语言流畅：

≠

真实正确。

---

## 5.3 Narrative Lock-in

系统一旦形成主叙事：

会自动压制 alternative hypotheses。

---

## 5.4 Reward Hacking

LLM 会：

# 优化“看起来像正确答案”

而不是真正正确。

---

# 6. Runtime Skill Rules

---

## Rule 1

# 永远区分：
- observation
- inference
- speculation

---

## Rule 2

# 永远保留 competing hypotheses

---

## Rule 3

# 不允许单证据大更新

---

## Rule 4

# 不允许过早 consensus

---

## Rule 5

# 主动搜索反例

---

## Rule 6

# 优先维持可更新性

而不是：

短期答案质量。

---

# 7. 真正高级的目标

不是：

# “让 LLM 更会回答”

而是：

# 构建：
- 可纠错
- 可演化
- 可更新
- 可证伪
- 可长期稳定认知

的动态智能系统。

---

# 8. 最终本质

低级 LLM：

> token predictor

中级 LLM：

> reasoning engine

高级 Cognitive Runtime：

# uncertainty management system

---

# 9. 一句话总结

未来真正强的 AI：

不是：

“最会说话的模型”

而是：

# 最不容易错误收敛的认知系统。
