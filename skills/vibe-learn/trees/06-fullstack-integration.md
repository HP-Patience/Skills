# 06 — 前后端对接

> 让前端页面和后端接口能正常通信

## 技能点列表

- **HTTP协议直觉**：浏览器(前端)发请求→服务器(后端)处理后返回响应。一次请求一次响应，无记忆。关键词: HTTP, 请求, 响应, 协议
- **JSON是什么**：前后端约定好的数据格式。长得像JS对象 `{"name":"张三","age":25}`。几乎所有现代API都用它。关键词: JSON, 数据格式, 序列化
- **序列化与反序列化**：序列化=把程序里的对象变成JSON字符串发出去；反序列化=收到的JSON字符串变回程序对象。关键词: 序列化, deserialization, parse, stringify
- **API文档怎么看**：Swagger/OpenAPI是标准格式，列出所有接口、参数、返回值，通常有在线页面可以直接测试。关键词: Swagger, OpenAPI, API文档, 接口文档
- **Postman/Insomnia怎么用**：图形化工具，填URL和方法(GET/POST)，发请求看返回。不写前端也能测试后端。关键词: Postman, Insomnia, 测试接口, API调试
- **CORS(跨域)**：浏览器安全策略。前端和后端在同一个域名下没事，不同域名默认被拦截。后端设置CORS头允许特定域名访问。关键词: CORS, 跨域, cross-origin, cors error
- **Cookie/Session/Token在前后端怎么传**：Cookie浏览器自动带；Token需要手动放请求头 `Authorization: Bearer xxx`。关键词: cookie, token, authorization, header
- **联调流程**：1)后端先把接口写好在Swagger上 → 2)前端用Postman确认接口通的 → 3)前端写代码调用 → 4)报错先看Network面板和Console。关键词: 联调, 对接, 前后端联调
- **Mock数据**：后端接口还没好时，前端自己造假数据先开发。关键词: mock, 假数据, 模拟数据
- **接口报错怎么定位**：看浏览器Network面板→看请求有没有发出去→看状态码(4xx是前端问题，5xx是后端问题)→看返回的error message。关键词: 接口报错, 排错, network, 状态码
- **请求超时与重试**：网络不好时设置超时时间(如10秒)；超时后要不要重试取决于操作是否幂等(查数据可重试，付钱不能)。关键词: timeout, 超时, 重试, retry
- **Webhook是什么**：和普通API相反。不是你去请求别人，是别人在有事件时主动请求你。用于支付通知、GitHub事件回调等。关键词: webhook, 回调, 事件通知
