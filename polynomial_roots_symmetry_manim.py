# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: Polynomial Graph Insight - Contact Orders & Symmetry
Topic: Lecture 27 - Polynomial Function Roots, Ratio Relations & Symmetry
Run with: manim -pql polynomial_roots_symmetry_manim.py PolynomialInsightScene
"""

from manim import *
import numpy as np

class PolynomialInsightScene(Scene):
    def construct(self):
        # 1. Title
        title = Title(
            r"다항함수를 보는 눈: 인수(접촉 차수)와 기하학적 대칭성",
            include_underline=True,
            font_size=30
        )
        subtitle = Text(
            "미분 계산보다 개형을 먼저 결정하는 8칸 박스법과 2:1 접선 비율의 원리",
            font_size=18,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. Cubic Graph and 8-Box Method
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=5,
            axis_config={"color": GRAY}
        ).to_edge(LEFT, buff=0.6)

        # f(x) = x^3 - 3x (roots at -sqrt(3), 0, sqrt(3); local max at -1, y=2; local min at 1, y=-2)
        cubic = axes.plot(lambda x: 0.5 * (x**3 - 3*x), x_range=[-2.4, 2.4], color=YELLOW)
        lbl_cubic = MathTex(r"f(x)", color=YELLOW, font_size=18).next_to(axes.c2p(2, 1), RIGHT)

        # Tangent at max (x = -1, y = 1) -> intersects at x = 2
        tan_max = DashedLine(axes.c2p(-2.5, 1), axes.c2p(2.5, 1), color=BLUE_B)
        dot_max = Dot(axes.c2p(-1, 1), color=RED, radius=0.08)
        dot_cross = Dot(axes.c2p(2, 1), color=GREEN, radius=0.08)
        dot_inflec = Dot(axes.c2p(0, 0), color=WHITE, radius=0.08)

        lbl_max = MathTex(r"\text{극대 } x=-1", font_size=16, color=RED).next_to(dot_max, UP, buff=0.1)
        lbl_inf = MathTex(r"\text{변곡점 } x=0", font_size=16, color=WHITE).next_to(dot_inflec, DOWN+RIGHT, buff=0.1)
        lbl_cross = MathTex(r"\text{교점 } x=2", font_size=16, color=GREEN).next_to(dot_cross, UP, buff=0.1)

        # Ratio bracket: length 1 vs length 2 -> 2:1
        ratio_lbl = MathTex(r"2 : 1 \text{ 비율 분할}", color=GOLD, font_size=19).next_to(tan_max, UP, buff=0.2)

        self.play(Create(axes), Create(cubic), Write(lbl_cubic))
        self.play(Create(tan_max), FadeIn(dot_max, dot_inflec, dot_cross), Write(VGroup(lbl_max, lbl_inf, lbl_cross)))
        self.play(Write(ratio_lbl))
        self.wait(1.5)

        # 3. Key Formulas Board
        board = VGroup(
            Text("★ 삼차함수 핵심 비율 공식", font_size=19, color=GOLD),
            MathTex(r"\text{변곡점 기준: } 1 : 1 : 1 \text{ 대칭 분할}", font_size=17, color=CYAN),
            MathTex(r"\text{극대/극소 접선: } 2 : 1 \text{ 내분점 원리}", font_size=17, color=GREEN_B),
            MathTex(r"\text{극값 높이차: } \Delta y = \frac{|a|}{2} L^3", font_size=19, color=YELLOW),
            Text("★ 인수 접촉 차수 (Contact Order)", font_size=19, color=GOLD),
            MathTex(r"(x-\alpha)^1 \implies \text{단순 관통 (Cross)}", font_size=16, color=WHITE),
            MathTex(r"(x-\alpha)^2 \implies \text{포물선 접함 (Bounce)}", font_size=16, color=WHITE),
            MathTex(r"(x-\alpha)^3 \implies \text{변곡 관통 접선 (Inflection)}", font_size=16, color=RED_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.6)

        rect = SurroundingRectangle(board, color=YELLOW_E, fill_color=BLACK, fill_opacity=0.88, buff=0.25)
        self.play(FadeIn(rect), Write(board))
        self.wait(2.5)
