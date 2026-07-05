# 诊断问题汇总

按 7 层 Harness 框架组织的完整诊断问题库。Audit 模式：对所有层回答问题。
Prevent 模式：把问题当设计清单逐层过。

---

## 第 1 层：项目搭建与发现

详见 `references/layer-1-discovery.md`

核心检查：
- Skill 有明确的入口点吗？（SKILL.md 是否起到路由器作用）
- Skill 声明了前提条件吗？（依赖项、所需工具、运行环境）
- Skill 能做环境检测吗？（在 Claude Code 还是 Claude.ai？多了哪些工具？）
- Skill 是否按复杂度分流任务？
- Skill 对启动失败有优雅降级吗？

## 第 2 层：上下文工程

详见 `references/layer-2-context.md`

核心检查：
- Skill 使用渐进式披露吗？（元数据 → SKILL.md 正文 → references）
- SKILL.md 是否在 200 行以内？
- 是否有路由表告诉 Agent 何时加载什么？
- References 是否有加载顺序/条件提示？
- Description 是否具体到能触发，又不至于太窄？
- 关键信息是否放在前 50 行？（利用上下文位置的 U 型曲线）

## 第 3 层：约束与守卫

详见 `references/layer-3-constraints.md`

核心检查：
- 输出格式是否明确定义？
- 是否有检查点/停止点？（强制 Agent 在关键节点停下来验证）
- 是否定义了"不该做什么"而不仅仅是"该做什么"？
- 是否说明了不适用场景？
- 规则是否解释了"为什么"而不只是"是什么"？
- 是否有权限/安全边界？

## 第 4 层：多 Agent 架构

详见 `references/layer-4-multi-agent.md`

核心检查：
- 如果使用子 Agent，行为边界清晰吗？
- Agent 间交接格式明确吗？
- 是否有并行 vs 串行的决策逻辑？
- 子 Agent 指令是否自包含？（不依赖当前对话上下文）
- 是否处理了缺少子 Agent 的环境？（纯 Claude.ai vs Claude Code）

## 第 5 层：评估与反馈

详见 `references/layer-5-evaluation.md`

核心检查：
- Skill 有自我检查机制吗？（完成前自查清单）
- 成功标准是否可量化？
- 是否有测试断言？
- 是否要求人工审核关键步骤？
- 是否可与 skill-creator eval pipeline 集成？

## 第 6 层：长时间运行任务

详见 `references/layer-6-long-running.md`

核心检查：
- 是否有检查点/状态管理？
- 是否能从中断中恢复？
- 步骤是否原子化（可独立重试）？
- 是否有进度通知机制？
- 是否在多步骤工作流中维护上下文？

## 第 7 层：诊断与恢复

详见 `references/layer-7-diagnosis.md`

核心检查：
- 是否定义了错误处理模式？
- 是否区分可恢复错误与致命错误？
- 是否有常见故障的排查指南？
- 是否与 self-improvement 集成（记录 learnings）？
- 是否有静默故障的检测机制？

---

## 使用指南

### Audit 模式

对目标 Skill 的每一层每一题回答 Yes/No/Partial，附证据引用。
最后汇总得分和未通过项，生成诊断报告。

### Prevent 模式

把问题转化为设计引导：
- 不是"你的 Skill 有路由表吗？"（审计语气）
- 而是"我们需要的核心流程有哪些？哪些放 SKILL.md 正文，哪些放 references？"（设计语气）

### Improve 模式

重点关注 Audit 中发现的 Weak/Missing 层的诊断问题，
对照 fix-recipes.md 逐项修复。
