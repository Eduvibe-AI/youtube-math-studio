from manim import *
import numpy as np

class RationalFunctionDVariationScene(Scene):
    def construct(self):
        # Dark modern background
        self.camera.background_color = "#0a0f1d"

        # 1. Title Banner
        title = Text("유리함수 y=(ax+b)/(cx+d)의 그래프 d 변화 분석", font="Malgun Gothic", font_size=32, color=YELLOW)
        subtitle = Text("알지오매스(Algeomath) 공학도구 기반 동적 기하학 해석", font="Malgun Gothic", font_size=18, color=BLUE_B)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.35)

        self.play(Write(title), FadeIn(subtitle, shift=UP))
        self.wait(1)

        # 2. Coordinate Plane (Left/Center)
        plane = NumberPlane(
            x_range=[-10, 10, 2],
            y_range=[-8, 8, 2],
            x_length=7.5,
            y_length=5.5,
            background_line_style={"stroke_color": "#1e293b", "stroke_width": 1.2}
        ).move_to(LEFT * 2.2 + DOWN * 0.4)

        x_label = MathTex("x", font_size=20, color=GRAY_B).next_to(plane.c2p(10, 0), RIGHT, buff=0.1)
        y_label = MathTex("y", font_size=20, color=GRAY_B).next_to(plane.c2p(0, 8), UP, buff=0.1)

        self.play(Create(plane), FadeIn(x_label), FadeIn(y_label))

        # 3. Fixed Elements:
        # Fixed horizontal asymptote y = 1
        h_asym = DashedLine(plane.c2p(-10, 1), plane.c2p(10, 1), color=GREEN_B, stroke_width=2.5, dash_length=0.15)
        h_asym_label = MathTex(r"y = 1\text{ (수평점근선, 고정)}", font_size=20, color=GREEN_B).next_to(plane.c2p(7, 1), UP, buff=0.1)

        # Fixed point (-2, 0)
        fixed_pt = Dot(plane.c2p(-2, 0), color=RED, radius=0.08)
        fixed_pt_label = MathTex(r"(-2, 0)\text{ [고정 정점]}", font_size=18, color=RED).next_to(fixed_pt, DL, buff=0.1)

        self.play(Create(h_asym), FadeIn(h_asym_label), Create(fixed_pt), FadeIn(fixed_pt_label))
        self.wait(1)

        # 4. Right Side Info Panel
        info_panel = RoundedRectangle(corner_radius=0.15, width=4.5, height=5.5, color=BLUE_D, fill_color="#0f172a", fill_opacity=0.9)
        info_panel.move_to(RIGHT * 4.2 + DOWN * 0.4)

        eq_main = MathTex(r"y = \frac{x+2}{x+d}", font_size=28, color=YELLOW).next_to(info_panel.get_top(), DOWN, buff=0.4)
        eq_std = MathTex(r"= 1 + \frac{2-d}{x+d}", font_size=24, color=WHITE).next_to(eq_main, DOWN, buff=0.2)

        info_t1 = MathTex(r"\bullet\ \text{수평점근선: } y = 1", font_size=20, color=GREEN_B).next_to(eq_std, DOWN, buff=0.4).align_to(info_panel, LEFT).shift(RIGHT * 0.3)
        info_t2 = MathTex(r"\bullet\ \text{수직점근선: } x = -d", font_size=20, color=YELLOW).next_to(info_t1, DOWN, buff=0.25).align_to(info_t1, LEFT)
        info_t3 = MathTex(r"\bullet\ \text{대칭의 중심: } (-d, 1)", font_size=20, color=PINK).next_to(info_t2, DOWN, buff=0.25).align_to(info_t1, LEFT)
        info_t4 = MathTex(r"\bullet\ \text{모양 계수: } k = 2 - d", font_size=20, color=TEAL).next_to(info_t3, DOWN, buff=0.25).align_to(info_t1, LEFT)

        self.play(
            Create(info_panel),
            Write(eq_main), Write(eq_std),
            FadeIn(info_t1), FadeIn(info_t2), FadeIn(info_t3), FadeIn(info_t4)
        )
        self.wait(1)

        # 5. Interactive Value Tracker for d
        d_val = ValueTracker(-5.0)

        # Dynamic vertical asymptote x = -d
        v_asym = always_redraw(lambda: DashedLine(
            plane.c2p(-d_val.get_value(), -8),
            plane.c2p(-d_val.get_value(), 8),
            color=YELLOW, stroke_width=2.5, dash_length=0.15
        ))

        # Dynamic center of symmetry dot (-d, 1)
        center_dot = always_redraw(lambda: Dot(
            plane.c2p(-d_val.get_value(), 1),
            color=PINK, radius=0.08
        ))

        # Dynamic curve (2 branches)
        def get_left_branch():
            d = d_val.get_value()
            asym_x = -d
            k = 2 - d
            if abs(k) < 0.05:
                # Degenerate line y = 1
                return Line(plane.c2p(-10, 1), plane.c2p(asym_x - 0.05, 1), color=ORANGE, stroke_width=3)
            return plane.plot(
                lambda x: 1 + k / (x + d),
                x_range=[-10, asym_x - 0.15],
                color=BLUE if k > 0 else RED,
                stroke_width=3.5
            )

        def get_right_branch():
            d = d_val.get_value()
            asym_x = -d
            k = 2 - d
            if abs(k) < 0.05:
                # Degenerate line y = 1
                return Line(plane.c2p(asym_x + 0.05, 1), plane.c2p(10, 1), color=ORANGE, stroke_width=3)
            return plane.plot(
                lambda x: 1 + k / (x + d),
                x_range=[asym_x + 0.15, 10],
                color=BLUE if k > 0 else RED,
                stroke_width=3.5
            )

        left_curve = always_redraw(get_left_branch)
        right_curve = always_redraw(get_right_branch)

        # Dynamic parameter label
        d_label = always_redraw(lambda: MathTex(
            f"d = {d_val.get_value():.1f},\\quad k = {2 - d_val.get_value():.1f}",
            font_size=20,
            color=BLUE if (2 - d_val.get_value()) > 0 else (RED if (2 - d_val.get_value()) < 0 else YELLOW)
        ).move_to(info_panel.get_bottom() + UP * 0.5))

        self.play(
            Create(v_asym), Create(center_dot),
            Create(left_curve), Create(right_curve),
            FadeIn(d_label)
        )
        self.wait(1.5)

        # 6. Animation: Morphing d from -5 to 1.8 (Phase 1: k > 0)
        phase1_text = Text("1단계: d < 2 일 때 (k > 0: 제1, 3사분면 쌍곡선)", font="Malgun Gothic", font_size=16, color=BLUE).next_to(title_group, DOWN, buff=0.1)
        self.play(FadeIn(phase1_text))
        self.play(d_val.animate.set_value(1.5), run_time=3.5, rate_func=linear)
        self.wait(1)

        # 7. Critical Point: d = 2.0 (Degeneracy / Line)
        self.play(FadeOut(phase1_text))
        crit_box = RoundedRectangle(corner_radius=0.1, width=7.0, height=0.8, color=YELLOW, fill_color="#451a03", fill_opacity=0.9).move_to(DOWN * 2.8 + LEFT * 2.2)
        crit_text = MathTex(r"\text{임계점 } d = 2:\ ad - bc = 0 \implies y = 1\ (x \ne -2)\text{ 직선으로 축퇴!}", font_size=18, color=YELLOW).move_to(crit_box)

        self.play(d_val.animate.set_value(2.0), run_time=1.5)
        self.play(FadeIn(crit_box), FadeIn(crit_text))
        self.wait(2)
        self.play(FadeOut(crit_box), FadeOut(crit_text))

        # 8. Phase 2: d > 2 (Quadrant Flip!)
        phase2_text = Text("2단계: d > 2 일 때 (k < 0: 제2, 4사분면으로 위치 대반전!)", font="Malgun Gothic", font_size=16, color=RED).next_to(title_group, DOWN, buff=0.1)
        self.play(FadeIn(phase2_text))
        self.play(d_val.animate.set_value(7.0), run_time=4.0, rate_func=linear)
        self.wait(2)

        self.play(FadeOut(phase2_text))
        self.wait(1)
