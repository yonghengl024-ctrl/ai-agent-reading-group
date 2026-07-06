# AI-Agent 教材共学分享资料库

本仓库用于整理教师共学小组围绕 AI-Agent 相关教材开展共学、汇报和讨论过程中形成的资料，包括章节教材链接、汇报视频、PPT/PDF、学习笔记、讨论问题和延伸阅读。

项目目标不是替代原教材，而是把共学过程中分散在网盘、会议记录和个人文件夹中的资料整理成一个结构稳定、便于检索、方便协作和可以长期引用的公开资料索引。

参考教材网站：

- https://ailingnan.xueheng.site:8000
- https://ai.lingnan.top/book/

> 说明：本仓库为学习交流资料归档，非教材官方网站或官方课程仓库。教材正文、更新和解释请以原教材网站为准。

## 快速入口

| 入口 | 说明 |
|---|---|
| [网页入口](https://yonghengl024-ctrl.github.io/ai-agent-reading-group/) | GitHub Pages 版资料导航 |
| [章节资料](#内容导航) | 按教材章节浏览 PPT、视频链接和笔记 |
| [上传指南](./UPLOAD_GUIDE.md) | 本地资料提交到 GitHub 的操作步骤 |
| [贡献说明](./CONTRIBUTING.md) | 文件命名、视频链接、版权检查要求 |
| [常见问题](./FAQ.md) | 视频、PPT、版权和 GitHub Pages 相关问题 |
| [汇报人](./speakers/) | 维护可公开的汇报人信息 |

## 项目背景

AI-Agent 相关工具和方法正在快速进入教学、科研、办公自动化、知识管理和实证研究等场景。教师共学小组围绕 AI-Agent 教材按章节开展阅读、汇报和实践分享，希望通过系统化归档降低重复学习成本，并为后续课程建设、科研协作和教学培训提供可复用材料。

本项目重点关注三个问题：

1. 如何把每章教材内容转化为可讨论、可复习的学习材料。
2. 如何把汇报视频、PPT、笔记和教材链接放在同一个稳定入口中。
3. 如何让不同参与者可以持续补充资料，同时保留清晰的版权和协作边界。

## 适用对象

本仓库适合以下使用者：

- 正在学习 AI-Agent 教材的教师、学生和研究者
- 希望快速定位某一章视频、PPT 或教材链接的共学成员
- 准备组织 AI-Agent 读书会、工作坊或课程讨论的团队
- 希望参考 AI-Agent 在教学、办公、知识库、投研和实证研究中应用案例的学习者

## 资料结构

仓库按章节组织资料，每一章对应一个目录：

```text
chapters/chapter-XX/
├── README.md   # 章节概览、汇报信息、教材链接
├── videos.md   # 汇报视频链接
├── notes.md    # 学习笔记、要点、讨论问题
└── slides/     # PPT 或 PDF
```

根目录中的主要文件：

| 文件 | 作用 |
|---|---|
| `README.md` | 项目主页和章节总目录 |
| `UPLOAD_GUIDE.md` | 上传到 GitHub 的操作步骤 |
| `CONTRIBUTING.md` | 资料提交规范 |
| `FAQ.md` | 常见问题 |
| `LICENSE` | 授权和版权说明 |
| `CITATION.cff` | 引用信息 |
| `docs/index.md` | GitHub Pages 展示页 |

## 当前进度

| 内容 | 状态 |
|---|---|
| 章节目录 | 已覆盖第 1 到第 23 章 |
| 教材链接 | 已补充 |
| 汇报视频链接 | 部分已补充 |
| PPT/PDF | 待上传 |
| 学习笔记 | 待完善 |
| GitHub Pages | 已开启 |

仍待补充视频链接的章节：

```text
第8章、第15章、第16章、第20章、第21章、第22章、第23章
```

## 内容导航

| 章节 | 主题 | 资料入口 | 教材 |
|---|---|---|---|
| 第 1 章 | 智能体概览与本书导读 | [进入](./chapters/chapter-01/) | [教材](https://ai.lingnan.top/book/chapters/chapter-1/) |
| 第 2 章 | 人机协作范式 | [进入](./chapters/chapter-02/) | [教材](https://ai.lingnan.top/book/chapters/chapter-2/) |
| 第 3 章 | 智能体框架安装与配置 | [进入](./chapters/chapter-03/) | [教材](https://ai.lingnan.top/book/chapters/chapter-3/) |
| 第 4 章 | 项目创建与规则文件 | [进入](./chapters/chapter-04/) | [教材](https://ai.lingnan.top/book/chapters/chapter-4/) |
| 第 5 章 | 提示词工程与任务规划 | [进入](./chapters/chapter-05/) | [教材](https://ai.lingnan.top/book/chapters/chapter-5/) |
| 第 6 章 | Git 与版本控制 | [进入](./chapters/chapter-06/) | [教材](https://ai.lingnan.top/book/chapters/chapter-6/) |
| 第 7 章 | Skills 基础 | [进入](./chapters/chapter-07/) | [教材](https://ai.lingnan.top/book/chapters/chapter-7/) |
| 第 8 章 | 多智能体基础：子代理 | [进入](./chapters/chapter-08/) | [教材](https://ai.lingnan.top/book/chapters/chapter-8/) |
| 第 9 章 | Skills 进阶 | [进入](./chapters/chapter-09/) | [教材](https://ai.lingnan.top/book/chapters/chapter-9/) |
| 第 10 章 | 智能体知识库设计 | [进入](./chapters/chapter-10/) | [教材](https://ai.lingnan.top/book/chapters/chapter-10/) |
| 第 11 章 | 多智能体进阶：Agent Teams | [进入](./chapters/chapter-11/) | [教材](https://ai.lingnan.top/book/chapters/chapter-11/) |
| 第 12 章 | Hooks | [进入](./chapters/chapter-12/) | [教材](https://ai.lingnan.top/book/chapters/chapter-12/) |
| 第 13 章 | 评估与迭代 | [进入](./chapters/chapter-13/) | [教材](https://ai.lingnan.top/book/chapters/chapter-13/) |
| 第 14 章 | 高阶使用技巧 | [进入](./chapters/chapter-14/) | [教材](https://ai.lingnan.top/book/chapters/chapter-14/) |
| 第 15 章 | 自动化办公工作台 | [进入](./chapters/chapter-15/) | [教材](https://ai.lingnan.top/book/chapters/chapter-15/) |
| 第 16 章 | 金融多源知识库开发实战 | [进入](./chapters/chapter-16/) | [教材](https://ai.lingnan.top/book/chapters/chapter-16/) |
| 第 17 章 | 多智能体投研系统 | [进入](./chapters/chapter-17/) | [教材](https://ai.lingnan.top/book/chapters/chapter-17/) |
| 第 18 章 | 文献综述智能体系统 | [进入](./chapters/chapter-18/) | [教材](https://ai.lingnan.top/book/chapters/chapter-18/) |
| 第 19 章 | AI 原生知识管理系统 | [进入](./chapters/chapter-19/) | [教材](https://ai.lingnan.top/book/chapters/chapter-19/) |
| 第 20 章 | AI 智能体与经济学实证研究 | [进入](./chapters/chapter-20/) | [教材](https://ai.lingnan.top/book/chapters/chapter-20/) |
| 第 21 章 | OpenClaw 入门：安装部署与首次对话 | [进入](./chapters/chapter-21/) | [教材](https://ai.lingnan.top/book/chapters/chapter-21/) |
| 第 22 章 | OpenClaw 架构：工作区、记忆与运行机制 | [进入](./chapters/chapter-22/) | [教材](https://ai.lingnan.top/book/chapters/chapter-22/) |
| 第 23 章 | OpenClaw 实战：管家调度专家 | [进入](./chapters/chapter-23/) | [教材](https://ai.lingnan.top/book/chapters/chapter-23/) |

## 资料类型

- **教材链接**：指向每一章原教材页面，便于对照阅读。
- **汇报视频**：保存为外部平台链接，当前主要使用百度网盘。
- **PPT/PDF**：每章汇报材料，建议优先上传 PDF，必要时同时保留 PPTX。
- **学习笔记**：整理核心概念、实践要点、讨论问题和延伸阅读。
- **协作记录**：通过 Issue 和 Pull Request 维护链接失效、资料更新和补充建议。

## 视频存放建议

视频文件通常较大，不建议直接提交到 GitHub 仓库。建议将视频上传到 Bilibili、腾讯会议回放、百度网盘、阿里云盘、YouTube 或对象存储服务，然后在对应章节的 `videos.md` 中维护链接。

本仓库的 `.gitignore` 已默认忽略常见视频格式，避免误提交大文件。

## 推荐贡献流程

1. 将 PPT 或 PDF 放到对应章节的 `slides/` 目录。
2. 将视频上传到外部平台。
3. 在对应章节的 `videos.md` 中补充视频链接。
4. 在对应章节的 `README.md` 中补充汇报人、日期和 PPT 链接。
5. 如有必要，在 `notes.md` 中补充本章要点、讨论问题和延伸阅读。

核心成员可以直接提交到仓库；其他参与者建议通过 Fork 和 Pull Request 提交修改。提交前请确认资料可以公开，且不包含学生信息、会议聊天记录、私人联系方式或未授权材料。

## 使用说明

本仓库资料仅用于教学、科研和学习交流。教材内容请以原教材网站为准；PPT、视频和笔记等资料由共学成员整理或提供，引用、转载或二次使用时请尊重原教材、原作者和汇报人的版权。

如发现链接失效、资料错误或版权风险，请通过 Issue 提交说明，或联系仓库维护者处理。

## 引用方式

如需引用本资料库，请注明仓库名称、章节、汇报人和访问日期。更正式的引用信息可参考 [CITATION.cff](./CITATION.cff)。
