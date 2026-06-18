# Vibe Learn 技能树索引

当用户提问时，按关键词匹配到对应的技能树文件，然后读取该文件获取具体技能点信息进行教学。

## 索引表

| 编号 | 类别 | 文件 | 一句话 | 关键词 |
|------|------|------|--------|--------|
| 01 | 项目工程基础 | `trees/01-project-engineering.md` | 搭环境、管依赖、跑项目 | npm, pip, package.json, 环境变量, .env, 虚拟环境, venv, 脚手架, 项目初始化, 依赖, lockfile, monorepo, 构建工具, 目录结构 |
| 02 | 版本控制(Git) | `trees/02-git.md` | 管理代码版本、多人协作 | git, commit, push, pull, branch, merge, rebase, PR, pull request, 冲突, clone, .gitignore, tag, release, stash, fork, GitHub, GitLab |
| 03 | 前端技术栈 | `trees/03-frontend.md` | 做网页界面和交互 | HTML, CSS, JavaScript, React, Vue, Next.js, 组件, state, props, hooks, 路由, 状态管理, Tailwind, shadcn, TypeScript, Vite, 响应式, 样式 |
| 04 | 后端技术栈 | `trees/04-backend.md` | 写接口、处理业务逻辑 | API, RESTful, CRUD, Express, FastAPI, Django, HTTP, 接口, 后端, 认证, JWT, OAuth, 中间件, middleware, 文件上传, 分页, 定时任务, WebSocket |
| 05 | 数据库 | `trees/05-database.md` | 存储和查询数据 | 数据库, SQL, NoSQL, PostgreSQL, MySQL, MongoDB, Redis, 表, ORM, Prisma, 主键, 外键, 索引, JOIN, 事务, migration, 查询 |
| 06 | 前后端对接 | `trees/06-fullstack-integration.md` | 让前端和后端能通信 | HTTP, JSON, API文档, Swagger, Postman, CORS, 跨域, 联调, mock, 请求, 响应, 状态码, cookie, token |
| 07 | 开发范式 | `trees/07-dev-paradigms.md` | 怎么搭架构、选技术路线 | MVC, MVVM, SPA, SSR, CSR, SSG, ISR, REST, GraphQL, tRPC, 微服务, 单体, Serverless, 架构, 渲染, 范式 |
| 08 | 部署与运维 | `trees/08-deploy-ops.md` | 把项目弄上线、保持运行 | 部署, deploy, Docker, CI/CD, Vercel, Railway, Nginx, 域名, DNS, HTTPS, SSL, 服务器, 日志, 监控, 备份, 环境, production, 灰度 |
| 09 | 测试 | `trees/09-testing.md` | 验证代码是否正确 | 测试, 单元测试, 集成测试, E2E, Jest, Vitest, Pytest, Playwright, TDD, mock, 覆盖率, 断言 |
| 10 | UI/UX设计 | `trees/10-ui-ux.md` | 设计好看好用的界面 | UI, UX, 设计, Figma, 组件库, 响应式, 颜色, 字体, 间距, 可用性, 设计系统, a11y, 动效, 线框图, 高保真 |
| 11 | 安全意识 | `trees/11-security.md` | 保护项目不被攻击 | 安全, SQL注入, XSS, CSRF, 密码, 哈希, 密钥, .env, HTTPS, CORS, 权限, RBAC, 漏洞, OWASP |
| 12 | 调试与排错 | `trees/12-debugging.md` | 找出Bug并修好 | 调试, debug, 报错, error, bug, stack trace, console, DevTools, 日志, log, 断点, 排查, 二分法 |
| 13 | 产品思维 | `trees/13-product-thinking.md` | 知道做什么功能、为什么做 | 产品, PM, 需求, MVP, 用户故事, 竞品, 用户旅程, 优先级, PRD, A/B测试, Kano, 功能拆分 |
| 14 | 项目管理 | `trees/14-project-management.md` | 管进度、管任务、管协作 | 项目, 敏捷, Agile, Scrum, 看板, Kanban, Sprint, 估时, 里程碑, 甘特图, 周报, Jira, Linear, 风险 |
| 15 | CEO | `trees/15-ceo.md` | 公司战略、商业模式、融资 | CEO, 战略, 商业模式, 融资, 估值, 股权, 董事会, 融资轮次, 竞争, pitch deck, 公司治理 |
| 16 | 人力资源(HR) | `trees/16-hr.md` | 招人、管人、薪酬绩效 | HR, 招聘, 面试, 简历, 薪资, 职级, KPI, OKR, 绩效, 期权, 入职, 离职, 团队, 技术面试 |
| 17 | 财务(CFO) | `trees/17-cfo.md` | 管钱、股权激励、合规 | CFO, 财务, 报表, 预算, 成本, 利润, 现金流, 估值, 股权激励, 分红, 个税, 融资, 审计 |
| 18 | 法务 | `trees/18-legal.md` | 法律合规、协议、知识产权 | 法务, 合同, 协议, 知识产权, IP, 开源协议, MIT, GPL, 隐私, 合规, 专利, 商标, 持股平台, 公司章程 |
| 19 | 工程习惯 | `trees/19-engineering-habits.md` | 写给人看、给AI看的代码习惯 | README, commit message, 命名, 注释, 重构, 代码审查, Code Review, 技术债, DRY, 文档 |

## 使用方式

1. 用户说"我想学 Git 分支"→ 匹配关键词 `git, branch` → 文件 `trees/02-git.md` → 找到"分支管理"技能点
2. 用户说"怎么部署到 Vercel"→ 匹配关键词 `部署, vercel` → 文件 `trees/08-deploy-ops.md` → 找到"云平台"技能点
3. 用户说"React 的 useState 怎么用"→ 匹配关键词 `React, state` → 文件 `trees/03-frontend.md` → 找到"状态管理"技能点
4. 用户说"我不知道这个叫啥，但我前端页面加载很慢"→ 模糊匹配 → 可能涉及 03-frontend(性能优化) / 07-dev-paradigms(SSR) / 08-deploy-ops(CDN) → 列出选项让用户选

## 多匹配处理

当用户问题匹配到多个技能树文件时：
1. 列出匹配到的类别
2. 让用户选择最想了解的
3. 一次只教一个技能点，不要混合
