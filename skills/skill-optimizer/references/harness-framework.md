# Harness Engineering 核心框架

## 公式与类比

```
Agent = Model + Harness
```

| 组件 | 类比 | 说明 |
|------|------|------|
| Model | CPU | 算力本身，生成能力极强但可能偏航 |
| Context Window | RAM | 工作记忆，有限且易稀释 |
| Harness | 操作系统 | 调度、约束、反馈、文件系统——一切让 CPU 有效工作的基础设施 |

**你不会指望 CPU 在裸机上高效运行，同理不该指望模型在没有 Harness 的项目里稳定输出。**

LangChain 的对照实验：不改模型，仅优化 Harness，Agent 准确率从 52.8% → 66.5%（+26%）。

## 四动词循环

Harness 的核心动作，贯穿全部 7 层：

```
Constrain（约束）→ Inform（告知）→ Agent 执行 → Verify（验证）→ Correct（修正）→ 循环
```

| 动词 | 中文 | 含义 | 落地形态 |
|------|------|------|---------|
| Constrain | 约束 | 给 Agent 设定边界和规则 | lint 规则、类型检查、pre-commit hooks、架构边界 |
| Inform | 告知 | 把正确知识放入 Agent 上下文 | AGENTS.md、docs/ 知识库、ADR、渐进式披露 |
| Verify | 验证 | 自动检验 Agent 的输出 | CI 测试、结构测试、自我检查清单、截图对比 |
| Correct | 修正 | 把错误信号反馈回 Agent | lint 错误嵌入修复指引、自审 + 交叉 Agent 评审 |

**关键认知**：你不能用一个非确定性系统去守护另一个非确定性系统。
Harness 的确定性部分（Linter、结构测试、CI 钩子）比 LLM 部分更重要。

## 7 层 Harness 模型

7 层从基础到高级，下层支撑上层：

| # | 层 | 解决什么问题 | 核心原则 |
|---|-----|-------------|---------|
| 1 | 项目搭建与发现 | Skill 不知道自己在什么环境 | 入口清晰，前提可检查，降级有路径 |
| 2 | 上下文工程 | Skill 看到的信息不对 | 给地图不给手册，渐进式披露，按需加载 |
| 3 | 约束与守卫 | Skill 犯重复的错 | 每犯一次错加一条规则，机械化执行 |
| 4 | 多 Agent 架构 | 单 Agent 搞不定复杂任务 | 分工明确，协议清晰，交接结构化 |
| 5 | 评估与反馈 | 不知道 Skill 做得好不好 | 让 AI 检查 AI，成功标准可量化 |
| 6 | 长时间运行 | Skill 跑着跑着就走偏了 | 进度文件 + 上下文重置 + 可恢复检查点 |
| 7 | 诊断与恢复 | 用户骂 Skill 不好用 | 问题在 Harness 不在模型，诊断覆盖所有层 |

## 核心原则详解

### 1. "给地图，不给手册"

传统做法是给 Agent 写详细的分步指令（手册），但这让 Agent 变得脆弱——
任何偏差都会导致它不知所措。

```markdown
# 不好的写法（手册——脆弱，任何偏差都会卡住）
Step 1: 打开 src/auth/login.ts
Step 2: 找到 handleLogin 函数
Step 3: 在第 42 行添加...

# 好的写法（地图——Agent 能自主导航）
Auth 系统在 src/auth/。登录流程：login.ts → validate.ts → session.ts。
限流中间件在 src/middleware/rateLimit.ts——参考它的模式。
每次修改 auth 都要在 src/auth/__tests__/ 里加测试。
```

地图让 Agent 能自主导航，手册让它成为脆弱的执行机器。
映射到 Skill 设计：**SKILL.md 是地图，不是百科全书。**

### 2. "每犯一次错，加一条规则"

Mitchell Hashimoto 的核心原则：

> "Anytime you find an agent makes a mistake, you take the time to engineer a
> solution such that the agent never makes that mistake again."

AGENTS.md / SKILL.md 不是写一次就忘的文档，它是**免疫系统**：
每次 Agent 犯错 → 加一条规则防止再犯 → 随着时间积累，Agent 对已知模式
的错误率趋近于零。

这就是 Martin Fowler 说的 "Relocating Rigor"——把人类通过 Code Review、
经验、直觉实施的质量把关，迁移到自动化检查中。

### 3. "约束解空间而非扩大它"

Agent 会忠实地复制并放大代码库中已有的模式——包括坏模式。
更少的有效选项意味着更少的错误答案。

- 选"无聊"的技术——训练数据充分、API 稳定的库，Agent 使用得更好
- 强制单向依赖流——不是靠文档约定而是靠 lint 规则机械执行
- 库白名单优于"随便用什么库"

### 4. "为删除而构建"

模型在变强，今天需要的约束明天可能就多余了。
每个规则都应该有一个明确的失效条件：
- 当模型不再犯某类错误时，对应的 lint 规则可以删除
- 当某条 AGENTS.md 规则从未被触发时，它只是在稀释上下文
- 定期审计 Harness 的反向指标：规则多≠质量高

### 5. "Blueprint 模式：确定性与概率性节点交替"

Stripe 的核心设计：

```
[Agent 实现] → [确定性 Lint] → [Agent 修 CI] → [确定性 CI 全量测试] → [人类 Review]
     ↑              ↑              ↑              ↑                   ↑
  概率性         确定性          概率性         确定性              人类判断
```

确定性门禁"夹住"概率性的 LLM 工作。Agent 最多尝试 2 轮 CI 就放弃，
而不是无限循环。映射到 Skill 设计：在 Skill 指令中嵌入确定性的检查步骤，
不要让 Agent 自己判断"做完了没有"。

### 6. "Harness = 数据集"

每次 Agent 交互都是一个训练信号：
- 它尝试了什么
- 什么成功了
- 什么失败了
- 修复方案是什么

这些痕迹（traces）就是竞争优势——不是用于微调模型，而是用于优化操作系统。

## 层间依赖关系

- 没有第 1 层（发现），上层无法获得正确的环境信息
- 没有第 2 层（上下文），第 5 层（评估）的标准可能不相关
- 没有第 3 层（约束），第 7 层（诊断）只能反复救火
- 第 5 层（评估）为第 7 层（诊断）提供信号源
- 第 6 层（长时间运行）强依赖第 1-3 层的基础设施

## 诊断视角 vs 设计视角

| 场景 | 用这个框架做什么 |
|------|----------------|
| 审计已有 Skill | 逐层打分，找缺失和薄弱层，识别故障模式 |
| 改进 Skill | 定位根因层，按修复配方逐项整改 |
| 设计新 Skill | 把诊断问题当设计清单，从第 1 层开始逐层构建 |

---

下一步：读 `references/diagnostic-questions.md` 进行具体诊断。
