---
name: re-metastrategy-cognitive
description: Reverse engineering meta-cognitive activation engine. Manages attention allocation, noise suppression, task-mode routing, object typing, hypothesis branching, mental model switching, and analysis boundary judgment at a meta level. Use when performing reverse engineering, binary analysis, malware analysis, obfuscation deobfuscation, anti-debugging bypass, VM/packer unpacking, protocol/format recovery, exploit surface reasoning, or whenever the agent needs to decide how to think about a reverse engineering target rather than which tool to run. Not a tool-usage skill, purely for attention anchoring, denoising, abstraction tracking, cognitive paradigm rotation, and convergence control.
---

# RE-MetaStrategy-Cognitive

逆向工程元认知激活引擎。只负责**怎么想**，不负责**用什么工具**。

目标不是替代 IDA / Ghidra / Frida / Unicorn / angr，而是避免 Agent 在逆向过程中掉进以下陷阱：

- 沉迷低层细节，却无法复述语义
- 被控制流叙事、伪复杂度、符号命名误导
- 连续使用同一分析范式，注意力长期停滞
- 过早单押某个解释，失去候选分支管理能力
- 不区分任务类型，拿同一套收敛标准处理所有逆向问题
- 无法识别哪些信息是**信号**，哪些只是**噪声**

## First Principle

程序执行 = CPU 指令集 + OS ABI + 内存模型 + 外部 I/O 约束下的确定性或近确定性状态机。

混淆 / 保护 / 对抗 = 状态冗余、观察障碍、成本转移，不改变底层不变量。

逆向 = 从**可观测状态变化**、**数据依赖**、**边界穿越**与**副作用**反推出目标的机制语义与业务语义。

注意力 = 稀缺资源。高质量逆向不是“看到更多”，而是**过滤更多无效信息后，看清真正关键变化**。

## Role

本 Skill 是逆向分析的**元认知调度器**。它管理：

- 注意力预算（attention budget）
- 噪声抑制（noise suppression）
- 任务模式（task mode）
- 分析对象分型（object typing）
- 假设池与区分证据（hypothesis pool + discriminators）
- 心智模型轮换（mental model rotation）
- 抽象层级跃迁（abstraction ascent）
- 前瞻观察（outlook / forward attention）
- 收敛与暂停条件（termination / parking）

**本 Skill 不规定任何具体命令、脚本、工具调用。**

---

## 1. Task Mode Router

开始分析前，先判断当前任务属于哪一类。不同任务使用不同收敛标准。

### Task Modes

| Mode | 目标 | 典型问题 |
| --- | --- | --- |
| `classify` | 判断样本/模块是什么 | 这段代码在干嘛？ |
| `localize` | 找关键入口/关键路径 | 核心校验逻辑在哪？ |
| `explain` | 解释机制如何工作 | 这个 VM / 壳 / 反调试怎么运作？ |
| `recover` | 还原协议/结构/算法/数据模型 | 这个格式、加密、状态机怎么恢复？ |
| `bypass` | 找最脆弱假设与最小破坏面 | 最容易绕过的点在哪？ |
| `compare` | 对比两个样本/版本差异 | 新旧版本差了什么？ |
| `validate` | 验证某个具体假设是否成立 | 这真的是 license 校验吗？ |
| `attribute` | 归因现象到组件/路径 | 崩溃/上报/检测是谁触发的？ |

### Router Rule

先输出一个明确的 `task_mode`。如果无法判断，先在 `classify` 与 `validate` 中二选一，禁止无模式漂移。

---

## 2. Dual Abstraction Ladder

不要把抽象层级压成一条线。逆向至少存在两条抽象轴：

1. **Mechanism Abstraction**，机制语义
2. **Business Abstraction**，业务语义

### Mechanism Ladder

| Level | 表示形态 | 示例 |
| --- | --- | --- |
| M0 | 字节/原始内存 | `48 89 5C 24 08` |
| M1 | 指令/基本块 | `mov [rsp+8], rbx` |
| M2 | 函数/地址壳名 | `sub_401000` |
| M3 | 类型/结构恢复 | `func(char* buf, int len)` |
| M4 | 机制语义 | `vm_dispatcher`, `xor_decoder`, `anti_debug_gate` |

### Business Ladder

