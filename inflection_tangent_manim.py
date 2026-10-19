"""
변곡접선 (Inflection Tangent) 완전 정리
3Blue1Brown 스타일 Manim 애니메이션 스크립트

실행 방법:
manim -pql inflection_tangent_manim.py InflectionTangentScene
"""

from manim import *
import numpy as np

class InflectionTangentScene(Scene):
    def construct(self):
        # 1. 메인 타이틀
        title = Title("삼차함수 변곡접선의 기하학적 성질 & 접선의 개수", include_underline=True)
        title.set_color(YELLOW)
        subtitle = Text("오목과 볼록이 바뀌는 변곡점에서의 유일무이한 관통 접선", font_size=20, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        # 2. 좌표축 설정
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6.5,
            y_length=5.5,
            axis_config={"color": BLUE_C, "include_numbers": True},
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.3)

        # 3. 삼차함수 그래프 f(x) = (x^3 - 3x) / 2
        def f(x):
            return (x**3 - 3*x) / 2.0

        curve = axes.plot(f, x_range=[-2.4, 2.4], color=TEAL, stroke_width=4)
        curve_label = MathTex(r"f(x) = \frac{1}{2}(x^3 - 3x)", font_size=30, color=TEAL).next_to(axes.c2p(1.8, 2.0), RIGHT)

        self.play(Create(axes), Create(curve), Write(curve_label))
        self.wait(1)

        # 4. 변곡점 (0, 0) 표시
        inf_dot = Dot(axes.c2p(0, 0), color=RED, radius=0.1)
        inf_label = MathTex(r"\text{변곡점 } (0, 0) \; [f''(x)=0]", font_size=28, color=RED).next_to(inf_dot, UP + RIGHT, buff=0.2)

        self.play(FadeIn(inf_dot), Write(inf_label))
        self.wait(1)

        # 5. 변곡접선 그리기 (f'(0) = -1.5 => y = -1.5x)
        def tangent_f(x):
            return -1.5 * x

        inf_tangent = axes.plot(tangent_f, x_range=[-1.8, 1.8], color=YELLOW, stroke_width=3.5)
        tangent_label = MathTex(r"\text{변곡접선 } y = -\frac{3}{2}x", font_size=28, color=YELLOW).next_to(axes.c2p(-1.4, 2.1), UP)

        self.play(Create(inf_tangent), Write(tangent_label))
        self.wait(1)

        # 6. 관통(Crossing) 설명 카드 (우측 상단)
        card1 = VGroup(
            Text("성질 1: 기하학적 관통", font_size=24, color=WHITE, weight=BOLD),
            MathTex(r"x < 0 : \text{위로 볼록 } (f'' < 0) \implies \text{접선이 위}", font_size=24, color=GRAY_A),
            MathTex(r"x > 0 : \text{아래로 볼록 } (f'' > 0) \implies \text{접선이 아래}", font_size=24, color=GRAY_A),
            Text("접선이 곡선을 꿰뚫고 관통함!", font_size=24, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_edge(RIGHT, buff=0.8).shift(UP * 1.0)

        self.play(FadeIn(card1))
        self.wait(2)

        # 7. 대수적 삼중근 카드 (우측 중단)
        card2 = VGroup(
            Text("성질 2: 대수적 삼중근", font_size=24, color=WHITE, weight=BOLD),
            MathTex(r"f(x) - g(x) = \frac{1}{2}x^3 = 0", font_size=28, color=BLUE_B),
            MathTex(r"\implies x = 0 \text{ (삼중근, Triple Root)}", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(card1, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(FadeIn(card2))
        self.wait(2)

        # 8. 접선의 개수 영역 판별 (수능 킬러)
        self.play(FadeOut(card1), FadeOut(card2))

        tangent_count_title = Text("성질 3: 접선의 개수 영역 판별", font_size=24, color=GOLD, weight=BOLD).to_edge(RIGHT, buff=0.8).shift(UP * 1.5)
        
        region3_label = MathTex(r"\text{곡선과 접선 사이 : } \mathbf{3\text{개}}", font_size=26, color=GREEN).next_to(tangent_count_title, DOWN, buff=0.35, aligned_edge=LEFT)
        region2_label = MathTex(r"\text{경계선(곡선·접선 위) : } \mathbf{2\text{개}}", font_size=26, color=YELLOW).next_to(region3_label, DOWN, buff=0.25, aligned_edge=LEFT)
        region1_label = MathTex(r"\text{바깥 영역 & 변곡점 : } \mathbf{1\text{개}}", font_size=26, color=RED).next_to(region2_label, DOWN, buff=0.25, aligned_edge=LEFT)

        card3 = VGroup(tangent_count_title, region3_label, region2_label, region1_label)
        self.play(FadeIn(card3))

        # 외부 점 P (0.5, 0.5)에서 3개의 접선 그리기 예시
        p_pt = axes.c2p(0.5, 0.5)
        p_dot = Dot(p_pt, color=GREEN, radius=0.08)
        p_label = MathTex(r"P", font_size=26, color=GREEN).next_to(p_dot, UP + RIGHT, buff=0.1)

        self.play(FadeIn(p_dot), Write(p_label))

        # 점 P에서 삼차곡선으로 뻗어나가는 3개의 접선
        # f(x) 접점 3개
        t_vals = [-1.43, -0.32, 1.75]
        t_lines = VGroup()
        for t in t_vals:
            t_pt = axes.c2p(t, f(t))
            line = Line(p_pt, t_pt, color=GREEN_B, stroke_width=2.5)
            dot = Dot(t_pt, color=GREEN_A, radius=0.06)
            t_lines.add(line, dot)

        self.play(Create(t_lines))
        self.wait(2)

        # 마무리 메시지
        conclusion = Text("변곡접선은 수능 킬러문항 접선 개수 판별의 절대 기준선!", font_size=22, color=YELLOW)
        conclusion.next_to(axes, DOWN, buff=0.35)
        self.play(Write(conclusion))
        self.wait(2)
