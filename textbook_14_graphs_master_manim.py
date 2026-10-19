# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: 14 High School Textbook Graphs Master Tree
Topic: Lecture 28 - Complete Classification and Geometric Properties
Run with: manim -pql textbook_14_graphs_master_manim.py Textbook14GraphsScene
"""

from manim import *
import numpy as np

class Textbook14GraphsScene(Scene):
    def construct(self):
        # 1. Title
        title = Title(
            r"대한민국 고교 교과서 14대 그래프 총정리",
            include_underline=True,
            font_size=32
        )
        subtitle = Text(
            "다항함수부터 초월함수, 이차곡선까지 수능에 출제되는 모든 곡선의 계통도",
            font_size=18,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. 4 Main Families
        col1 = VGroup(
            Text("[1] 다항함수 4형제", font_size=19, color=GOLD),
            Text("1. 1차함수: y = ax + b (기울기와 절편)", font_size=16),
            Text("2. 2차함수: y = ax² + bx + c (축 대칭)", font_size=16),
            Text("3. 3차함수: 점대칭 변곡점과 2:1 비율", font_size=16),
            Text("4. 4차함수: 이중접선 및 선대칭 W형", font_size=16),
            Text("[2] 분수/무리함수", font_size=19, color=GOLD),
            Text("5. 유리함수: y = k/(x-p) + q (점근선 교점)", font_size=16),
            Text("6. 무리함수: y = √(ax+b) + c (시작점과 방향)", font_size=16),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(LEFT, buff=0.6)

        col2 = VGroup(
            Text("[3] 초월함수 패밀리", font_size=19, color=GOLD),
            Text("7. 지수함수: y = aˣ (수평 점근선 y=0)", font_size=16),
            Text("8. 로그함수: y = logₐ x (수직 점근선 x=0)", font_size=16),
            Text("9. 삼각함수: sin, cos, tan (단위원 주기성)", font_size=16),
            Text("[4] 기하 이차곡선 4총사", font_size=19, color=GOLD),
            Text("10. 원: (x-a)² + (y-b)² = r²", font_size=16),
            Text("11. 포물선: y² = 4px (초점과 준선)", font_size=16),
            Text("12. 타원: x²/a² + y²/b² = 1 (거리 합 2a)", font_size=16),
            Text("13. 쌍곡선: x²/a² - y²/b² = ±1 (점근선)", font_size=16),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(RIGHT, buff=0.6)

        bg1 = SurroundingRectangle(col1, color=BLUE_D, fill_color=BLACK, fill_opacity=0.85, buff=0.22)
        bg2 = SurroundingRectangle(col2, color=PURPLE_D, fill_color=BLACK, fill_opacity=0.85, buff=0.22)

        self.play(FadeIn(bg1), Write(col1))
        self.play(FadeIn(bg2), Write(col2))
        self.wait(2.5)
