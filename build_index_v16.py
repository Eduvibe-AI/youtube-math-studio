# -*- coding: utf-8 -*-
"""
Script to build and inject Lecture 16 into index.html
Lecture: [2분] 단위원으로 조지는 삼각함수
Instructor: Bae Sang-myeon (MathPresso / Chulbyuk Math)
YouTube Short: https://youtube.com/shorts/-waKGGBKVSU
"""

import os
import re

def main():
    html_path = 'index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read manim code for tab
    with open('unit_circle_trig_manim.py', 'r', encoding='utf-8') as f:
        manim_code = f.read()

    # 1. Update Switcher Bar: Add btnLec16 as active, remove active from btnLec15
    if 'id="btnLec16"' not in html:
        old_btn15 = '<button class="lecture-btn active" id="btnLec15" onclick="setLecture(15)">'
        if old_btn15 in html:
            new_btn_block = '''<button class="lecture-btn active" id="btnLec16" onclick="setLecture(16)">
          단위원 삼각함수 정복 (배상면)
        </button>
        <button class="lecture-btn" id="btnLec15" onclick="setLecture(15)">'''
            html = html.replace(old_btn15, new_btn_block, 1)
            print("Added btnLec16 to switcher bar.")
        else:
            old_btn15_alt = '<button class="lecture-btn" id="btnLec15" onclick="setLecture(15)">'
            if old_btn15_alt in html:
                new_btn_block = '''<button class="lecture-btn active" id="btnLec16" onclick="setLecture(16)">
          단위원 삼각함수 정복 (배상면)
        </button>
        <button class="lecture-btn" id="btnLec15" onclick="setLecture(15)">'''
                html = html.replace(old_btn15_alt, new_btn_block, 1)
                print("Added btnLec16 to switcher bar (alt).")

    # Update captured_summary button label
    html = html.replace('📸 사진 1~15 핵심 전용 페이지', '📸 사진 1~16 핵심 전용 페이지')

    # 2. Hide lecture15View if active
    if '<div id="lecture15View">' in html:
        html = html.replace('<div id="lecture15View">', '<div id="lecture15View" style="display: none;">', 1)
        print("Set lecture15View to display: none.")

    # 3. Create Lecture 16 View HTML
    escaped_manim = (manim_code
                     .replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;'))

    lecture16_template = '''    <!-- ============================================================== -->
    <!-- SECTION FOR LECTURE 16 (UNIT CIRCLE TRIGONOMETRY: MATHPRESSO)     -->
    <!-- ============================================================== -->
    <div id="lecture16View">
      <header>
        <div class="badge-pill" style="border-color: rgba(56, 189, 248, 0.4); color: #38bdf8; box-shadow: 0 0 20px rgba(56, 189, 248, 0.3);">
          ⚡ 제16강 · 매스프레소 MathPresso (배상면 선생님 / 철벽수학)
        </div>
        <h1 style="background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #f43f5e 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          [2분] 단위원으로 완벽 정복하는 삼각함수
        </h1>
        <p class="subtitle" style="max-width: 900px; margin: 0 auto; line-height: 1.7; color: #cbd5e1;">
          "복잡한 삼각함수 공식들, 이제 더 이상 외우지 마세요!"<br>
          단위원 $x^2 + y^2 = 1$ 위의 점 $P(\\cos\\theta, \\sin\\theta)$ 하나로
          <strong>정의 · 음각 공식 ($-\\theta$) · 각변환 ($\\pi-\\theta$) · 그래프 생성 · 킬러 삼각부등식</strong>까지
          단 2분 만에 완벽하게 꿰뚫는 배상면 선생님의 기하학적 정석 강의입니다.
        </p>
      </header>

      <!-- TOP SUMMARY BANNER -->
      <div style="background: linear-gradient(135deg, rgba(56, 189, 248, 0.15), rgba(129, 140, 248, 0.1), rgba(15, 23, 42, 0.95)); border: 2px solid rgba(56, 189, 248, 0.4); border-radius: 20px; padding: 26px; margin-bottom: 35px; box-shadow: 0 12px 36px rgba(0, 0, 0, 0.5);">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; text-align: center;">
          <div style="background: rgba(15, 23, 42, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.3);">
            <div style="color: #38bdf8; font-weight: bold; font-size: 0.9rem;">1. 삼각함수의 본질</div>
            <div style="color: #fff; font-size: 1.1rem; margin-top: 4px; font-family: monospace;">$\\cos\\theta = x,\\ \\sin\\theta = y$</div>
            <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 2px;">$\\tan\\theta =$ 동경의 기울기</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(244, 63, 94, 0.3);">
            <div style="color: #f43f5e; font-weight: bold; font-size: 0.9rem;">2. 음각 공식 ($-\\theta$)</div>
            <div style="color: #fff; font-size: 1.1rem; margin-top: 4px; font-family: monospace;">$x$축 대칭 $\\implies \\cos$ 유지</div>
            <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 2px;">$\\sin, \\tan$는 부호 반전</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(234, 179, 8, 0.3);">
            <div style="color: #facc15; font-weight: bold; font-size: 0.9rem;">3. 각변환 ($\\pi-\\theta$)</div>
            <div style="color: #fff; font-size: 1.1rem; margin-top: 4px; font-family: monospace;">$y$축 대칭 $\\implies \\sin$ 유지</div>
            <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 2px;">$\\cos, \\tan$는 부호 반전</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); padding: 14px; border-radius: 12px; border: 1px solid rgba(74, 222, 128, 0.3);">
            <div style="color: #4ade80; font-weight: bold; font-size: 0.9rem;">4. 부등식 1초 컷</div>
            <div style="color: #fff; font-size: 1.1rem; margin-top: 4px; font-family: monospace;">$\\sin\\theta < \\cos\\theta \\iff y < x$</div>
            <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 2px;">직선 $y=x$의 아래쪽 영역!</div>
          </div>
        </div>
      </div>

      <!-- MAIN INTERACTIVE LAB: UNIT CIRCLE SIMULATOR -->
      <div class="card" style="margin-bottom: 40px; border-color: rgba(56, 189, 248, 0.4); box-shadow: 0 10px 30px rgba(56, 189, 248, 0.15);">
        <h2 style="color: #38bdf8; display: flex; align-items: center; gap: 10px;">
          <span>🔬</span> 단위원 삼각함수 &amp; 기하학적 대칭 인터랙티브 랩
        </h2>
        <p style="color: #94a3b8; margin-bottom: 20px;">
          각도 $\\theta$를 드래그하거나 슬라이더를 조작하여 동경의 회전, 삼각함수의 기하학적 길이($\\cos, \\sin, \\tan$),
          대칭이동($x$축, $y$축), 삼각부등식($y < x$) 영역을 직접 시각화해보세요.
        </p>

        <!-- LAB MODE CONTROLS -->
        <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; padding: 20px; margin-bottom: 22px;">
          <div style="display: flex; flex-wrap: wrap; gap: 10px; align-items: center; margin-bottom: 16px;">
            <span style="font-weight: 700; color: #e2e8f0; font-size: 0.95rem;">모드 선택:</span>
            <button class="nav-btn active" id="btnMode16_1" onclick="setMode16(1)">1. 기본 정의 ($P(\\cos\\theta, \\sin\\theta)$)</button>
            <button class="nav-btn" id="btnMode16_2" onclick="setMode16(2)">2. 음각 공식 ($- \\theta$, $x$축 대칭)</button>
            <button class="nav-btn" id="btnMode16_3" onclick="setMode16(3)">3. 각변환 ($\\pi - \\theta$, $y$축 대칭)</button>
            <button class="nav-btn" id="btnMode16_4" onclick="setMode16(4)" style="border-color: #facc15; color: #facc15;">4. 삼각부등식 ($\\sin\\theta < \\cos\\theta$)</button>
          </div>

          <!-- ANGLE PRESETS & SLIDER -->
          <div style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-bottom: 16px;">
            <span style="font-size: 0.85rem; color: #94a3b8;">특수각 바로가기:</span>
            <button class="nav-btn" onclick="setAngle16(30)" style="padding: 4px 10px; font-size: 0.8rem;">30° (π/6)</button>
            <button class="nav-btn" onclick="setAngle16(45)" style="padding: 4px 10px; font-size: 0.8rem; border-color: #facc15;">45° (π/4)</button>
            <button class="nav-btn" onclick="setAngle16(60)" style="padding: 4px 10px; font-size: 0.8rem;">60° (π/3)</button>
            <button class="nav-btn" onclick="setAngle16(90)" style="padding: 4px 10px; font-size: 0.8rem;">90° (π/2)</button>
            <button class="nav-btn" onclick="setAngle16(120)" style="padding: 4px 10px; font-size: 0.8rem;">120° (2π/3)</button>
            <button class="nav-btn" onclick="setAngle16(135)" style="padding: 4px 10px; font-size: 0.8rem;">135° (3π/4)</button>
            <button class="nav-btn" onclick="setAngle16(180)" style="padding: 4px 10px; font-size: 0.8rem;">180° (π)</button>
            <button class="nav-btn" onclick="setAngle16(225)" style="padding: 4px 10px; font-size: 0.8rem; border-color: #facc15;">225° (5π/4)</button>
            <button class="nav-btn" onclick="setAngle16(270)" style="padding: 4px 10px; font-size: 0.8rem;">270° (3π/2)</button>
            <button class="nav-btn" onclick="setAngle16(315)" style="padding: 4px 10px; font-size: 0.8rem;">315° (7π/4)</button>
          </div>

          <div style="display: flex; flex-wrap: wrap; gap: 16px; align-items: center;">
            <div style="flex: 1; min-width: 250px; display: flex; align-items: center; gap: 12px;">
              <span style="color: #38bdf8; font-weight: bold; font-size: 0.95rem;">각도 $\\theta$ 슬라이더:</span>
              <input type="range" id="sliderAngle16" min="0" max="360" value="45" style="flex: 1; accent-color: #38bdf8;" oninput="updateFromAngleSlider16(this.value)">
              <span id="labelAngleDeg16" style="color: #facc15; font-family: monospace; font-weight: bold; min-width: 48px; text-align: right;">45°</span>
            </div>
            <div style="color: #94a3b8; font-size: 0.85rem; font-family: monospace;" id="labelAngleRad16">
              $\\theta = 0.250\\pi$ rad
            </div>
          </div>
        </div>

        <!-- REALTIME VALUES -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 14px; margin-bottom: 22px;">
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 12px; padding: 12px; text-align: center;">
            <div style="font-size: 0.8rem; color: #94a3b8;">x좌표 = $\\cos\\theta$</div>
            <div id="statCos16" style="font-size: 1.2rem; font-weight: bold; color: #38bdf8; font-family: monospace;">+0.7071</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(74, 222, 128, 0.3); border-radius: 12px; padding: 12px; text-align: center;">
            <div style="font-size: 0.8rem; color: #94a3b8;">y좌표 = $\\sin\\theta$</div>
            <div id="statSin16" style="font-size: 1.2rem; font-weight: bold; color: #4ade80; font-family: monospace;">+0.7071</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(244, 63, 94, 0.3); border-radius: 12px; padding: 12px; text-align: center;">
            <div style="font-size: 0.8rem; color: #94a3b8;">기울기 = $\\tan\\theta$</div>
            <div id="statTan16" style="font-size: 1.2rem; font-weight: bold; color: #f43f5e; font-family: monospace;">+1.0000</div>
          </div>
          <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(234, 179, 8, 0.3); border-radius: 12px; padding: 12px; text-align: center;">
            <div style="font-size: 0.8rem; color: #94a3b8;">항등식 $\\sin^2 + \\cos^2$</div>
            <div id="statIdentity16" style="font-size: 1.2rem; font-weight: bold; color: #facc15; font-family: monospace;">1.0000</div>
          </div>
        </div>

        <!-- CANVAS -->
        <div style="background: #070d19; border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 16px; padding: 15px; position: relative;">
          <canvas id="canvasUnitCircle16" width="900" height="520" style="width: 100%; height: auto; display: block; cursor: crosshair;"></canvas>
          <div id="canvasNote16" style="margin-top: 10px; font-size: 0.85rem; color: #94a3b8; text-align: center;">
            💡 원 위를 클릭하거나 마우스로 드래그하면 동경의 각도 $\\theta$를 실시간으로 변경할 수 있습니다.
          </div>
        </div>
      </div>

      <!-- IN-DEPTH CONCEPT TABS -->
      <div class="card" style="margin-bottom: 40px;">
        <h2 style="color: #38bdf8; display: flex; align-items: center; gap: 10px;">
          <span>📚</span> 단위원 삼각함수 핵심 원리 &amp; 수능 킬러 가이드
        </h2>

        <div style="display: flex; gap: 10px; margin-bottom: 24px; border-bottom: 1px solid #334155; padding-bottom: 12px; flex-wrap: wrap;">
          <button class="nav-btn active" id="tabBtnL16_1" onclick="switchL16Tab(1)">1. 단위원과 본질적 정의</button>
          <button class="nav-btn" id="tabBtnL16_2" onclick="switchL16Tab(2)">2. 음각 공식 (x축 대칭)</button>
          <button class="nav-btn" id="tabBtnL16_3" onclick="switchL16Tab(3)">3. 각변환 공식 (y축 대칭)</button>
          <button class="nav-btn" id="tabBtnL16_4" onclick="switchL16Tab(4)">4. 그래프 생성 원리</button>
          <button class="nav-btn" id="tabBtnL16_5" onclick="switchL16Tab(5)">5. 삼각부등식 1초 컷 비법</button>
          <button class="nav-btn" id="tabBtnL16_6" onclick="switchL16Tab(6)">6. Manim 애니메이션 코드</button>
        </div>

        <!-- TAB 1: DEFINITION -->
        <div id="tabL16_1" class="tab-content" style="display: block;">
          <h3 style="color: #38bdf8;">1. 단위원 $x^2 + y^2 = 1$과 삼각함수의 기하학적 정의</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            중학교 시절 배웠던 "직각삼각형의 변의 비"로서의 삼각비는 $0^\\circ < \\theta < 90^\\circ$의 예각에만 갇혀 있습니다.<br>
            고등학교 수학Ⅰ에서 각을 음수와 $360^\\circ$ 이상인 모든 실수(일반각)로 확장하기 위한 <strong>유일한 출발점이 바로 단위원</strong>입니다.
          </p>
          <div style="background: rgba(15, 23, 42, 0.8); border-left: 4px solid #38bdf8; padding: 18px; border-radius: 0 12px 12px 0; margin: 20px 0;">
            <p style="color: #e2e8f0; margin: 0 0 10px 0; font-weight: bold;">
              단위원 $x^2 + y^2 = 1$ 위의 점 $P$에 대하여, $x$축 양의 방향과 선분 $OP$가 이루는 각이 $\\theta$일 때:
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 15px;">
              <div style="background: #0f172a; padding: 12px; border-radius: 8px; border: 1px solid #38bdf8;">
                <span style="color: #38bdf8; font-weight: bold;">$\\cos\\theta$</span> = 점 $P$의 <strong>$x$좌표</strong> (가로 위치)
              </div>
              <div style="background: #0f172a; padding: 12px; border-radius: 8px; border: 1px solid #4ade80;">
                <span style="color: #4ade80; font-weight: bold;">$\\sin\\theta$</span> = 점 $P$의 <strong>$y$좌표</strong> (세로 높이)
              </div>
              <div style="background: #0f172a; padding: 12px; border-radius: 8px; border: 1px solid #f43f5e;">
                <span style="color: #f43f5e; font-weight: bold;">$\\tan\\theta$</span> = 동경 $OP$의 <strong>기울기 (Slope)</strong>
              </div>
            </div>
          </div>
          <p style="color: #cbd5e1; line-height: 1.8;">
            점 $P(\\cos\\theta, \\sin\\theta)$는 단위원 $x^2 + y^2 = 1$의 둘레 위에 있으므로, 그 좌표를 방정식에 대입하면:
          </p>
          <div style="text-align: center; font-size: 1.3rem; color: #facc15; font-family: monospace; margin: 15px 0;">
            $$(\\cos\\theta)^2 + (\\sin\\theta)^2 = 1 \\iff \\sin^2\\theta + \\cos^2\\theta = 1$$
          </div>
          <p style="color: #cbd5e1; line-height: 1.8;">
            어떤 기교도 없이, <strong>"단위원 위의 점"이라는 정의 그 자체</strong>에서 모든 피타고라스 삼각항등식이 자명하게 탄생합니다.
          </p>
        </div>

        <!-- TAB 2: NEGATIVE ANGLE -->
        <div id="tabL16_2" class="tab-content" style="display: none;">
          <h3 style="color: #f43f5e;">2. 음각 공식 ($- \\theta$)과 $x$축 대칭이동</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            $\\cos(-\\theta)$는 왜 부호가 그대로이고, $\\sin(-\\theta)$는 왜 마이너스가 튀어나올까요?
            단위원에서 <strong>$x$축 대칭</strong> 하나만 그리면 1초 만에 증명됩니다.
          </p>
          <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(244, 63, 94, 0.3); border-radius: 12px; padding: 20px; margin: 20px 0;">
            <ul style="color: #e2e8f0; line-height: 1.9; margin: 0; padding-left: 20px;">
              <li>동경 $\\theta$의 점: $P(\\cos\\theta, \\sin\\theta)$</li>
              <li>점 $P$를 <strong>$x$축 대칭이동</strong>한 점: $Q$ $\\implies$ 동경의 각은 <strong>$-\\theta$</strong></li>
              <li>점 $Q$의 좌표 정의: $(\\cos(-\\theta), \\sin(-\\theta))$</li>
              <li>그런데 $x$축 대칭의 좌표 변환 공식: $(x, y) \\to (x, -y) = (\\cos\\theta, -\\sin\\theta)$</li>
            </ul>
            <hr style="border: 0; border-top: 1px dashed #475569; margin: 15px 0;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; text-align: center;">
              <div style="background: #0b1120; padding: 12px; border-radius: 8px;">
                <div style="color: #38bdf8; font-weight: bold;">$\\cos(-\\theta) = \\cos\\theta$</div>
                <div style="color: #94a3b8; font-size: 0.85rem;">$x$좌표 불변 (우함수)</div>
              </div>
              <div style="background: #0b1120; padding: 12px; border-radius: 8px;">
                <div style="color: #4ade80; font-weight: bold;">$\\sin(-\\theta) = -\\sin\\theta$</div>
                <div style="color: #94a3b8; font-size: 0.85rem;">$y$좌표 부호 반전 (기함수)</div>
              </div>
              <div style="background: #0b1120; padding: 12px; border-radius: 8px;">
                <div style="color: #f43f5e; font-weight: bold;">$\\tan(-\\theta) = -\\tan\\theta$</div>
                <div style="color: #94a3b8; font-size: 0.85rem;">동경 기울기 반전 (기함수)</div>
              </div>
            </div>
          </div>
        </div>

        <!-- TAB 3: PI MINUS THETA -->
        <div id="tabL16_3" class="tab-content" style="display: none;">
          <h3 style="color: #facc15;">3. 각변환 공식 ($\\pi - \\theta$)과 $y$축 대칭이동</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            학생들이 가장 헷갈려하는 2사분면 각변환 공식 $\\pi - \\theta$ ($180^\\circ - \\theta$)는
            단위원에서 <strong>$y$축 대칭이동</strong>으로 완벽하게 정리됩니다.
          </p>
          <div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(234, 179, 8, 0.3); border-radius: 12px; padding: 20px; margin: 20px 0;">
            <p style="color: #e2e8f0; line-height: 1.8; margin-bottom: 12px;">
              각 $\\pi$($180^\\circ$)는 음의 $x$축입니다. 여기서 $\\theta$만큼 거꾸로 돌아간 동경 $\\pi - \\theta$는
              동경 $\\theta$와 <strong>$y$축에 대하여 좌우 대칭</strong>입니다.
            </p>
            <div style="background: #0b1120; padding: 16px; border-radius: 10px; margin-bottom: 12px;">
              $$\\begin{aligned}
              \\sin(\\pi - \\theta) &= \\sin\\theta \\quad (y\\text{좌표 높이가 완벽히 동일!}) \\\\
              \\cos(\\pi - \\theta) &= -\\cos\\theta \\quad (x\\text{좌표 좌우가 반대!}) \\\\
              \\tan(\\pi - \\theta) &= -\\tan\\theta \\quad (\\text{기울기의 부호가 반대!})
              \\end{aligned}$$
            </div>
            <p style="color: #4ade80; font-weight: bold; margin: 0;">
              💡 "사인은 높이니까 $y$축 대칭을 해도 높이가 같아서 그대로 양수!"라는 배상면 선생님의 설명 한마디면 평생 까먹지 않습니다.
            </p>
          </div>
        </div>

        <!-- TAB 4: GRAPH UNFOLDING -->
        <div id="tabL16_4" class="tab-content" style="display: none;">
          <h3 style="color: #818cf8;">4. 삼각함수 3대 곡선($\\sin, \\cos, \\tan$)의 생성 원리</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            단위원에서 각 $\\theta$가 $0$부터 $2\\pi$까지 회전할 때, 점 $P$의 움직임을 가로축(시간/각도 $\\theta$)으로 펼치면 세 가지 그래프가 자연스럽게 탄생합니다.
          </p>
          <div style="display: grid; gap: 15px; margin: 20px 0;">
            <div style="background: rgba(15, 23, 42, 0.8); border-left: 4px solid #4ade80; padding: 16px; border-radius: 0 10px 10px 0;">
              <h4 style="color: #4ade80; margin: 0 0 6px 0;">1) $y = \\sin\\theta$ 곡선의 생성</h4>
              <p style="color: #cbd5e1; margin: 0; font-size: 0.95rem; line-height: 1.6;">
                점 $P$의 <strong>$y$좌표(높이)</strong>를 각 $\\frac{\\pi}{2}$($90^\\circ$) 간격으로 펼쳐서 점을 찍어나갑니다.<br>
                높이 변화: $0 \\to +1 \\to 0 \\to -1 \\to 0$ 주기로 사인 곡선 형성.
              </p>
            </div>
            <div style="background: rgba(15, 23, 42, 0.8); border-left: 4px solid #38bdf8; padding: 16px; border-radius: 0 10px 10px 0;">
              <h4 style="color: #38bdf8; margin: 0 0 6px 0;">2) $y = \\cos\\theta$ 곡선의 생성</h4>
              <p style="color: #cbd5e1; margin: 0; font-size: 0.95rem; line-height: 1.6;">
                점 $P$의 <strong>$x$좌표(가로 변위)</strong>를 펼쳐서 오른쪽 그래프의 높이로 나타냅니다.<br>
                가로 위치 변화: $+1 \\to 0 \\to -1 \\to 0 \\to +1$ 주기로 코사인 곡선 형성.
              </p>
            </div>
            <div style="background: rgba(15, 23, 42, 0.8); border-left: 4px solid #f43f5e; padding: 16px; border-radius: 0 10px 10px 0;">
              <h4 style="color: #f43f5e; margin: 0 0 6px 0;">3) $y = \\tan\\theta$ 곡선과 점근선의 비밀</h4>
              <p style="color: #cbd5e1; margin: 0; font-size: 0.95rem; line-height: 1.6;">
                동경 $OP$의 <strong>기울기</strong>를 찍어나갑니다.<br>
                $\\theta = \\frac{\\pi}{2}, \\frac{3\\pi}{2}$에서는 동경이 $y$축과 겹쳐 <strong>수직선</strong>이 되므로 <strong>기울기가 존재하지 않음(무한대)</strong> $\\implies$ <strong>점근선 $x = \\frac{\\pi}{2} + n\\pi$</strong> 탄생!
              </p>
            </div>
          </div>
        </div>

        <!-- TAB 5: INEQUALITY -->
        <div id="tabL16_5" class="tab-content" style="display: none;">
          <h3 style="color: #facc15;">5. 삼각부등식 $\\sin\\theta < \\cos\\theta$ 1초 컷 비법</h3>
          <p style="color: #cbd5e1; line-height: 1.8;">
            내신/수능에서 사인과 코사인의 대소를 묻는 부등식이 나오면 대부분의 학생들이 두 개의 파동 그래프를 겹쳐 그리느라 시간을 낭비합니다.<br>
            배상면 선생님의 <strong>단위원 영역 치환법</strong>을 쓰면 작도 없이 1초 만에 암산됩니다!
          </p>
          <div style="background: rgba(15, 23, 42, 0.9); border: 2px solid #facc15; border-radius: 14px; padding: 22px; margin: 20px 0;">
            <div style="font-size: 1.15rem; color: #facc15; font-weight: bold; margin-bottom: 12px;">
              [문제]: $0 \\le \\theta < 2\\pi$ 일 때, 부등식 $\\sin\\theta < \\cos\\theta$ 를 푸시오.
            </div>
            <div style="background: #0b1120; padding: 16px; border-radius: 10px; margin-bottom: 15px;">
              <p style="color: #e2e8f0; line-height: 1.8; margin: 0;">
                1) 삼각함수의 단위원 정의: $\\sin\\theta = y, \\;\\; \\cos\\theta = x$<br>
                2) 부등식에 대입: <strong>$y < x$</strong><br>
                3) 단위원 $x^2 + y^2 = 1$ 둘레에서 <strong>직선 $y = x$의 아래쪽 영역($y < x$)</strong>에 있는 각도를 찾는다!<br>
                4) 단위원과 $y = x$의 교점: $\\theta = 45^\\circ (\\frac{\\pi}{4}), \\;\\; 225^\\circ (\\frac{5\\pi}{4})$<br>
                5) $y=x$의 아래쪽에 해당하는 원의 둘레 범위:<br>
                <span style="font-size: 1.2rem; color: #facc15; font-weight: bold; font-family: monospace;">
                  $$0 \\le \\theta < \\frac{\\pi}{4} \\quad \\text{또는} \\quad \\frac{5\\pi}{4} < \\theta < 2\\pi$$
                </span>
                (도 단위: $0^\\circ \\le \\theta < 45^\\circ \\;\\cup\\; 225^\\circ < \\theta < 360^\\circ$)
              </p>
            </div>
            <p style="color: #4ade80; font-weight: bold; margin: 0;">
              ✨ 단위원에 $45^\\circ$ 대각선 하나 긋는 것만으로 정답 구간이 한눈에 드러납니다!
            </p>
          </div>
        </div>

        <!-- TAB 6: MANIM CODE -->
        <div id="tabL16_6" class="tab-content" style="display: none;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <h3 style="color: #38bdf8; margin: 0;">3Blue1Brown 스타일 Manim Community 애니메이션 코드</h3>
            <button class="nav-btn" onclick="copyManimCode16()" style="padding: 6px 14px; font-size: 0.85rem; border-color: #38bdf8;">📋 코드 복사</button>
          </div>
          <p style="color: #94a3b8; font-size: 0.9rem;">
            단위원 회전, $\\cos/\\sin$ 사영선, $x$축/ $y$축 대칭점, 직선 $y=x$와 삼각부등식 해 집합 호(Arc)를 시각화한 파이썬 스크립트입니다.
          </p>
          <pre id="manimPre16" style="background: #0f172a; border: 1px solid #334155; border-radius: 10px; padding: 18px; color: #e2e8f0; font-family: 'Consolas', monospace; font-size: 0.85rem; max-height: 500px; overflow-y: auto; line-height: 1.5;"><code>__MANIM_CODE__</code></pre>
        </div>
      </div>

      <!-- TIMELINE CAPTURE CARDS -->
      <div class="card" style="margin-bottom: 40px;">
        <h2 style="color: #38bdf8; display: flex; align-items: center; gap: 10px;">
          <span>🎬</span> 타임라인별 핵심 판서 &amp; 화면 캡처 해설 (10장)
        </h2>
        <p style="color: #94a3b8; margin-bottom: 25px;">
          배상면 선생님의 114초 강의 흐름을 10장의 고화질(1080p) 프레임으로 정밀 분석했습니다.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
          <!-- CARD 1 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v16/01_unit_circle_p_definition.jpg" alt="01 단위원 정의" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">00:09</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">01. 단위원과 $P(\\cos\\theta, \\sin\\theta)$</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                단위원 $x^2+y^2=1$ 위의 점 $P$의 $x$좌표는 $\\cos\\theta$, $y$좌표는 $\\sin\\theta$, 기울기는 $\\tan\\theta$.
              </p>
            </div>
          </div>

          <!-- CARD 2 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v16/02_sin_square_plus_cos_square_one.jpg" alt="02 피타고라스 항등식" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">00:20</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">02. 피타고라스 항등식의 탄생</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                단위원 식 $x^2+y^2=1$에 좌표를 대입하여 $\\sin^2\\theta + \\cos^2\\theta = 1$이 즉각 성립함을 보입니다.
              </p>
            </div>
          </div>

          <!-- CARD 3 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v16/03_x_axis_symmetry_negative_theta.jpg" alt="03 x축 대칭" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">00:32</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">03. $x$축 대칭이동과 동경 $-\\theta$</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                점 $P$를 $x$축 대칭이동한 점 $Q$의 동경은 $-\\theta$가 되며, $Q(\\cos(-\\theta), \\sin(-\\theta))$로 정의됩니다.
              </p>
            </div>
          </div>

          <!-- CARD 4 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v16/04_negative_angle_formulas_derived.jpg" alt="04 음각 공식 유도" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">00:44</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">04. 음각 공식의 완성</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $Q(\\cos\\theta, -\\sin\\theta)$와의 성분 비교를 통해 $\\cos(-\\theta) = \\cos\\theta, \\sin(-\\theta) = -\\sin\\theta$ 유도.
              </p>
            </div>
          </div>

          <!-- CARD 5 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v16/05_pi_minus_theta_y_axis_symmetry.jpg" alt="05 y축 대칭 각변환" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">01:00</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">05. 각변환 $\\pi-\\theta$와 $y$축 대칭</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                동경 $\\pi-\\theta$는 $\\theta$와 $y$축 대칭이므로 높이($\\sin$)는 같고, 가로($\\cos$)와 기울기($\\tan$)는 부호가 반전됩니다.
              </p>
            </div>
          </div>

          <!-- CARD 6 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v16/06_sin_curve_unfolding_y_coord.jpg" alt="06 사인 곡선 펼치기" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">01:14</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">06. $y = \\sin\\theta$ 곡선의 생성</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                각 $\\theta$를 $\\frac{\\pi}{2}$ 간격으로 펼치며 점 $P$의 $y$좌표(높이)를 추적하여 부드러운 사인 파동을 그립니다.
              </p>
            </div>
          </div>

          <!-- CARD 7 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v16/07_cos_and_tan_curve_generation.jpg" alt="07 코사인과 탄젠트 곡선" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">01:25</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">07. $\\cos, \\tan$ 곡선의 연속 생성</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                코사인은 점 $P$의 $x$좌표를, 탄젠트는 선분 $OP$의 기울기를 추적하여 곡선을 만듭니다.
              </p>
            </div>
          </div>

          <!-- CARD 8 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v16/08_tan_asymptote_vertical_slope.jpg" alt="08 탄젠트 점근선" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">01:32</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">08. 탄젠트 점근선의 원리</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $\\theta = \\frac{\\pi}{2} + n\\pi$에서는 동경이 수직선이 되어 기울기가 정의되지 않으므로 점근선이 됩니다.
              </p>
            </div>
          </div>

          <!-- CARD 9 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v16/09_trig_inequality_sin_less_cos.jpg" alt="09 삼각부등식" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">01:41</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">09. 삼각부등식: $\\sin\\theta < \\cos\\theta$</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                $\\sin\\theta=y, \\cos\\theta=x$로 두어 부등식을 $y < x$로 치환하고, 직선 $y=x$의 아래쪽 영역을 단위원에서 탐색합니다.
              </p>
            </div>
          </div>

          <!-- CARD 10 -->
          <div style="background: #0f172a; border: 1px solid rgba(148, 163, 184, 0.2); border-radius: 14px; overflow: hidden;">
            <img src="captures_v16/10_trig_inequality_final_solution_range.jpg" alt="10 부등식 최종 해" style="width: 100%; height: auto; display: block;">
            <div style="padding: 16px;">
              <span class="badge" style="background: #334155; color: #38bdf8; font-size: 0.75rem;">01:48</span>
              <h4 style="color: #f8fafc; margin: 8px 0 6px 0;">10. 최종 부등식 해 도출</h4>
              <p style="color: #94a3b8; font-size: 0.85rem; margin: 0; line-height: 1.6;">
                교점 $45^\\circ$와 $225^\\circ$를 기준으로 $0^\\circ \\le \\theta < 45^\\circ$ 및 $225^\\circ < \\theta < 360^\\circ$의 명쾌한 해 완성!
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
'''

    lecture16_html = lecture16_template.replace('__MANIM_CODE__', escaped_manim)

    # Insert lecture16View before lecture15View
    idx_lec15 = html.find('<div id="lecture15View"')
    if idx_lec15 != -1:
        html = html[:idx_lec15] + lecture16_html + '\n' + html[idx_lec15:]
        print("Inserted lecture16View before lecture15View.")

    # 4. Insert Lecture 16 JavaScript
    js_code_16 = '''
    // ==============================================================
    // JAVASCRIPT FOR LECTURE 16 (UNIT CIRCLE TRIGONOMETRY: MATHPRESSO)
    // ==============================================================
    let currentAngleDeg16 = 45;
    let currentMode16 = 1;
    let isDraggingUnitCircle16 = false;

    function setAngle16(deg) {
      currentAngleDeg16 = (deg % 360 + 360) % 360;
      const slider = document.getElementById("sliderAngle16");
      if (slider) slider.value = currentAngleDeg16;
      updateL16();
    }

    function updateFromAngleSlider16(val) {
      currentAngleDeg16 = parseFloat(val);
      updateL16();
    }

    function setMode16(mode) {
      currentMode16 = mode;
      for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`btnMode16_${i}`);
        if (btn) btn.classList.toggle("active", i === mode);
      }
      renderCanvasL16();
    }

    function updateL16() {
      const deg = currentAngleDeg16;
      const rad = deg * Math.PI / 180;
      const cosVal = Math.cos(rad);
      const sinVal = Math.sin(rad);
      const tanVal = Math.tan(rad);

      // Update labels
      const degLabel = document.getElementById("labelAngleDeg16");
      const radLabel = document.getElementById("labelAngleRad16");
      if (degLabel) degLabel.innerText = `${Math.round(deg)}°`;
      if (radLabel) radLabel.innerHTML = `$\\theta = ${(rad / Math.PI).toFixed(3)}\\pi$ rad (${rad.toFixed(3)})`;

      const statCos = document.getElementById("statCos16");
      const statSin = document.getElementById("statSin16");
      const statTan = document.getElementById("statTan16");
      const statId = document.getElementById("statIdentity16");

      if (statCos) statCos.innerText = (cosVal >= 0 ? "+" : "") + cosVal.toFixed(4);
      if (statSin) statSin.innerText = (sinVal >= 0 ? "+" : "") + sinVal.toFixed(4);
      if (statTan) {
        if (Math.abs(cosVal) < 1e-4) {
          statTan.innerText = "정의 안 됨 (점근선)";
        } else {
          statTan.innerText = (tanVal >= 0 ? "+" : "") + tanVal.toFixed(4);
        }
      }
      if (statId) statId.innerText = (cosVal * cosVal + sinVal * sinVal).toFixed(4);

      renderCanvasL16();
      if (window.MathJax && MathJax.typesetPromise) {
        MathJax.typesetPromise([radLabel]);
      }
    }

    function renderCanvasL16() {
      const canvas = document.getElementById("canvasUnitCircle16");
      if (!canvas) return;
      const ctx = canvas.getContext("2d");
      const w = canvas.width;
      const h = canvas.height;

      ctx.clearRect(0, 0, w, h);

      const cx = w * 0.42;
      const cy = h * 0.5;
      const r = Math.min(w, h) * 0.38;

      const deg = currentAngleDeg16;
      const rad = deg * Math.PI / 180;
      const cosVal = Math.cos(rad);
      const sinVal = Math.sin(rad);
      const tanVal = Math.tan(rad);

      const px = cx + r * cosVal;
      const py = cy - r * sinVal;

      // Draw Grid / Coordinate Axes
      ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
      ctx.lineWidth = 1.5;

      // X axis
      ctx.beginPath();
      ctx.moveTo(cx - r - 60, cy);
      ctx.lineTo(cx + r + 60, cy);
      ctx.stroke();

      // Y axis
      ctx.beginPath();
      ctx.moveTo(cx, cy - r - 50);
      ctx.lineTo(cx, cy + r + 50);
      ctx.stroke();

      // Axis labels
      ctx.fillStyle = "#94a3b8";
      ctx.font = "bold 13px 'Consolas', monospace";
      ctx.fillText("x", cx + r + 45, cy + 18);
      ctx.fillText("y", cx + 12, cy - r - 35);
      ctx.fillText("O", cx - 18, cy + 18);
      ctx.fillText("1", cx + r, cy + 18);
      ctx.fillText("-1", cx - r - 22, cy + 18);
      ctx.fillText("1", cx - 18, cy - r);
      ctx.fillText("-1", cx - 22, cy + r + 15);

      // Unit Circle
      ctx.strokeStyle = "rgba(255, 255, 255, 0.7)";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.arc(cx, cy, r, 0, Math.PI * 2);
      ctx.stroke();

      // MODE SPECIFIC RENDERING
      if (currentMode16 === 4) {
        // MODE 4: INEQUALITY sin(theta) < cos(theta) <=> y < x
        // Draw line y = x
        ctx.strokeStyle = "#f43f5e";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        const lineExtent = r * 1.3;
        ctx.moveTo(cx - lineExtent, cy + lineExtent);
        ctx.lineTo(cx + lineExtent, cy - lineExtent);
        ctx.stroke();

        ctx.fillStyle = "#f43f5e";
        ctx.font = "bold 14px 'Consolas', monospace";
        ctx.fillText("y = x", cx + lineExtent + 8, cy - lineExtent);

        // Highlight below-region (y < x) on circle
        ctx.strokeStyle = "#facc15";
        ctx.lineWidth = 7;

        // Arc 1: 0 to 45 deg (-0 to -45 deg in canvas radians)
        ctx.beginPath();
        ctx.arc(cx, cy, r, -Math.PI / 4, 0, false);
        ctx.stroke();

        // Arc 2: 225 to 360 deg
        ctx.beginPath();
        ctx.arc(cx, cy, r, 0, -5 * Math.PI / 4, false);
        ctx.stroke();

        // Dots at intersections 45 deg and 225 deg
        const p45x = cx + r * Math.SQRT1_2;
        const p45y = cy - r * Math.SQRT1_2;
        const p225x = cx - r * Math.SQRT1_2;
        const p225y = cy + r * Math.SQRT1_2;

        ctx.fillStyle = "#facc15";
        ctx.beginPath(); ctx.arc(p45x, p45y, 6, 0, Math.PI * 2); ctx.fill();
        ctx.beginPath(); ctx.arc(p225x, p225y, 6, 0, Math.PI * 2); ctx.fill();

        ctx.fillText("45° (π/4)", p45x + 10, p45y - 5);
        ctx.fillText("225° (5π/4)", p225x - 85, p225y + 15);

        // Explanatory badge
        ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
        ctx.fillRect(w * 0.65, 30, w * 0.32, 220);
        ctx.strokeStyle = "#facc15";
        ctx.strokeRect(w * 0.65, 30, w * 0.32, 220);

        ctx.fillStyle = "#facc15";
        ctx.font = "bold 15px sans-serif";
        ctx.fillText("부등식 sin θ < cos θ 판정", w * 0.67, 60);

        ctx.fillStyle = "#e2e8f0";
        ctx.font = "13px 'Consolas', monospace";
        ctx.fillText("1) sin θ = y, cos θ = x 대입", w * 0.67, 95);
        ctx.fillText("2) y < x (직선 y = x 의 아래)", w * 0.67, 125);
        ctx.fillText("3) 단위원 둘레 중 노란 호 영역:", w * 0.67, 155);

        ctx.fillStyle = "#4ade80";
        ctx.font = "bold 14px 'Consolas', monospace";
        ctx.fillText("0 ≤ θ < π/4 (0° ~ 45°)", w * 0.67, 190);
        ctx.fillText("5π/4 < θ < 2π (225° ~ 360°)", w * 0.67, 220);
      }

      if (currentMode16 === 2) {
        // MODE 2: NEGATIVE ANGLE (-theta, x-axis symmetry)
        const qy = cy + r * sinVal; // mirrored across x-axis
        ctx.strokeStyle = "rgba(244, 63, 94, 0.5)";
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(px, py);
        ctx.lineTo(px, qy);
        ctx.stroke();
        ctx.setLineDash([]);

        // Ray to Q
        ctx.strokeStyle = "#f43f5e";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(px, qy);
        ctx.stroke();

        // Dot Q
        ctx.fillStyle = "#f43f5e";
        ctx.beginPath(); ctx.arc(px, qy, 6, 0, Math.PI * 2); ctx.fill();
        ctx.font = "bold 13px 'Consolas', monospace";
        ctx.fillText("Q(cos(-θ), sin(-θ))", px + 10, qy + 16);
        ctx.fillText(`= (${cosVal.toFixed(2)}, ${(-sinVal).toFixed(2)})`, px + 10, qy + 34);

        // Explanation panel
        ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
        ctx.fillRect(w * 0.65, 30, w * 0.32, 190);
        ctx.strokeStyle = "#f43f5e";
        ctx.strokeRect(w * 0.65, 30, w * 0.32, 190);

        ctx.fillStyle = "#f43f5e";
        ctx.font = "bold 15px sans-serif";
        ctx.fillText("음각 공식 (-θ, x축 대칭)", w * 0.67, 60);

        ctx.fillStyle = "#e2e8f0";
        ctx.font = "13px 'Consolas', monospace";
        ctx.fillText("• cos(-θ) = cos θ (x좌표 불변)", w * 0.67, 95);
        ctx.fillText("• sin(-θ) = -sin θ (y좌표 반전)", w * 0.67, 130);
        ctx.fillText("• tan(-θ) = -tan θ (기울기 반전)", w * 0.67, 165);
      }

      if (currentMode16 === 3) {
        // MODE 3: PI - THETA (y-axis symmetry)
        const rx = cx - r * cosVal; // mirrored across y-axis
        ctx.strokeStyle = "rgba(234, 179, 8, 0.5)";
        ctx.setLineDash([4, 4]);
        ctx.beginPath();
        ctx.moveTo(px, py);
        ctx.lineTo(rx, py);
        ctx.stroke();
        ctx.setLineDash([]);

        // Ray to R
        ctx.strokeStyle = "#facc15";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(rx, py);
        ctx.stroke();

        // Dot R
        ctx.fillStyle = "#facc15";
        ctx.beginPath(); ctx.arc(rx, py, 6, 0, Math.PI * 2); ctx.fill();
        ctx.font = "bold 13px 'Consolas', monospace";
        ctx.fillText("R(cos(π-θ), sin(π-θ))", rx - 180, py - 10);
        ctx.fillText(`= (${(-cosVal).toFixed(2)}, ${sinVal.toFixed(2)})`, rx - 180, py + 10);

        // Explanation panel
        ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
        ctx.fillRect(w * 0.65, 30, w * 0.32, 190);
        ctx.strokeStyle = "#facc15";
        ctx.strokeRect(w * 0.65, 30, w * 0.32, 190);

        ctx.fillStyle = "#facc15";
        ctx.font = "bold 15px sans-serif";
        ctx.fillText("각변환 공식 (π - θ, y축 대칭)", w * 0.67, 60);

        ctx.fillStyle = "#e2e8f0";
        ctx.font = "13px 'Consolas', monospace";
        ctx.fillText("• sin(π-θ) = sin θ (높이 동일!)", w * 0.67, 95);
        ctx.fillText("• cos(π-θ) = -cos θ (x좌표 반전)", w * 0.67, 130);
        ctx.fillText("• tan(π-θ) = -tan θ (기울기 반전)", w * 0.67, 165);
      }

      // Draw Main Angle Arc
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.arc(cx, cy, 35, 0, -rad, true);
      ctx.stroke();

      // Main Ray OP
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(px, py);
      ctx.stroke();

      // Coordinate Projections: cos (horizontal blue) & sin (vertical green)
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3.5;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(px, cy);
      ctx.stroke();

      ctx.strokeStyle = "#4ade80";
      ctx.lineWidth = 3.5;
      ctx.beginPath();
      ctx.moveTo(px, cy);
      ctx.lineTo(px, py);
      ctx.stroke();

      // Dot P
      ctx.fillStyle = "#facc15";
      ctx.beginPath();
      ctx.arc(px, py, 7, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 2;
      ctx.stroke();

      // Point P Label
      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 14px 'Consolas', monospace";
      ctx.fillText(`P(cos θ, sin θ)`, px + 10, py - 10);
      ctx.font = "12px 'Consolas', monospace";
      ctx.fillStyle = "#cbd5e1";
      ctx.fillText(`= (${cosVal.toFixed(3)}, ${sinVal.toFixed(3)})`, px + 10, py + 8);

      if (currentMode16 === 1) {
        // Definition mode side info
        ctx.fillStyle = "rgba(15, 23, 42, 0.9)";
        ctx.fillRect(w * 0.65, 30, w * 0.32, 210);
        ctx.strokeStyle = "#38bdf8";
        ctx.strokeRect(w * 0.65, 30, w * 0.32, 210);

        ctx.fillStyle = "#38bdf8";
        ctx.font = "bold 15px sans-serif";
        ctx.fillText("단위원 위의 점 P 정의", w * 0.67, 60);

        ctx.fillStyle = "#38bdf8";
        ctx.font = "13px 'Consolas', monospace";
        ctx.fillText(`• cos θ (x좌표) = ${cosVal.toFixed(3)}`, w * 0.67, 95);

        ctx.fillStyle = "#4ade80";
        ctx.fillText(`• sin θ (y좌표) = ${sinVal.toFixed(3)}`, w * 0.67, 130);

        ctx.fillStyle = "#f43f5e";
        ctx.fillText(`• tan θ (기울기) = ${Math.abs(cosVal) < 1e-4 ? "무한대" : tanVal.toFixed(3)}`, w * 0.67, 165);

        ctx.fillStyle = "#facc15";
        ctx.fillText(`• cos²θ + sin²θ = 1.000`, w * 0.67, 200);
      }
    }

    function initCanvasInteractions16() {
      const canvas = document.getElementById("canvasUnitCircle16");
      if (!canvas) return;

      function handleMove(e) {
        const rect = canvas.getBoundingClientRect();
        const clientX = e.clientX || (e.touches && e.touches[0].clientX);
        const clientY = e.clientY || (e.touches && e.touches[0].clientY);
        if (clientX === undefined) return;

        const mx = (clientX - rect.left) * (canvas.width / rect.width);
        const my = (clientY - rect.top) * (canvas.height / rect.height);

        const cx = canvas.width * 0.42;
        const cy = canvas.height * 0.5;

        const dx = mx - cx;
        const dy = -(my - cy); // flip y

        let angleRad = Math.atan2(dy, dx);
        if (angleRad < 0) angleRad += 2 * Math.PI;

        const angleDeg = angleRad * 180 / Math.PI;
        setAngle16(angleDeg);
      }

      canvas.addEventListener("mousedown", (e) => {
        isDraggingUnitCircle16 = true;
        handleMove(e);
      });

      window.addEventListener("mousemove", (e) => {
        if (isDraggingUnitCircle16) {
          handleMove(e);
        }
      });

      window.addEventListener("mouseup", () => {
        isDraggingUnitCircle16 = false;
      });

      canvas.addEventListener("touchstart", (e) => {
        isDraggingUnitCircle16 = true;
        handleMove(e);
      }, { passive: true });

      window.addEventListener("touchmove", (e) => {
        if (isDraggingUnitCircle16) {
          handleMove(e);
        }
      }, { passive: true });

      window.addEventListener("touchend", () => {
        isDraggingUnitCircle16 = false;
      });
    }

    function switchL16Tab(tabIdx) {
      for (let i = 1; i <= 6; i++) {
        const btn = document.getElementById(`tabBtnL16_${i}`);
        const content = document.getElementById(`tabL16_${i}`);
        if (btn) btn.classList.toggle("active", i === tabIdx);
        if (content) content.style.display = (i === tabIdx) ? "block" : "none";
      }
      if (window.MathJax && MathJax.typesetPromise) {
        MathJax.typesetPromise();
      }
    }

    function copyManimCode16() {
      const codeEl = document.querySelector("#manimPre16 code");
      if (codeEl) {
        navigator.clipboard.writeText(codeEl.innerText).then(() => {
          alert("Manim 파이썬 코드가 클립보드에 복사되었습니다!");
        }).catch(() => {
          alert("복사 실패. 텍스트를 직접 선택해 복사해주세요.");
        });
      }
    }

    function renderL16() {
      updateL16();
      initCanvasInteractions16();
      if (window.MathJax && MathJax.typesetPromise) {
        MathJax.typesetPromise();
      }
    }
'''

    # Insert Lecture 16 JS before Lecture 15 JS
    idx_js15 = html.find('// ==============================================================')
    if idx_js15 != -1:
        html = html[:idx_js15] + js_code_16 + '\n' + html[idx_js15:]
        print("Inserted Lecture 16 JavaScript.")

    # 5. Update setLecture loop from 15 to 16
    html = html.replace('for (let i = 1; i <= 15; i++)', 'for (let i = 1; i <= 16; i++)')
    print("Updated setLecture loop to 16.")

    # Add num === 16 render handler
    old_l15_check = 'if (num === 15) setTimeout(renderL15, 50);'
    new_l16_check = 'if (num === 16) setTimeout(renderL16, 50);\n      else if (num === 15) setTimeout(renderL15, 50);'
    html = html.replace(old_l15_check, new_l16_check, 1)
    print("Added num === 16 render handler to setLecture.")

    # Update window load handler
    html = html.replace('setLecture(15);', 'setLecture(16);')
    html = html.replace('setTimeout(renderL15, 200);', 'setTimeout(renderL16, 200);')
    print("Updated window load handler to initialize Lecture 16.")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html successfully updated with Lecture 16!")

if __name__ == '__main__':
    main()
