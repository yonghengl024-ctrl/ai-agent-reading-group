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
    position: relative;
    isolation: isolate;
    min-height: 100vh;
    overflow-x: hidden;
    background: var(--wash);
  }

  body::before,
  body::after {
    content: "";
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
  }

  body::before {
    background-image:
      linear-gradient(118deg, rgba(8, 127, 140, .18) 0%, rgba(8, 127, 140, 0) 34%),
      linear-gradient(248deg, rgba(184, 107, 47, .16) 0%, rgba(184, 107, 47, 0) 38%),
      linear-gradient(42deg, rgba(64, 81, 181, .12) 0%, rgba(64, 81, 181, 0) 36%),
      linear-gradient(180deg, rgba(255, 255, 255, .82), rgba(246, 248, 251, .94));
    background-position: 0% 0%, 100% 0%, 18% 100%, 0 0;
    background-size: 170% 170%, 180% 180%, 160% 160%, 100% 100%;
    animation: color-flow 22s ease-in-out infinite alternate;
  }

  body::after {
    opacity: .58;
    background-image:
      linear-gradient(105deg, transparent 0 34%, rgba(255, 255, 255, .62) 43%, transparent 53%),
      repeating-linear-gradient(90deg, rgba(23, 32, 51, .05) 0 1px, transparent 1px 58px),
      repeating-linear-gradient(0deg, rgba(23, 32, 51, .04) 0 1px, transparent 1px 58px);
    background-size: 240% 240%, 58px 58px, 58px 58px;
    background-position: -80% -40%, 0 0, 0 0;
    animation: grid-flow 28s linear infinite;
  }

  .agent-canvas {
    position: fixed;
    inset: 0;
    z-index: 1;
    width: 100vw;
    height: 100vh;
    opacity: .92;
    pointer-events: none;
  }

  .page-shell {
    position: relative;
    z-index: 2;
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
    background: rgba(255, 255, 255, .78);
    backdrop-filter: blur(10px);
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
    background: rgba(255, 255, 255, .76);
    backdrop-filter: blur(12px);
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
    background: rgba(255, 255, 255, .76);
    backdrop-filter: blur(12px);
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
    body::before,
    body::after {
      animation: none;
    }

    .agent-canvas {
      display: none;
    }
  }

  @keyframes color-flow {
    from {
      background-position: 0% 0%, 100% 0%, 18% 100%, 0 0;
    }

    to {
      background-position: 34% 18%, 70% 28%, 82% 58%, 0 0;
    }
  }

  @keyframes grid-flow {
    from {
      background-position: -80% -40%, 0 0, 0 0;
    }

    to {
      background-position: 120% 70%, 58px 34px, 34px 58px;
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

<canvas class="agent-canvas" id="agent-bg" aria-hidden="true"></canvas>

<div class="page-shell">
  <section class="hero">
    <div>
      <p class="eyebrow">AI-Agent 使用指南</p>
      <h1>AI-Agent 使用介绍与实践资料</h1>
      <p class="lead">围绕 AI-Agent 的实际使用整理教材链接、讲解视频、PPT/PDF/HTML 演示文稿和实践案例。当前第一期以《AI-Agent》教材导读为主线，后续会继续扩展其他专题分享。</p>
      <div class="badges">
        <img alt="Chapters" src="https://img.shields.io/badge/chapters-23-087f8c">
        <img alt="Video links" src="https://img.shields.io/badge/video_links-16%2F23-b86b2f">
        <img alt="Materials" src="https://img.shields.io/badge/materials-PPT%2FPDF%2FHTML-2f7d32">
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
    <div class="metric"><strong>8</strong><span>章节已有 PPT/PDF/HTML 资料</span></div>
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

<script>
  (function () {
    var canvas = document.getElementById("agent-bg");
    var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

    if (!canvas || reducedMotion.matches) {
      if (canvas) {
        canvas.remove();
      }
      return;
    }

    var ctx = canvas.getContext("2d");
    if (!ctx) {
      return;
    }

    var width = 0;
    var height = 0;
    var dpr = 1;
    var frameId = 0;
    var nodes = [];
    var edges = [];
    var pointer = { x: 0, y: 0, tx: 0.5, ty: 0.5, active: false };
    var colors = ["8, 127, 140", "64, 81, 181", "184, 107, 47", "47, 125, 50"];
    var nodeTemplates = [
      { u: 0.09, v: 0.24, d: 0.34, g: 0 },
      { u: 0.09, v: 0.58, d: 0.42, g: 0 },
      { u: 0.23, v: 0.16, d: 0.72, g: 1 },
      { u: 0.25, v: 0.42, d: 0.86, g: 2 },
      { u: 0.23, v: 0.72, d: 0.62, g: 3 },
      { u: 0.41, v: 0.26, d: 1.04, g: 1 },
      { u: 0.42, v: 0.58, d: 1.12, g: 2 },
      { u: 0.57, v: 0.20, d: 1.24, g: 0 },
      { u: 0.59, v: 0.45, d: 1.36, g: 1 },
      { u: 0.56, v: 0.70, d: 1.14, g: 3 },
      { u: 0.74, v: 0.18, d: 1.02, g: 2 },
      { u: 0.76, v: 0.40, d: 1.18, g: 0 },
      { u: 0.75, v: 0.64, d: 1.00, g: 1 },
      { u: 0.91, v: 0.31, d: 0.74, g: 3 },
      { u: 0.91, v: 0.58, d: 0.66, g: 2 },
      { u: 0.80, v: 0.80, d: 0.78, g: 0 },
      { u: 0.36, v: 0.82, d: 0.74, g: 1 }
    ];
    var edgePairs = [
      [0, 3], [1, 3], [2, 5], [3, 5], [4, 6],
      [5, 7], [5, 8], [6, 8], [6, 9], [7, 10],
      [8, 10], [8, 11], [9, 12], [10, 13], [11, 13],
      [11, 14], [12, 14], [8, 15], [15, 16], [16, 6],
      [3, 7], [4, 16]
    ];
    var lanes = [
      { p: [[0.03, 0.18], [0.30, 0.05], [0.69, 0.21], [0.98, 0.12]], c: "64, 81, 181", s: 0.050, o: 0.08 },
      { p: [[0.02, 0.52], [0.31, 0.42], [0.62, 0.61], [0.98, 0.48]], c: "8, 127, 140", s: 0.064, o: 0.24 },
      { p: [[0.04, 0.82], [0.33, 0.86], [0.66, 0.75], [0.96, 0.88]], c: "184, 107, 47", s: 0.046, o: 0.42 },
      { p: [[0.16, 0.96], [0.35, 0.64], [0.63, 0.36], [0.86, 0.04]], c: "47, 125, 50", s: 0.056, o: 0.61 }
    ];

    function resizeCanvas() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      width = window.innerWidth;
      height = window.innerHeight;
      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
      canvas.style.width = width + "px";
      canvas.style.height = height + "px";
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      buildScene();
    }

    function buildScene() {
      nodes = [];
      edges = [];

      for (var i = 0; i < nodeTemplates.length; i += 1) {
        var template = nodeTemplates[i];
        nodes.push({
          u: template.u,
          v: template.v,
          d: template.d,
          g: template.g,
          phase: i * 0.73,
          size: 9 + (i % 4) * 1.7
        });
      }

      for (var j = 0; j < edgePairs.length; j += 1) {
        edges.push({
          from: edgePairs[j][0],
          to: edgePairs[j][1],
          phase: (j * 0.137) % 1,
          speed: 0.060 + (j % 5) * 0.008,
          bend: (j % 2 === 0 ? 1 : -1) * (28 + (j % 4) * 10)
        });
      }
    }

    function parallax(depth) {
      return {
        x: (pointer.tx - 0.5) * 48 * depth,
        y: (pointer.ty - 0.5) * 34 * depth
      };
    }

    function nodePoint(node, time) {
      var drift = parallax(node.d);
      return {
        x: node.u * width + drift.x + Math.sin(time * 0.38 + node.phase) * 4.5,
        y: node.v * height + drift.y + Math.cos(time * 0.32 + node.phase) * 3.8
      };
    }

    function lanePoint(lane, index, time) {
      var p = lane.p[index];
      var depth = 0.56 + index * 0.12;
      var drift = parallax(depth);
      return {
        x: p[0] * width + drift.x + Math.sin(time * 0.18 + index) * 8,
        y: p[1] * height + drift.y + Math.cos(time * 0.16 + index) * 6
      };
    }

    function cubicPoint(a, b, c, d, t) {
      var mt = 1 - t;
      return {
        x: mt * mt * mt * a.x + 3 * mt * mt * t * b.x + 3 * mt * t * t * c.x + t * t * t * d.x,
        y: mt * mt * mt * a.y + 3 * mt * mt * t * b.y + 3 * mt * t * t * c.y + t * t * t * d.y
      };
    }

    function drawDiamond(x, y, size, angle, fillStyle, strokeStyle, lineWidth) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(angle);
      ctx.beginPath();
      ctx.moveTo(0, -size);
      ctx.lineTo(size, 0);
      ctx.lineTo(0, size);
      ctx.lineTo(-size, 0);
      ctx.closePath();
      if (fillStyle) {
        ctx.fillStyle = fillStyle;
        ctx.fill();
      }
      if (strokeStyle) {
        ctx.strokeStyle = strokeStyle;
        ctx.lineWidth = lineWidth || 1;
        ctx.stroke();
      }
      ctx.restore();
    }

    function drawChip(x, y, size, angle, color, intensity) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(angle);
      ctx.fillStyle = "rgba(255, 255, 255, " + (0.50 + intensity * 0.20).toFixed(3) + ")";
      ctx.strokeStyle = "rgba(" + color + ", " + (0.46 + intensity * 0.34).toFixed(3) + ")";
      ctx.lineWidth = 1.25 + intensity * 0.9;
      ctx.beginPath();
      ctx.rect(-size, -size, size * 2, size * 2);
      ctx.fill();
      ctx.stroke();

      ctx.strokeStyle = "rgba(" + color + ", " + (0.24 + intensity * 0.28).toFixed(3) + ")";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(-size * 1.55, -size * 0.45);
      ctx.lineTo(-size, -size * 0.45);
      ctx.moveTo(-size * 1.55, size * 0.45);
      ctx.lineTo(-size, size * 0.45);
      ctx.moveTo(size, -size * 0.45);
      ctx.lineTo(size * 1.55, -size * 0.45);
      ctx.moveTo(size, size * 0.45);
      ctx.lineTo(size * 1.55, size * 0.45);
      ctx.moveTo(-size * 0.45, -size * 1.55);
      ctx.lineTo(-size * 0.45, -size);
      ctx.moveTo(size * 0.45, -size * 1.55);
      ctx.lineTo(size * 0.45, -size);
      ctx.moveTo(-size * 0.45, size);
      ctx.lineTo(-size * 0.45, size * 1.55);
      ctx.moveTo(size * 0.45, size);
      ctx.lineTo(size * 0.45, size * 1.55);
      ctx.stroke();

      ctx.strokeStyle = "rgba(23, 32, 51, .18)";
      ctx.beginPath();
      ctx.moveTo(-size * 0.45, 0);
      ctx.lineTo(size * 0.45, 0);
      ctx.moveTo(0, -size * 0.45);
      ctx.lineTo(0, size * 0.45);
      ctx.stroke();
      ctx.restore();
    }

    function drawPacket(point, tangent, color, size, alpha) {
      var angle = Math.atan2(tangent.y, tangent.x);
      ctx.save();
      ctx.translate(point.x, point.y);
      ctx.rotate(angle);
      ctx.fillStyle = "rgba(" + color + ", " + alpha.toFixed(3) + ")";
      ctx.strokeStyle = "rgba(255, 255, 255, " + Math.min(0.82, alpha + 0.24).toFixed(3) + ")";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(size, 0);
      ctx.lineTo(0, size * 0.58);
      ctx.lineTo(-size, 0);
      ctx.lineTo(0, -size * 0.58);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();
      ctx.restore();
    }

    function drawIsometricGrid(time) {
      var spacing = Math.max(46, Math.min(74, width / 18));
      var extent = Math.max(width, height) * 1.55;
      var shift = (time * 18) % spacing;
      var drift = parallax(0.36);

      ctx.save();
      ctx.translate(width * 0.5 + drift.x, height * 0.58 + drift.y);
      ctx.rotate(-0.36);
      ctx.scale(1, 0.52);

      for (var i = -extent; i <= extent; i += spacing) {
        var major = Math.round((i + extent) / spacing) % 4 === 0;
        ctx.strokeStyle = major ? "rgba(64, 81, 181, .105)" : "rgba(23, 32, 51, .052)";
        ctx.lineWidth = major ? 1.15 : 0.8;
        ctx.beginPath();
        ctx.moveTo(i + shift, -extent);
        ctx.lineTo(i + shift, extent);
        ctx.moveTo(-extent, i - shift);
        ctx.lineTo(extent, i - shift);
        ctx.stroke();
      }

      ctx.strokeStyle = "rgba(8, 127, 140, .12)";
      ctx.setLineDash([10, 18]);
      ctx.lineDashOffset = -time * 34;
      ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.moveTo(-extent, 0);
      ctx.lineTo(extent, 0);
      ctx.moveTo(0, -extent);
      ctx.lineTo(0, extent);
      ctx.stroke();
      ctx.restore();
    }

    function drawSweep(time) {
      var travel = (time * 130) % (width + height);
      var gradient;

      ctx.save();
      ctx.translate(travel - height * 0.45, 0);
      ctx.rotate(-0.54);
      gradient = ctx.createLinearGradient(-60, 0, 120, 0);
      gradient.addColorStop(0, "rgba(255, 255, 255, 0)");
      gradient.addColorStop(0.42, "rgba(255, 255, 255, .18)");
      gradient.addColorStop(0.52, "rgba(8, 127, 140, .10)");
      gradient.addColorStop(1, "rgba(255, 255, 255, 0)");
      ctx.fillStyle = gradient;
      ctx.fillRect(-80, -height, 180, height * 3);
      ctx.restore();
    }

    function drawLanes(time) {
      for (var i = 0; i < lanes.length; i += 1) {
        var lane = lanes[i];
        var a = lanePoint(lane, 0, time);
        var b = lanePoint(lane, 1, time);
        var c = lanePoint(lane, 2, time);
        var d = lanePoint(lane, 3, time);

        ctx.save();
        ctx.lineCap = "round";
        ctx.strokeStyle = "rgba(" + lane.c + ", .075)";
        ctx.lineWidth = 18;
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.bezierCurveTo(b.x, b.y, c.x, c.y, d.x, d.y);
        ctx.stroke();

        ctx.strokeStyle = "rgba(" + lane.c + ", .22)";
        ctx.lineWidth = 1.5;
        ctx.setLineDash([9, 18]);
        ctx.lineDashOffset = -time * 72 * lane.s * 10;
        ctx.beginPath();
        ctx.moveTo(a.x, a.y);
        ctx.bezierCurveTo(b.x, b.y, c.x, c.y, d.x, d.y);
        ctx.stroke();
        ctx.restore();

        for (var k = 0; k < 4; k += 1) {
          var t = (time * lane.s + lane.o + k * 0.27) % 1;
          var point = cubicPoint(a, b, c, d, t);
          var next = cubicPoint(a, b, c, d, Math.min(1, t + 0.015));
          drawPacket(point, { x: next.x - point.x, y: next.y - point.y }, lane.c, 8, 0.64);
        }
      }
    }

    function edgeCurve(edge, time) {
      var a = nodePoint(nodes[edge.from], time);
      var d = nodePoint(nodes[edge.to], time);
      var dx = d.x - a.x;
      var dy = d.y - a.y;
      var c1 = { x: a.x + dx * 0.34 - dy * 0.08, y: a.y + dy * 0.24 + edge.bend };
      var c2 = { x: a.x + dx * 0.68 + dy * 0.08, y: a.y + dy * 0.76 - edge.bend };
      return { a: a, b: c1, c: c2, d: d };
    }

    function drawGraph(time) {
      for (var i = 0; i < edges.length; i += 1) {
        var edge = edges[i];
        var curve = edgeCurve(edge, time);
        var color = colors[nodes[edge.to].g];
        var pulse = (time * edge.speed + edge.phase) % 1;
        var pulsePoint = cubicPoint(curve.a, curve.b, curve.c, curve.d, pulse);
        var nextPoint = cubicPoint(curve.a, curve.b, curve.c, curve.d, Math.min(1, pulse + 0.018));

        ctx.save();
        ctx.lineCap = "round";
        ctx.strokeStyle = "rgba(23, 32, 51, .08)";
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(curve.a.x, curve.a.y);
        ctx.bezierCurveTo(curve.b.x, curve.b.y, curve.c.x, curve.c.y, curve.d.x, curve.d.y);
        ctx.stroke();

        ctx.strokeStyle = "rgba(" + color + ", .24)";
        ctx.lineWidth = 1.25;
        ctx.beginPath();
        ctx.moveTo(curve.a.x, curve.a.y);
        ctx.bezierCurveTo(curve.b.x, curve.b.y, curve.c.x, curve.c.y, curve.d.x, curve.d.y);
        ctx.stroke();
        ctx.restore();

        drawPacket(pulsePoint, { x: nextPoint.x - pulsePoint.x, y: nextPoint.y - pulsePoint.y }, color, 6.4, 0.72);
      }

      for (var j = 0; j < nodes.length; j += 1) {
        var node = nodes[j];
        var point = nodePoint(node, time);
        var dist = pointer.active ? Math.sqrt(Math.pow(point.x - pointer.x, 2) + Math.pow(point.y - pointer.y, 2)) : 9999;
        var focus = Math.max(0, 1 - dist / 210);
        var angle = Math.PI / 4 + Math.sin(time * 0.22 + node.phase) * 0.08;
        var size = node.size + focus * 5 + Math.sin(time * 1.8 + node.phase) * 0.6;
        var color = colors[node.g];

        if (focus > 0.02) {
          ctx.strokeStyle = "rgba(" + color + ", " + (focus * 0.42).toFixed(3) + ")";
          ctx.lineWidth = 1.2;
          ctx.beginPath();
          ctx.moveTo(pointer.x, pointer.y);
          ctx.lineTo(point.x, point.y);
          ctx.stroke();
        }

        drawDiamond(point.x, point.y, size * 2.65, angle, "rgba(" + color + ", .035)", "rgba(" + color + ", .11)", 1);
        drawChip(point.x, point.y, size, angle, color, focus);
      }
    }

    function drawSignalBars(time) {
      var count = Math.max(28, Math.floor(width / 34));
      var drift = parallax(0.22);

      ctx.save();
      ctx.lineCap = "round";

      for (var i = 0; i < count; i += 1) {
        var base = (i / count) * (width + 180) - 90;
        var y = ((time * 42 + i * 47) % (height + 120)) - 60;
        var x = base + Math.sin(time * 0.7 + i) * 26 + drift.x;
        var length = 16 + (i % 5) * 8;
        var alpha = 0.06 + (i % 4) * 0.025;

        ctx.strokeStyle = "rgba(23, 32, 51, " + alpha.toFixed(3) + ")";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(x, y + drift.y);
        ctx.lineTo(x + length, y + length * 0.42 + drift.y);
        ctx.stroke();
      }

      ctx.restore();
    }

    function animate(now) {
      var time = now * 0.001;
      var targetX = pointer.active ? pointer.x / Math.max(1, width) : 0.5;
      var targetY = pointer.active ? pointer.y / Math.max(1, height) : 0.5;

      pointer.tx += (targetX - pointer.tx) * 0.045;
      pointer.ty += (targetY - pointer.ty) * 0.045;

      ctx.clearRect(0, 0, width, height);
      drawIsometricGrid(time);
      drawSignalBars(time);
      drawLanes(time);
      drawGraph(time);
      drawSweep(time);
      frameId = window.requestAnimationFrame(animate);
    }

    function start() {
      if (!frameId) {
        frameId = window.requestAnimationFrame(animate);
      }
    }

    function stop() {
      if (frameId) {
        window.cancelAnimationFrame(frameId);
        frameId = 0;
      }
    }

    window.addEventListener("resize", resizeCanvas);
    window.addEventListener("pointermove", function (event) {
      pointer.x = event.clientX;
      pointer.y = event.clientY;
      pointer.active = true;
    });
    window.addEventListener("pointerleave", function () {
      pointer.active = false;
    });
    window.addEventListener("blur", function () {
      pointer.active = false;
    });
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) {
        stop();
      } else {
        start();
      }
    });

    if (typeof reducedMotion.addEventListener === "function") {
      reducedMotion.addEventListener("change", function (event) {
        if (event.matches) {
          stop();
          canvas.remove();
        }
      });
    }

    resizeCanvas();
    start();
  }());
</script>
