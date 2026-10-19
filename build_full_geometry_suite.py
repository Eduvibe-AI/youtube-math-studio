import os

def generate_page():
    # We will generate the entire rpm_pro_geometry_56_59.html with 42 questions
    html_code = '''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RPM Pro 중학 2-2 [56~59쪽] 평행사변형 시험만점 3초 초고속 일반화 공식 마스터</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+KR:wght@300;400;500;700;900&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  
  <!-- KaTeX -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});"></script>

  <style>
    :root {
      --bg-primary: #070a13;
      --bg-secondary: #0f172a;
      --bg-card: rgba(15, 23, 42, 0.88);
      --bg-card-hover: rgba(30, 41, 59, 0.95);
      --border-color: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(56, 189, 248, 0.35);
      --accent-blue: #38bdf8;
      --accent-gold: #fbbf24;
      --accent-purple: #c084fc;
      --accent-green: #34d399;
      --accent-rose: #fb7185;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 22px;
      --shadow-card: 0 16px 36px -12px rgba(0, 0, 0, 0.6), 0 0 0 1px var(--border-color);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg-primary);
      background-image: 
        radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.12) 0px, transparent 45%),
        radial-gradient(at 100% 0%, rgba(192, 132, 252, 0.12) 0px, transparent 50%),
        radial-gradient(at 50% 100%, rgba(251, 191, 36, 0.08) 0px, transparent 50%);
      background-attachment: fixed;
      color: var(--text-main);
      font-family: 'Inter', 'Noto Sans KR', sans-serif;
      line-height: 1.6;
      padding-bottom: 90px;
    }

    .container { max-width: 1320px; margin: 0 auto; padding: 0 24px; }
    
    /* Top Header Bar */
    header {
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-color);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 14px 0;
    }
    .header-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .logo-area {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .logo-badge {
      background: linear-gradient(135deg, #ef4444, #f43f5e);
      color: #fff;
      font-weight: 800;
      font-size: 14px;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: -0.5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .logo-title {
      font-size: 18px;
      font-weight: 700;
      color: #fff;
    }
    .header-links {
      display: flex;
      gap: 8px;
      align-items: center;
      flex-wrap: wrap;
    }
    .btn-nav {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      text-decoration: none;
      font-size: 13px;
      font-weight: 600;
      transition: all 0.2s;
    }
    .btn-nav:hover, .btn-nav.active {
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--accent-blue);
      color: #fff;
    }

    /* Hero Banner */
    .hero {
      padding: 36px 0 20px;
      text-align: center;
    }
    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 6px 16px;
      border-radius: 30px;
      font-size: 13px;
      font-weight: 700;
      color: var(--accent-blue);
      margin-bottom: 14px;
    }
    .hero h1 {
      font-size: 32px;
      font-weight: 800;
      line-height: 1.3;
      margin-bottom: 12px;
      background: linear-gradient(135deg, #ffffff 40%, #94a3b8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero p {
      font-size: 15px;
      color: var(--text-muted);
      max-width: 860px;
      margin: 0 auto;
    }

    /* 8 Master Formulas Banner */
    .cheatsheet-banner {
      background: linear-gradient(135deg, rgba(30, 58, 138, 0.4), rgba(88, 28, 135, 0.3));
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: var(--radius-lg);
      padding: 22px;
      margin-bottom: 28px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
    }
    .cheatsheet-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }
    .cheatsheet-title {
      font-size: 19px;
      font-weight: 700;
      color: var(--accent-gold);
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .formulas-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
      gap: 12px;
    }
    .formula-mini-card {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-md);
      padding: 12px 14px;
      transition: all 0.2s;
      cursor: pointer;
    }
    .formula-mini-card:hover {
      border-color: var(--accent-blue);
      transform: translateY(-2px);
      background: rgba(30, 41, 59, 0.9);
    }
    .f-badge {
      display: inline-block;
      font-size: 11px;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 4px;
      margin-bottom: 4px;
    }
    .f-title {
      font-size: 14.5px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 3px;
    }
    .f-desc {
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.4;
    }
    .f-apply {
      font-size: 11px;
      color: var(--accent-gold);
      margin-top: 5px;
      font-family: 'JetBrains Mono', monospace;
    }

    /* Category Navigation Bar */
    .category-nav-bar {
      display: flex;
      gap: 10px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }
    .cat-btn {
      padding: 10px 20px;
      border-radius: var(--radius-md);
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      font-size: 14.5px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .cat-btn:hover {
      background: rgba(30, 41, 59, 0.9);
      color: #fff;
      border-color: rgba(255, 255, 255, 0.2);
    }
    .cat-btn.active {
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.25), rgba(192, 132, 252, 0.25));
      border-color: var(--accent-blue);
      color: #fff;
      box-shadow: 0 0 16px rgba(56, 189, 248, 0.25);
    }
    .cat-badge {
      padding: 2px 7px;
      border-radius: 9999px;
      font-size: 11.5px;
      background: rgba(255, 255, 255, 0.1);
      color: #93c5fd;
    }
    .cat-btn.active .cat-badge {
      background: #0284c7;
      color: #fff;
    }

    /* Page Tabs & Filters */
    .filter-bar {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      margin-bottom: 22px;
      background: rgba(15, 23, 42, 0.6);
      padding: 12px 18px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
    }
    .tab-group {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .tab-btn {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 7px 16px;
      border-radius: var(--radius-sm);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .tab-btn:hover, .tab-btn.active {
      background: var(--accent-blue);
      color: #070a13;
      border-color: var(--accent-blue);
      font-weight: 700;
    }
    .stat-badge {
      font-size: 13px;
      color: var(--text-muted);
      background: rgba(0, 0, 0, 0.4);
      padding: 6px 14px;
      border-radius: 20px;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Questions Grid */
    .questions-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 22px;
    }
    @media (min-width: 960px) {
      .questions-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    .q-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 22px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
      transition: transform 0.2s, border-color 0.2s;
    }
    .q-card:hover {
      border-color: var(--border-accent);
      transform: translateY(-2px);
    }
    .q-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
    }
    .q-card.vip::before {
      background: linear-gradient(90deg, #f59e0b, #ef4444);
    }
    .q-card.twin::before {
      background: linear-gradient(90deg, #10b981, #06b6d4);
    }
    .q-card.variation::before {
      background: linear-gradient(90deg, #f97316, #eab308);
    }
    .q-card.advanced::before {
      background: linear-gradient(90deg, #ec4899, #8b5cf6);
    }

    .q-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }
    .q-number-box {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .q-num {
      font-size: 19px;
      font-weight: 800;
      color: #fff;
    }
    .badge-tag {
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
    }
    .badge-red { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }
    .badge-amber { background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
    .badge-purple { background: rgba(168, 85, 247, 0.2); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); }
    .badge-blue { background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }
    .badge-green { background: rgba(52, 211, 153, 0.2); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.3); }

    .q-points {
      font-size: 12px;
      font-weight: 700;
      color: var(--text-dim);
      background: rgba(255, 255, 255, 0.05);
      padding: 2px 8px;
      border-radius: 4px;
    }

    .q-content {
      font-size: 14.5px;
      color: #e2e8f0;
      margin-bottom: 14px;
      line-height: 1.6;
    }

    .q-diagram-wrap {
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: var(--radius-md);
      padding: 12px;
      margin-bottom: 14px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .q-diagram-wrap svg {
      max-width: 100%;
      height: auto;
    }

    /* Answer & Method Boxes */
    .answer-tag {
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(52, 211, 153, 0.12);
      border: 1px solid rgba(52, 211, 153, 0.3);
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      margin-bottom: 12px;
    }
    .ans-label { font-size: 12px; font-weight: 800; color: var(--accent-green); }
    .ans-val { font-size: 16px; font-weight: 800; color: #fff; }

    .solution-box {
      border-radius: var(--radius-md);
      padding: 12px 14px;
      margin-bottom: 10px;
      font-size: 13px;
    }
    
    .sol-slow {
      background: rgba(239, 68, 68, 0.06);
      border-left: 3px solid #ef4444;
      color: #cbd5e1;
    }
    .sol-slow-title {
      font-weight: 700;
      color: #f87171;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .sol-fast {
      background: rgba(56, 189, 248, 0.08);
      border-left: 3px solid var(--accent-blue);
      border-top: 1px solid rgba(56, 189, 248, 0.15);
      border-right: 1px solid rgba(56, 189, 248, 0.15);
      border-bottom: 1px solid rgba(56, 189, 248, 0.15);
    }
    .sol-fast-title {
      font-weight: 800;
      color: var(--accent-blue);
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .sol-fast .formula-highlight {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 6px 10px;
      border-radius: 6px;
      font-family: 'JetBrains Mono', monospace;
      color: var(--accent-gold);
      font-weight: 600;
      margin: 6px 0;
      font-size: 13.5px;
    }

    .master-note {
      background: rgba(251, 191, 36, 0.07);
      border: 1px dashed rgba(251, 191, 36, 0.35);
      border-radius: var(--radius-sm);
      padding: 10px 12px;
      font-size: 12.5px;
      color: #fef08a;
      line-height: 1.5;
    }

    /* Modal for original scan */
    .modal-overlay {
      display: none;
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
      z-index: 999;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }
    .modal-overlay.active { display: flex; }
    .modal-box {
      max-width: 900px;
      max-height: 90vh;
      background: #0f172a;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      overflow: auto;
      padding: 20px;
      position: relative;
    }
    .modal-close {
      position: absolute;
      top: 14px;
      right: 14px;
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: #fff;
      font-size: 20px;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
    }

    /* Interactive Lab Box */
    .lab-box {
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid var(--border-accent);
      border-radius: var(--radius-lg);
      padding: 22px;
      margin: 36px 0;
    }
    .lab-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }
    .lab-title {
      font-size: 19px;
      font-weight: 800;
      color: var(--accent-blue);
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .canvas-controls {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 12px;
    }
    .btn-ctrl {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-color);
      color: #fff;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 13px;
      cursor: pointer;
      font-weight: 600;
    }
    .btn-ctrl.active {
      background: var(--accent-purple);
      border-color: var(--accent-purple);
    }
    #labCanvas {
      width: 100%;
      height: 340px;
      background: #080c17;
      border-radius: var(--radius-md);
      border: 1px solid rgba(255, 255, 255, 0.05);
      display: block;
    }
  </style>
</head>
<body>

  <header>
    <div class="container header-inner">
      <div class="logo-area">
        <span class="logo-badge">YouTube Math Studio</span>
        <span class="logo-title">RPM Pro 중학 2-2 · 평행사변형 3초 공식 & 심화응용 포털</span>
      </div>
      <div class="header-links">
        <a href="index.html" class="btn-nav">🏠 메인 포털</a>
        <a href="javascript:void(0)" onclick="openPageModal('56')" class="btn-nav">📄 56쪽 원본</a>
        <a href="javascript:void(0)" onclick="openPageModal('57')" class="btn-nav">📄 57쪽 원본</a>
        <a href="javascript:void(0)" onclick="openPageModal('58')" class="btn-nav">📄 58쪽 원본</a>
        <a href="javascript:void(0)" onclick="openPageModal('59')" class="btn-nav">📄 59쪽 원본</a>
        <a href="rpm_geometry_master_cheatsheet.png" target="_blank" class="btn-nav" style="background:#2563eb; color:#fff; border-color:#38bdf8;">📥 공식집 고화질 받기</a>
      </div>
    </div>
  </header>

  <div class="container">
    
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-badge">⚡ RPM Pro 중학 2-2 평행사변형 마스터 (본문 24제 + 유사 6제 + 변형 6제 + 1등급 심화 6제 = 총 42제)</div>
      <h1>답지의 긴 증명은 가라! 3초 만에 끝내는 평행사변형 킬러 공식</h1>
      <p>교재 답지의 번거로운 삼각형 합동 증명($\triangle \equiv \triangle$) 대신, 어떤 변형 문제가 나오더라도 눈으로 보자마자 3초 컷할 수 있는 8대 일반화 마스터 공식과 실전 쌍둥이·변형·심화 팩입니다.</p>
    </section>

    <!-- 8 Master Formulas Banner -->
    <section class="cheatsheet-banner">
      <div class="cheatsheet-header">
        <div class="cheatsheet-title">
          <span>🚀 시험장 킬러 무기 : 평행사변형 8대 절대 일반화 공식</span>
        </div>
        <span style="font-size:12px; color:var(--text-muted);">공식을 클릭하면 관련 문항들만 즉시 필터링됩니다.</span>
      </div>
      <div class="formulas-grid">
        <div class="formula-mini-card" onclick="filterByFormula('F1')">
          <span class="f-badge badge-amber">공식 01</span>
          <div class="f-title">엇각 + 내각 이등분선 = 100% 이등변</div>
          <div class="f-desc">평행선 사이 내각을 이등분하면 엇각에 의해 밑각이 같아져 무조건 $AB = BE$ 이등변!</div>
          <div class="f-apply">본문 233, 234, 242, 245, 250 / 변형 V1</div>
        </div>
        <div class="formula-mini-card" onclick="filterByFormula('F2')">
          <span class="f-badge badge-blue">공식 02</span>
          <div class="f-title">이웃한 두 내각의 이등분선 직교 ($90^\circ$)</div>
          <div class="f-desc">$\angle A + \angle B = 180^\circ \implies \frac{1}{2}(\angle A+\angle B) = 90^\circ$! 역성질: $90^\circ$ 교각이면 대변도 이등분선!</div>
          <div class="f-apply">본문 220, 245 / 유사 T2 / 변형 V2</div>
        </div>
        <div class="formula-mini-card" onclick="filterByFormula('F3')">
          <span class="f-badge badge-red">공식 03</span>
          <div class="f-title">종이 접기(대칭) 각도 보존 & 이등변</div>
          <div class="f-desc">[접은 각 = 원래 각 = 엇각] 삼위일체! 연장선 외각 $\theta$에 대해 $2x + \theta = 180^\circ$ 성립!</div>
          <div class="f-apply">본문 243, 246 / 유사 T3 / 변형 V6</div>
        </div>
        <div class="formula-mini-card" onclick="filterByFormula('F4')">
          <span class="f-badge badge-purple">공식 04</span>
          <div class="f-title">대각선 교점 $O$ = 직각삼각형 외심 정리</div>
          <div class="f-desc">대각선 중점 $O$는 수선 $\triangle AHC$의 빗변 중점 = **외심**! $OA=OC=OH \implies \triangle OHC$ 이등변!</div>
          <div class="f-apply">본문 247 / 유사 T4 / 변형 V4</div>
        </div>
        <div class="formula-mini-card" onclick="filterByFormula('F5')">
          <span class="f-badge badge-amber">공식 05</span>
          <div class="f-title">내부점 $P$ 대변 넓이 합 불변 & 밑변 공유식</div>
          <div class="f-desc">$S_{상} + S_{하} = S_{좌} + S_{우} = \frac{1}{2}\square$. 밑변 공유 $\triangle AQD = \frac{1}{2}\square = S_{PBC} + S_{PDA}$</div>
          <div class="f-apply">본문 248 / 유사 T5 / 변형 V5</div>
        </div>
        <div class="formula-mini-card" onclick="filterByFormula('F6')">
          <span class="f-badge badge-blue">공식 06</span>
          <div class="f-title">대변 중점 연결 사각형 1/4 격자 넓이</div>
          <div class="f-desc">대변 중점 연결 대각 교차 사각형 넓이는 항상 $\square AEGH = \frac{1}{4} \square ABCD$</div>
          <div class="f-apply">본문 241 / 유사 T6 / 심화 A5</div>
        </div>
        <div class="formula-mini-card" onclick="filterByFormula('F7')">
          <span class="f-badge badge-red">공식 07</span>
          <div class="f-title">변의 중점 관통선 모래시계 1:1 합동</div>
          <div class="f-desc">중점 관통선은 연장선과 1:1 합동 형성 $\implies$ 바깥 선분 = 본래 변 길이 = 밑변 전체의 $\frac{1}{2}$!</div>
          <div class="f-apply">본문 232, 252 / 변형 V3</div>
        </div>
        <div class="formula-mini-card" onclick="filterByFormula('F8')">
          <span class="f-badge badge-purple">공식 08</span>
          <div class="f-title">대각선 이등분 & 둘레/수선 대칭 공식</div>
          <div class="f-desc">$\triangle OCD$ 둘레 = $CD + \frac{1}{2}(AC + BD)$. 대각선 수선의 발 대칭 $\implies \square EBFD$ 평행사변형!</div>
          <div class="f-apply">본문 229, 231, 235, 239, 249, 251</div>
        </div>
      </div>
    </section>

    <!-- Category Tabs Bar -->
    <div class="category-nav-bar">
      <button class="cat-btn active" onclick="switchCategory('all')">
        <span>✨ 전체 문항 보기</span>
        <span class="cat-badge">42</span>
      </button>
      <button class="cat-btn" onclick="switchCategory('original')">
        <span>📘 교재 본문 24제</span>
        <span class="cat-badge">24</span>
      </button>
      <button class="cat-btn" onclick="switchCategory('twin')">
        <span>👯 유사·쌍둥이 팩</span>
        <span class="cat-badge">6</span>
      </button>
      <button class="cat-btn" onclick="switchCategory('variation')">
        <span>🔄 실전 내신 변형 팩</span>
        <span class="cat-badge">6</span>
      </button>
      <button class="cat-btn" onclick="switchCategory('advanced')">
        <span>🔥 1등급 킬러 심화 팩</span>
        <span class="cat-badge">6</span>
      </button>
    </div>

    <!-- Secondary Filter Bar -->
    <div class="filter-bar">
      <div class="tab-group" id="pageTabGroup">
        <button class="tab-btn active" onclick="filterPage('all')">전체 쪽수</button>
        <button class="tab-btn" onclick="filterPage('56')">56쪽 (229~235)</button>
        <button class="tab-btn" onclick="filterPage('57')">57쪽 (236~242)</button>
        <button class="tab-btn" onclick="filterPage('58')">58쪽 (243~248)</button>
        <button class="tab-btn" onclick="filterPage('59')">59쪽 (249~252)</button>
      </div>
      <div class="stat-badge" id="statBadge">
        현재 <strong style="color:var(--accent-blue);" id="countDisplay">42문항</strong> 표시 중
      </div>
    </div>

    <!-- Interactive Geometry Lab -->
    <section class="lab-box">
      <div class="lab-header">
        <div class="lab-title">
          <span>🧪 인터랙티브 기하 실험실 (눈으로 증명하는 일반화 공식)</span>
        </div>
        <div class="canvas-controls">
          <button class="btn-ctrl active" onclick="setLabMode('bisector')">1. 이등분선+이등변 원리</button>
          <button class="btn-ctrl" onclick="setLabMode('internal_point')">2. 내부점 P 넓이 보존</button>
          <button class="btn-ctrl" onclick="setLabMode('circumcenter')">3. 대각선 교점 외심 원리</button>
          <button class="btn-ctrl" onclick="setLabMode('folding')">4. 종이접기 대칭각</button>
        </div>
      </div>
      <canvas id="labCanvas" width="1200" height="340"></canvas>
      <div id="labDesc" style="margin-top:10px; font-size:13px; color:var(--text-muted);">
        마우스로 점을 드래그하거나 모드를 변경하여 공식이 왜 언제나 성립하는지 시각적으로 확인하세요.
      </div>
    </section>

    <!-- Questions Grid Container -->
    <div class="questions-grid" id="questionsContainer">
      <!-- Generated via JS below -->
    </div>

  </div>

  <!-- Page Image Modal -->
  <div class="modal-overlay" id="pageModal" onclick="closePageModal(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <button class="modal-close" onclick="closePageModal()">&times;</button>
      <h3 id="modalTitle" style="color:var(--accent-blue); margin-bottom:14px; font-size:18px;"></h3>
      <img id="modalImg" src="" alt="교재 원본" style="width:100%; height:auto; border-radius:8px;">
    </div>
  </div>

  <script src="rpm_questions_data.js"></script>
  <script>
    let currentCategory = 'all';
    let currentPage = 'all';
    let currentFormula = 'all';

    function switchCategory(cat) {
      currentCategory = cat;
      currentPage = 'all';
      currentFormula = 'all';
      document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
      event.currentTarget.classList.add('active');
      document.querySelectorAll('#pageTabGroup .tab-btn').forEach((b, idx) => {
        if (idx === 0) b.classList.add('active');
        else b.classList.remove('active');
      });
      applyFilters();
    }

    function filterPage(pg) {
      currentPage = pg;
      currentFormula = 'all';
      document.querySelectorAll('#pageTabGroup .tab-btn').forEach(b => b.classList.remove('active'));
      event.currentTarget.classList.add('active');
      applyFilters();
    }

    function filterByFormula(fCode) {
      currentFormula = fCode;
      applyFilters();
      document.getElementById('questionsContainer').scrollIntoView({ behavior: 'smooth' });
    }

    function applyFilters() {
      let filtered = allQuestions;
      if (currentCategory !== 'all') {
        filtered = filtered.filter(q => q.category === currentCategory);
      }
      if (currentPage !== 'all') {
        filtered = filtered.filter(q => q.page === currentPage);
      }
      if (currentFormula !== 'all') {
        filtered = filtered.filter(q => q.formula === currentFormula);
      }
      renderQuestions(filtered);
      document.getElementById('countDisplay').innerText = `${filtered.length}문항`;
    }

    // Render questions to grid
    function renderQuestions(list) {
      const container = document.getElementById('questionsContainer');
      container.innerHTML = list.map(q => `
        <div class="q-card ${q.cardClass || ''}" data-category="${q.category}">
          <div class="q-header">
            <div class="q-number-box">
              <span class="q-num">${q.num}</span>
              <span class="badge-tag ${q.badgeClass}">${q.badge}</span>
              <span class="badge-tag badge-purple">${q.pageBadge || q.page + '쪽'}</span>
            </div>
            <span class="q-points">${q.score}</span>
          </div>

          <h3 style="font-size:16.5px; font-weight:700; color:#fff; margin-bottom:8px;">${q.title}</h3>
          <div class="q-content">${q.text}</div>

          ${q.choices && q.choices.length > 0 ? `
            <div style="display:flex; flex-wrap:wrap; gap:8px; margin-bottom:14px; font-size:13px; color:#94a3b8;">
              ${q.choices.map(c => `<span style="background:rgba(255,255,255,0.04); padding:3px 8px; border-radius:4px;">${c}</span>`).join('')}
            </div>
          ` : ''}

          <div class="q-diagram-wrap">
            ${q.svg}
          </div>

          <div class="answer-tag">
            <span class="ans-label">FINAL 정답</span>
            <span class="ans-val">${q.ans}</span>
          </div>

          <div class="solution-box sol-slow">
            <div class="sol-slow-title">❌ 교재 답지식 긴 증명 풀이 (시간 낭비 주의)</div>
            <div>${q.slow}</div>
          </div>

          <div class="solution-box sol-fast">
            <div class="sol-fast-title">⚡ 3초 마스터 초고속 일반화 공식</div>
            <div>${q.fast}</div>
          </div>

          <div class="master-note">
            <strong>💡 시험 변형 킬러 팁:</strong> ${q.note}
          </div>
        </div>
      `).join('');

      if (window.renderMathInElement) {
        renderMathInElement(container, {
          delimiters: [
            {left: '$$', right: '$$', display: true},
            {left: '$', right: '$', display: false}
          ]
        });
      }
    }

    // Modal
    function openPageModal(pg) {
      const modal = document.getElementById('pageModal');
      const title = document.getElementById('modalTitle');
      const img = document.getElementById('modalImg');
      title.innerText = `RPM Pro 중학 2-2 [${pg}쪽] 교재 고화질 원본 스캔본`;
      img.src = `rpm_pro_pages/page_${pg}.png`;
      modal.classList.add('active');
    }
    function closePageModal() {
      document.getElementById('pageModal').classList.remove('active');
    }

    // Initial render
    window.addEventListener('DOMContentLoaded', () => {
      applyFilters();
      initLab();
    });

    // Interactive Lab Canvas
    let labMode = 'bisector';
    function setLabMode(m) {
      labMode = m;
      document.querySelectorAll('.btn-ctrl').forEach(b => b.classList.remove('active'));
      event.currentTarget.classList.add('active');
      drawLab();
    }

    function initLab() {
      const canvas = document.getElementById('labCanvas');
      window.addEventListener('resize', drawLab);
      drawLab();
    }

    function drawLab() {
      const canvas = document.getElementById('labCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width = canvas.parentElement.clientWidth - 44;
      const h = canvas.height = 320;

      ctx.clearRect(0, 0, w, h);

      if (labMode === 'bisector') {
        document.getElementById('labDesc').innerHTML = 
          "<strong style='color:#38bdf8;'>[공식 1: 엇각+이등분선]</strong> 평행선 사이에서 각 $\\\\angle A$의 이등분선 $AE$를 그으면 $\\\\angle BAE = \\\\angle DAE$(이등분) = $\\\\angle BEA$(엇각)이 되어 <strong>$\\\\triangle ABE$는 100% 이등변삼각형($AB = BE$)</strong>이 됩니다!";
        
        const bx = w * 0.15, by = h * 0.8;
        const ax = w * 0.3, ay = h * 0.2;
        const dx = w * 0.8, dy = h * 0.2;
        const cx = w * 0.65, cy = h * 0.8;

        ctx.beginPath();
        ctx.moveTo(bx, by); ctx.lineTo(ax, ay); ctx.lineTo(dx, dy); ctx.lineTo(cx, cy); ctx.closePath();
        ctx.fillStyle = "rgba(56, 189, 248, 0.05)"; ctx.fill();
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5; ctx.stroke();

        const abDist = Math.hypot(ax - bx, ay - by);
        const ex = bx + abDist * 1.3;
        const ey = by;

        ctx.beginPath();
        ctx.moveTo(bx, by); ctx.lineTo(ax, ay); ctx.lineTo(ex, ey); ctx.closePath();
        ctx.fillStyle = "rgba(244, 63, 94, 0.2)"; ctx.fill();

        ctx.beginPath(); ctx.moveTo(ax, ay); ctx.lineTo(ex, ey); ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 3; ctx.stroke();

        ctx.fillStyle = "#fff"; ctx.font = "bold 15px Inter, Noto Sans KR";
        ctx.fillText("A", ax - 15, ay - 10);
        ctx.fillText("B", bx - 20, by + 15);
        ctx.fillText("C", cx + 15, cy + 15);
        ctx.fillText("D", dx + 15, dy - 10);
        ctx.fillText("E", ex, ey + 22);

        ctx.fillStyle = "#fbbf24";
        ctx.fillText("● (이등분)", ax + 10, ay + 28);
        ctx.fillText("● (엇각)", ex - 25, ey - 15);
        ctx.fillStyle = "#34d399";
        ctx.fillText("AB = BE (무조건 이등변!)", (bx + ex)/2 - 60, by - 20);

      } else if (labMode === 'internal_point') {
        document.getElementById('labDesc').innerHTML = 
          "<strong style='color:#fbbf24;'>[공식 5: 내부점 P 넓이 보존]</strong> 내부 점 $P$에 대해 상하 삼각형 넓이의 합($S_{상}+S_{하}$)은 좌우 삼각형 넓이의 합($S_{좌}+S_{우}$)과 항상 같고, 전체 평행사변형 넓이의 정확히 $\\\\frac{1}{2}$입니다!";

        const bx = w * 0.15, by = h * 0.8;
        const ax = w * 0.28, ay = h * 0.2;
        const dx = w * 0.82, dy = h * 0.2;
        const cx = w * 0.69, cy = h * 0.8;
        const px = w * 0.48, py = h * 0.45;

        ctx.beginPath();
        ctx.moveTo(ax, ay); ctx.lineTo(dx, dy); ctx.lineTo(px, py); ctx.closePath();
        ctx.fillStyle = "rgba(56, 189, 248, 0.25)"; ctx.fill();

        ctx.beginPath();
        ctx.moveTo(bx, by); ctx.lineTo(cx, cy); ctx.lineTo(px, py); ctx.closePath();
        ctx.fillStyle = "rgba(56, 189, 248, 0.25)"; ctx.fill();

        ctx.beginPath();
        ctx.moveTo(ax, ay); ctx.lineTo(bx, by); ctx.lineTo(px, py); ctx.closePath();
        ctx.fillStyle = "rgba(192, 132, 252, 0.25)"; ctx.fill();

        ctx.beginPath();
        ctx.moveTo(dx, dy); ctx.lineTo(cx, cy); ctx.lineTo(px, py); ctx.closePath();
        ctx.fillStyle = "rgba(192, 132, 252, 0.25)"; ctx.fill();

        ctx.beginPath();
        ctx.moveTo(bx, by); ctx.lineTo(ax, ay); ctx.lineTo(dx, dy); ctx.lineTo(cx, cy); ctx.closePath();
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(ax, ay); ctx.lineTo(px, py);
        ctx.moveTo(bx, by); ctx.lineTo(px, py);
        ctx.moveTo(cx, cy); ctx.lineTo(px, py);
        ctx.moveTo(dx, dy); ctx.lineTo(px, py);
        ctx.strokeStyle = "rgba(255,255,255,0.4)"; ctx.lineWidth = 1.5; ctx.stroke();

        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px JetBrains Mono";
        ctx.fillText("S(상)", (ax+dx)/2 - 15, ay + 30);
        ctx.fillText("S(하)", (bx+cx)/2 - 15, by - 15);
        ctx.fillStyle = "#c084fc";
        ctx.fillText("S(좌)", ax - 5, (ay+by)/2);
        ctx.fillText("S(우)", dx - 30, (dy+cy)/2);

        ctx.fillStyle = "#f43f5e";
        ctx.beginPath(); ctx.arc(px, py, 5, 0, Math.PI*2); ctx.fill();
        ctx.fillText("P", px + 10, py - 5);

      } else if (labMode === 'circumcenter') {
        document.getElementById('labDesc').innerHTML = 
          "<strong style='color:#f43f5e;'>[공식 4: 대각선 교점 O = 외심]</strong> 직각삼각형 $\\\\triangle AHC$에서 빗변의 중점 $O$는 외심입니다. 따라서 $OA = OC = OH$가 되어 $\\\\triangle OHC$는 항상 이등변삼각형이 됩니다!";

        const bx = w * 0.15, by = h * 0.8;
        const ax = w * 0.3, ay = h * 0.2;
        const dx = w * 0.8, dy = h * 0.2;
        const cx = w * 0.65, cy = h * 0.8;
        const hx = ax, hy = by;
        const ox = (ax + cx) / 2, oy = (ay + cy) / 2;

        ctx.beginPath();
        ctx.moveTo(bx, by); ctx.lineTo(ax, ay); ctx.lineTo(dx, dy); ctx.lineTo(cx, cy); ctx.closePath();
        ctx.strokeStyle = "rgba(255,255,255,0.2)"; ctx.lineWidth = 1.5; ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(ax, ay); ctx.lineTo(hx, hy); ctx.lineTo(cx, cy); ctx.closePath();
        ctx.fillStyle = "rgba(251, 191, 36, 0.15)"; ctx.fill();
        ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2; ctx.stroke();

        ctx.beginPath(); ctx.moveTo(ax, ay); ctx.lineTo(cx, cy); ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2; ctx.stroke();
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(hx, hy); ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5; ctx.stroke();

        ctx.fillStyle = "#f43f5e";
        ctx.beginPath(); ctx.arc(ox, oy, 6, 0, Math.PI*2); ctx.fill();
        ctx.fillText("O (외심!)", ox + 10, oy);

        ctx.fillStyle = "#fff";
        ctx.fillText("H (90°)", hx - 20, hy + 20);
        ctx.fillText("A", ax - 15, ay - 10);
        ctx.fillText("C", cx + 10, cy + 15);

        ctx.fillStyle = "#34d399"; ctx.font = "bold 13px Inter, Noto Sans KR";
        ctx.fillText("OA = OC = OH (외심 반지름)", ox - 50, oy + 40);

      } else if (labMode === 'folding') {
        document.getElementById('labDesc').innerHTML = 
          "<strong style='color:#34d399;'>[공식 3: 종이접기 대칭각]</strong> 선을 따라 접으면 [접은 각 = 원래 각]이 되고, 평행선 엇각과 같아지므로 접힌 삼각형 $\\\\triangle FBD$는 무조건 $FB = FD$인 이등변삼각형이 됩니다!";

        const bx = w * 0.2, by = h * 0.8;
        const dx = w * 0.8, dy = h * 0.3;
        const fx = w * 0.15, fy = h * 0.15;

        ctx.beginPath();
        ctx.moveTo(bx, by); ctx.lineTo(dx, dy); ctx.lineTo(fx, fy); ctx.closePath();
        ctx.fillStyle = "rgba(52, 211, 153, 0.2)"; ctx.fill();
        ctx.strokeStyle = "#34d399"; ctx.lineWidth = 2.5; ctx.stroke();

        ctx.fillStyle = "#fff";
        ctx.fillText("B", bx - 15, by + 15);
        ctx.fillText("D", dx + 15, dy);
        ctx.fillText("F", fx - 10, fy - 10);

        ctx.fillStyle = "#fbbf24";
        ctx.fillText("86° (꼭지각)", fx + 15, fy + 20);
        ctx.fillText("x (밑각)", bx + 25, by - 20);
        ctx.fillText("x (밑각)", dx - 55, dy + 20);

        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 14px JetBrains Mono";
        ctx.fillText("2x + 86° = 180° => x = 47°", w * 0.45, h * 0.6);
      }
    }
  </script>
</body>
</html>
'''
    with open('rpm_pro_geometry_56_59.html', 'w', encoding='utf-8') as f:
        f.write(html_code)
    print("Base template written to rpm_pro_geometry_56_59.html")

if __name__ == '__main__':
    generate_page()
