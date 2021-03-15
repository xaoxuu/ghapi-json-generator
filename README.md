# github-api

一个通过定时缓存 GitHub API 数据并提供加速访问的工具，解决了直接调用 GitHub API 频率有限制以及速度过慢的问题。

示例：https://gh-api.xaoxuu.com/v1/users?target=xaoxuu

## 使用方法

1. 把本仓库 fork 到您的 GitHub 中
2. 修改 `config.yml` 中的配置信息
3. 前往 Actions 页面，点击允许运行
4. 点击 star 以主动触发 Action 进行测试

等待 Action 运行完毕，生成 output 路径以及文件就说明配置成功了。

> 为了方便更新，请不要直接使用 fork 的仓库作为数据来源仓库，而仅仅作为缓存仓库，当 API 更新时，直接删掉并重新 fork 就可以了。

## API 文档

### users

```
https://gh-api.xaoxuu.com/v1/users?source={owner/repo}&target={owner}
```

> 自己部署 API 可以省略 `source` 参数

### contributors

```
https://gh-api.xaoxuu.com/v1/contributors?source={owner/repo}&target={owner/repo}
```

示例：https://gh-api.xaoxuu.com/v1/contributors?source=xaoxuu/github-api&target=xaoxuu/hexo-theme-stellar

### releases

```
https://gh-api.xaoxuu.com/v1/releases?source={owner/repo}&target={owner/repo}
```

示例：https://gh-api.xaoxuu.com/v1/releases?source=xaoxuu/github-api&target=xaoxuu/hexo-theme-stellar

### issues

```
https://gh-api.xaoxuu.com/v1/issues?source={owner/repo}&target={owner/repo}
```

示例：https://gh-api.xaoxuu.com/v1/issues?source=xaoxuu/github-api&target=xaoxuu/hexo-theme-stellar

## 自己部署 API 可以缩短链接

修改配置文件中的 `source_repo` 并以您 fork 的仓库为源码创建 Vercel App，请求您的 API 时可以省略 `source` 参数：

```
https://github-api-yourname.vercel.app/v1/users?target={owner}
https://github-api-yourname.vercel.app/v1/contributors?target={owner/repo}
https://github-api-yourname.vercel.app/v1/releases?target={owner/repo}
https://github-api-yourname.vercel.app/v1/issues?target={owner/repo}
```
