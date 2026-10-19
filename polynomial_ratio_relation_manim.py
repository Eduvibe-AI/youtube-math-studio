"""
다항함수 비율 관계는 단 하나! (m : n 내분점 공식)
3Blue1Brown 스타일 Manim 애니메이션 스크립트

실행 방법:
manim -pql polynomial_ratio_relation_manim.py PolynomialRatioScene
"""

from manim import *
import numpy as np

class PolynomialRatioScene(Scene):
    def construct(self):
        # 1. 메인 타이틀
        title = Title("다항함수 극값 비율 관계는 단 하나! (m : n 내분점)", include_underline=True)
        title.set_color(YELLOW)
        subtitle = Text("롤의 정리에서 탄생한 모든 다항함수의 만능 비율 공식", font_size=20, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        # 2. 만능 내분점 공식 배너
        formula_tex = MathTex(
            r"f(x) = p(x-a)^m (x-b)^n \implies f'(c) = 0 \iff c = \frac{mb + na}{m + n} \quad (m : n \text{ 내분점})",
            font_size=32,
            color=YELLOW
        )
        box_rect = SurroundingRectangle(formula_tex, color=GOLD, buff=0.2, stroke_width=2)
        universal_banner = VGroup(box_rect, formula_tex).to_edge(UP, buff=1.0)
        self.play(FadeIn(universal_banner))
        self.wait(1)

        # 3. 좌표축 설정
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[-3, 3, 1],
            x_length=7.0,
            y_length=4.5,
            axis_config={"color": BLUE_C, "include_numbers": False},
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.4)

        a_val, b_val = 1.0, 5.0
        a_dot = Dot(axes.c2p(a_val, 0), color=RED)
        b_dot = Dot(axes.c2p(b_val, 0), color=RED)
        a_label = MathTex("a", font_size=32, color=RED).next_to(a_dot, DOWN)
        b_label = MathTex("b", font_size=32, color=RED).next_to(b_dot, DOWN)

        self.play(Create(axes), FadeIn(a_dot, b_dot, a_label, b_label))

        # 4. 차수별 3대 케이스 순차 애니메이션
        cases = [
            {
                "title": "1. 이차함수 (m=1, n=1)",
                "ratio": r"1 : 1 \text{ 내분점 (중점)}",
                "c_val": (1.0 + 5.0) / 2.0, # 3.0
                "func": lambda x: -0.6 * (x - 1.0) * (x - 5.0),
                "color": TEAL
            },
            {
                "title": "2. 삼차함수 (m=2, n=1)",
                "ratio": r"2 : 1 \text{ 내분점}",
                "c_val": (2 * 5.0 + 1 * 1.0) / 3.0, # 3.67
                "func": lambda x: 0.22 * ((x - 1.0)**2) * (5.0 - x),
                "color": BLUE_D
            },
            {
                "title": "3. 사차함수 (m=3, n=1)",
                "ratio": r"3 : 1 \text{ 내분점}",
                "c_val": (3 * 5.0 + 1 * 1.0) / 4.0, # 4.0
                "func": lambda x: 0.08 * ((x - 1.0)**3) * (5.0 - x),
                "color": PURPLE_B
            }
        ]

        curr_curve = None
        curr_c_dot = None
        curr_tan = None
        curr_card = None

        for case in cases:
            c = case["c_val"]
            curve = axes.plot(case["func"], x_range=[0.8, 5.2], color=case["color"], stroke_width=4)
            
            c_pt = axes.c2p(c, case["func"](c))
            c_dot = Dot(c_pt, color=YELLOW, radius=0.08)
            c_label = MathTex("c", font_size=30, color=YELLOW).next_to(c_dot, UP)

            # 극값 접선 (수평 접선 기울기 0)
            tan_line = Line(axes.c2p(c - 0.8, case["func"](c)), axes.c2p(c + 0.8, case["func"](c)), color=YELLOW, stroke_width=2.5)

            card_title = Text(case["title"], font_size=24, color=WHITE, weight=BOLD)
            ratio_tex = MathTex(case["ratio"], font_size=28, color=case["color"])
            c_calc = MathTex(f"c = \\frac{{{c:.2f}}}", font_size=26, color=GRAY_A)
            card = VGroup(card_title, ratio_tex).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            card.to_edge(RIGHT, buff=0.8).shift(DOWN * 0.4)

            if curr_curve is None:
                self.play(Create(curve), FadeIn(c_dot, c_label, tan_line, card))
            else:
                self.play(
                    Transform(curr_curve, curve),
                    Transform(curr_c_dot, VGroup(c_dot, c_label, tan_line)),
                    FadeOut(curr_card),
                    FadeIn(card)
                )

            curr_curve = curve
            curr_c_dot = VGroup(c_dot, c_label, tan_line)
            curr_card = card
            self.wait(1.5)

        # 마무리 메시지
        conclusion = Text("다항함수 극값 비율 관계는 외우지 말고 m : n 내분점으로 끝!", font_size=22, color=YELLOW)
        conclusion.next_to(axes, DOWN, buff=0.35)
        self.play(Write(conclusion))
        self.wait(2)
