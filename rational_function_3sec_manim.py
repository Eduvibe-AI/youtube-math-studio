"""
유리함수 평행이동과 나머지 정리 3초 풀이법
3Blue1Brown 스타일 Manim 애니메이션 스크립트

포함 주제:
1. 유리함수의 출생 함수 y = k/x와 평행이동 (곡률 불변성)
2. 교과서 나눗셈 vs 나머지 정리 1초 대입법 비교
3. 차길영 3초 풀이법: 선지 ①~⑤ 스피드런 및 정답 ③번 도출

실행 방법:
manim -pql rational_function_3sec_manim.py RationalFunction3SecScene
"""

from manim import *
import numpy as np

class RationalFunction3SecScene(Scene):
    def construct(self):
        # 1. Title
        title = Title("유리함수 평행이동: 나머지 정리 3초 풀이법", include_underline=True)
        title.set_color(GOLD)
        subtitle = Text("차길영의 세븐에듀: 출생 함수 y = k/x 와 분자 상수 초고속 도출", font_size=20, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        # ==============================================================
        # PART 1: 출생 함수 y = -3/x 와 평행이동
        # ==============================================================
        part1_label = Text("Part 1. 평행이동의 본질: 기본형 y = k/x 의 곡률 불변", font_size=24, color=BLUE_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part1_label))

        axes = Axes(
            x_range=[-5, 4, 1],
            y_range=[-4, 6, 1],
            x_length=7.5,
            y_length=4.5,
            axis_config={"color": GRAY_C, "include_numbers": False}
        ).shift(DOWN * 0.3)

        self.play(Create(axes))

        # Base hyperbola: y = -3/x
        # Branch 1: x in [-4.5, -0.4], Branch 2: x in [0.4, 3.5]
        hyp_base_left = axes.plot(lambda x: -3/x, x_range=[-4.5, -0.4], color=TEAL, stroke_width=2.5)
        hyp_base_right = axes.plot(lambda x: -3/x, x_range=[0.4, 3.5], color=TEAL, stroke_width=2.5)
        lbl_base = MathTex(r"y = \frac{-3}{x} \quad (k = -3)", font_size=22, color=TEAL).next_to(axes.c2p(2, -1.5), RIGHT)

        self.play(Create(hyp_base_left), Create(hyp_base_right), Write(lbl_base))
        self.wait(1)

        # Shifted hyperbola: y = (2x - 1)/(x + 1) = -3/(x + 1) + 2
        # Asymptotes: x = -1, y = 2
        asymp_v = DashedLine(axes.c2p(-1, -4), axes.c2p(-1, 6), color=YELLOW, stroke_width=2)
        asymp_h = DashedLine(axes.c2p(-5, 2), axes.c2p(4, 2), color=YELLOW, stroke_width=2)
        center_dot = Dot(axes.c2p(-1, 2), color=YELLOW)
        lbl_center = MathTex(r"(-1, 2)", font_size=18, color=YELLOW).next_to(center_dot, UR, buff=0.1)

        hyp_shift_left = axes.plot(lambda x: -3/(x+1) + 2, x_range=[-4.5, -1.4], color=RED_B, stroke_width=3)
        hyp_shift_right = axes.plot(lambda x: -3/(x+1) + 2, x_range=[-0.6, 3.5], color=RED_B, stroke_width=3)
        lbl_shift = MathTex(r"y = \frac{2x - 1}{x + 1} = \frac{-3}{x + 1} + 2", font_size=22, color=RED_B).next_to(axes.c2p(-1, 4), LEFT)

        self.play(Create(asymp_v), Create(asymp_h), FadeIn(center_dot, lbl_center))
        self.play(TransformFromCopy(hyp_base_left, hyp_shift_left),
                  TransformFromCopy(hyp_base_right, hyp_shift_right),
                  Write(lbl_shift))
        self.wait(2)

        self.play(FadeOut(hyp_base_left), FadeOut(hyp_base_right), FadeOut(lbl_base),
                  FadeOut(hyp_shift_left), FadeOut(hyp_shift_right), FadeOut(lbl_shift),
                  FadeOut(asymp_v), FadeOut(asymp_h), FadeOut(center_dot), FadeOut(lbl_center),
                  FadeOut(axes), FadeOut(part1_label))

        # ==============================================================
        # PART 2: 교과서 나눗셈 vs 나머지 정리 1초 공식
        # ==============================================================
        part2_label = Text("Part 2. 나머지 정리를 이용한 분자 k 초고속 판정", font_size=24, color=GREEN_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part2_label))

        box_math = VGroup(
            MathTex(r"\text{주어진 식: } y = \frac{2x - 1}{x + 1}", font_size=28, color=WHITE),
            MathTex(r"\text{1. 분모 } x + 1 = 0 \implies \mathbf{x = -1}", font_size=26, color=YELLOW),
            MathTex(r"\text{2. 분자 } 2x - 1 \text{에 대입: } 2(-1) - 1 = \mathbf{-3}", font_size=28, color=RED_B),
            MathTex(r"\implies \text{출생 함수: } \mathbf{y = \frac{-3}{x} \quad (k = -3)}", font_size=30, color=GOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(UP * 0.2)

        surr_rect = SurroundingRectangle(box_math, color=GOLD, buff=0.3)

        self.play(Write(box_math[0]))
        self.wait(0.5)
        self.play(Write(box_math[1]))
        self.wait(0.5)
        self.play(Write(box_math[2]))
        self.wait(0.5)
        self.play(Write(box_math[3]), Create(surr_rect))
        self.wait(1.5)

        # ==============================================================
        # PART 3: 5개 선지 스피드런 판정
        # ==============================================================
        self.play(FadeOut(box_math), FadeOut(surr_rect), FadeOut(part2_label))

        part3_label = Text("Part 3. 5개 선지 3초 스피드런 (k = -3 매칭)", font_size=24, color=GOLD).to_edge(UP, buff=1.0)
        self.play(FadeIn(part3_label))

        options = VGroup(
            MathTex(r"\text{① } y = \frac{2 - x}{x + 1} \implies 2 - (-1) = 3 \ne -3 \quad \text{\bf [탈락]}", font_size=22, color=GRAY_B),
            MathTex(r"\text{② } y = \frac{x + 4}{x + 1} \implies (-1) + 4 = 3 \ne -3 \quad \text{\bf [탈락]}", font_size=22, color=GRAY_B),
            MathTex(r"\text{③ } y = \frac{-2x - 5}{x + 1} \implies -2(-1) - 5 = \mathbf{-3} \quad \text{\bf [★ 정답! 일치 ★]}", font_size=24, color=GOLD),
            MathTex(r"\text{④ } y = \frac{x + 3}{x + 1} \implies (-1) + 3 = 2 \ne -3 \quad \text{\bf [탈락]}", font_size=22, color=GRAY_B),
            MathTex(r"\text{⑤ } y = \frac{2x + 1}{x + 1} \implies 2(-1) + 1 = -1 \ne -3 \quad \text{\bf [탈락]}", font_size=22, color=GRAY_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(DOWN * 0.3)

        match_box = SurroundingRectangle(options[2], color=YELLOW, buff=0.15)

        for i, opt in enumerate(options):
            self.play(FadeIn(opt), run_time=0.4)
            if i == 2:
                self.play(Create(match_box), run_time=0.5)

        self.wait(2)
