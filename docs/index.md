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
    var width = 0;
    var height = 0;
    var dpr = 1;
    var frameId = 0;
    var particles = [];
    var pointer = { x: 0, y: 0, active: false };

    function particleCount() {
      var area = width * height;
      return Math.min(110, Math.max(46, Math.floor(area / 18500)));
    }

    function createParticles() {
      var count = particleCount();
      var goldenAngle = Math.PI * (3 - Math.sqrt(5));
      var cx = width * 0.52;
      var cy = height * 0.46;
      var spread = Math.min(width, height) * 0.64;
      var next = [];

      for (var i = 0; i < count; i += 1) {
        var ratio = Math.sqrt((i + 0.5) / count);
        var angle = i * goldenAngle;
        var x = cx + Math.cos(angle) * spread * ratio + (Math.random() - 0.5) * 80;
        var y = cy + Math.sin(angle) * spread * ratio + (Math.random() - 0.5) * 80;

        next.push({
          x: Math.max(24, Math.min(width - 24, x)),
          y: Math.max(24, Math.min(height - 24, y)),
          vx: (Math.random() - 0.5) * 0.28,
          vy: (Math.random() - 0.5) * 0.28,
          r: 1.3 + Math.random() * 1.8,
          phase: Math.random() * Math.PI * 2,
          tone: Math.random()
        });
      }

      particles = next;
    }

    function resizeCanvas() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      width = window.innerWidth;
      height = window.innerHeight;
      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
      canvas.style.width = width + "px";
      canvas.style.height = height + "px";
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      createParticles();
    }

    function drawOrbit(time) {
      var size = Math.min(width, height);
      var cx = width * 0.73 + Math.sin(time * 0.22) * 18;
      var cy = height * 0.28 + Math.cos(time * 0.18) * 14;

      ctx.save();
      ctx.lineWidth = 1.1;
      ctx.setLineDash([9, 17]);
      ctx.lineDashOffset = -time * 26;
      ctx.strokeStyle = "rgba(64, 81, 181, 0.16)";
      ctx.beginPath();
      ctx.ellipse(cx, cy, size * 0.42, size * 0.12, -0.34, 0, Math.PI * 2);
      ctx.stroke();

      ctx.setLineDash([5, 20]);
      ctx.lineDashOffset = time * 18;
      ctx.strokeStyle = "rgba(8, 127, 140, 0.15)";
      ctx.beginPath();
      ctx.ellipse(width * 0.25, height * 0.76, size * 0.34, size * 0.095, 0.46, 0, Math.PI * 2);
      ctx.stroke();
      ctx.restore();
    }

    function updateParticles(time) {
      var margin = 36;

      for (var i = 0; i < particles.length; i += 1) {
        var p = particles[i];
        var flowX = Math.sin(time * 0.42 + p.phase) * 0.045;
        var flowY = Math.cos(time * 0.38 + p.phase) * 0.045;

        p.vx += flowX;
        p.vy += flowY;

        if (pointer.active) {
          var dx = p.x - pointer.x;
          var dy = p.y - pointer.y;
          var distance = Math.sqrt(dx * dx + dy * dy) || 1;

          if (distance < 190) {
            var force = (1 - distance / 190) * 0.038;
            p.vx += (dx / distance) * force;
            p.vy += (dy / distance) * force;
          }
        }

        p.vx *= 0.965;
        p.vy *= 0.965;
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < -margin) p.x = width + margin;
        if (p.x > width + margin) p.x = -margin;
        if (p.y < -margin) p.y = height + margin;
        if (p.y > height + margin) p.y = -margin;
      }
    }

    function drawLinks() {
      var maxDistance = Math.min(172, Math.max(112, width * 0.13));
      var maxDistanceSq = maxDistance * maxDistance;

      for (var i = 0; i < particles.length; i += 1) {
        for (var j = i + 1; j < particles.length; j += 1) {
          var a = particles[i];
          var b = particles[j];
          var dx = a.x - b.x;
          var dy = a.y - b.y;
          var distanceSq = dx * dx + dy * dy;

          if (distanceSq < maxDistanceSq) {
            var distance = Math.sqrt(distanceSq);
            var alpha = Math.pow(1 - distance / maxDistance, 2) * 0.26;
            ctx.strokeStyle = "rgba(8, 127, 140, " + alpha.toFixed(3) + ")";
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(a.x, a.y);
            ctx.lineTo(b.x, b.y);
            ctx.stroke();
          }
        }
      }

      if (pointer.active) {
        for (var k = 0; k < particles.length; k += 1) {
          var p = particles[k];
          var px = p.x - pointer.x;
          var py = p.y - pointer.y;
          var pointerDistance = Math.sqrt(px * px + py * py);

          if (pointerDistance < 230) {
            var pointerAlpha = Math.pow(1 - pointerDistance / 230, 2) * 0.42;
            ctx.strokeStyle = "rgba(184, 107, 47, " + pointerAlpha.toFixed(3) + ")";
            ctx.lineWidth = 1.15;
            ctx.beginPath();
            ctx.moveTo(pointer.x, pointer.y);
            ctx.lineTo(p.x, p.y);
            ctx.stroke();
          }
        }
      }
    }

    function drawParticles(time) {
      for (var i = 0; i < particles.length; i += 1) {
        var p = particles[i];
        var pulse = Math.sin(time * 1.6 + p.phase) * 0.45;
        var radius = p.r + pulse;
        var color = p.tone > 0.62 ? "64, 81, 181" : p.tone > 0.28 ? "8, 127, 140" : "184, 107, 47";
        var glow = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, radius * 6.2);

        glow.addColorStop(0, "rgba(" + color + ", 0.42)");
        glow.addColorStop(0.45, "rgba(" + color + ", 0.14)");
        glow.addColorStop(1, "rgba(" + color + ", 0)");
        ctx.fillStyle = glow;
        ctx.beginPath();
        ctx.arc(p.x, p.y, radius * 6.2, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = "rgba(" + color + ", 0.72)";
        ctx.beginPath();
        ctx.arc(p.x, p.y, Math.max(1.2, radius), 0, Math.PI * 2);
        ctx.fill();
      }
    }

    function animate(now) {
      var time = now * 0.001;
      ctx.clearRect(0, 0, width, height);
      drawOrbit(time);
      updateParticles(time);
      drawLinks();
      drawParticles(time);
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
