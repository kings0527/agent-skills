# Agent Skills

一套面向 AI Agent 的**高阶认知技能仓库**。这些技能不是简单的工具说明，而是把复杂任务里的**注意力分配、抽象切换、约束分析、噪声抑制、前瞻判断与收敛控制**沉淀成可复用的思维框架。

适合用于：
- 复杂决策
- 工程分析
- 架构评估
- 逆向工程
- 高噪声、高不确定性的复杂问题求解

## 设计理念

这些 skills 关注的不是“怎么调用工具”，而是：

- **怎么看问题**
- **先看哪里**
- **哪些该忽略**
- **何时切换模型**
- **何时停止继续深挖**
- **如何从复杂表象压缩出高价值信号**

换句话说，这个仓库更偏向 **meta-skills / cognitive skills**，帮助 Agent 在复杂上下文中保持清晰，而不是被信息淹没。

## 技能列表

| 技能 | 定位 | 核心关注 | 适用场景 |
|------|------|----------|---------|
| [FOUDF](./FOUDF/) | 通用元认知决策框架 | System / Layer / Probability / Constraint / Game | 跨领域复杂决策、策略分析、关系判断、政策/商业/人生问题 |
| [DevTrace](./DevTrace/) | 工程分析与技术决策框架 | Topology / Abstraction / Entropy / Constraint / Dependency | 架构评估、重构决策、技术选型、复杂工程问题定位 |
| [re-metastrategy-cognitive](./re-metastrategy-cognitive/) | 逆向工程元认知控制器 | Attention Budget / Noise Suppression / Task Mode / Object Typing / Hypothesis Pool / Mental Models / Outlook | 逆向分析、恶意代码分析、混淆/反调试、协议恢复、漏洞面推理 |

## 安装方式

### OpenClaw

将技能复制到你的 `skills` 目录：

```bash
# 安装全部
git clone https://github.com/kings0527/agent-skills.git
cp -r agent-skills/* ~/.openclaw/workspace/skills/
```

或按需单独安装：

```bash
mkdir -p ~/.openclaw/workspace/skills/FOUDF
curl -o ~/.openclaw/workspace/skills/FOUDF/SKILL.md \
  https://raw.githubusercontent.com/kings0527/agent-skills/main/FOUDF/SKILL.md

mkdir -p ~/.openclaw/workspace/skills/DevTrace
curl -o ~/.openclaw/workspace/skills/DevTrace/SKILL.md \
  https://raw.githubusercontent.com/kings0527/agent-skills/main/DevTrace/SKILL.md

mkdir -p ~/.openclaw/workspace/skills/re-metastrategy-cognitive
curl -o ~/.openclaw/workspace/skills/re-metastrategy-cognitive/SKILL.md \
  https://raw.githubusercontent.com/kings0527/agent-skills/main/re-metastrategy-cognitive/SKILL.md
```

### Claude Code / 其他 CLI Agent

将 `SKILL.md` 放入你的项目目录、全局规则目录，或在代理配置中引用：

```bash
curl -O https://raw.githubusercontent.com/kings0527/agent-skills/main/FOUDF/SKILL.md
curl -O https://raw.githubusercontent.com/kings0527/agent-skills/main/DevTrace/SKILL.md
curl -O https://raw.githubusercontent.com/kings0527/agent-skills/main/re-metastrategy-cognitive/SKILL.md
```

### Cursor / Windsurf / 其他 IDE Agent

在项目规则文件中引用：

```markdown
# Cognitive Skill References
- 通用决策: https://raw.githubusercontent.com/kings0527/agent-skills/main/FOUDF/SKILL.md
- 工程分析: https://raw.githubusercontent.com/kings0527/agent-skills/main/DevTrace/SKILL.md
- 逆向元认知: https://raw.githubusercontent.com/kings0527/agent-skills/main/re-metastrategy-cognitive/SKILL.md
```

## 框架对比

| 维度 | FOUDF | DevTrace | RE-MetaStrategy |
|------|-------|----------|-----------------|
| **定位** | 通用元认知决策框架 | 工程分析框架 | 逆向元认知控制器 |
| **适用域** | 任何复杂系统 | 技术/架构系统 | 二进制/恶意代码/保护机制 |
| **主要问题** | 怎么判断复杂局势 | 怎么理解工程系统 | 怎么在高噪声目标中分配注意力 |
| **核心关注** | 系统、分层、概率、约束、博弈 | 拓扑、抽象、熵增、约束、依赖 | 注意力预算、噪声抑制、对象分型、假设池、前瞻观察 |
| **典型输出** | 判断框架、概率推演、约束分析 | 架构图景、风险面、依赖分析 | 机制语义、业务语义、去噪结果、关键观测点 |
| **典型场景** | 选专业、评架构、分析关系、制定政策 | 微服务拆分、重构评估、技术选型、代码审查 | 逆向分析、VM/壳、反调试、协议恢复、绕过面定位 |

## 使用示例

### FOUDF 示例：职业选择

```text
用户：我在纠结要不要跳槽去创业公司

Agent（启用 FOUDF）：
【系统】你当前职业网络 → 家庭期望、社会评价、经济需求
       跳槽会切断稳定收入节点，但接入新机会网络
【分层】"创业公司"标签 → 股权+不确定性 → 实际是赌赛道
【概率】60%公司3年内倒闭，20%持平，20%成功退出
【约束】存款支撑多久？年龄对风险的承受力？
【博弈】创始人的收益函数 vs 你的（他赌的是你的时间）
```

### DevTrace 示例：微服务拆分

```text
用户：我们想把单体拆成微服务

Agent（启用 DevTrace）：
【拓扑】Gateway→Monolith→Payment/Inventory，关键路径是下单-支付-库存
【熵增】跨服务排障、状态机复杂度上升，需要观测性纪律
【约束】DevOps人力、延迟要求、一致性边界
【依赖】Service Mesh、分布式追踪、消息队列

结论：建议但需前置条件，先补链路追踪和幂等策略
```

### re-metastrategy-cognitive 示例：逆向校验逻辑

```text
用户：帮我判断这个样本里的 license 校验核心逻辑在哪里

Agent（启用 re-metastrategy-cognitive）：
- Task Mode: localize
- Object Type: parser_or_validator / anti_debug_gate / business_logic 候选分型
- Attention Budget: 将入口、失败分支、副作用路径设为 high
- Noise Suppression: 把 telemetry wrapper、日志层、运行时模板先压缩并暂时忽略
- Hypothesis Pool:
  1. license_check
  2. environment_gate
  3. telemetry_precheck
- Mental Model: trust_chain + temporal_delta + forward_projection
- 收敛目标：定位关键校验路径，并区分它与环境探针/埋点逻辑
```

## 适合什么样的 Agent

如果你的 Agent 经常出现以下问题，这个仓库会很有帮助：

- 读了很多信息，但抓不到重点
- 会分析，但不会过滤噪声
- 结论很多，却没有收敛
- 很会解释局部，却看不清系统层面
- 会被复杂表象吸住，失去前瞻视角

这些 skills 的价值不在于替你做工具调用，而在于帮 Agent 在复杂问题里形成更稳定的**认知秩序**。

## 贡献

欢迎贡献新的技能或改进现有框架：

1. Fork 本仓库
2. 在对应目录修改或新增技能
3. 提交 PR

每个技能需要包含 `SKILL.md` 文件，遵循 [AgentSkills 规范](https://clawhub.com)。

## License

MIT License - 自由使用、修改、分发
