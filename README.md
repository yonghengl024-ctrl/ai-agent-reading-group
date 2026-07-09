# AI-Agent 使用介绍与实践资料

<p>
  <img alt="Chapters" src="https://img.shields.io/badge/chapters-23-087f8c">
  <img alt="Video links" src="https://img.shields.io/badge/video_links-16%2F23-b86b2f">
  <img alt="Materials" src="https://img.shields.io/badge/materials-PPT%2FPDF%2FHTML-2f7d32">
  <img alt="Series" src="https://img.shields.io/badge/series-book%20%2B%20topics-4051b5">
  <img alt="GitHub Pages" src="https://img.shields.io/badge/GitHub_Pages-online-4051b5">
</p>

本仓库用于系统介绍 AI-Agent 的核心概念、工具使用、工作流设计和典型实践场景，整理学习分享中的教材链接、讲解视频、PPT/HTML/PDF、实践案例和延伸阅读。

当前第一期内容以《AI-Agent》教材学习分享为主线。教材学习完成后，本仓库会继续收录其他 AI-Agent 相关专题分享、工具实践、案例复盘和工作流资料。

项目目标不是替代原教材，而是围绕 AI-Agent 的实际使用建立一个结构稳定、便于检索、方便维护和可以长期引用的公开资料入口。读者可以按教材章节了解 AI-Agent 从基础概念、提示词工程、版本控制、Skills、多智能体、Hooks，到知识库、办公自动化、投研系统、文献综述和经济学实证研究等场景中的使用方法；后续也可以按专题继续检索新的分享内容。

参考教材网站：

- https://ailingnan.xueheng.site:8000
- https://ai.lingnan.top/book/

> 说明：本仓库为 AI-Agent 使用介绍和实践资料整理项目，非教材官方网站或官方课程仓库。教材正文、更新和解释请以原教材网站为准。

## 快速入口