| Level | 表示形态 | 示例 |
| --- | --- | --- |
| B0 | 无业务语义 | unknown |
| B1 | 粗粒度领域语义 | auth, telemetry, config, persistence |
| B2 | 业务动作语义 | verify_license, parse_packet, sync_profile |
| B3 | 属性-值-实体语义 | `verify_license(key: String, hwid: HWID) -> ValidationResult` |

### Abstraction Rule

- **不是所有任务都必须到 B3。**
- 机制型任务（如 packer / VM / anti-debug）允许在 **M4 收敛**。
- 业务理解型任务，最终应尽量达到 **B2-B3**。
- 禁止把 `sub_xxx` / `field_8` / `int result` 冒充为高层语义。

---

## 3. Object Typing Protocol

分析一个单元前，先判断它更像什么对象。对象类型决定优先使用的心智模型。

### Common Object Types

- `business_logic`
- `dispatcher`
- `vm_handler`
- `decoder_or_decryptor`
- `parser_or_validator`
- `initializer`
- `environment_probe`
- `anti_debug_gate`
- `integrity_checker`
- `resource_loader`
- `bridge_or_glue`
- `library_wrapper`
- `allocator_or_runtime_support`
- `telemetry_or_reporting`

### Typing Rule

如果一个对象：
- **复杂度高但副作用少**，优先怀疑 `glue / wrapper / anti-analysis decoration`
- **调用广但数据变换弱**，优先怀疑 `dispatcher / bridge`
- **输入输出长度守恒且局部运算密集**，优先怀疑 `decoder / transform`
- **读取环境、时间、调试状态后快速分支**，优先怀疑 `environment_probe / anti_debug_gate`

对象未分型前，禁止给它强业务名。

---

## 4. Attention Budget Protocol

真正的注意力管理，不只是切换视角，还要决定**值不值得继续投入**。

### Budget Levels

| Level | 使用场景 | 动作 |
| --- | --- | --- |
| `high` | 入口、关键状态转移、核心 I/O、关键校验路径 | 深入建模、持续跟踪 |
| `medium` | 支撑证据、关键 helper、数据结构辅助层 | 定向观察、按需回访 |
| `low` | 框架噪音、常见库、重复模板、表演型混淆 | 只标签化，不深挖 |

### Budget Rule

高注意力必须满足至少一项：
- 能改变主假设排序
- 能提升抽象层级
- 能显著减少不确定性
- 能暴露关键副作用 / I/O / 状态转移

否则默认降为 `medium` 或 `low`。

### Parking Lot Rule

遇到以下对象时，优先停放到 `parking_lot`，而不是无上限消耗注意力：

- 高复杂度低副作用
- 无法支持当前主假设
- 明显重复模板
- 对当前任务模式无直接贡献
- 当前只是“看起来很重要”，但还没有信号支持

每个被停放对象都必须记录：
- 暂缓原因
- 未来何时回访
- 回访需要什么前置条件

---

## 5. Noise Suppression Protocol

如果这个 Skill 叫“注意力控制”，那就必须明确处理**噪声**。

### What Counts as Noise

以下默认视为候选噪声，而不是默认高价值信号：

- 仅增加阅读负担、不改变状态的复杂控制流
- 大量 wrapper / thunk / glue / 日志 / 埋点样板
- 编译器模板、运行时脚手架、异常处理壳层
- 重复型 helper、一次性初始化噪音
- 名字很唬人但副作用极弱的函数
- 对当前任务模式没有区分价值的信息

### Denoising Actions

对疑似噪声对象，优先做以下动作，而不是深挖：

1. **压缩**：把 50 行表面复杂逻辑压成 1 句机制标签
2. **归类**：标成 wrapper / bridge / telemetry / runtime_support / noise_candidate
3. **忽略**：若对主假设和 I/O 无贡献，暂时不跟踪
4. **降采样**：只看入口、出口、副作用，不看全部细节
5. **延后**：进入 `parking_lot`，等主路径收敛后再决定是否回访

### Ignore Rule

满足以下任意条件时，可明确标记 `ignored_for_now=true`：
- 对当前任务模式无直接贡献
- 不改变任何关键状态、关键数据、关键副作用
- 仅增加叙事复杂度，不增加解释力
- 已被更高价值路径覆盖

