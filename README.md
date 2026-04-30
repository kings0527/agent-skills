# Agent Skills

一套用于 AI Agent 的技能集合，包含**通用决策框架**、**工程分析框架**，以及**逆向工程元认知框架**，帮助 Agent 在复杂任务中更系统化地分配注意力、切换思维模型并收敛结论。

## 技能列表

| 技能 | 说明 | 适用场景 |
|------|------|---------|
| [FOUDF](./FOUDF/) | 五算子通用决策框架 | 跨领域复杂决策（商业/政策/人际关系/技术选型等） |
| [DevTrace](./DevTrace/) | 技术决策五算子 | 工程落地（架构决策/技术选型/代码审查/重构评估） |
| [re-metastrategy-cognitive](./re-metastrategy-cognitive/) | 逆向工程元认知控制器 | 逆向分析、恶意代码分析、混淆/反调试、协议恢复、漏洞面推理 |

## 安装方式

### OpenClaw

将技能复制到你的 skills 目录：

```bash
# 安装全部
git clone https://github.com/kings0527/agent-skills.git
cp -r agent-skills/* ~/.openclaw/workspace/skills/

# 或单独安装
curl -o ~/.openclaw/workspace/skills/FOUDF/SKILL.md \
  https://raw.githubusercontent.com/kings0527/agent-skills/main/FOUDF/SKILL.md

curl -o ~/.openclaw/workspace/skills/DevTrace/SKILL.md \
  https://raw.githubusercontent.com/kings0527/agent-skills/main/DevTrace/SKILL.md

mkdir -p ~/.openclaw/workspace/skills/re-metastrategy-cognitive
curl -o ~/.openclaw/workspace/skills/re-metastrategy-cognitive/SKILL.md \
  https://raw.githubusercontent.com/kings0527/agent-skills/main/re-metastrategy-cognitive/SKILL.md
```

### Claude Code / 其他 CLI Agent

将 SKILL.md 放入你的项目或全局提示词目录：

```bash
# 下载到项目目录
curl -O https://raw.githubusercontent.com/kings0527/agent-skills/main/FOUDF/SKILL.md
curl -O https://raw.githubusercontent.com/kings0527/agent-skills/main/DevTrace/SKILL.md
curl -O https://raw.githubusercontent.com/kings0527/agent-skills/main/re-metastrategy-cognitive/SKILL.md

# 或在 CLAUDE.md 中引用
# 参考这些思维框架进行复杂决策分析...
```

### Cursor / Windsurf / 其他 IDE Agent

在项目规则文件中引入：

```markdown
# 决策框架参考
- 通用决策: https://raw.githubusercontent.com/kings0527/agent-skills/main/FOUDF/SKILL.md
- 技术决策: https://raw.githubusercontent.com/kings0527/agent-skills/main/DevTrace/SKILL.md
- 逆向元认知: https://raw.githubusercontent.com/kings0527/agent-skills/main/re-metastrategy-cognitive/SKILL.md
```

## 框架对比

| 维度 | FOUDF | DevTrace | RE-MetaStrategy |
|------|-------|----------|-----------------|
| **定位** | 元认知工具 | 工程落地工具 | 逆向元认知控制器 |
| **适用域** | 任何复杂系统 | 技术系统 | 二进制/恶意代码/保护机制 |
| **核心关注** | System / Layer / Probability / Constraint / Game | Topology / Abstraction / Entropy / Constraint / Dependency | Attention Budget / Task Mode / Object Typing / Hypothesis Pool / Mental Models |
| **输出风格** | 概率建模、博弈推演 | 拓扑图、熵增评估、依赖清单 | 机制语义、业务语义、区分证据、收敛控制 |
| **典型场景** | 选专业、评架构、分析关系、制定政策 | 微服务拆分、技术选型、重构评估、代码审查 | 逆向分析、VM/壳、反调试、协议恢复、绕过面定位 |

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
- Hypothesis Pool:
  1. license_check
  2. environment_gate
  3. telemetry_precheck
- Mental Model: trust_chain + temporal_delta
- 收敛目标：定位关键校验路径，并区分它与环境探针/埋点逻辑
```

## 贡献

欢迎贡献新的技能或改进现有框架：

1. Fork 本仓库
2. 在对应目录修改或新增技能
3. 提交 PR

每个技能需要包含 `SKILL.md` 文件，遵循 [AgentSkills 规范](https://clawhub.com)。

## License

MIT License - 自由使用、修改、分发
