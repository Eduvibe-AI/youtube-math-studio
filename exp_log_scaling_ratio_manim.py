"""
ExpLogScalingRatioManim (제32강 시각화)
지수함수와 로그함수의 수평·수직 확대·축소(스케일링) 비율 원리
y = 2^x vs y = 4^x = 2^(2x) (수평 1/2 축소, 1:1 선분비)
y = log_2(x) vs y = log_4(x) = (1/2)log_2(x) (수직 1/2 축소)
"""

from manim import *
import numpy as np

class ExpLogScalingRatioScene(Scene):
    def construct(self):
        # 1. Title
        title = Text("지수·로그함수의 확대·축소 & 실전 비율 관계", font_size=36, color=YELLOW)
        subtitle = Text("동일 y선상 1:1 중점 분할 & 동일 x선상 1:2 높이비", font_size=22, color=BLUE_B)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2).to_edge(UP)
        self.play(Write(title_group))
        self.wait(1)

        # 2. Coordinate System
        axes = Axes(
            x_range=[-0.5, 4.5, 1],
            y_range=[-0.5, 8.5, 2],
            x_length=7,
            y_length=5,
            axis_config={"color": GREY, "include_numbers": False}
        ).shift(DOWN * 0.6 + LEFT * 2)

        x_label = axes.get_x_axis_label(Tex("x").scale(0.8))
        y_label = axes.get_y_axis_label(Tex("y").scale(0.8))

        self.play(Create(axes), Write(x_label), Write(y_label))

        # 3. Exponential Graphs: y = 2^x and y = 4^x
        graph_2x = axes.plot(lambda x: 2**x, x_range=[0, 3], color=BLUE)
        label_2x = Tex("y = 2^x", color=BLUE).scale(0.75).next_to(graph_2x.get_end(), RIGHT)

        graph_4x = axes.plot(lambda x: 4**x, x_range=[0, 1.5], color=TEAL)
        label_4x = Tex("y = 4^x = 2^{2x}", color=TEAL).scale(0.75).next_to(graph_4x.get_end(), UP)

        self.play(Create(graph_2x), Write(label_2x))
        self.play(Create(graph_4x), Write(label_4x))
        self.wait(1)

        # 4. Horizontal line y = 4
        y_val = 4
        h_line = axes.get_horizontal_line(axes.c2p(2, y_val), color=YELLOW, stroke_width=2.5)
        h_label = Tex("y = k = 4", color=YELLOW).scale(0.7).next_to(h_line, LEFT)
        self.play(Create(h_line), Write(h_label))

        # Points on curves: A(1, 4) on 4^x, B(2, 4) on 2^x
        pt_A = Dot(axes.c2p(1, 4), color=RED)
        pt_B = Dot(axes.c2p(2, 4), color=GREEN)
        pt_O = Dot(axes.c2p(0, 4), color=GREY)

        lbl_A = Tex("A(1, 4)", color=RED).scale(0.65).next_to(pt_A, UP+LEFT, buff=0.1)
        lbl_B = Tex("B(2, 4)", color=GREEN).scale(0.65).next_to(pt_B, UP+RIGHT, buff=0.1)

        self.play(FadeIn(pt_O), FadeIn(pt_A, lbl_A), FadeIn(pt_B, lbl_B))

        # Ratio bracket 1 : 1
        brace1 = BraceBetweenPoints(axes.c2p(0, 4), axes.c2p(1, 4), direction=DOWN).shift(DOWN*0.1)
        txt1 = brace1.get_text("1").scale(0.7).set_color(YELLOW)

        brace2 = BraceBetweenPoints(axes.c2p(1, 4), axes.c2p(2, 4), direction=DOWN).shift(DOWN*0.1)
        txt2 = brace2.get_text("1").scale(0.7).set_color(YELLOW)

        self.play(GrowFromCenter(brace1), FadeIn(txt1), GrowFromCenter(brace2), FadeIn(txt2))
        self.wait(1)

        # 5. Explanatory Card on the right
        card_box = RoundedRectangle(corner_radius=0.2, width=4.5, height=4.2, color=BLUE_D, fill_opacity=0.15)
        card_box.shift(RIGHT * 3.8 + DOWN * 0.6)

        formula_text = VGroup(
            Text("★ 수능 실전 압축 공식", font_size=20, color=GOLD),
            Tex(r"y = 4^x = 2^{2x} \implies x\text{축 } \frac{1}{2}\text{배 축소}", font_size=22),
            Tex(r"\text{동일 } y \text{에서 } x_A : x_B = 1 : 2", font_size=22, color=YELLOW),
            Tex(r"\implies \overline{OA} = \overline{AB} \text{ (1 : 1 중점)}", font_size=22, color=GREEN_B),
            Line(LEFT*1.8, RIGHT*1.8, color=GREY),
            Tex(r"y = \log_4 x = \frac{1}{2}\log_2 x", font_size=22),
            Tex(r"\text{동일 } x \text{에서 } y\text{좌표 } 1 : 2 \text{ 높이비}", font_size=20, color=BLUE_B),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).move_to(card_box)

        self.play(FadeIn(card_box), Write(formula_text))
        self.wait(2)
