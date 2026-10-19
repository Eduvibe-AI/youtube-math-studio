# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: Taylor & Maclaurin Series Approximation
Topic: Lecture 26 - Transcendental Function Polynomial Approximation
Run with: manim -pql taylor_series_approximation_manim.py TaylorSeriesScene
"""

from manim import *
import numpy as np

class TaylorSeriesScene(Scene):
    def construct(self):
        # 1. Title
        title = Title(
            r"테일러 급수: 초월함수의 다항함수 근사 원리",
            include_underline=True,
            font_size=32
        )
        subtitle = Text(
            "미분 계수를 일치시켜 복잡한 초월함수(e^x, sin x, cos x)를 다항식으로 포개는 마법",
            font_size=18,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. Function Graph Comparison (Axes)
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-2.5, 4.5, 1],
            x_length=6,
            y_length=5,
            axis_config={"color": GRAY}
        ).to_edge(LEFT, buff=0.6)

        # e^x and its approximations
        graph_exp = axes.plot(lambda x: np.exp(x), x_range=[-3, 1.5], color=WHITE)
        lbl_exp = MathTex(r"y = e^x", color=WHITE, font_size=18).next_to(axes.c2p(1.2, np.exp(1.2)), UP+LEFT, buff=0.1)

        p1 = axes.plot(lambda x: 1 + x, x_range=[-2.5, 2.5], color=BLUE)
        lbl_p1 = MathTex(r"P_1(x) = 1 + x", color=BLUE, font_size=16).next_to(axes.c2p(2, 3), RIGHT, buff=0.1)

        p2 = axes.plot(lambda x: 1 + x + 0.5 * x**2, x_range=[-2.5, 2.0], color=YELLOW)
        lbl_p2 = MathTex(r"P_2(x) = 1 + x + \frac{x^2}{2!}", color=YELLOW, font_size=16).next_to(axes.c2p(1.8, 4), UP, buff=0.1)

        self.play(Create(axes), Create(graph_exp), Write(lbl_exp))
        self.wait(1)
        self.play(Create(p1), Write(lbl_p1))
        self.wait(1)
        self.play(Create(p2), Write(lbl_p2))
        self.wait(1)

        # 3. Formula Derivation Board
        board = VGroup(
            Text("★ 매클로린 급수 (x=0 중심 전개)", font_size=20, color=GOLD),
            MathTex(r"f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n", font_size=19, color=WHITE),
            MathTex(r"e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots", font_size=17, color=CYAN),
            MathTex(r"\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots \text{ (홀수차)}", font_size=17, color=GREEN_B),
            MathTex(r"\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots \text{ (짝수차)}", font_size=17, color=YELLOW),
            Text("★ 오일러 공식의 탄생", font_size=19, color=GOLD),
            MathTex(r"e^{ix} = \cos x + i\sin x", font_size=22, color=RED_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.6)

        rect = SurroundingRectangle(board, color=BLUE_D, fill_color=BLACK, fill_opacity=0.88, buff=0.25)
        self.play(FadeIn(rect), Write(board))
        self.wait(2.5)
