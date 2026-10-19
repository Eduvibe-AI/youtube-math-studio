"""
DistanceProductRuleManim (제36강 시각화)
다항함수 거리곱 공식: 높이차 h = |a| * d1 * d2 * ...
수능 킬러의 계산량을 1/10로 단축시키는 압도적 효율 공식
"""

from manim import *
import numpy as np

class DistanceProductRuleScene(Scene):
    def construct(self):
        title = Text("다항함수 거리곱 공식 (Distance Product)", font_size=36, color=YELLOW)
        subtitle = Text("높이차 h = |a| × d₁ × d₂ (인수정리와 기하학적 수평 거리의 곱)", font_size=22, color=BLUE_B)
        VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)

        # Coordinate axes
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-4, 6, 2],
            x_length=7,
            y_length=4.5,
            axis_config={"color": GREY}
        ).shift(DOWN * 0.5 + LEFT * 1.8)

        # Parabola f(x) = -(x-1)(x-5) = -x^2 + 6x - 5 (roots at 1 and 5)
        func = lambda x: -(x - 1) * (x - 5)
        graph = axes.plot(func, x_range=[0.5, 5.5], color=BLUE_B)

        self.play(Create(axes), Create(graph))

        # Root dots
        dot1 = Dot(axes.c2p(1, 0), color=YELLOW)
        dot5 = Dot(axes.c2p(5, 0), color=YELLOW)
        lbl1 = Tex("x_1 = 1").scale(0.65).next_to(dot1, DOWN)
        lbl5 = Tex("x_2 = 5").scale(0.65).next_to(dot5, DOWN)

        self.play(FadeIn(dot1, lbl1), FadeIn(dot5, lbl5))

        # Peak at x = 3 (height = 4)
        peak = Dot(axes.c2p(3, 4), color=RED)
        base = Dot(axes.c2p(3, 0), color=GREY)
        h_line = Line(axes.c2p(3, 0), axes.c2p(3, 4), color=RED, stroke_width=3)
        lbl_h = Tex("h = 4", color=RED).scale(0.7).next_to(h_line, RIGHT)

        self.play(FadeIn(base), Create(h_line), FadeIn(peak), Write(lbl_h))

        # Distance brackets d1 = 2, d2 = 2
        brace1 = BraceBetweenPoints(axes.c2p(1, 0), axes.c2p(3, 0), direction=UP).shift(UP*0.1)
        txt_d1 = brace1.get_text("d₁ = 2").scale(0.6).set_color(YELLOW)

        brace2 = BraceBetweenPoints(axes.c2p(3, 0), axes.c2p(5, 0), direction=UP).shift(UP*0.1)
        txt_d2 = brace2.get_text("d₂ = 2").scale(0.6).set_color(YELLOW)

        self.play(GrowFromCenter(brace1), FadeIn(txt_d1), GrowFromCenter(brace2), FadeIn(txt_d2))

        # Right Summary Box
        summary_box = RoundedRectangle(corner_radius=0.2, width=4.6, height=4.2, color=GOLD, fill_opacity=0.15)
        summary_box.shift(RIGHT * 4.0 + DOWN * 0.5)

        box_text = VGroup(
            Text("★ 수능 압도적 치트키", font_size=20, color=GOLD),
            Tex(r"f(x) - k = a(x - x_1)(x - x_2)", font_size=20),
            Tex(r"\text{높이차 } h = |a| \times d_1 \times d_2", font_size=22, color=YELLOW),
            Tex(r"h = |1| \times 2 \times 2 = 4!", font_size=22, color=GREEN_B),
            Line(LEFT*1.8, RIGHT*1.8, color=GREY),
            Tex(r"\text{접점은 } d^2 \text{ (제곱)으로 계산}", font_size=19, color=PINK),
            Tex(r"\text{미분계수 } f'(x_1) = |a| \prod_{i \ne 1} d_i", font_size=18, color=BLUE_B)
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to(summary_box)

        self.play(FadeIn(summary_box), Write(box_text))
        self.wait(2)
