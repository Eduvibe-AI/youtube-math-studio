"""
CircleInscribedAngleManim (제35강 시각화)
원의 성질 핵심: 원주각 = 중심각 / 2, 지름의 원주각 90도, 내접사각형 대각의 합 180도
"""

from manim import *
import numpy as np

class CircleInscribedAngleScene(Scene):
    def construct(self):
        title = Text("원의 성질 핵심 정리: 원주각과 내접사각형", font_size=36, color=YELLOW)
        subtitle = Text("원주각은 중심각의 절반 & 지름에 대한 원주각은 90도", font_size=22, color=BLUE_B)
        VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)

        # Circle with center O
        R = 2.2
        circle = Circle(radius=R, color=BLUE_B).shift(LEFT * 2.5 + DOWN * 0.4)
        center_O = Dot(circle.get_center(), color=WHITE)
        lbl_O = Tex("O").scale(0.7).next_to(center_O, DOWN+LEFT, buff=0.1)

        # Points A, B on circle (Arc)
        ang_A = -2.5
        ang_B = -0.6
        ang_P = 1.3

        pt_A = circle.get_center() + np.array([R*np.cos(ang_A), R*np.sin(ang_A), 0])
        pt_B = circle.get_center() + np.array([R*np.cos(ang_B), R*np.sin(ang_B), 0])
        pt_P = circle.get_center() + np.array([R*np.cos(ang_P), R*np.sin(ang_P), 0])

        dot_A = Dot(pt_A, color=YELLOW)
        dot_B = Dot(pt_B, color=YELLOW)
        dot_P = Dot(pt_P, color=RED)

        lbl_A = Tex("A").scale(0.7).next_to(dot_A, DOWN+LEFT)
        lbl_B = Tex("B").scale(0.7).next_to(dot_B, DOWN+RIGHT)
        lbl_P = Tex("P").scale(0.7).next_to(dot_P, UP)

        # Lines for Inscribed Angle APB and Central Angle AOB
        line_PA = Line(pt_P, pt_A, color=RED)
        line_PB = Line(pt_P, pt_B, color=RED)
        line_OA = Line(circle.get_center(), pt_A, color=YELLOW, stroke_width=2.5)
        line_OB = Line(circle.get_center(), pt_B, color=YELLOW, stroke_width=2.5)

        self.play(Create(circle), FadeIn(center_O, lbl_O))
        self.play(FadeIn(dot_A, lbl_A), FadeIn(dot_B, lbl_B))
        self.play(Create(line_OA), Create(line_OB))
        self.play(FadeIn(dot_P, lbl_P), Create(line_PA), Create(line_PB))

        # Right Summary Box
        summary_box = RoundedRectangle(corner_radius=0.2, width=5.2, height=4.5, color=BLUE_D, fill_opacity=0.15)
        summary_box.shift(RIGHT * 3.4 + DOWN * 0.4)

        box_text = VGroup(
            Text("★ 수능 기하 원의 3대 핵심", font_size=20, color=GOLD),
            Tex(r"\angle APB = \frac{1}{2} \angle AOB \text{ (원주각 공식)}", font_size=20, color=YELLOW),
            Line(LEFT*2.2, RIGHT*2.2, color=GREY),
            Tex(r"\text{선분 } AB \text{가 지름} \implies \angle APB = 90^\circ", font_size=20, color=GREEN_B),
            Line(LEFT*2.2, RIGHT*2.2, color=GREY),
            Tex(r"\text{원 내접사각형 대각의 합 } = 180^\circ", font_size=20, color=BLUE_B),
            Tex(r"\cos(180^\circ - \theta) = -\cos\theta \text{ 연계}", font_size=19, color=PINK)
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).move_to(summary_box)

        self.play(FadeIn(summary_box), Write(box_text))
        self.wait(2)
