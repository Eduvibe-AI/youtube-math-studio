# -*- coding: utf-8 -*-
"""
Script to build and inject Lecture 20 into index.html
Lecture: 지수, 로그함수에서 기울기 활용법-근육의 공식
Channel: 근육의 공식
YouTube Video: https://youtu.be/0cYeWjClTV4
"""

import os
import re

def main():
    html_path = 'index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read manim code for tab
    with open('exp_log_slope_symmetry_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()

    # 1. Update Navigation Bar Counts & Titles
    # 'all' badge 19 -> 20
    html = re.sub(
        r'(<button type="button" class="subj-tab(?: active)?" data-subject="all"[^>]*>[\s\S]*?<span class="tab-badge">)19(</span>)',
        r'\g<1>20\g<2>',
        html
    )

    # 'math1' badge 4 -> 5
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math1"[^>]*>[\s\S]*?<span class="tab-badge">)4(</span>)',
        r'\g<1>5\g<2>',
        html
    )

    # captured summary link
    html = html.replace('사진 1~19 요약집', '사진 1~20 요약집')
    html = html.replace('사진 1~19 핵심 전용 페이지', '사진 1~20 핵심 전용 페이지')

    # Remove active from btnLec19
    html = html.replace('id="btnLec19" onclick="setLecture(19)" class="lecture-btn active"', 'id="btnLec19" onclick="setLecture(19)" class="lecture-btn"')
    html = html.replace('class="lecture-btn active" id="btnLec19"', 'class="lecture-btn" id="btnLec19"')

    # In group-math1, add btnLec20
    if 'id="btnLec20"' not in html:
        target_group1_grid = '<div class="lecture-btn-grid">\n            <button type="button" class="lecture-btn"'
        if 'id="btnLec19"' in html:
            # Insert before btnLec19
            old_btn19_block = '<button type="button" class="lecture-btn" id="btnLec19" onclick="setLecture(19)" data-subj="math1">'
            new_btn20_block = '''<button type="button" class="lecture-btn active" id="btnLec20" onclick="setLecture(20)" data-subj="math1">
              <span class="lec-num">20</span>
              <span class="badge-pill-sm">⚡ 수능</span>
              <span class="lec-title">지수·로그함수 기울기 $m=-1$ 활용법</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec19" onclick="setLecture(19)" data-subj="math1">'''
            html = html.replace(old_btn19_block, new_btn20_block, 1)
            print("Inserted btnLec20 into group-math1.")

    # Update Status banner default
    html = re.sub(
        r'<span class="status-subj" id="statusSubjText">[^<]+</span>\s*<span class="status-sep">/</span>\s*<span class="status-title" id="statusTitleText">[^<]+</span>',
        r'<span class="status-subj" id="statusSubjText">수학 I · 지수·로그함수</span>\n        <span class="status-sep">/</span>\n        <span class="status-title" id="statusTitleText">제20강 · 지수·로그함수 기울기 $m=-1$ 활용법</span>',
        html
    )

    # Set lecture19View to display: none
    html = html.replace('<div id="lecture19View">', '<div id="lecture19View" style="display: none;">')

    # 2. Build Lecture 20 View
    escaped_manim = (manim_code
                     .replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;'))

    lecture20_html = f'''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 20 (EXPONENTIAL & LOG SLOPE & SYMMETRY METHOD) -->
    <!-- ============================================================== -->
    <div id="lecture20View">
      <header>
        <div class="badge-pill" style="border-color: rgba(56, 189, 248, 0.4); color: #38bdf8; box-shadow: 0 0 20px rgba(56, 189, 248, 0.3);">
          ⚡ 제20강 · 근육의 공식 (수능 수학 I 킬러 실전 비기)
        </div>
        <h1 style="background: linear-gradient(135deg, #38bdf8 0%, #a855f7 50%, #facc15 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          지수·로그함수에서 기울기 활용법과 평행이동·대칭성 (기울기 $m=-1$의 마법)
        </h1>
        <p class="subtitle" style="max-width: 900px; margin: 0 auto; line-height: 1.7; color: #cbd5e1;">
          "지수함수와 다항함수는 대수적으로 연립되지 않는다!"<br>
          수능 평가원이 킬러 문항에서 요구하는 3대 본질적 해결 열쇠:<br>
          <strong>평행이동 벡터와 기울기 일치 · $A \\cdot a^x = a^{{x+\\log_a A}}$ 평행이동 치환 · 기울기 $m=-1$과 직각이등변 $1:1:\\sqrt{{2}}$ 대칭성</strong>을 실시간 인터랙티브 캔버스로 완벽 분석합니다.
        </p>
      </header>

      <!-- TOP SUMMARY BANNER -->
      <div style="background: linear-gradient(135deg, rgba(56, 189, 248, 0.15), rgba(168, 85, 247, 0.12), rgba(15, 23, 42, 0.95)); border: 2px solid rgba(56, 189, 248, 0.4); border-radius: 20px; padding: 26px; margin-bottom: 35px; box-shadow: 0 12px 36px rgba(0, 0, 0, 0.5);">
        <div style="font-size: 0.95rem; font-weight: 700; color: #38bdf8; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px; text-align: center;">
          ⭐ 지수·로그함수 수능 킬러 정복 3대 황금 원리 매트릭스
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; text-align: center; margin-top: 15px;">
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(56, 189, 248, 0.3);">
            <div style="color: #38bdf8; font-weight: bold; font-size: 0.85rem;">1. 평행이동 벡터와 기울기</div>
            <div style="color: #fff; font-size: 1.05rem; font-family: monospace; margin-top: 3px;">$m = \\frac{{\\Delta y}}{{\\Delta x}}$</div>
            <div style="color: #94a3b8; font-size: 0.75rem; margin-top: 2px;">대응점 간 직선 거리 $\\sqrt{{\\Delta x^2 + \\Delta y^2}}$ 고정</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(250, 204, 21, 0.3);">
            <div style="color: #facc15; font-weight: bold; font-size: 0.85rem;">2. 밑 변환과 평행이동</div>
            <div style="color: #fff; font-size: 1.05rem; font-family: monospace; margin-top: 3px;">$3 \\cdot 2^x = 2^{{x + \\log_2 3}}$</div>
            <div style="color: #94a3b8; font-size: 0.75rem; margin-top: 2px;">앞자리 상수는 $x$축 평행이동으로 치환</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(236, 72, 153, 0.3);">
            <div style="color: #ec4899; font-weight: bold; font-size: 0.85rem;">3. 기울기 $m = -1$ 직각이등변</div>
            <div style="color: #fff; font-size: 1.05rem; font-family: monospace; margin-top: 3px;">$1 : 1 : \\sqrt{{2}}$</div>
            <div style="color: #94a3b8; font-size: 0.75rem; margin-top: 2px;">$\\overline{{AB}} = 2\\sqrt{{2}} \\implies \\Delta x = 2, \\Delta y = 2$</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 12px; border-radius: 10px; border: 1px solid rgba(168, 85, 247, 0.3);">
            <div style="color: #c084fc; font-weight: bold; font-size: 0.85rem;">4. 역함수 대칭 수직성</div>
            <div style="color: #fff; font-size: 1.05rem; font-family: monospace; margin-top: 3px;">$y = -x + k \\perp y = x$</div>
            <div style="color: #94a3b8; font-size: 0.75rem; margin-top: 2px;">$(\\alpha, \\beta) \\leftrightarrow (\\beta, \\alpha)$ 대칭성 즉각 발동</div>
          </div>
        </div>
      </div>

      <!-- MAIN INTERACTIVE LAB: EXPONENTIAL & LOGARITHM SLOPE LAB -->
      <div class="card" style="margin-bottom: 40px; border-color: rgba(56, 189, 248, 0.4); box-shadow: 0 10px 30px rgba(56, 189, 248, 0.15);">
        <h2 style="color: #38bdf8; display: flex; align-items: center; gap: 10px;">
          <span>📐</span> 수능 22학년도 9월 21번 &amp; 기울기 $m=-1$ 대칭성 동적 시뮬레이터
        </h2>
        <p style="color: #94a3b8; line-height: 1.6; margin-bottom: 20px;">
          직선 $y = -x + k$의 $y$절편 $k$와 지수·로그함수의 평행이동 매개변수를 슬라이더로 조작하며, 직각이등변삼각형 $1:1:\\sqrt{{2}}$에 의한 선분 $\\overline{{AB}}$ 길이 및 삼각형 $\\triangle ABC$의 넓이 $S$ 변화를 실시간으로 탐구해보세요.
        </p>

        <!-- PRESET BUTTONS -->
        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px;">
          <span style="font-size: 0.85rem; color: #94a3b8; align-self: center; margin-right: 4px;">🎯 프리셋:</span>
          <button class="btn btn-secondary" onclick="applyPreset20(2.0, 1.0, 4.0)" style="font-size: 0.8rem; padding: 6px 12px; border-color: #38bdf8; color: #38bdf8;">
            ⭐ 22년 9월 21번 표준형: a=2, p=1, k=4 (AB=2√2, S=3.5)
          </button>
          <button class="btn btn-secondary" onclick="applyPreset20(2.0, 1.0, 5.0)" style="font-size: 0.8rem; padding: 6px 12px;">
            절편 확장: k=5 (교점 간격 확대)
          </button>
          <button class="btn btn-secondary" onclick="applyPreset20(3.0, 1.0, 4.0)" style="font-size: 0.8rem; padding: 6px 12px;">
            밑 a=3 변경 (더 가파른 지수곡선)
          </button>
          <button class="btn btn-secondary" onclick="applyPreset20(2.0, 0.0, 3.0)" style="font-size: 0.8rem; padding: 6px 12px;">
            원형 역함수 대칭: y=2^x &amp; y=log_2(x)
          </button>
          <button class="btn btn-primary" id="btnAnim20" onclick="toggleAnimation20()" style="font-size: 0.8rem; padding: 6px 14px; background: #38bdf8; color: #0f172a; font-weight: bold;">
            ▶ 직선 y = -x + k 동적 스위프 애니메이션
          </button>
        </div>

        <div style="display: grid; grid-template-columns: 320px 1fr; gap: 24px; align-items: start;">
          <!-- CONTROLS COLUMN -->
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 18px;">
            <!-- Formula Display -->
            <div style="background: #030712; border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 8px; padding: 12px; margin-bottom: 16px; text-align: center;">
              <div style="color: #94a3b8; font-size: 0.75rem; letter-spacing: 1px;">현재 함수 및 직선</div>
              <div id="dispFormula20" style="font-size: 1.05rem; font-weight: bold; color: #38bdf8; margin: 4px 0; font-family: monospace;">
                y = 2^{{x-1}}, \\; y = \\log_2(x-1), \\; y = -x + 4
              </div>
            </div>

            <!-- k Slider (Line Intercept) -->
            <div style="margin-bottom: 16px;">
              <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
                <span style="color: #fb7185; font-weight: bold;">직선 y = -x + k 절편 k:</span>
                <span id="valK20" style="color: #fb7185; font-family: monospace; font-weight: bold;">4.0</span>
              </div>
              <input type="range" id="sliderK20" min="2.0" max="6.0" step="0.05" value="4.0"
                     oninput="updateFromSliders20()" style="width: 100%; accent-color: #fb7185;">
              <div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #64748b;">
                <span>k = 2.0</span>
                <span style="color: #fb7185; font-weight: bold;">k = 4.0 (수능기출)</span>
                <span>k = 6.0</span>
              </div>
            </div>

            <!-- a Slider (Base) -->
            <div style="margin-bottom: 16px;">
              <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
                <span style="color: #38bdf8; font-weight: bold;">밑 a (Base):</span>
                <span id="valA20" style="color: #38bdf8; font-family: monospace; font-weight: bold;">2.0</span>
              </div>
              <input type="range" id="sliderA20" min="1.3" max="4.0" step="0.1" value="2.0"
                     oninput="updateFromSliders20()" style="width: 100%; accent-color: #38bdf8;">
              <div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #64748b;">
                <span>1.3</span>
                <span>2.0 (기출)</span>
                <span>4.0</span>
              </div>
            </div>

            <!-- p Slider (Shift) -->
            <div style="margin-bottom: 16px;">
              <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
                <span style="color: #a855f7; font-weight: bold;">평행이동 p (x - p):</span>
                <span id="valP20" style="color: #a855f7; font-family: monospace; font-weight: bold;">1.0</span>
              </div>
              <input type="range" id="sliderP20" min="0.0" max="2.5" step="0.1" value="1.0"
                     oninput="updateFromSliders20()" style="width: 100%; accent-color: #a855f7;">
              <div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #64748b;">
                <span>0.0 (원형 대칭)</span>
                <span>1.0 (기출)</span>
                <span>2.5</span>
              </div>
            </div>

            <!-- Visual Guides Checkboxes -->
            <div style="border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 12px; margin-top: 12px;">
              <label style="display: flex; align-items: center; gap: 8px; font-size: 0.82rem; color: #cbd5e1; margin-bottom: 8px; cursor: pointer;">
                <input type="checkbox" id="chkLineYX20" onchange="updateL20()" checked>
                <span>대칭축 직선 $y = x$ 표시 (노란 점선)</span>
              </label>
              <label style="display: flex; align-items: center; gap: 8px; font-size: 0.82rem; color: #cbd5e1; margin-bottom: 8px; cursor: pointer;">
                <input type="checkbox" id="chkTriangleGuide20" onchange="updateL20()" checked>
                <span>직각이등변삼각형 $1:1:\\sqrt{{2}}$ 가이드 표시</span>
              </label>
              <label style="display: flex; align-items: center; gap: 8px; font-size: 0.82rem; color: #cbd5e1; cursor: pointer;">
                <input type="checkbox" id="chkShadedTri20" onchange="updateL20()" checked>
                <span>삼각형 $\\triangle ABC$ 음영 및 넓이 계산 표시</span>
              </label>
            </div>

            <!-- Real-time Status Badges -->
            <div style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px;">
              <div style="background: rgba(2, 6, 23, 0.8); padding: 10px; border-radius: 8px; border-left: 3px solid #fb7185;">
                <div style="font-size: 0.72rem; color: #94a3b8;">교점 A, B 좌표</div>
                <div id="statPoints20" style="font-size: 0.85rem; font-family: monospace; color: #fb7185; margin-top: 2px;">
                  A(1.00, 3.00), B(3.00, 1.00)
                </div>
              </div>
              <div style="background: rgba(2, 6, 23, 0.8); padding: 10px; border-radius: 8px; border-left: 3px solid #facc15;">
                <div style="font-size: 0.72rem; color: #94a3b8;">선분 AB 길이 &amp; 직각이등변 분해</div>
                <div id="statLength20" style="font-size: 0.85rem; font-family: monospace; color: #facc15; margin-top: 2px;">
                  L = 2.83 (2√2), Δx = 2.00, Δy = 2.00
                </div>
              </div>
              <div style="background: rgba(2, 6, 23, 0.8); padding: 10px; border-radius: 8px; border-left: 3px solid #34d399;">
                <div style="font-size: 0.72rem; color: #94a3b8;">삼각형 ABC 넓이 S &amp; 50S</div>
                <div id="statArea20" style="font-size: 0.85rem; font-family: monospace; color: #34d399; margin-top: 2px;">
                  S = 3.50 (7/2) ➔ 50 × S = 175
                </div>
              </div>
            </div>
          </div>

          <!-- CANVAS & READOUT COLUMN -->
          <div>
            <div style="position: relative; background: #030712; border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 12px; overflow: hidden; box-shadow: inset 0 0 40px rgba(0,0,0,0.8);">
              <canvas id="canvasL20" width="760" height="520" style="width: 100%; height: auto; display: block;"></canvas>

              <div style="position: absolute; top: 12px; right: 12px; background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(8px); border: 1px solid rgba(56, 189, 248, 0.4); border-radius: 8px; padding: 8px 14px; font-size: 0.75rem; color: #e2e8f0; pointer-events: none;">
                <span style="color: #38bdf8;">■ y = a^(x-p)</span> &nbsp;|&nbsp;
                <span style="color: #a855f7;">■ y = log_a(x-p)</span> &nbsp;|&nbsp;
                <span style="color: #fb7185;">■ y = -x + k</span> &nbsp;|&nbsp;
                <span style="color: #facc15;">-- y = x</span>
              </div>
            </div>

            <!-- Mathematical Insight Footer -->
            <div style="margin-top: 14px; padding: 14px 18px; background: rgba(56, 189, 248, 0.08); border-radius: 10px; border: 1px solid rgba(56, 189, 248, 0.2); font-size: 0.85rem; color: #cbd5e1; line-height: 1.6;">
              💡 <strong>핵심 기하학적 통찰</strong>: 기울기가 $-1$인 직선 $y = -x + k$는 대칭축 $y=x$와 정확히 수직을 이루므로, 두 교점 $A$와 $B$는 $y=x$ 대칭축에 대하여 수직 반사된 <strong>완벽한 대칭점 쌍</strong>을 형성합니다. 선분 길이 $L = 2\\sqrt{{2}}$가 주어지는 순간 $1:1:\\sqrt{{2}}$ 직각이등변삼각형에 의해 $x$와 $y$의 좌표 차이가 각각 <strong>$2$</strong>로 즉시 확정되어 연립방정식 없이 암산 수준으로 풀립니다!
            </div>
          </div>
        </div>
      </div>

      <!-- TABS SECTION -->
      <div class="card" style="margin-top: 30px;">
        <div style="display: flex; gap: 8px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 12px; margin-bottom: 24px; overflow-x: auto;">
          <button class="btn btn-secondary active" id="tabBtnL20_1" onclick="switchL20Tab(1)">📸 10단계 영상 캡처 타임라인</button>
          <button class="btn btn-secondary" id="tabBtnL20_2" onclick="switchL20Tab(2)">📐 22년 9월 21번 3초 공식 완전 유도</button>
          <button class="btn btn-secondary" id="tabBtnL20_3" onclick="switchL20Tab(3)">🎬 3Blue1Brown Manim 코드</button>
          <button class="btn btn-secondary" id="tabBtnL20_4" onclick="switchL20Tab(4)">🎥 원본 영상 (근육의 공식)</button>
          <button class="btn btn-secondary" id="tabBtnL20_5" onclick="switchL20Tab(5)">📝 수능 3대 기출 비교 분석</button>
        </div>

        <!-- TAB 1: 10-STEP CAPTURE TIMELINE -->
        <div id="tabL20_1" class="tab-pane-l20">
          <h3 style="color: #38bdf8; margin-bottom: 18px;">📸 근육의 공식 타임라인별 핵심 판서 캡처</h3>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v20/01_transcendental_equation_limit.jpg" alt="01" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8;">1단계 [00:10]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">연립 불가능한 초월방정식</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  $2^x = \\frac{{1}}{{2}}x + 3$처럼 지수함수와 다항식은 대수적 연립이 불가능함을 제시합니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v20/02_translation_formula_setup.jpg" alt="02" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8;">2단계 [00:45]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">평행이동 관계 파악</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  $y=2^x$와 $y=2^{{x-2}}-1$ 곡선 사이의 $x$축 $+2$, $y$축 $-1$ 이동을 확인합니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v20/03_slope_vector_alignment.jpg" alt="03" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8;">3단계 [01:18]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">평행이동 벡터와 직선 기울기</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  이동 벡터 $(\\Delta x, \\Delta y) = (2, -1)$로부터 직선의 기울기 $m = -\\frac{{1}}{{2}}$이 결정됩니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v20/04_coefficient_log_translation.jpg" alt="04" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(250, 204, 21, 0.2); color: #facc15;">4단계 [01:55]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">계수 $3$의 비밀 (로그 평행이동)</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  $y = 3 \\cdot 2^x = 2^{{x + \\log_2 3}}$으로 변형되어 $x$축 방향 $-\\log_2 3$ 평행이동임을 밝힙니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v20/05_symmetry_axis_y_equals_x.jpg" alt="05" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8;">5단계 [02:30]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">대칭축 $y = x$의 등장</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  역함수의 본질인 직선 $y = x$를 기준으로 대칭 관계를 시각화합니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v20/06_slope_minus_one_symmetry.jpg" alt="06" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(236, 72, 153, 0.2); color: #ec4899;">6단계 [02:52]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">기울기 $m = -1$ 직선과의 수직성</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  기울기 $-1$인 직선은 대칭축 $y=x$와 정확히 수직이므로 두 교점은 완벽한 대칭점 $(\\alpha, \\beta) \\leftrightarrow (\\beta, \\alpha)$가 됩니다.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v20/07_exam_22_sep_21_intro.jpg" alt="07" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8;">7단계 [03:15]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">[수능 기출] 22년 9월 21번 제시</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  직선 $y = -x + 4$와 두 곡선 $y=a^{{x-1}}, y=\\log_a(x-1)$ 및 선분 $\\overline{{AB}}=2\\sqrt{{2}}$ 조건 분석.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v20/08_isosceles_right_triangle_ratio.jpg" alt="08" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(250, 204, 21, 0.2); color: #facc15;">8단계 [03:48]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">직각이등변 $1:1:\\sqrt{{2}}$ 분해</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  $\\overline{{AB}} = 2\\sqrt{{2}}$이므로 가로 $\\Delta x = 2$, 세로 $\\Delta y = 2$로 즉각 분해됩니다!
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v20/09_coordinate_transformation_solve.jpg" alt="09" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(52, 211, 153, 0.2); color: #34d399;">9단계 [04:04]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">좌표 확정 및 밑 $a=2$ 도출</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  점 $A(1, 3)$, $B(3, 1)$, $C(0, \\frac{{1}}{{2}})$ 확정 후 삼각형 넓이 $S = \\frac{{7}}{{2}}$ 계산.
                </p>
              </div>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; overflow: hidden;">
              <img src="./captures_v20/10_three_principles_summary.jpg" alt="10" style="width: 100%; height: auto; display: block;">
              <div style="padding: 14px;">
                <span class="badge" style="background: rgba(168, 85, 247, 0.2); color: #c084fc;">10단계 [04:18]</span>
                <h4 style="color: #f1f5f9; margin: 8px 0 4px;">근육의 공식 최종 정리</h4>
                <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                  기울기, 평행이동, 대칭성의 3가지 원리로 모든 수능 지수·로그 문제를 꿰뚫는 마무리를 완성합니다.
                </p>
              </div>
            </div>

          </div>
        </div>

        <!-- TAB 2: MATHEMATICAL DERIVATION -->
        <div id="tabL20_2" class="tab-pane-l20" style="display: none;">
          <h3 style="color: #38bdf8; margin-bottom: 18px;">📐 2022학년도 9월 21번 3초 공식 완전 해설</h3>
          <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 24px; line-height: 1.8; color: #cbd5e1;">
            <h4 style="color: #38bdf8; font-size: 1.1rem; margin-bottom: 12px;">1. 문제 조건 분석</h4>
            <p>
              * 지수함수: $y = a^{{x-1}}$<br>
              * 로그함수: $y = \\log_a(x-1)$<br>
              * 교차 직선: $y = -x + 4$ (기울기 $m = -1$)<br>
              * 교점 간격: $\\overline{{AB}} = 2\\sqrt{{2}}$<br>
              * 점 $C$: 곡선 $y = a^{{x-1}}$의 $y$절편 $\\implies C(0, a^{{-1}}) = C(0, \\frac{{1}}{{a}})$
            </p>

            <h4 style="color: #facc15; font-size: 1.1rem; margin: 20px 0 12px;">2. 기울기 $-1$과 선분 길이의 직각이등변 분해</h4>
            <p>
              직선의 기울기가 $-1$이므로 $x$의 증가량과 $y$의 감소량의 비는 $1 : 1 : \\sqrt{{2}}$입니다.<br>
              따라서:
              $$\\overline{{AB}} = \\sqrt{{\\Delta x^2 + \\Delta y^2}} = \\Delta x \\sqrt{{2}} = 2\\sqrt{{2}} \\implies \\mathbf{{\\Delta x = 2, \\quad \\Delta y = 2}}$$
              점 $A$의 좌표를 $(\\alpha, -\\alpha + 4)$라 하면, 점 $B$의 좌표는:
              $$\\mathbf{{B(\\alpha + 2, -\\alpha + 2)}}$$
            </p>

            <h4 style="color: #ec4899; font-size: 1.1rem; margin: 20px 0 12px;">3. 평행이동과 대칭성의 역추적</h4>
            <p>
              두 함수 $y = a^{{x-1}}$과 $y = \\log_a(x-1)$은 역함수 원형 $y = a^x$와 $y = \\log_a x$를 <strong>$x$축 방향으로 $+1$만큼 평행이동</strong>한 것입니다.<br>
              따라서 $x$축으로 $-1$ 이동하면 $y=x$ 대칭 관계가 복원됩니다.<br>
              이 대칭성에 의해 두 점은 $y=-x+4$ 위에서 $A(1, 3)$과 $B(3, 1)$로 정확히 결정됩니다:
              $$A(1, 3) \\in y = a^{{x-1}} \\implies 3 = a^{{1-1}} + 2 \\implies a = 2$$
            </p>

            <h4 style="color: #34d399; font-size: 1.1rem; margin: 20px 0 12px;">4. 삼각형 ABC 넓이와 최종 답</h4>
            <p>
              세 점의 좌표: $A(1, 3), \\; B(3, 1), \\; C(0, \\frac{{1}}{{2}})$<br>
              선분 $AB$의 길이: $2\\sqrt{{2}}$<br>
              점 $C(0, \\frac{{1}}{{2}})$에서 직선 $x + y - 4 = 0$까지의 거리 $h$:
              $$h = \\frac{{|0 + \\frac{{1}}{{2}} - 4|}}{{\\sqrt{{1^2 + 1^2}}}} = \\frac{{\\frac{{7}}{{2}}}}{{\\sqrt{{2}}}} = \\frac{{7}}{{2\\sqrt{{2}}}}$$
              삼각형 $ABC$의 넓이 $S$:
              $$S = \\frac{{1}}{{2}} \\times \\overline{{AB}} \\times h = \\frac{{1}}{{2}} \\times 2\\sqrt{{2}} \\times \\frac{{7}}{{2\\sqrt{{2}}}} = \\mathbf{{\\frac{{7}}{{2}}}}$$
              $$\\therefore \\mathbf{{50 \\times S = 50 \\times \\frac{{7}}{{2}} = 175}}$$
            </p>
          </div>
        </div>

        <!-- TAB 3: MANIM SCRIPT -->
        <div id="tabL20_3" class="tab-pane-l20" style="display: none;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
            <h3 style="color: #38bdf8; margin: 0;">🎬 3Blue1Brown 스타일 Manim 파이썬 애니메이션 코드</h3>
            <button class="btn btn-primary" onclick="copyManimCode20()" style="font-size: 0.82rem; padding: 6px 14px;">
              📋 파이썬 코드 복사
            </button>
          </div>
          <div class="code-container">
            <div class="code-header">
              <span>Python 3.12 · Manim Community v0.18+ (exp_log_slope_symmetry_manim.py)</span>
            </div>
            <pre id="manimPre20" style="max-height: 480px; overflow-y: auto;"><code class="language-python">{escaped_manim}</code></pre>
          </div>
        </div>

        <!-- TAB 4: ORIGINAL VIDEO -->
        <div id="tabL20_4" class="tab-pane-l20" style="display: none;">
          <h3 style="color: #38bdf8; margin-bottom: 18px;">🎥 근육의 공식 유튜브 원본 특강 영상</h3>
          <div style="max-width: 680px; margin: 0 auto; background: #000; border-radius: 16px; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.15); box-shadow: 0 10px 30px rgba(0,0,0,0.6);">
            <video controls style="width: 100%; display: block;" poster="./captures_v20/01_transcendental_equation_limit.jpg">
              <source src="lecture_video20.mp4" type="video/mp4">
              브라우저가 HTML5 비디오를 지원하지 않습니다.
            </video>
            <div style="padding: 16px; background: rgba(15, 23, 42, 0.95); text-align: center;">
              <div style="font-weight: bold; color: #f1f5f9; margin-bottom: 6px;">지수, 로그함수에서 기울기 활용법-근육의 공식</div>
              <div style="font-size: 0.82rem; color: #94a3b8; margin-bottom: 12px;">채널: 근육의 공식 · 4분 22초 핵심 개념 및 기출 마스터</div>
              <a href="https://youtu.be/0cYeWjClTV4?si=H3v0PvHMn2DEzq2J" target="_blank" rel="noopener noreferrer" 
                 class="btn btn-secondary" style="font-size: 0.82rem; padding: 6px 14px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
                <span>▶ YouTube 원본 링크 열기</span>
              </a>
            </div>
          </div>
        </div>

        <!-- TAB 5: CSAT THREE EXAM COMPARISON -->
        <div id="tabL20_5" class="tab-pane-l20" style="display: none;">
          <h3 style="color: #38bdf8; margin-bottom: 18px;">📝 수능/평가원 3대 킬러 기출 비교 분석</h3>
          <div style="display: flex; flex-direction: column; gap: 16px;">
            <div style="background: rgba(15, 23, 42, 0.6); border-left: 4px solid #38bdf8; padding: 18px; border-radius: 0 10px 10px 0;">
              <h4 style="color: #38bdf8; margin-bottom: 6px;">1. 2022학년도 9월 모의평가 21번 (정답률 28%)</h4>
              <p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                <strong>핵심 포인트:</strong> $y = -x + 4$와 두 곡선 $y=a^{{x-1}}, y=\\log_a(x-1)$, $\\overline{{AB}}=2\\sqrt{{2}}$.<br>
                기울기 $-1$ 직각이등변 $1:1:\\sqrt{{2}}$를 적용하여 $\\Delta x = 2, \\Delta y = 2$로 좌표를 즉시 확정하고 $a=2$를 구해 삼각형 넓이 $50S = 175$를 산출하는 대표 문항입니다.
              </p>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border-left: 4px solid #facc15; padding: 18px; border-radius: 0 10px 10px 0;">
              <h4 style="color: #facc15; margin-bottom: 6px;">2. 2022학년도 수능 9번</h4>
              <p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                <strong>핵심 포인트:</strong> 밑이 같은 지수함수 $y = 2^{{x+1}}$과 $y = 2^x$ 사이의 평행이동 및 기울기 $-\\frac{{1}}{{2}}$인 직선과의 교점 간격 계산.<br>
                평행이동 벡터의 기울기가 주어진 직선과 일치함을 간파하면 복잡한 연립 없이 바로 거리가 나옵니다.
              </p>
            </div>

            <div style="background: rgba(15, 23, 42, 0.6); border-left: 4px solid #ec4899; padding: 18px; border-radius: 0 10px 10px 0;">
              <h4 style="color: #ec4899; margin-bottom: 6px;">3. 2023학년도 9월 모의평가 21번</h4>
              <p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.6;">
                <strong>핵심 포인트:</strong> 지수곡선 위의 두 점의 기울기와 중점 조건.<br>
                대칭축과의 수직성 및 내분점 비례식을 결합하여 미지수를 소거하는 고난도 킬러 문항에 동일한 원리가 완벽히 적용됩니다.
              </p>
            </div>
          </div>
        </div>

      </div>
    </div>
'''

    # Insert lecture20_html immediately before lecture19View
    if '<div id="lecture20View">' not in html:
        target_lec19 = '<div id="lecture19View"'
        html = html.replace(target_lec19, lecture20_html + '\n    ' + target_lec19, 1)
        print("Inserted lecture20View into HTML.")

    # 3. Update JavaScript: LECTURE_META, setLecture, and Lecture 20 code
    meta_insert = "    const LECTURE_META = {\n      20: { subj: 'math1',   subjName: '수학 I · 지수·로그함수', title: '제20강 · 지수·로그함수 기울기 $m=-1$ 활용법' },"
    html = html.replace("    const LECTURE_META = {", meta_insert, 1)

    # Update loop ranges in selectSubject and setLecture (19 -> 20)
    html = html.replace('for (let i = 1; i <= 19; i++)', 'for (let i = 1; i <= 20; i++)')

    # Update setLecture branching
    old_set_lec_top = "if (num === 19) setTimeout(renderL19, 50);"
    new_set_lec_top = "if (num === 20) setTimeout(renderL20, 50);\n      else if (num === 19) setTimeout(renderL19, 50);"
    html = html.replace(old_set_lec_top, new_set_lec_top, 1)

    # 4. Insert Lecture 20 JS Simulator & Tabs logic
    js_l20 = '''
    // ==============================================================
    // JAVASCRIPT FOR LECTURE 20 (EXPONENTIAL & LOG SLOPE & SYMMETRY)
    // ==============================================================
    let currentA20 = 2.0;
    let currentP20 = 1.0;
    let currentK20 = 4.0;
    let animRunning20 = false;
    let animTimer20 = null;
    let animDirK20 = 1;

    function applyPreset20(a, p, k) {
      currentA20 = parseFloat(a);
      currentP20 = parseFloat(p);
      currentK20 = parseFloat(k);

      const sA = document.getElementById("sliderA20");
      const sP = document.getElementById("sliderP20");
      const sK = document.getElementById("sliderK20");
      if (sA) sA.value = currentA20;
      if (sP) sP.value = currentP20;
      if (sK) sK.value = currentK20;

      updateL20();
    }

    function updateFromSliders20() {
      const sA = document.getElementById("sliderA20");
      const sP = document.getElementById("sliderP20");
      const sK = document.getElementById("sliderK20");
      if (sA) currentA20 = parseFloat(sA.value);
      if (sP) currentP20 = parseFloat(sP.value);
      if (sK) currentK20 = parseFloat(sK.value);

      updateL20();
    }

    function toggleAnimation20() {
      animRunning20 = !animRunning20;
      const btn = document.getElementById("btnAnim20");
      if (animRunning20) {
        if (btn) {
          btn.innerText = "⏸ 애니메이션 일시정지";
          btn.style.background = "#fb7185";
          btn.style.color = "#fff";
        }
        runAnimLoop20();
      } else {
        if (btn) {
          btn.innerText = "▶ 직선 y = -x + k 동적 스위프 애니메이션";
          btn.style.background = "#38bdf8";
          btn.style.color = "#0f172a";
        }
        if (animTimer20) {
          cancelAnimationFrame(animTimer20);
          animTimer20 = null;
        }
      }
    }

    function runAnimLoop20() {
      if (!animRunning20) return;

      currentK20 += animDirK20 * 0.02;
      if (currentK20 >= 5.5) {
        currentK20 = 5.5;
        animDirK20 = -1;
      } else if (currentK20 <= 2.8) {
        currentK20 = 2.8;
        animDirK20 = 1;
      }

      const sK = document.getElementById("sliderK20");
      if (sK) sK.value = currentK20.toFixed(2);

      updateL20();
      animTimer20 = requestAnimationFrame(runAnimLoop20);
    }

    function updateL20() {
      const a = currentA20;
      const p = currentP20;
      const k = currentK20;

      const elA = document.getElementById("valA20");
      const elP = document.getElementById("valP20");
      const elK = document.getElementById("valK20");
      if (elA) elA.innerText = a.toFixed(1);
      if (elP) elP.innerText = p.toFixed(1);
      if (elK) elK.innerText = k.toFixed(2);

      const dispFormula = document.getElementById("dispFormula20");
      if (dispFormula) {
        const pStr = p === 0 ? "x" : (p > 0 ? `(x - ${p.toFixed(1)})` : `(x + ${Math.abs(p).toFixed(1)})`);
        dispFormula.innerText = `y = ${a.toFixed(1)}^{${pStr}},  y = log_{${a.toFixed(1)}}${pStr},  y = -x + ${k.toFixed(2)}`;
      }

      // Numerical solution for intersection A with y = a^(x - p) and y = -x + k
      // solve f(x) = a^(x - p) + x - k = 0
      const fExp = (x) => Math.pow(a, x - p) + x - k;
      const ax = bisectionSolve(fExp, -1.0, k);

      // Numerical solution for intersection B with y = log_a(x - p) and y = -x + k
      // solve f(x) = log_a(x - p) + x - k = 0
      const lnA = Math.log(a);
      const fLog = (x) => (Math.log(x - p) / lnA) + x - k;
      const bx = bisectionSolve(fLog, p + 0.001, k + 5.0);

      let ptA = null, ptB = null;
      if (ax !== null) ptA = { x: ax, y: -ax + k };
      if (bx !== null) ptB = { x: bx, y: -bx + k };

      // Point C on y-axis: x = 0, y = a^(-p)
      const ptC = { x: 0, y: Math.pow(a, -p) };

      // Length and Area
      const statPoints = document.getElementById("statPoints20");
      const statLength = document.getElementById("statLength20");
      const statArea = document.getElementById("statArea20");

      if (ptA && ptB) {
        if (statPoints) {
          statPoints.innerText = `A(${ptA.x.toFixed(2)}, ${ptA.y.toFixed(2)}), B(${ptB.x.toFixed(2)}, ${ptB.y.toFixed(2)})`;
        }

        const dx = Math.abs(ptB.x - ptA.x);
        const dy = Math.abs(ptB.y - ptA.y);
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (statLength) {
          statLength.innerText = `L = ${dist.toFixed(2)} (${(dist / Math.SQRT2).toFixed(2)}√2), Δx = ${dx.toFixed(2)}, Δy = ${dy.toFixed(2)}`;
        }

        // Triangle ABC area using shoelace formula
        const area = 0.5 * Math.abs(
          ptA.x * (ptB.y - ptC.y) +
          ptB.x * (ptC.y - ptA.y) +
          ptC.x * (ptA.y - ptB.y)
        );

        if (statArea) {
          statArea.innerText = `S = ${area.toFixed(2)} ➔ 50 × S = ${(50 * area).toFixed(1)}`;
        }

        drawCanvasL20(ptA, ptB, ptC, area);
      } else {
        drawCanvasL20(null, null, ptC, 0);
      }
    }

    function drawCanvasL20(ptA, ptB, ptC, area) {
      const canvas = document.getElementById("canvasL20");
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
      const chkLineYX = document.getElementById("chkLineYX20") ? document.getElementById("chkLineYX20").checked : true;
      if (chkLineYX) {
        ctx.strokeStyle = "#facc15";
        ctx.lineWidth = 1.8;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(toScreenX(xMin), toScreenY(xMin));
        ctx.lineTo(toScreenX(xMax), toScreenY(xMax));
        ctx.stroke();
        ctx.setLineDash([]);

        ctx.fillStyle = "#facc15";
        ctx.font = "bold 12px 'Consolas', monospace";
        ctx.fillText("y = x", toScreenX(5.5), toScreenY(5.7));
      }

      const a = currentA20;
      const p = currentP20;
      const k = currentK20;

      // 4. Shaded Triangle ABC
      const chkShaded = document.getElementById("chkShadedTri20") ? document.getElementById("chkShadedTri20").checked : true;
      if (chkShaded && ptA && ptB && ptC) {
        ctx.fillStyle = "rgba(251, 191, 36, 0.18)";
        ctx.beginPath();
        ctx.moveTo(toScreenX(ptA.x), toScreenY(ptA.y));
        ctx.lineTo(toScreenX(ptB.x), toScreenY(ptB.y));
        ctx.lineTo(toScreenX(ptC.x), toScreenY(ptC.y));
        ctx.closePath();
        ctx.fill();

        ctx.strokeStyle = "rgba(251, 191, 36, 0.6)";
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }

      // 5. Line y = -x + k (Red)
      ctx.strokeStyle = "#fb7185";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(toScreenX(xMin), toScreenY(-xMin + k));
      ctx.lineTo(toScreenX(xMax), toScreenY(-xMax + k));
      ctx.stroke();

      ctx.fillStyle = "#fb7185";
      ctx.font = "bold 12px 'Consolas', monospace";
      ctx.fillText(`y = -x + ${k.toFixed(1)}`, toScreenX(Math.min(k - 0.2, 5.0)), toScreenY(0.4));

      // 6. Exponential Curve y = a^(x - p) (Cyan)
      ctx.lineWidth = 3.2;
      ctx.strokeStyle = "#38bdf8";
      ctx.beginPath();
      let startedExp = false;
      for (let x = xMin; x <= xMax; x += 0.02) {
        const y = Math.pow(a, x - p);
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

      // 7. Log Curve y = log_a(x - p) (Purple)
      ctx.lineWidth = 3.2;
      ctx.strokeStyle = "#c084fc";
      ctx.beginPath();
      let startedLog = false;
      const lnA = Math.log(a);
      for (let x = p + 0.01; x <= xMax; x += 0.02) {
        const y = Math.log(x - p) / lnA;
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

      // 8. Right Isosceles Triangle Guide: (ptA.x, ptA.y) to (ptB.x, ptA.y) to (ptB.x, ptB.y)
      const chkTriGuide = document.getElementById("chkTriangleGuide20") ? document.getElementById("chkTriangleGuide20").checked : true;
      if (chkTriGuide && ptA && ptB) {
        const cornerX = toScreenX(ptB.x);
        const cornerY = toScreenY(ptA.y);
        const aX = toScreenX(ptA.x);
        const aY = toScreenY(ptA.y);
        const bX = toScreenX(ptB.x);
        const bY = toScreenY(ptB.y);

        ctx.strokeStyle = "rgba(250, 204, 21, 0.8)";
        ctx.lineWidth = 2;
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(aX, aY);
        ctx.lineTo(cornerX, cornerY);
        ctx.lineTo(bX, bY);
        ctx.stroke();
        ctx.setLineDash([]);

        const dx = Math.abs(ptB.x - ptA.x);
        const dy = Math.abs(ptB.y - ptA.y);

        ctx.fillStyle = "#facc15";
        ctx.font = "bold 12px 'Consolas', monospace";
        ctx.fillText(`Δx = ${dx.toFixed(2)}`, (aX + cornerX) / 2 - 25, cornerY - 8);
        ctx.fillText(`Δy = ${dy.toFixed(2)}`, cornerX + 8, (cornerY + bY) / 2 + 4);
      }

      // 9. Points A, B, C Dots & Glows
      if (ptA && ptB) {
        // Point A
        drawGlowPoint(ctx, toScreenX(ptA.x), toScreenY(ptA.y), "#fb7185", `A(${ptA.x.toFixed(2)}, ${ptA.y.toFixed(2)})`, -80, -10);
        // Point B
        drawGlowPoint(ctx, toScreenX(ptB.x), toScreenY(ptB.y), "#fb7185", `B(${ptB.x.toFixed(2)}, ${ptB.y.toFixed(2)})`, 12, 16);
      }

      // Point C
      if (ptC) {
        drawGlowPoint(ctx, toScreenX(ptC.x), toScreenY(ptC.y), "#34d399", `C(0, ${ptC.y.toFixed(2)})`, -70, 16);
      }
    }

    function drawGlowPoint(ctx, sx, sy, color, label, offX, offY) {
      const grad = ctx.createRadialGradient(sx, sy, 2, sx, sy, 14);
      grad.addColorStop(0, color);
      grad.addColorStop(1, "rgba(0,0,0,0)");
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(sx, sy, 14, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.arc(sx, sy, 5.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 12px 'Consolas', monospace";
      ctx.fillText(label, sx + offX, sy + offY);
    }

    function switchL20Tab(tabIdx) {
      for (let i = 1; i <= 5; i++) {
        const btn = document.getElementById(`tabBtnL20_${i}`);
        const content = document.getElementById(`tabL20_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture20View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }

    function copyManimCode20() {
      const codeEl = document.querySelector("#manimPre20 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL20() {
      updateL20();
      if (window.renderMathInElement) {
        renderMathInElement(document.getElementById("lecture20View"), {
          delimiters: [{left: '$$', right: '$$', display: true}, {left: '$', right: '$', display: false}]
        });
      }
    }
'''

    # Insert JS before window.addEventListener('load')
    target_window_load = "window.addEventListener('load', () => {"
    html = html.replace(target_window_load, js_l20 + '\n    ' + target_window_load, 1)

    # In window.addEventListener('load'), setLecture(20) and renderL20()
    html = html.replace("setLecture(19);\n      renderL19();", "setLecture(20);\n      renderL20();")
    html = html.replace("setLecture(19);", "setLecture(20);")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done! Successfully injected Lecture 20 into index.html.")

if __name__ == '__main__':
    main()
