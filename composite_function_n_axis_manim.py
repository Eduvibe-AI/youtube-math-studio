# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: Composite Function Graphing via N-Axis Skill
Topic: N-Axis Coordinate Transformation and Dynamic Trajectory Mapping
Run with: manim -pql composite_function_n_axis_manim.py CompositeFunctionNAxisScene
"""

from manim import *
import numpy as np

class CompositeFunctionNAxisScene(Scene):
    def construct(self):
        # 1. Title
        title = Title(
            r"합성함수 그래프 그리기: N축 스킬",
            include_underline=True,
            font_size=32
        )
        subtitle = Text(
            "속함수 t = g(x)와 겉함수 y = f(t)의 공통 t축 직교 결합",
            font_size=20,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. Dual Coordinate System Setup (N-Axis)
        # Bottom-left: g(x) with horizontal x and vertical t
        axes_g = Axes(
            x_range=[-0.5, 4.5, 1],
            y_range=[-0.5, 4.5, 1],
            x_length=3.8,
            y_length=3.8,
            axis_config={"color": BLUE_C, "include_numbers": True, "font_size": 14},
        ).to_corner(DL, buff=1.0)
        labels_g = axes_g.get_axis_labels(x_label="x", y_label="t")

        # Top-right: f(t) rotated so horizontal axis is t
        axes_f = Axes(
            x_range=[-0.5, 4.5, 1],
            y_range=[-0.5, 4.5, 1],
            x_length=3.8,
            y_length=3.8,
            axis_config={"color": GREEN_C, "include_numbers": True, "font_size": 14},
        ).to_corner(UR, buff=1.0)
        labels_f = axes_f.get_axis_labels(x_label="t", y_label="y")

        self.play(Create(axes_g), Write(labels_g), Create(axes_f), Write(labels_f))
        self.wait(1)

        # 3. Inner Function: g(x) = Piecewise Linear or V-Shape (e.g. 2 - |x - 2|)
        # Let g(x) be a triangle from (0,0) -> (2,3) -> (4,0)
        g_pts = [axes_g.c2p(0, 0), axes_g.c2p(2, 3), axes_g.c2p(4, 0)]
        curve_g = VMobject(color=BLUE_A, stroke_width=3.5)
        curve_g.set_points_as_corners(g_pts)
        lbl_g = MathTex(r"t = g(x)", color=BLUE_A, font_size=20).next_to(axes_g.c2p(2, 3), UP, buff=0.1)

        # 4. Outer Function: f(t) = (t - 1)^2 / 2 or Piecewise
        # Let f(t) be (0, 1) -> (1.5, 3.5) -> (3, 0)
        f_pts = [axes_f.c2p(0, 1), axes_f.c2p(1.5, 3.5), axes_f.c2p(3, 0), axes_f.c2p(4, 2)]
        curve_f = VMobject(color=GREEN_A, stroke_width=3.5)
        curve_f.set_points_as_corners(f_pts)
        lbl_f = MathTex(r"y = f(t)", color=GREEN_A, font_size=20).next_to(axes_f.c2p(1.5, 3.5), UP, buff=0.1)

        self.play(Create(curve_g), Write(lbl_g), Create(curve_f), Write(lbl_f))
        self.wait(1)

        # 5. Explaining N-Axis Dynamic Mapping
        info_panel = VGroup(
            Text("★ N축 스킬 3단계 알고리즘", font_size=18, color=GOLD),
            Text("1. 속함수 t = g(x)의 치역 구간 추적", font_size=15, color=WHITE),
            MathTex(r"x: 0 \to 2 \implies t: 0 \to 3", font_size=16, color=BLUE_B),
            MathTex(r"x: 2 \to 4 \implies t: 3 \to 0 \text{ (턴어라운드!)}", font_size=16, color=RED_B),
            Text("2. t 구간을 겉함수 f(t)에 순서대로 대입", font_size=15, color=WHITE),
            Text("3. f(g(x)) 극값 = g(x) 턴 지점 + f(t) 극값", font_size=15, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_corner(UL, buff=1.0)

        bg_info = SurroundingRectangle(info_panel, color=BLUE_E, fill_color=BLACK, fill_opacity=0.85, buff=0.2)

        self.play(FadeIn(bg_info), Write(info_panel))
        self.wait(3)
