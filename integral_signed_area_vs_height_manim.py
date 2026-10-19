"""
IntegralSignedAreaVsHeightManim (제33강 시각화)
"적분을 넓이로만 보면 하수다!"
정적분의 이중성: 피적분함수 f(t)의 부호 있는 넓이 (+S1, -S2) vs 원함수 g(x)의 함숫값 높이 변화량
"""

from manim import *
import numpy as np

class IntegralSignedAreaVsHeightScene(Scene):
    def construct(self):
        # 1. Header
        title = Text("정적분의 본질: 넓이 vs 함숫값의 이중성", font_size=36, color=YELLOW)
        subtitle = Text("f(t)의 부호 있는 넓이 누적 = 원함수 g(x)의 높이 변화량 g(x) - g(a)", font_size=20, color=BLUE_B)
        VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)

        # 2. Upper Axes: f(t) = -(t-1)(t-3) (Cubic or Parabola with + and - area)
        axes_f = Axes(
            x_range=[-0.5, 4.5, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=5.5,
            y_length=2.6,
            axis_config={"color": GREY}
        ).shift(UP * 0.8 + LEFT * 3)

        label_f_axis = axes_f.get_y_axis_label(Tex("f(t)").scale(0.7))

        # Function f(t) = -(t - 1)(t - 3) = -t^2 + 4t - 3
        func_f = lambda t: -(t - 1) * (t - 3)
        graph_f = axes_f.plot(func_f, x_range=[0.5, 4], color=WHITE)
        label_f = Tex("f(t) = -(t-1)(t-3)", color=WHITE).scale(0.6).next_to(graph_f.get_end(), RIGHT)

        # Areas
        area_pos = axes_f.get_area(graph_f, x_range=[1, 3], color=BLUE, opacity=0.45)
        txt_s1 = Tex("+S_1", color=BLUE_B).scale(0.7).move_to(axes_f.c2p(2, 0.5))

        area_neg = axes_f.get_area(graph_f, x_range=[3, 4], color=RED, opacity=0.45)
        txt_s2 = Tex("-S_2", color=RED_B).scale(0.7).move_to(axes_f.c2p(3.5, -0.8))

        self.play(Create(axes_f), Write(label_f_axis), Create(graph_f), Write(label_f))
        self.play(FadeIn(area_pos), Write(txt_s1), FadeIn(area_neg), Write(txt_s2))

        # 3. Lower Axes: g(x) = int_1^x f(t)dt
        axes_g = Axes(
            x_range=[-0.5, 4.5, 1],
            y_range=[-0.5, 2.0, 0.5],
            x_length=5.5,
            y_length=2.4,
            axis_config={"color": GREY}
        ).shift(DOWN * 2.0 + LEFT * 3)

        label_g_axis = axes_g.get_y_axis_label(Tex("g(x)").scale(0.7))

        # Antiderivative g(x) = -x^3/3 + 2x^2 - 3x + 4/3
        func_g = lambda x: - (x**3)/3 + 2*(x**2) - 3*x + 4/3
        graph_g = axes_g.plot(func_g, x_range=[0.8, 4], color=YELLOW)
        label_g = Tex(r"g(x) = \int_1^x f(t)dt", color=YELLOW).scale(0.65).next_to(graph_g.get_end(), RIGHT)

        self.play(Create(axes_g), Write(label_g_axis), Create(graph_g), Write(label_g))

        # Critical points on g(x): x=1 (min/start), x=3 (max, peak +S1)
        dot_g1 = Dot(axes_g.c2p(1, 0), color=GREEN)
        lbl_g1 = Tex("g(1)=0").scale(0.6).next_to(dot_g1, DOWN)

        dot_g3 = Dot(axes_g.c2p(3, 4/3), color=GOLD)
        lbl_g3 = Tex(r"g(3)=+S_1").scale(0.6).next_to(dot_g3, UP)

        self.play(FadeIn(dot_g1, lbl_g1), FadeIn(dot_g3, lbl_g3))

        # 4. Right side Summary Panel
        summary_box = RoundedRectangle(corner_radius=0.2, width=5.0, height=5.2, color=BLUE_E, fill_opacity=0.2)
        summary_box.shift(RIGHT * 3.6 + DOWN * 0.6)

        summary_content = VGroup(
            Text("★ 수능 수학 1등급 통찰", font_size=20, color=GOLD),
            Tex(r"\text{정적분 } \int_a^b f(t)dt \ne \text{단순 넓이}", font_size=20, color=RED_B),
            Tex(r"\int_a^b f(t)dt = \mathbf{S_1 - S_2} \text{ (부호 있는 넓이)}", font_size=20, color=YELLOW),
            Line(LEFT*2.1, RIGHT*2.1, color=GREY),
            Text("원함수 g(x)와의 완벽한 동치 관계:", font_size=18, color=GREEN_B),
            Tex(r"g'(x) = f(x) \implies f(t)\text{의 부호 = } g(x)\text{의 증감}", font_size=20),
            Tex(r"\int_1^3 f(t)dt = g(3) - g(1) = \mathbf{\text{높이 변화량}}", font_size=20, color=BLUE_B),
            Tex(r"\text{극대}\cdot\text{극소 높이 차} = \text{둘러싸인 넓이 } S_1", font_size=19, color=PINK)
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to(summary_box)

        self.play(FadeIn(summary_box), Write(summary_content))
        self.wait(2)
