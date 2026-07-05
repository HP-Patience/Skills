---
name: skill-optimizer
description: >
  基于 Harness Engineering 原则审计和优化 Claude Code Skill。当用户想要审计
  一个 Skill 的结构质量、改进现有 Skill 的 harness 设计、在写新 Skill 前做预防性
  设计评审时使用。触发词包括："skill 审计"、"优化 skill"、"改进我的 skill"、
  "skill review"、"skill audit"、"harness 审计"、"skill 质量检查"、"我的 skill
  有什么问题"、"帮我看下这个 skill"。也适用于 Skill 反复出现系统性问题时——
  此 Skill 诊断的是 harness 层面，而非单次任务输出。
---

# Skill Optimizer

基于 **Harness Engineering** 的诊断和优化 Skill，核心公式：

> **Agent = Model + Harness**
>
> Agent 表现不好，80% 的原因不在模型，在 Harness。——Anthropic

Harness 是围绕模型的一切：上下文、约束、工具、验证循环。本 Skill 审计的是 Harness
结构，不是单次任务输出。

## Quick Reference

| 模式 | 触发场景 | 做什么 |
|------|---------|--------|
| **Audit** | "审计这个 skill"、"review my skill" | 读取 skill，按 7 层诊断，输出报告 |
| **Improve** | "改进这个 skill"、"fix my skill" | 先 Audit，再按修复配方逐项改进 |
| **Prevent** | "我想写一个新 skill" | 用 Harness 原则引导设计，预防问题 |

## 模式选择

1. 用户要**创建**新 Skill？→ **Prevent** 模式
2. 用户要**修复/改进**已有 Skill？→ **Improve** 模式
3. 其他（评审、审计、"这个好不好？"）→ **Audit** 模式

## 路由逻辑

根据模式按优先级读 reference 文件：

- **所有模式**：先读 `references/harness-framework.md`（核心模型）
- **Audit**：再读 `references/diagnostic-questions.md` → `references/audit-report-template.md`
- **Improve**：再读 `references/failure-patterns.md` → `references/fix-recipes.md`
- **Prevent**：再读 `references/diagnostic-questions.md`（把问题当设计清单用）
- **深入某层**：读对应的 `references/layer-N-*.md`

## Audit 模式流程

```
1. 读取目标 Skill 的 SKILL.md 和所有 bundled resources
2. 对 7 层逐一回答诊断问题
3. 每层评分：Strong / Adequate / Weak / Missing
4. 识别 3-5 个最严重的故障模式
5. 按 references/audit-report-template.md 输出诊断报告
6. 询问用户是否对 Weak/Missing 层进入 Improve 模式
```

**重要**：审计结果必须有具体的证据引用（引用原 Skill 的具体行/段），
不能只是"感觉不好"。每个评分都要解释"为什么"。

## Improve 模式流程

```
1. 先跑 Audit（必须先诊断）
2. 按影响排序展示问题，每项附修复方案
3. 一次只修复一项（对应的 Constrain→Inform→Verify→Correct 原则）
4. 每项修复后，用 2-3 个测试提示验证
5. 重审受影响层（不全量重审）
6. 重复直到用户满意或所有 Critical/High 问题解决
7. 建议：结构修复完成后，用 skill-creator 的 eval pipeline 做量化前后对比
```

**一次一个修复**——这对应"每犯一次错，加一条规则"。批量修复无法判断哪个改动
真正有效。

## Prevent 模式流程

```
1. 问 5 个问题（不多于 5）：
   - 这个 Skill 要完成什么任务？
   - 什么时候触发？（给 3 个用户的真实说法示例）
   - 期望的输出格式是什么？
   - 可能出什么错？（想 2-3 个失败场景）
   - 需要脚本还是纯指令就够了？
2. 把 references/diagnostic-questions.md 当设计清单逐层过
3. 设计 Skill 结构（渐进式披露方案）
4. 写 SKILL.md 草稿
5. 自审计草稿
6. 展示给用户，迭代
```

## 7 层 Harness 框架速览

