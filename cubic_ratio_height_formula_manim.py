"""
CubicRatioHeightFormulaManim (제37강 시각화)
3차함수 1:1:1:1 4등분 박스 비율 관계와 극대·극소 높이차 공식 H = (|a|/2) * L^3
수능 14번/22번 킬러 30초 컷의 완성
"""

from manim import *
import numpy as np

class CubicRatioHeightFormulaScene(Scene):
    def construct(self):
        title = Text("삼차함수 비율관계 & 극대·극소 높이차 공식", font_size=36, color=YELLOW)
        subtitle = Text("1:1:1:1 박스 비율 & 극대·극소 높이차 H = (|a|/2) L³", font_size=22, color=BLUE_B)
        VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)

        # Coordinate axes
        axes = Axes(
            x_range=[-2.5, 4.5, 1],
            y_range=[-5, 5, 2],
            x_length=7.5,
            y_length=4.8,
            axis_config={"color": GREY}
        ).shift(DOWN * 0.5 + LEFT * 1.8)

        # Standard cubic f(x) = (x + 1)^2 (x - 2) -> scaled and centered
        # Let roots of derivative be alpha=-1 (max) and beta=1 (min). L = 2.
        # f(x) = x^3 - 3x.
        # At x = -1: f(-1) = 2 (Local Max)
        # At x = 1: f(1) = -2 (Local Min)
        # Tangent at max (y = 2): crosses at x = 2. Distance from -1 to 2 is 3. (1:1:1 ratio)
        func = lambda x: (x**3) - 3*x
        graph = axes.plot(func, x_range=[-2.2, 2.3], color=WHITE)

        self.play(Create(axes), Create(graph))

        # Horizontal tangent line at y = 2
        tan_max = axes.get_horizontal_line(axes.c2p(2, 2), color=YELLOW, stroke_width=2)
        # Horizontal tangent line at y = -2
        tan_min = axes.get_horizontal_line(axes.c2p(2, -2), color=YELLOW, stroke_width=2)

        self.play(Create(tan_max), Create(tan_min))

        # Critical points: x = -1, 0 (inflection), 1, 2
        pts = [-1, 0, 1, 2]
        labels = [r"\alpha \text{ (극대)}", r"\text{변곡}", r"\beta \text{ (극소)}", r"\text{교점}"]
        colors = [RED, GREY, BLUE, GREEN]

        for p, lbl, col in zip(pts, labels, colors):
            v_line = DashedLine(axes.c2p(p, -3), axes.c2p(p, 3), color=col, stroke_width=1.5)
            dot = Dot(axes.c2p(p, func(p)), color=col)
            txt = Tex(lbl, color=col).scale(0.55).next_to(axes.c2p(p, -3), DOWN)
            self.play(Create(v_line), FadeIn(dot), Write(txt), run_time=0.4)

        # Height indicator
        h_line = DoubleArrow(axes.c2p(1, -2), axes.c2p(1, 2), color=RED_B, stroke_width=3)
        h_txt = Tex(r"H = 4", color=RED_B).scale(0.7).next_to(h_line, RIGHT)
        self.play(Create(h_line), Write(h_txt))

        # Right Summary Box
        summary_box = RoundedRectangle(corner_radius=0.2, width=4.8, height=4.5, color=GOLD, fill_opacity=0.15)
        summary_box.shift(RIGHT * 3.8 + DOWN * 0.5)

        box_text = VGroup(
            Text("★ 수능 수학 킬러 공식", font_size=20, color=GOLD),
            Tex(r"\text{간격 비율 } 1 : 1 : 1 : 1", font_size=22, color=YELLOW),
            Line(LEFT*1.9, RIGHT*1.9, color=GREY),
            Tex(r"\text{극대}\cdot\text{극소 높이차 공식:}", font_size=19, color=GREEN_B),
            Tex(r"H = \frac{|a|}{2} L^3", font_size=26, color=RED_B),
            Tex(r"(L = x_{\text{극소}} - x_{\text{극대}})", font_size=17, color=GREY),
            Line(LEFT*1.9, RIGHT*1.9, color=GREY),
            Tex(r"\text{예: } a=1, L=2 \implies H = 4!", font_size=20, color=BLUE_B)
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT).move_to(summary_box)

        self.play(FadeIn(summary_box), Write(box_text))
        self.wait(2)
