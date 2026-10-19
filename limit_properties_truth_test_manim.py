# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: Limit Properties Truth Testing via Substitution
Topic: Lecture 29 - Limits of Functions Truth Testing without Counterexamples
Run with: manim -pql limit_properties_truth_test_manim.py LimitTruthTestScene
"""

from manim import *
import numpy as np

class LimitTruthTestScene(Scene):
    def construct(self):
        # 1. Title
        title = Title(
            r"함수의 극한의 성질 진위판단: 반례 없는 치환법 마스터",
            include_underline=True,
            font_size=30
        )
        subtitle = Text(
            "수렴하는 덩어리를 h(x)로 치환하여 단 3초 만에 참/거짓을 판정하는 핵심 알고리즘",
            font_size=18,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. Main Theorems
        rule_box = VGroup(
            Text("★ 극한의 기본 성질 대전제 (교과서 핵심)", font_size=19, color=GOLD),
            MathTex(r"\lim_{x \to a} f(x) = \alpha, \quad \lim_{x \to a} g(x) = \beta \quad (\text{둘 다 수렴할 때만!})", font_size=17, color=CYAN),
            MathTex(r"1.\; \lim [f(x) \pm g(x)] = \alpha \pm \beta", font_size=17, color=WHITE),
            MathTex(r"2.\; \lim [f(x) \cdot g(x)] = \alpha \cdot \beta", font_size=17, color=WHITE),
            MathTex(r"3.\; \lim \frac{f(x)}{g(x)} = \frac{\alpha}{\beta} \quad (\mathbf{\beta \neq 0} \text{ 일 때만 참!})", font_size=17, color=RED_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(LEFT, buff=0.6)

        rect1 = SurroundingRectangle(rule_box, color=BLUE_E, fill_color=BLACK, fill_opacity=0.85, buff=0.25)
        self.play(FadeIn(rect1), Write(rule_box))
        self.wait(1.5)

        # 3. Substitution Method (h(x) technique)
        sub_box = VGroup(
            Text("★ 마법의 치환법 (Substitution Technique)", font_size=19, color=GOLD),
            MathTex(r"\text{조건: } \lim f(x) \text{ 와 } \lim [f(x)+g(x)] \text{ 가 수렴}", font_size=16, color=YELLOW),
            MathTex(r"\text{치환: } f(x) + g(x) = h(x) \implies g(x) = h(x) - f(x)", font_size=17, color=GREEN_B),
            MathTex(r"\lim g(x) = \lim h(x) - \lim f(x) = \text{수렴 } \implies \mathbf{참(True)}", font_size=17, color=CYAN),
            MathTex(r"\text{주의: } \lim [f(x) \cdot g(x)] = k(x) \implies g(x) = \frac{k(x)}{f(x)}", font_size=17, color=YELLOW),
            MathTex(r"\lim f(x) = 0 \text{ 가능성 존재 } \implies \mathbf{거짓(False)}", font_size=18, color=RED_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(RIGHT, buff=0.6)

        rect2 = SurroundingRectangle(sub_box, color=PURPLE_E, fill_color=BLACK, fill_opacity=0.88, buff=0.25)
        self.play(FadeIn(rect2), Write(sub_box))
        self.wait(2.5)