详细内容读 `references/harness-framework.md`。

| # | 层 | 核心问题 |
|---|-----|---------|
| 1 | 项目搭建与发现 | Skill 能自我定位吗？有入口和前提检查吗？ |
| 2 | 上下文工程 | 正确的信息在正确的时间加载了吗？ |
| 3 | 约束与守卫 | 边界清晰吗？规则被强制了吗？ |
| 4 | 多 Agent 架构 | 任务被有效分解了吗？子 Agent 边界清晰吗？ |
| 5 | 评估与反馈 | Skill 能测量自己的质量吗？ |
| 6 | 长时间运行 | Skill 能在中断后恢复吗？ |
| 7 | 诊断与恢复 | Skill 能检测并修复自己的错误吗？ |

## 核心概念速览

四个动词贯穿所有层，形成闭环：

> **Constrain**（约束）→ 给 Agent 设定边界和规则
> **Inform**（告知）→ 把正确知识放入 Agent 上下文
> **Verify**（验证）→ 自动检验 Agent 的输出
> **Correct**（修正）→ 把错误信号反馈回 Agent

关键原则：

- **"给地图，不给手册"** — AGENTS.md / SKILL.md 是索引，不是百科全书
- **"每犯一次错，加一条规则"** — 把每次失败转化为一个机械化的检查
- **"约束解空间"** — 更少的有效选项意味着更少的错误答案
- **"为删除而构建"** — 模型在变强，今天的约束明天可能多余

## 与 skill-creator 的关系

- **skill-creator** 处理 **WHAT**（draft → test → review → improve 流程）
- **skill-optimizer** 处理 **HOW**（harness 质量，结构设计）

先用 skill-optimizer 诊断结构问题，修复完后再用 skill-creator 的 eval pipeline
做量化对比。两者互补，不是替代。

## 自我指涉

此 Skill 本身需要通过自己的审计。如果用它审计自己发现 Weak 层，
那些也是需要修复的 bug。

## 不适用场景

- 不适用于评估单次 Agent 任务输出——这是审计 Skill **结构质量**，不是审计任务结果
- 如果只是想看 Skill 的触发率/基准数据，直接用 skill-creator 的 eval pipeline
- 如果 Skill 只有 20 行且只做一件事，可能不需要完整的 7 层审计——用 Prevent 模式
  快速过一下即可

## 审计自己的输出

每次 Audit 完成后，自检：
1. 每个评分是否有**具体证据引用**（不能"感觉不好"）？
2. 诊断报告是否遵循了 `references/audit-report-template.md` 的格式？
3. 修复建议是否指向了 `references/fix-recipes.md` 的具体配方？
4. 是否按严重度排序了？（Critical → High → Medium → Low）

## 遇到问题时的处理

| 情况 | 处理方式 |
|------|---------|
| 目标 Skill 不存在或路径错误 | 确认路径，让用户重新提供 |
| 目标 Skill 没有 SKILL.md | 告诉用户这不是有效 Skill，建议用 skill-creator 创建 |
| 目标 Skill 只有 SKILL.md 无 references | 正常审计，第 2 层上下文工程会扣分 |
| 无法确定评分（两可之间） | 取低分（宁可低估，不高估），附注"需更多证据" |
| 用户不接受某条审计结果 | 接受反馈，如果用户有道理则修正（这本身就是 Correct 循环） |

## 评分标准

| 评分 | 含义 |
|------|------|
| **Strong** | 层内各维度得分 ≥ 80% |
| **Adequate** | 核心维度 ≥ 70%，其余 ≥ 50% |
| **Weak** | 核心维度 < 70%，或任一维度 < 50% |
| **Missing** | 该层不存在（如没有评估机制、无错误处理） |

## 故障严重度

| 严重度 | 含义 |
|--------|------|
| **Critical** | Skill 无法可靠触发或输出不可控 |
| **High** | 重要机制缺失，频繁出问题 |
| **Medium** | 有改进空间，当前勉强能用 |
| **Low** | 锦上添花，不修也无大碍 |
