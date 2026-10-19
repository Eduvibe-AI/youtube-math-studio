from manim import *
import numpy as np

class SquareRootFunctionGSPScene(Scene):
    def construct(self):
        # 1. Dark modern background
        self.camera.background_color = "#0a0f1d"

        # Title Banner
        title = Text("무리함수 y = √(a(x-p)) + q의 그래프와 기하학적 성질", font="Malgun Gothic", font_size=28, color=YELLOW)
        subtitle = Text("GSP5 동적 기하 작도 및 2차 포물선 역함수 대칭 해석", font="Malgun Gothic", font_size=18, color=BLUE_B)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.3)

        self.play(Write(title), FadeIn(subtitle, shift=UP))
        self.wait(1)

        # 2. Coordinate Plane (Left)
        plane = NumberPlane(
            x_range=[-6, 8, 1],
            y_range=[-4, 6, 1],
            x_length=7.5,
            y_length=5.5,
            background_line_style={"stroke_color": "#1e293b", "stroke_width": 1.2}
        ).move_to(LEFT * 2.5 + DOWN * 0.4)

        x_label = MathTex("x", font_size=20, color=GRAY_B).next_to(plane.c2p(8, 0), RIGHT, buff=0.1)
        y_label = MathTex("y", font_size=20, color=GRAY_B).next_to(plane.c2p(0, 6), UP, buff=0.1)

        self.play(Create(plane), FadeIn(x_label), FadeIn(y_label))

        # 3. Right Info Panel
        info_panel = RoundedRectangle(
            corner_radius=0.15, width=4.5, height=5.5,
            color=BLUE_D, fill_color="#0f172a", fill_opacity=0.9
        ).move_to(RIGHT * 4.0 + DOWN * 0.4)

        eq_main = MathTex(r"y = \sqrt{a(x-p)} + q", font_size=26, color=YELLOW).next_to(info_panel.get_top(), DOWN, buff=0.35)
        
        info_box = VGroup(
            MathTex(r"\bullet\ \text{시작점(꼭짓점): } (p, q)", font_size=20, color=PINK),
            MathTex(r"\bullet\ a > 0: x \ge p\text{ (우상향 제1사분면)}", font_size=18, color=GREEN_B),
            MathTex(r"\bullet\ a < 0: x \le p\text{ (좌상향 제2사분면)}", font_size=18, color=ORANGE),
            MathTex(r"\bullet\ |a|\text{ 증가 } \implies \text{곡선의 폭/증가량 확대}", font_size=18, color=TEAL_B),
            MathTex(r"\bullet\ y = x\text{ 대칭: 포물선 } x = y^2\text{ 의 반쪽}", font_size=18, color=PURPLE_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(eq_main, DOWN, buff=0.4).shift(RIGHT * 0.15)

        self.play(Create(info_panel), Write(eq_main), FadeIn(info_box, shift=UP))
        self.wait(1)

        # 4. PART 1: The Parabola Half & y = x Reflection
        line_diag = DashedLine(plane.c2p(-4, -4), plane.c2p(6, 6), color=GRAY_A, stroke_width=2)
        diag_label = MathTex("y = x", font_size=18, color=GRAY_A).next_to(plane.c2p(5.5, 5.5), UL, buff=0.1)

        parabola = plane.plot(lambda x: x**2, x_range=[0, 2.4], color=BLUE, stroke_width=3)
        parabola_label = MathTex(r"y = x^2\ (x \ge 0)", font_size=20, color=BLUE).next_to(plane.c2p(1.8, 3.24), LEFT, buff=0.15)

        sqrt_basic = plane.plot(lambda x: np.sqrt(x), x_range=[0, 7], color=RED, stroke_width=3.5)
        sqrt_label = MathTex(r"y = \sqrt{x}", font_size=20, color=RED).next_to(plane.c2p(6, np.sqrt(6)), UR, buff=0.1)

        self.play(Create(line_diag), FadeIn(diag_label))
        self.play(Create(parabola), Write(parabola_label))
        self.wait(1)

        self.play(
            TransformFromCopy(parabola, sqrt_basic),
            Write(sqrt_label),
            run_time=2
        )
        self.wait(1)
        self.play(FadeOut(parabola), FadeOut(parabola_label), FadeOut(line_diag), FadeOut(diag_label))

        # 5. PART 2: Dynamic Parameters Animation (a, p, q)
        a_tracker = ValueTracker(1.0)
        p_tracker = ValueTracker(0.0)
        q_tracker = ValueTracker(0.0)

        vertex_dot = always_redraw(lambda: Dot(
            plane.c2p(p_tracker.get_value(), q_tracker.get_value()),
            color=PINK, radius=0.09
        ))

        vertex_label = always_redraw(lambda: MathTex(
            f"({p_tracker.get_value():.1f}, {q_tracker.get_value():.1f})",
            font_size=18, color=PINK
        ).next_to(vertex_dot, DL, buff=0.1))

        def get_dynamic_curve():
            a = a_tracker.get_value()
            p = p_tracker.get_value()
            q = q_tracker.get_value()
            if abs(a) < 1e-4:
                return VMobject()
            if a > 0:
                x_max = 7.8
                if p >= x_max:
                    return VMobject()
                return plane.plot(lambda x: np.sqrt(a * (x - p)) + q, x_range=[p, x_max], color=RED, stroke_width=3.5)
            else:
                x_min = -5.8
                if p <= x_min:
                    return VMobject()
                return plane.plot(lambda x: np.sqrt(a * (x - p)) + q, x_range=[x_min, p], color=ORANGE, stroke_width=3.5)

        dynamic_curve = always_redraw(get_dynamic_curve)

        self.play(
            FadeOut(sqrt_basic), FadeOut(sqrt_label),
            FadeIn(dynamic_curve), FadeIn(vertex_dot), FadeIn(vertex_label)
        )
        self.wait(1)

        # Dynamic Status in Info Panel
        status_text = always_redraw(lambda: VGroup(
            MathTex(f"a = {a_tracker.get_value():.1f}", font_size=22, color=YELLOW),
            MathTex(f"p = {p_tracker.get_value():.1f}", font_size=22, color=BLUE_B),
            MathTex(f"q = {q_tracker.get_value():.1f}", font_size=22, color=GREEN_B),
        ).arrange(RIGHT, buff=0.3).next_to(eq_main, DOWN, buff=0.2))

        self.add(status_text)
        self.wait(1)

        # Animate Parameter 'a' Dilation (1.0 -> 3.5 -> 1.0)
        self.play(a_tracker.animate.set_value(3.5), run_time=2, rate_func=smooth)
        self.wait(0.5)
        self.play(a_tracker.animate.set_value(0.5), run_time=1.5, rate_func=smooth)
        self.wait(0.5)
        self.play(a_tracker.animate.set_value(1.0), run_time=1, rate_func=smooth)
        self.wait(1)

        # Animate Parameter 'a' Sign Flip (1.0 -> -1.5)
        self.play(a_tracker.animate.set_value(-1.5), run_time=2, rate_func=smooth)
        self.wait(1)
        self.play(a_tracker.animate.set_value(1.5), run_time=1.5, rate_func=smooth)
        self.wait(1)

        # Animate Parameter 'p' and 'q' Translation
        self.play(p_tracker.animate.set_value(3.0), run_time=1.5, rate_func=smooth)
        self.wait(0.5)
        self.play(q_tracker.animate.set_value(2.0), run_time=1.5, rate_func=smooth)
        self.wait(1)

        # Move to 3rd quadrant position
        self.play(p_tracker.animate.set_value(-2.0), q_tracker.animate.set_value(-1.5), run_time=2, rate_func=smooth)
        self.wait(1)

        # Return to origin
        self.play(p_tracker.animate.set_value(0.0), q_tracker.animate.set_value(0.0), a_tracker.animate.set_value(1.0), run_time=1.5)
        self.wait(1)

        # Final Summary Callout
        summary_rect = RoundedRectangle(corner_radius=0.15, width=6.5, height=1.6, color=YELLOW, fill_color="#030712", fill_opacity=0.95)
        summary_rect.move_to(DOWN * 0.4)
        summary_title = Text("핵심 정리 (GSP5 무작정 따라하기 결론)", font="Malgun Gothic", font_size=20, color=YELLOW).next_to(summary_rect.get_top(), DOWN, buff=0.2)
        summary_body = Text(
            "• a의 부호: 뻗어나가는 사분면 방향 (우/좌)\n"
            "• |a|의 크기: 곡선의 벌어짐 폭(증가량)\n"
            "• p, q: 꼭짓점(p, q)의 x축, y축 평행이동",
            font="Malgun Gothic", font_size=16, color=WHITE, line_spacing=0.8
        ).next_to(summary_title, DOWN, buff=0.15)
        summary_group = VGroup(summary_rect, summary_title, summary_body)

        self.play(FadeIn(summary_group, shift=UP))
        self.wait(3)
