# 02 — 版本控制(Git)

> 管理代码版本，多人协作，不怕改崩

## 技能点列表

- **Git是什么**：分布式版本控制系统。记录每次修改快照，随时回退、合并。关键词: git, 版本控制, 版本管理
- **基本操作**：git init(创建仓库)、git clone(下载远程仓库)、git add(暂存修改)、git commit(提交快照)、git push(上传到远程)、git pull(拉取远程更新)。关键词: git init, git clone, git add, git commit, git push, git pull, 基本命令
- **.gitignore怎么写**：告诉Git哪些文件不要追踪(密钥、node_modules、编译产物)。关键词: .gitignore, 忽略文件, 不提交
- **分支(branch)**：独立开发线。主分支(main/master)是稳定版，功能分支(feature branch)做新功能，改完合并回去。关键词: branch, 分支, checkout, feature branch, 功能分支
- **合并(merge vs rebase)**：merge保留完整历史，rebase让历史变成一条线。日常用merge，想要干净历史用rebase。关键词: merge, rebase, 合并, 变基
- **冲突解决**：两个人改了同一行代码，Git不知道听谁的，需要你手动决定。关键词: conflict, 冲突, merge conflict, 解决冲突
- **Pull Request(PR) / Merge Request(MR)**：合并前让别人过目你的代码。GitHub叫PR，GitLab叫MR。关键词: PR, pull request, merge request, 代码评审
- **Code Review怎么做**：不是找茬。检查代码逻辑、安全、可读性。关键词: code review, 审查, review
- **协作模型**：Git Flow(复杂，适合有版本发布)、GitHub Flow(简单，main+feature分支)、Trunk-Based(直接推main，用feature flag)。关键词: git flow, github flow, trunk-based, 协作流程
- **tag与release**：tag是Git里的版本标记(v1.0.0)，release是GitHub上的打包发布。关键词: tag, release, 版本发布, semantic versioning
- **救火命令**：git reset(撤销commit)、git revert(安全撤销，产生新commit)、git stash(暂存未完成的修改)、git cherry-pick(挑一个commit到当前分支)。关键词: reset, revert, stash, cherry-pick, 撤销, 回退
- **GitHub/GitLab/Gitee差异**：都是Git的云存储平台，核心操作一样，CI/CD配置各有格式。关键词: github, gitlab, gitee
