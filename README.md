# Skills

我在 AI 编程助手（如 Claude Code）中自用的一系列 AI Agent 技能（Skills），用于编程与学习。

## 常用技能

下面这五个是我日常最常用的技能，放在这里方便快速查找：

- **[humanizer-zh](skills/humanizer-zh/)**：去除中文文本中的 AI 写作痕迹，让表达更自然。
- **[blog-cover-prompt](skills/blog-cover-prompt/)**：按博客既有风格生成封面绘图提示词。
- **[beautify-github-readme](skills/beautify-github-readme/)**：整理并美化 GitHub README 的内容层级与视觉呈现。
- **[requirement-validate](skills/requirement-validate/)**：先复述并确认需求，确认后结束，不直接进入实现。
- **[vibe-learn](skills/vibe-learn/)**：面向非科班开发者，教授工具使用和向 AI 描述需求的方法。

## 技能列表

| 技能 | 说明 |
|------|------|
| [vibe-learn](skills/vibe-learn/) | 为 Vibe Coding / 非科班开发者教授项目开发实践技能。只教"怎么用"和"怎么向AI描述需求"。 |
| [requirement-validate](skills/requirement-validate/) | 需求理解确认闭环。复述需求让用户确认，确认后再实现。 |
| [nsfc-figure-prompts](skills/nsfc-figure-prompts/) | 为NSFC基金申请书生成AI科研绘图提示词。涵盖架构图、技术路线图、机制示意图等学术插画的prompt生成，基于经过7轮迭代验证的8张图模板。 |
| [material-suitability-audit](skills/material-suitability-audit/) | 学习材料多角度适合度审计。五维度评估 → 教学重构 → 用户确认修改。 |
| [study-doc-writer](skills/study-doc-writer/) | 为理解型学习者创建或重写学习文档，强调因果链、推导、边界、练习和复习沉淀。 |
| [skill-optimizer](skills/skill-optimizer/) | 分析和优化 Agent Skill 定义，通过 7 层诊断框架发现并修复问题。 |
| [systematic-planning](skills/systematic-planning/) | 系统规划技能。把学习、考试、项目、能力建设或 skill 设计目标拆成可执行、可复盘、可调整的计划。 |
| [image-understanding](skills/image-understanding/) | 使用本地 Qwen2-VL-2B-Instruct 视觉语言模型分析图片，支持中文描述和图片问答。 |
| [teach](skills/teach/) | Alvar 方法的一对一自适应教学：探查理解边缘、规划依赖路径，并逐步教学。 |
| [probe](skills/probe/) | 使用分级测验探查学习者的知识状态，生成理解地图。 |
| [learn-profile](skills/learn-profile/) | 建立学习者档案，记录基础、目标、节奏和教学偏好。 |
| [learn-visual](skills/learn-visual/) | 为单个教学概念生成并检查可视化图示。 |
| [learn-verify](skills/learn-verify/) | 在教学前核查事实、定理、历史或工具/API 相关断言。 |
| [beautify-github-readme](skills/beautify-github-readme/) | 重构 GitHub README 的内容层级与项目原生视觉系统，固定首屏摘要和 Shields.io 徽章布局，或独立创建 SVG、PNG/WebP 和可选 GIF 资产。 |
| [blog-cover-prompt](skills/blog-cover-prompt/) | 根据文章标题、摘要或正文，生成与 Firefly 博客现有封面一致的深蓝黑底、电蓝全息技术封面绘图提示词。 |
| [humanizer-zh](skills/humanizer-zh/) | 去除中文文本中的 AI 写作痕迹，调整空泛表达、机械句式与模板化结构；译自 blader/humanizer，参考 hardikpandya/stop-slop。 |

## 目录结构

```
├── README.md
└── skills/                      # 技能定义
    ├── vibe-learn/              # Vibe coding 教学技能
    ├── requirement-validate/    # 需求验证技能
    ├── nsfc-figure-prompts/     # NSFC 科研绘图提示词生成技能
    ├── material-suitability-audit/  # 学习材料适合度审计技能
    ├── study-doc-writer/        # 理解型学习文档写作技能
    ├── skill-optimizer/         # Skill 优化诊断技能
    ├── systematic-planning/     # 系统规划技能
    ├── image-understanding/     # 本地视觉语言模型图片理解技能
    ├── teach/                   # Alvar 方法一对一教学
    ├── probe/                   # Alvar 方法理解探查
    ├── learn-profile/           # 学习者档案
    ├── learn-visual/            # 教学概念可视化
    ├── learn-verify/            # 教学事实核查
    ├── beautify-github-readme/  # GitHub README 内容与视觉设计
    ├── blog-cover-prompt/       # 博客封面绘图提示词
    └── humanizer-zh/            # 中文 AI 写作去痕
```

## 使用方式

技能适用于 Claude Code 或兼容的 AI 编程助手。克隆仓库后按需使用。

```bash
git clone https://github.com/HP-Patience/Skills.git
```

每个技能目录下包含 `SKILL.md`（技能定义）及其他支持文件。

## 第三方技能来源

- **humanizer-zh**：收录自 [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)，本次保留本地版本（上游提交 `91f3d394db8419c20d67ebe22a96cf8fee0a404b`），未升级到上游新版。核心内容翻译自 [blader/humanizer](https://github.com/blader/humanizer)，实用规则参考 [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)，基础指南为维基百科的 [AI 写作特征](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)。原项目的 MIT 许可证与版权声明保留在 [skills/humanizer-zh/LICENSE](skills/humanizer-zh/LICENSE)。

## 许可

MIT
