# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: The Law of Cosines Geometry & Intuition
Topic: Lecture 30 - Law of Cosines Principles & Decision Matrix
Run with: manim -pql cosine_rule_geometry_manim.py CosineRuleScene
"""

from manim import *
import numpy as np

class CosineRuleScene(Scene):
    def construct(self):
        # 1. Title
        title = Title(
            r"삼각함수의 활용: 코사인법칙의 원리와 기하학적 직관",
            include_underline=True,
            font_size=30
        )
        subtitle = Text(
            "피타고라스 정리의 일반화: a² = b² + c² - 2bc cos A 의 증명과 실전 활용",
            font_size=18,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. Geometric Triangle Setup
        pC = np.array([-2.5, -1.0, 0])
        pA = pC + np.array([2.0, 2.5, 0])
        pB = pC + np.array([4.5, 0, 0])
        pH = np.array([pA[0], pC[1], 0])

        dotC = Dot(pC, color=WHITE, radius=0.07)
        dotA = Dot(pA, color=YELLOW, radius=0.07)
        dotB = Dot(pB, color=GREEN, radius=0.07)
        dotH = Dot(pH, color=GRAY, radius=0.05)

        lblC = MathTex(r"C", font_size=18).next_to(dotC, DOWN+LEFT, buff=0.1)
        lblA = MathTex(r"A", font_size=18).next_to(dotA, UP, buff=0.1)
        lblB = MathTex(r"B", font_size=18).next_to(dotB, DOWN+RIGHT, buff=0.1)

        side_b = Line(pA, pC, color=BLUE_B, stroke_width=3) # b
        side_c = Line(pA, pB, color=GOLD, stroke_width=3)   # c
        side_a = Line(pB, pC, color=RED_B, stroke_width=3)  # a
        alt_h = DashedLine(pA, pH, color=GRAY, stroke_width=2) # h = b sin C

        tri_group = VGroup(side_b, side_c, side_a, alt_h, dotC, dotA, dotB, dotH, lblC, lblA, lblB).to_edge(LEFT, buff=0.8)

        self.play(Create(side_b), Create(side_c), Create(side_a), FadeIn(dotA, dotB, dotC), Write(VGroup(lblA, lblB, lblC)))
        self.play(Create(alt_h), FadeIn(dotH))
        self.wait(1)

        # 3. Formulas Board
        board = VGroup(
            Text("★ 코사인법칙 2대 핵심 수식", font_size=19, color=GOLD),
            MathTex(r"\text{1. 길이 산출형 (표준형): } a^2 = b^2 + c^2 - 2bc \cos A", font_size=17, color=CYAN),
            MathTex(r"\text{2. 각도 산출형 (변형형): } \cos A = \frac{b^2 + c^2 - a^2}{2bc}", font_size=17, color=YELLOW),
            Text("★ 삼각형 결정 3대 상황", font_size=19, color=GOLD),
            MathTex(r"\text{Case 1: 두 변과 끼인각(SAS) } \implies \text{대변 길이 확정}", font_size=16, color=WHITE),
            MathTex(r"\text{Case 2: 세 변의 길이(SSS) } \implies \text{모든 각도 산출}", font_size=16, color=WHITE),
            MathTex(r"\text{Case 3: 피타고라스 정리는 } A = 90^\circ \text{ 의 특수 케이스!}", font_size=16, color=GREEN_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.6)

        rect = SurroundingRectangle(board, color=BLUE_D, fill_color=BLACK, fill_opacity=0.88, buff=0.25)
        self.play(FadeIn(rect), Write(board))
        self.wait(2.5)
