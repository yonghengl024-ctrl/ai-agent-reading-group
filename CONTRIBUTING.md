# 资料提交说明

## 第一期教材导读资料

每章资料放在 `chapters/chapter-XX/` 目录下：

- `README.md`：章节概览、讲解信息、教材链接和资料入口
- `videos.md`：讲解视频链接
- `slides/`：PPT、PDF 或 HTML 演示文稿
- `examples/`：可选，实践案例、代码和示例数据
- `notes.md`：可选，有正式内容时再添加学习笔记

## 后续专题分享资料

教材学习完成后的其他 AI-Agent 分享内容放在 `topics/` 目录下。每个专题建议单独建一个目录：

```text
topics/topic-name/
├── README.md
├── videos.md
├── slides/
└── examples/
```

专题目录名建议稳定、简短，优先使用英文或拼音。专题 `README.md` 中应说明主题、分享人、资料入口、适用场景和必要的引用来源。

## 文件命名

建议使用清晰、稳定的英文文件名，避免不同系统之间的编码问题：

```text
chapter-01-speaker-name.pdf
chapter-01-speaker-name.pptx
```

如果需要保留中文标题，也建议加上章节编号：

```text
chapter-01-智能体概览与本书导读.pdf
```

## 视频文件

请不要直接提交 `.mp4`、`.mov`、`.mkv` 等大视频文件。先上传到外部平台，再把链接写入对应章节或专题的 `videos.md`。

## 版权与授权

提交资料前请确认：

1. PPT 是否可以公开下载。
2. 视频是否可以公开观看。
3. 是否包含学生信息、会议聊天记录、未授权图片或其他敏感内容。
4. 是否需要隐藏讲解人联系方式。