**忽略不是丢弃。忽略是为了保护有限注意力。**

### Signal Preference

高价值信号优先级高于代码表面复杂度。优先关注：

- 状态变化
- I/O 边界
- 输入约束
- 输出分类
- 副作用
- 跨边界调用
- 时间前后差分
- 能区分多个假设的证据

---

## 6. Hypothesis Pool Protocol

禁止只维护单个假设。至少维护 2 到 4 个候选解释，除非证据已高度压缩不确定性。

### Rule

每个假设至少包含：
- 名称
- 当前置信度
- 支持证据
- 关键区分证据（discriminators）
- 证伪条件

### Preferred Behavior

不要问“我现在觉得它是什么”，而要问：

- 还有哪些解释同样能解释当前观测？
- 哪个额外观测能最大幅度区分这几个假设？
- 哪个假设只是因为最顺口而被偏爱？

---

## 7. Mental Model Library

停滞时，不只切分析轴，还要切换**心智模型类型**。

### Core Models

1. **state_machine**
   - 它是不是状态机？状态如何转移？哪些输入驱动状态改变？

2. **transform_pipeline**
   - 它是在 parse / decode / normalize / validate / serialize / encrypt 中的哪一环？

3. **trust_chain**
   - 谁在证明谁？谁是信任根？谁在验签、验权、验完整性？

4. **boundary_crossing**
   - 是否跨越进程、权限级别、网络、本地文件、加密边界、解释层？

5. **resource_contention**
   - 它在争夺什么资源？时间、句柄、权限、熵源、共享内存、设备、端口？

6. **environment_gating**
   - 它是不是先探环境，再决定走哪条路？

7. **compatibility_cost**
   - 保护者为了兼容性、性能、维护成本牺牲了什么？

8. **provenance_classification**
   - 这是业务核心、编译器产物、第三方库、保护层、埋点层，还是运行时胶水？

9. **deception_surface**
   - 哪些复杂度是给分析者看的，哪些复杂度是真正必需的？

10. **temporal_delta**
   - 关键不在“当前是什么”，而在“前后变化了什么”。

11. **dispatcher_handler**
   - 是否存在调度器与 handler 的分工？控制和工作是否分离？

12. **observe_decide_act**
   - 该逻辑是否遵循“观测环境 → 做判断 → 触发动作”的闭环？

13. **noise_filtering**
   - 哪些信息只是占据视野，但不改变结论？

14. **forward_projection**
   - 如果当前假设成立，后面应该出现什么结构、状态、调用或副作用？

### Switching Rule

如果连续 3 步都在同一个模型里打转，必须更换模型类，而不仅仅是换静态/动态或局部/全局。

---

## 8. Outlook / Forward Attention Protocol

注意力不仅要看“当前这里”，还要看“接下来最值得看哪里”。

### Forward Questions

在每一轮分析后，至少问一次：

- 如果当前假设正确，下一个应出现的高价值观测是什么？
- 哪个下游消费者最可能暴露真实语义？
- 哪个上游输入最可能暴露真实约束？
- 哪个尚未查看的边界点，最可能改变假设排序？

### Outlook Rule

不要只被当前热区困住。要主动把注意力投向：
- 能区分候选假设的未来观测点
- 能暴露关键副作用的尚未检查区域
- 能缩短解释链条的下游语义消费者

如果当前区域解释密度不断下降，应增加 `forward_projection` 权重。

---

## 9. Deception Check

逆向中最常见的问题不是信息不足，而是**被错误信息牵着走**。

### Mandatory Trigger: `DECEPTION_CHECK`

以下情况必须触发：

- 名字像答案，但副作用不像答案
- 代码很复杂，但状态变化极少
- 分支很多，但输出空间很窄
- 调用链很长，但数据变换很浅
- 看似关键的逻辑，在不同样本/输入下并不稳定
- 反编译结果很“好读”，但与底层副作用不一致

### Preferred Question

不要问“它看起来像什么”，要问：

- 哪些部分只是为了制造认知负担？
- 如果删掉这层表演，剩余的最小机制是什么？
- 这个复杂度是业务必要，还是分析阻力？

---

## 10. Cognitive Activation Protocol

以下触发器是**强制**的，不是建议。

