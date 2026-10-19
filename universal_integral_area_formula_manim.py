"""
정적분 넓이 공식 만능 정리 (Universal Integral Area Formula)
3Blue1Brown 스타일 Manim 애니메이션 스크립트

실행 방법:
manim -pql universal_integral_area_formula_manim.py UniversalIntegralAreaFormula
"""

from manim import *
import numpy as np

class UniversalIntegralAreaFormula(Scene):
    def construct(self):
        # 1. 메인 타이틀
        title = Title("정적분 넓이공식: 이거 하나면 끝 (만능 공식)", include_underline=True)
        title.set_color(YELLOW)
        subtitle = Text("모든 다항함수 정적분 넓이를 관통하는 단 하나의 공식", font_size=20, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        # 2. 만능 공식 배너 표시 (상단)
        universal_box = VGroup()
        formula_tex = MathTex(
            r"S = |a| \cdot \frac{m! \, n!}{(m+n+1)!} (\beta - \alpha)^{m+n+1}",
            font_size=36,
            color=YELLOW
        )
        box_rect = SurroundingRectangle(formula_tex, color=GOLD, buff=0.25, stroke_width=2)
        bg_rect = BackgroundRectangle(box_rect, color=BLACK, fill_opacity=0.8)
        universal_banner = VGroup(bg_rect, box_rect, formula_tex).to_edge(UP, buff=1.0)

        self.play(FadeIn(universal_banner))
        self.wait(1)

        # 3. 좌측: 좌표평면 및 그래프
        axes = Axes(
            x_range=[0, 4.5, 1],
            y_range=[-0.5, 3.5, 1],
            x_length=6.0,
            y_length=4.5,
            axis_config={"color": BLUE_C, "include_numbers": False},
        ).to_edge(LEFT, buff=0.6).shift(DOWN * 0.5)

        alpha_val = 1.0
        beta_val = 3.5

        alpha_dot = Dot(axes.c2p(alpha_val, 0), color=RED)
        beta_dot = Dot(axes.c2p(beta_val, 0), color=RED)
        alpha_label = MathTex(r"\alpha", font_size=32, color=RED).next_to(alpha_dot, DOWN)
        beta_label = MathTex(r"\beta", font_size=32, color=RED).next_to(beta_dot, DOWN)

        axis_group = VGroup(axes, alpha_dot, beta_dot, alpha_label, beta_label)
        self.play(Create(axes), FadeIn(alpha_dot, beta_dot, alpha_label, beta_label))

        # 4. 우측: 케이스별 설명 카드 패널
        right_panel = VGroup().to_edge(RIGHT, buff=0.8).shift(DOWN * 0.4)

        cases_data = [
            {
                "name": "1. 이차함수 (두 실근 관통)",
                "mn": "m = 1, \\quad n = 1",
                "calc": r"\frac{1! \cdot 1!}{3!} = \frac{1}{6}",
                "result": r"S = \frac{|a|}{6}(\beta-\alpha)^3",
                "color": TEAL,
                "func": lambda x: 1.6 * (x - 1.0) * (3.5 - x) if (1.0 <= x <= 3.5) else 0
            },
            {
                "name": "2. 삼차함수 (접선 & 관통점)",
                "mn": "m = 2, \\quad n = 1",
                "calc": r"\frac{2! \cdot 1!}{4!} = \frac{2}{24} = \frac{1}{12}",
                "result": r"S = \frac{|a|}{12}(\beta-\alpha)^4",
                "color": BLUE_D,
                "func": lambda x: 0.8 * ((x - 1.0)**2) * (3.5 - x) if (1.0 <= x <= 3.5) else 0
            },
            {
                "name": "3. 사차함수 (삼중접선 & 관통)",
                "mn": "m = 3, \\quad n = 1",
                "calc": r"\frac{3! \cdot 1!}{5!} = \frac{6}{120} = \frac{1}{20}",
                "result": r"S = \frac{|a|}{20}(\beta-\alpha)^5",
                "color": PURPLE_B,
                "func": lambda x: 0.35 * ((x - 1.0)**3) * (3.5 - x) if (1.0 <= x <= 3.5) else 0
            },
            {
                "name": "4. 사차함수 (이중접선 대칭)",
                "mn": "m = 2, \\quad n = 2",
                "calc": r"\frac{2! \cdot 2!}{5!} = \frac{4}{120} = \frac{1}{30}",
                "result": r"S = \frac{|a|}{30}(\beta-\alpha)^5",
                "color": GREEN_C,
                "func": lambda x: 0.65 * ((x - 1.0)**2) * ((3.5 - x)**2) if (1.0 <= x <= 3.5) else 0
            }
        ]

        current_curve = None
        current_area = None
        current_text_group = None

        for case in cases_data:
            # 새 곡선 플롯 및 영역 색칠
            curve = axes.plot(case["func"], x_range=[1.0, 3.5], color=case["color"], stroke_width=4)
            area = axes.get_area(curve, x_range=[1.0, 3.5], color=case["color"], opacity=0.55)

            # 설명 텍스트 카드 생성
            card_title = Text(case["name"], font_size=24, color=WHITE, weight=BOLD)
            mn_tex = MathTex(case["mn"], font_size=28, color=YELLOW_B)
            calc_tex = MathTex(r"\text{계수}: \;" + case["calc"], font_size=28, color=GRAY_A)
            res_tex = MathTex(case["result"], font_size=32, color=case["color"])
            res_rect = SurroundingRectangle(res_tex, color=case["color"], buff=0.15)

            card_group = VGroup(card_title, mn_tex, calc_tex, VGroup(res_rect, res_tex))
            card_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            card_group.to_edge(RIGHT, buff=0.8).shift(DOWN * 0.4)

            if current_curve is None:
                self.play(Create(curve), FadeIn(area), FadeIn(card_group))
            else:
                self.play(
                    Transform(current_curve, curve),
                    Transform(current_area, area),
                    FadeOut(current_text_group),
                    FadeIn(card_group)
                )

            current_curve = curve
            current_area = area
            current_text_group = card_group
            self.wait(1.5)

        # 5. 요약 결론 마무리
        self.wait(1)
        summary_text = Text(
            "지수의 팩토리얼 분수만 기억하면 수능 정적분 넓이 3초 해결!",
            font_size=24,
            color=YELLOW
        ).next_to(axes, DOWN, buff=0.4)
        self.play(Write(summary_text))
        self.wait(2)
