# -*- coding: utf-8 -*-
"""
Script to build and inject Lecture 19 into index.html
Lecture: [수1/미적분] 지수함수와 로그함수 (역함수 교점)
Channel: 너도 아는 수학
YouTube Shorts: https://youtube.com/shorts/hTNIh08SkLA
"""

import os
import re

def main():
    html_path = 'index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read manim code for tab
    with open('exp_log_inverse_intersection_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()

    # 1. Update Navigation Bar Counts & Titles
    # 'all' badge 18 -> 19
    html = re.sub(
        r'(<button type="button" class="subj-tab(?: active)?" data-subject="all"[^>]*>[\s\S]*?<span class="tab-badge">)18(</span>)',
        r'\g<1>19\g<2>',
        html
    )

    # 'math1' badge 3 -> 4, and title
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math1"[^>]*>[\s\S]*?<span class="tab-text">)([^<]+)(</span>[\s\S]*?<span class="tab-badge">)3(</span>)',
        r'\g<1>수학 I · 지수로그·삼각\g<3>4\g<4>',
        html
    )

    # captured summary link
    html = html.replace('사진 1~18 요약집', '사진 1~19 요약집')
    html = html.replace('사진 1~18 핵심 전용 페이지', '사진 1~19 핵심 전용 페이지')

    # Remove active from btnLec18
    html = html.replace('id="btnLec18" onclick="setLecture(18)" class="lecture-btn active"', 'id="btnLec18" onclick="setLecture(18)" class="lecture-btn"')
    html = html.replace('class="lecture-btn active" id="btnLec18"', 'class="lecture-btn" id="btnLec18"')

    # In group-math1, add btnLec19
    if 'id="btnLec19"' not in html:
        target_group1 = '<div class="subject-panel" id="group-math1" data-subj="math1">'
        math1_replacement = '''<div class="subject-panel" id="group-math1" data-subj="math1">
          <div class="subj-header">
            <span class="subj-indicator ind-green"></span>
            <span class="subj-title-text">📗 수학 I · 지수·로그 &amp; 삼각함수</span>
            <span class="subj-sub">(지수·로그함수 역함수 교점 · 단위원 · 8칸 박스법 · 삼각비)</span>
          </div>
          <div class="lecture-btn-grid">
            <button type="button" class="lecture-btn active" id="btnLec19" onclick="setLecture(19)" data-subj="math1">
              <span class="lec-num">19</span>
              <span class="badge-pill-sm">⚡ 8초</span>
              <span class="lec-title">지수·로그함수와 역함수 교점</span>
            </button>'''
        
        # Replace the header and start of grid
        old_math1_header_pattern = r'<div class="subject-panel" id="group-math1" data-subj="math1">\s*<div class="subj-header">[\s\S]*?</div>\s*<div class="lecture-btn-grid">'
        html = re.sub(old_math1_header_pattern, math1_replacement, html, count=1)
        print("Inserted btnLec19 into group-math1.")

    # Update Status banner default
    html = re.sub(
        r'<span class="status-subj" id="statusSubjText">[^<]+</span>\s*<span class="status-sep">/</span>\s*<span class="status-title" id="statusTitleText">[^<]+</span>',
        r'<span class="status-subj" id="statusSubjText">수학 I · 지수·로그함수</span>\n        <span class="status-sep">/</span>\n        <span class="status-title" id="statusTitleText">제19강 · 지수·로그함수와 역함수 교점</span>',
        html
    )

    # Set lecture18View to display: none
    html = html.replace('<div id="lecture18View">', '<div id="lecture18View" style="display: none;">')

    # 2. Build Lecture 19 View
    escaped_manim = (manim_code
                     .replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;'))

    lecture19_html = f'''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 19 (EXPONENTIAL & LOGARITHMIC INVERSE INTERSECTION) -->
    <!-- ============================================================== -->
    <div id="lecture19View">
      <header>
        <div class="badge-pill" style="border-color: rgba(52, 211, 153, 0.4); color: #34d399; box-shadow: 0 0 20px rgba(52, 211, 153, 0.3);">
          ⚡ 제19강 · 너도 아는 수학 (수1/미적분)
        </div>
        <h1 style="background: linear-gradient(135deg, #34d399 0%, #38bdf8 50%, #fbbf24 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          지수함수와 로그함수의 역함수 교점과 임계 밑 $a = e^{{1/e}}$
        </h1>
        <p class="subtitle" style="max-width: 900px; margin: 0 auto; line-height: 1.7; color: #cbd5e1;">
          "밑이 같은 지수함수와 로그함수는 서로 역함수이며 $y=x$ 대칭이다!"<br>
          밑 $a > 1$일 때, 두 그래프의 교점 개수는 어떻게 달라질까?<br>
          <strong>접선 기울기 1 조건 · 자연상수 접점 $(e, e)$ · 임계 밑 $a = e^{{1/e}} \\approx 1.4447$ · 0개/1개/2개 분기</strong>를 실시간 인터랙티브 시각화로 완벽 마스터합니다.
        </p>
      </header>

      <!-- TOP SUMMARY BANNER -->
      <div style="background: linear-gradient(135deg, rgba(52, 211, 153, 0.15), rgba(56, 189, 248, 0.12), rgba(15, 23, 42, 0.95)); border: 2px solid rgba(52, 211, 153, 0.4); border-radius: 20px; padding: 26px; margin-bottom: 35px; box-shadow: 0 12px 36px rgba(0, 0, 0, 0.5);">
        <div style="font-size: 0.95rem; font-weight: 700; color: #34d399; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px; text-align: center;">
          ⭐ 지수·로그 역함수 교점 황금 공식 매트릭스: $f(x)=a^x, \\; g(x)=\\log_a x$
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; text-align: center; margin-top: 15px;">
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(52, 211, 153, 0.3);">
            <div style="color: #34d399; font-weight: bold; font-size: 0.85rem;">1. 교점 2개 (관통)</div>
            <div style="color: #fff; font-size: 1.05rem; font-family: monospace; margin-top: 3px;">$1 < a < e^{{1/e}} \\approx 1.445$</div>
            <div style="color: #94a3b8; font-size: 0.75rem; margin-top: 2px;">예: $a=\\sqrt{{2}} \\implies (2,2), (4,4)$</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(251, 191, 36, 0.3);">
            <div style="color: #fbbf24; font-weight: bold; font-size: 0.85rem;">2. 접점 1개 (임계치)</div>
            <div style="color: #fff; font-size: 1.05rem; font-family: monospace; margin-top: 3px;">$a = e^{{1/e}} \\approx 1.4447$</div>
            <div style="color: #94a3b8; font-size: 0.75rem; margin-top: 2px;">유일한 접점 $(e, e)$ 탄생</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(244, 63, 94, 0.3);">
            <div style="color: #f43f5e; font-weight: bold; font-size: 0.85rem;">3. 교점 0개 (분리)</div>
            <div style="color: #fff; font-size: 1.05rem; font-family: monospace; margin-top: 3px;">$a > e^{{1/e}} \\approx 1.445$</div>
            <div style="color: #94a3b8; font-size: 0.75rem; margin-top: 2px;">예: $a=2, 3 \\implies a^x > x$ 항상 성립</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(192, 132, 252, 0.3);">
            <div style="color: #c084fc; font-weight: bold; font-size: 0.85rem;">4. 감소함수 킬러 반례</div>
            <div style="color: #fff; font-size: 1.05rem; font-family: monospace; margin-top: 3px;">$0 < a < e^{{-e}} \\approx 0.066$</div>
            <div style="color: #94a3b8; font-size: 0.75rem; margin-top: 2px;">교점 3개 (2개는 $y=x$ 바깥 대칭점)</div>
          </div>
        </div>
      </div>

      <!-- MAIN INTERACTIVE LAB: EXPONENTIAL & LOGARITHM INTERSECTION SIMULATOR -->
      <div class="card" style="margin-bottom: 40px; border-color: rgba(52, 211, 153, 0.4); box-shadow: 0 10px 30px rgba(52, 211, 153, 0.15);">
        <h2 style="color: #34d399; display: flex; align-items: center; gap: 10px;">
          <span>📈</span> 지수함수 $y=a^x$ 와 로그함수 $y=\\log_a x$ 동적 교점 실험실
        </h2>
        <p style="color: #94a3b8; line-height: 1.6; margin-bottom: 20px;">
          밑 $a$ 슬라이더를 미세 조작하며 지수곡선과 로그곡선이 직선 $y=x$와 만나는 교점 개수(0개, 1개 접함, 2개)를 실시간으로 탐구해보세요.
        </p>

        <!-- PRESET BUTTONS -->
        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px;">
          <span style="font-size: 0.85rem; color: #94a3b8; align-self: center; margin-right: 4px;">🎯 프리셋:</span>
          <button class="btn btn-secondary" onclick="applyPreset19(1.4447)" style="font-size: 0.8rem; padding: 6px 12px; border-color: #fbbf24; color: #fbbf24;">
            🌟 임계 밑: a = e^(1/e) ≈ 1.445 (접점 1개)
          </button>
          <button class="btn btn-secondary" onclick="applyPreset19(1.4142)" style="font-size: 0.8rem; padding: 6px 12px;">
            수능 빈출: a = √2 ≈ 1.414 (교점 2개: (2,2), (4,4))
          </button>
          <button class="btn btn-secondary" onclick="applyPreset19(1.25)" style="font-size: 0.8rem; padding: 6px 12px;">
            완만한 증가: a = 1.25 (교점 2개)
          </button>
          <button class="btn btn-secondary" onclick="applyPreset19(2.0)" style="font-size: 0.8rem; padding: 6px 12px;">
            교과서 기본형: a = 2.0 (교점 0개)
          </button>
          <button class="btn btn-secondary" onclick="applyPreset19(0.5)" style="font-size: 0.8rem; padding: 6px 12px;">
            감소함수: a = 0.5 (교점 1개)
          </button>
          <button class="btn btn-secondary" onclick="applyPreset19(0.04)" style="font-size: 0.8rem; padding: 6px 12px; border-color: #c084fc; color: #c084fc;">
            🚨 킬러 반례: a = 0.04 &lt; e^(-e) (교점 3개!)
          </button>
          <button class="btn btn-primary" id="btnAnim19" onclick="toggleAnimation19()" style="font-size: 0.8rem; padding: 6px 14px; background: #34d399; color: #0f172a; font-weight: bold;">
            ▶ 밑 a 임계 스위프 애니메이션
          </button>
        </div>

        <div style="display: grid; grid-template-columns: 320px 1fr; gap: 24px; align-items: start;">
          <!-- CONTROLS COLUMN -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 18px;">
            <!-- Formula Display -->
            <div style="background: #030712; border: 1px solid rgba(52, 211, 153, 0.4); border-radius: 8px; padding: 12px; margin-bottom: 16px; text-align: center;">
              <div style="color: #94a3b8; font-size: 0.75rem; letter-spacing: 1px;">현재 함수 쌍</div>
              <div id="dispFormula19" style="font-size: 1.15rem; font-weight: bold; color: #34d399; margin: 4px 0; font-family: monospace;">
                y = 1.445^x &amp; y = log_{{1.445}}(x)
              </div>
            </div>

            <!-- a Slider -->
            <div style="margin-bottom: 18px;">
              <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
                <span style="color: #34d399; font-weight: bold;">밑 a (Base):</span>
                <span id="valA19" style="color: #34d399; font-family: monospace; font-weight: bold; font-size: 1rem;">1.445</span>
              </div>
              <input type="range" id="sliderA19" min="0.02" max="3.0" step="0.005" value="1.4447"
                     oninput="updateFromSliders19()" style="width: 100%; accent-color: #34d399;">
              <div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #64748b; margin-top: 4px;">
                <span>0.02 (급감소)</span>
                <span style="color: #fbbf24; font-weight: bold;">e^(1/e)≈1.445</span>
                <span>3.0 (급증가)</span>
              </div>
            </div>

            <!-- Visual Guides Checkboxes -->
            <div style="border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 14px; margin-top: 14px;">
              <label style="display: flex; align-items: center; gap: 8px; font-size: 0.82rem; color: #cbd5e1; margin-bottom: 10px; cursor: pointer;">
                <input type="checkbox" id="chkLineYX19" onchange="updateL19()" checked>
                <span>대칭축 직선 $y = x$ 표시 (노란 점선)</span>
              </label>
              <label style="display: flex; align-items: center; gap: 8px; font-size: 0.82rem; color: #cbd5e1; margin-bottom: 10px; cursor: pointer;">
                <input type="checkbox" id="chkCritPoint19" onchange="updateL19()" checked>
                <span>임계 접점 $(e, e) \\approx (2.718, 2.718)$ 가이드</span>
              </label>
              <label style="display: flex; align-items: center; gap: 8px; font-size: 0.82rem; color: #cbd5e1; margin-bottom: 10px; cursor: pointer;">
                <input type="checkbox" id="chkShowLog19" onchange="updateL19()" checked>
                <span>역함수 $y = \\log_a x$ 곡선 함께 표시</span>
              </label>
              <label style="display: flex; align-items: center; gap: 8px; font-size: 0.82rem; color: #cbd5e1; cursor: pointer;">
                <input type="checkbox" id="chkIntersections19" onchange="updateL19()" checked>
                <span>교점 좌표 실시간 감지 및 하이라이트</span>
              </label>
            </div>

            <!-- Status Readout Cards -->
            <div style="margin-top: 20px; display: flex; flex-direction: column; gap: 10px;">
              <div style="background: rgba(2, 6, 23, 0.8); padding: 12px; border-radius: 8px; border-left: 3px solid #34d399;">
                <div style="font-size: 0.72rem; color: #94a3b8; text-transform: uppercase;">교점 판정 상태</div>
                <div id="statStatus19" style="font-size: 0.95rem; font-weight: bold; color: #fbbf24; margin-top: 2px;">
                  1개 접점 (접함!)
                </div>
              </div>
              <div style="background: rgba(2, 6, 23, 0.8); padding: 12px; border-radius: 8px; border-left: 3px solid #38bdf8;">
                <div style="font-size: 0.72rem; color: #94a3b8; text-transform: uppercase;">실시간 교점 좌표</div>
                <div id="statCoords19" style="font-size: 0.85rem; font-family: monospace; color: #38bdf8; margin-top: 2px;">
                  (2.72, 2.72)
                </div>
              </div>
            </div>
          </div>

          <!-- CANVAS & READOUT COLUMN -->
          <div>
            <div style="position: relative; background: #030712; border: 1px solid rgba(52, 211, 153, 0.3); border-radius: 12px; overflow: hidden; box-shadow: inset 0 0 40px rgba(0,0,0,0.8);">
              <canvas id="canvasL19" width="760" height="520" style="width: 100%; height: auto; display: block;"></canvas>
              
              <!-- Quick Info Badge in Canvas -->
              <div style="position: absolute; top: 12px; right: 12px; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(8px); border: 1px solid rgba(52, 211, 153, 0.4); border-radius: 8px; padding: 8px 14px; font-size: 0.75rem; color: #e2e8f0; pointer-events: none;">
                <span style="color: #38bdf8;">■ y = a^x (지수)</span> &nbsp;|&nbsp;
                <span style="color: #fb7185;">■ y = log_a(x) (로그)</span> &nbsp;|&nbsp;
                <span style="color: #facc15;">-- y = x</span>
              </div>
            </div>

            <!-- Mathematical Insight Footer -->
            <div style="margin-top: 14px; padding: 14px 18px; background: rgba(52, 211, 153, 0.08); border-radius: 10px; border: 1px solid rgba(52, 211, 153, 0.2); font-size: 0.85rem; color: #cbd5e1; line-height: 1.6;">
              💡 <strong>핵심 기하학적 원리</strong>: 밑 $a > 1$일 때 $f(x)=a^x$는 단조 증가하므로 역함수와의 모든 교점은 반드시 직선 $y=x$ 위에 위치합니다. 곡선이 $y=x$와 접하는 조건인 $a^t = t$ 및 $a^t \\ln a = 1$로부터 접점은 정확히 <strong>$(e, e)$</strong>이며, 이때의 밑은 <strong>$a = e^{{1/e}} \\approx 1.444668$</strong>임을 수학적으로 증명할 수 있습니다.
            </div>
          </div>
        </div>
      </div>

      <!-- TABS SECTION -->
      <div class="card" style="margin-top: 30px;">
        <div style="display: flex; gap: 8px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 12px; margin-bottom: 24px; overflow-x: auto;">
          <button class="btn btn-secondary active" id="tabBtnL19_1" onclick="switchL19Tab(1)">📸 9단계 영상 캡처 타임라인</button>
          <button class="btn btn-secondary" id="tabBtnL19_2" onclick="switchL19Tab(2)">📐 엄밀한 수학적 유도 ($a=e^{{1/e}}$)</button>
          <button class="btn btn-secondary" id="tabBtnL19_3" onclick="switchL19Tab(3)">🎬 3Blue1Brown Manim 코드</button>
          <button class="btn btn-secondary" id="tabBtnL19_4" onclick="switchL19Tab(4)">🎥 원본 쇼츠 영상 (너도 아는 수학)</button>
          <button class="btn btn-secondary" id="tabBtnL19_5" onclick="switchL19Tab(5)">📝 수능 킬러 진위판정 공략</button>
        </div>

        <!-- TAB 1: 9-STEP CAPTURE TIMELINE -->
        <div id="tabL19_1" class="tab-pane-l19">
          <h3 style="color: #34d399; margin-bottom: 18px;">📸 너도 아는 수학 쇼츠 타임라인별 핵심 판서 캡처</h3>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
            
            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v19/01_title_intro.jpg" alt="01_title_intro" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(52, 211, 153, 0.2); color: #34d399;">1단계 [00:01]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">지수함수와 로그함수 세팅</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  밑이 $a$로 동일한 두 함수 $y=a^x$와 $y=\log_a x$는 서로 역함수 관계임을 선언하며 강의가 시작됩니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v19/02_exp_log_inverse_setup.jpg" alt="02_exp_log_inverse_setup" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(52, 211, 153, 0.2); color: #34d399;">2단계 [00:02]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">대칭축 직선 $y = x$</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  역함수의 기하학적 본질인 직선 $y=x$ 대칭축을 작도하여 두 곡선이 거울에 비친 상임을 직관화합니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v19/03_line_y_equals_x_symmetry.jpg" alt="03_line_y_equals_x_symmetry" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(52, 211, 153, 0.2); color: #34d399;">3단계 [00:03]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">대칭 곡선의 대비</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  지수함수의 점 $(0, 1)$과 로그함수의 점 $(1, 0)$이 완벽히 대칭 대응됨을 비교합니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v19/04_curve_intersection_concept.jpg" alt="04_curve_intersection_concept" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(52, 211, 153, 0.2); color: #34d399;">4단계 [00:04]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">교점의 존재성 문제 제기</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  "과연 두 곡선은 만날 수 있을까?" 교과서 예제에 익숙한 학생들의 편견을 깨는 질문을 던집니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v19/05_base_value_comparison.jpg" alt="05_base_value_comparison" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(52, 211, 153, 0.2); color: #34d399;">5단계 [00:05]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">밑 $a$의 축소와 곡선의 하강</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  밑 $a$가 작아질수록 $y=a^x$ 곡선의 경사가 완만해지며 직선 $y=x$를 향해 점점 내려앉습니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v19/06_tangent_critical_point.jpg" alt="06_tangent_critical_point" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(251, 191, 36, 0.2); color: #fbbf24;">6단계 [00:06]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">임계 접점 $(e, e)$와 $a = e^{{1/e}}$</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  마침내 두 곡선이 직선 $y=x$와 정확히 한 점 $(e, e)$에서 접하는 역사적 순간이 포착됩니다!
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v19/07_intersection_count_cases.jpg" alt="07_intersection_count_cases" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(52, 211, 153, 0.2); color: #34d399;">7단계 [00:06]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">교점 2개 영역: $1 < a < e^{{1/e}}$</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  밑이 더 작아지면 곡선이 $y=x$ 아래로 파고들며 2개의 뚜렷한 교점($a=\sqrt{{2}} \\implies (2,2), (4,4)$)을 생성합니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v19/08_exam_key_takeaway.jpg" alt="08_exam_key_takeaway" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(52, 211, 153, 0.2); color: #34d399;">8단계 [00:07]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">수능 핵심 공식 정리</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  지수함수와 로그함수의 교점 개수 문제는 $a = e^{{1/e}} \\approx 1.4447$을 경계로 완벽히 분류됨을 정리합니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v19/09_final_summary_screen.jpg" alt="09_final_summary_screen" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(52, 211, 153, 0.2); color: #34d399;">9단계 [00:08]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">최종 마스터 요약</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  $a > e^{{1/e}} \\implies 0$개, $a = e^{{1/e}} \\implies 1$개, $1 < a < e^{{1/e}} \\implies 2$개 공식을 최종 각인합니다.
                </p>
              </div>
            </div>

          </div>
        </div>

        <!-- TAB 2: MATHEMATICAL DERIVATION -->
        <div id="tabL19_2" class="tab-pane-l19" style="display: none;">
          <h3 style="color: #34d399; margin-bottom: 18px;">📐 임계 밑 $a = e^{{1/e}}$의 미분학적 완전 유도</h3>
          <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 24px; line-height: 1.8; color: #cbd5e1;">
            <h4 style="color: #38bdf8; font-size: 1.1rem; margin-bottom: 12px;">1. 단조 증가 함수 역함수 교점의 대원칙</h4>
            <p>
              밑 $a > 1$일 때 $f(x) = a^x$는 실수 전체에서 <strong>엄격한 단조 증가 함수(Strictly Increasing Function)</strong>입니다.<br>
              단조 증가 함수 $f(x)$와 그 역함수 $f^{{-1}}(x)$의 교점 $(x, y)$는 <strong>반드시 직선 $y = x$ 위에만 존재</strong>합니다.<br>
              따라서 방정식 $a^x = \\log_a x$의 해를 구하는 것은 곧 방정식 <strong>$a^x = x$</strong>의 실근을 구하는 것과 완벽히 동치입니다.
            </p>

            <h4 style="color: #fbbf24; font-size: 1.1rem; margin: 20px 0 12px;">2. 접함 조건의 연립방정식 수립</h4>
            <p>
              곡선 $y = a^x$가 직선 $y = x$에 접하는 접점의 $x$좌표를 $t$라고 두면, 두 가지 필수 조건이 성립해야 합니다:
            </p>
            <ol style="margin-left: 20px; margin-bottom: 16px;">
              <li><strong>함숫값 일치 조건</strong>: $a^t = t \\quad \\cdots\\cdots$ [식 ①]</li>
              <li><strong>접선 기울기 일치 조건</strong>: $\\frac{{d}}{{dx}}(a^x)\\Big|_{{x=t}} = a^t \\ln a = 1 \\quad \\cdots\\cdots$ [식 ②]</li>
            </ol>

            <h4 style="color: #34d399; font-size: 1.1rem; margin: 20px 0 12px;">3. 접점 $(e, e)$ 및 임계 밑 $a$ 도출</h4>
            <p>
              [식 ①]의 $a^t = t$를 [식 ②]에 대입하면:
              $$t \\cdot \\ln a = 1 \\implies \\ln(a^t) = 1 \\implies a^t = e$$
              [식 ①]에 의해 $a^t = t$이므로:
              $$\\mathbf{{t = e \\approx 2.7182818...}}$$
              접점의 좌표는 놀랍게도 <strong>$(e, e)$</strong>로 결정됩니다!<br>
              이제 $a^e = e$이므로 양변에 $\\frac{{1}}{{e}}$제곱을 취하면:
              $$\\mathbf{{a = e^{{1/e}} = \\sqrt[e]{{e}} \\approx 1.44466786...}}$$
            </p>

            <h4 style="color: #c084fc; font-size: 1.1rem; margin: 20px 0 12px;">4. 감소함수 $0 < a < 1$ 킬러 반례 탐구</h4>
            <p>
              $a < 1$이면 $f(x)=a^x$는 단조 감소 함수가 됩니다. 이때는 $y=x$ 위에 교점이 항상 1개 존재하지만, 
              <strong>$a < e^{{-e}} \\approx 0.065988$</strong>이 되면 직선 $y=x$ 위의 점 외에 
              $y=x$에 대칭인 두 점 $(\\alpha, \\beta)$와 $(\\beta, \\alpha)$ (단, $\\alpha \\ne \\beta$)가 추가로 생겨 
              <strong>총 3개의 교점</strong>을 갖게 됩니다.
            </p>
          </div>
        </div>

        <!-- TAB 3: MANIM SCRIPT -->
        <div id="tabL19_3" class="tab-pane-l19" style="display: none;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
            <h3 style="color: #34d399; margin: 0;">🎬 3Blue1Brown 스타일 Manim 파이썬 애니메이션 코드</h3>
            <button class="btn btn-primary" onclick="copyManimCode19()" style="font-size: 0.82rem; padding: 6px 14px;">
              📋 파이썬 코드 복사
            </button>
          </div>
          <div class="code-container">
            <div class="code-header">
              <span>Python 3.12 · Manim Community v0.18+ (exp_log_inverse_intersection_manim.py)</span>
            </div>
            <pre id="manimPre19" style="max-height: 480px; overflow-y: auto;"><code class="language-python">{escaped_manim}</code></pre>
          </div>
        </div>

        <!-- TAB 4: ORIGINAL VIDEO -->
        <div id="tabL19_4" class="tab-pane-l19" style="display: none;">
          <h3 style="color: #34d399; margin-bottom: 18px;">🎥 너도 아는 수학 유튜브 원본 쇼츠 영상</h3>
          <div style="max-width: 480px; margin: 0 auto; background: #000; border-radius: 16px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.15); box-shadow: 0 10px 30px rgba(0,0,0,0.6);">
            <video controls style="width: 100%; display: block;" poster="./captures_v19/01_title_intro.jpg">
              <source src="lecture_video19.mp4" type="video/mp4">
              브라우저가 HTML5 비디오를 지원하지 않습니다.
            </video>
            <div style="padding: 16px; background: rgba(15, 23, 42, 0.95); text-align: center;">
              <div style="font-weight: bold; color: #f1f5f9; margin-bottom: 6px;">[수1/미적분] 지수함수와 로그함수 (역함수 교점)</div>
              <div style="font-size: 0.82rem; color: #94a3b8; margin-bottom: 12px;">채널: 너도 아는 수학 · 8초 숏폼 핵심 특강</div>
              <a href="https://youtube.com/shorts/hTNIh08SkLA?si=iC67jRzYPWcehJ36" target="_blank" rel="noopener noreferrer" 
                 class="btn btn-secondary" style="font-size: 0.82rem; padding: 6px 14px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
                <span>▶ YouTube 원본 링크 열기</span>
              </a>
            </div>
          </div>
        </div>

        <!-- TAB 5: CSAT KILLER TIPS -->
        <div id="tabL19_5" class="tab-pane-l19" style="display: none;">
          <h3 style="color: #34d399; margin-bottom: 18px;">📝 수능/모의고사 실전 기출 진위판정(ㄱ, ㄴ, ㄷ) 단골 함정</h3>
          <div style="display: flex; flex-direction: column; gap: 16px;">
            <div style="background: rgba(15, 23, 42, 0.6); border-left: 4px solid #f43f5e; padding: 18px; border-radius: 0 10px 10px 0;">
              <h4 style="color: #f43f5e; margin-bottom: 6px;">🚨 함정 1: "지수함수와 로그함수의 교점은 많아야 1개이다?"</h4>
              <p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                <strong>오답률 70% 단골!</strong> 밑이 $1 < a < e^{{1/e}} \\approx 1.4447$이면 <strong>서로 다른 2개의 교점</strong>이 생깁니다. 특히 $a = \\sqrt{{2}}$일 때 교점 $(2, 2)$와 $(4, 4)$는 수능 객관식 보기에 단골로 등장하는 대표 정수 좌표입니다.
              </p>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border-left: 4px solid #fbbf24; padding: 18px; border-radius: 0 10px 10px 0;">
              <h4 style="color: #fbbf24; margin-bottom: 6px;">⚡ 함정 2: "역함수와의 교점은 반드시 $y=x$ 위에만 존재한다?"</h4>
              <p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                <strong>조건을 확인하세요!</strong> 밑 $a > 1$인 '증가함수'일 때만 참입니다. 만약 $0 < a < 1$인 '감소함수'이고 $a < e^{{-e}}$이면, $y=x$ 바깥에서 $(x_1, y_1)$과 $(y_1, x_1)$ 형태로 <strong>대칭인 교점 쌍 2개가 추가되어 총 3개의 교점</strong>이 발생합니다.
              </p>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border-left: 4px solid #34d399; padding: 18px; border-radius: 0 10px 10px 0;">
              <h4 style="color: #34d399; margin-bottom: 6px;">💡 실전 풀이 공식: 방정식 $a^x = x$ 판별법</h4>
              <p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                함수 $h(x) = a^x - x$로 놓으면 $h'(x) = a^x \\ln a - 1 = 0$에서 극솟값 $x = -\\frac{{\\ln(\\ln a)}}{{\\ln a}}$가 발생합니다. 극솟값이 0보다 작으면 실근 2개, 0이면 1개(접함), 0보다 크면 0개가 됩니다.
              </p>
            </div>
          </div>
        </div>

      </div>
    </div>
'''

    # Insert lecture19_html immediately before lecture18View
    if '<div id="lecture19View">' not in html:
        target_lec18 = '<div id="lecture18View"'
        html = html.replace(target_lec18, lecture19_html + '\n    ' + target_lec18, 1)
        print("Inserted lecture19View into HTML.")

    # 3. Update JavaScript: LECTURE_META, setLecture, and Lecture 19 code
    meta_insert = "    const LECTURE_META = {\n      19: { subj: 'math1',   subjName: '수학 I · 지수·로그함수', title: '제19강 · 지수·로그함수와 역함수 교점' },"
    html = html.replace("    const LECTURE_META = {", meta_insert, 1)

    # Update loop ranges in selectSubject and setLecture (18 -> 19)
    html = html.replace('for (let i = 1; i <= 18; i++)', 'for (let i = 1; i <= 19; i++)')

    # Update setLecture branching
    old_set_lec_top = "if (num === 18) setTimeout(renderL18, 50);"
    new_set_lec_top = "if (num === 19) setTimeout(renderL19, 50);\n      else if (num === 18) setTimeout(renderL18, 50);"
    html = html.replace(old_set_lec_top, new_set_lec_top, 1)

    # 4. Insert Lecture 19 JS Simulator & Tabs logic
    js_l19 = '''
    // ==============================================================
    // JAVASCRIPT FOR LECTURE 19 (EXPONENTIAL & LOGARITHMIC INTERSECTION)
    // ==============================================================
    let currentA19 = 1.44466786; // e^(1/e)
    let animRunning19 = false;
    let animTimer19 = null;
    let animDirA19 = 1;

    function applyPreset19(val) {
      currentA19 = parseFloat(val);
      const slider = document.getElementById("sliderA19");
      if (slider) slider.value = currentA19;
      updateL19();
    }

    function updateFromSliders19() {
      const slider = document.getElementById("sliderA19");
      if (slider) currentA19 = parseFloat(slider.value);
      updateL19();
    }

    function toggleAnimation19() {
      animRunning19 = !animRunning19;
      const btn = document.getElementById("btnAnim19");
      if (animRunning19) {
        if (btn) {
          btn.innerText = "⏸ 애니메이션 일시정지";
          btn.style.background = "#fb7185";
          btn.style.color = "#fff";
        }
        runAnimLoop19();
      } else {
        if (btn) {
          btn.innerText = "▶ 밑 a 임계 스위프 애니메이션";
          btn.style.background = "#34d399";
          btn.style.color = "#0f172a";
        }
        if (animTimer19) {
          cancelAnimationFrame(animTimer19);
          animTimer19 = null;
        }
      }
    }

    function runAnimLoop19() {
      if (!animRunning19) return;

      currentA19 += animDirA19 * 0.006;
      if (currentA19 >= 2.2) {
        currentA19 = 2.2;
        animDirA19 = -1;
      } else if (currentA19 <= 1.15) {
        currentA19 = 1.15;
        animDirA19 = 1;
      }

      const slider = document.getElementById("sliderA19");
      if (slider) slider.value = currentA19.toFixed(4);

      updateL19();
      animTimer19 = requestAnimationFrame(runAnimLoop19);
    }

    function updateL19() {
      const a = currentA19;
      const elA = document.getElementById("valA19");
      if (elA) elA.innerText = a.toFixed(4);

      const dispFormula = document.getElementById("dispFormula19");
      if (dispFormula) {
        dispFormula.innerText = `y = ${a.toFixed(3)}^x  &  y = log_{${a.toFixed(3)}}(x)`;
      }

      const statStatus = document.getElementById("statStatus19");
      const statCoords = document.getElementById("statCoords19");

      const critA = Math.exp(1 / Math.E); // ~1.444668
      const diff = a - critA;

      let intersections = [];

      if (a > 1.0) {
        // Intersections with y = x: solve a^x = x
        if (Math.abs(diff) < 0.005) {
          if (statStatus) {
            statStatus.innerHTML = '<span style="color:#fbbf24;">🌟 1개 접점 (접함! a = e^(1/e))</span>';
          }
          intersections = [{ x: Math.E, y: Math.E }];
        } else if (a < critA) {
          if (statStatus) {
            statStatus.innerHTML = '<span style="color:#34d399;">🟢 서로 다른 2개 교점 (y = x 관통)</span>';
          }
          // Numerically solve a^x = x for two roots: x1 in (1, e) and x2 in (e, 15)
          const f = (x) => Math.pow(a, x) - x;
          const r1 = bisectionSolve(f, 0.1, Math.E);
          const r2 = bisectionSolve(f, Math.E, 14.0);
          if (r1 !== null) intersections.push({ x: r1, y: r1 });
          if (r2 !== null) intersections.push({ x: r2, y: r2 });
        } else {
          if (statStatus) {
            statStatus.innerHTML = '<span style="color:#f43f5e;">🔴 교점 0개 (만나지 않음: a^x > x)</span>';
          }
        }
      } else {
        // a < 1.0 decreasing function
        const f = (x) => Math.pow(a, x) - x;
        const r = bisectionSolve(f, 0.01, 5.0);
        if (r !== null) intersections.push({ x: r, y: r });
        if (a < Math.exp(-Math.E)) {
          if (statStatus) {
            statStatus.innerHTML = '<span style="color:#c084fc;">🚨 교점 3개! (a < e^(-e) 킬러 반례)</span>';
          }
        } else {
          if (statStatus) {
            statStatus.innerHTML = '<span style="color:#38bdf8;">🔵 1개 교점 (y = x 위)</span>';
          }
        }
      }

      if (statCoords) {
        if (intersections.length === 0) {
          statCoords.innerText = "교점 없음 (공집합 ∅)";
        } else {
          statCoords.innerText = intersections.map(p => `(${p.x.toFixed(2)}, ${p.y.toFixed(2)})`).join(" , ");
        }
      }

      drawCanvasL19(intersections);
    }

    function bisectionSolve(f, low, high) {
      let fLow = f(low);
      let fHigh = f(high);
      if (isNaN(fLow) || isNaN(fHigh)) return null;
      if (fLow * fHigh > 0) return null;
      for (let i = 0; i < 40; i++) {
        let mid = (low + high) / 2;
        let fMid = f(mid);
        if (Math.abs(fMid) < 1e-6) return mid;
        if (fLow * fMid < 0) {
          high = mid;
          fHigh = fMid;
        } else {
          low = mid;
          fLow = fMid;
        }
      }
      return (low + high) / 2;
    }

    function drawCanvasL19(intersections) {
      const canvas = document.getElementById("canvasL19");
      if (!canvas) return;
      const ctx = canvas.getContext("2d");
      const W = canvas.width;
      const H = canvas.height;

      ctx.clearRect(0, 0, W, H);

      const xMin = -1.5, xMax = 6.5;
      const yMin = -1.5, yMax = 6.5;

      function toScreenX(x) {
        return (x - xMin) / (xMax - xMin) * W;
      }
      function toScreenY(y) {
        return H - (y - yMin) / (yMax - yMin) * H;
      }

      const origX = toScreenX(0);
      const origY = toScreenY(0);

      // 1. Grid
      ctx.lineWidth = 1;
      ctx.strokeStyle = "rgba(255, 255, 255, 0.06)";
      for (let x = Math.ceil(xMin); x <= Math.floor(xMax); x++) {
        const sx = toScreenX(x);
        ctx.beginPath();
        ctx.moveTo(sx, 0);
        ctx.lineTo(sx, H);
        ctx.stroke();
      }
      for (let y = Math.ceil(yMin); y <= Math.floor(yMax); y++) {
        const sy = toScreenY(y);
        ctx.beginPath();
        ctx.moveTo(0, sy);
        ctx.lineTo(W, sy);
        ctx.stroke();
      }

      // 2. Axes
      ctx.strokeStyle = "rgba(148, 163, 184, 0.4)";
      ctx.lineWidth = 1.8;
      // X Axis
      ctx.beginPath();
      ctx.moveTo(0, origY);
      ctx.lineTo(W, origY);
      ctx.stroke();
      // Y Axis
      ctx.beginPath();
      ctx.moveTo(origX, 0);
      ctx.lineTo(origX, H);
      ctx.stroke();

      // Axis Labels
      ctx.fillStyle = "#94a3b8";
      ctx.font = "bold 12px 'Consolas', monospace";
      ctx.fillText("x", W - 18, origY + 16);
      ctx.fillText("y", origX + 10, 18);
      ctx.fillText("O", origX - 16, origY + 16);

      // Grid Numbers
      for (let i = 1; i <= 6; i++) {
        ctx.fillText(i.toString(), toScreenX(i) - 4, origY + 16);
        ctx.fillText(i.toString(), origX - 18, toScreenY(i) + 4);
      }

      // 3. Line y = x
      const chkLineYX = document.getElementById("chkLineYX19") ? document.getElementById("chkLineYX19").checked : true;
      if (chkLineYX) {
        ctx.strokeStyle = "#facc15";
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(toScreenX(xMin), toScreenY(xMin));
        ctx.lineTo(toScreenX(xMax), toScreenY(xMax));
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "#facc15";
        ctx.font = "bold 12px 'Consolas', monospace";
        ctx.fillText("y = x", toScreenX(5.6), toScreenY(5.8));
      }

      // 4. Critical Point (e, e)
      const chkCrit = document.getElementById("chkCritPoint19") ? document.getElementById("chkCritPoint19").checked : true;
      if (chkCrit) {
        const eX = toScreenX(Math.E);
        const eY = toScreenY(Math.E);

        ctx.strokeStyle = "rgba(251, 191, 36, 0.35)";
        ctx.lineWidth = 1.2;
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(eX, origY);
        ctx.lineTo(eX, eY);
        ctx.lineTo(origX, eY);
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "rgba(251, 191, 36, 0.4)";
        ctx.beginPath();
        ctx.arc(eX, eY, 9, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = "#fbbf24";
        ctx.beginPath();
        ctx.arc(eX, eY, 4, 0, Math.PI * 2);
        ctx.fill();

        ctx.font = "bold 11px 'Consolas', monospace";
        ctx.fillText("임계점 (e, e)", eX - 70, eY - 10);
      }

      const a = currentA19;

      // 5. Exponential Curve: y = a^x
      ctx.lineWidth = 3.2;
      ctx.strokeStyle = "#38bdf8";
      ctx.beginPath();
      let startedExp = false;
      for (let x = xMin; x <= xMax; x += 0.02) {
        const y = Math.pow(a, x);
        if (!isNaN(y) && isFinite(y) && y >= yMin - 5 && y <= yMax + 5) {
          const sx = toScreenX(x);
          const sy = toScreenY(y);
          if (!startedExp) {
            ctx.moveTo(sx, sy);
            startedExp = true;
          } else {
            ctx.lineTo(sx, sy);
          }
        }
      }
      ctx.stroke();

      // Label y = a^x
      const labelExpX = Math.min(2.5, xMax - 1.0);
      const labelExpY = Math.pow(a, labelExpX);
      if (labelExpY <= yMax) {
        ctx.fillStyle = "#38bdf8";
        ctx.font = "bold 13px 'Consolas', monospace";
        ctx.fillText(`y = ${a.toFixed(2)}^x`, toScreenX(labelExpX) + 8, toScreenY(labelExpY) - 10);
      }

      // 6. Logarithmic Curve: y = log_a(x)
      const chkLog = document.getElementById("chkShowLog19") ? document.getElementById("chkShowLog19").checked : true;
      if (chkLog) {
        ctx.lineWidth = 3.2;
        ctx.strokeStyle = "#fb7185";
        ctx.beginPath();
        let startedLog = false;
        const lnA = Math.log(a);
        for (let x = 0.02; x <= xMax; x += 0.02) {
          const y = Math.log(x) / lnA;
          if (!isNaN(y) && isFinite(y) && y >= yMin - 5 && y <= yMax + 5) {
            const sx = toScreenX(x);
            const sy = toScreenY(y);
            if (!startedLog) {
              ctx.moveTo(sx, sy);
              startedLog = true;
            } else {
              ctx.lineTo(sx, sy);
            }
          }
        }
        ctx.stroke();

        // Label y = log_a(x)
        const labelLogX = 4.5;
        const labelLogY = Math.log(labelLogX) / lnA;
        if (labelLogY >= yMin && labelLogY <= yMax) {
          ctx.fillStyle = "#fb7185";
          ctx.font = "bold 13px 'Consolas', monospace";
          ctx.fillText(`y = log_{${a.toFixed(2)}}(x)`, toScreenX(labelLogX) - 30, toScreenY(labelLogY) + 20);
        }
      }

      // 7. Highlight Intersections
      const chkInter = document.getElementById("chkIntersections19") ? document.getElementById("chkIntersections19").checked : true;
      if (chkInter && intersections && intersections.length > 0) {
        intersections.forEach((pt, idx) => {
          const px = toScreenX(pt.x);
          const py = toScreenY(pt.y);

          // Glow Halo
          const grad = ctx.createRadialGradient(px, py, 2, px, py, 14);
          grad.addColorStop(0, "rgba(52, 211, 153, 0.9)");
          grad.addColorStop(1, "rgba(52, 211, 153, 0)");
          ctx.fillStyle = grad;
          ctx.beginPath();
          ctx.arc(px, py, 14, 0, Math.PI * 2);
          ctx.fill();

          // Dot
          ctx.fillStyle = "#34d399";
          ctx.beginPath();
          ctx.arc(px, py, 6, 0, Math.PI * 2);
          ctx.fill();
          ctx.strokeStyle = "#ffffff";
          ctx.lineWidth = 2;
          ctx.stroke();

          // Label
          ctx.fillStyle = "#ffffff";
          ctx.font = "bold 12px 'Consolas', monospace";
          ctx.fillText(`교점 ${idx + 1} (${pt.x.toFixed(2)}, ${pt.y.toFixed(2)})`, px + 12, py - 8);
        });
      }
    }

    function switchL19Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL19_${i}`);
        const content = document.getElementById(`tabL19_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture19View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode19() {
      const codeEl = document.querySelector("#manimPre19 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL19() {
      updateL19();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture19View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }
'''

    # Insert JS before window.addEventListener('load')
    target_window_load = "window.addEventListener('load', () => {"
    html = html.replace(target_window_load, js_l19 + '\n    ' + target_window_load, 1)

    # In window.addEventListener('load'), setLecture(19) and renderL19()
    html = html.replace("setLecture(18);\n      renderL18();", "setLecture(19);\n      renderL19();")
    html = html.replace("setLecture(18);", "setLecture(19);")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done! Successfully injected Lecture 19 into index.html.")

if __name__ == '__main__':
    main()
