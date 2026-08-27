# Skills

我在 AI 编程助手（如 Claude Code）中自用的一系列 AI Agent 技能（Skills），用于编程与学习。

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
    └── beautify-github-readme/  # GitHub README 内容与视觉设计
```

## 使用方式

技能适用于 Claude Code 或兼容的 AI 编程助手。克隆仓库后按需使用。

```bash
git clone https://github.com/HP-Patience/Skills.git
```

每个技能目录下包含 `SKILL.md`（技能定义）及其他支持文件。

## 许可

MIT
