# github-api

一个通过定时缓存 GitHub API 数据并提供加速访问的工具，解决了直接调用 GitHub API 频率有限制以及速度过慢的问题。

## 使用方法

把本仓库 fork 到您的 GitHub 中，然后修改 `config.yml` 中的配置信息，点击 star 以触发 Action，等待 Action 运行完毕，生成 output 路径以及文件即配置成功。

## 直接请求

https://github-api-xaoxuu.vercel.app/v1/contributors?api=xaoxuu/github-api&repo=xaoxuu/hexo-theme-stellar
https://github-api-xaoxuu.vercel.app/v1/releases?api=xaoxuu/github-api&repo=xaoxuu/hexo-theme-stellar

## 自己部署缩短链接

以您 fork 的仓库为源码创建 Vercel App：

```
https://github-api-yourname.vercel.app/v1/contributors?repo=xaoxuu/hexo-theme-stellar
https://github-api-yourname.vercel.app/v1/releases?repo=xaoxuu/hexo-theme-stellar
```
