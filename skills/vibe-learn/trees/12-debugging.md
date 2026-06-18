# 调试与排错

- **调试心态**: bug是常态不是失败，每个bug都能被找到。不要焦虑、不要猜、不要乱改。冷静读报错→定位→验证→修复，有系统地来。 关键词: 调试心态、系统性排查、冷静排错、debug方法论
- **读报错信息方法论**: 从最后一行往前读。最后一行通常是最直接的错误描述。先看错误类型(SyntaxError/TypeError/ReferenceError)→再看出错文件名和行号→最后看调用链。 关键词: 报错阅读、错误类型、行号定位、错误栈、错误描述
- **Stack Trace怎么看**: 函数调用链从外到内排列，最上面的行是入口，最底下的行是触发错误的实际位置。从下往上找到你自己写的代码处，那才是你需要修的地方。 关键词: Stack Trace、调用栈、调用链、堆栈跟踪、错误定位
- **浏览器DevTools**: Console看报错和日志、Network看请求状态码和响应体、Application看localStorage/sessionStorage/cookie、Elements看DOM结构和CSS。F12打开的万能工具箱。 关键词: DevTools、F12、Console、Network、Chrome开发者工具
- **后端日志怎么打怎么看**: 开发时console.log/print足够。生产环境用日志库(winston/loguru)，按级别(debug/info/warn/error)分类，关键节点(请求进来、数据库操作、异常)必须打日志。 关键词: 日志、winston、loguru、日志级别、关键节点
- **二分法定位问题**: 注释掉一半代码→还报错？注释另一半→不断缩小区间，直到精确定位到某一行。适用于任何"以前好好的突然坏了"的场景。 关键词: 二分法、代码注释、缩小范围、定位bug、快速排查
- **排除法**: 先确认不是外部因素：网络通不通？数据库连不连通？环境变量配了没？文件权限对不对？端口被占没？这些外部问题最容易被忽略。 关键词: 排除法、外部因素、环境检查、网络排查、权限检查
- **git bisect找到坏commit**: git bisect start→git bisect bad标记当前有问题→git bisect good 某次正常的commit→git自动二分切换commit给你测试→直到定位引入bug的commit。 关键词: git bisect、二分定位、commit回溯、版本定位、回归bug
- **如何向AI描述Bug**: 描述症状(什么情况下出什么错)+贴完整报错日志+说你用的技术栈和版本+你已经试过什么。越具体AI越能帮你，别只说"不行了"。 关键词: AI调试、bug描述、报错日志、问题描述、提问技巧
- **搜索报错信息**: Google搜完整错误信息(去掉文件名和路径)→优先看GitHub Issues和官方文档→其次StackOverflow→看回答的时间，太老的方案可能过时。 关键词: 报错搜索、Google、GitHub Issues、StackOverflow、搜索技巧
- **本地能跑服务器不行**: 逐项排查：环境变量是否一致、Node/Python版本是否相同、数据库连接串是否正确、文件路径大小写(本地Windows不区分服务器Linux区分)、端口防火墙。 关键词: 环境差异、部署排查、路径大小写、版本一致、环境变量
- **前端调试**: F12打开DevTools→Network看接口返回的状态码(4xx前端问题5xx后端问题)和响应体→Console看JS报错→Application看cookie/token是否过期。 关键词: 前端调试、接口调试、状态码、Console、Network面板
- **后端调试**: 加日志打印关键变量→用curl/Postman直接打接口拿原始响应→看数据库是否实际写入了数据→逐层排查(路由层→业务层→数据层)。 关键词: 后端调试、curl、Postman、数据库验证、分层排查
- **常见错误类型**: Syntax(语法写错,括号/引号/缩进不对)→Runtime(运行时崩,null/undefined/类型错误)→Logic(代码能跑但结果不对,算法逻辑问题)→Network(连不上,超时,CORS)。 关键词: 错误分类、Syntax、Runtime、Logic、Network
