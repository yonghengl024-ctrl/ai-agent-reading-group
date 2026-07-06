# 上传到 GitHub 的操作步骤

## 1. 检查资料

当前仓库只保存 Markdown、PPT、PDF、图片和资料索引。视频文件请先上传到外部平台，然后把链接写入对应章节的 `videos.md`。

## 2. 添加 PPT 或 PDF

把每章 PPT 或 PDF 放入对应目录：

```text
chapters/chapter-01/slides/
chapters/chapter-02/slides/
```

推荐文件名：

```text
chapter-01-speaker-name.pdf
chapter-01-speaker-name.pptx
```

然后在该章节的 `README.md` 和 `videos.md` 中补上链接。

## 3. 初始化本地 Git 仓库

在 `ai-agent-reading-group` 目录中执行：

```bash
git init
git add .
git commit -m "Initial AI-Agent reading group materials"
```

## 4. 在 GitHub 创建远程仓库

在 GitHub 页面新建仓库，建议名称：

```text
ai-agent-reading-group
```

如果不是官方项目，请在仓库描述中写清楚：

```text
教师共学小组 AI-Agent 学习分享资料归档，非官方教材仓库。
```

## 5. 关联远程仓库并上传

把下面命令中的 `你的用户名` 替换为你的 GitHub 用户名：

```bash
git remote add origin https://github.com/你的用户名/ai-agent-reading-group.git
git branch -M main
git push -u origin main
```

## 6. 开启 GitHub Pages

如果希望形成网页展示：

1. 进入 GitHub 仓库页面。
2. 打开 `Settings`。
3. 点击 `Pages`。
4. Source 选择 `Deploy from a branch`。
5. Branch 选择 `main`，目录选择 `/docs`。
6. 保存后等待 GitHub 生成页面链接。

