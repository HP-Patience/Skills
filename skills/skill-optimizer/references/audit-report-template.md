# Audit Report Template

使用此模板输出 Skill 审计报告。格式固定——遵循此模板确保输出一致。

## 模板

```markdown
# Skill Audit: {skill-name}

**审计时间**: {timestamp}
**Skill 路径**: {path}
**SKILL.md 行数**: {N} 行
**References 数量**: {N} 个文件

---

## Executive Summary

**总体评分**: {Strong / Adequate / Needs Work / Critical Issues}

**一句话诊断**: {最核心的问题是什么}

**Top 3 问题**:
1. [{severity}] {问题简述} — {影响}
2. [{severity}] {问题简述} — {影响}
3. [{severity}] {问题简述} — {影响}

---

## Layer Scores

| # | Layer | Score | Key Gap |
|---|-------|-------|---------|
| 1 | 项目搭建与发现 | {score} | {一句话} |
| 2 | 上下文工程 | {score} | {一句话} |
| 3 | 约束与守卫 | {score} | {一句话} |
| 4 | 多 Agent 架构 | {score} | {一句话} |
| 5 | 评估与反馈 | {score} | {一句话} |
| 6 | 长时间运行 | {score} | {一句话} |
| 7 | 诊断与恢复 | {score} | {一句话} |

---

## Detailed Findings

### Layer 1: 项目搭建与发现 — {score}

**证据**:
- {具体引用 skill 中的内容，文件名:行号}

**通过的检查** ({N}/{total}):
- {检查项} ✅

**未通过的检查** ({N}/{total}):
- {检查项} ❌ — {为什么重要}

### Layer 2: 上下文工程 — {score}

{同上格式}

### Layer 3: 约束与守卫 — {score}

{同上格式}

### Layer 4: 多 Agent 架构 — {score}

{同上格式}

### Layer 5: 评估与反馈 — {score}

{同上格式}

### Layer 6: 长时间运行 — {score}

{同上格式}

### Layer 7: 诊断与恢复 — {score}

{同上格式}

---

## Failure Patterns Identified

| # | Pattern | Severity | Evidence | Fix Recipe |
|---|---------|----------|----------|------------|
| 1 | {名称} | {严重度} | {证据} | {指向 fix-recipes.md} |
| 2 | {名称} | {严重度} | {证据} | {指向 fix-recipes.md} |

---

## Recommendations

按优先级排列：

### Critical
1. **{标题}** — 影响: {描述}。修复: {简要方案}。预估改动: {大/中/小}

### High
2. **{标题}** — 影响: {描述}。修复: {简要方案}。预估改动: {大/中/小}

### Medium
3. **{标题}** — 影响: {描述}。修复: {简要方案}。预估改动: {大/中/小}

### Low
4. **{标题}** — 影响: {描述}。修复: {简要方案}。预估改动: {大/中/小}

---

## Next Steps

- [ ] {优先修复 Critical 项}
- [ ] {进入 Improve 模式逐项修复}
- [ ] {修复完成后用 skill-creator 做量化前后对比}
```
