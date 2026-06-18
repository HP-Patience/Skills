# 08 — 部署与运维(DevOps + Operations)

> 把项目弄上线、保持运行、出问题能恢复

## 技能点列表

- **部署三步骤**：Build(编译/打包)→Serve(运行)→Deploy(推到服务器)。关键词: build, serve, deploy, 部署流程
- **云平台对比**：Vercel(前端/Next.js最佳)、Railway(全栈简便)、Netlify(静态站)、AWS(全能但复杂)、VPS(自控但需自己配)。关键词: Vercel, Railway, Netlify, AWS, VPS, 云平台
- **PaaS vs IaaS vs VPS**：PaaS(Vercel/Railway)=上传代码就能跑，不用管服务器；IaaS(AWS EC2)=租虚拟机自己配；VPS=租独立服务器。关键词: PaaS, IaaS, SaaS
- **Docker是什么**：把应用和环境打包成一个"集装箱"，在哪都能跑，消除"我电脑上能跑啊"问题。关键词: Docker, 容器, container
- **Dockerfile/docker-compose**：Dockerfile=单容器构建说明书；docker-compose=编排多容器(如应用+数据库+Redis一起跑)。关键词: Dockerfile, docker-compose, 容器编排
- **容器 vs 虚拟机**：容器共享操作系统内核(轻量、快)、虚拟机每个有自己操作系统(重、隔离强)。关键词: 容器, 虚拟机, VM
- **CI/CD是什么**：CI=每次提交代码自动测试+构建；CD=自动部署到服务器。关键词: CI/CD, 持续集成, 持续部署, 自动化
- **GitHub Actions**：GitHub内置的CI/CD工具，在仓库里写.github/workflows/deploy.yml就能自动部署。关键词: GitHub Actions, workflow, yml
- **域名/DNS/HTTPS**：域名=网站地址(example.com)；DNS=把域名翻译成IP；HTTPS=加密传输(需要SSL证书，Let's Encrypt免费)。关键词: 域名, DNS, HTTPS, SSL, Let's Encrypt
- **环境区分**：dev(开发-天天改)→staging(预发布-和正式环境一样)→production(正式-用户在用)。关键词: dev, staging, production, 环境
- **Feature Flag/灰度发布**：Feature Flag=用开关控制新功能对哪些用户可见；灰度发布=先把新版给1%用户，没问题再推全量。关键词: feature flag, 灰度, 金丝雀发布
- **服务器基础**：CPU(算力)、内存(同时跑多少)、磁盘(存多少数据)、带宽(传输速度)。关键词: CPU, 内存, 磁盘, 服务器配置
- **进程管理**：PM2(Node.js进程守护)、systemd(Linux自带)、supervisor(Python)。进程挂了自动重启。关键词: PM2, systemd, supervisor, 进程守护
- **Nginx反向代理**：接收所有请求→根据域名/路径分发给不同后端应用。关键词: Nginx, 反向代理, 负载均衡
- **CDN是什么**：把静态文件(图片/JS/CSS)缓存到全球各地节点，用户从最近的下载。关键词: CDN, 内容分发, 加速
- **对象存储(S3/OSS)**：存图片/文件的地方，无限容量，通过URL访问。关键词: S3, OSS, 对象存储, 文件存储
- **日志与监控**：日志=记录应用运行时发生了什么；监控=图表化观测系统指标(CPU/内存/请求量)+异常告警。关键词: 日志, 监控, Prometheus, Grafana, 告警
- **数据库备份与恢复**：定时导出数据库到安全位置(不同服务器/云端)，出问题能从备份恢复。关键词: 备份, 恢复, pg_dump, 容灾
- **零停机部署**：更新代码时不停服务。做法：先启新版→等待健康检查通过→切换流量到新版→停旧版。关键词: 零停机, zero downtime, 滚动更新
- **故障排查SOP**：1)先看是不是最近刚部署了什么 2)看日志/监控面板 3)确认数据库和外部服务通不通 4)重启大法 5)回滚到上一个版本。关键词: 故障, 排查, SOP, 回滚