| 入口 | 说明 |
|---|---|
| [网页入口](https://yonghengl024-ctrl.github.io/ai-agent-reading-group/) | GitHub Pages 版资料导航 |
| [第一期教材章节](#第一期教材导读) | 按章节浏览教材、视频、PPT 和实践案例 |
| [后续专题](./topics/) | 教材学习完成后的 AI-Agent 专题分享入口 |
| [上传指南](./UPLOAD_GUIDE.md) | 本地资料提交到 GitHub 的操作步骤 |
| [贡献说明](./CONTRIBUTING.md) | 文件命名、视频链接、版权检查要求 |
| [常见问题](./FAQ.md) | 视频、PPT、版权和 GitHub Pages 相关问题 |
| [讲解人](./speakers/) | 维护可公开的讲解人信息 |

## 项目背景

AI-Agent 相关工具和方法正在快速进入教学、科研、办公自动化、知识管理、金融投研和实证研究等场景。很多使用者面对的主要问题不是缺少概念介绍，而是不知道如何把智能体工具落到具体任务中：如何配置框架、如何写规则文件、如何设计提示词、如何组织 Skills、如何使用子代理和多智能体团队、如何搭建知识库和自动化工作流。

本项目围绕这些实际使用问题组织资料，希望帮助读者从“知道 AI-Agent 是什么”进一步走向“能够用 AI-Agent 完成具体任务”。

第一期内容按照《AI-Agent》教材章节组织；后续内容会按专题组织，避免把不同来源、不同形式的学习分享混在同一个章节体系中。

本项目重点关注三个问题：

1. 如何理解 AI-Agent 的基本工作方式和人机协作范式。
2. 如何掌握 AI-Agent 工具链中的配置、提示词、规则、Skills、Hooks 和多智能体机制。
3. 如何把 AI-Agent 应用于办公自动化、知识库、投研、文献综述和经济学实证研究等具体场景。

## 适用对象

本仓库适合以下使用者：

- 正在入门 AI-Agent 工具和智能体工作流的学习者
- 希望快速定位某一主题视频、PPT 或教材链接的使用者
- 准备设计 AI-Agent 教学、培训、工作坊或课程材料的团队
- 希望参考 AI-Agent 在教学、办公、知识库、投研和实证研究中应用案例的研究者和实践者

## 资料结构

仓库按章节组织资料，每一章对应一个目录：

```text
chapters/chapter-XX/
├── README.md   # 主题概览、讲解信息、教材链接
├── videos.md   # 讲解视频链接
├── slides/     # PPT、PDF 或 HTML 演示文稿
└── examples/   # 可选，实践案例和代码资料
```

教材学习完成后的专题分享放在 `topics/` 目录中，每个专题使用独立目录：

```text
topics/topic-name/
├── README.md
├── videos.md
├── slides/
└── examples/
```

根目录中的主要文件：

| 文件 | 作用 |
|---|---|
| `README.md` | 项目主页和章节总目录 |
| `UPLOAD_GUIDE.md` | 上传到 GitHub 的操作步骤 |
| `CONTRIBUTING.md` | 资料提交规范 |
| `FAQ.md` | 常见问题 |
| `topics/README.md` | 后续专题分享入口 |
| `LICENSE` | 授权和版权说明 |
| `CITATION.cff` | 引用信息 |
| `docs/index.md` | GitHub Pages 展示页 |

## 当前进度

| 内容 | 状态 |
|---|---|
| 第一期教材导读 | 已覆盖第 1 到第 23 章 |
| 教材链接 | 已补充 |
| 讲解视频链接 | 已补充 16/23 |
| PPT/PDF/HTML | 已补充第 6、9-14、18 章 |
| 实践案例 | 已补充第 13、14 章 |
| 后续专题分享 | 将按主题持续添加到 `topics/` |
| 学习笔记 | 有内容时按章节添加 |
| GitHub Pages | 已开启 |

暂缺视频链接的主题：

```text
第8章、第15章、第16章、第20章、第21章、第22章、第23章
```

## 后续扩展

本仓库不是一次性的教材配套仓库。第一期教材学习完成后，后续 AI-Agent 相关分享会按专题继续沉淀，例如：

- AI-Agent 工具实操和工作流模板
- 教学、科研、办公、金融、知识管理等场景案例
- 新工具、新框架或重要论文的分享资料
- 可复用的提示词、规则文件、Skills、Hooks 和自动化方案

这类内容优先放入 `topics/`，每个专题使用独立目录维护 README、视频链接、PPT/HTML/PDF 和实践案例，避免与当前 23 章教材目录混在一起。

## 第一期教材导读

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
- **讲解视频**：保存为外部平台链接，当前主要使用百度网盘。
- **PPT/HTML/PDF**：每章讲解材料，建议优先上传 PDF 或 HTML 版本，必要时同时保留 PPTX。
- **实践案例**：放置可公开的规则文件、代码、示例数据和工作流说明。
- **学习笔记**：有正式内容时再按章节添加，避免保留空白模板。
- **协作记录**：通过 Issue 和 Pull Request 维护链接失效、资料更新和补充建议。

## 视频存放建议

视频文件通常较大，不建议直接提交到 GitHub 仓库。建议将视频上传到 Bilibili、腾讯会议回放、百度网盘、阿里云盘、YouTube 或对象存储服务，然后在对应章节的 `videos.md` 中维护链接。

本仓库的 `.gitignore` 已默认忽略常见视频格式，避免误提交大文件。

## 推荐贡献流程

1. 将 PPT 或 PDF 放到对应章节的 `slides/` 目录。
2. 将视频上传到外部平台。
3. 在对应章节的 `videos.md` 中补充视频链接。
4. 在对应章节的 `README.md` 中补充讲解人、教材链接和资料链接。
5. 如有实践案例，将资料放到对应章节的 `examples/` 目录，并补充简短说明。
6. 如有正式学习笔记，再按章节添加 `notes.md`。

核心成员可以直接提交到仓库；其他参与者建议通过 Fork 和 Pull Request 提交修改。提交前请确认资料可以公开，且不包含学生信息、会议聊天记录、私人联系方式或未授权材料。

## 使用说明

本仓库资料仅用于教学、科研和非商业学习交流。教材内容请以原教材网站为准；PPT、视频和案例等资料由相关讲解人整理或提供，引用、转载或二次使用时请尊重原教材、原作者和讲解人的版权。

如发现链接失效、资料错误或版权风险，请通过 Issue 提交说明，或联系仓库维护者处理。

## 引用方式

如需引用本项目，请注明仓库名称、章节、讲解人和访问日期。更正式的引用信息可参考 [CITATION.cff](./CITATION.cff)。
