# github-api

一个通过定时缓存 GitHub API 数据的工具，解决了直接调用 GitHub API 频率有限制以及速度过慢的问题。


## 使用方法

1. 把本仓库 fork 到您的 GitHub 中。
2. 修改 `config.yml` 中的配置信息。
3. 前往 Actions 页面，点击绿色的「enable workflows」按钮。
4. 刷新 Actions 页面，点击左侧「Generator」选项卡，再点击右侧的「enable workflow」按钮。
4. 点击 Star 以主动触发 Action 进行测试。

等待 Action 运行完毕，生成 output 路径以及文件就说明配置成功了。

> 为了方便更新，请不要直接使用 fork 的仓库作为数据来源仓库，而仅仅作为缓存仓库，当 API 更新时，直接删掉并重新 fork 就可以了。
