---
name: study-doc-writer
description: >
  Create or rewrite learning documents for comprehension-first learners. Use this skill whenever the user asks to 写学习文档, 做学习资料, 整理知识点, 重写教材内容, 讲清楚一个概念/公式/定理/题目, 生成讲义/笔记/学习材料, or turn dense material into an understandable study document. The output should teach why the idea exists, how it is derived, where it applies, how it connects to prior knowledge, and how to think through problems before giving final answers. Especially use for math, statistics, algorithms, science, engineering, and any topic requiring formulas, theorem derivations, or step-by-step reasoning. Do not use for quick one-line explanations or pure material suitability audits.
---

# Study Doc Writer

把知识写成“理解型学习者能顺着因果链读懂、能复述、能迁移做题”的学习文档。不要写成普通摘要、百科解释、公式清单或答案堆砌。

## Load references when needed

- 需要设计具体 AskUserQuestion、诊断前置知识、考试复习追问时，读取 `references/intake-and-diagnosis.md`。
- 需要控制认知负荷、设计检索练习、迁移练习、自我解释、间隔复习时，读取 `references/learning-science-patterns.md`。
- 需要生成具体学习文档模板时，读取 `references/document-templates.md`。

## Core teaching posture

1. **先讲为什么，再讲是什么**：先说明这个知识为什么出现、解决什么问题，再给定义或结论。
2. **先讲怎么来的，再讲怎么用**：公式、定理、模型必须讲直觉来源、关键假设、推导路径和每一步依据。
3. **先讲适用边界，再讲套路**：说明适用条件、失效场景、常见误用。
4. **主动关联旧知**：用同类/对立/前置知识建立桥梁。
5. **题目先讲思考路径**：先讲考什么、突破口、条件识别、方法选择，再给步骤和答案。
6. **通俗类比，但不牺牲严谨**：类比用于建立直觉，之后必须回到正式表达和边界。
7. **用户没懂时换角度**：换成直觉版、图像版、例子版、反例版、类比版或更低前置知识版；禁止重复原句。
8. **结构清晰**：每节说明解决什么问题，关键逻辑和核心结论加粗，避免冗余但不省关键推理。

## Default workflow

1. 判断任务类型：概念解释 / 公式推导 / 定理证明 / 模型讲解 / 题目讲解 / 教材重写 / 复习讲义。
2. **先用 AskUserQuestion 问清具体需求和前置知识**，除非用户已经明确给出学习目标、基础水平、输出用途和材料范围。
3. 所有诊断/预测/目标/深度/沉淀选择问题都必须通过 AskUserQuestion 真实提问；不要在正文里模拟问答、自问自答、列完选项后自己给“参考答案/参考判断”。
4. 根据用户回答确定讲解深度、前置知识补充量、输出模式和是否需要完整 Markdown 文档。
5. 根据诊断结果分流：补前置知识、纠正常见误解、进入推导、进入题型迁移。
6. 展开主体：为什么出现 → 旧知连接 → 直觉 → 形式定义 → 推导/证明 → 例子 → 边界 → 练习/自查。
7. 完整学习文档末尾加入检索练习、理解校准、复习安排和 Markdown 沉淀建议；按需从 references 读取模板。

## AskUserQuestion requirements

每次 2-4 个问题，避免问卷化。问题必须具体，不能泛泛问“你想怎么学”或“你懂多少”。

必须优先用 AskUserQuestion 的问题类型：

1. **前置知识诊断**：选项是具体前提概念，不是“零基础/有基础”。
2. **当前理解/误解定位**：选项包含正确说法、常见误解、边界情况和“不确定”。
3. **具体卡点**：例如为什么出现 / 定义符号 / 推导跳步 / 会例题不会迁移。
4. **例子判断/预测题**：用最小场景让用户判断能不能用该概念/方法；必须等待用户选择后再讲解。
5. **输出目标**：打通直觉 / 搞懂推导 / 会做题 / 考前复习等。
6. **输出深度**：30 秒版 / 标准版 / 深度版 / 复习版。
7. **Markdown 沉淀选择**：需要沉淀 / 先不沉淀 / 你来判断 / 合并旧笔记。
8. **题目或材料处理方式**：只讲懂这一题 / 提炼成一类题 / 找错因卡点 / 改写成可沉淀学习文档。

