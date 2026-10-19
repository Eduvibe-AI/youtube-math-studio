# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: Exponential & Logarithmic Functions Fast Review
Topic: Lecture 31 - Pre-CSAT Concept Summary for Exp & Log Functions
Run with: manim -pql exp_log_quick_summary_manim.py ExpLogQuickScene
"""

from manim import *
import numpy as np

class ExpLogQuickScene(Scene):
    def construct(self):
        # 1. Title
        title = Title(
            r"지수함수와 로그함수: 수능 직전 20초 개념 요약",
            include_underline=True,
            font_size=32
        )
        subtitle = Text(
            "밑의 범위(a > 1 vs 0 < a < 1), 점근선, 정점 및 y = x 역함수 대칭 구조",
            font_size=18,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. Graph Axes
        axes = Axes(
            x_range=[-3, 4, 1],
            y_range=[-3, 4, 1],
            x_length=5.5,
            y_length=5.5,
            axis_config={"color": GRAY}
        ).to_edge(LEFT, buff=0.8)

        # y = x dashed
        line_diag = axes.plot(lambda x: x, color=GRAY_B, stroke_opacity=0.6)

        # y = 2^x
        g_exp = axes.plot(lambda x: 2**x, x_range=[-3, 2], color=CYAN)
        dot_exp = Dot(axes.c2p(0, 1), color=YELLOW, radius=0.07)
        lbl_exp = MathTex(r"y = 2^x", color=CYAN, font_size=17).next_to(axes.c2p(1.5, 2.8), RIGHT)

        # y = log2(x)
        g_log = axes.plot(lambda x: np.log2(x), x_range=[0.125, 4], color=GOLD)
        dot_log = Dot(axes.c2p(1, 0), color=YELLOW, radius=0.07)
        lbl_log = MathTex(r"y = \log_2 x", color=GOLD, font_size=17).next_to(axes.c2p(3.5, np.log2(3.5)), DOWN)

        self.play(Create(axes), Create(line_diag))
        self.play(Create(g_exp), FadeIn(dot_exp), Write(lbl_exp))
        self.play(Create(g_log), FadeIn(dot_log), Write(lbl_log))
        self.wait(1)

        # 3. Fast Checklist Board
        board = VGroup(
            Text("★ 수능 시험장 3대 체크포인트", font_size=19, color=GOLD),
            MathTex(r"1.\; a > 1 \implies \text{증가함수 (우상향)}", font_size=17, color=WHITE),
            MathTex(r"2.\; 0 < a < 1 \implies \text{감소함수 (우하향)}", font_size=17, color=WHITE),
            MathTex(r"3.\; \text{지수함수 점근선: } y = 0 \text{ (x축)}, \quad \text{정점 } (0, 1)", font_size=16, color=CYAN),
            MathTex(r"4.\; \text{로그함수 점근선: } x = 0 \text{ (y축)}, \quad \text{정점 } (1, 0)", font_size=16, color=GOLD),
            MathTex(r"5.\; y = x \text{ 대칭 } \iff \text{서로 역함수 관계}", font_size=18, color=RED_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.6)

        rect = SurroundingRectangle(board, color=PURPLE_D, fill_color=BLACK, fill_opacity=0.88, buff=0.25)
        self.play(FadeIn(rect), Write(board))
        self.wait(2.5)
