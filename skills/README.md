# Skills

Claude Code skills collection. 每个子目录是一个可独立安装的 skill，通常包含 `SKILL.md` 和可选的 `references/`、`README.md` 等辅助文件。

## 安装方式

把需要的 skill 目录复制到 Claude Code 的 skills 目录，然后重启 Claude Code：

```bash
# macOS / Linux
cp -r <skill-name> ~/.claude/skills/

# Windows 示例
cp -r <skill-name> C:/Users/<你>/\.claude/skills/
```

安装后可在 Claude Code 中用 `/skill-name` 调用，或让 Claude 根据触发场景自动使用。

## Skill 列表

| Skill | 用途 |
|---|---|
| `material-suitability-audit` | 多角度评估学习材料、教材或学习路线是否适合理解型学习者，并给出教学重构方案。 |
| `nsfc-figure-prompts` | 为 NSFC / 科研申请书生成统一学术风格的 AI 绘图提示词。 |
| `requirement-validate` | 需求理解确认闭环：先复述、再让用户确认，不进入实现阶段。 |
| `skill-optimizer` | 基于 Harness Engineering 原则审计和优化 Claude Code Skill。 |
| `study-doc-writer` | 为理解型学习者创建或重写学习文档、讲义、笔记和概念解释。 |
| `systematic-planning` | 把模糊学习、考试、项目、能力建设或 skill 设计目标转成可执行、可复盘、可调整的系统计划。 |
| `vibe-learn` | 面向 vibe coding / 非科班开发者，教授如何用专业语言向 AI 描述需求。 |

## 目录约定

```text
<skill-name>/
├── SKILL.md          # skill 入口、触发条件和主流程
├── README.md         # 可选：面向用户的说明
└── references/       # 可选：详细规则、模板、案例或检查清单
```

原则：`SKILL.md` 保持可快速加载；大篇幅模板、案例和细则放进 `references/`。
