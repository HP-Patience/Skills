# 07 — 开发范式

> 知道怎么搭架构、选渲染策略、选通信方式

## 技能点列表

- **MVC/MVVM概念**：MVC=Model(数据)+View(界面)+Controller(逻辑协调)；MVVM多一个ViewModel自动同步View和Model。不用深究，框架已经帮你实现了。关键词: MVC, MVVM, 架构模式
- **三层架构**：表现层(Controller)→业务层(Service)→数据层(Repository/DAO)。每层只干自己的事，不跨层调用。关键词: 三层架构, 分层, controller, service, repository
- **SPA vs MPA**：SPA(单页应用)=一个HTML，页面切换不刷新，用户体验流畅。MPA(多页应用)=每个页面独立HTML，SEO好。关键词: SPA, MPA, 单页应用, 多页应用
- **CSR/SSR/SSG/ISR**：CSR=浏览器渲染(慢首屏)；SSR=服务器渲染好HTML(快首屏，SEO好)；SSG=构建时生成静态HTML(最快)；ISR=SSG+按需重新生成。关键词: CSR, SSR, SSG, ISR, 渲染, 首屏
- **怎么选渲染策略**：需要SEO→SSR/SSG；纯后台系统→CSR；内容网站→SSG；两者都要→Next.js ISR。关键词: 选渲染, Next.js, 渲染策略
- **REST vs GraphQL vs tRPC**：REST=多个固定接口(最通用)；GraphQL=一个接口，前端指定要什么数据(灵活但复杂)；tRPC=前后端共享类型，直接调函数(全栈TS首选)。关键词: REST, GraphQL, tRPC, 接口风格
- **BFF(Backend For Frontend)**：为每种前端(Web/iOS/Android)各写一个专用后端层，避免一个接口服务所有端导致数据冗余。关键词: BFF, 后端即前端
- **微服务 vs 单体**：单体=所有功能一个大项目(小团队首选)；微服务=拆成独立小服务(大团队需要但复杂度暴增)。小项目用单体，别上来就微服务。关键词: 微服务, 单体, 架构选型
- **Serverless**：不用管服务器，写函数上传到平台(AWS Lambda/Vercel Functions)，按调用次数付费。关键词: Serverless, 无服务器, lambda, function
- **事件驱动架构**：系统通过事件通信而不是直接调用。用户注册→触发"注册事件"→各模块(发邮件/统计/推荐)各自响应。关键词: 事件驱动, event-driven, 解耦
- **CQRS(读写分离直觉)**：读操作和写操作用不同的模型/数据库。读用Redis缓存加速，写用主库保证一致。关键词: CQRS, 读写分离
- **面向对象(OOP) vs 函数式(FP)**：OOP=数据和方法绑在一起(class)；FP=数据是数据，函数是函数，强调不可变。不用刻意学，React偏向FP，Java偏OOP。关键词: OOP, FP, 面向对象, 函数式
- **设计模式是什么**：解决常见问题的代码模板。开局知道有这个东西就行，遇到具体场景让AI推荐模式。关键词: 设计模式, design pattern
