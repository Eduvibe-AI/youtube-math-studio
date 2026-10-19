# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: Triangle Geometry - The Inevitable Thinking Process
Topic: 2024 CSAT Math #13 In-Depth Analysis (Sine & Cosine Rule Decision Matrix)
Run with: manim -pql sine_cosine_rule_necessity_manim.py SineCosineNecessityScene
"""

from manim import *
import numpy as np

class SineCosineNecessityScene(Scene):
    def construct(self):
        # 1. Title
        title = Title(
            r"도형 문제를 풀 때 최상위권들이 \textquotedblleft 반드시\textquotedblright\ 하는 생각",
            include_underline=True,
            font_size=30
        )
        subtitle = Text(
            "2024 수능 13번 심층 분석: 공통선분과 미지수 선택의 필연성",
            font_size=19,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. Geometric Diagram Setup (Triangle ABC and Adjacent Triangle ACD)
        # B at origin (0,0), A at (3*cos(60), 3*sin(60)) = (1.5, 3*sqrt(3)/2)
        # C at (4, 0)
        # AB = 3, BC = 4, AC = sqrt(9 + 16 - 2*3*4*0.5) = sqrt(25 - 12) = sqrt(13)
        scale = 0.9
        pB = np.array([-2.5, -1.0, 0])
        pA = pB + np.array([3.0 * np.cos(np.pi / 3), 3.0 * np.sin(np.pi / 3), 0]) * scale
        pC = pB + np.array([4.0, 0, 0]) * scale
        pD = pC + np.array([1.8, 2.2, 0]) * scale

        # Vertices & Labels
        dotB = Dot(pB, color=WHITE, radius=0.07)
        dotA = Dot(pA, color=YELLOW, radius=0.07)
        dotC = Dot(pC, color=GREEN, radius=0.07)
        dotD = Dot(pD, color=CYAN, radius=0.07)

        lblB = MathTex(r"B", font_size=20).next_to(dotB, DOWN+LEFT, buff=0.1)
        lblA = MathTex(r"A", font_size=20).next_to(dotA, UP, buff=0.1)
        lblC = MathTex(r"C", font_size=20).next_to(dotC, DOWN, buff=0.1)
        lblD = MathTex(r"D", font_size=20).next_to(dotD, UP+RIGHT, buff=0.1)

        # Edges
        edge_AB = Line(pB, pA, color=BLUE_B, stroke_width=3)
        edge_BC = Line(pB, pC, color=GOLD, stroke_width=3.5) # Common segment x = 4
        edge_AC = Line(pA, pC, color=RED_B, stroke_width=3)   # Length sqrt(13)
        edge_CD = Line(pC, pD, color=CYAN, stroke_width=2.5)
        edge_AD = Line(pA, pD, color=CYAN, stroke_width=2.5)

        # Angle at B = pi/3
        angle_B = Angle(edge_BC, edge_AB, radius=0.45, color=YELLOW)
        lbl_angle_B = MathTex(r"\frac{\pi}{3}", color=YELLOW, font_size=18).next_to(angle_B, UP+RIGHT, buff=0.05)

        # Length labels
        lbl_len_AB = MathTex(r"3", color=BLUE_B, font_size=18).next_to(edge_AB.get_center(), UP+LEFT, buff=0.1)
        lbl_len_AC = MathTex(r"\sqrt{13}", color=RED_B, font_size=18).next_to(edge_AC.get_center(), UP+RIGHT, buff=0.1)
        lbl_len_BC = MathTex(r"x = \overline{BC}", color=GOLD, font_size=18).next_to(edge_BC.get_center(), DOWN, buff=0.15)

        tri_group = VGroup(
            edge_AB, edge_BC, edge_AC, edge_CD, edge_AD,
            dotB, dotA, dotC, dotD,
            lblB, lblA, lblC, lblD,
            angle_B, lbl_angle_B,
            lbl_len_AB, lbl_len_AC, lbl_len_BC
        ).to_edge(LEFT, buff=0.8)

        self.play(Create(edge_AB), Create(edge_BC), Create(edge_AC), FadeIn(dotA, dotB, dotC), Write(VGroup(lblA, lblB, lblC)))
        self.play(Create(angle_B), Write(lbl_angle_B), Write(lbl_len_AB), Write(lbl_len_AC), Write(lbl_len_BC))
        self.wait(1)

        # 3. Deriving Cosine Rule with non-included angle
        math_steps = VGroup(
            Text("★ 1단계: 비끼인각 코사인 법칙의 필연성", font_size=18, color=GOLD),
            MathTex(r"(\sqrt{13})^2 = 3^2 + x^2 - 2 \cdot 3 \cdot x \cdot \cos\left(\frac{\pi}{3}\right)", font_size=17),
            MathTex(r"13 = 9 + x^2 - 3x", font_size=17, color=BLUE_B),
            MathTex(r"x^2 - 3x - 4 = 0", font_size=18, color=YELLOW),
            MathTex(r"(x - 4)(x + 1) = 0 \implies x = 4", font_size=18, color=GREEN_B),
            Text("★ 2단계: 공통선분 결정 후 도미노 연쇄 해결", font_size=18, color=GOLD),
            MathTex(r"\overline{BC} = 4 \text{ 가 확정되며 인접 삼각형 정보 100\% 복원!}", font_size=16, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.6)

        bg_card = SurroundingRectangle(math_steps, color=BLUE_E, fill_color=BLACK, fill_opacity=0.88, buff=0.25)

        self.play(FadeIn(bg_card), Write(math_steps[:5]))
        self.wait(1.5)

        # Show adjacent triangle
        self.play(Create(edge_CD), Create(edge_AD), FadeIn(dotD), Write(lblD), Write(math_steps[5:]))
        self.wait(3)
