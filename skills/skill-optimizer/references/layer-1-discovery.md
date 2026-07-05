# 第 1 层：项目搭建与发现

**何时加载**: Audit、Prevent 模式；或诊断 Skill 的自定位能力时。

**核心问题**: Skill 能自我定位吗？有清晰的入口和前提检查吗？

---

## 诊断问题

### 入口与路由

1. SKILL.md 是否起到路由器作用？（不是堆砌内容，而是告诉 Agent 去哪里找）
2. Skill 的第一个指令是否清晰？（Agent 打开 SKILL.md 后，前 3 段内就知道该做什么）
3. 是否有 Quick Reference 表或类似机制让 Agent 快速定位？

**优秀示例**: self-improvement 的 Quick Reference 表，Agent 5 秒内能路由到正确操作。

### 前提与依赖

4. Skill 是否声明了必需工具/环境？（如"需要 Puppeteer MCP"、"需要 Python 3.10+"）
5. 如果前提不满足，Skill 是否给出了明确的报错和解决方案？
6. 是否有引导设置步骤（setup/bootstrap）？

**优秀示例**: cython-pyd-reverse 的 Prerequisites 表格，运行前检查 Ghidra、Python 环境。

### 环境检测

7. Skill 是否区分不同运行环境？（Claude Code vs Claude.ai vs Cowork）
8. 是否利用了环境优势？（Claude Code 有 subagent 和 hook，Claude.ai 没有）
9. 是否在环境能力不足时有降级路径？

### 任务分流

10. Skill 是否按复杂度分流任务？（简单任务直接做，复杂任务走完整流程）
11. 是否有明确的"简单场景快速路径"和"复杂场景完整路径"？
12. 任务范围是否明确？（有没有说明"这个 Skill 不管什么"）

**优秀示例**: huashu-design 明确"不适用场景: 生产级 Web App"，避免越界。

### 启动失败处理

13. 最关键的前提条件缺失时，Skill 是否优雅失败（而非静默卡死）？
14. 启动失败的错误信息是否告诉用户怎么修复？

---

## 本层优秀模式

| 模式 | 来源 | 说明 |
|------|------|------|
| Quick Reference 表 | self-improvement | 顶部的 "Situation → Action" 表，Agent 秒级路由 |
| Prerequisites 表 | cython-pyd-reverse | "Before starting, verify" 前置检查表 |
| 适用/不适用边界 | huashu-design | 明确写 "不适用场景" |
| 环境降级 | mcp-builder | Claude Code/Claude.ai/Cowork 三段适配 |

## 本层常见故障

1. **无入口路由**: SKILL.md 开头就是详细步骤，Agent 不知道这是不是要完整读完
2. **前提隐式**: 需要特定工具但未声明，Agent 跑到一半才发现做不了
3. **无环境区分**: 在 Claude.ai 上用了只有 Claude Code 才有的功能

## 评分指南

| 评分 | 标准 |
|------|------|
| **Strong** | 入口清晰，前提完整，环境感知，降级有路径 |
| **Adequate** | 有入口和前提声明，但环境区分不完善 |
| **Weak** | 入口模糊或前提不完整 |
| **Missing** | 无入口设计，无前提检查，Agent 无从下手 |
