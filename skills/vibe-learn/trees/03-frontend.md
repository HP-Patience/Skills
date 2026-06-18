# 03 — 前端技术栈

> 做网页界面和交互：HTML结构、CSS样式、JavaScript行为

## 技能点列表

- **HTML/CSS/JavaScript三者关系**：HTML是骨架(放什么内容)，CSS是皮肤(长什么样)，JS是肌肉(做什么动作)。关键词: HTML, CSS, JavaScript, 三者关系
- **DOM是什么**：浏览器把HTML解析成一棵树，JS可以操作这棵树改变页面。关键词: DOM, document, 页面结构
- **前端框架为什么存在**：原生JS操作DOM太麻烦，框架帮你自动同步数据和页面。关键词: 前端框架, React, Vue, 为什么用框架
- **React核心概念**：组件(UI积木块)、JSX(HTML写在JS里)、state(组件记忆)、props(父子传值)、hooks(给函数组件加能力)。关键词: React, 组件, JSX, state, props, hooks, useState, useEffect
- **Vue核心概念**：模板(HTML+指令)、响应式数据(ref/reactive)、组合式API(setup)。关键词: Vue, 模板, ref, reactive, 组合式API, SFC
- **Next.js是什么**：React的增强版框架。集成路由、SSR、SSG、API路由，省去手搭脚手架。关键词: Next.js, SSR, App Router, 服务器端渲染
- **怎么选框架**：快速上线选Next.js(全栈React框架)；轻量交互选Vue；要生态成熟选React。不确定就Next.js。关键词: 选框架, React还是Vue, 技术选型
- **组件化思维**：页面拆成独立可复用的小块。每个组件只做一件事。关键词: 组件, component, 复用, 拆组件, 单一职责
- **状态管理**：组件自己的数据用useState；多个组件共享用Context/Zustand；全局复杂状态用Redux/Pinia。关键词: 状态管理, useState, Redux, Zustand, Pinia, 全局状态, context
- **路由**：URL和页面的映射关系。用户访问/about就显示关于页。前端路由不刷新整页。关键词: 路由, router, react-router, next-router, vue-router
- **样式方案对比**：CSS Modules(组件隔离)、Tailwind(原子化class)、shadcn/ui(Tailwind组件库，复制粘贴使用)、SCSS(CSS增强版)。关键词: 样式, CSS, Tailwind, shadcn, CSS Modules, SCSS
- **响应式设计**：网页自动适应手机/平板/电脑屏幕。核心用@media查询或Tailwind的sm/md/lg断点。关键词: 响应式, responsive, 移动端, 断点, breakpoint, media query
- **API调用**：fetch(原生)、axios(老牌库)、react-query/SWR(缓存+自动刷新)。关键词: fetch, axios, API调用, 数据获取, react-query
- **表单处理**：react-hook-form(性能好)、formik(老牌)。核心：校验→提交→反馈。关键词: 表单, form, 校验, validation, react-hook-form
- **前端存储**：localStorage(持久存)、sessionStorage(关标签页就丢)、cookie(会自动发给服务器)。关键词: localStorage, sessionStorage, cookie, 前端存储
- **TypeScript是什么**：带类型检查的JavaScript。写代码时帮你发现"把字符串当数字用"这种低级错误。关键词: TypeScript, TS, 类型, type, interface
- **构建工具**：Vite(新一代，开发快)、Webpack(老牌稳定)、Turbopack(Rust写的极速构建)。关键词: Vite, Webpack, build, 打包, 构建
- **HMR(热更新)**：改代码后页面自动刷新，不用手动F5。关键词: HMR, 热更新, hot reload
- **前端性能优化**：图片懒加载、代码分割、减少请求数、压缩资源。关键词: 性能优化, 懒加载, 代码分割, lighthouse
