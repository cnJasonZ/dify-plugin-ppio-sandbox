## PPIO Sandbox

### 介绍

这是一个用于 Dify 的插件，用于集成 [PPIO Agent 沙箱](https://ppio.com/ai-computing/sandbox?utm_source=github_dify&utm_medium=github_readme&utm_campaign=link)。它兼容 E2B API，提供安全隔离的云端沙箱，用于执行 AI 生成的任务。

### 功能

- 在 PPIO Agent 沙箱中运行代码。支持 Python 和 JavaScript 代码。
- 在 PPIO Agent 沙箱中运行 Linux 命令。
- 上传文件到 PPIO Agent 沙箱。需要一个已存在的沙箱 ID。
- 从 PPIO Agent 沙箱下载文件。需要一个已存在的沙箱 ID。

### Usage

1. 从 Dify 的 marketplace 安装插件。

2. 安装完成后，将插件添加到您的 workflow 中。

![](_assets/ppio-01.png)

3. [注册 PPIO 账号](https://ppio.com/user/register?invited_by=JXATT3&utm_source=github_dify&utm_medium=github_readme&utm_campaign=link)
4. 创建并保存您的 API 密钥 [这里](https://ppio.com/settings/key-management?utm_source=github_dify&utm_medium=github_readme&utm_campaign=link)。
   - 点击您的 [用户头像] → [API 密钥管理] 访问控制台。
     ![](_assets/ppio-02.png)
   - 点击 **创建** 生成新的 API 密钥。自定义名称，并注意该密钥 **在生成后只会显示一次** — 确保复制并安全保存，以确保未来可以持续使用。
     ![](_assets/ppio-03.png)

5. 在 Dify 的 workflow 中，点击 **API Key 授权配置** 按钮，粘贴您刚刚保存的 PPIO API 密钥，并点击 **保存** 按钮。
   ![](_assets/ppio-04.png)
   ![](_assets/ppio-05.png)

6. 现在您可以在您的 workflow 中使用 PPIO Agent 沙箱，或者在其他应用中使用。

该插件的源代码：[https://github.com/cnJasonZ/dify-plugin-ppio-sandbox](https://github.com/cnJasonZ/dify-plugin-ppio-sandbox)
