# 04 — 后端技术栈

> 写接口、处理业务逻辑、操作数据库、返回数据给前端

## 技能点列表

- **后端是什么**：运行在服务器上的代码。接收前端请求，处理数据，返回结果。关键词: 后端, server, 服务器端, 后端是什么
- **语言/框架速览**：Node.js(Express/Fastify)、Python(FastAPI/Django/Flask)、Go(Gin/Echo)、Java(Spring Boot)。关键词: Express, FastAPI, Django, Spring Boot, Gin, 后端框架, 后端语言
- **后端框架怎么选**：和AI协作最友好→Python FastAPI(类型自动生成文档)；前端转全栈→Node.js Express；高性能高并发→Go。关键词: 选后端框架, 技术选型
- **API设计(RESTful)**：一种接口命名约定。GET拿数据、POST新建、PUT/PATCH更新、DELETE删除。URL用名词复数(/users、/posts)。关键词: RESTful, API设计, REST, 接口规范
- **CRUD是什么**：Create(创建)、Read(读取)、Update(更新)、Delete(删除)——最基础的四种数据操作。关键词: CRUD, 增删改查
- **HTTP方法**：GET(请求数据)、POST(提交新数据)、PUT(全量更新)、PATCH(部分更新)、DELETE(删除)。关键词: GET, POST, PUT, DELETE, HTTP方法
- **状态码直觉**：200(成功)、201(创建成功)、301(永久重定向)、400(你的请求有问题)、401(没登录)、403(没权限)、404(找不到)、500(服务器挂了)。关键词: 状态码, status code, 200, 404, 500
- **请求与响应结构**：Request = URL + Method + Headers + Body。Response = Status Code + Headers + Body。关键词: request, response, body, header
- **路由与控制器**：路由决定"哪个URL走哪段代码"，控制器写具体处理逻辑。关键词: router, controller, 路由, 控制器
- **中间件(Middleware)**：请求到达控制器之前经历的处理链。常见：日志记录、认证检查、CORS处理。关键词: middleware, 中间件, 拦截
- **认证(Authentication) vs 授权(Authorization)**：认证=你是谁(登录)；授权=你能干什么(权限)。关键词: auth, 认证, 授权, 登录, 权限
- **JWT工作方式**：登录后服务器发一个签名的"通行证"(token)，之后每次请求带上它，服务器验证签名不验证内容。关键词: JWT, token, 令牌, 无状态认证
- **OAuth第三方登录**："用GitHub/微信/Google账号登录"。用户跳去第三方授权，拿授权码换token。关键词: OAuth, 第三方登录, 社交登录
- **Session vs Token**：Session是服务器记住你是谁(占用内存)；Token是无状态的(不占内存，适合多服务器)。关键词: session, cookie, token, 有状态, 无状态
- **文件上传处理**：前端multipart/form-data发文件→后端接收→存到本地或对象存储(S3)→数据库记路径。关键词: 文件上传, multipart, 对象存储, upload
- **数据校验(Validation)**：检查用户输入合法(邮箱格式、密码长度、必填项)。后端校验是安全的最后防线。关键词: validation, 校验, 输入校验
- **错误处理与统一返回格式**：定义统一的返回结构如{code, data, message}，所有接口错误都能预判。关键词: 错误处理, error handling, 返回格式
- **分页(Pagination)**：数据太多不分页会慢死。常见：offset分页(page+size)和cursor分页(游标，适合实时数据)。关键词: 分页, pagination, 页码, 游标
- **定时任务(Cron Job)**：定时执行的代码。如每天凌晨备份数据库、每小时清理过期token。关键词: cron, 定时任务, 计划任务, schedule
- **消息队列**：异步处理耗时任务。用户注册后发邮件不需要立即完成，扔到队列里慢慢发。Redis/BullMQ。关键词: 消息队列, queue, 异步, Redis, BullMQ
- **WebSocket**：服务器可以主动推送消息给前端。用于聊天、实时通知、股票行情。关键词: WebSocket, 实时通信, 推送, socket.io
- **API版本管理**：接口改了老用户不受影响。常见：/api/v1/users 和 /api/v2/users 并存。关键词: API版本, 版本管理, api versioning
