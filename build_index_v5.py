# -*- coding: utf-8 -*-
"""
Script to inject Lecture 5 (Euclid's Pythagorean Theorem Proof) into index.html
Preserving all existing Lectures 1, 2, 3, 4 without alteration.
"""

import os

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the lecture switcher bar
    old_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (4 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec4" onclick="setLecture(4)">
          <span class="badge-pill-sm">신규 강의</span>
          다항함수 비율관계는 단 하나! ($m:n$ 내분점)
        </button>'''

    new_switcher_head = '''    <!-- TOP LECTURE SELECTOR BAR (5 LECTURES) -->
    <div class="lecture-switcher-bar">
      <div class="lecture-switcher">
        <button class="lecture-btn active" id="btnLec5" onclick="setLecture(5)">
          <span class="badge-pill-sm">최신 강의</span>
          피타고라스 정리 (유클리드 증명)
        </button>
        <button class="lecture-btn" id="btnLec4" onclick="setLecture(4)">
          다항함수 비율관계는 단 하나! ($m:n$ 내분점)
        </button>'''

    if old_switcher_head not in content:
        print("ERROR: old_switcher_head not found in index.html!")
        return

    content = content.replace(old_switcher_head, new_switcher_head, 1)

    # 2. Update lecture4View to start hidden:
    old_lec4_start = '<div id="lecture4View">'
    new_lec4_start = '<div id="lecture4View" style="display: none;">'
    if old_lec4_start not in content:
        print("ERROR: old_lec4_start not found!")
        return

    # Lecture 5 Section HTML
    lecture5_html = r'''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 5 (PYTHAGOREAN THEOREM: EUCLID'S PROOF)    -->
    <!-- ============================================================== -->
    <div id="lecture5View">
      <header>
        <div class="badge-pill" style="border-color: rgba(56, 189, 248, 0.4); color: var(--accent-blue);">
          <span>📐 중학교 2학년 2학기 기하 · 피타고라스 정리의 꽃</span>
        </div>
        <h1>피타고라스의 정리 — 유클리드(Euclid) 증명법의 본질</h1>
        <p class="subtitle">
          직각삼각형의 세 변을 한 변으로 하는 세 정사각형의 넓이 관계를 <strong>밑변과 높이가 같은 삼각형의 등적변형</strong> 및 <strong>$SAS$ 합동</strong>으로 완벽하게 증명하는 유클리드 원론(Elements) 제1권 47번 명제!
        </p>

        <div class="source-meta">
          <span>🎬 채널: <strong>너도 아는 수학 (@yisrisri_math)</strong></span>
          <span>•</span>
          <a href="https://youtube.com/shorts/mHLirHeKkiQ" target="_blank" rel="noopener">
            <span>YouTube Shorts 영상 보기</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          </a>
        </div>
      </header>

      <!-- Tab Bar for Lecture 5 -->
      <div class="tab-bar">
        <button class="tab-btn active" onclick="switchLec5Tab('l5SimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          인터랙티브 유클리드 등적변형 시뮬레이터
        </button>
        <button class="tab-btn" onclick="switchLec5Tab('l5CaptureTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          강의 판서 캡처 & 타임라인 (7단계)
        </button>
        <button class="tab-btn" onclick="switchLec5Tab('l5ProofTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>
          수학교과서식 정형화 & 내신/수능 기출 연계
        </button>
        <button class="tab-btn" onclick="switchLec5Tab('l5ManimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          3Blue1Brown Manim 파이썬 코드
        </button>
      </div>

      <!-- TAB 1: INTERACTIVE SIMULATOR (LECTURE 5) -->
      <div id="l5SimTab" class="tab-panel active">
        <div class="glass-card">
          <!-- Formula Banner -->
          <div class="formula-banner">
            <div class="label">🌟 유클리드 원론(Elements) Book I, Prop. 47 핵심 등식</div>
            <div class="math-main">
              $$\triangle IAG = \triangle IAD \equiv \triangle GAB = \triangle JAB \implies \square AHGI = \text{직사각형 } ABJK = a^2$$
              $$\mathbf{a^2 + b^2 = c^2 \iff \square AHGI + \square GDEF = \square ABCD}$$
            </div>
          </div>

          <div class="sim-grid">
            <!-- Canvas Box -->
            <div class="canvas-box">
              <canvas id="l5Canvas" width="560" height="520"></canvas>
              <div style="font-size: 0.85rem; color: var(--text-dim); margin-top: 10px; text-align: center;">
                직각삼각형 $\triangle AGD$ ($\angle G = 90^\circ$)와 세 정사각형 $\square AHGI(a^2)$, $\square GDEF(b^2)$, $\square ABCD(c^2)$ 및 등적분할선 $GKJ$
              </div>
            </div>

            <!-- Controls & Live Evaluation -->
            <div class="sim-controls">
              <!-- Step Controller -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎬 유클리드 8단계 증명 프로세스</span>
                  <span class="badge-pill-sm" id="l5StepBadge" style="background: var(--accent-blue); color: #000; font-weight: 700;">Step 0 / 8</span>
                </div>

                <div style="margin-bottom: 12px;">
                  <input type="range" id="l5StepSlider" min="0" max="8" value="0" step="1" oninput="setL5Step(this.value)" style="width: 100%; accent-color: var(--accent-blue);">
                </div>

                <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                  <button class="preset-btn" onclick="prevL5Step()" style="flex: 1; text-align: center; padding: 8px;">◀ 이전</button>
                  <button class="preset-btn" id="l5AutoPlayBtn" onclick="toggleL5AutoPlay()" style="flex: 1.5; text-align: center; padding: 8px; background: rgba(56, 189, 248, 0.15); color: var(--accent-blue);">▶ 자동 재생</button>
                  <button class="preset-btn" onclick="nextL5Step()" style="flex: 1; text-align: center; padding: 8px;">다음 ▶</button>
                </div>

                <div id="l5StepDescCard" style="background: rgba(15, 23, 42, 0.7); border-radius: var(--radius-sm); border: 1px solid var(--border-color); padding: 14px; margin-top: 12px; font-size: 0.88rem; line-height: 1.6;">
                  <div id="l5StepTitle" style="color: var(--accent-gold); font-weight: 700; margin-bottom: 4px;">Step 0: 초기 작도 (기본 도형 설정)</div>
                  <div id="l5StepText" style="color: var(--text-muted);">직각삼각형 $\triangle AGD$의 세 변에 각각 정사각형 $AHGI(a^2)$, $GDEF(b^2)$, $ABCD(c^2)$를 작도하고, 꼭짓점 $G$에서 밑변 $BC$에 수선 $GKJ$를 내립니다.</div>
                </div>
              </div>

              <!-- Triangle Sides Controller -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎛️ 직각삼각형 변의 길이 ($a, b$) 조절</span>
                </div>
                
                <div class="preset-grid" style="grid-template-columns: repeat(2, 1fr); margin-bottom: 12px;">
                  <button class="preset-btn active" id="p5btn-345" onclick="setL5Preset(3, 4)">
                    <span>$a=3, b=4$ ($c=5$)</span>
                    <span class="p-sub">기본 피타고라스 수</span>
                  </button>
                  <button class="preset-btn" id="p5btn-51213" onclick="setL5Preset(5, 12)">
                    <span>$a=5, b=12$ ($c=13$)</span>
                    <span class="p-sub">유명 피타고라스 수</span>
                  </button>
                  <button class="preset-btn" id="p5btn-6810" onclick="setL5Preset(6, 8)">
                    <span>$a=6, b=8$ ($c=10$)</span>
                    <span class="p-sub">2배 확대 삼각형</span>
                  </button>
                  <button class="preset-btn" id="p5btn-iso" onclick="setL5Preset(4, 4)">
                    <span>$a=4, b=4$ ($c=4\sqrt{2}$)</span>
                    <span class="p-sub">직각이등변삼각형</span>
                  </button>
                </div>

                <div class="slider-row">
                  <label>밑변 $a$: <strong id="l5aVal" style="color: var(--accent-blue);">3</strong></label>
                  <input type="range" id="l5a" min="2" max="8" value="3" step="0.5" oninput="updateL5FromSliders()">
                </div>
                <div class="slider-row">
                  <label>높이 $b$: <strong id="l5bVal" style="color: var(--accent-purple);">4</strong></label>
                  <input type="range" id="l5b" min="2" max="8" value="4" step="0.5" oninput="updateL5FromSliders()">
                </div>
              </div>

              <!-- Live Numeric Analysis -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">📊 실시간 넓이 및 피타고라스 등식 검증</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; text-align: center; margin-bottom: 12px;">
                  <div style="background: rgba(56, 189, 248, 0.08); padding: 10px; border-radius: var(--radius-sm); border: 1px solid rgba(56, 189, 248, 0.2);">
                    <div style="font-size: 0.76rem; color: var(--accent-blue); font-weight: 600;">좌측 정사각형 $a^2$</div>
                    <div id="l5AreaA" style="font-size: 1.25rem; font-weight: 800; color: #fff;">9.00</div>
                  </div>
                  <div style="background: rgba(192, 132, 252, 0.08); padding: 10px; border-radius: var(--radius-sm); border: 1px solid rgba(192, 132, 252, 0.2);">
                    <div style="font-size: 0.76rem; color: var(--accent-purple); font-weight: 600;">우측 정사각형 $b^2$</div>
                    <div id="l5AreaB" style="font-size: 1.25rem; font-weight: 800; color: #fff;">16.00</div>
                  </div>
                  <div style="background: rgba(251, 191, 36, 0.08); padding: 10px; border-radius: var(--radius-sm); border: 1px solid rgba(251, 191, 36, 0.2);">
                    <div style="font-size: 0.76rem; color: var(--accent-gold); font-weight: 600;">빗변 정사각형 $c^2$</div>
                    <div id="l5AreaC" style="font-size: 1.25rem; font-weight: 800; color: #fff;">25.00</div>
                  </div>
                </div>

                <div style="font-size: 0.86rem; color: var(--text-muted); background: rgba(255, 255, 255, 0.02); padding: 10px 14px; border-radius: var(--radius-sm); border: 1px solid var(--border-color);">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                    <span>빗변 길이 $c = \sqrt{a^2 + b^2}$:</span>
                    <strong id="l5cVal" style="color: var(--accent-green);">5.000</strong>
                  </div>
                  <div style="display: flex; justify-content: space-between;">
                    <span>등식 검증 ($a^2 + b^2 \stackrel{?}{=} c^2$):</span>
                    <strong id="l5SumCheck" style="color: var(--accent-gold);">9.00 + 16.00 = 25.00 (일치!)</strong>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: LECTURE CAPTURES & TIMELINE -->
      <div id="l5CaptureTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.35rem; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;">
            <span>📸</span> 강의 핵심 판서 캡처 & 7단계 완벽 타임라인 (너도 아는 수학)
          </h2>

          <div style="display: grid; grid-template-columns: 1fr; gap: 28px;">
            <!-- Step 1 -->
            <div class="control-card">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span class="control-title">01. [도입] 직각삼각형과 세 변 위의 정사각형 작도 (0:00)</span>
                <span class="badge-pill-sm" style="background: rgba(56, 189, 248, 0.2); color: var(--accent-blue);">도입 작도</span>
              </div>
              <div class="capture-img-wrapper">
                <img src="captures_v5/frame_01_0s.jpg" alt="피타고라스 정리 도입">
              </div>
              <div class="quote-box">
                "직각삼각형의 직각을 낀 두 변 $a, b$와 빗변 $c$에 각각 정사각형을 그리고, 꼭짓점 $G$에서 밑변으로 수선을 내립니다."
              </div>
              <div class="explanation-text">
                $\angle AGD = 90^\circ$인 직각삼각형의 변 $\overline{AG}$ 위에 정사각형 $AHGI$, 변 $\overline{GD}$ 위에 정사각형 $GDEF$, 빗변 $\overline{AD}$ 위에 정사각형 $ABCD$를 작도합니다. 꼭짓점 $G$에서 수선의 발 $K, J$를 내려 빗변의 큰 정사각형을 두 개의 직사각형 $ABJK$와 $JKCD$로 분할합니다.
              </div>
            </div>

            <!-- Step 2 -->
            <div class="control-card">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span class="control-title">02. [1단계] SAS 합동 — 삼각형 IAD와 삼각형 GAB (0:03)</span>
                <span class="badge-pill-sm" style="background: rgba(52, 211, 153, 0.2); color: var(--accent-green);">SAS 합동</span>
              </div>
              <div class="capture-img-wrapper">
                <img src="captures_v5/frame_02_3s.jpg" alt="SAS 합동">
              </div>
              <div class="quote-box">
                "$\overline{IA} = \overline{GA}$, $\overline{AD} = \overline{AB}$, 끼인각 $\angle IAD = 90^\circ + \angle A = \angle GAB$ 이므로 $\triangle IAD \equiv \triangle GAB$!"
              </div>
              <div class="explanation-text">
                삼각형 $\triangle IAD$를 시계 반대방향으로 점 $A$를 중심으로 $90^\circ$ 회전시키면 정확히 삼각형 $\triangle GAB$와 포개어집니다. 두 변의 길이와 그 사이 끼인각이 같으므로 <strong>$SAS$ 합동</strong>이 성립하며, 따라서 두 삼각형의 넓이는 완벽하게 같습니다.
              </div>
            </div>

            <!-- Step 3 -->
            <div class="control-card">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span class="control-title">03. [2단계] 평행선 사이의 등적변형 — 선분 AB ∥ 선분 GJ (0:06)</span>
                <span class="badge-pill-sm" style="background: rgba(251, 191, 36, 0.2); color: var(--accent-gold);">등적변형</span>
              </div>
              <div class="capture-img-wrapper">
                <img src="captures_v5/frame_03_6s.jpg" alt="평행선 사이 등적변형">
              </div>
              <div class="quote-box">
                "선분 $AB$와 수선 $GJ$는 평행하므로, 밑변 $AB$를 고정하고 꼭짓점을 $G$에서 $J$로 이동해도 삼각형의 넓이는 변하지 않습니다!"
              </div>
              <div class="explanation-text">
                $\overline{AB} \perp \overline{AD}$이고 수선 $\overline{GJ} \perp \overline{AD}$이므로 두 직선은 평행($\overline{AB} \parallel \overline{GJ}$)합니다. 따라서 밑변 $\overline{AB}$를 공유하는 $\triangle GAB$와 $\triangle JAB$는 높이가 같아 넓이가 일치합니다:
                $$\triangle GAB = \triangle JAB = \frac{1}{2} \text{직사각형 } ABJK$$
              </div>
            </div>

            <!-- Step 4 -->
            <div class="control-card">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span class="control-title">04. [3단계] 좌측 정사각형 넓이 = 좌측 직사각형 넓이 a² (0:09)</span>
                <span class="badge-pill-sm" style="background: rgba(56, 189, 248, 0.2); color: var(--accent-blue);">좌측 정복 a²</span>
              </div>
              <div class="capture-img-wrapper">
                <img src="captures_v5/frame_04_9s.jpg" alt="좌측 직사각형 a^2">
              </div>
              <div class="quote-box">
                "따라서 좌측 정사각형 $AHGI$의 넓이는 빗변 위의 좌측 직사각형 $ABJK$의 넓이와 완벽히 같습니다! ($a^2$)"
              </div>
              <div class="explanation-text">
                $\square AHGI = 2 \times \triangle IAG = 2 \times \triangle IAD = 2 \times \triangle GAB = 2 \times \triangle JAB = \text{직사각형 } ABJK = a^2$.
                즉, 직각을 낀 한 변 위의 정사각형 넓이가 빗변 직사각형의 분할 넓이로 완벽하게 이전됩니다.
              </div>
            </div>

            <!-- Step 5 & 6 -->
            <div class="control-card">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span class="control-title">05. [4~5단계] 우측 정사각형의 등적변형 및 직사각형 b² 이전 (0:12 ~ 0:15)</span>
                <span class="badge-pill-sm" style="background: rgba(192, 132, 252, 0.2); color: var(--accent-purple);">우측 정복 b²</span>
              </div>
              <div class="capture-img-wrapper">
                <img src="captures_v5/frame_06_15s.jpg" alt="우측 직사각형 b^2">
              </div>
              <div class="quote-box">
                "마찬가지로 $\overline{GJ} \parallel \overline{DC}$이므로, 우측 정사각형 $GDEF$의 넓이도 빗변의 우측 직사각형 $JKCD$의 넓이와 같습니다! ($b^2$)"
              </div>
              <div class="explanation-text">
                우측 정사각형 $GDEF$에 대해서도 완벽히 대칭적으로 성립합니다:
                $$\triangle GDE = \triangle EAD \equiv \triangle GCD = \triangle JCD = \frac{1}{2} \text{직사각형 } JKCD$$
                $$\therefore \square GDEF = \text{직사각형 } JKCD = b^2$$
              </div>
            </div>

            <!-- Step 7 -->
            <div class="control-card">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span class="control-title">06. [6단계] 피타고라스의 정리 최종 완성 (0:18)</span>
                <span class="badge-pill-sm" style="background: rgba(251, 191, 36, 0.2); color: var(--accent-gold);">증명 종결</span>
              </div>
              <div class="capture-img-wrapper">
                <img src="captures_v5/frame_07_18s.jpg" alt="피타고라스 정리 완성">
              </div>
              <div class="quote-box">
                "빗변의 정사각형 $c^2$은 두 직사각형의 합이므로, $\mathbf{a^2 + b^2 = c^2}$이 성립합니다!"
              </div>
              <div class="explanation-text">
                빗변 $\overline{AD}$를 한 변으로 하는 큰 정사각형 $ABCD$의 넓이 $c^2$은 수선 $GKJ$에 의해 나뉜 두 직사각형 넓이의 합과 같습니다:
                $$\square ABCD = \text{직사각형 } ABJK + \text{직사각형 } JKCD = a^2 + b^2 = c^2$$
                이로써 기하학 역사상 가장 위대한 정리인 피타고라스 정리가 유클리드의 완벽한 논리로 증명되었습니다.
              </div>
            </div>

          </div>
        </div>
      </div>

      <!-- TAB 3: TEXTBOOK & EXAM LINKAGE -->
      <div id="l5ProofTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.35rem; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;">
            <span>📖</span> 대한민국 중학교 2학년 2학기 수학교과서식 정형화 & 기출 족보
          </h2>

          <div class="control-card" style="margin-bottom: 24px;">
            <div style="font-size: 0.85rem; color: var(--accent-blue); font-weight: 700; margin-bottom: 6px;">[교과 단원명] 중학교 2학년 수학 (2학기) > V. 도형의 닮음과 피타고라스 정리 > 2. 피타고라스 정리</div>
            <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 12px;">생각 열기 (Open Thinking)</h3>
            <div style="color: var(--text-muted); font-size: 0.92rem; line-height: 1.65;">
              오른쪽 그림과 같이 직각을 낀 두 변의 길이가 각각 $a, b$이고 빗변의 길이가 $c$인 직각삼각형의 각 변을 한 변으로 하는 정사각형을 그릴 때, 가장 큰 정사각형의 넓이는 나머지 두 정사각형의 넓이의 합과 같을까? 고대 그리스의 수학자 유클리드는 보조선과 삼각형의 등적변형을 이용하여 이를 명쾌하게 증명하였다.
            </div>
          </div>

          <!-- Textbook Theorem Definition -->
          <div class="math-callout">
            <h3 style="color: var(--accent-blue); font-size: 1.05rem; margin-bottom: 10px;">📌 [정리] 피타고라스 정리 (Pythagorean Theorem)</h3>
            <p style="color: #fff; font-size: 0.95rem; line-height: 1.7;">
              직각삼각형에서 직각을 낀 두 변의 길이를 각각 $a, b$라 하고, 빗변의 길이를 $c$라 하면 다음 관계가 성립한다.
              $$\mathbf{a^2 + b^2 = c^2}$$
              즉, <strong>(빗변 위의 정사각형의 넓이) = (다른 두 변 위의 정사각형의 넓이의 합)</strong>
            </p>
          </div>

          <!-- 5 Equivalent Triangles Chart -->
          <div class="control-card" style="margin-bottom: 24px;">
            <div class="control-header">
              <span class="control-title" style="color: var(--accent-gold);">⚡ [내신 시험 100% 출제] 유클리드 증명 5대 동치 삼각형 암기 공식</span>
            </div>
            <div style="overflow-x: auto;">
              <table class="math-table">
                <thead>
                  <tr>
                    <th>삼각형 기호</th>
                    <th>넓이 관계</th>
                    <th>동치 사유 (교과서 근거)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>$\triangle IAG$</strong></td>
                    <td>$\frac{1}{2} a^2$</td>
                    <td>정사각형 $AHGI$의 대각선에 의한 절반</td>
                  </tr>
                  <tr>
                    <td><strong>$\triangle IAD$</strong></td>
                    <td>$\frac{1}{2} a^2$</td>
                    <td>$\overline{IA} \parallel \overline{GH}$, 밑변 $IA$ 공통 (등적변형)</td>
                  </tr>
                  <tr>
                    <td><strong>$\triangle GAB$</strong></td>
                    <td>$\frac{1}{2} a^2$</td>
                    <td>$\triangle IAD \equiv \triangle GAB$ ($SAS$ 합동: $IA=GA, AD=AB, \angle IAD=\angle GAB$)</td>
                  </tr>
                  <tr>
                    <td><strong>$\triangle KAB$</strong></td>
                    <td>$\frac{1}{2} a^2$</td>
                    <td>$\overline{AB} \parallel \overline{GJ}$, 밑변 $AB$ 공통 (등적변형)</td>
                  </tr>
                  <tr>
                    <td><strong>$\triangle JAB$</strong></td>
                    <td>$\frac{1}{2} a^2$</td>
                    <td>직사각형 $ABJK$의 대각선에 의한 절반 ($\frac{1}{2} \times \text{직사각형 } ABJK$)</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div style="margin-top: 12px; font-size: 0.88rem; color: #fca5a5; background: rgba(239, 68, 68, 0.1); padding: 10px 14px; border-radius: var(--radius-sm); border: 1px solid rgba(239, 68, 68, 0.2);">
              ⚠️ <strong>오답 함정 주의:</strong> $\triangle HIG$나 $\triangle GKD$ 등은 밑변이나 높이가 일치하지 않으므로 위 5개 삼각형과 넓이가 다릅니다. "다음 중 넓이가 나머지 넷과 다른 하나는?" 단골 오답 선지입니다.
            </div>
          </div>

          <!-- Textbook Examples -->
          <div class="control-card">
            <div class="control-header">
              <span class="control-title">✏️ 교과서 수준별 예제 및 풀이</span>
            </div>

            <!-- Example 1 -->
            <div style="border-bottom: 1px solid var(--border-color); padding-bottom: 16px; margin-bottom: 16px;">
              <div style="font-weight: 700; color: var(--accent-blue); margin-bottom: 6px;">[예제 1 - 기본 넓이 추론]</div>
              <p style="color: var(--text-main); font-size: 0.92rem; margin-bottom: 8px;">
                $\angle G = 90^\circ$인 직각삼각형 $AGD$에서 $\overline{AG} = 6\text{ cm}$, $\overline{GD} = 8\text{ cm}$일 때, 유클리드 작도에서 직사각형 $ABJK$의 넓이를 구하시오.
              </p>
              <div style="background: rgba(255, 255, 255, 0.03); padding: 12px; border-radius: var(--radius-sm); font-size: 0.88rem; color: var(--text-muted);">
                <strong>[풀이]</strong><br>
                유클리드 증명에 의해 정사각형 $AHGI$의 넓이와 직사각형 $ABJK$의 넓이는 같습니다.<br>
                정사각형 $AHGI$의 한 변의 길이는 $\overline{AG} = 6\text{ cm}$이므로,<br>
                $\text{직사각형 } ABJK = \square AHGI = 6^2 = \mathbf{36\text{ cm}^2}$.
              </div>
            </div>

            <!-- Example 2 -->
            <div style="border-bottom: 1px solid var(--border-color); padding-bottom: 16px; margin-bottom: 16px;">
              <div style="font-weight: 700; color: var(--accent-gold); margin-bottom: 6px;">[예제 2 - 내신 빈출 객관식 킬러]</div>
              <p style="color: var(--text-main); font-size: 0.92rem; margin-bottom: 8px;">
                다음 유클리드 증명 그림에서 넓이가 삼각형 $\triangle IAD$와 같지 <strong>않은</strong> 것은?<br>
                ① $\triangle IAG$ &nbsp;&nbsp;&nbsp; ② $\triangle GAB$ &nbsp;&nbsp;&nbsp; ③ $\triangle JAB$ &nbsp;&nbsp;&nbsp; ④ $\triangle KAB$ &nbsp;&nbsp;&nbsp; ⑤ $\triangle HIG$
              </p>
              <div style="background: rgba(255, 255, 255, 0.03); padding: 12px; border-radius: var(--radius-sm); font-size: 0.88rem; color: var(--text-muted);">
                <strong>[정답 및 해설] ⑤번</strong><br>
                $\triangle IAG, \triangle IAD, \triangle GAB, \triangle KAB, \triangle JAB$는 모두 밑변과 높이가 같거나 합동이므로 넓이가 정사각형 $AHGI$의 절반인 $\frac{1}{2}a^2$로 서로 같습니다.<br>
                반면 $\triangle HIG$는 정사각형 $AHGI$의 또 다른 대각선에 의한 절반이기는 하나, 문제의 변형 계열($AD$ 또는 $GJ$와 연계된 사슬)에 속하지 않거나 변형 조건에 부합하지 않으며, 특히 빗변 수선 쪽 삼각형 $\triangle GKD$ 등과 섞여 출제될 때 오답이 됩니다.
              </div>
            </div>

            <!-- Example 3 -->
            <div>
              <div style="font-weight: 700; color: var(--accent-green); margin-bottom: 6px;">[예제 3 - 고등/수능 연계: 직각삼각형의 사영정리(소 공식) 유도]</div>
              <p style="color: var(--text-main); font-size: 0.92rem; margin-bottom: 8px;">
                유클리드 증명에서 직각삼각형 $AGD$의 꼭짓점 $G$에서 빗변 $AD$에 내린 수선의 발을 $K$라 할 때, $\overline{AG}^2 = \overline{AK} \times \overline{AD}$가 성립함을 증명하시오.
              </p>
              <div style="background: rgba(255, 255, 255, 0.03); padding: 12px; border-radius: var(--radius-sm); font-size: 0.88rem; color: var(--text-muted);">
                <strong>[증명]</strong><br>
                정사각형 $ABCD$의 한 변의 길이는 $\overline{AD}$이므로 $\overline{AB} = \overline{AD}$입니다.<br>
                직사각형 $ABJK$의 가로의 길이는 $\overline{AK}$, 세로의 길이는 $\overline{AB} = \overline{AD}$이므로,<br>
                $$\text{직사각형 } ABJK = \overline{AK} \times \overline{AD}$$
                유클리드 정리에 의해 정사각형 $AHGI$의 넓이($\overline{AG}^2$)는 직사각형 $ABJK$의 넓이와 같으므로,<br>
                $$\mathbf{\overline{AG}^2 = \overline{AK} \times \overline{AD}}$$
                이는 고등학교 수학 도형과 기하에서 직각삼각형의 닮음비로 유도되는 <strong>사영정리(Projection Theorem)</strong>와 완벽히 일치합니다!
              </div>
            </div>

          </div>

        </div>
      </div>

      <!-- TAB 4: MANIM PYTHON SCRIPT (LECTURE 5) -->
      <div id="l5ManimTab" class="tab-panel">
        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <div>
              <h2 style="font-size: 1.35rem; color: #fff;">🎬 3Blue1Brown 스타일 Manim 파이썬 애니메이션 코드</h2>
              <p style="font-size: 0.88rem; color: var(--text-dim); margin-top: 4px;">
                `pythagorean_euclid_manim.py` — 유클리드 등적변형 및 $SAS$ 회전 합동 렌더링
              </p>
            </div>
            <button class="copy-btn" onclick="copyL5ManimCode()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right: 4px; vertical-align: middle;"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
              코드 복사하기
            </button>
          </div>

          <div class="code-container">
            <div class="code-header">
              <span style="font-size: 0.82rem; color: var(--accent-blue); font-family: 'JetBrains Mono', monospace;">pythagorean_euclid_manim.py</span>
              <span style="font-size: 0.78rem; color: var(--text-dim);">실행 명령어: manim -pql pythagorean_euclid_manim.py PythagoreanEuclidProof</span>
            </div>
            <pre><code id="l5ManimCodeText">from manim import *
import numpy as np

class PythagoreanEuclidProof(Scene):
    def construct(self):
        # 1. Title & Introduction
        title = Title(
            r"\textbf{피타고라스의 정리 — 유클리드 증명 (Euclid's Proof)}",
            font_size=38, color=BLUE_B
        )
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.75).to_corner(UL))

        # 2. Coordinates Setup for Right Triangle AGD
        c_len = 3.2
        A = np.array([-c_len / 2, 0.2, 0])
        D = np.array([c_len / 2, 0.2, 0])
        
        # 3-4-5 right triangle proportion
        theta = np.arccos(0.6)
        G = A + np.array([1.92 * np.cos(theta), 1.92 * np.sin(theta), 0])

        B = A + np.array([0, -c_len, 0])
        C = D + np.array([0, -c_len, 0])

        # Left square AHGI (side a):
        v_AG = G - A
        v_perp_AG = np.array([-v_AG[1], v_AG[0], 0])
        I = A + v_perp_AG
        H = G + v_perp_AG

        # Right square GDEF (side b):
        v_GD = D - G
        v_perp_GD = np.array([v_GD[1], -v_GD[0], 0])
        E = D + v_perp_GD
        F = G + v_perp_GD

        # Perpendicular line GKJ
        K = np.array([G[0], A[1], 0])
        J = np.array([G[0], B[1], 0])

        # 3. Draw Polygons & Labels
        tri_AGD = Polygon(A, G, D, color=WHITE, stroke_width=2.5, fill_color=DARK_BLUE, fill_opacity=0.3)
        sq_ABCD = Polygon(A, B, C, D, color=BLUE_D, stroke_width=2)
        sq_AHGI = Polygon(A, H, G, I, color=TEAL_D, stroke_width=2)
        sq_GDEF = Polygon(G, F, E, D, color=PURPLE_D, stroke_width=2)
        line_GJ = DashedLine(G, J, color=YELLOW, stroke_width=2)

        self.play(Create(tri_AGD), Create(sq_ABCD), Create(sq_AHGI), Create(sq_GDEF))
        self.play(Create(line_GJ))

        # 4. Step 1: Area of IAG = 1/2 AHGI
        tri_IAG = Polygon(I, A, G, color=TEAL_A, fill_color=TEAL, fill_opacity=0.55)
        self.play(FadeIn(tri_IAG))

        # 5. Step 2: Shear tri_IAG -> tri_IAD (Base IA parallel to GH)
        tri_IAD = Polygon(I, A, D, color=TEAL_A, fill_color=TEAL, fill_opacity=0.55)
        self.play(Transform(tri_IAG, tri_IAD))

        # 6. Step 3: SAS Congruence: tri_IAD === tri_GAB (Rotation by 90 deg)
        tri_GAB = Polygon(G, A, B, color=GREEN_B, fill_color=GREEN, fill_opacity=0.55)
        self.play(Transform(tri_IAG, tri_GAB))

        # 7. Step 4: Shear tri_GAB -> tri_JAB (Base AB parallel to GJ)
        tri_JAB = Polygon(J, A, B, color=GREEN_B, fill_color=GREEN, fill_opacity=0.55)
        self.play(Transform(tri_IAG, tri_JAB))

        # 8. Step 5: Area(Square AHGI) = Area(Rectangle ABJK) = a^2
        rect_ABJK = Polygon(A, B, J, K, color=TEAL, fill_color=TEAL, fill_opacity=0.6)
        sq_AHGI_f = Polygon(A, H, G, I, color=TEAL, fill_color=TEAL, fill_opacity=0.6)
        self.play(FadeOut(tri_IAG), FadeIn(sq_AHGI_f), FadeIn(rect_ABJK))

        # 9. Step 6: Right Side: Square GDEF = Rectangle JKCD = b^2
        rect_JKCD = Polygon(K, J, C, D, color=PURPLE, fill_color=PURPLE, fill_opacity=0.6)
        sq_GDEF_f = Polygon(G, F, E, D, color=PURPLE, fill_color=PURPLE, fill_opacity=0.6)
        self.play(FadeIn(sq_GDEF_f), FadeIn(rect_JKCD))

        # 10. Conclusion: a^2 + b^2 = c^2
        final_formula = MathTex(r"\mathbf{a^2 + b^2 = c^2}", font_size=46, color=YELLOW).to_edge(DOWN)
        self.play(Write(final_formula))
        self.play(Circumscribe(final_formula, color=GOLD))
        self.wait(3)</code></pre>
          </div>
        </div>
      </div>

    </div>
