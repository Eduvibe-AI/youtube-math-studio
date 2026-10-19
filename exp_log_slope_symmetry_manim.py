# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: Exponential & Logarithmic Functions - Slope & Symmetry
Topic: Utilizing Slope m = -1 & Translation Vectors in CSAT Math (2022 Sep #21)
Run with: manim -pql exp_log_slope_symmetry_manim.py ExpLogSlopeSymmetryScene
"""

from manim import *
import numpy as np

class ExpLogSlopeSymmetryScene(Scene):
    def construct(self):
        # 1. Title & Introduction
        title = Title(
            r"지수·로그함수에서 기울기 활용법과 평행이동·대칭성",
            include_underline=True,
            font_size=34
        )
        subtitle = Text(
            "기울기 m = -1 과 직각이등변삼각형 (1 : 1 : √2) 의 마법",
            font_size=20,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. Setup Axes
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 6, 1],
            x_length=6.2,
            y_length=6.2,
            axis_config={"color": BLUE_D, "include_numbers": True, "font_size": 16},
        ).to_edge(LEFT, buff=0.8)

        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Symmetry Axis y = x
        line_yx = axes.plot(lambda x: x, x_range=[-0.5, 5.5], color=YELLOW, stroke_width=2)
        line_yx_label = MathTex(r"y = x", color=YELLOW, font_size=20).next_to(axes.c2p(5.2, 5.2), UP+LEFT, buff=0.1)

        self.play(Create(axes), Write(axes_labels), Create(line_yx), Write(line_yx_label))
        self.wait(1)

        # 3. Line with Slope m = -1: y = -x + 4
        line_perp = axes.plot(lambda x: -x + 4, x_range=[0.2, 4.5], color=RED, stroke_width=3)
        line_perp_label = MathTex(r"y = -x + 4", color=RED, font_size=22).next_to(axes.c2p(4.0, 0.0), UP+RIGHT, buff=0.15)
        perp_symbol = RightAngle(
            Line(axes.c2p(2, 2), axes.c2p(1, 1)),
            Line(axes.c2p(2, 2), axes.c2p(1, 3)),
            length=0.25, color=GOLD
        )

        self.play(Create(line_perp), Write(line_perp_label), Create(perp_symbol))
        self.wait(1)

        # 4. Curves: y = 2^(x-1) and y = log_2(x-1)
        exp_curve = axes.plot(
            lambda x: 2**(x - 1),
            x_range=[-0.5, 3.5],
            color=CYAN,
            stroke_width=3.5
        )
        exp_label = MathTex(r"y = a^{x-1} \;(a=2)", color=CYAN, font_size=20).next_to(axes.c2p(2.8, 3.5), LEFT, buff=0.1)

        log_curve = axes.plot(
            lambda x: np.log2(np.maximum(x - 1, 0.01)),
            x_range=[1.08, 5.5],
            color=PINK,
            stroke_width=3.5
        )
        log_label = MathTex(r"y = \log_a(x-1)", color=PINK, font_size=20).next_to(axes.c2p(4.5, 1.8), DOWN, buff=0.1)

        self.play(Create(exp_curve), Write(exp_label))
        self.play(Create(log_curve), Write(log_label))
        self.wait(1)

        # 5. Intersections A(1, 3) and B(3, 1)
        dot_a = Dot(axes.c2p(1, 3), color=YELLOW, radius=0.09)
        dot_b = Dot(axes.c2p(3, 1), color=YELLOW, radius=0.09)
        label_a = MathTex(r"A(1, 3)", color=YELLOW, font_size=20).next_to(dot_a, UP+LEFT, buff=0.1)
        label_b = MathTex(r"B(3, 1)", color=YELLOW, font_size=20).next_to(dot_b, DOWN+RIGHT, buff=0.1)

        self.play(FadeIn(dot_a), FadeIn(dot_b), Write(label_a), Write(label_b))

        # 6. Right Isosceles Triangle: dx = 2, dy = 2 -> AB = 2*sqrt(2)
        tri_corner = axes.c2p(3, 3)
        h_line = Line(axes.c2p(1, 3), tri_corner, color=ORANGE, stroke_width=2.5)
        v_line = Line(tri_corner, axes.c2p(3, 1), color=ORANGE, stroke_width=2.5)
        h_label = MathTex(r"\Delta x = 2", color=ORANGE, font_size=18).next_to(h_line, UP, buff=0.1)
        v_label = MathTex(r"\Delta y = 2", color=ORANGE, font_size=18).next_to(v_line, RIGHT, buff=0.1)
        hypot_label = MathTex(r"L = 2\sqrt{2}", color=RED, font_size=20).next_to(axes.c2p(2, 2), DOWN+LEFT, buff=0.2)

        self.play(Create(h_line), Write(h_label), Create(v_line), Write(v_label), Write(hypot_label))
        self.wait(1.5)

        # 7. Third Point C(0, 1/2) and Shaded Triangle ABC
        dot_c = Dot(axes.c2p(0, 0.5), color=GREEN, radius=0.08)
        label_c = MathTex(r"C(0, \frac{1}{2})", color=GREEN, font_size=18).next_to(dot_c, LEFT, buff=0.1)

        tri_polygon = Polygon(
            axes.c2p(1, 3), axes.c2p(3, 1), axes.c2p(0, 0.5),
            color=GOLD, fill_color=GOLD, fill_opacity=0.3
        )
        area_text = MathTex(r"S = \frac{7}{2} \implies 50S = 175", color=GOLD, font_size=22).to_corner(UR, buff=1.0)

        self.play(FadeIn(dot_c), Write(label_c), FadeIn(tri_polygon), Write(area_text))
        self.wait(2)

        # 8. Side Explanation Card
        info_box = RoundedRectangle(
            height=3.5, width=4.8, corner_radius=0.2,
            color=BLUE_E, fill_color="#070a13", fill_opacity=0.9
        ).to_edge(RIGHT, buff=0.5).shift(DOWN*0.5)

        summary_p = Text(
            "수능 지수·로그 3대 해법:\n1. 평행이동 벡터 = 기울기\n2. m = -1 이면 y = x 수직 대칭\n3. L = 2√2 -> dx = 2, dy = 2\n초스피드 4점 킬러 정복!",
            font_size=16, color=LIGHT_GRAY, line_spacing=1.3
        ).move_to(info_box)

        self.play(FadeIn(info_box), Write(summary_p))
        self.wait(3)