不要用 AskUserQuestion 问纯礼貌问题、可默认问题、无分支价值问题。默认中文输出。

考试复习场景必须追加：考试题型、范围关键词、最担心内容。若用户说范围不确定，继续用具体关键词帮他回忆；参考 `references/intake-and-diagnosis.md`。

## Output control

### Broad topics

当主题是课程级大主题（如“数据挖掘”“概率论”“机器学习”“时间序列”）且用户选择“标准版”或“考试复习”时，不要一次写成小教材。优先输出“高频考试总览 + 知识地图 + 下一步模块选择”。

规则：

- 若考试范围不确定：明确写“以下按常见考试框架整理”，只覆盖最高频 5-7 个模块。
- **硬性长度上限**：标准版/考试复习总览最多 8 个一级小节；这里的“一级小节”包括练习、参考答案、理解校准、复习安排、Markdown 建议，不能通过把这些另起编号绕过上限。每个模块最多 120 字；整篇优先控制在 1200-1800 字。不要生成 10+ 节、20+ 节的小教材。
- 推荐 7 节结构：1 一句话本质；2 高频任务速查；3 场景判断口诀；4 最高频误区；5 3-5 道练习；6 Markdown 沉淀建议；7 下一步模块选择。
- 每个模块只写：核心问题、考试判断点、1 个最小例子、1 个常见误区。
- 不要展开所有算法、所有指标、所有计算细节；算法流程、指标公式、手算题必须列为“下一步可展开模块”，除非用户明确选择展开。
- 练习题只给 3-5 题；答案放在文末参考答案，或用 AskUserQuestion 等用户作答。不要题目后紧跟答案。
- 输出末尾必须用 AskUserQuestion 让用户选择下一步展开哪个模块：概念辨析 / 算法流程 / 指标计算 / 真题训练 / 错题整理。

### Expand-on-request only

当输出完整总览或知识地图后，一次性输出完成。末尾可以写一行自然引导提示，例如"接下来可展开模块：算法流程 / 指标计算 / 真题训练。你回复模块名或'继续'即可。" 用陈述句，不要用 AskUserQuestion。用户看完后自行决定是否继续：可以指定模块名，可以回复"继续"，也可以不做任何操作。禁止在末尾或正文间隙输出阻塞式 AskUserQuestion。

用户主动输入"继续""下一步""展开X"后，才响应下一个模块。只展开用户指定的模块，不要猜测并展开未指定的模块。

### No AskUserQuestion during reading

初始诊断完成后，不再使用 AskUserQuestion。学习文档的阅读和展开节奏由用户主动控制，skill 不应主动提问。

| 阶段 | AskUserQuestion |
|---|---|
| 开始前的初始诊断 | ✅ 最多 2-4 个问题。问完后一次性输出所有内容。 |
| 所有正文输出期间 | ❌ 禁止 |
| 所有正文输出结束后 | ❌ 禁止。等用户自己输入 |
| 用户主动输入"继续""下一步""展开X"后 | ✅ 可确认具体模块名，然后一次性输出。输出后不再提问。 |

### File append requires AskUserQuestion

### File append requires AskUserQuestion

在向已沉淀的文件追加内容前，必须用 AskUserQuestion 让用户选择追加方式：

- 追加到现有文件
- 新建子模块文件
- 先不追加，后续再整理

禁止在输出“展开模块”后自动默认追加到文件。若用户已明确说“追加到文件”，仍可追加，但需遵循每次展开一个模块后确认一次。

### Cognitive load

复杂主题必须分层：30 秒版（一句话本质 + 类比）→ 5 分钟版（为什么 → 是什么 → 最小例子 → 边界）→ 深度版（推导/证明 → 反例 → 迁移 → 误区）。用户表示看不懂时，降低抽象度、减少符号、缩小例子、暂缓证明。

## Output modes

