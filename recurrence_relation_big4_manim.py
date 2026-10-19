# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: Recurrence Relations Big 4 & Alpha Transformation
Topic: Lecture 25 - Sequence Recurrence Relations Master Scene
Run with: manim -pql recurrence_relation_big4_manim.py RecurrenceRelationScene
"""

from manim import *
import numpy as np

class RecurrenceRelationScene(Scene):
    def construct(self):
        # 1. Title
        title = Title(
            r"점화식 25분 아작내기: Big 4 \& \textalpha\ 변환 마스터",
            include_underline=True,
            font_size=32
        )
        subtitle = Text(
            "이웃하는 두 항 사이의 관계식으로부터 일반항 a_n을 단숨에 도출하는 체계",
            font_size=18,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. Big 4 Classification Board
        big4_box = VGroup(
            Text("★ 수열 점화식 기본 Big 4", font_size=20, color=GOLD),
            MathTex(r"\text{Big 1: } a_{n+1} - a_n = d \implies a_n = a_1 + (n-1)d", font_size=17, color=BLUE_B),
            MathTex(r"\text{Big 2: } \frac{a_{n+1}}{a_n} = r \implies a_n = a_1 \cdot r^{n-1}", font_size=17, color=GREEN_B),
            MathTex(r"\text{Big 3: } a_{n+1} = a_n + f(n) \implies a_n = a_1 + \sum_{k=1}^{n-1} f(k)", font_size=17, color=YELLOW),
            MathTex(r"\text{Big 4: } a_{n+1} = f(n) a_n \implies a_n = a_1 \cdot \prod_{k=1}^{n-1} f(k)", font_size=17, color=RED_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(LEFT, buff=0.6)

        rect1 = SurroundingRectangle(big4_box, color=BLUE_E, fill_color=BLACK, fill_opacity=0.85, buff=0.25)
        self.play(FadeIn(rect1), Write(big4_box))
        self.wait(1.5)

        # 3. Alpha Method Derivation (Application 1: a_{n+1} = p a_n + q)
        alpha_box = VGroup(
            Text("★ 실전 1순위: 알파(α) 특성방정식", font_size=20, color=GOLD),
            MathTex(r"a_{n+1} = p \, a_n + q \quad (p \neq 1)", font_size=18, color=WHITE),
            MathTex(r"\text{특성근: } \alpha = p\,\alpha + q \implies \alpha = \frac{q}{1-p}", font_size=17, color=YELLOW),
            MathTex(r"\text{변형: } (a_{n+1} - \alpha) = p\,(a_n - \alpha)", font_size=18, color=GREEN_B),
            MathTex(r"\implies \{a_n - \alpha\} \text{ 는 공비 } p \text{인 등비수열!}", font_size=17, color=CYAN),
            MathTex(r"a_n - \alpha = (a_1 - \alpha)\,p^{n-1}", font_size=18, color=RED_B),
            MathTex(r"\therefore a_n = (a_1 - \alpha)\,p^{n-1} + \alpha", font_size=20, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(RIGHT, buff=0.6)

        rect2 = SurroundingRectangle(alpha_box, color=PURPLE_E, fill_color=BLACK, fill_opacity=0.88, buff=0.25)
        self.play(FadeIn(rect2), Write(alpha_box))
        self.wait(2)
