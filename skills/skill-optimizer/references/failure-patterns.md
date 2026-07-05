# 故障模式目录

14 种常见 Skill 故障模式。每种包含症状、根因、严重度、和指向 fix-recipes.md 的修复配方。

---

## 1. 巨型 SKILL.md（Monolithic SKILL.md）

**症状**: SKILL.md 超过 500 行，所有内容堆在一个文件里。
**根因**: 没有使用渐进式披露，所有知识一次性倾倒。
**严重度**: Critical
**影响**: Agent 面对超长指令时信息稀释（"Lost in the Middle"效应），关键指令被淹没。
**修复**: 见 `fix-recipes.md` → 配方 1

---

## 2. 描述失效（Description Failure）

**症状**: Skill 该触发时不触发，或不该触发时误触发。
**根因**: description 太宽泛（"帮助做数据任务"）或太窄（只匹配精确短语）。
**严重度**: Critical
**影响**: Skill 形同虚设。
**修复**: 见 `fix-recipes.md` → 配方 2

---

## 3. 上下文过载（Context Overload）

**症状**: SKILL.md 指示 Agent 一次性加载所有 references，即使和当前任务无关。
**根因**: 未区分"总是需要"和"按场景需要"，缺少路由逻辑。
**严重度**: High
**影响**: 上下文稀释，Agent 注意力分散，token 浪费。
**修复**: 见 `fix-recipes.md` → 配方 3

---

## 4. 隐性知识假设（Implicit Knowledge Assumption）

**症状**: Skill 的指令依赖 Agent 默认已知的信息，但这些信息不在 Skill 中，也不在 references 中。
**根因**: 写 Skill 的人假设 Agent"应该知道"，没有明确写入。
**严重度**: High
**影响**: 输出质量飘忽不定，取决于模型是否有对应训练数据。
**修复**: 见 `fix-recipes.md` → 配方 4

---

## 5. 无验证（No Verification）

**症状**: Skill 执行完就结束了，没有自我检查步骤。"做完了"就是"做好了"。
**根因**: 没有嵌入 Verify 步骤，没有断言或成功标准。
**严重度**: Critical
**影响**: 模型对"第一个看起来可行的方案"产生偏见（first plausible solution bias），
输出经常有未检测到的错误。
**修复**: 见 `fix-recipes.md` → 配方 5

---

## 6. 硬编码综合征（Hardcoded Values Syndrome）

**症状**: Skill 包含硬编码路径、文件结构、项目名称。"打开 src/auth/login.ts"这种。
**根因**: Skill 为特定项目定制，不可迁移。
**严重度**: Medium
**影响**: 迁移到其他项目时完全失效。
**修复**: 见 `fix-recipes.md` → 配方 6

---

## 7. 约束蔓延（Rule Sprawl）

**症状**: 每次出问题就加一条规则，规则越来越多但没有结构。SKILL.md 变成规则坟场。
**根因**: 未使用"为删除而构建"原则。规则只添加不清理。
**严重度**: Medium
**影响**: 上下文被低质量规则稀释，Agent 无从区分轻重。
**修复**: 见 `fix-recipes.md` → 配方 7

---

## 8. 幽灵子 Agent（Ghost Subagent）

**症状**: Skill 提到"用子 Agent 处理 X"，但没有定义子 Agent 的行为边界、输入输出格式、错误处理。
**根因**: 多 Agent 设计不完整，只描述意图不描述协议。
**严重度**: High
**影响**: 子 Agent 行为不可预测，交接信息丢失，整体输出不稳定。
**修复**: 见 `fix-recipes.md` → 配方 8

---

## 9. 无错误模型（No Error Model）

**症状**: Skill 假设一切顺利。没有错误处理逻辑，没有降级路径。
**根因**: 写 Skill 时只考虑了 happy path。
**严重度**: High
**影响**: 遇到任何异常就卡住或静默失败。
**修复**: 见 `fix-recipes.md` → 配方 9

---

## 10. 状态失忆（State Amnesia）

**症状**: 对长时间运行任务，没有检查点、进度记录或恢复机制。中断后从头开始。
**根因**: 未考虑会话中断场景。
**严重度**: Medium
**影响**: 长时间任务不可靠，浪费大量 token 重做已完成的工作。
**修复**: 见 `fix-recipes.md` → 配方 10

---

## 11. 工具不足（Tool Scarcity）

**症状**: Skill 让 Agent 用自然语言做重复性、确定性工作（如格式转换、批量重命名），而不是提供脚本。
**根因**: 过度依赖 LLM 能力，忽略了确定性工具的效率和可靠性。
**严重度**: Medium
**影响**: 慢、贵、输出不一致。每次都要"重新发明"。
**修复**: 见 `fix-recipes.md` → 配方 11

---

## 12. 输出模糊（Output Ambiguity）

**症状**: Skill 没有规定输出格式，"生成一个报告"但没有说报告结构是什么。
**根因**: 缺乏 Constrain 思维，输出完全靠模型自由发挥。
**严重度**: Critical
**影响**: 每次运行输出结构不同，下游无法可靠消费。用户每次都要重新理解。
**修复**: 见 `fix-recipes.md` → 配方 12

---

## 13. 无路由表（No Routing Table）

**症状**: SKILL.md 正文很长但没有告诉 Agent"什么时候读哪个 reference 文件"。Agent 要么全读，要么不读。
**根因**: 未理解 JSON 路由模式。SKILL.md 正文是地图，应该告诉 Agent 去哪里。
**严重度**: High
**影响**: 无关信息加载到上下文，相关信息可能被遗漏。
**修复**: 见 `fix-recipes.md` → 配方 13

---

## 14. 无禁区（No Negative Space）

**症状**: Skill 只定义了"做什么"，没有定义"不做什么"、"不适用于什么场景"。
**根因**: 写 Skill 时只想覆盖 happy path，未考虑边界。
**严重度**: Medium
**影响**: Skill 被错误场景触发时行为不可控。与其他 Skill 的职责边界模糊。
**修复**: 见 `fix-recipes.md` → 配方 14

---

## 严重度速查

| 严重度 | 含义 | 何时修复 |
|--------|------|---------|
| **Critical** | Skill 无法可靠触发或输出不可控 | 立即 |
| **High** | 重要机制缺失，频繁出问题 | 本次迭代 |
| **Medium** | 有改进空间，当前勉强能用 | 下次迭代 |
| **Low** | 锦上添花 | 有精力时 |

---

下一步：读 `references/fix-recipes.md` 获取每种模式的修复方案。
