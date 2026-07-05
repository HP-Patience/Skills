# 第 2 层：上下文工程

**何时加载**: Audit、Prevent 模式；或诊断 Skill 的上下文管理能力时。

**核心问题**: 正确的信息在正确的时机以正确的量加载了吗？

---

## 诊断问题

### 渐进式披露

1. SKILL.md 是否 < 200 行？（复杂 Skill 可放宽到 300 行，超过 500 行是 Critical）
2. 信息是否按三层加载？（Metadata → SKILL.md body → References）
3. SKILL.md 是否真的起到了路由器的作用，而不仅仅是个"目录"？
4. 是否避免了把一个超长文件拆成 10 个中等文件然后全部加载？（这不算渐进式披露）

### 路由表

5. SKILL.md 是否有路由表或等效机制？（告诉 Agent 在什么场景下读哪个 reference）
6. 路由表的场景粒度是否合适？（太粗 = 什么场景都加载同一个文件；太细 = Agent 找不到）
7. 路由表是否放在 SKILL.md 靠前位置？（前 50 行是最佳位置——U 型曲线原理）

**糟糕模式**: SKILL.md 末尾写 "See also: references/a.md, references/b.md, references/c.md"——没有场景区分，Agent 要么全读，要么不读。

**优秀模式**: mcp-builder 的 "Load During Phase X" 标签。

### 信息密度与位置

8. 最重要信息是否放在文件前 30% 的位置？（"Lost in the Middle"——Agent 对中间位置的利用率显著低于开头和结尾）
9. 每条指令是否解释了"为什么"而不只是"是什么"？（帮助 Agent 在边界情况下做出正确判断）
10. 是否避免了"每个指令都标注重要"？（所有东西都是 important = 没有东西重要）
11. 关键约束是否用反例说明？（"不要做 X，因为会导致 Y" 比 "做 Z" 更易被遵守）

### Description 质量

12. Description 是否包含具体的动作关键词和输入类型？
13. Description 是否包含用户可能说的自然语言触发词？（而不是技术术语）
14. Description 是否覆盖了"用户不点名 Skill 但明显需要"的场景？
15. Description 长度是否在 1024 字符以内？

**诊断提示**: Description 是三层加载的第一层——如果这层失效，Skill 永远不会被加载。
宁愿稍微宽泛（多触发）也不愿过于狭窄（不触发）。误触发可以通过 SKILL.md 正文中的
"不适用场景"来筛选。

### 上下文清洁度

16. 是否存在"死内容"？（从未被触发过的规则、过时的引用、废弃的示例）
17. 一条规则能写成一行吗？如果不能，它是否值得保留？
18. 代码示例是否优于段落描述？（GitHub 对 2500+ AGENTS.md 的分析结论）

---

## 本层优秀模式

| 模式 | 来源 | 说明 |
|------|------|------|
| 路由表 | skill-optimizer | "路由逻辑"段，按模式指定加载哪个 reference |
| Phase 标签 | mcp-builder | "Load During Phase 1/2" 明确加载时机 |
| 场景分流 | huashu-design | "做动画 → references/animation.md" |
| 加载条件 | self-improvement | 每个 reference 说明"何时使用" |

## 本层常见故障

1. **单块 SKILL.md**: 所有内容在一个 800 行文件中，无路由
2. **全加载**: 路由表没有场景区分，Agent 全读
3. **信息稀释**: 关键指令淹没在长文本中（参考 U 型曲线）
4. **Description 失效**: 过宽/过窄，Skill 不触发或误触发

## 评分指南

| 评分 | 标准 |
|------|------|
| **Strong** | SKILL.md <200 行，路由表清晰，description 具体，渐进式披露完整 |
| **Adequate** | SKILL.md <500 行，有基本路由，description 可用 |
| **Weak** | SKILL.md >500 行或路由缺失，信息组织随意 |
| **Missing** | 一个巨大文件，无路由，无分层，全量倾倒 |