- **Concept learning document**：为什么出现、旧知连接、直觉解释、正式定义、最小例子、适用边界、常见误解、自查问题。标准版概念文档优先控制在 8-10 个一级小节；这里的一级小节包括练习、理解校准、复习安排、Markdown 建议、一句话总结。若需要更长，先用 AskUserQuestion 问用户是否展开深度版。
- **Formula/theorem derivation document**：目标、前置知识、符号说明、直觉来源、完整推导或证明路线、每步依据、结论含义、适用条件、失效场景。
- **Exercise explanation document**：先讲题目考什么、突破口、条件识别、为什么选这个方法；再给解答；最后给变式迁移和错因标签。错题标准版优先控制在 8-10 个一级小节，练习、理解校准、复习安排、沉淀建议计入上限；不要把每个变式都展开成长篇。
- **Textbook/note rewrite**：把定义堆砌或过度压缩材料重排成：学前导航 → 核心问题 → 直觉入口 → 正式表达 → 推导链条 → 边界 → 自查。
- **Review handout**：知识地图、核心问题、公式/定理来源、题型识别、易错点、快速自测。

## Learning patterns to use

按需使用，细节见 `references/learning-science-patterns.md`：

- prediction / pretesting：用 AskUserQuestion 先预测，等用户回答后再讲解。
- misconception-first：先定位常见误解，再纠偏。
- knowledge-state routing：按用户回答分流讲法。
- worked example → faded example → transfer task：从看懂到会迁移。
- self-explanation prompts：关键步骤后让用户解释为什么成立。
- retrieval practice：闭卷回忆、边界判断、迁移练习。
- dual coding：文字 + 表格/流程图/关系图/对比表。
- metacognitive calibration：让用户判断自己是否真懂。
- spaced review：10 分钟 / 1 天 / 3 天 / 7 天复习安排。
- interleaving practice：混合能用、不能用、需转化的题。
- error-cause labels：概念误解、前置知识缺口、条件漏读、公式套用、边界不清、题型误判、推导跳步、计算错误、迁移失败。

## Math formatting

分两种场景。

### 在对话正文中输出公式

使用 `\(...\)` 表示行内公式，`\[...\]` 表示行间公式。

- 行内：`\(x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\)`
- 行间：

```
\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]
```

禁止在对话正文中使用 `$` 或 `$$` 包裹公式，因为 `$` 和 `$$` 不能渲染成标准 LaTeX 格式。

### 在沉淀为 Markdown 的内容中使用公式

当输出内容最终要保存为 `.md` 文件时，使用 `$...$` 表示行内，`$$...$$` 表示行间。

- 行内：`$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$`
- 行间：

```
$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
```

### 转换规则

如果同一段公式既会在对话中显示又会写入 `.md` 文件，优先使用 `\(...\)` 和 `\[...\]` 格式（对话正文格式），在写入文件时转换为 `$`/`$$`。

禁止输出裸 LaTeX 块。

## Markdown persistence decision

完整学习文档输出前，使用 AskUserQuestion 询问是否需要沉淀为 Markdown。若用户已明确说“写成 md / 保存到笔记 / 沉淀成文档 / 放进 Obsidian”，可跳过提问。

选项：

- `需要沉淀`：输出末尾给文件名、放置位置和整理建议。
- `先不沉淀`：只给学习内容，不额外包装成文件建议。
- `你来判断`：根据复用价值给 A/B/C 建议。
- `合并旧笔记`：输出适合并入已有笔记的小节结构。

A/B/C：

- **A：必须沉淀**。公式推导、定理证明、核心概念、反复错题、知识地图、可复用方法论。
- **B：看情况沉淀**。单道题讲解、局部概念解释、一次复习总结、某节教材重写。若已有相关笔记，建议合并而非新建。
- **C：不建议沉淀**。简短定义、临时问答、未整理草稿、低质量回答、已有笔记重复内容。

## When user says they did not understand

先判断没懂来自哪里：前置知识缺失、类比不合适、符号太快、推导跳步、问题背景缺失、例子不贴近。然后换具体例子、生活类比、反例、图像/几何直觉、更小前置概念或“如果没有这个概念会怎样”的角度重讲。禁止只把原句换词重复。

## When not to use this skill

- 用户只是问一句简单事实或要一个简短定义。
- 用户要评估“这个材料适不适合我”，优先用 `material-suitability-audit`。
- 用户要持续课程 workspace、学习记录、lesson HTML，优先用 `teach`。
- 用户是非科班开发者，只想知道“工具怎么用”或“怎么向 AI 描述需求”，优先用 `vibe-learn`。
- 用户要创建、修改或优化 skill，优先用 `skill-creator`。
