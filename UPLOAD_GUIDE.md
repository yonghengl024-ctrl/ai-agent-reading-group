# 资料上传与更新指南

本指南说明如何向本仓库补充 AI-Agent 使用介绍与实践资料，包括 PPT/PDF、视频链接、章节说明和实践笔记。

## 上传前检查

提交资料前请确认：

1. PPT/PDF 可以公开或在本仓库中共享。
2. 视频链接可以公开访问，且有效期尽量设置为永久有效。
3. 资料中不包含学生信息、会议聊天记录、私人联系方式或未授权图片。
4. 视频文件不要直接上传到 GitHub，应先上传到百度网盘、Bilibili、阿里云盘或其他外部平台。

## 文件放置位置

每章资料放在对应章节目录中：

```text
chapters/chapter-XX/
├── README.md
├── videos.md
├── slides/
└── examples/   # 可选
```

常见更新位置：

| 内容 | 文件位置 |
|---|---|
| PPT/PDF | `chapters/chapter-XX/slides/` |
| 视频链接 | `chapters/chapter-XX/videos.md` |
| 讲解人、教材链接、资料说明 | `chapters/chapter-XX/README.md` |
| 实践案例、代码、示例数据 | `chapters/chapter-XX/examples/` |
| 学习笔记 | 有正式内容时添加 `chapters/chapter-XX/notes.md` |

## PPT/PDF 命名建议

建议使用清晰稳定的文件名：

```text
chapter-01-ai-agent-overview.pdf
chapter-01-ai-agent-overview.pptx
```

如果保留中文标题，也建议带上章节编号：

```text
chapter-01-智能体概览与本书导读.pdf
```

## 视频链接填写方式

视频不要直接上传到 GitHub。请先上传到外部平台，然后修改对应章节的 `videos.md`。

示例：

```markdown
| 讲解人 | 视频链接 | PPT |
|---|---|---|
| xxx | [百度网盘](https://pan.baidu.com/s/xxxx?pwd=abcd) | [PDF](./slides/chapter-01-ai-agent-overview.pdf) |
```

如果 PPT 还没有上传，可以用 `-` 标记：

```markdown
| xxx | [百度网盘](https://pan.baidu.com/s/xxxx?pwd=abcd) | - |
```

## 有写权限的上传流程

如果你已经被加入为 collaborator，并且拥有 `Write` 权限，可以直接提交到本仓库。

第一次操作：

```bash
git clone https://github.com/yonghengl024-ctrl/ai-agent-reading-group.git
cd ai-agent-reading-group
```

每次更新资料：

```bash
git pull
git add .
git commit -m "Update chapter XX materials"
git push
```

提交信息建议写清楚更新内容，例如：

```bash
git commit -m "Add chapter 01 slides"
git commit -m "Update chapter 08 video link"
git commit -m "Add chapter 12 notes"
```

## 没有写权限的上传流程

如果你没有本仓库写权限，请通过 Fork 和 Pull Request 提交。

网页操作流程：

1. 打开仓库页面。
2. 点击右上角 `Fork`，复制一份到自己的 GitHub 账号。
3. 在自己的 Fork 仓库中上传或修改文件。
4. 提交修改后点击 `Contribute`。
5. 点击 `Open pull request`。
6. 按模板说明本次更新内容。
7. 等待仓库维护者审核并合并。

命令行操作流程：

```bash
git clone https://github.com/你的用户名/ai-agent-reading-group.git
cd ai-agent-reading-group
git checkout -b update-chapter-XX
```

修改文件后：

```bash
git add .
git commit -m "Update chapter XX materials"
git push -u origin update-chapter-XX
```

然后回到 GitHub 页面创建 Pull Request。

## 不建议上传的内容

请不要上传：

- `.mp4`、`.mov`、`.mkv` 等视频文件
- 未授权转载的图片、教材全文或第三方课件
- 包含个人隐私或会议内部信息的文件
- 与 AI-Agent 使用介绍无关的资料

仓库已经通过 `.gitignore` 忽略常见视频格式，但提交前仍建议检查一次：

```bash
git status
```
