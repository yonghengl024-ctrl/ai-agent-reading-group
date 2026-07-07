---
title: AI-Agent 使用介绍与实践资料
---

<style>
  :root {
    --ink: #172033;
    --muted: #5f6b7a;
    --line: #d8e0e8;
    --paper: #ffffff;
    --wash: #f6f8fb;
    --teal: #087f8c;
    --green: #2f7d32;
    --amber: #b86b2f;
    --indigo: #4051b5;
  }

  body {
    background: var(--wash);
    background-image:
      linear-gradient(120deg, rgba(8, 127, 140, .10), rgba(8, 127, 140, 0) 34%),
      linear-gradient(245deg, rgba(184, 107, 47, .10), rgba(184, 107, 47, 0) 34%),
      repeating-linear-gradient(90deg, rgba(23, 32, 51, .035) 0 1px, transparent 1px 36px),
      repeating-linear-gradient(0deg, rgba(23, 32, 51, .03) 0 1px, transparent 1px 36px);
    background-size: 100% 560px, 100% 560px, 36px 36px, 36px 36px;
    animation: background-drift 18s ease-in-out infinite alternate;
  }

  .page-shell {
    max-width: 1180px;
    margin: 0 auto;
    padding: 34px 20px 58px;
    color: var(--ink);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
  }

  .hero {
    display: grid;
    grid-template-columns: minmax(0, 1.35fr) minmax(260px, .65fr);
    gap: 32px;
    align-items: end;
    padding: 20px 0 30px;
    border-bottom: 1px solid var(--line);
  }

  .eyebrow {
    margin: 0 0 10px;
    color: var(--teal);
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
  }

  .hero h1 {
    margin: 0;
    max-width: 780px;
    font-size: clamp(34px, 5vw, 58px);
    line-height: 1.05;
    letter-spacing: 0;
  }

  .lead {
    max-width: 760px;
    margin: 18px 0 0;
    color: var(--muted);
    font-size: 17px;
    line-height: 1.75;
  }

  .badges {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 20px;
  }

  .badges img {
    height: 22px;
  }

  .linkbar {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 24px;
  }

  .linkbar a,
  .card-actions a {
    display: inline-flex;
    align-items: center;
    min-height: 38px;
    padding: 8px 13px;
    border: 1px solid var(--line);
    border-radius: 6px;
    background: var(--paper);
    color: var(--ink);
    text-decoration: none;
    font-size: 14px;
    font-weight: 650;
  }

  .linkbar a.primary {
    border-color: var(--teal);
    background: var(--teal);
    color: #ffffff;
  }

  .route {
    border-left: 4px solid var(--amber);
    padding: 14px 0 14px 18px;
  }

  .route strong {
    display: block;
    margin-bottom: 8px;
    font-size: 15px;
  }

  .route code {
    display: block;
    overflow-x: auto;
    padding: 12px;
    border-radius: 6px;
    background: #172033;
    color: #ffffff;
    font-size: 13px;
    white-space: nowrap;
  }

  .metrics {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 14px;
    margin: 26px 0 38px;
  }

  .metric {
    min-height: 104px;
    padding: 18px;
    border: 1px solid var(--line);
    border-radius: 8px;
    background: var(--paper);
    box-shadow: 0 12px 26px rgba(23, 32, 51, .05);
  }

  .metric strong {
    display: block;
    font-size: 28px;
    line-height: 1;
  }

  .metric span {
    display: block;
    margin-top: 10px;
    color: var(--muted);
    font-size: 14px;
  }

  .section-heading {
    display: flex;
    justify-content: space-between;
    gap: 18px;
    align-items: end;
    margin: 34px 0 14px;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--line);
  }

  .section-heading h2 {
    margin: 0;
    font-size: 24px;
    letter-spacing: 0;
  }

  .section-heading p {
    max-width: 520px;
    margin: 0;
    color: var(--muted);
    font-size: 14px;
    line-height: 1.6;
  }

  .chapter-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(245px, 1fr));
    gap: 14px;
  }

  .chapter-card {
    min-height: 174px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 18px;
    border: 1px solid var(--line);
    border-radius: 8px;
    background: var(--paper);
    box-shadow: 0 12px 26px rgba(23, 32, 51, .045);
    transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease;
  }

  .chapter-card:hover {
    transform: translateY(-4px);
    border-color: rgba(8, 127, 140, .45);
    box-shadow: 0 18px 34px rgba(23, 32, 51, .09);
  }

  .chapter-card h3 {
    margin: 0 0 12px;
    font-size: 16px;
    line-height: 1.45;
  }

  .chapter-card h3 span {
    display: block;
    margin-top: 4px;
    font-size: 15px;
    font-weight: 600;
  }

  .tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 16px;
  }

  .tag {
    padding: 4px 7px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 700;
    line-height: 1.1;
  }

  .tag.textbook {
    background: #e8f3f4;
    color: var(--teal);
  }

  .tag.video {
    background: #f5ede5;
    color: var(--amber);
  }

  .tag.material {
    background: #e9f3ea;
    color: var(--green);
  }

  .tag.example {
    background: #eceefd;
    color: var(--indigo);
  }

  .card-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  .footer-note {
    margin-top: 34px;
    padding-top: 18px;
    border-top: 1px solid var(--line);
    color: var(--muted);
    font-size: 14px;
    line-height: 1.7;
  }

  @media (max-width: 820px) {
    .hero,
    .metrics {
      grid-template-columns: 1fr;
    }

    .section-heading {
      display: block;
    }

    .section-heading p {
      margin-top: 8px;
    }
  }

  @media (prefers-reduced-motion: no-preference) {
    .hero,
    .metric,
    .chapter-card {
      animation: rise-in .52s ease both;
    }

    .metric:nth-child(2) { animation-delay: .05s; }
    .metric:nth-child(3) { animation-delay: .1s; }
    .metric:nth-child(4) { animation-delay: .15s; }
    .chapter-card:nth-child(2n) { animation-delay: .04s; }
    .chapter-card:nth-child(3n) { animation-delay: .08s; }
    .chapter-card:nth-child(4n) { animation-delay: .12s; }
  }

  @media (prefers-reduced-motion: reduce) {
    body {
      animation: none;
    }

    .chapter-card {
      transition: none;
    }
  }

  @keyframes background-drift {
    from {
      background-position: 0 0, 100% 0, 0 0, 0 0;
    }

    to {
      background-position: 0 28px, 100% -28px, 18px 12px, 12px 18px;
    }
  }

  @keyframes rise-in {
    from {
      opacity: 0;
      transform: translateY(14px);
    }

    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
</style>

<div class="page-shell">
  <section class="hero">
    <div>
      <p class="eyebrow">AI-Agent 使用指南</p>
      <h1>AI-Agent 使用介绍与实践资料</h1>
      <p class="lead">围绕 AI-Agent 的实际使用整理教材链接、讲解视频、PPT/HTML 演示文稿和实践案例，覆盖基础概念、工具机制、知识库、Hooks、多智能体和科研办公场景。</p>
      <div class="badges">
        <img alt="Chapters" src="https://img.shields.io/badge/chapters-23-087f8c">
        <img alt="Video links" src="https://img.shields.io/badge/video_links-16%2F23-b86b2f">
        <img alt="Materials" src="https://img.shields.io/badge/materials-PPT%2FHTML-2f7d32">
        <img alt="GitHub Pages" src="https://img.shields.io/badge/GitHub_Pages-online-4051b5">
      </div>
      <div class="linkbar">
        <a class="primary" href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group">GitHub 仓库</a>
        <a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/blob/main/UPLOAD_GUIDE.md">上传指南</a>
        <a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/issues">问题反馈</a>
        <a href="https://ai.lingnan.top/book/">教材网站</a>
      </div>
    </div>
    <div class="route">
      <strong>推荐阅读路径</strong>
      <code>基础概念 -> 工具机制 -> 工作流设计 -> 场景实践</code>
    </div>
  </section>

  <section class="metrics">
    <div class="metric"><strong>23</strong><span>章节目录已建立</span></div>
    <div class="metric"><strong>16</strong><span>章节已有视频链接</span></div>
    <div class="metric"><strong>6</strong><span>章节已有 PPT/HTML 资料</span></div>
    <div class="metric"><strong>2</strong><span>章节已有实践案例</span></div>
  </section>

  <section>
    <div class="section-heading">
      <h2>基础入门</h2>
      <p>从智能体概念、人机协作、环境配置、规则文件、提示词工程和版本控制开始。</p>
    </div>
    <div class="chapter-grid">
      <article class="chapter-card"><div><h3>第 1 章<span>智能体概览与本书导读</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-01">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-1/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 2 章<span>人机协作范式</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-02">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-2/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 3 章<span>智能体框架安装与配置</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-03">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-3/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 4 章<span>项目创建与规则文件</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-04">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-4/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 5 章<span>提示词工程与任务规划</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-05">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-5/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 6 章<span>Git 与版本控制</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-06">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-6/">教材</a></div></article>
    </div>
  </section>

  <section>
    <div class="section-heading">
      <h2>工具机制</h2>
      <p>围绕 Skills、多智能体、知识库、Agent Teams、Hooks、评估迭代和高阶使用技巧组织资料。</p>
    </div>
    <div class="chapter-grid">
      <article class="chapter-card"><div><h3>第 7 章<span>Skills 基础</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-07">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-7/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 8 章<span>多智能体基础：子代理</span></h3><div class="tags"><span class="tag textbook">教材</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-08">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-8/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 9 章<span>Skills 进阶</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span><span class="tag material">PPT</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-09">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-9/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 10 章<span>智能体知识库设计</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span><span class="tag material">PPT</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-10">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-10/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 11 章<span>多智能体进阶：Agent Teams</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-11">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-11/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 12 章<span>Hooks</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span><span class="tag material">PPT</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-12">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-12/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 13 章<span>评估与迭代</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span><span class="tag material">HTML</span><span class="tag example">案例</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-13">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-13/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 14 章<span>高阶使用技巧</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span><span class="tag material">HTML</span><span class="tag example">案例</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-14">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-14/">教材</a></div></article>
    </div>
  </section>

  <section>
    <div class="section-heading">
      <h2>场景实践</h2>
      <p>面向办公自动化、金融知识库、投研系统、文献综述、知识管理、经济学实证和 OpenClaw 实战。</p>
    </div>
    <div class="chapter-grid">
      <article class="chapter-card"><div><h3>第 15 章<span>自动化办公工作台</span></h3><div class="tags"><span class="tag textbook">教材</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-15">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-15/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 16 章<span>金融多源知识库开发实战</span></h3><div class="tags"><span class="tag textbook">教材</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-16">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-16/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 17 章<span>多智能体投研系统</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-17">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-17/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 18 章<span>文献综述智能体系统</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span><span class="tag material">PPT</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-18">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-18/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 19 章<span>AI 原生知识管理系统</span></h3><div class="tags"><span class="tag textbook">教材</span><span class="tag video">视频</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-19">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-19/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 20 章<span>AI 智能体与经济学实证研究</span></h3><div class="tags"><span class="tag textbook">教材</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-20">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-20/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 21 章<span>OpenClaw 入门：安装部署与首次对话</span></h3><div class="tags"><span class="tag textbook">教材</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-21">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-21/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 22 章<span>OpenClaw 架构：工作区、记忆与运行机制</span></h3><div class="tags"><span class="tag textbook">教材</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-22">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-22/">教材</a></div></article>
      <article class="chapter-card"><div><h3>第 23 章<span>OpenClaw 实战：管家调度专家</span></h3><div class="tags"><span class="tag textbook">教材</span></div></div><div class="card-actions"><a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters/chapter-23">资料</a><a href="https://ai.lingnan.top/book/chapters/chapter-23/">教材</a></div></article>
    </div>
  </section>

  <p class="footer-note">本项目为 AI-Agent 使用介绍和实践资料整理项目，非教材官方网站。教材正文、更新和解释请以原教材网站为准。</p>
</div>
