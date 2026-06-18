# 01 — 项目工程基础

> 把代码跑起来的第一步：装依赖、配环境、建项目骨架

## 技能点列表

- **包管理器**：管理项目依赖的工具。npm(Node.js)、pip(Python)、cargo(Rust)、pnpm/yarn(npm替代品)。关键词: npm, pip, 安装依赖, package.json, requirements.txt
- **package.json解读**：Node.js项目的身份证。记录项目名、版本、依赖、启动脚本。关键词: package.json, dependencies, devDependencies, scripts
- **requirements.txt / pyproject.toml**：Python项目的依赖清单。关键词: pip install, requirements, pyproject
- **项目初始化与脚手架**：一键生成项目骨架的命令。create-react-app、vite create、create-next-app、django-admin。关键词: 脚手架, 初始化项目, create, init, 新建项目
- **环境变量(.env)**：存放敏感配置(密钥、密码、数据库地址)的文件，不提交到Git。关键词: .env, 环境变量, 配置, API密钥, 数据库地址
- **虚拟环境**：为每个Python项目创建独立依赖空间，防止A项目污染B项目。venv/conda。Node.js用nvm管理Node版本。关键词: venv, conda, nvm, 虚拟环境, 隔离
- **依赖锁定文件**：锁死依赖版本，防止"在我电脑上能跑"。package-lock.json / yarn.lock / poetry.lock / Pipfile.lock。关键词: lockfile, 版本锁定, 依赖冲突
- **项目目录结构规范**：常见约定——src放源码、tests放测试、docs放文档、public放静态文件。关键词: 目录结构, src, components, utils, 项目结构
- **monorepo vs polyrepo**：一个仓库管多个项目 vs 每个项目一个仓库。关键词: monorepo, turborepo, 多项目, workspace
- **本地开发 vs 生产环境**：开发用hot-reload+假数据，生产要压缩+优化。关键词: development, production, 构建, build, 环境差异
- **构建工具概览**：前端：Vite(新快)、Webpack(老稳)、Turbopack(新生)。Python不用构建。关键词: 构建工具, build tool, bundler
