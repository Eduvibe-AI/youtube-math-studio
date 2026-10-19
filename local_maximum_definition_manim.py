"""
이게 극대라고?! 함수의 극대·극소의 진짜 수학적 정의
3Blue1Brown 스타일 Manim 애니메이션 스크립트

포함 주제:
1. 흔한 오개념: f'(a) = 0 이어야만 극대인가? (NO!)
2. 교과서의 엄밀한 정의: 열린구간 내에서 f(x) ≤ f(a)
3. 4대 극대 그래프 시각화 (첨점, 구멍 뚫린 상수함수, 계단식 불연속, 포물선 상단점)
4. 열린구간(Open Interval) 스트립과 보라색 극대점 검증
5. 배상면 선생님의 마법 암기: 극뾰대 & 극뻥대!

실행 방법:
manim -pql local_maximum_definition_manim.py LocalMaximumDefinitionScene
"""

from manim import *
import numpy as np

class LocalMaximumDefinitionScene(Scene):
    def construct(self):
        # 1. Title
        title = Title("함수의 극대: 뾰족해도 펑크 나도 극대다!", include_underline=True)
        title.set_color(GOLD)
        subtitle = Text("매스프레소 배상면 선생님 / 열린구간 부등식 정의 f(x) ≤ f(a)", font_size=20, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        # ==============================================================
        # PART 1: 수학Ⅱ 교과서 공식 정의
        # ==============================================================
        def_box = VGroup(
            Text("2015 / 2022 개정 교육과정 수학Ⅱ 교과서 정의", font_size=22, color=BLUE_B),
            MathTex(
                r"x = a\text{를 포함하는 어떤 열린구간의 모든 } x\text{에 대하여}",
                font_size=24, color=WHITE
            ),
            MathTex(
                r"\mathbf{f(x) \le f(a)}",
                font_size=36, color=YELLOW
            ),
            Text("일 때, 함수 f(x)는 x = a에서 '극대'라 하고, f(a)를 '극댓값'이라 한다.", font_size=20, color=GRAY_B),
            Text("※ 미분가능성, 연속성과는 완전히 무관함!", font_size=20, color=RED_B)
        ).arrange(DOWN, buff=0.25).shift(UP * 0.2)

        box_border = SurroundingRectangle(def_box, color=YELLOW, buff=0.3)

        self.play(Write(def_box), Create(box_border))
        self.wait(2)
        self.play(FadeOut(def_box), FadeOut(box_border))

        # ==============================================================
        # PART 2: 4대 그래프 그리드 세팅
        # ==============================================================
        part2_title = Text("다음 중 x = a에서 극대인 것은? (정답: 4개 모두 극대!)", font_size=24, color=GOLD).to_edge(UP, buff=1.0)
        self.play(FadeIn(part2_title))

        # 4 Mini-Axes
        # Top-Left: Cusp (첨점)
        # Top-Right: Punctured Constant (극뻥대)
        # Bottom-Left: Step Discontinuity
        # Bottom-Right: Punctured Parabola
        centers = [
            [-3.5, 1.2, 0],  # 1
            [2.5, 1.2, 0],   # 2
            [-3.5, -1.8, 0], # 3
            [2.5, -1.8, 0]   # 4
        ]

        labels = ["① 뾰족한 첨점 (극뾰대)", "② 펑크 난 상수함수 (극뻥대)", "③ 계단식 불연속", "④ 펑크 난 포물선"]
        colors = [TEAL, GREEN, BLUE, ORANGE]

        graphs_group = VGroup()

        for idx, (c, lbl_txt, col) in enumerate(zip(centers, labels, colors)):
            ax = Axes(
                x_range=[-1.5, 1.5, 1],
                y_range=[-1.0, 1.8, 1],
                x_length=4.5,
                y_length=2.5,
                axis_config={"color": GRAY_D, "stroke_width": 1.5}
            ).move_to(c)

            lbl = Text(lbl_txt, font_size=16, color=col).next_to(ax, UP, buff=0.1)

            # Dashed vertical line x = a (x = 0)
            line_a = DashedLine(ax.c2p(0, -1.0), ax.c2p(0, 1.8), color=GRAY_B, stroke_width=1.5)
            lbl_a = MathTex("a", font_size=18, color=GRAY_B).next_to(ax.c2p(0, -1.0), DOWN, buff=0.1)

            # Red interval strip (a - delta, a + delta)
            strip = Polygon(
                ax.c2p(-0.35, -1.0), ax.c2p(0.35, -1.0), ax.c2p(0.35, 1.8), ax.c2p(-0.35, 1.8),
                fill_color=RED, fill_opacity=0.2, stroke_width=0
            )

            # Curves & Points
            if idx == 0:
                # Cusp: y = 1.2 - 1.2 * |x|
                curve = ax.plot(lambda x: 1.2 - 1.2 * abs(x), x_range=[-1.2, 1.2], color=YELLOW, stroke_width=2.5)
                dot_max = Dot(ax.c2p(0, 1.2), color=PURPLE_A, radius=0.08)
                sub_grp = VGroup(ax, lbl, line_a, lbl_a, strip, curve, dot_max)

            elif idx == 1:
                # Constant with hole: y = 0.2, dot at (0, 1.2)
                curve1 = ax.plot(lambda x: 0.2, x_range=[-1.2, -0.05], color=YELLOW, stroke_width=2.5)
                curve2 = ax.plot(lambda x: 0.2, x_range=[0.05, 1.2], color=YELLOW, stroke_width=2.5)
                hole = Circle(radius=0.06, color=YELLOW, fill_color=BLACK, fill_opacity=1).move_to(ax.c2p(0, 0.2))
                dot_max = Dot(ax.c2p(0, 1.2), color=PURPLE_A, radius=0.08)
                sub_grp = VGroup(ax, lbl, line_a, lbl_a, strip, curve1, curve2, hole, dot_max)

            elif idx == 2:
                # Step: left decreases to (0, -0.2), dot at (0, 0.8), right decreases from 0.8
                curve1 = ax.plot(lambda x: 0.8*x**2 - 0.2, x_range=[-1.2, -0.05], color=YELLOW, stroke_width=2.5)
                curve2 = ax.plot(lambda x: -0.8*x + 0.6, x_range=[0.05, 1.2], color=YELLOW, stroke_width=2.5)
                hole = Circle(radius=0.06, color=YELLOW, fill_color=BLACK, fill_opacity=1).move_to(ax.c2p(0, -0.2))
                dot_max = Dot(ax.c2p(0, 0.8), color=PURPLE_A, radius=0.08)
                sub_grp = VGroup(ax, lbl, line_a, lbl_a, strip, curve1, curve2, hole, dot_max)

            elif idx == 3:
                # Parabola with hole at bottom: y = 1.0 * x^2 - 0.3, dot at (0, 0.9)
                curve = ax.plot(lambda x: 1.0 * x**2 - 0.3, x_range=[-1.2, 1.2], color=YELLOW, stroke_width=2.5)
                hole = Circle(radius=0.06, color=YELLOW, fill_color=BLACK, fill_opacity=1).move_to(ax.c2p(0, -0.3))
                dot_max = Dot(ax.c2p(0, 0.9), color=PURPLE_A, radius=0.08)
                sub_grp = VGroup(ax, lbl, line_a, lbl_a, strip, curve, hole, dot_max)

            graphs_group.add(sub_grp)

        self.play(FadeIn(graphs_group))
        self.wait(2.5)

        # Highlight that in the red strip, the purple dot is the HIGHEST point!
        check_banner = VGroup(
            Text("✔ 빨간 열린구간 안에서 보라색 점 f(a)가 주변의 모든 점보다 항상 크거나 같다!", font_size=20, color=GREEN_B),
            MathTex(r"\mathbf{\forall x \in (a - \delta, a + \delta) \implies f(x) \le f(a)}", font_size=24, color=GOLD)
        ).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.3)

        self.play(Write(check_banner))
        self.wait(2.5)

        # ==============================================================
        # PART 3: 결론 및 배티 암기법
        # ==============================================================
        self.play(FadeOut(graphs_group), FadeOut(check_banner), FadeOut(part2_title))

        final_box = VGroup(
            Text("배상면 선생님의 극대 완전정복 암기 공식", font_size=24, color=GOLD),
            Text("1. 극뾰대 : 뾰족해도 주변보다 높으면 극대!", font_size=22, color=TEAL_A),
            Text("2. 극뻥대 : 구멍이 뻥 뚫려도 점이 위에 있으면 극대!", font_size=22, color=PINK),
            Text("3. 미분 불가능이나 불연속이라고 제끼지 말 것!", font_size=22, color=RED_B),
            MathTex(r"\mathbf{\text{극대의 본질은 미분이 아니라 '부등식 } f(x) \le f(a)\text{'이다!}}", font_size=26, color=YELLOW)
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        box_final = SurroundingRectangle(final_box, color=GOLD, buff=0.3)

        self.play(Write(final_box), Create(box_final))
        self.wait(3)

        self.play(FadeOut(final_box), FadeOut(box_final))
        end_text = Text("함수의 극대·극소 개념 완전 정복 완료!", font_size=32, color=YELLOW)
        self.play(Write(end_text))
        self.wait(2)
