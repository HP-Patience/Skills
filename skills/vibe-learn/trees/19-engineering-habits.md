# 工程习惯

- **写README**: 项目名+一句话介绍+怎么安装+怎么跑+怎么部署,3分钟让人看懂。关键词: README, 项目文档, 安装, 部署, 快速开始
- **Commit Message规范(Conventional Commits)**: feat(新功能)、fix(修bug)、docs(文档)、refactor(重构)、chore(杂活)。格式:`type(scope): message`。关键词: commit message, Conventional Commits, feat, fix, docs, refactor, chore, 提交规范
- **命名规范直觉**: 变量用名词(userName),函数用动词(getUser),布尔用is/has开头(isActive),常量全大写API_BASE_URL。关键词: 命名规范, 变量命名, 函数命名, 布尔命名, 常量命名, camelCase, UPPER_CASE
- **注释原则**: Why > What(解释为什么要这样做而不是做了什么)。别写`// add 1 to i`这种废话。关键词: 注释, 代码注释, Why注释, 注释原则
- **DRY vs WET**: Don't Repeat Yourself(三次重复就抽象) vs Write Everything Twice(两次重复可以忍,别过度抽象)。关键词: DRY, WET, 代码复用, 抽象, 过度抽象, 重复代码
- **代码审查清单**: 逻辑对了吗?安全吗?有测试吗?命名清楚吗?有文档吗?关键词: 代码审查, code review, 检查清单, 逻辑, 安全, 测试, 命名, 文档
- **Code Review心态**: 不是被审判人格,是让代码更好。改的是代码不是你。关键词: Code Review心态, 代码审查心态, 反馈, 改进
- **技术文档什么时候写**: 接口文档在写代码前写(先约定);架构文档在搭好骨架后写;操作手册在发布前写。关键词: 技术文档, API文档, 架构文档, 操作手册, 文档时机
- **技术债务概念**: 为了快速上线做的妥协(没写测试/没优化/代码丑),以后要还。关键词: 技术债务, tech debt, 快速上线, 妥协, 重构
- **重构是什么**: 不改外部行为只改内部结构。提变量名、拆函数、去重复。关键词: 重构, refactoring, 内部结构, 提取变量, 拆分函数, 去重复
- **结对编程**: 两人共用一台电脑写代码。一个写(Driver),一个想(Navigator)。关键词: 结对编程, pair programming, Driver, Navigator, 协作
- **AI协作心智模型**: AI是你的加速引擎,不是自动驾驶。你做决策(用什么技术/怎么设计),AI做执行(写代码/写测试/写文档)。关键词: AI协作, 心智模型, 加速引擎, 自动驾驶, 人类决策, AI执行
- **持续学习路径**: 做一个完整项目 > 看100个教程。学新东西的时候边做边学最有效。关键词: 持续学习, 项目驱动, 边做边学, learning by doing, 教程
