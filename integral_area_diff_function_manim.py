"""
정적분과 넓이 & 차함수의 마법 (그래프의 넓이와 두 곡선 사이의 면적)
3Blue1Brown 스타일 Manim 애니메이션 스크립트

포함 주제:
1. 정적분(Signed Area)과 기하학적 넓이(Absolute Area)의 차이
2. 차함수 h(x) = f(x) - g(x) 변환과 기하학적 넓이 불변성 (Area Invariance)
3. 3차함수와 직선 예제: 실근(0, 1, 3)과 구간별 정적분 S1 + S2 = 37/12

실행 방법:
manim -pql integral_area_diff_function_manim.py IntegralAreaDiffFunctionScene
"""

from manim import *
import numpy as np

class IntegralAreaDiffFunctionScene(Scene):
    def construct(self):
        # 1. Title
        title = Title("정적분과 넓이: 차함수 $h(x) = f(x) - g(x)$의 기하학", include_underline=True)
        title.set_color(GOLD)
        subtitle = Text("사오수학 30강: 두 곡선 사이의 넓이와 x축 평탄화 불변 원리", font_size=20, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        # ==============================================================
        # PART 1: 부호 면적(Signed Area) vs 기하학적 넓이(Absolute Area)
        # ==============================================================
        part1_label = Text("Part 1. 정적분 vs 넓이: x축 아래 구간의 부호 반전", font_size=24, color=BLUE_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part1_label))

        axes1 = Axes(
            x_range=[-0.5, 5.5, 1],
            y_range=[-7, 3, 2],
            x_length=8.0,
            y_length=4.0,
            axis_config={"color": BLUE_E, "include_numbers": False}
        ).shift(DOWN * 0.4)

        self.play(Create(axes1))

        # f(x) = x^2 - 5x on [0, 5]
        def f_parabola(x):
            return x**2 - 5*x

        parabola = axes1.plot(f_parabola, x_range=[-0.2, 5.2], color=TEAL, stroke_width=3)
        label_f = MathTex(r"y = x^2 - 5x", font_size=24, color=TEAL).next_to(axes1.c2p(5, 0), UP, buff=0.2)

        # Roots
        dot0 = Dot(axes1.c2p(0, 0), color=YELLOW)
        dot5 = Dot(axes1.c2p(5, 0), color=YELLOW)
        lbl0 = MathTex("0", font_size=20, color=YELLOW).next_to(dot0, UP, buff=0.15)
        lbl5 = MathTex("5", font_size=20, color=YELLOW).next_to(dot5, DOWN, buff=0.15)

        self.play(Create(parabola), Write(label_f), FadeIn(dot0, dot5, lbl0, lbl5))

        # Shading lower region
        area_neg = axes1.get_area(parabola, x_range=[0, 5], color=RED, opacity=0.4)
        lbl_neg = MathTex(r"\int_0^5 (x^2 - 5x)dx = -\frac{125}{6} < 0", font_size=22, color=RED_B).move_to(axes1.c2p(2.5, -3.2))

        self.play(FadeIn(area_neg), Write(lbl_neg))
        self.wait(1)

        # Absolute value flip
        lbl_abs = MathTex(r"\text{넓이 } S = -\int_0^5 (x^2 - 5x)dx = \mathbf{+\frac{125}{6}}", font_size=24, color=GREEN_B).next_to(lbl_neg, DOWN, buff=0.3)
        self.play(Write(lbl_abs))
        self.wait(1.5)

        self.play(FadeOut(parabola), FadeOut(label_f), FadeOut(dot0), FadeOut(dot5), FadeOut(lbl0), FadeOut(lbl5),
                  FadeOut(area_neg), FadeOut(lbl_neg), FadeOut(lbl_abs), FadeOut(axes1), FadeOut(part1_label))

        # ==============================================================
        # PART 2: 두 곡선 사이의 넓이와 차함수 불변성 (The Diff-Function)
        # ==============================================================
        part2_label = Text("Part 2. 차함수 h(x) = f(x) - g(x)를 통한 x축 평탄화", font_size=24, color=GREEN_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part2_label))

        # Upper axes for f(x) and g(x)
        axes_top = Axes(x_range=[-0.5, 3.5, 1], y_range=[-1, 5, 2], x_length=6.0, y_length=2.5,
                        axis_config={"color": GRAY_C}).shift(UP * 0.8 + LEFT * 0.2)
        # Lower axes for h(x) = f(x) - g(x)
        axes_bot = Axes(x_range=[-0.5, 3.5, 1], y_range=[-3, 2, 2], x_length=6.0, y_length=2.2,
                        axis_config={"color": GRAY_C}).shift(DOWN * 2.0 + LEFT * 0.2)

        # f(x) = x(x-2)^2, g(x) = x
        f_cubic = lambda x: x * (x - 2)**2
        g_line = lambda x: x
        h_diff = lambda x: x**3 - 4*x**2 + 3*x

        plot_f = axes_top.plot(f_cubic, x_range=[0, 3.2], color=BLUE, stroke_width=2.5)
        plot_g = axes_top.plot(g_line, x_range=[-0.2, 3.2], color=RED, stroke_width=2)
        lbl_curves = MathTex(r"y = f(x)", r"\text{ vs }", r"y = g(x)", font_size=20).next_to(axes_top, RIGHT, buff=0.3)
        lbl_curves[0].set_color(BLUE)
        lbl_curves[2].set_color(RED)

        # Areas between f and g
        area1_top = axes_top.get_area(plot_f, x_range=[0, 1], bounded_graph=plot_g, color=GREEN, opacity=0.45)
        area2_top = axes_top.get_area(plot_g, x_range=[1, 3], bounded_graph=plot_f, color=ORANGE, opacity=0.45)
        lbl_s1_top = MathTex(r"S_1", font_size=20, color=GREEN_B).move_to(axes_top.c2p(0.5, 0.8))
        lbl_s2_top = MathTex(r"S_2", font_size=20, color=ORANGE).move_to(axes_top.c2p(2.0, 1.3))

        self.play(Create(axes_top), Create(plot_f), Create(plot_g), Write(lbl_curves))
        self.play(FadeIn(area1_top, area2_top, lbl_s1_top, lbl_s2_top))
        self.wait(1)

        # Lower Diff graph: h(x) = f(x) - g(x)
        plot_h = axes_bot.plot(h_diff, x_range=[-0.2, 3.2], color=YELLOW, stroke_width=3)
        lbl_h = MathTex(r"y = f(x) - g(x) = x(x-1)(x-3)", font_size=20, color=YELLOW).next_to(axes_bot, RIGHT, buff=0.3)

        area1_bot = axes_bot.get_area(plot_h, x_range=[0, 1], color=GREEN, opacity=0.45)
        area2_bot = axes_bot.get_area(plot_h, x_range=[1, 3], color=ORANGE, opacity=0.45)
        lbl_s1_bot = MathTex(r"S_1 = \frac{5}{12}", font_size=18, color=GREEN_B).move_to(axes_bot.c2p(0.5, 0.6))
        lbl_s2_bot = MathTex(r"S_2 = \frac{8}{3}", font_size=18, color=ORANGE).move_to(axes_bot.c2p(2.0, -1.0))

        # Transformation arrows
        arrow = Arrow(axes_top.get_bottom(), axes_bot.get_top(), color=GOLD, stroke_width=3)
        arrow_lbl = Text("차함수 변환 (면적 100% 보존)", font_size=16, color=GOLD).next_to(arrow, RIGHT, buff=0.1)

        self.play(Create(axes_bot), GrowArrow(arrow), FadeIn(arrow_lbl))
        self.play(Create(plot_h), Write(lbl_h), FadeIn(area1_bot, area2_bot, lbl_s1_bot, lbl_s2_bot))
        self.wait(2)

        # Final Result Banner
        final_box = SurroundingRectangle(lbl_h, buff=0.15, color=GOLD)
        final_txt = MathTex(r"\mathbf{S = S_1 + S_2 = \frac{5}{12} + \frac{32}{12} = \frac{37}{12}}", font_size=24, color=GOLD)
        final_txt.to_edge(DOWN, buff=0.3)

        self.play(Create(final_box), Write(final_txt))
        self.wait(2)