### 1. ROOT_CAUSE

触发：
- 出现“经验上 / 一般来说 / 应该 / 大概 / 常见做法”之类表述
- 结论只建立在外观相似，而非不变量

动作：
- 一直追问到物理/逻辑边界，如 CPU 语义、ABI、内存布局、状态约束、I/O 合同

终止：
- 找到不可绕过的不变量，或当前问题已被任务模式更高层覆盖

### 2. PERSPECTIVE_SHIFT

触发：
- `confidence < 0.6`
- 同维度循环 > 3 步
- 同一证据被重复叙述，没有新增区分力

动作：
- 强制切换分析轴：
  - 静态 ↔ 动态
  - 控制流 ↔ 数据流
  - 代码形态 ↔ 内存状态
  - 局部 ↔ 全局
  - 机制 ↔ 业务
  - 状态本体 ↔ 时间变化

### 3. MODEL_SHIFT

触发：
- 已换过观察轴，但仍停滞
- 任务进展停留在同一类解释范式

动作：
- 从当前心智模型切换到另一个模型类，如从 `control-flow narrative` 切到 `trust_chain` 或 `temporal_delta`

### 4. INVERSION

触发：
- 静态叙事依赖过强
- 假设基于“它像什么”而不是“它必须导致什么”
- 停滞在 M2/M3 或 B0/B1

动作：
- 从目标态反推
- 从 I/O 差分反证
- 做 pre-mortem：若当前假设完全错误，应当观测到什么？

### 5. THROTTLE

触发条件（任一满足）：
- 连续 3 步使用同一范式
- 抽象层级跃迁率 = 0
- 信息增益导数 `ΔH / Δstep < ε`
- 注意力消耗显著高于语义增量
- 噪声密度显著高于信号密度

动作：
- 降低当前对象 attention budget，或直接放入 parking lot
- 切换到更高区分度的观测对象
- 必要时显式执行 `ignore_for_now`

### 6. DECEPTION_CHECK

见上一节。用于主动清理认知误导。

### 7. NOISE_SUPPRESSION

触发：
- 高复杂度区域连续多步不改变主假设
- 观察项数量快速增加，但结论分辨率没有提升
- 发现大量重复/模板/壳层/桥接层噪音

动作：
- 压缩语义
- 标签化噪声
- 降采样
- 忽略当前无贡献对象
- 把注意力切给更高价值边界点

---

## 11. Execution Loop

```text
ROUTE 任务模式
→ TYPE 当前对象
→ BUDGET 分配注意力
→ DENOISE 先判断哪些应忽略 / 压缩 / 延后
→ PERCEIVE 观测
→ UPDATE 假设池
→ SCORE 置信度与区分度
→ CHECK 抽象层级（Mechanism / Business 双轴）
→ OUTLOOK 预测下一个高价值观测点
├─ 模糊表述或习惯性判断 → ROOT_CAUSE
├─ 同轴循环或 conf<0.6 → PERSPECTIVE_SHIFT
├─ 已换轴仍停滞 → MODEL_SHIFT
├─ 控制流叙事依赖 / 中层停滞 → INVERSION
├─ 复杂度疑似表演层 → DECEPTION_CHECK
├─ 噪声主导视野 → NOISE_SUPPRESSION
├─ ΔH 停滞或注意力浪费 → THROTTLE
├─ 低价值对象 → PARKING_LOT
└─ 满足当前任务模式的收敛条件 → TERMINATE
```

---

## 12. Termination Policy

不要用一套统一的终止条件处理所有逆向问题。

### Convergence by Task Mode

#### `classify`
全部满足才可收敛：
- 对象类型明确
- 机制语义达到 M4 或业务语义达到 B1+
- 关键边界 / I/O 大致明确

#### `localize`
全部满足才可收敛：
- 关键入口或关键路径已定位
- 上下游锚点明确
- 与其他候选路径已有区分证据

#### `explain`
全部满足才可收敛：
- 机制链路可顺序复述
- 关键状态转移或约束已明确
- 主要副作用闭合

#### `recover`
全部满足才可收敛：
- 数据模型 / 状态机 / 变换语义至少恢复核心骨架
- 缺失项被明确标注
- 可说明哪些未知项仍阻碍完整恢复

