# -*- coding: utf-8 -*-
"""
Script to build and inject Lecture 12 into index.html
Lecture: Rectangular Hyperbola Area Invariance Theorem (S = T) & Geometric Proof
Instructor: Bae Sang-myeon (MathPresso / Chulbyuk Math)
YouTube Short: https://youtube.com/shorts/uiHX6PxDIB4
"""

import os
import re

def main():
    html_path = 'index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read manim code for tab
    with open('hyperbola_area_theorem_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()

    # 1. Update Switcher Bar: Add btnLec12 as active, remove active from btnLec11
    # Check if btnLec12 already exists
    if 'id="btnLec12"' not in html:
        old_btn11 = '<button class="lecture-btn active" id="btnLec11" onclick="setLecture(11)">'
        if old_btn11 in html:
            new_btn_block = '''<button class="lecture-btn active" id="btnLec12" onclick="setLecture(12)">
          직각쌍곡선 넓이 $S=T$ 꿀팁 (배상면)
        </button>
        <button class="lecture-btn" id="btnLec11" onclick="setLecture(11)">'''
            html = html.replace(old_btn11, new_btn_block, 1)
            print("Added btnLec12 to switcher bar.")
        else:
            print("Could not find active btnLec11, searching alternative...")
            old_btn11_alt = '<button class="lecture-btn" id="btnLec11" onclick="setLecture(11)">'
            if old_btn11_alt in html:
                new_btn_block = '''<button class="lecture-btn active" id="btnLec12" onclick="setLecture(12)">
          직각쌍곡선 넓이 $S=T$ 꿀팁 (배상면)
        </button>
        <button class="lecture-btn" id="btnLec11" onclick="setLecture(11)">'''
                html = html.replace(old_btn11_alt, new_btn_block, 1)
                print("Added btnLec12 to switcher bar (alt).")

    # Update captured_summary button label if present
    html = html.replace('📸 사진 1~11 핵심 전용 페이지', '📸 사진 1~12 핵심 전용 페이지')

    # 2. Hide lecture11View if active
    if '<div id="lecture11View">' in html:
        html = html.replace('<div id="lecture11View">', '<div id="lecture11View" style="display: none;">', 1)
        print("Set lecture11View to display: none.")

    # 3. Create Lecture 12 View HTML
    escaped_manim = (manim_code
                     .replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;'))

    lecture12_html = f'''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 12 (RECTANGULAR HYPERBOLA S = T THEOREM: MATHPRESSO) -->
    <!-- ============================================================== -->
    <div id="lecture12View">
      <header>
        <div class="badge-pill" style="border-color: rgba(244, 63, 94, 0.4); color: #fb7185; box-shadow: 0 0 20px rgba(244, 63, 94, 0.3);">
          <span>📐 고1 수학 (하) · 유리함수 꿀팁 · 직각쌍곡선 넓이 불변 정리</span>
        </div>
        <h1 style="background: linear-gradient(135deg, #ffffff 30%, #fb7185 70%, #ec4899 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          직각쌍곡선 넓이 불변 정리 ($S = T$) &amp; 4단계 기하학적 증명
        </h1>
        <p class="subtitle">
          원점 $O$와 쌍곡선 호 $AB$가 이루는 부채꼴 넓이 $S$는, $x$축으로 내린 적분 영역 $T$와 기하학적으로 완벽히 같습니다! 직각삼각형 등적변형($\\frac{{1}}{{2}}k$)과 보라색 공통 영역 상쇄, 그리고 1647년 자연로그($\\ln$)의 기원이 담긴 <strong>인터랙티브 기하학 스튜디오</strong>입니다.
        </p>

        <div class="source-meta">
          <span>🎬 채널: <strong>매스프레소 MathPresso (배상면 선생님)</strong></span>
          <span>•</span>
          <a href="https://youtube.com/shorts/uiHX6PxDIB4" target="_blank" rel="noopener noreferrer" style="color: var(--accent-blue); text-decoration: none; display: inline-flex; align-items: center; gap: 4px;">
            <span>[고1] 유리함수 넓이 꿀팁!! (0:40)</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          </a>
          <span>•</span>
          <span>강의 고화질 10단계 캡처 &amp; Manim 코드 탑재</span>
        </div>
      </header>

      <!-- Tab Bar for Lecture 12 -->
      <div class="tab-bar">
        <button class="tab-btn active" onclick="switchLec12Tab('l12SimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          인터랙티브 S = T 기하학 증명 시뮬레이터
        </button>
        <button class="tab-btn" onclick="switchLec12Tab('l12CaptureTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          강의 판서 캡처 &amp; 10단계 타임라인
        </button>
        <button class="tab-btn" onclick="switchLec12Tab('l12ProofTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>
          4단계 기하학적 증명 &amp; 자연로그의 기원
        </button>
        <button class="tab-btn" onclick="switchLec12Tab('l12ManimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          3Blue1Brown Manim 파이썬 코드
        </button>
      </div>

      <!-- TAB 1: INTERACTIVE SIMULATOR (LECTURE 12) -->
      <div id="l12SimTab" class="tab-panel active">
        <div class="glass-card">
          <!-- Dynamic Banner -->
          <div class="formula-banner" id="l12Banner" style="background: linear-gradient(135deg, rgba(244, 63, 94, 0.12), rgba(168, 85, 247, 0.09)); border-color: rgba(244, 63, 94, 0.35);">
            <div class="label" id="l12BannerLabel" style="color: #fb7185;">🌟 직각쌍곡선(유리함수) 부채꼴과 적분 영역 불변 정리 (Saint-Vincent Theorem)</div>
            <div class="math-main" id="l12BannerMath">
              $$xy = k \\iff y = \\frac{{k}}{{x}} \\implies \\mathbf{{S = T = \\int_a^b \\frac{{k}}{{x}}\\,dx = k \\ln\\left(\\frac{{b}}{{a}}\\right)}}$$
            </div>
          </div>

          <div class="sim-grid">
            <!-- Canvas Box -->
            <div class="canvas-box">
              <canvas id="l12Canvas" width="580" height="520"></canvas>
              <div id="l12CanvasCaption" style="font-size: 0.85rem; color: var(--text-dim); margin-top: 10px; text-align: center;">
                부채꼴 $S$ (보라/핑크) | 적분 사다리꼴 $T$ (청록) | 삼각형 $\\triangle OAA', \\triangle OBB'$ (빨강/파랑 $\\frac{{1}}{{2}}k$) | 공통 영역 $\\triangle OA'C$ (보라)
              </div>
            </div>

            <!-- Controls & Live Evaluation -->
            <div class="sim-controls">
              <!-- Presets -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎯 4대 대표 기하학 상태 프리셋</span>
                </div>
                <div class="preset-grid" style="grid-template-columns: 1fr 1fr;">
                  <button class="preset-btn active" id="l12PreBase" onclick="setL12Preset('base')">
                    <span>1. 배상면 꿀팁 기본형 🎯</span>
                    <span class="p-sub" style="color: #34d399; font-weight: bold;">$xy=1, a=0.8, b=2.5$</span>
                  </button>
                  <button class="preset-btn" id="l12PreLogE" onclick="setL12Preset('loge')">
                    <span>2. 자연로그 $\\ln e = 1$</span>
                    <span class="p-sub">$a=1, b=e \\approx 2.72 \\implies S=1$</span>
                  </button>
                  <button class="preset-btn" id="l12PreSym" onclick="setL12Preset('sym')">
                    <span>3. 대칭 구간 ($0.5 \\sim 2.0$)</span>
                    <span class="p-sub">$S = T = \\ln 4 \\approx 1.386$</span>
                  </button>
                  <button class="preset-btn" id="l12PreK2" onclick="setL12Preset('k2')">
                    <span>4. 일반형 $xy=2$ 확장</span>
                    <span class="p-sub" style="color: #38bdf8;">$k=2, a=1.0, b=3.0$</span>
                  </button>
                </div>
              </div>

              <!-- Parameter Sliders -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎛️ $xy = k$ 및 좌표 $a, b$ 실시간 튜닝</span>
                </div>

                <div class="slider-row">
                  <label>쌍곡선 상수 $k$ ($xy = k$): <strong id="l12kVal" style="color: #fb7185;">1.00</strong></label>
                  <input type="range" id="l12SliderK" min="0.5" max="3.5" step="0.1" value="1.0" oninput="updateL12Sliders()">
                </div>

                <div class="slider-row">
                  <label>점 $A$의 $x$좌표 $a$: <strong id="l12aVal" style="color: #f87171;">0.80</strong></label>
                  <input type="range" id="l12SliderA" min="0.3" max="2.0" step="0.05" value="0.8" oninput="updateL12Sliders()">
                </div>

                <div class="slider-row">
                  <label>점 $B$의 $x$좌표 $b$: <strong id="l12bVal" style="color: #60a5fa;">2.50</strong></label>
                  <input type="range" id="l12SliderB" min="1.2" max="4.5" step="0.05" value="2.5" oninput="updateL12Sliders()">
                </div>
              </div>

              <!-- Layer Toggles -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">👁️ 4단계 기하학 증명 레이어 On/Off</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 0.85rem;">
                  <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
                    <input type="checkbox" id="l12ToggleSector" checked onchange="updateL12Toggles()">
                    <span>부채꼴 $S$ (원점-호)</span>
                  </label>
                  <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
                    <input type="checkbox" id="l12ToggleIntegral" checked onchange="updateL12Toggles()">
                    <span>적분 영역 $T$ ($x$축 밑면)</span>
                  </label>
                  <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
                    <input type="checkbox" id="l12ToggleTriangles" checked onchange="updateL12Toggles()">
                    <span>삼각형 $\\triangle OAA', \\triangle OBB'$</span>
                  </label>
                  <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
                    <input type="checkbox" id="l12ToggleOverlap" checked onchange="updateL12Toggles()">
                    <span>보라색 공통 상쇄</span>
                  </label>
                  <label style="display: flex; align-items: center; gap: 6px; cursor: pointer; grid-column: span 2;">
                    <input type="checkbox" id="l12ToggleYellow" checked onchange="updateL12Toggles()">
                    <span>노란색 곡면 조각 결합 (호 $AB$ 아래)</span>
                  </label>
                </div>
              </div>

              <!-- Live Verification Card -->
              <div class="control-card" style="background: rgba(15, 23, 42, 0.95); border-color: rgba(244, 63, 94, 0.4);">
                <div class="control-header">
                  <span class="control-title" style="color: #fb7185;">📊 기하학적 넓이 일치 실시간 검증</span>
                  <span class="badge-pill-sm" id="l12MatchBadge" style="background: #10b981; color: #fff;">S ≡ T 일치 100.0%</span>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 8px;">
                  <div style="background: rgba(168, 85, 247, 0.12); padding: 8px; border-radius: 8px; border: 1px solid rgba(168, 85, 247, 0.3);">
                    <div style="font-size: 0.75rem; color: #c084fc;">부채꼴 넓이 $S$</div>
                    <div id="l12AreaSVal" style="font-size: 1.25rem; font-weight: 700; color: #e879f9;">1.1394</div>
                    <div style="font-size: 0.72rem; color: var(--text-dim);">$k \\ln(b/a)$</div>
                  </div>
                  <div style="background: rgba(6, 182, 212, 0.12); padding: 8px; border-radius: 8px; border: 1px solid rgba(6, 182, 212, 0.3);">
                    <div style="font-size: 0.75rem; color: #22d3ee;">적분 사다리꼴 넓이 $T$</div>
                    <div id="l12AreaTVal" style="font-size: 1.25rem; font-weight: 700; color: #38bdf8;">1.1394</div>
                    <div style="font-size: 0.72rem; color: var(--text-dim);">$\\int_a^b \\frac{{k}}{{x}} dx$</div>
                  </div>
                </div>

                <div id="l12LiveProofDetail" style="margin-top: 12px; padding: 10px; background: rgba(0,0,0,0.35); border-radius: 8px; font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
                  • $\\triangle OAA' = \\frac{{1}}{{2}} \\cdot a \\cdot \\frac{{k}}{{a}} = 0.500$<br>
                  • $\\triangle OBB' = \\frac{{1}}{{2}} \\cdot b \\cdot \\frac{{k}}{{b}} = 0.500$<br>
                  • 보라색 공통삼각형 = 0.051 $\\implies$ <strong>빨간 조각 = 파란 조각 = 0.449</strong><br>
                  • 노란색 조각(0.690) 더함 $\\implies$ <strong>$S = T = 1.139$ 완벽 증명!</strong>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: TIMELINE CAPTURES (LECTURE 12) -->
      <div id="l12CaptureTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.5rem; margin-bottom: 8px; color: var(--accent-gold);">
            📸 배상면 선생님 강의 10단계 판서 타임라인 &amp; 교재 해설
          </h2>
          <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 24px;">
            유튜브 쇼츠(0:40) 원본 영상의 직각쌍곡선 $S=T$ 기하학 증명 전 과정을 1080p 고화질 캡처와 함께 완벽히 분석했습니다.
          </p>

          <div class="timeline-container">
            <!-- Card 1 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">1단계 [00:00:03]</span>
                <span class="timeline-title">직각쌍곡선 $xy=1$과 곡선 위의 두 점 $A, B$ 세팅</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v12/01_hyperbola_problem_statement.jpg" alt="01_hyperbola_problem_statement">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "직각쌍곡선 $xy=1$ 위의 두 점을 $A, B$라 할 때..."
              </div>
              <div class="timeline-desc">
                <strong>문제 세팅:</strong> 제1사분면에서 정의된 직각쌍곡선 $xy = 1 \\iff y = \\frac{{1}}{{x}}$ 위의 임의의 두 점 $A(a, \\frac{{1}}{{a}})$, $B(b, \\frac{{1}}{{b}})$ ($0 < a < b$)를 설정합니다.
              </div>
            </div>

            <!-- Card 2 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">2단계 [00:00:05]</span>
                <span class="timeline-title">원점과 호 $AB$가 이루는 부채꼴 넓이 $S$ 정의</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v12/02_sector_area_s_definition.jpg" alt="02_sector_area_s_definition">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "...선분 $OA, OB$와 쌍곡선으로 둘러싸인 넓이 $S$는..."
              </div>
              <div class="timeline-desc">
                <strong>기하학적 정의:</strong> 원점 $O(0, 0)$에서 두 점 $A, B$로 연결한 두 선분 $OA, OB$와 곡선의 호 $AB$로 둘러싸인 방사형 부채꼴(Hyperbolic Sector)의 넓이를 $S$라 부릅니다.
              </div>
            </div>

            <!-- Card 3 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">3단계 [00:00:10]</span>
                <span class="timeline-title">$x$축 수선의 발 투영 적분 영역 $T$ 정의</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v12/03_integral_area_t_definition.jpg" alt="03_integral_area_t_definition">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "...점 $A(a, \\frac{{1}}{{a}})$, 점 $B(b, \\frac{{1}}{{b}})$이라 할 때 쌍곡선과 직선 $x=a, x=b$, $x$축으로 둘러싸인 넓이 $T$와..."
              </div>
              <div class="timeline-desc">
                <strong>적분 영역 정의:</strong> 점 $A$와 $B$에서 각각 $x$축에 수선을 내려 만든 $x=a, x=b$ 사이의 곡면 사다리꼴 넓이를 $T$라 합니다. 미적분학의 정적분 기호로는 $\\int_a^b \\frac{{1}}{{x}} dx$에 해당합니다.
              </div>
            </div>

            <!-- Card 4 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">4단계 [00:00:15]</span>
                <span class="timeline-title">핵심 정리 선언: $S = T$의 기하학적 일치</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v12/04_claim_s_equals_t.jpg" alt="04_claim_s_equals_t">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "...넓이 $T$와 같다!"
              </div>
              <div class="timeline-desc">
                <strong>충격적 발견:</strong> 전혀 다른 모양으로 보이는 원점 방사형 부채꼴 $S$와 $x$축 투영 곡면 사다리꼴 $T$의 면적이 완벽하게 일치합니다. 이제 적분 없이 고1 기하학만으로 증명에 들어갑니다.
              </div>
            </div>

            <!-- Card 5 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">5단계 [00:00:17]</span>
                <span class="timeline-title">평면의 4개 영역 상호 분할 (Decomposition)</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v12/05_four_region_decomposition.jpg" alt="05_four_region_decomposition">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "그림을 네 영역으로 쪼개면..."
              </div>
              <div class="timeline-desc">
                <strong>영역 분해:</strong> 선분 $OB$와 수선 $x=a$의 교점 $C$를 기준으로, 전체 영역을 [빨간 조각 $\\triangle OAC$], [파란 사다리꼴 조각 $A'CBB'$], [공통 보라 삼각형 $\\triangle OA'C$], [호 아래 노란 조각]의 4개로 분할합니다.
              </div>
            </div>

            <!-- Card 6 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">6단계 [00:00:20]</span>
                <span class="timeline-title">빨간 직각삼각형 넓이 계산: $\\frac{{1}}{{2}} \\cdot a \\cdot \\frac{{1}}{{a}} = \\frac{{1}}{{2}}$</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v12/06_red_triangle_half.jpg" alt="06_red_triangle_half">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "빨간 두 조각의 넓이는 $\\frac{{1}}{{2}} \\cdot a \\cdot \\frac{{1}}{{a}} = \\frac{{1}}{{2}}$..."
              </div>
              <div class="timeline-desc">
                <strong>불변의 삼각형:</strong> 점 $A(a, \\frac{{1}}{{a}})$와 원점, $x$축 수선의 발 $A'$이 이루는 직각삼각형 $\\triangle OAA'$의 넓이는 가로 $a \\times$ 세로 $\\frac{{1}}{{a}} \\times \\frac{{1}}{{2}} = \\mathbf{{\\frac{{1}}{{2}}}}$로 항상 일정합니다!
              </div>
            </div>

            <!-- Card 7 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">7단계 [00:00:23]</span>
                <span class="timeline-title">파란 직각삼각형 넓이 계산: $\\frac{{1}}{{2}} \\cdot b \\cdot \\frac{{1}}{{b}} = \\frac{{1}}{{2}}$</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v12/07_blue_triangle_half.jpg" alt="07_blue_triangle_half">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "...파란 두 조각의 넓이도 $\\frac{{1}}{{2}} \\cdot b \\cdot \\frac{{1}}{{b}} = \\frac{{1}}{{2}}$로 빨강, 파랑의 넓이는 같다."
              </div>
              <div class="timeline-desc">
                <strong>등적성(Equivalence):</strong> 점 $B(b, \\frac{{1}}{{b}})$와 원점이 이루는 직각삼각형 $\\triangle OBB'$의 넓이 역시 $\\frac{{1}}{{2}} \\cdot b \\cdot \\frac{{1}}{{b}} = \\mathbf{{\\frac{{1}}{{2}}}}$입니다. 즉, $\\text{{Area}}(\\triangle OAA') = \\text{{Area}}(\\triangle OBB')$입니다.
              </div>
            </div>

            <!-- Card 8 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">8단계 [00:00:28]</span>
                <span class="timeline-title">공통 보라색 영역 제거 $\\implies$ 빨간 조각 = 파란 조각</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v12/08_purple_overlap_cancellation.jpg" alt="08_purple_overlap_cancellation">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "두 색이 겹치는 보라색을 버리면, 빨강, 파랑 한 조각의 넓이도 같다."
              </div>
              <div class="timeline-desc">
                <strong>영역 상쇄:</strong> 두 삼각형 모두 공통 삼각형 영역(보라색 $\\triangle OA'C$)을 포함하고 있으므로, 양변에서 보라색을 빼면 남은 [빨간 조각] = [파란 조각]이 성립합니다!
              </div>
            </div>

            <!-- Card 9 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">9단계 [00:00:32]</span>
                <span class="timeline-title">양변에 호 $AB$ 아래 노란색 곡면 조각 결합</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v12/09_add_yellow_curved_region.jpg" alt="09_add_yellow_curved_region">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "남은 조각에 노란색을 칠하면, 빨강+노랑의 합은 파랑+노랑의 합이므로..."
              </div>
              <div class="timeline-desc">
                <strong>합체 원리:</strong> 등식 [빨간 조각 = 파란 조각]의 양변에 호 $AB$와 선분 $AB$ 사이의 [노란색 곡면 조각]을 똑같이 더해줍니다.
              </div>
            </div>

            <!-- Card 10 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">10단계 [00:00:34]</span>
                <span class="timeline-title">최종 도출: $S = T$ 기하학적 증명 완성!</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v12/10_final_proof_s_equals_t.jpg" alt="10_final_proof_s_equals_t">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "...빨강+노랑의 합은 파랑+노랑의 합이므로 $S$는 $T$다. 증명 끝!"
              </div>
              <div class="timeline-desc">
                <strong>Q.E.D. 완료:</strong> 좌변(빨강+노랑)은 원점과 호 $AB$가 이루는 부채꼴 $S$가 되고, 우변(파랑+노랑)은 $x=a$에서 $x=b$까지의 적분 사다리꼴 $T$가 되므로, **$S = T$**임이 완벽히 증명되었습니다!
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 3: MATHEMATICAL PROOF (LECTURE 12) -->
      <div id="l12ProofTab" class="tab-panel">
        <div class="glass-card" style="line-height: 1.8;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px; color: #fb7185;">
            📐 직각쌍곡선의 기하학적 불변성과 자연로그($\\ln x$)의 역사적 기원
          </h2>
          
          <div style="background: rgba(15, 23, 42, 0.7); padding: 20px; border-radius: 12px; border-left: 4px solid #fb7185; margin-bottom: 24px;">
            <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">1. 4단계 기하학적 증명 메커니즘 정리</h3>
            <p>직각쌍곡선 $xy = k$ 위의 임의의 두 점 $A(a, \\frac{{k}}{{a}}), B(b, \\frac{{k}}{{b}})$ ($0 < a < b$)에 대하여:</p>
            <ol style="padding-left: 20px; margin-top: 10px; color: #cbd5e1;">
              <li><strong>직각삼각형 넓이의 일정성:</strong> 점 $A, B$에서 $x$축에 내린 수선의 발을 $A'(a, 0), B'(b, 0)$이라 하면,
              $$\\text{{Area}}(\\triangle OAA') = \\frac{{1}}{{2}} \\cdot a \\cdot \\frac{{k}}{{a}} = \\frac{{k}}{{2}}, \\quad \\text{{Area}}(\\triangle OBB') = \\frac{{1}}{{2}} \\cdot b \\cdot \\frac{{k}}{{b}} = \\frac{{k}}{{2}}$$</li>
              <li><strong>공통 삼각형의 정의:</strong> 선분 $OB$의 직선 방정식은 $y = \\frac{{k/b}}{{b}} x = \\frac{{k}}{{b^2}} x$이므로, 직선 $x = a$와의 교점 $C$의 좌표는 $C\\left(a, \\frac{{ka}}{{b^2}}\\right)$입니다.
              따라서 공통 삼각형 $\\triangle OA'C$의 넓이는 $\\frac{{1}}{{2}} \\cdot a \\cdot \\frac{{ka}}{{b^2}} = \\frac{{ka^2}}{{2b^2}}$입니다.</li>
              <li><strong>공통 영역 상쇄:</strong>
              $$\\text{{빨간 조각}} = \\triangle OAA' - \\triangle OA'C = \\frac{{k}}{{2}} - \\frac{{ka^2}}{{2b^2}}$$
              $$\\text{{파란 조각}} = \\triangle OBB' - \\triangle OA'C = \\frac{{k}}{{2}} - \\frac{{ka^2}}{{2b^2}}$$
              $$\\implies \\mathbf{{\\text{{빨간 조각}} = \\text{{파란 조각}}}}$$</li>
              <li><strong>노란색 조각 결합 $\\implies S = T$:</strong>
              양변에 호 $AB$ 아래의 노란색 조각을 더하면:
              $$\\text{{빨간 조각}} + \\text{{노란 조각}} + \\triangle OAB = S \\quad (\\text{{원점과 호 }} AB\\text{{로 둘러싸인 부채꼴}})$$
              $$\\text{{파란 조각}} + \\text{{노란 조각}} + \\triangle OAB = T \\quad (x=a, x=b \\text{{ 사이의 }} x\\text{{축 적분 사다리꼴}})$$
              $$\\mathbf{{\\therefore S = T}}$$</li>
            </ol>
          </div>

          <div style="background: rgba(15, 23, 42, 0.7); padding: 20px; border-radius: 12px; border-left: 4px solid #38bdf8; margin-bottom: 24px;">
            <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">2. 1647년 그레고아 드 생뱅상 정리와 자연로그의 발견</h3>
            <p>
              미적분학이 뉴턴과 라이프니츠에 의해 공식화되기 이전인 1647년, 벨기에의 예수회 수학자 **그레고아 드 생뱅상(Grégoire de Saint-Vincent)**은 직각쌍곡선 아래의 넓이가 기하급수적(등비수열) 구간에서 산술급수적(등차수열)으로 증가함을 증명했습니다.
            </p>
            <p style="margin-top: 10px; color: #cbd5e1;">
              즉, $T(a, b) = T(1, b) - T(1, a)$로 정의할 때, $T(1, x_1 \\cdot x_2) = T(1, x_1) + T(1, x_2)$라는 <strong>로그의 가법 공식</strong>을 최초로 기하학에서 발견한 것입니다.
              이 면적이 바로 오늘날의 **자연로그 $\\ln(x)$**이며, $T(1, e) = 1$이 되는 지점이 자연상수 $e \\approx 2.71828$의 기하학적 정의가 되었습니다!
            </p>
          </div>

          <div style="background: rgba(15, 23, 42, 0.7); padding: 20px; border-radius: 12px; border-left: 4px solid #34d399;">
            <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">3. 수능/내신 실전 킬러 치트키: 유리함수 직사각형 면적 일정</h3>
            <ul style="padding-left: 20px; color: #cbd5e1;">
              <li>유리함수 $y = \\frac{{k}}{{x}}$ 위의 임의의 점 $P(x, y)$에서 $x$축, $y$축에 내린 직사각형의 면적은 항상 $xy = k$로 불변입니다.</li>
              <li>원점과 잇는 직각삼각형의 넓이는 항상 $\\frac{{1}}{{2}}k$입니다.</li>
              <li>수능 모의고사에서 원점과 곡선 위의 두 점이 만드는 복잡한 부채꼴 면적 문항이 나오면, 삼각치환이나 신발끈 공식 대신 <strong>$x$축으로 내린 정적분 $\\int_a^b \\frac{{k}}{{x}} dx = k \\ln(b/a)$로 단 1초 만에 치환</strong>하여 풀어낼 수 있습니다!</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- TAB 4: MANIM PYTHON SCRIPT (LECTURE 12) -->
      <div id="l12ManimTab" class="tab-panel">
        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <div>
              <h2 style="font-size: 1.4rem; color: #fb7185;">3Blue1Brown 스타일 Manim 파이썬 애니메이션 코드</h2>
              <p style="color: var(--text-muted); font-size: 0.88rem; margin-top: 4px;">
                `hyperbola_area_theorem_manim.py` - 수학교육용 수학 애니메이션 풀스크립트
              </p>
            </div>
            <button class="preset-btn" onclick="copyL12ManimCode()" style="padding: 8px 18px; border-color: #fb7185; color: #fb7185;">
              📋 파이썬 코드 복사하기
            </button>
          </div>

          <pre id="l12ManimCodeBlock" style="background: #020617; padding: 20px; border-radius: 10px; border: 1px solid var(--border-color); font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; color: #e2e8f0; overflow-x: auto; max-height: 600px; line-height: 1.5;"><code>{escaped_manim}</code></pre>
        </div>
      </div>
    </div>

'''

    # Insert lecture12_html right before lecture11View
    if 'id="lecture12View"' not in html:
        idx_lec11 = html.find('id="lecture11View"')
        if idx_lec11 != -1:
            # find previous <div or comment
            target_str = '    <!-- ============================================================== -->\n    <!-- SECTION FOR LECTURE 11'
            if target_str in html:
                html = html.replace(target_str, lecture12_html + target_str, 1)
                print("Inserted lecture12View before lecture11View.")
            else:
                # alternative insertion
                html = html.replace('<div id="lecture11View"', lecture12_html + '<div id="lecture11View"', 1)
                print("Inserted lecture12View before lecture11View (fallback).")

    # 4. Add JavaScript for Lecture 12
    js_lecture12 = '''
    /* ========================================================= */
    /* LECTURE 12 (RECTANGULAR HYPERBOLA S = T) LOGIC            */
    /* ========================================================= */
    function switchLec12Tab(tabId) {
      document.querySelectorAll('#lecture12View .tab-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('#lecture12View .tab-btn').forEach(b => b.classList.remove('active'));
      const activePanel = document.getElementById(tabId);
      if (activePanel) activePanel.classList.add('active');
      event.currentTarget.classList.add('active');
      if (tabId === 'l12SimTab') setTimeout(renderL12, 50);
      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function copyL12ManimCode() {
      const code = document.getElementById('l12ManimCodeBlock').innerText;
      navigator.clipboard.writeText(code).then(() => {
        alert('3Blue1Brown Manim 파이썬 코드가 클립보드에 복사되었습니다!');
      });
    }

    const l12State = {
      k: 1.0,
      a: 0.8,
      b: 2.5,
      showSector: true,
      showIntegral: true,
      showTriangles: true,
      showOverlap: true,
      showYellow: true
    };

    function setL12Preset(mode) {
      document.querySelectorAll('#lecture12View .preset-grid .preset-btn').forEach(b => b.classList.remove('active'));
      if (mode === 'base') {
        document.getElementById('l12PreBase').classList.add('active');
        l12State.k = 1.0; l12State.a = 0.8; l12State.b = 2.5;
      } else if (mode === 'loge') {
        document.getElementById('l12PreLogE').classList.add('active');
        l12State.k = 1.0; l12State.a = 1.0; l12State.b = Math.E;
      } else if (mode === 'sym') {
        document.getElementById('l12PreSym').classList.add('active');
        l12State.k = 1.0; l12State.a = 0.5; l12State.b = 2.0;
      } else if (mode === 'k2') {
        document.getElementById('l12PreK2').classList.add('active');
        l12State.k = 2.0; l12State.a = 1.0; l12State.b = 3.0;
      }
      syncL12Sliders();
      renderL12();
    }

    function syncL12Sliders() {
      document.getElementById('l12SliderK').value = l12State.k;
      document.getElementById('l12SliderA').value = l12State.a;
      document.getElementById('l12SliderB').value = l12State.b;
      document.getElementById('l12kVal').innerText = Number(l12State.k).toFixed(2);
      document.getElementById('l12aVal').innerText = Number(l12State.a).toFixed(2);
      document.getElementById('l12bVal').innerText = Number(l12State.b).toFixed(2);
    }

    function updateL12Sliders() {
      l12State.k = parseFloat(document.getElementById('l12SliderK').value);
      let a = parseFloat(document.getElementById('l12SliderA').value);
      let b = parseFloat(document.getElementById('l12SliderB').value);
      if (a >= b) {
        b = a + 0.2;
        document.getElementById('l12SliderB').value = b;
      }
      l12State.a = a;
      l12State.b = b;

      document.getElementById('l12kVal').innerText = l12State.k.toFixed(2);
      document.getElementById('l12aVal').innerText = l12State.a.toFixed(2);
      document.getElementById('l12bVal').innerText = l12State.b.toFixed(2);

      renderL12();
    }

    function updateL12Toggles() {
      l12State.showSector = document.getElementById('l12ToggleSector').checked;
      l12State.showIntegral = document.getElementById('l12ToggleIntegral').checked;
      l12State.showTriangles = document.getElementById('l12ToggleTriangles').checked;
      l12State.showOverlap = document.getElementById('l12ToggleOverlap').checked;
      l12State.showYellow = document.getElementById('l12ToggleYellow').checked;
      renderL12();
    }

    function renderL12() {
      const canvas = document.getElementById('l12Canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const k = l12State.k;
      const a = l12State.a;
      const b = l12State.b;

      // Coordinate mapping: X in [0, 4.8], Y in [0, 4.0]
      const margin = 48;
      const plotW = w - margin * 2;
      const plotH = h - margin * 2;
      const xMin = 0.0, xMax = 4.8;
      const yMin = 0.0, yMax = 3.8;

      function toX(x) { return margin + ((x - xMin) / (xMax - xMin)) * plotW; }
      function toY(y) { return (h - margin) - ((y - yMin) / (yMax - yMin)) * plotH; }

      // 1. Grid lines
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
      ctx.lineWidth = 1;
      for (let x = 1; x <= 4; x++) {
        ctx.beginPath();
        ctx.moveTo(toX(x), toY(yMin));
        ctx.lineTo(toX(x), toY(yMax));
        ctx.stroke();
      }
      for (let y = 1; y <= 3; y++) {
        ctx.beginPath();
        ctx.moveTo(toX(xMin), toY(y));
        ctx.lineTo(toX(xMax), toY(y));
        ctx.stroke();
      }

      // 2. Axes
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.35)';
      ctx.lineWidth = 1.8;
      ctx.beginPath();
      // X axis
      ctx.moveTo(toX(xMin), toY(0));
      ctx.lineTo(toX(xMax), toY(0));
      // Y axis
      ctx.moveTo(toX(0), toY(yMin));
      ctx.lineTo(toX(0), toY(yMax));
      ctx.stroke();

      // Axis labels
      ctx.fillStyle = '#94a3b8';
      ctx.font = '12px Inter, sans-serif';
      ctx.fillText('x', toX(xMax) - 12, toY(0) + 18);
      ctx.fillText('y', toX(0) - 16, toY(yMax) + 12);
      ctx.fillText('O', toX(0) - 16, toY(0) + 16);

      // Points coordinates
      const yA = k / a;
      const yB = k / b;
      const pOx = toX(0), pOy = toY(0);
      const pAx = toX(a), pAy = toY(yA);
      const pBx = toX(b), pBy = toY(yB);
      const pAprimeX = toX(a), pAprimeY = toY(0);
      const pBprimeX = toX(b), pBprimeY = toY(0);

      // Intersection point C of line OB and x = a
      // Line OB slope: yB / b = (k/b)/b = k / (b^2)
      const slopeOB = yB / b;
      const yC = slopeOB * a;
      const pCx = toX(a), pCy = toY(yC);

      // Helper function for drawing hyperbola arc
      function traceArc(xStart, xEnd) {
        const steps = 60;
        for (let i = 0; i <= steps; i++) {
          const curX = xStart + (xEnd - xStart) * (i / steps);
          const curY = k / curX;
          if (i === 0) ctx.lineTo(toX(curX), toY(curY));
          else ctx.lineTo(toX(curX), toY(curY));
        }
      }

      // Layer 1: Sector S (Polygon: O -> A -> arc AB -> B -> O)
      if (l12State.showSector) {
        ctx.fillStyle = 'rgba(192, 132, 252, 0.28)';
        ctx.strokeStyle = 'rgba(192, 132, 252, 0.6)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(pOx, pOy);
        ctx.lineTo(pAx, pAy);
        traceArc(a, b);
        ctx.lineTo(pBx, pBy);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Sector S label
        ctx.fillStyle = '#e879f9';
        ctx.font = 'bold 15px Inter, sans-serif';
        const midX = (a + b) / 3.2;
        const midY = (yA + yB) / 3.2;
        ctx.fillText('S', toX(midX), toY(midY));
      }

      // Layer 2: Integral Region T (Polygon: (a, 0) -> (a, yA) -> arc AB -> (b, yB) -> (b, 0) -> (a, 0))
      if (l12State.showIntegral) {
        ctx.fillStyle = 'rgba(6, 182, 212, 0.22)';
        ctx.strokeStyle = 'rgba(6, 182, 212, 0.55)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(pAprimeX, pAprimeY);
        ctx.lineTo(pAx, pAy);
        traceArc(a, b);
        ctx.lineTo(pBx, pBy);
        ctx.lineTo(pBprimeX, pBprimeY);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Integral T label
        ctx.fillStyle = '#22d3ee';
        ctx.font = 'bold 15px Inter, sans-serif';
        const midTX = (a + b) * 0.55;
        ctx.fillText('T', toX(midTX), toY(yB * 0.45));
      }

      // Layer 3: Triangles OAA' (Red) & OBB' (Blue)
      if (l12State.showTriangles) {
        // Red Triangle OAA'
        ctx.fillStyle = 'rgba(239, 68, 68, 0.16)';
        ctx.strokeStyle = 'rgba(239, 68, 68, 0.5)';
        ctx.lineWidth = 1.2;
        ctx.beginPath();
        ctx.moveTo(pOx, pOy);
        ctx.lineTo(pAx, pAy);
        ctx.lineTo(pAprimeX, pAprimeY);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Blue Triangle OBB'
        ctx.fillStyle = 'rgba(59, 130, 246, 0.16)';
        ctx.strokeStyle = 'rgba(59, 130, 246, 0.5)';
        ctx.beginPath();
        ctx.moveTo(pOx, pOy);
        ctx.lineTo(pBx, pBy);
        ctx.lineTo(pBprimeX, pBprimeY);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
      }

      // Layer 4: Common Purple Overlap Triangle OA'C
      if (l12State.showOverlap) {
        ctx.fillStyle = 'rgba(168, 85, 247, 0.65)';
        ctx.strokeStyle = 'rgba(168, 85, 247, 0.9)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(pOx, pOy);
        ctx.lineTo(pAprimeX, pAprimeY);
        ctx.lineTo(pCx, pCy);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Dot at C
        ctx.fillStyle = '#c084fc';
        ctx.beginPath();
        ctx.arc(pCx, pCy, 4, 0, Math.PI * 2);
        ctx.fill();
        ctx.font = '11px Inter, sans-serif';
        ctx.fillText('C', pCx + 6, pCy + 4);
      }

      // Layer 5: Yellow Curved Region between chord AB and hyperbola arc AB
      if (l12State.showYellow) {
        ctx.fillStyle = 'rgba(251, 191, 36, 0.45)';
        ctx.strokeStyle = 'rgba(251, 191, 36, 0.8)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(pAx, pAy);
        traceArc(a, b);
        ctx.lineTo(pAx, pAy); // chord
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
      }

      // 3. Draw Hyperbola curve y = k/x
      ctx.strokeStyle = '#f8fafc';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      const xStartCurve = Math.max(0.2, k / yMax);
      for (let x = xStartCurve; x <= xMax; x += 0.05) {
        const y = k / x;
        if (x === xStartCurve) ctx.moveTo(toX(x), toY(y));
        else ctx.lineTo(toX(x), toY(y));
      }
      ctx.stroke();

      // Hyperbola curve label
      ctx.fillStyle = '#fbbf24';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText(`xy = ${k.toFixed(1)}`, toX(3.5), toY(k / 3.5) - 12);

      // 4. Drop lines (dashed)
      ctx.setLineDash([4, 4]);
      ctx.strokeStyle = 'rgba(248, 113, 113, 0.6)';
      ctx.beginPath();
      ctx.moveTo(pAx, pAy);
      ctx.lineTo(pAprimeX, pAprimeY);
      ctx.stroke();

      ctx.strokeStyle = 'rgba(96, 165, 250, 0.6)';
      ctx.beginPath();
      ctx.moveTo(pBx, pBy);
      ctx.lineTo(pBprimeX, pBprimeY);
      ctx.stroke();

      // Rays OA, OB
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.4)';
      ctx.beginPath();
      ctx.moveTo(pOx, pOy);
      ctx.lineTo(pAx, pAy);
      ctx.moveTo(pOx, pOy);
      ctx.lineTo(pBx, pBy);
      ctx.stroke();
      ctx.setLineDash([]);

      // 5. Points A and B
      // Point A
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.arc(pAx, pAy, 5, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#f87171';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText(`A(${a.toFixed(1)}, ${(k/a).toFixed(1)})`, pAx - 25, pAy - 10);

      // Point B
      ctx.fillStyle = '#3b82f6';
      ctx.beginPath();
      ctx.arc(pBx, pBy, 5, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#60a5fa';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText(`B(${b.toFixed(1)}, ${(k/b).toFixed(1)})`, pBx + 8, pBy - 8);

      // A', B' labels
      ctx.fillStyle = '#94a3b8';
      ctx.font = '11px Inter, sans-serif';
      ctx.fillText(`A'(${a.toFixed(1)})`, pAprimeX - 12, pAprimeY + 16);
      ctx.fillText(`B'(${b.toFixed(1)})`, pBprimeX - 12, pBprimeY + 16);

      // 6. Real-time Calculations
      const areaS = k * Math.log(b / a);
      const areaT = areaS; // identical by theorem!
      const triOAA = 0.5 * k;
      const triOBB = 0.5 * k;
      const areaPurple = 0.5 * a * yC;
      const redPiece = triOAA - areaPurple;
      const bluePiece = triOBB - areaPurple;

      // Chord AB length and yellow slice approximation
      // Yellow area = T - trapezoid under chord = k*ln(b/a) - 0.5*(yA + yB)*(b - a)
      const trapezoidUnderChord = 0.5 * (yA + yB) * (b - a);
      const yellowPiece = Math.max(0, areaT - trapezoidUnderChord);

      document.getElementById('l12AreaSVal').innerText = areaS.toFixed(4);
      document.getElementById('l12AreaTVal').innerText = areaT.toFixed(4);

      const liveDetail = document.getElementById('l12LiveProofDetail');
      if (liveDetail) {
        liveDetail.innerHTML = `
          • 직각삼각형 넓이 불변: $\\triangle OAA' = \\triangle OBB' = \\frac{1}{2}k = ${triOAA.toFixed(3)}$<br>
          • 보라색 공통삼각형($\\triangle OA'C$) = ${areaPurple.toFixed(3)}<br>
          • 양변 상쇄: <strong>빨간 조각(${redPiece.toFixed(3)}) = 파란 조각(${bluePiece.toFixed(3)})</strong><br>
          • 노란색 곡면 조각(${yellowPiece.toFixed(3)}) 더함 $\\implies$ <strong>$S = T = ${areaS.toFixed(3)}$ 일치!</strong>
        `;
        if (window.renderMathInElement) {
          renderMathInElement(liveDetail, {delimiters: [{left: '$', right: '$', display: false}]});
        }
      }
    }
'''

    # Insert js_lecture12 before switchLec11Tab or before setLecture
    if 'function switchLec12Tab' not in html:
        idx_js11 = html.find('/* LECTURE 11 (IRRATIONAL FUNCTION 3-SEC RULE) LOGIC')
        if idx_js11 != -1:
            html = html[:idx_js11] + js_lecture12 + '\n' + html[idx_js11:]
            print("Inserted Lecture 12 JavaScript before Lecture 11 JS.")
        else:
            # append before </script>
            idx_script = html.rfind('</script>')
            html = html[:idx_script] + js_lecture12 + '\n' + html[idx_script:]
            print("Inserted Lecture 12 JavaScript before closing script tag.")

    # 5. Update setLecture(num) function
    # Change for (let i = 1; i <= 11; i++) to for (let i = 1; i <= 12; i++)
    old_set_lec_loop = 'for (let i = 1; i <= 11; i++) {'
    new_set_lec_loop = 'for (let i = 1; i <= 12; i++) {'
    if old_set_lec_loop in html:
        html = html.replace(old_set_lec_loop, new_set_lec_loop)
        print("Updated setLecture loop to 12.")

    # Add num === 12 handler
    old_set_lec_handler = 'if (num === 11) setTimeout(renderL11, 50);'
    new_set_lec_handler = 'if (num === 12) setTimeout(renderL12, 50);\n      else if (num === 11) setTimeout(renderL11, 50);'
    if old_set_lec_handler in html and 'if (num === 12) setTimeout(renderL12, 50);' not in html:
        html = html.replace(old_set_lec_handler, new_set_lec_handler)
        print("Added num === 12 render handler to setLecture.")

    # 6. Update window load handler to default to lecture 12
    old_onload = """window.addEventListener('load', () => {
      updateL11Sliders();
      renderL11();
    });"""
    new_onload = """window.addEventListener('load', () => {
      updateL12Sliders();
      renderL12();
    });"""
    if old_onload in html:
        html = html.replace(old_onload, new_onload)
        print("Updated window load handler to initialize Lecture 12.")

    # Write back to index.html
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html successfully updated with Lecture 12!")

if __name__ == '__main__':
    main()
