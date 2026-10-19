# -*- coding: utf-8 -*-
"""
Manim Community Animation Script: Exponential & Logarithmic Inverse Function Intersection
Topic: y = a^x vs y = log_a(x) and the Critical Base a = e^(1/e) ~ 1.4447
Run with: manim -pql exp_log_inverse_intersection_manim.py ExpLogInverseIntersectionScene
"""

from manim import *
import numpy as np

class ExpLogInverseIntersectionScene(Scene):
    def construct(self):
        # 1. Title & Introduction
        title = Title(
            r"지수함수와 로그함수의 역함수 교점과 임계 밑 $a = e^{1/e}$",
            include_underline=True,
            font_size=36
        )
        subtitle = Text(
            "y = a^x 와 y = log_a(x) 의 교점 개수는 어떻게 변할까?",
            font_size=20,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(subtitle), title.animate.scale(0.8).to_corner(UL))

        # 2. Setup Axes
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 6, 1],
            x_length=6.5,
            y_length=6.5,
            axis_config={"color": BLUE_D, "include_numbers": True, "font_size": 16},
        ).to_edge(LEFT, buff=0.8)

        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Line y = x
        line_yx = axes.plot(lambda x: x, x_range=[-0.5, 5.5], color=YELLOW, stroke_width=2.5)
        line_yx_label = MathTex(r"y = x", color=YELLOW, font_size=22).next_to(axes.c2p(5.2, 5.2), UP+LEFT, buff=0.1)

        self.play(Create(axes), Write(axes_labels), Create(line_yx), Write(line_yx_label))
        self.wait(1)

        # 3. Info Panel on the Right
        info_panel = VGroup().to_edge(RIGHT, buff=0.6)
        
        formula_box = RoundedRectangle(
            height=5.5, width=4.8, corner_radius=0.2,
            color=BLUE_E, fill_color="#0a101f", fill_opacity=0.85
        ).to_edge(RIGHT, buff=0.6)

        panel_title = Text("교점 판정 매트릭스", font_size=22, color=GOLD).move_to(formula_box.get_top() + DOWN*0.4)
        
        # ValueTracker for Base a
        a_tracker = ValueTracker(2.0)

        # Dynamic Functions
        def get_exp_curve():
            val_a = a_tracker.get_value()
            x_max = min(5.5, np.log(6.0) / np.log(val_a)) if val_a > 1.0 else 5.5
            return axes.plot(
                lambda x: val_a**x,
                x_range=[-0.8, x_max],
                color=CYAN,
                stroke_width=3.5
            )

        def get_log_curve():
            val_a = a_tracker.get_value()
            return axes.plot(
                lambda x: np.log(x) / np.log(val_a),
                x_range=[0.05, 5.5],
                color=PINK,
                stroke_width=3.5
            )

        exp_curve = always_redraw(get_exp_curve)
        log_curve = always_redraw(get_log_curve)

        exp_label = MathTex(r"f(x) = a^x", color=CYAN, font_size=24).next_to(formula_box.get_top(), DOWN, buff=1.0)
        log_label = MathTex(r"g(x) = \log_a x", color=PINK, font_size=24).next_to(exp_label, DOWN, buff=0.3)

        base_text = always_redraw(lambda: MathTex(
            rf"a = {a_tracker.get_value():.3f}",
            color=WHITE,
            font_size=26
        ).next_to(log_label, DOWN, buff=0.4))

        status_text = always_redraw(lambda: Text(
            "교점 0개 (만나지 않음)" if a_tracker.get_value() > 1.4447 + 0.01 else (
                "접점 1개 (e, e) 에서 접함!" if abs(a_tracker.get_value() - 1.4447) <= 0.01 else "교점 2개 (y = x 관통)"
            ),
            font_size=18,
            color=RED if a_tracker.get_value() > 1.445 else (GOLD if abs(a_tracker.get_value() - 1.4447) <= 0.01 else GREEN)
        ).next_to(base_text, DOWN, buff=0.3))

        self.play(FadeIn(formula_box), Write(panel_title), Write(exp_label), Write(log_label))
        self.play(Create(exp_curve), Create(log_curve), FadeIn(base_text), FadeIn(status_text))
        self.wait(1.5)

        # 4. Scenario 1: a = 2.0 (No intersection)
        explanation1 = Text(
            "Case 1: a > e^(1/e) (~1.445)\n지수 곡선이 y=x 위쪽에 위치하여\n교점이 전혀 발생하지 않음!",
            font_size=16, color=LIGHT_GRAY, line_spacing=1.3
        ).next_to(status_text, DOWN, buff=0.4)
        self.play(FadeIn(explanation1))
        self.wait(2)

        # 5. Scenario 2: Decreasing a to Critical Value e^(1/e) ~ 1.444668
        e_val = np.e
        crit_a = np.exp(1 / e_val)  # ~1.444668

        self.play(
            a_tracker.animate.set_value(crit_a),
            FadeOut(explanation1),
            run_time=3.5,
            rate_func=linear
        )

        tangent_dot = Dot(axes.c2p(e_val, e_val), color=YELLOW, radius=0.1)
        tangent_halo = Circle(radius=0.25, color=YELLOW).move_to(tangent_dot)
        tangent_label = MathTex(r"(e, e) \approx (2.718, 2.718)", color=YELLOW, font_size=20).next_to(tangent_dot, UP+LEFT, buff=0.15)

        explanation2 = Text(
            "Case 2: a = e^(1/e) (~1.4447)\n접선의 기울기가 1이 되는 유일한 점\n(e, e) 에서 y=x 와 완벽히 접함!",
            font_size=16, color=GOLD, line_spacing=1.3
        ).next_to(status_text, DOWN, buff=0.4)

        self.play(
            FadeIn(tangent_dot),
            Create(tangent_halo),
            Write(tangent_label),
            FadeIn(explanation2)
        )
        self.wait(2.5)

        # 6. Scenario 3: Decreasing a to sqrt(2) ~ 1.414 (2 Intersections)
        sqrt2 = np.sqrt(2)
        self.play(
            a_tracker.animate.set_value(sqrt2),
            FadeOut(tangent_dot),
            FadeOut(tangent_halo),
            FadeOut(tangent_label),
            FadeOut(explanation2),
            run_time=2.5
        )

        dot1 = Dot(axes.c2p(2, 2), color=GREEN, radius=0.09)
        dot2 = Dot(axes.c2p(4, 4), color=GREEN, radius=0.09)
        label1 = MathTex(r"(2, 2)", color=GREEN, font_size=20).next_to(dot1, DOWN+RIGHT, buff=0.1)
        label2 = MathTex(r"(4, 4)", color=GREEN, font_size=20).next_to(dot2, UP+LEFT, buff=0.1)

        explanation3 = Text(
            "Case 3: 1 < a < e^(1/e)\na = sqrt(2) ~ 1.414 일 때\n(2, 2) 와 (4, 4) 2개 점에서 교차!",
            font_size=16, color=GREEN_B, line_spacing=1.3
        ).next_to(status_text, DOWN, buff=0.4)

        self.play(
            FadeIn(dot1), FadeIn(dot2),
            Write(label1), Write(label2),
            FadeIn(explanation3)
        )
        self.wait(3)

        # 7. Summary Overlay Banner
        final_box = RoundedRectangle(
            height=1.4, width=11.5, corner_radius=0.15,
            color=GOLD, fill_color=BLACK, fill_opacity=0.9
        ).to_edge(DOWN, buff=0.3)

        summary_text = MathTex(
            r"\text{핵심 요약: } a > e^{1/e} \implies 0\text{개}, \quad "
            r"a = e^{1/e} \implies 1\text{개}(e, e), \quad "
            r"1 < a < e^{1/e} \implies 2\text{개}",
            font_size=24, color=GOLD
        ).move_to(final_box)

        self.play(FadeIn(final_box), Write(summary_text))
        self.wait(3)
