# -*- coding: utf-8 -*-
"""
Script to build and inject Lecture 14 into index.html
Lecture: Is This a Local Maximum?! The Rigorous Definition of Extremum (Sharp & Punctured Extrema)
Instructor: Bae Sang-myeon (MathPresso / Chulbyuk Math)
YouTube Short: https://youtube.com/shorts/-yso0bScGvY
"""

import os
import re

def main():
    html_path = 'index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read manim code for tab
    with open('local_maximum_definition_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()

    # 1. Update Switcher Bar: Add btnLec14 as active, remove active from btnLec13
    if 'id="btnLec14"' not in html:
        old_btn13 = '<button class="lecture-btn active" id="btnLec13" onclick="setLecture(13)">'
        if old_btn13 in html:
            new_btn_block = '''<button class="lecture-btn active" id="btnLec14" onclick="setLecture(14)">
          이게 극대라고?! (배상면)
        </button>
        <button class="lecture-btn" id="btnLec13" onclick="setLecture(13)">'''
            html = html.replace(old_btn13, new_btn_block, 1)
            print("Added btnLec14 to switcher bar.")
        else:
            old_btn13_alt = '<button class="lecture-btn" id="btnLec13" onclick="setLecture(13)">'
            if old_btn13_alt in html:
                new_btn_block = '''<button class="lecture-btn active" id="btnLec14" onclick="setLecture(14)">
          이게 극대라고?! (배상면)
        </button>
        <button class="lecture-btn" id="btnLec13" onclick="setLecture(13)">'''
                html = html.replace(old_btn13_alt, new_btn_block, 1)
                print("Added btnLec14 to switcher bar (alt).")

    # Update captured_summary button label
    html = html.replace('📸 사진 1~13 핵심 전용 페이지', '📸 사진 1~14 핵심 전용 페이지')

    # 2. Hide lecture13View if active
    if '<div id="lecture13View">' in html:
        html = html.replace('<div id="lecture13View">', '<div id="lecture13View" style="display: none;">', 1)
        print("Set lecture13View to display: none.")

    # 3. Create Lecture 14 View HTML
    escaped_manim = (manim_code
                     .replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;'))

    lecture14_html = f'''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 14 (IS THIS LOCAL MAXIMUM?!: MATHPRESSO)     -->
    <!-- ============================================================== -->
    <div id="lecture14View">
      <header>
        <div class="badge-pill" style="border-color: rgba(239, 68, 68, 0.4); color: #f87171; box-shadow: 0 0 20px rgba(239, 68, 68, 0.3);">
          <span>📐 고1·고2 수학Ⅱ · 함수의 극대·극소 · 수능 킬러 진위판정 오개념 박멸</span>
        </div>
        <h1 style="background: linear-gradient(135deg, #ffffff 30%, #f87171 70%, #fb923c 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          이게 극대라고?! 함수의 극대·극소 진짜 정의 &amp; 극뾰대·극뻥대
        </h1>
        <p class="subtitle">
          "미분 불가능하다고 제끼지 말기! 뾰족해도 극대(극뾰대), 구멍이 뻥 뚫려도 극대(극뻥대)!" 열린구간 부등식 $f(x) \\le f(a)$의 본질을 현미경처럼 들여다보는 <strong>국소 최댓값(Local Maximum) 기하학 스튜디오</strong>입니다.
        </p>

        <div class="source-meta">
          <span>🎬 채널: <strong>매스프레소 MathPresso (배상면 선생님)</strong></span>
          <span>•</span>
          <a href="https://youtube.com/shorts/-yso0bScGvY" target="_blank" rel="noopener noreferrer" style="color: var(--accent-blue); text-decoration: none; display: inline-flex; align-items: center; gap: 4px;">
            <span>이게 극대라고 ?!! (0:33)</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          </a>
          <span>•</span>
          <span>강의 고화질 10단계 캡처 &amp; Manim 코드 탑재</span>
        </div>
      </header>

      <!-- Tab Bar for Lecture 14 -->
      <div class="tab-bar">
        <button class="tab-btn active" onclick="switchLec14Tab('l14SimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          인터랙티브 열린구간 국소 판정기 &amp; 4대 극대 시뮬레이터
        </button>
        <button class="tab-btn" onclick="switchLec14Tab('l14CaptureTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          강의 판서 캡처 &amp; 10단계 타임라인
        </button>
        <button class="tab-btn" onclick="switchLec14Tab('l14ProofTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>
          극대·극소 교과서식 정형화 &amp; 수능 ㄱ,ㄴ,ㄷ 치트키
        </button>
        <button class="tab-btn" onclick="switchLec14Tab('l14ManimTab')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          3Blue1Brown Manim 파이썬 코드
        </button>
      </div>

      <!-- TAB 1: INTERACTIVE SIMULATOR (LECTURE 14) -->
      <div id="l14SimTab" class="tab-panel active">
        <div class="glass-card">
          <!-- Dynamic Banner -->
          <div class="formula-banner" id="l14Banner" style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(245, 158, 11, 0.08)); border-color: rgba(239, 68, 68, 0.35);">
            <div class="label" id="l14BannerLabel" style="color: #f87171;">🌟 2015·2022 개정 수학Ⅱ 교과서 공식 정의 : 열린구간 부등식 판정법</div>
            <div class="math-main" id="l14BannerMath">
              $$x = a\\text{{를 포함하는 어떤 열린구간의 모든 }} x\\text{{에 대하여 }} \\mathbf{{f(x) \\le f(a)}} \\iff x=a\\text{{에서 극대 (Local Maximum)}}$$
            </div>
          </div>

          <div class="sim-grid">
            <!-- Canvas Box -->
            <div class="canvas-box">
              <canvas id="l14Canvas" width="580" height="520"></canvas>
              <div id="l14CanvasCaption" style="font-size: 0.85rem; color: var(--text-dim); margin-top: 10px; text-align: center;">
                열린구간 $(a-\\delta, a+\\delta)$ (빨간 띠) | 극대점 $(a, f(a))$ (보라색 구슬) | 함수 곡선 (노란색) | 펑크(빈 원)
              </div>
            </div>

            <!-- Controls & Live Evaluation -->
            <div class="sim-controls">
              <!-- Mode Selection -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🎯 4대 극대 케이스 선택</span>
                </div>
                <div class="preset-grid" style="grid-template-columns: 1fr 1fr;">
                  <button class="preset-btn active" id="l14CaseGrid" onclick="setL14Case('grid')" style="grid-column: span 2;">
                    <span>🌟 4개 케이스 동시 분할 비교 (영상 원본)</span>
                    <span class="p-sub" style="color: #f59e0b; font-weight: bold;">① 뾰족점 · ② 상수펑크 · ③ 계단식 · ④ 포물선펑크</span>
                  </button>
                  <button class="preset-btn" id="l14Case1" onclick="setL14Case('case1')">
                    <span>① 뾰족한 첨점 (극뾰대)</span>
                    <span class="p-sub" style="color: #38bdf8;">연속이지만 미분불가</span>
                  </button>
                  <button class="preset-btn" id="l14Case2" onclick="setL14Case('case2')">
                    <span>② 펑크 난 상수함수 (극뻥대)</span>
                    <span class="p-sub" style="color: #ec4899;">불연속 고립 상단점</span>
                  </button>
                  <button class="preset-btn" id="l14Case3" onclick="setL14Case('case3')">
                    <span>③ 계단식 불연속</span>
                    <span class="p-sub" style="color: #a78bfa;">좌우 비대칭 불연속</span>
                  </button>
                  <button class="preset-btn" id="l14Case4" onclick="setL14Case('case4')">
                    <span>④ 펑크 난 포물선</span>
                    <span class="p-sub" style="color: #34d399;">바닥 펑크 + 상단 점</span>
                  </button>
                </div>
              </div>

              <!-- Interval Parameter Sliders -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">🔬 열린구간 반경 $\\delta$ (Delta) 현미경 조절</span>
                </div>

                <div class="slider-row">
                  <label>열린구간 폭 $\\delta$: <strong id="l14DeltaVal" style="color: #f87171;">0.35</strong></label>
                  <input type="range" id="l14SliderDelta" min="0.10" max="0.80" step="0.05" value="0.35" oninput="updateL14Sliders()">
                </div>

                <div class="slider-row">
                  <label>검증 기준점 $x = a$: <strong id="l14AVal" style="color: #fbbf24;">0.00</strong></label>
                  <input type="range" id="l14SliderA" min="-1.0" max="1.0" step="0.1" value="0.0" oninput="updateL14Sliders()">
                </div>
              </div>

              <!-- Visual Layer Toggles -->
              <div class="control-card">
                <div class="control-header">
                  <span class="control-title">👁️ 시각화 레이어 On/Off</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 0.85rem;">
                  <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
                    <input type="checkbox" id="l14ToggleStrip" checked onchange="updateL14Toggles()">
                    <span>열린구간 $(a-\\delta, a+\\delta)$ 빨간 띠</span>
                  </label>
                  <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
                    <input type="checkbox" id="l14ToggleBoundLine" checked onchange="updateL14Toggles()">
                    <span>상한 기준선 $y = f(a)$</span>
                  </label>
                  <label style="display: flex; align-items: center; gap: 6px; cursor: pointer; grid-column: span 2;">
                    <input type="checkbox" id="l14ToggleDots" checked onchange="updateL14Toggles()">
                    <span>보라색 극대점 &amp; 펑크 구멍 강조</span>
                  </label>
                </div>
              </div>

              <!-- Real-time Verification Badge -->
              <div class="control-card" style="background: rgba(15, 23, 42, 0.95); border-color: rgba(239, 68, 68, 0.4);">
                <div class="control-header">
                  <span class="control-title" style="color: #f87171;">📊 국소 부등식 $f(x) \\le f(a)$ 판정 결과</span>
                  <span class="badge-pill-sm" id="l14JudgeBadge" style="background: #10b981; color: #fff;">극대 완벽 성립 (Local Max ⭕)</span>
                </div>

                <div id="l14LiveAnalysisText" style="margin-top: 10px; padding: 12px; background: rgba(0,0,0,0.35); border-radius: 8px; font-size: 0.84rem; color: #cbd5e1; line-height: 1.7;">
                  • <strong>열린구간 내부 조사:</strong> $x \\in (a-\\delta, a+\\delta)$ 내의 모든 점이 $f(a)$보다 낮거나 같습니다.<br>
                  • <strong>미분가능 여부:</strong> $f'(a)$ 존재 여부와 무관하게 <strong>극대 성립!</strong><br>
                  • <strong>배티의 암기 공식:</strong> 극대, 극뻥대, 뾰족해도 극대! 구멍이 뻥 뚫려도 주변보다 높으면 극대!
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: TIMELINE CAPTURES (LECTURE 14) -->
      <div id="l14CaptureTab" class="tab-panel">
        <div class="glass-card">
          <h2 style="font-size: 1.5rem; margin-bottom: 8px; color: var(--accent-gold);">
            📸 배상면 선생님 강의 10단계 판서 타임라인 &amp; 교재 해설
          </h2>
          <p style="color: var(--text-muted); font-size: 0.92rem; margin-bottom: 24px;">
            유튜브 쇼츠(0:33) 원본 영상의 극대 판정 퀴즈 전 과정을 1080p 고화질 캡처와 함께 완벽히 분석했습니다.
          </p>

          <div class="timeline-container">
            <!-- Card 1 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">1단계 [00:00:01]</span>
                <span class="timeline-title">인트로: "함수의 극대" 등장</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v14/01_local_maximum_intro.jpg" alt="01_local_maximum_intro">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "함수의 극대란..."
              </div>
              <div class="timeline-desc">
                <strong>도입부:</strong> 수능과 내신에서 수험생들이 가장 많이 오해하는 개념인 '극대'의 진짜 정의를 던집니다.
              </div>
            </div>

            <!-- Card 2 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">2단계 [00:00:03]</span>
                <span class="timeline-title">극대의 본질: "국소적으로 주변보다 높은 점"</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v14/02_definition_higher_than_neighbors.jpg" alt="02_definition_higher_than_neighbors">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "...국소적으로 주변보다 높은 점을 뜻한다."
              </div>
              <div class="timeline-desc">
                <strong>수학적 핵심:</strong> 전체 정의역이 아니라 특정 $x$ 주변의 좁은 '동네(열린구간)' 안에서 가장 높은 점을 의미합니다.
              </div>
            </div>

            <!-- Card 3 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">3단계 [00:00:06]</span>
                <span class="timeline-title">핵심 퀴즈 제시: "다음 중 $x=a$에서 극대인 것?"</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v14/03_question_which_is_local_max.jpg" alt="03_question_which_is_local_max">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "다음 중 x는 a에서 극대인 것은? 1번, 2번, 3번, 4번."
              </div>
              <div class="timeline-desc">
                <strong>문제 출제:</strong> 부드러운 언덕이 아닌, 뾰족점과 구멍 뚫린 특이점 4개를 제시합니다.
              </div>
            </div>

            <!-- Card 4 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">4단계 [00:00:11]</span>
                <span class="timeline-title">4대 후보 그래프 등장 (수험생 고정관념 테스트)</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v14/04_four_candidate_graphs.jpg" alt="04_four_candidate_graphs">
              </div>
              <div class="timeline-quote">
                <strong>화면 구성:</strong> ① 첨점, ② 펑크 난 수평선, ③ 계단식 불연속, ④ 펑크 난 포물선.
              </div>
              <div class="timeline-desc">
                <strong>그래프 분석:</strong> 보통 학생들은 미분이 불가능하거나 구멍이 났다는 이유로 4개 모두 탈락시키기 십상입니다.
              </div>
            </div>

            <!-- Card 5 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">5단계 [00:00:14]</span>
                <span class="timeline-title">정답 공개: "네 개 모두 극대!"</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v14/05_all_four_are_local_max.jpg" alt="05_all_four_are_local_max">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "정답은 네 개 모두 극대!"
              </div>
              <div class="timeline-desc">
                <strong>충격적 결과:</strong> 네 그래프 모두에 빨간 동그라미가 쳐지며 모두 극대임이 선언됩니다.
              </div>
            </div>

            <!-- Card 6 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">6단계 [00:00:16]</span>
                <span class="timeline-title">수학적 증명: 열린구간(Open Interval) 빨간 띠 설정</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v14/06_open_interval_definition.jpg" alt="06_open_interval_definition">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "x는 a의 좌우로 충분히 작은 구간을 잡았을 때..."
              </div>
              <div class="timeline-desc">
                <strong>기하학적 검증:</strong> 점 $x=a$를 포함하는 좁은 빨간 수직 띠 $(a-\\delta, a+\\delta)$를 시각화합니다.
              </div>
            </div>

            <!-- Card 7 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">7단계 [00:00:19]</span>
                <span class="timeline-title">보라색 점의 우위 확인: "주변보다 높기 때문!"</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v14/07_purple_dots_highest_points.jpg" alt="07_purple_dots_highest_points">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "...x는 a에서 주변보다 높기 때문이다."
              </div>
              <div class="timeline-desc">
                <strong>부등식 충족:</strong> 빨간 띠 안에서 $x=a$의 보라색 점이 주변의 모든 점보다 확실히 높은 곳에 존재합니다 ($f(x) \\le f(a)$).
              </div>
            </div>

            <!-- Card 8 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">8단계 [00:00:21]</span>
                <span class="timeline-title">수험생 경고: "미분 불가능하다고 제끼지 말기!"</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v14/08_do_not_exclude_non_differentiable.jpg" alt="08_do_not_exclude_non_differentiable">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "미분 불가능하다고 제끼지 말기!"
              </div>
              <div class="timeline-desc">
                <strong>수능 킬러 명제:</strong> "극대 $\\implies f'(a) = 0$"이라는 거짓 명제에 속아 첨점이나 불연속점을 버리지 말라는 강력한 당부입니다.
              </div>
            </div>

            <!-- Card 9 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">9단계 [00:00:27]</span>
                <span class="timeline-title">배티의 마법 암기법: "극대, 극뻥대, 뾰족해도 극대!"</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v14/09_peak_and_puncture_rhymes.jpg" alt="09_peak_and_puncture_rhymes">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "이렇게 기억해라. 극대, 극뻥대, 뾰족해도 극대!"
              </div>
              <div class="timeline-desc">
                <strong>귀에 꽂히는 라임:</strong> 극뾰대(뾰족해도 극대), 극뻥대(구멍 뚫려도 점이 위에 있으면 극대)로 단 1초 만에 뇌리에 각인됩니다.
              </div>
            </div>

            <!-- Card 10 -->
            <div class="timeline-card">
              <div class="timeline-header">
                <span class="timeline-badge">10단계 [00:00:31]</span>
                <span class="timeline-title">최종 결론: "구멍이 뻥 뚫려도 주변보다 높으면 극대다!"</span>
              </div>
              <div class="timeline-img-box">
                <img src="./captures_v14/10_final_definition_higher_than_neighbors.jpg" alt="10_final_definition_higher_than_neighbors">
              </div>
              <div class="timeline-quote">
                <strong>선생님 설명:</strong> "구멍이 뻥 뚫려도 주변보다 높으면 극대다."
              </div>
              <div class="timeline-desc">
                <strong>개념 완성:</strong> 극대의 본질은 미분계수가 아니라 **부등식 $f(x) \\le f(a)$**임을 명쾌하게 정리하며 강의가 마무리됩니다.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 3: MATHEMATICAL PROOF & RULES (LECTURE 14) -->
      <div id="l14ProofTab" class="tab-panel">
        <div class="glass-card" style="line-height: 1.8;">
          <h2 style="font-size: 1.5rem; margin-bottom: 12px; color: #f87171;">
            📐 함수의 극대·극소 엄밀한 교과서 정의 &amp; 수능 ㄱ,ㄴ,ㄷ 킬러 분석
          </h2>
          
          <div style="background: rgba(15, 23, 42, 0.7); padding: 20px; border-radius: 12px; border-left: 4px solid #f87171; margin-bottom: 24px;">
            <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">1. 현행 교육과정 교과서 공식 정의</h3>
            <p>
              함수 $f(x)$에 대하여 $x = a$를 포함하는 어떤 열린구간(Open Interval)이 존재하여, 그 구간에 속하는 모든 $x$에 대하여:
            </p>
            <ul style="padding-left: 20px; margin-top: 8px; color: #cbd5e1;">
              <li>$$\mathbf{{f(x) \\le f(a)}} \\implies f(x)\\text{{는 }} x=a\\text{{에서 }} \\mathbf{{\\text{{극대(Local Maximum)}}}}\\text{{라 하고, }} f(a)\\text{{를 }} \\mathbf{{\\text{{극댓값}}}}\\text{{이라 한다.}}$$</li>
              <li>$$\mathbf{{f(x) \\ge f(a)}} \\implies f(x)\\text{{는 }} x=a\\text{{에서 }} \\mathbf{{\\text{{극소(Local Minimum)}}}}\\text{{라 하고, }} f(a)\\text{{를 }} \\mathbf{{\\text{{극솟값}}}}\\text{{이라 한다.}}$$</li>
            </ul>
            <p style="margin-top: 10px; color: #fbbf24;">
              💡 <strong>핵심 포인트:</strong> 정의 어디에도 <strong>'미분가능'</strong>이나 <strong>'연속'</strong>이라는 조건이 없습니다! 오직 부등식 $f(x) \\le f(a)$ 하나만이 기준입니다.
            </p>
          </div>

          <div style="background: rgba(15, 23, 42, 0.7); padding: 20px; border-radius: 12px; border-left: 4px solid #38bdf8; margin-bottom: 24px;">
            <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">2. 수능/모의고사 단골 기출 참/거짓(ㄱ,ㄴ,ㄷ) 판정표</h3>
            <table style="width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 0.88rem; color: #cbd5e1;">
              <thead>
                <tr style="background: rgba(255,255,255,0.06); text-align: left;">
                  <th style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">시험 출제 명제</th>
                  <th style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">참/거짓</th>
                  <th style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">이유 및 반례</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); font-weight: bold;">1. $f(x)$가 $x=a$에서 극값을 가지면 $f'(a) = 0$이다.</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); color: #ef4444; font-weight: bold;">거짓 (X)</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">반례: $f(x) = -|x|$는 $x=0$에서 극대이지만 $f'(0)$은 미분불가!</td>
                </tr>
                <tr>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); font-weight: bold;">2. $f(x)$가 $x=a$에서 <strong>미분가능하고</strong> 극값을 가지면 $f'(a) = 0$이다.</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); color: #34d399; font-weight: bold;">참 (O)</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">페르마의 극값 정리(Fermat's Theorem). 미분가능 조건이 있을 때만 성립!</td>
                </tr>
                <tr>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); font-weight: bold;">3. $f'(a) = 0$이면 $f(x)$는 $x=a$에서 극값을 가진다.</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); color: #ef4444; font-weight: bold;">거짓 (X)</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">반례: $f(x) = x^3$은 $f'(0) = 0$이지만 극값이 아님 (변곡점).</td>
                </tr>
                <tr>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); font-weight: bold;">4. 상수함수 $f(x) = c$의 모든 점은 극대이자 극소이다.</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1); color: #34d399; font-weight: bold;">참 (O)</td>
                  <td style="padding: 10px; border: 1px solid rgba(255,255,255,0.1);">모든 $x$에 대해 $c \\le c$이므로 $f(x) \\le f(a)$와 $f(x) \\ge f(a)$를 동시 만족!</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="background: rgba(15, 23, 42, 0.7); padding: 20px; border-radius: 12px; border-left: 4px solid #34d399;">
            <h3 style="color: #fff; font-size: 1.15rem; margin-bottom: 8px;">3. 수능 킬러 문항 $g(x) = |f(x) - t|$와의 연결</h3>
            <ul style="padding-left: 20px; color: #cbd5e1;">
              <li>꺾어 올린 함수 $g(x) = |f(x) - t|$가 $x$축과 만나는 점 중 $f'(x) \\ne 0$인 점들은 뾰족한 첨점이 됩니다.</li>
              <li>이 첨점들은 <strong>미분은 불가능하지만 완벽한 '극소(Local Minimum)'</strong>가 됩니다!</li>
              <li>평가원 킬러 문항에서 "함수 $g(x)$의 극값의 개수를 구하시오"라고 물었을 때 미분계수가 0인 점만 세면 치명적인 오답이 됩니다!</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- TAB 4: MANIM PYTHON SCRIPT (LECTURE 14) -->
      <div id="l14ManimTab" class="tab-panel">
        <div class="glass-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <div>
              <h2 style="font-size: 1.4rem; color: #f87171;">3Blue1Brown 스타일 Manim 파이썬 애니메이션 코드</h2>
              <p style="color: var(--text-muted); font-size: 0.88rem; margin-top: 4px;">
                `local_maximum_definition_manim.py` - 수학교육용 수학 애니메이션 풀스크립트
              </p>
            </div>
            <button class="preset-btn" onclick="copyL14ManimCode()" style="padding: 8px 18px; border-color: #f87171; color: #f87171;">
              📋 파이썬 코드 복사하기
            </button>
          </div>

          <pre id="l14ManimCodeBlock" style="background: #020617; padding: 20px; border-radius: 10px; border: 1px solid var(--border-color); font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; color: #e2e8f0; overflow-x: auto; max-height: 600px; line-height: 1.5;"><code>{escaped_manim}</code></pre>
        </div>
      </div>
    </div>

'''

    # Insert lecture14_html right before lecture13View
    if 'id="lecture14View"' not in html:
        idx_lec13 = html.find('id="lecture13View"')
        if idx_lec13 != -1:
            target_str = '    <!-- ============================================================== -->\n    <!-- SECTION FOR LECTURE 13'
            if target_str in html:
                html = html.replace(target_str, lecture14_html + target_str, 1)
                print("Inserted lecture14View before lecture13View.")
            else:
                html = html.replace('<div id="lecture13View"', lecture14_html + '<div id="lecture13View"', 1)
                print("Inserted lecture14View before lecture13View (fallback).")

    # 4. Add JavaScript for Lecture 14
    js_lecture14 = '''
    /* ========================================================= */
    /* LECTURE 14 (IS THIS LOCAL MAXIMUM?!: MATHPRESSO) LOGIC    */
    /* ========================================================= */
    function switchLec14Tab(tabId) {
      document.querySelectorAll('#lecture14View .tab-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('#lecture14View .tab-btn').forEach(b => b.classList.remove('active'));
      const activePanel = document.getElementById(tabId);
      if (activePanel) activePanel.classList.add('active');
      event.currentTarget.classList.add('active');
      if (tabId === 'l14SimTab') setTimeout(renderL14, 50);
      if (window.renderMathInElement) {
        renderMathInElement(document.body, {delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]});
      }
    }

    function copyL14ManimCode() {
      const code = document.getElementById('l14ManimCodeBlock').innerText;
      navigator.clipboard.writeText(code).then(() => {
        alert('3Blue1Brown Manim 파이썬 코드가 클립보드에 복사되었습니다!');
      });
    }

    const l14State = {
      activeCase: 'grid', // 'grid', 'case1', 'case2', 'case3', 'case4'
      delta: 0.35,
      a: 0.0,
      showStrip: true,
      showBoundLine: true,
      showDots: true
    };

    function setL14Case(caseName) {
      document.querySelectorAll('#lecture14View .preset-grid .preset-btn').forEach(b => b.classList.remove('active'));
      l14State.activeCase = caseName;
      if (caseName === 'grid') document.getElementById('l14CaseGrid').classList.add('active');
      else if (caseName === 'case1') document.getElementById('l14Case1').classList.add('active');
      else if (caseName === 'case2') document.getElementById('l14Case2').classList.add('active');
      else if (caseName === 'case3') document.getElementById('l14Case3').classList.add('active');
      else if (caseName === 'case4') document.getElementById('l14Case4').classList.add('active');

      updateL14InfoCard();
      renderL14();
    }

    function updateL14Sliders() {
      l14State.delta = parseFloat(document.getElementById('l14SliderDelta').value);
      l14State.a = parseFloat(document.getElementById('l14SliderA').value);
      document.getElementById('l14DeltaVal').innerText = l14State.delta.toFixed(2);
      document.getElementById('l14AVal').innerText = l14State.a.toFixed(2);
      renderL14();
    }

    function updateL14Toggles() {
      l14State.showStrip = document.getElementById('l14ToggleStrip').checked;
      l14State.showBoundLine = document.getElementById('l14ToggleBoundLine').checked;
      l14State.showDots = document.getElementById('l14ToggleDots').checked;
      renderL14();
    }

    function updateL14InfoCard() {
      const text = document.getElementById('l14LiveAnalysisText');
      if (!text) return;

      const c = l14State.activeCase;
      if (c === 'grid') {
        text.innerHTML = `
          • <strong>4개 케이스 동시 분할 비교:</strong> ① 뾰족점(극뾰대), ② 펑크 난 상수함수(극뻥대), ③ 계단식 불연속, ④ 펑크 난 포물선.<br>
          • <strong>공통 결론:</strong> 4개 모두 점 $x=a$ 주변의 좁은 빨간 띠(열린구간) 안에서 $f(a)$가 가장 높으므로 <strong>4개 모두 100% 극대</strong>입니다!<br>
          • <strong>배티의 한마디:</strong> "미분 불가능하다고 제끼지 말기! 극대, 극뻥대, 뾰족해도 극대!"
        `;
      } else if (c === 'case1') {
        text.innerHTML = `
          • <strong>① 뾰족한 첨점 (극뾰대):</strong> $f(x) = M - k|x-a|$ 형태입니다.<br>
          • <strong>미분계수:</strong> 좌미분계수($+k$)와 우미분계수($-k$)가 달라 $f'(a)$는 존재하지 않습니다 (미분불가).<br>
          • <strong>극대 판정:</strong> 열린구간 $(a-\\delta, a+\\delta)$의 모든 $x$에 대해 $f(x) \\le f(a)$이므로 <strong>완벽한 극대!</strong>
        `;
      } else if (c === 'case2') {
        text.innerHTML = `
          • <strong>② 펑크 난 상수함수 (극뻥대):</strong> $x \\ne a$일 때 $f(x) = c$, $x=a$일 때 $f(a) = c + 1$.<br>
          • <strong>연속성:</strong> $\\lim_{{x \\to a}} f(x) = c \\ne f(a)$로 $x=a$에서 불연속입니다.<br>
          • <strong>극대 판정:</strong> 열린구간의 모든 $x$에 대해 $c \\le c + 1$이므로 <strong>완벽한 극대!</strong>
        `;
      } else if (c === 'case3') {
        text.innerHTML = `
          • <strong>③ 계단식 불연속:</strong> 좌극한 $< f(a)$, 우극한 $< f(a)$인 불연속 계단점.<br>
          • <strong>극대 판정:</strong> 좌우로 아주 좁은 열린구간을 잡으면 $f(a)$가 좌우 곡선의 모든 값보다 위에 있으므로 <strong>극대 성립!</strong>
        `;
      } else if (c === 'case4') {
        text.innerHTML = `
          • <strong>④ 펑크 난 포물선 (U자형 바닥 펑크):</strong> 원래 곡선의 최솟값 자리에 펑크가 나고 점이 상단에 찍힘.<br>
          • <strong>반전:</strong> 원래 포물선은 아래로 볼록하지만, $x=a$의 함숫값이 튀어나와 있으므로 <strong>국소적으로 극대!</strong>
        `;
      }

      if (window.renderMathInElement) {
        renderMathInElement(text, {delimiters: [{left: '$', right: '$', display: false}]});
      }
    }

    function renderL14() {
      const canvas = document.getElementById('l14Canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const delta = l14State.delta;
      const a = l14State.a;
      const c = l14State.activeCase;

      if (c === 'grid') {
        // Render 2x2 Grid with all 4 cases
        const halfW = w / 2;
        const halfH = h / 2;

        drawMiniCase(ctx, 1, 0, 0, halfW, halfH, '① 뾰족한 첨점 (극뾰대)', delta, a);
        drawMiniCase(ctx, 2, halfW, 0, halfW, halfH, '② 펑크 난 상수함수 (극뻥대)', delta, a);
        drawMiniCase(ctx, 3, 0, halfH, halfW, halfH, '③ 계단식 불연속', delta, a);
        drawMiniCase(ctx, 4, halfW, halfH, halfW, halfH, '④ 펑크 난 포물선', delta, a);

      } else {
        // Single Expanded Case
        const caseNum = parseInt(c.replace('case', ''));
        const titles = {
          1: '① 뾰족한 첨점 (극뾰대) : f(x) = M - k|x-a|',
          2: '② 펑크 난 상수함수 (극뻥대) : 불연속 고립 상단점',
          3: '③ 계단식 불연속 : 좌우 분리 불연속점',
          4: '④ 펑크 난 포물선 : 바닥 펑크 + 상단 분리점'
        };
        drawSingleCase(ctx, caseNum, 0, 0, w, h, titles[caseNum], delta, a);
      }
    }

    function drawMiniCase(ctx, caseNum, ox, oy, pw, ph, title, delta, a) {
      const margin = 28;
      const plotW = pw - margin * 2;
      const plotH = ph - margin * 2;
      const xMin = -1.5, xMax = 1.5;
      const yMin = -0.8, yMax = 1.8;

      function toX(x) { return ox + margin + ((x - xMin) / (xMax - xMin)) * plotW; }
      function toY(y) { return oy + (ph - margin) - ((y - yMin) / (yMax - yMin)) * plotH; }

      // Sub-box background & border
      ctx.fillStyle = 'rgba(15, 23, 42, 0.45)';
      ctx.fillRect(ox + 4, oy + 4, pw - 8, ph - 8);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
      ctx.strokeRect(ox + 4, oy + 4, pw - 8, ph - 8);

      // Title
      ctx.fillStyle = '#fbbf24';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText(title, ox + 12, oy + 22);

      // Red open interval strip
      if (l14State.showStrip) {
        ctx.fillStyle = 'rgba(239, 68, 68, 0.22)';
        const stripLeft = toX(a - delta);
        const stripRight = toX(a + delta);
        ctx.fillRect(stripLeft, oy + margin, stripRight - stripLeft, plotH);
      }

      // Vertical line x = a
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
      ctx.setLineDash([3, 3]);
      ctx.beginPath();
      ctx.moveTo(toX(a), oy + margin);
      ctx.lineTo(toX(a), oy + ph - margin);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText('a', toX(a) - 3, oy + ph - margin + 14);

      // Draw Curve according to caseNum
      drawCurveForCase(ctx, caseNum, toX, toY, a);
    }

    function drawSingleCase(ctx, caseNum, ox, oy, pw, ph, title, delta, a) {
      const margin = 48;
      const plotW = pw - margin * 2;
      const plotH = ph - margin * 2;
      const xMin = -1.8, xMax = 1.8;
      const yMin = -0.8, yMax = 1.8;

      function toX(x) { return ox + margin + ((x - xMin) / (xMax - xMin)) * plotW; }
      function toY(y) { return oy + (ph - margin) - ((y - yMin) / (yMax - yMin)) * plotH; }

      // Title
      ctx.fillStyle = '#f87171';
      ctx.font = 'bold 16px Inter, sans-serif';
      ctx.fillText(title, ox + 20, oy + 32);

      // Red open interval strip
      if (l14State.showStrip) {
        ctx.fillStyle = 'rgba(239, 68, 68, 0.22)';
        const stripLeft = toX(a - delta);
        const stripRight = toX(a + delta);
        ctx.fillRect(stripLeft, oy + margin, stripRight - stripLeft, plotH);

        // Strip boundaries text
        ctx.fillStyle = '#f87171';
        ctx.font = '11px Inter, sans-serif';
        ctx.fillText('a - δ', stripLeft - 12, oy + ph - margin + 18);
        ctx.fillText('a + δ', stripRight - 12, oy + ph - margin + 18);
      }

      // Axes
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.35)';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(toX(xMin), toY(0));
      ctx.lineTo(toX(xMax), toY(0));
      ctx.stroke();

      // Vertical line x = a
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(toX(a), oy + margin);
      ctx.lineTo(toX(a), oy + ph - margin);
      ctx.stroke();
      ctx.setLineDash([]);

      ctx.fillStyle = '#f8fafc';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillText('x = a', toX(a) - 14, oy + ph - margin + 16);

      // Draw Curve
      drawCurveForCase(ctx, caseNum, toX, toY, a);
    }

    function drawCurveForCase(ctx, caseNum, toX, toY, a) {
      let maxVal = 1.2;

      if (caseNum === 1) {
        // Cusp: y = 1.2 - 1.2 * |x - a|
        maxVal = 1.2;
        ctx.strokeStyle = '#facc15';
        ctx.lineWidth = 2.8;
        ctx.beginPath();
        for (let x = -1.4; x <= 1.4; x += 0.05) {
          const y = 1.2 - 1.2 * Math.abs(x - a);
          if (x === -1.4) ctx.moveTo(toX(x), toY(y));
          else ctx.lineTo(toX(x), toY(y));
        }
        ctx.stroke();

      } else if (caseNum === 2) {
        // Constant y = 0.2 with hole at x = a, dot at y = 1.2
        maxVal = 1.2;
        ctx.strokeStyle = '#facc15';
        ctx.lineWidth = 2.8;
        // left
        ctx.beginPath();
        ctx.moveTo(toX(-1.4), toY(0.2));
        ctx.lineTo(toX(a - 0.06), toY(0.2));
        ctx.stroke();
        // right
        ctx.beginPath();
        ctx.moveTo(toX(a + 0.06), toY(0.2));
        ctx.lineTo(toX(1.4), toY(0.2));
        ctx.stroke();

        // Hole
        drawHole(ctx, toX(a), toY(0.2), '#facc15');

      } else if (caseNum === 3) {
        // Step discontinuity: left approaches (a, -0.2), dot at (a, 0.8), right decreases
        maxVal = 0.8;
        ctx.strokeStyle = '#facc15';
        ctx.lineWidth = 2.8;
        // left curve
        ctx.beginPath();
        for (let x = -1.4; x <= a - 0.06; x += 0.05) {
          const y = 0.7 * Math.pow(x - a, 2) - 0.2;
          if (x === -1.4) ctx.moveTo(toX(x), toY(y));
          else ctx.lineTo(toX(x), toY(y));
        }
        ctx.stroke();

        // right curve
        ctx.beginPath();
        for (let x = a + 0.06; x <= 1.4; x += 0.05) {
          const y = -0.7 * (x - a) + 0.6;
          if (x === a + 0.06) ctx.moveTo(toX(x), toY(y));
          else ctx.lineTo(toX(x), toY(y));
        }
        ctx.stroke();

        // Hole at left end
        drawHole(ctx, toX(a), toY(-0.2), '#facc15');

      } else if (caseNum === 4) {
        // Parabola y = 1.0*(x-a)^2 - 0.3 with hole at (a, -0.3), dot at (a, 0.9)
        maxVal = 0.9;
        ctx.strokeStyle = '#facc15';
        ctx.lineWidth = 2.8;
        ctx.beginPath();
        for (let x = -1.4; x <= a - 0.06; x += 0.05) {
          const y = 1.0 * Math.pow(x - a, 2) - 0.3;
          if (x === -1.4) ctx.moveTo(toX(x), toY(y));
          else ctx.lineTo(toX(x), toY(y));
        }
        ctx.stroke();

        ctx.beginPath();
        for (let x = a + 0.06; x <= 1.4; x += 0.05) {
          const y = 1.0 * Math.pow(x - a, 2) - 0.3;
          if (x === a + 0.06) ctx.moveTo(toX(x), toY(y));
          else ctx.lineTo(toX(x), toY(y));
        }
        ctx.stroke();

        // Hole at bottom
        drawHole(ctx, toX(a), toY(-0.3), '#facc15');
      }

      // Bound line y = f(a)
      if (l14State.showBoundLine) {
        ctx.strokeStyle = 'rgba(168, 85, 247, 0.5)';
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(toX(-1.4), toY(maxVal));
        ctx.lineTo(toX(1.4), toY(maxVal));
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Purple local max dot
      if (l14State.showDots) {
        ctx.fillStyle = '#c084fc';
        ctx.beginPath();
        ctx.arc(toX(a), toY(maxVal), 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }
    }

    function drawHole(ctx, cx, cy, col) {
      ctx.fillStyle = '#070a13';
      ctx.beginPath();
      ctx.arc(cx, cy, 4.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = col;
      ctx.lineWidth = 2.0;
      ctx.stroke();
    }
'''

    # Insert js_lecture14 before switchLec13Tab
    if 'function switchLec14Tab' not in html:
        idx_js13 = html.find('/* LECTURE 13 (Y VS F(X): TERRITORY VS RESIDENT) LOGIC')
        if idx_js13 != -1:
            html = html[:idx_js13] + js_lecture14 + '\n' + html[idx_js13:]
            print("Inserted Lecture 14 JavaScript before Lecture 13 JS.")
        else:
            idx_script = html.rfind('</script>')
            html = html[:idx_script] + js_lecture14 + '\n' + html[idx_script:]
            print("Inserted Lecture 14 JavaScript before closing script tag.")

    # 5. Update setLecture(num) loop and handlers
    # Change for (let i = 1; i <= 13; i++) to for (let i = 1; i <= 14; i++)
    old_loop = 'for (let i = 1; i <= 13; i++) {'
    new_loop = 'for (let i = 1; i <= 14; i++) {'
    if old_loop in html:
        html = html.replace(old_loop, new_loop)
        print("Updated setLecture loop to 14.")

    # Add num === 14 handler
    old_handler = 'if (num === 13) setTimeout(renderL13, 50);'
    new_handler = 'if (num === 14) setTimeout(renderL14, 50);\n      else if (num === 13) setTimeout(renderL13, 50);'
    if old_handler in html and 'if (num === 14) setTimeout(renderL14, 50);' not in html:
        html = html.replace(old_handler, new_handler)
        print("Added num === 14 render handler to setLecture.")

    # 6. Update window load handler to default to lecture 14
    old_onload = """window.addEventListener('load', () => {
      renderL13();
    });"""
    new_onload = """window.addEventListener('load', () => {
      renderL14();
    });"""
    if old_onload in html:
        html = html.replace(old_onload, new_onload)
        print("Updated window load handler to initialize Lecture 14.")

    # Write back to index.html
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html successfully updated with Lecture 14!")

if __name__ == '__main__':
    main()
