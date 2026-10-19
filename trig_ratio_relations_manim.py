# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: Trigonometric Function Ratio Relations (8-Box Matrix)
Topic: Special Angles and Ratio Relations in Trig Graphs (y = sin x)
Run with: manim -pql trig_ratio_relations_manim.py TrigRatioRelationsScene
"""

from manim import *
import numpy as np

class TrigRatioRelationsScene(Scene):
    def construct(self):
        # 1. Title & Introduction
        title = Title(
            r"삼각함수에서도 \textquotedblleft 비율관계\textquotedblright 를 사용하는 방법",
            include_underline=True,
            font_size=32
        )
        subtitle = Text(
            "8칸 박스법과 높이 절반 (y = 1/2) 1 : 2 황금 분할 원리",
            font_size=20,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. Setup Axes for one full period (0 to 2*pi)
        axes = Axes(
            x_range=[-0.2, 2 * np.pi + 0.5, np.pi / 2],
            y_range=[-1.4, 1.4, 0.5],
            x_length=7.5,
            y_length=5.0,
            axis_config={"color": BLUE_D, "include_numbers": False},
        ).to_edge(LEFT, buff=0.8)

        # X-axis ticks & labels
        x_labels = VGroup(
            MathTex(r"0", font_size=18).next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.1),
            MathTex(r"\frac{\pi}{2}", font_size=18).next_to(axes.c2p(np.pi / 2, 0), DOWN, buff=0.15),
            MathTex(r"\pi", font_size=18).next_to(axes.c2p(np.pi, 0), DOWN, buff=0.15),
            MathTex(r"\frac{3\pi}{2}", font_size=18).next_to(axes.c2p(3 * np.pi / 2, 0), DOWN, buff=0.15),
            MathTex(r"2\pi", font_size=18).next_to(axes.c2p(2 * np.pi, 0), DOWN, buff=0.15),
        )

        y_labels = VGroup(
            MathTex(r"1", font_size=18).next_to(axes.c2p(0, 1), LEFT, buff=0.15),
            MathTex(r"0.5", font_size=16, color=YELLOW).next_to(axes.c2p(0, 0.5), LEFT, buff=0.15),
            MathTex(r"-1", font_size=18).next_to(axes.c2p(0, -1), LEFT, buff=0.15),
        )

        self.play(Create(axes), Write(x_labels), Write(y_labels))

        # 3. 8-Box Grid (4 columns, 2 rows)
        grid_boxes = VGroup()
        for i in range(4):
            x_start = i * (np.pi / 2)
            for j in [0, -1]:
                p1 = axes.c2p(x_start, j)
                p2 = axes.c2p(x_start + np.pi / 2, j + 1)
                rect = Rectangle(
                    width=abs(axes.c2p(np.pi / 2, 0)[0] - axes.c2p(0, 0)[0]),
                    height=abs(axes.c2p(0, 1)[1] - axes.c2p(0, 0)[1]),
                    stroke_color=BLUE_E,
                    stroke_width=1.2,
                    stroke_opacity=0.6,
                    fill_opacity=0.04,
                    fill_color=BLUE
                ).move_to((p1 + p2) / 2)
                grid_boxes.add(rect)

        self.play(Create(grid_boxes))
        self.wait(1)

        # 4. Plot y = sin(x)
        sin_curve = axes.plot(
            lambda x: np.sin(x),
            x_range=[0, 2 * np.pi],
            color=CYAN,
            stroke_width=3.5
        )
        curve_label = MathTex(r"y = \sin x", color=CYAN, font_size=24).next_to(axes.c2p(np.pi / 2, 1), UP, buff=0.1)

        self.play(Create(sin_curve), Write(curve_label))
        self.wait(1)

        # 5. Highlight Ratio at y = 1/2: x = pi/6 (1 : 2 split)
        line_half = axes.plot(lambda x: 0.5, x_range=[0, np.pi], color=YELLOW, stroke_width=2)
        line_half.set_stroke(opacity=0.7)

        dot_p6 = Dot(axes.c2p(np.pi / 6, 0.5), color=RED, radius=0.08)
        dot_p2 = Dot(axes.c2p(np.pi / 2, 1.0), color=GOLD, radius=0.08)

        v_line1 = DashedLine(axes.c2p(np.pi / 6, 0), axes.c2p(np.pi / 6, 0.5), color=RED_B, stroke_width=1.5)
        v_line2 = DashedLine(axes.c2p(np.pi / 2, 0), axes.c2p(np.pi / 2, 1.0), color=GOLD_B, stroke_width=1.5)

        lbl_p6 = MathTex(r"\frac{\pi}{6}", color=RED, font_size=18).next_to(axes.c2p(np.pi / 6, 0), DOWN, buff=0.3)

        # Ratio Bracket 1 : 2
        brace1 = BraceBetweenPoints(axes.c2p(0, 0), axes.c2p(np.pi / 6, 0), direction=UP, buff=0.1)
        brace2 = BraceBetweenPoints(axes.c2p(np.pi / 6, 0), axes.c2p(np.pi / 2, 0), direction=UP, buff=0.1)
        ratio1 = MathTex(r"1", color=RED, font_size=18).next_to(brace1, UP, buff=0.05)
        ratio2 = MathTex(r"2", color=YELLOW, font_size=18).next_to(brace2, UP, buff=0.05)

        self.play(Create(line_half))
        self.play(FadeIn(dot_p6), Create(v_line1), Write(lbl_p6))
        self.play(Create(brace1), Write(ratio1), Create(brace2), Write(ratio2))
        self.wait(1.5)

        # 6. Theory Card
        theory_box = VGroup(
            Text("★ 삼각함수 1:2 분할 정리", font_size=18, color=GOLD),
            MathTex(r"\sin x = \frac{1}{2} \iff x = \frac{\pi}{6} = \frac{1}{3} \cdot \frac{\pi}{2}", font_size=18),
            MathTex(r"\text{구간 } [0, \pi/2] \text{를 } 1 : 2 \text{로 내분!}", font_size=16, color=YELLOW),
            MathTex(r"\sin x = \frac{\sqrt{3}}{2} \iff x = \frac{\pi}{3} \text{ (2 : 1 내분)}", font_size=16, color=GREEN_B),
            MathTex(r"\sin x = \frac{\sqrt{2}}{2} \iff x = \frac{\pi}{4} \text{ (1 : 1 정중앙)}", font_size=16, color=BLUE_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(RIGHT, buff=0.6)

        bg_card = SurroundingRectangle(theory_box, color=BLUE_E, fill_color=BLACK, fill_opacity=0.8, buff=0.25)

        self.play(FadeIn(bg_card), Write(theory_box))
        self.wait(3)