'''

    content = content.replace(old_lec4_start, lecture5_html + '\n\n    ' + new_lec4_start, 1)

    # 3. Update JavaScript section:
    old_script_head = '''    /* ========================================================= */
    /* GLOBAL LECTURE SWITCHER (LECTURES 1, 2, 3, 4)             */
    /* ========================================================= */
    function setLecture(num) {
      for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`btnLec${i}`);
        const view = document.getElementById(`lecture${i}View`);
        if (btn) btn.classList.toggle('active', i === num);
        if (view) view.style.display = (i === num) ? 'block' : 'none';
      }

      if (num === 4) setTimeout(renderL4, 50);
      else if (num === 3) setTimeout(renderL3, 50);
      else if (num === 2) setTimeout(renderL2, 50);
      else if (num === 1) setTimeout(renderL1, 50);

      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }'''

    new_script_head = '''    /* ========================================================= */
    /* GLOBAL LECTURE SWITCHER (LECTURES 1, 2, 3, 4, 5)          */
    /* ========================================================= */
    function setLecture(num) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`btnLec${i}`);
        const view = document.getElementById(`lecture${i}View`);
        if (btn) btn.classList.toggle('active', i === num);
        if (view) view.style.display = (i === num) ? 'block' : 'none';
      }

      if (num === 5) setTimeout(renderL5, 50);
      else if (num === 4) setTimeout(renderL4, 50);
      else if (num === 3) setTimeout(renderL3, 50);
      else if (num === 2) setTimeout(renderL2, 50);
      else if (num === 1) setTimeout(renderL1, 50);

      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function switchLec5Tab(tabId) {
      document.querySelectorAll('#lecture5View .tab-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('#lecture5View .tab-btn').forEach(b => b.classList.remove('active'));
      const activePanel = document.getElementById(tabId);
      if (activePanel) activePanel.classList.add('active');
      event.currentTarget.classList.add('active');
      if (tabId === 'l5SimTab') setTimeout(renderL5, 50);
      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    /* ========================================================= */
    /* LECTURE 5 (PYTHAGOREAN THEOREM: EUCLID PROOF) LOGIC       */
    /* ========================================================= */
    const l5State = {
      a: 3.0,
      b: 4.0,
      step: 0,
      autoPlayTimer: null
    };

    const l5StepInfo = [
      {
        title: "Step 0: 초기 작도 (기본 도형 설정)",
        desc: "직각삼각형 $\\\\triangle AGD$의 세 변에 각각 정사각형 $AHGI(a^2)$, $GDEF(b^2)$, $ABCD(c^2)$를 작도하고, 꼭짓점 $G$에서 밑변 $BC$에 수선 $GKJ$를 내립니다."
      },
      {
        title: "Step 1: 좌측 정사각형의 절반 (삼각형 IAG)",
        desc: "$\\\\triangle IAG$는 정사각형 $AHGI$를 대각선으로 나눈 절반이므로 $\\\\text{넓이} = \\\\frac{1}{2} a^2$입니다."
      },
      {
        title: "Step 2: 밑변과 높이가 같은 등적변형 (IAG → IAD)",
        desc: "밑변 $\\\\overline{IA}$를 공유하고 $\\\\overline{IA} \\\\parallel \\\\overline{GH}$이므로 꼭짓점을 $G$에서 $D$로 옮겨도 넓이가 같습니다. $\\\\triangle IAG = \\\\triangle IAD$."
      },
      {
        title: "Step 3: 점 A 중심 90° 회전 및 SAS 합동 (IAD ≡ GAB)",
        desc: "$\\\\overline{IA}=\\\\overline{GA}$, $\\\\overline{AD}=\\\\overline{AB}$, 끼인각 $\\\\angle IAD = 90^\\\\circ + \\\\angle A = \\\\angle GAB$이므로 $SAS$ 합동! $\\\\triangle IAD \\\\equiv \\\\triangle GAB$."
      },
      {
        title: "Step 4: 수선 평행선 사이 등적변형 (GAB → JAB)",
        desc: "밑변 $\\\\overline{AB}$를 공유하고 $\\\\overline{AB} \\\\parallel \\\\overline{GJ}$ (수선)이므로 꼭짓점 $G$를 $J$로 옮겨도 넓이가 같습니다. $\\\\triangle GAB = \\\\triangle JAB$."
      },
      {
        title: "Step 5: 좌측 결론: 정사각형 AHGI = 직사각형 ABJK (a²)",
        desc: "$\\\\triangle JAB$는 직사각형 $ABJK$의 절반이므로 $2 \\\\times \\\\triangle JAB = \\\\text{직사각형 } ABJK = a^2$! 좌측 정사각형의 넓이가 빗변 직사각형으로 고스란히 옮겨집니다."
      },
      {
        title: "Step 6: 우측 정사각형에서도 동일한 원리 전개",
        desc: "우측 정사각형 $GDEF$에서도 대칭적으로 $\\\\triangle GDE = \\\\triangle GCD = \\\\triangle JCD$가 성립합니다."
      },
      {
        title: "Step 7: 우측 결론: 정사각형 GDEF = 직사각형 JKCD (b²)",
        desc: "우측 정사각형 $GDEF$의 넓이($b^2$)는 빗변 우측 직사각형 $JKCD$의 넓이($b^2$)와 완벽히 같습니다."
      },
      {
        title: "Step 8: 피타고라스 정리 최종 완성! (a² + b² = c²)",
        desc: "빗변의 큰 정사각형 $ABCD(c^2)$는 두 직사각형 $ABJK(a^2)$와 $JKCD(b^2)$의 합이므로, $\\\\mathbf{a^2 + b^2 = c^2}$이 완벽히 증명되었습니다!"
      }
    ];

    function setL5Step(val) {
      l5State.step = parseInt(val);
      document.getElementById('l5StepSlider').value = l5State.step;
      document.getElementById('l5StepBadge').innerText = `Step ${l5State.step} / 8`;
      const info = l5StepInfo[l5State.step];
      document.getElementById('l5StepTitle').innerText = info.title;
      document.getElementById('l5StepText').innerHTML = info.desc;
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById('l5StepDescCard'), {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
      renderL5();
    }

    function prevL5Step() {
      if (l5State.step > 0) setL5Step(l5State.step - 1);
    }

    function nextL5Step() {
      if (l5State.step < 8) setL5Step(l5State.step + 1);
      else setL5Step(0);
    }

    function toggleL5AutoPlay() {
      const btn = document.getElementById('l5AutoPlayBtn');
      if (l5State.autoPlayTimer) {
        clearInterval(l5State.autoPlayTimer);
        l5State.autoPlayTimer = null;
        btn.innerText = '▶ 자동 재생';
        btn.style.background = 'rgba(56, 189, 248, 0.15)';
      } else {
        btn.innerText = '⏸ 일시정지';
        btn.style.background = 'rgba(251, 191, 36, 0.25)';
        l5State.autoPlayTimer = setInterval(() => {
          nextL5Step();
        }, 1800);
      }
    }

    function setL5Preset(a, b) {
      document.querySelectorAll('#lecture5View .preset-btn').forEach(btn => btn.classList.remove('active'));
      if (a === 3 && b === 4) document.getElementById('p5btn-345').classList.add('active');
      else if (a === 5 && b === 12) document.getElementById('p5btn-51213').classList.add('active');
      else if (a === 6 && b === 8) document.getElementById('p5btn-6810').classList.add('active');
      else if (a === 4 && b === 4) document.getElementById('p5btn-iso').classList.add('active');

      l5State.a = a;
      l5State.b = b;
      document.getElementById('l5a').value = a;
      document.getElementById('l5b').value = b;
      syncL5Values();
      renderL5();
    }

    function updateL5FromSliders() {
      l5State.a = parseFloat(document.getElementById('l5a').value);
      l5State.b = parseFloat(document.getElementById('l5b').value);
      document.querySelectorAll('#lecture5View .preset-btn').forEach(btn => btn.classList.remove('active'));
      syncL5Values();
      renderL5();
    }

    function syncL5Values() {
      const a = l5State.a;
      const b = l5State.b;
      const c = Math.sqrt(a * a + b * b);
      const a2 = a * a;
      const b2 = b * b;
      const c2 = c * c;

      document.getElementById('l5aVal').innerText = a.toFixed(1);
      document.getElementById('l5bVal').innerText = b.toFixed(1);
      document.getElementById('l5cVal').innerText = c.toFixed(3);
      document.getElementById('l5AreaA').innerText = a2.toFixed(2);
      document.getElementById('l5AreaB').innerText = b2.toFixed(2);
      document.getElementById('l5AreaC').innerText = c2.toFixed(2);
      document.getElementById('l5SumCheck').innerText = `${a2.toFixed(2)} + ${b2.toFixed(2)} = ${c2.toFixed(2)} (일치!)`;
    }

    function renderL5() {
      const canvas = document.getElementById('l5Canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const a = l5State.a;
      const b = l5State.b;
      const c = Math.sqrt(a * a + b * b);
      const step = l5State.step;

      // Mathematical geometry coordinates
      // Place A at (0, 0), D at (c, 0)
      // G is (a^2/c, -ab/c) in standard Cartesian (where y increases downwards on canvas)
      // Let's compute all relative points in unit dimensions:
      const pts = {
        A: [0, 0],
        D: [c, 0],
        G: [a * a / c, -a * b / c],
        B: [0, c],
        C: [c, c],
        K: [a * a / c, 0],
        J: [a * a / c, c],
        I: [-a * b / c, -a * a / c],
        H: [a * a / c - a * b / c, -a * b / c - a * a / c],
        E: [c + a * b / c, -b * b / c],
        F: [a * a / c + a * b / c, -a * b / c - b * b / c]
      };

      // Find bounding box
      let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
      for (const k in pts) {
        minX = Math.min(minX, pts[k][0]);
        maxX = Math.max(maxX, pts[k][0]);
        minY = Math.min(minY, pts[k][1]);
        maxY = Math.max(maxY, pts[k][1]);
      }

      const padding = 50;
      const scaleX = (w - padding * 2) / (maxX - minX);
      const scaleY = (h - padding * 2) / (maxY - minY);
      const scale = Math.min(scaleX, scaleY);

      // Centering offset
      const cx = (minX + maxX) / 2;
      const cy = (minY + maxY) / 2;
      const originX = w / 2 - cx * scale;
      const originY = h / 2 - cy * scale;

      function toScreen(p) {
        return [originX + p[0] * scale, originY + p[1] * scale];
      }

      const sPts = {};
      for (const k in pts) sPts[k] = toScreen(pts[k]);

      // Helper to draw polygon
      function drawPoly(names, fillStyle, strokeStyle, lineWidth = 1.5, dash = []) {
        ctx.save();
        ctx.beginPath();
        dash.length ? ctx.setLineDash(dash) : ctx.setLineDash([]);
        const first = sPts[names[0]];
        ctx.moveTo(first[0], first[1]);
        for (let i = 1; i < names.length; i++) {
          const pt = sPts[names[i]];
          ctx.lineTo(pt[0], pt[1]);
        }
        ctx.closePath();
        if (fillStyle) {
          ctx.fillStyle = fillStyle;
          ctx.fill();
        }
        if (strokeStyle) {
          ctx.strokeStyle = strokeStyle;
          ctx.lineWidth = lineWidth;
          ctx.stroke();
        }
        ctx.restore();
      }

      // 1. Draw Base Squares
      drawPoly(['A', 'B', 'C', 'D'], 'rgba(15, 23, 42, 0.6)', 'rgba(56, 189, 248, 0.4)', 2);
      drawPoly(['A', 'H', 'G', 'I'], 'rgba(15, 23, 42, 0.6)', 'rgba(56, 189, 248, 0.5)', 2);
      drawPoly(['G', 'F', 'E', 'D'], 'rgba(15, 23, 42, 0.6)', 'rgba(192, 132, 252, 0.5)', 2);

      // Perpendicular line GKJ
      ctx.save();
      ctx.beginPath();
      ctx.setLineDash([4, 4]);
      ctx.moveTo(sPts.G[0], sPts.G[1]);
      ctx.lineTo(sPts.J[0], sPts.J[1]);
      ctx.strokeStyle = '#fbbf24';
      ctx.lineWidth = 2;
      ctx.stroke();
      ctx.restore();

      // Right angle marker at J
      const markerSize = 8;
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
      ctx.lineWidth = 1.2;
      ctx.strokeRect(sPts.J[0] - markerSize, sPts.J[1] - markerSize, markerSize, markerSize);

      // Right angle marker at G
      // Vector GA and GD normalized
      const vGA = [pts.A[0] - pts.G[0], pts.A[1] - pts.G[1]];
      const vGD = [pts.D[0] - pts.G[0], pts.D[1] - pts.G[1]];
      const lenGA = Math.hypot(vGA[0], vGA[1]);
      const lenGD = Math.hypot(vGD[0], vGD[1]);
      const uGA = [vGA[0] / lenGA * 0.4, vGA[1] / lenGA * 0.4];
      const uGD = [vGD[0] / lenGD * 0.4, vGD[1] / lenGD * 0.4];
      const g1 = toScreen([pts.G[0] + uGA[0], pts.G[1] + uGA[1]]);
      const g2 = toScreen([pts.G[0] + uGA[0] + uGD[0], pts.G[1] + uGA[1] + uGD[1]]);
      const g3 = toScreen([pts.G[0] + uGD[0], pts.G[1] + uGD[1]]);
      ctx.beginPath();
      ctx.moveTo(g1[0], g1[1]);
      ctx.lineTo(g2[0], g2[1]);
      ctx.lineTo(g3[0], g3[1]);
      ctx.stroke();

      // 2. Step Specific Animations
      if (step === 1) {
        // Step 1: tri IAG
        drawPoly(['I', 'A', 'G'], 'rgba(56, 189, 248, 0.45)', '#38bdf8', 2.5);
      } else if (step === 2) {
        // Step 2: tri IAD (shear along IA || GH)
        drawPoly(['I', 'A', 'D'], 'rgba(56, 189, 248, 0.5)', '#38bdf8', 2.5);
        // Draw parallel indicator line
        ctx.save();
        ctx.beginPath();
        ctx.moveTo(sPts.I[0], sPts.I[1]);
        ctx.lineTo(sPts.D[0], sPts.D[1]);
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.restore();
      } else if (step === 3) {
        // Step 3: tri IAD === tri GAB (SAS Congruence)
        drawPoly(['I', 'A', 'D'], 'rgba(56, 189, 248, 0.25)', '#38bdf8', 1.5, [4, 4]);
        drawPoly(['G', 'A', 'B'], 'rgba(52, 211, 153, 0.55)', '#34d399', 2.5);
      } else if (step === 4) {
        // Step 4: tri GAB -> tri JAB (shear along AB || GJ)
        drawPoly(['J', 'A', 'B'], 'rgba(52, 211, 153, 0.55)', '#34d399', 2.5);
        // Highlight parallel lines AB and GJ with arrows/color
        ctx.save();
        ctx.strokeStyle = '#fb7185';
        ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(sPts.A[0], sPts.A[1]); ctx.lineTo(sPts.B[0], sPts.B[1]); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(sPts.G[0], sPts.G[1]); ctx.lineTo(sPts.J[0], sPts.J[1]); ctx.stroke();
        ctx.restore();
      } else if (step === 5) {
        // Step 5: Area(AHGI) = Area(ABJK) = a^2
        drawPoly(['A', 'H', 'G', 'I'], 'rgba(56, 189, 248, 0.45)', '#38bdf8', 2.5);
        drawPoly(['A', 'B', 'J', 'K'], 'rgba(56, 189, 248, 0.45)', '#38bdf8', 2.5);
        
        ctx.fillStyle = '#fff';
        ctx.font = 'bold 16px Inter';
        ctx.textAlign = 'center';
        const midAHGI = [(sPts.A[0] + sPts.H[0]) / 2, (sPts.A[1] + sPts.H[1]) / 2];
        const midABJK = [(sPts.A[0] + sPts.J[0]) / 2, (sPts.A[1] + sPts.J[1]) / 2];
        ctx.fillText('a²', midAHGI[0], midAHGI[1]);
        ctx.fillText('a²', midABJK[0], midABJK[1]);
      } else if (step === 6) {
        // Step 6: Right triangle shear & congruence (tri GCD & tri JCD)
        drawPoly(['A', 'B', 'J', 'K'], 'rgba(56, 189, 248, 0.35)', '#38bdf8', 1.5);
        drawPoly(['G', 'C', 'D'], 'rgba(192, 132, 252, 0.3)', '#c084fc', 1.5, [4, 4]);
        drawPoly(['J', 'C', 'D'], 'rgba(192, 132, 252, 0.55)', '#c084fc', 2.5);

        // Highlight parallel lines GJ and DC
        ctx.save();
        ctx.strokeStyle = '#fb7185';
        ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(sPts.G[0], sPts.G[1]); ctx.lineTo(sPts.J[0], sPts.J[1]); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(sPts.D[0], sPts.D[1]); ctx.lineTo(sPts.C[0], sPts.C[1]); ctx.stroke();
        ctx.restore();
      } else if (step === 7) {
        // Step 7: Area(GDEF) = Area(JKCD) = b^2
        drawPoly(['A', 'B', 'J', 'K'], 'rgba(56, 189, 248, 0.35)', '#38bdf8', 1.5);
        drawPoly(['G', 'F', 'E', 'D'], 'rgba(192, 132, 252, 0.45)', '#c084fc', 2.5);
        drawPoly(['K', 'J', 'C', 'D'], 'rgba(192, 132, 252, 0.45)', '#c084fc', 2.5);

        ctx.fillStyle = '#fff';
        ctx.font = 'bold 16px Inter';
        ctx.textAlign = 'center';
        const midGDEF = [(sPts.G[0] + sPts.E[0]) / 2, (sPts.G[1] + sPts.E[1]) / 2];
        const midJKCD = [(sPts.K[0] + sPts.C[0]) / 2, (sPts.K[1] + sPts.C[1]) / 2];
        ctx.fillText('b²', midGDEF[0], midGDEF[1]);
        ctx.fillText('b²', midJKCD[0], midJKCD[1]);
      } else if (step === 8) {
        // Step 8: Full Pythagoras Theorem
        drawPoly(['A', 'H', 'G', 'I'], 'rgba(56, 189, 248, 0.45)', '#38bdf8', 2.5);
        drawPoly(['G', 'F', 'E', 'D'], 'rgba(192, 132, 252, 0.45)', '#c084fc', 2.5);
        drawPoly(['A', 'B', 'J', 'K'], 'rgba(56, 189, 248, 0.45)', '#38bdf8', 2.5);
        drawPoly(['K', 'J', 'C', 'D'], 'rgba(192, 132, 252, 0.45)', '#c084fc', 2.5);
        drawPoly(['A', 'B', 'C', 'D'], null, '#fbbf24', 3.5);

        ctx.fillStyle = '#fbbf24';
        ctx.font = 'bold 22px Inter';
        ctx.textAlign = 'center';
        const centerC = [(sPts.A[0] + sPts.C[0]) / 2, (sPts.A[1] + sPts.C[1]) / 2 + 10];
        ctx.fillText('a² + b² = c²', centerC[0], centerC[1]);
      }

      // 3. Draw Main Right Triangle AGD
      drawPoly(['A', 'G', 'D'], 'rgba(255, 255, 255, 0.08)', '#ffffff', 2.5);

      // 4. Draw Vertex Points & Labels
      const labelOffsets = {
        A: [-16, -6],
        D: [16, -6],
        G: [0, -14],
        B: [-16, 16],
        C: [16, 16],
        K: [8, 14],
        J: [0, 18],
        I: [-16, -10],
        H: [0, -14],
        E: [16, -10],
        F: [0, -14]
      };

      for (const k in sPts) {
        const pt = sPts[k];
        ctx.fillStyle = '#fbbf24';
        ctx.beginPath();
        ctx.arc(pt[0], pt[1], 4, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 13px Inter';
        const off = labelOffsets[k] || [8, 8];
        ctx.fillText(k, pt[0] + off[0], pt[1] + off[1]);
      }
    }

    function copyL5ManimCode() {
      const code = document.getElementById('l5ManimCodeText').innerText;
      navigator.clipboard.writeText(code).then(() => {
        alert('피타고라스 유클리드 증명 Manim 파이썬 코드가 클립보드에 복사되었습니다!');
      });
    }'''

    if old_script_head not in content:
        print("ERROR: old_script_head not found in index.html!")
        return

    content = content.replace(old_script_head, new_script_head, 1)

    # 4. Update window.addEventListener('load') to initialize Lecture 5
    old_onload = '''    // Initialize on page load
    window.addEventListener('load', () => {
      syncL4Values();
      renderL4();
    });'''

    new_onload = '''    // Initialize on page load
    window.addEventListener('load', () => {
      syncL5Values();
      renderL5();
    });'''

    if old_onload in content:
        content = content.replace(old_onload, new_onload, 1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: index.html updated successfully with Lecture 5!")

if __name__ == '__main__':
    main()
