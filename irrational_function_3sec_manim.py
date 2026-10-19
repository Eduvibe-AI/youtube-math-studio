"""
무리함수와 역함수의 교점 & 3초 풀이법
3Blue1Brown 스타일 Manim 애니메이션 스크립트

포함 주제:
1. 무리함수 f(x) = sqrt(x-3) + k 와 역함수의 교점 = y = x 와의 교점
2. k 값 변화에 따른 기하학적 교점 개수 (0개 -> 접함 1개 -> 2개 -> 1개)
3. 시작점 (3, k)가 y = x 위에 닿는 순간: k_max = 3 도출

실행 방법:
manim -pql irrational_function_3sec_manim.py IrrationalFunction3SecScene
"""

from manim import *
import numpy as np

class IrrationalFunction3SecScene(Scene):
    def construct(self):
        # 1. Title
        title = Title("무리함수와 역함수의 교점: 3초 풀이법", include_underline=True)
        title.set_color(GOLD)
        subtitle = Text("차길영의 세븐에듀: 시작점 (3, k)와 대칭축 y = x의 기하학", font_size=20, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        # ==============================================================
        # PART 1: 무리함수와 역함수, 그리고 대칭축 y = x
        # ==============================================================
        part1_label = Text("Part 1. 역함수와의 교점은 대칭축 y = x 위에서만 존재", font_size=24, color=BLUE_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part1_label))

        axes = Axes(
            x_range=[-1, 7, 1],
            y_range=[-1, 7, 1],
            x_length=6.0,
            y_length=6.0,
            axis_config={"color": GRAY_C, "include_numbers": False}
        ).shift(DOWN * 0.4)

        self.play(Create(axes))

        # Line y = x
        line_yx = axes.plot(lambda x: x, x_range=[-0.5, 6.5], color=YELLOW, stroke_width=2.5)
        lbl_yx = MathTex(r"y = x", font_size=22, color=YELLOW).next_to(axes.c2p(6, 6), UR, buff=0.1)
        self.play(Create(line_yx), Write(lbl_yx))

        # Case k = 3: f(x) = sqrt(x-3) + 3
        f_curve = axes.plot(lambda x: np.sqrt(x - 3) + 3, x_range=[3.0, 6.5], color=TEAL, stroke_width=3)
        lbl_f = MathTex(r"f(x) = \sqrt{x - 3} + 3", font_size=22, color=TEAL).next_to(axes.c2p(5.5, 4.5), DR)

        # Inverse: f^-1(x) = (x-3)^2 + 3 for x >= 3
        f_inv = axes.plot(lambda x: (x - 3)**2 + 3, x_range=[3.0, 4.8], color=PINK, stroke_width=2.5)
        lbl_inv = MathTex(r"f^{-1}(x)", font_size=20, color=PINK).next_to(axes.c2p(4.5, 5.2), UL)

        # Starting point (3, 3)
        start_dot = Dot(axes.c2p(3, 3), color=GOLD, radius=0.08)
        lbl_start = MathTex(r"(3, 3)", font_size=18, color=GOLD).next_to(start_dot, DL, buff=0.15)

        # Second intersection (4, 4)
        dot44 = Dot(axes.c2p(4, 4), color=RED_B, radius=0.08)
        lbl_44 = MathTex(r"(4, 4)", font_size=18, color=RED_B).next_to(dot44, UR, buff=0.15)

        self.play(Create(f_curve), Write(lbl_f), Create(f_inv), Write(lbl_inv))
        self.play(FadeIn(start_dot, lbl_start, dot44, lbl_44))
        self.wait(1.5)

        # Replace inverse with y = x
        replace_text = Text("역함수를 지우고 y = x와의 교점으로 치환!", font_size=20, color=YELLOW).to_edge(RIGHT, buff=0.8).shift(UP * 1.5)
        self.play(FadeOut(f_inv), FadeOut(lbl_inv), Write(replace_text))
        self.wait(1)

        self.play(FadeOut(f_curve), FadeOut(lbl_f), FadeOut(start_dot), FadeOut(lbl_start),
                  FadeOut(dot44), FadeOut(lbl_44), FadeOut(replace_text), FadeOut(part1_label))

        # ==============================================================
        # PART 2: k 변화에 따른 기하학적 교점 수와 최댓값
        # ==============================================================
        part2_label = Text("Part 2. 시작점 (3, k)가 y = x 위에 닿을 때 k가 최대!", font_size=24, color=GOLD).to_edge(UP, buff=1.0)
        self.play(FadeIn(part2_label))

        # Case 1: k = 3.6 (Too high -> 1 intersection)
        c_high = axes.plot(lambda x: np.sqrt(x - 3) + 3.6, x_range=[3.0, 6.5], color=RED, stroke_width=2)
        dot_high = Dot(axes.c2p(3, 3.6), color=RED)
        lbl_high = Text("k = 3.6: 시작점이 y=x 위쪽 -> 교점 1개 (실패)", font_size=16, color=RED).to_edge(RIGHT, buff=0.5).shift(UP * 1.8)

        self.play(Create(c_high), FadeIn(dot_high), Write(lbl_high))
        self.wait(1)

        # Case 2: k = 3.0 (Touch y=x -> 2 intersections, MAXIMUM!)
        c_max = axes.plot(lambda x: np.sqrt(x - 3) + 3.0, x_range=[3.0, 6.5], color=GOLD, stroke_width=3.5)
        dot_max = Dot(axes.c2p(3, 3.0), color=GOLD, radius=0.1)
        lbl_max = Text("k = 3.0: 시작점이 y=x 위 안착 -> 교점 2개 (최댓값!)", font_size=18, color=GOLD).to_edge(RIGHT, buff=0.5).shift(UP * 0.8)

        self.play(Transform(c_high, c_max), Transform(dot_high, dot_max), Write(lbl_max))
        self.wait(1.5)

        # Case 3: k = 2.75 (Tangent line D = 0)
        c_tan = axes.plot(lambda x: np.sqrt(x - 3) + 2.75, x_range=[3.0, 6.5], color=BLUE, stroke_width=2)
        lbl_tan = Text("k = 2.75 (11/4): 접할 때 (최솟값)", font_size=16, color=BLUE).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.2)

        self.play(Create(c_tan), Write(lbl_tan))
        self.wait(1.5)

        # Summary box
        self.play(FadeOut(lbl_high), FadeOut(lbl_max), FadeOut(lbl_tan), FadeOut(c_high), FadeOut(c_tan), FadeOut(dot_high))

        summary_box = VGroup(
            MathTex(r"\text{무리함수 } f(x) = \sqrt{x - 3} + k \text{의 시작점: } (3, k)", font_size=26, color=WHITE),
            MathTex(r"\text{두 점에서 만나기 위한 } k\text{의 상한: 시작점이 } y = x \text{ 위에 있을 때}", font_size=24, color=YELLOW),
            MathTex(r"x = y \implies 3 = k \implies \mathbf{k_{\max} = 3}", font_size=32, color=GOLD),
            MathTex(r"\text{실전 3초 판정: 시작점 } x\text{좌표가 곧 } k\text{의 최댓값!}", font_size=24, color=GREEN_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).to_edge(RIGHT, buff=0.6).shift(UP * 0.5)

        rect = SurroundingRectangle(summary_box, color=GOLD, buff=0.25)
        self.play(Write(summary_box), Create(rect))
        self.wait(2.5)
