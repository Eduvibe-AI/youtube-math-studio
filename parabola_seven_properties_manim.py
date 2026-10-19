# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: 7 Geometric Properties of Parabolas
Topic: Focal Chords, Directrix Orthogonal Tangents, and Harmonic Mean
Run with: manim -pql parabola_seven_properties_manim.py ParabolaSevenPropertiesScene
"""

from manim import *
import numpy as np

class ParabolaSevenPropertiesScene(Scene):
    def construct(self):
        # 1. Title
        title = Title(
            r"포물선의 기하학적 성질 7가지",
            include_underline=True,
            font_size=32
        )
        subtitle = Text(
            "초점현 조화평균 (1/a + 1/b = 1/p) 과 준선 위 두 접선의 직교성 (90°)",
            font_size=20,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. Setup Axes for y^2 = 4px with p = 1
        p_val = 1.0
        axes = Axes(
            x_range=[-2.5, 5.0, 1],
            y_range=[-4.0, 4.0, 1],
            x_length=6.5,
            y_length=5.5,
            axis_config={"color": BLUE_D, "include_numbers": True, "font_size": 14},
        ).to_edge(LEFT, buff=0.8)

        # 3. Focus F(p, 0) and Directrix x = -p
        focus_dot = Dot(axes.c2p(p_val, 0), color=YELLOW, radius=0.08)
        focus_label = MathTex(r"F(p, 0)", color=YELLOW, font_size=18).next_to(focus_dot, DOWN, buff=0.15)

        directrix = axes.plot_line_graph(
            x_values=[-p_val, -p_val],
            y_values=[-3.8, 3.8],
            line_color=RED,
            stroke_width=2.5,
            add_vertex_dots=False
        )
        dir_label = MathTex(r"x = -p", color=RED, font_size=18).next_to(axes.c2p(-p_val, 3.2), LEFT, buff=0.15)

        # 4. Parabola y^2 = 4px (x = y^2 / 4)
        y_vals = np.linspace(-3.6, 3.6, 120)
        x_vals = (y_vals**2) / (4 * p_val)
        parabola_curve = axes.plot_line_graph(
            x_values=x_vals,
            y_values=y_vals,
            line_color=BLUE_B,
            stroke_width=3.5,
            add_vertex_dots=False
        )
        parabola_label = MathTex(r"y^2 = 4px", color=BLUE_B, font_size=22).next_to(axes.c2p(4.0, 3.2), RIGHT, buff=0.1)

        self.play(Create(axes), Create(directrix), Write(dir_label), FadeIn(focus_dot), Write(focus_label))
        self.play(Create(parabola_curve), Write(parabola_label))
        self.wait(1)

        # 5. Focal Chord AB passing through F(p,0)
        # Point A at y = 2 -> x = 1 (A = (1, 2))
        # Slope through (1,2) and (1,0) would be vertical; let's pick A = (4, 4) or A with y = 2.5
        # Line through (p, 0): y = m*(x - p). Let m = 1 -> y = x - 1
        # (x - 1)^2 = 4x -> x^2 - 6x + 1 = 0 -> x = 3 +- 2*sqrt(2)
        xA = 3 + 2 * np.sqrt(2)
        yA = xA - 1
        xB = 3 - 2 * np.sqrt(2)
        yB = xB - 1

        dotA = Dot(axes.c2p(xA, yA), color=GREEN, radius=0.07)
        dotB = Dot(axes.c2p(xB, yB), color=GREEN, radius=0.07)
        lblA = MathTex(r"A", color=GREEN, font_size=18).next_to(dotA, UP, buff=0.1)
        lblB = MathTex(r"B", color=GREEN, font_size=18).next_to(dotB, DOWN, buff=0.1)

        chord_AB = Line(axes.c2p(xA, yA), axes.c2p(xB, yB), color=GOLD, stroke_width=2.5)

        self.play(Create(chord_AB), FadeIn(dotA), Write(lblA), FadeIn(dotB), Write(lblB))
        self.wait(1)

        # 6. Theory Card with 7 Properties
        theory_card = VGroup(
            Text("★ 포물선의 7대 기하학적 성질", font_size=18, color=GOLD),
            MathTex(r"1.\ \frac{1}{\overline{AF}} + \frac{1}{\overline{BF}} = \frac{1}{p} \text{ (조화평균)}", font_size=15, color=WHITE),
            MathTex(r"2.\ \text{준선 위에서 그은 두 접선은 } 90^\circ \text{ 직교}", font_size=15, color=YELLOW),
            MathTex(r"3.\ \overline{FP} = \overline{FT} = \overline{PH} \text{ (접선 마름모 성질)}", font_size=15, color=WHITE),
            MathTex(r"4.\ \text{축에 평행한 광선은 반사되어 초점 } F \text{로 집광}", font_size=15, color=CYAN),
            MathTex(r"5.\ \text{법선의 } x\text{절편 길이(Subnormal) } = 2p \text{ 일정}", font_size=15, color=WHITE),
            MathTex(r"6.\ \overline{AB}\text{를 지름으로 하는 원은 준선에 접함}", font_size=15, color=GREEN_B),
            MathTex(r"7.\ \text{포물선 활꼴 : 외접삼각형 넓이비 } = 2 : 1", font_size=15, color=GOLD_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_edge(RIGHT, buff=0.5)

        bg_card = SurroundingRectangle(theory_card, color=BLUE_E, fill_color=BLACK, fill_opacity=0.9, buff=0.2)

        self.play(FadeIn(bg_card), Write(theory_card))
        self.wait(3)
