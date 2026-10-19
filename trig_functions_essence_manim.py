"""
삼각비부터 삼각함수까지의 수학적 본질
3Blue1Brown 스타일 Manim 애니메이션 스크립트

포함 주제:
1. 직각삼각형에서 단위원으로의 도약 (Unit Circle & P(cosθ, sinθ))
2. 호도법의 탄생: 원호의 길이를 실수 수직선으로 펼치기 (Radian Unrolling)
3. 단위원 회전에서 사인파(Sine Wave) 생성 및 원점 미분계수 (sin x)' = cos x

실행 방법:
manim -pql trig_functions_essence_manim.py TrigFunctionsEssenceScene
"""

from manim import *
import numpy as np

class TrigFunctionsEssenceScene(Scene):
    def construct(self):
        # 1. 인트로 타이틀
        title = Title("삼각비부터 삼각함수까지: 수학적 일반화의 본질", include_underline=True)
        title.set_color(GOLD)
        subtitle = Text("직각삼각형의 변의 비에서 실수 전체의 함수로의 대도약", font_size=20, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        # ==============================================================
        # PART 1: 빗변 1인 직각삼각형에서 단위원으로
        # ==============================================================
        part1_label = Text("Part 1. 단위원과 좌표 P(cosθ, sinθ)로의 일반화", font_size=24, color=BLUE_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part1_label))

        axes = Axes(
            x_range=[-1.8, 1.8, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=6.0,
            y_length=5.0,
            axis_config={"color": BLUE_E, "include_numbers": False}
        ).shift(LEFT * 2.5 + DOWN * 0.3)

        unit_circle = Circle(radius=1.8, color=BLUE_C, stroke_width=2.5).move_to(axes.c2p(0, 0))
        self.play(Create(axes), Create(unit_circle))

        # Angle theta tracker
        theta_val = ValueTracker(np.pi / 6) # 30 deg

        def get_arm():
            th = theta_val.get_value()
            pt = axes.c2p(np.cos(th), np.sin(th))
            return Line(axes.c2p(0, 0), pt, color=YELLOW, stroke_width=3.5)

        def get_cos_line():
            th = theta_val.get_value()
            return Line(axes.c2p(0, 0), axes.c2p(np.cos(th), 0), color=TEAL, stroke_width=3)

        def get_sin_line():
            th = theta_val.get_value()
            return Line(axes.c2p(np.cos(th), 0), axes.c2p(np.cos(th), np.sin(th)), color=GOLD, stroke_width=3)

        def get_dot():
            th = theta_val.get_value()
            return Dot(axes.c2p(np.cos(th), np.sin(th)), color=RED)

        arm = always_redraw(get_arm)
        cos_l = always_redraw(get_cos_line)
        sin_l = always_redraw(get_sin_line)
        dot_p = always_redraw(get_dot)

        # Labels
        lbl_p = MathTex(r"P(\cos\theta, \;\sin\theta)", font_size=24, color=YELLOW).to_edge(RIGHT, buff=2.0).shift(UP * 1.5)
        lbl_cos = MathTex(r"x\text{-좌표} = \cos\theta \quad (\text{밑변})", font_size=22, color=TEAL).next_to(lbl_p, DOWN, buff=0.4)
        lbl_sin = MathTex(r"y\text{-좌표} = \sin\theta \quad (\text{높이})", font_size=22, color=GOLD).next_to(lbl_cos, DOWN, buff=0.3)
        lbl_pyth = MathTex(r"\cos^2\theta + \sin^2\theta = 1", font_size=26, color=WHITE).next_to(lbl_sin, DOWN, buff=0.5)

        self.play(Create(arm), Create(cos_l), Create(sin_l), Create(dot_p))
        self.play(Write(lbl_p), Write(lbl_cos), Write(lbl_sin), Write(lbl_pyth))
        self.wait(1)

        # Rotate around the circle: 30 deg -> 150 deg (2nd quad) -> 240 deg (3rd quad) -> 315 deg (4th quad)
        self.play(theta_val.animate.set_value(5 * np.pi / 6), run_time=2) # 2nd quad: cos < 0, sin > 0
        self.wait(0.5)
        self.play(theta_val.animate.set_value(4 * np.pi / 3), run_time=2) # 3rd quad: cos < 0, sin < 0
        self.wait(0.5)
        self.play(theta_val.animate.set_value(7 * np.pi / 4), run_time=2) # 4th quad: cos > 0, sin < 0
        self.wait(1)

        self.play(
            FadeOut(axes), FadeOut(unit_circle), FadeOut(arm), FadeOut(cos_l),
            FadeOut(sin_l), FadeOut(dot_p), FadeOut(lbl_p), FadeOut(lbl_cos),
            FadeOut(lbl_sin), FadeOut(lbl_pyth), FadeOut(part1_label)
        )

        # ==============================================================
        # PART 2: 호도법 (Radian)의 탄생과 실수화
        # ==============================================================
        part2_label = Text("Part 2. 육십분법의 한계와 호도법(Radian)의 필연성", font_size=24, color=GOLD).to_edge(UP, buff=1.0)
        self.play(FadeIn(part2_label))

        rad_card = VGroup(
            MathTex(r"\text{육십분법 }(360^\circ)\text{의 한계: 인위적 각도 단위, 실수 수직선에 올릴 수 없음}", font_size=22, color=GRAY_A),
            MathTex(r"\text{호도법(Radian)의 정의: } \theta = \frac{l}{r} \quad \left[\frac{\text{길이}}{\text{길이}} = \text{무차원 순수 실수}\right]", font_size=24, color=YELLOW),
            MathTex(r"r = 1 \text{ (단위원)} \implies \mathbf{l = \theta \quad (\text{호의 길이 자체가 각도의 크기!})}", font_size=26, color=GOLD),
            MathTex(r"360^\circ = 2\pi \text{ rad} \iff \mathbf{180^\circ = \pi \text{ rad}} \iff 1\text{ rad} = \frac{180^\circ}{\pi} \approx 57.3^\circ", font_size=22, color=TEAL)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).center().shift(DOWN * 0.2)

        self.play(Write(rad_card))
        self.wait(3)
        self.play(FadeOut(rad_card), FadeOut(part2_label))

        # ==============================================================
        # PART 3: 단위원에서 사인 곡선 y = sin x 생성 & 미분
        # ==============================================================
        part3_label = Text("Part 3. 사인파 생성 및 자연스러운 미분 (sin x)' = cos x", font_size=24, color=GREEN_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part3_label))

        circle_center = LEFT * 4.5 + DOWN * 0.5
        c_radius = 1.4
        c_axes = Axes(x_range=[-1.3, 1.3], y_range=[-1.3, 1.3], x_length=2.8, y_length=2.8, axis_config={"color": BLUE_E}).move_to(circle_center)
        c_circle = Circle(radius=c_radius, color=BLUE_C, stroke_width=2).move_to(circle_center)

        graph_axes = Axes(
            x_range=[0, 2*np.pi + 0.3, np.pi/2],
            y_range=[-1.5, 1.5, 1],
            x_length=6.5,
            y_length=3.0,
            axis_config={"color": BLUE_E, "include_numbers": False}
        ).shift(RIGHT * 2.2 + DOWN * 0.5)

        # Labels on graph axes
        x_lbl = MathTex(r"x \text{ (실수, rad)}", font_size=18, color=GRAY_A).next_to(graph_axes.x_axis, RIGHT)
        pi_lbl = MathTex(r"\pi", font_size=20).next_to(graph_axes.c2p(np.pi, 0), DOWN)
        two_pi_lbl = MathTex(r"2\pi", font_size=20).next_to(graph_axes.c2p(2*np.pi, 0), DOWN)

        sine_curve = graph_axes.plot(lambda x: np.sin(x), x_range=[0, 2*np.pi], color=GOLD, stroke_width=3.5)

        diff_note = MathTex(
            r"\lim_{x \to 0}\frac{\sin x}{x} = 1 \implies \mathbf{(\sin x)' = \cos x \quad (\text{호도법에서만 성립하는 최고의 미분})}",
            font_size=22, color=YELLOW
        ).to_edge(DOWN, buff=0.8)

        self.play(Create(c_axes), Create(c_circle), Create(graph_axes), Write(x_lbl), Write(pi_lbl), Write(two_pi_lbl))
        self.play(Create(sine_curve), run_time=3)
        self.play(Write(diff_note))
        self.wait(3)

        final_msg = Text("수학의 본질: 한계를 깨부수고 개념을 일반화하는 위대한 도약!", font_size=22, color=YELLOW)
        final_msg.to_edge(DOWN, buff=0.3)
        self.play(Transform(diff_note, final_msg))
        self.wait(2)
