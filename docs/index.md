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

  .linkbar a {
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

  .stage-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
    margin: 0 0 38px;
  }

  .stage-card {
    padding: 20px;
    border: 1px solid var(--line);
    border-radius: 8px;
    background: var(--paper);
    box-shadow: 0 12px 26px rgba(23, 32, 51, .045);
  }

  .stage-card h2 {
    margin: 0 0 10px;
    font-size: 22px;
    letter-spacing: 0;
  }

  .stage-card p {
    margin: 0;
    color: var(--muted);
    font-size: 15px;
    line-height: 1.7;
  }

  .stage-card a {
    display: inline-flex;
    margin-top: 16px;
    color: var(--teal);
    font-weight: 700;
    text-decoration: none;
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
    .metrics,
    .stage-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (prefers-reduced-motion: no-preference) {
    .hero,
    .metric,
    .stage-card {
      animation: rise-in .52s ease both;
    }

    .metric:nth-child(2) { animation-delay: .05s; }
    .metric:nth-child(3) { animation-delay: .1s; }
    .metric:nth-child(4) { animation-delay: .15s; }
  }

  @media (prefers-reduced-motion: reduce) {
    body {
      animation: none;
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
      <p class="lead">围绕 AI-Agent 的实际使用整理教材链接、讲解视频、PPT/HTML 演示文稿和实践案例。当前第一期以《AI-Agent》教材导读为主线，后续会继续扩展其他专题分享。</p>
      <div class="badges">
        <img alt="Chapters" src="https://img.shields.io/badge/chapters-23-087f8c">
        <img alt="Video links" src="https://img.shields.io/badge/video_links-16%2F23-b86b2f">
        <img alt="Materials" src="https://img.shields.io/badge/materials-PPT%2FHTML-2f7d32">
        <img alt="GitHub Pages" src="https://img.shields.io/badge/GitHub_Pages-online-4051b5">
      </div>
      <div class="linkbar">
        <a class="primary" href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group">GitHub 仓库</a>
        <a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/blob/main/UPLOAD_GUIDE.md">上传指南</a>
        <a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/topics">后续专题</a>
        <a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/issues">问题反馈</a>
        <a href="https://ai.lingnan.top/book/">教材网站</a>
      </div>
    </div>
    <div class="route">
      <strong>推荐阅读路径</strong>
      <code>教材导读 -> 实践资料 -> 后续专题 -> 持续更新</code>
    </div>
  </section>

  <section class="metrics">
    <div class="metric"><strong>23</strong><span>章节目录已建立</span></div>
    <div class="metric"><strong>16</strong><span>章节已有视频链接</span></div>
    <div class="metric"><strong>6</strong><span>章节已有 PPT/HTML 资料</span></div>
    <div class="metric"><strong>2</strong><span>章节已有实践案例</span></div>
  </section>

  <section class="stage-grid">
    <div class="stage-card">
      <h2>第一期：教材导读</h2>
      <p>保留 23 章教材学习资料，按章节维护教材链接、视频、PPT/HTML/PDF 和实践案例。</p>
      <a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/chapters">查看章节资料</a>
    </div>
    <div class="stage-card">
      <h2>后续：专题分享</h2>
      <p>教材学习完成后，新的 AI-Agent 工具实践、案例复盘、论文分享和工作流模板会放入独立专题目录。</p>
      <a href="https://github.com/yonghengl024-ctrl/ai-agent-reading-group/tree/main/topics">查看专题入口</a>
    </div>
  </section>

  <p class="footer-note">本项目为 AI-Agent 使用介绍和实践资料整理项目，非教材官方网站。当前第一期围绕《AI-Agent》教材导读，后续专题分享将继续沉淀到 topics 目录。教材正文、更新和解释请以原教材网站为准。</p>
</div>