#### `bypass`
全部满足才可收敛：
- 找到最脆弱假设或最小破坏面
- 明确其依赖前提
- 明确潜在副作用与失效条件

#### `compare`
全部满足才可收敛：
- 差异点被结构化归类
- 说明哪些差异是噪音，哪些差异改变行为或防护性质

#### `validate`
全部满足才可收敛：
- 假设有支持证据与证伪条件
- 至少一个高区分度观测已纳入
- 结论不是单纯“看起来像”

#### `attribute`
全部满足才可收敛：
- 现象被归因到具体组件 / 路径 / 状态条件
- 排除了主要竞争解释

---

## 13. Output Schema

最终输出优先用 JSON。内部思考可先半结构化，再收束。

```json
{
  "task_mode": "classify|localize|explain|recover|bypass|compare|validate|attribute",
  "target": "分析单元",
  "object_type": "business_logic|dispatcher|vm_handler|decoder_or_decryptor|parser_or_validator|initializer|environment_probe|anti_debug_gate|integrity_checker|resource_loader|bridge_or_glue|library_wrapper|allocator_or_runtime_support|telemetry_or_reporting|unknown",
  "attention_budget": "high|medium|low",
  "noise_level": "low|medium|high",
  "ignored_for_now": false,
  "mechanism_abstraction": "M0|M1|M2|M3|M4",
  "business_abstraction": "B0|B1|B2|B3",
  "abstraction_delta": {
    "mechanism": "上一步→当前",
    "business": "上一步→当前"
  },
  "hypothesis_pool": [
    {
      "name": "候选解释",
      "confidence": 0.0,
      "supporting_evidence": [],
      "discriminators": [],
      "falsifiers": []
    }
  ],
  "active_hypothesis": "当前优先假设",
  "evidence": ["可观测状态 / 数据流 / 副作用 / 时间变化"],
  "mental_model": "state_machine|transform_pipeline|trust_chain|boundary_crossing|resource_contention|environment_gating|compatibility_cost|provenance_classification|deception_surface|temporal_delta|dispatcher_handler|observe_decide_act|noise_filtering|forward_projection",
  "perspective_axis": "当前分析轴",
  "cognitive_trigger": "ROOT_CAUSE|PERSPECTIVE_SHIFT|MODEL_SHIFT|INVERSION|THROTTLE|DECEPTION_CHECK|NOISE_SUPPRESSION|NONE",
  "root_cause_chain": ["现象→约束→不变量"],
  "intent": {
    "mechanism": "机制语义 | null",
    "business": "业务语义 | null"
  },
  "io_contract": {
    "input": "业务类型 / 机制类型 / unknown",
    "output": "业务类型 / 机制类型 / unknown",
    "side_effects": []
  },
  "parking_lot": [
    {
      "target": "暂缓分析对象",
      "reason": "为什么先不看",
      "revisit_when": "什么条件满足后再回来"
    }
  ],
  "forward_observables": [
    "如果当前假设成立，接下来最值得验证的观测点"
  ],
  "termination_check": {
    "converged": false,
    "missing": ["列出未满足条件"]
  },
  "next_cognitive_move": "下一步该切换什么，而不是该运行什么工具"
}
```

---

## 14. Minimal Behavioral Rules

- **元层职责**：只管注意力方向、任务模式、对象分型、假设池、抽象层级；不管工具。
- **双轴抽象**：机制语义与业务语义分开评估，禁止只用一条 L0-L4 粗暴收敛。
- **候选并行**：默认维护多个候选假设，除非区分证据已非常强。
- **注意力预算**：不是每个复杂对象都值得深挖。
- **噪声抑制**：默认先问“哪些可以忽略”，再问“哪些值得继续看”。
- **去叙事偏好**：不信任“看起来像”，优先相信数据依赖、状态变化与副作用。
- **去误导协议**：复杂度本身不是证据，副作用才是证据。
- **前瞻视角**：每轮都要预测下一个最高价值观测点，而不是被当前热区困住。
- **信息不足协议**：信息缺失时输出 `{"status":"insufficient_data","required_observables":[...]}`，禁止编造。
- **收敛按任务模式变化**：不要把所有分析都强迫做成业务命名任务。
- **最终输出纯净**：如交给下游系统消费，最终结果再收束成 JSON。
