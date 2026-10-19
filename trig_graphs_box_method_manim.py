"""
삼각함수 그래프 완전 정복 (8칸 박스법과 파라미터 변환)
3Blue1Brown 스타일 Manim 애니메이션 스크립트

포함 주제:
1. 8칸 박스법(4등분 격자)을 활용한 사인 & 코사인 기본 작도
2. 파라미터 a, b, c, d의 기하학적 변환 (진폭, 주기, 평행이동)
3. 수능/내신 실전: 그래프에서 계수 초고속 역추적 알고리즘

실행 방법:
manim -pql trig_graphs_box_method_manim.py TrigGraphsBoxMethodScene
"""

from manim import *
import numpy as np

class TrigGraphsBoxMethodScene(Scene):
    def construct(self):
        # 1. 메인 타이틀
        title = Title("삼각함수 그래프 완전 정복: 8칸 박스법", include_underline=True)
        title.set_color(GOLD)
        subtitle = Text("사오수학 17강: 주기 4등분과 최대·최소 중심선의 완벽한 시각화", font_size=20, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        # ==============================================================
        # PART 1: 8칸 박스 격자 작도와 기본 파형
        # ==============================================================
        part1_label = Text("Part 1. 8칸 박스법(4등분 격자)으로 그리는 sin & cos", font_size=24, color=BLUE_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part1_label))

        axes = Axes(
            x_range=[-0.5, 7.0, 1],
            y_range=[-2.2, 2.2, 1],
            x_length=9.0,
            y_length=4.5,
            axis_config={"color": BLUE_E, "include_numbers": False}
        ).shift(DOWN * 0.3)

        self.play(Create(axes))

        # 8-box grid: 4 columns (width = 2pi / 4 = pi/2 ~ 1.57), 2 rows (height = 1 each)
        grid_lines = VGroup()
        x_steps = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
        x_labels = [r"0", r"\frac{\pi}{2}", r"\pi", r"\frac{3\pi}{2}", r"2\pi"]

        # Vertical grid lines
        for x_val, lbl_str in zip(x_steps, x_labels):
            p_top = axes.c2p(x_val, 1)
            p_bot = axes.c2p(x_val, -1)
            line = DashedLine(p_bot, p_top, color=GRAY_D, stroke_width=1.5)
            lbl = MathTex(lbl_str, font_size=20, color=YELLOW).next_to(axes.c2p(x_val, 0), DOWN, buff=0.25)
            grid_lines.add(line, lbl)

        # Horizontal grid lines (y = 1, y = 0, y = -1)
        line_top = DashedLine(axes.c2p(0, 1), axes.c2p(2*np.pi, 1), color=GRAY_C, stroke_width=2)
        line_mid = Line(axes.c2p(0, 0), axes.c2p(2*np.pi, 0), color=TEAL, stroke_width=1.5)
        line_bot = DashedLine(axes.c2p(0, -1), axes.c2p(2*np.pi, -1), color=GRAY_C, stroke_width=2)
        lbl_top = MathTex(r"+1 \text{ (최대)}", font_size=18, color=GREEN).next_to(axes.c2p(0, 1), LEFT)
        lbl_bot = MathTex(r"-1 \text{ (최소)}", font_size=18, color=RED).next_to(axes.c2p(0, -1), LEFT)
        grid_lines.add(line_top, line_mid, line_bot, lbl_top, lbl_bot)

        # Box outline
        box_rect = Rectangle(
            width=axes.c2p(2*np.pi, 0)[0] - axes.c2p(0, 0)[0],
            height=axes.c2p(0, 1)[1] - axes.c2p(0, -1)[1],
            color=GOLD, stroke_width=2
        ).move_to(axes.c2p(np.pi, 0))

        self.play(Create(box_rect), Create(grid_lines))
        self.wait(1)

        # Key 5 points for Sine: (0,0), (pi/2, 1), (pi, 0), (3pi/2, -1), (2pi, 0)
        sin_pts = [
            axes.c2p(0, 0), axes.c2p(np.pi/2, 1), axes.c2p(np.pi, 0),
            axes.c2p(3*np.pi/2, -1), axes.c2p(2*np.pi, 0)
        ]
        sin_dots = VGroup(*[Dot(p, color=YELLOW, radius=0.08) for p in sin_pts])

        sin_curve = axes.plot(lambda x: np.sin(x), x_range=[0, 2*np.pi], color=YELLOW, stroke_width=4)
        lbl_sin_fn = MathTex(r"y = \sin x", font_size=26, color=YELLOW).next_to(axes.c2p(np.pi/2, 1), UP, buff=0.2)

        self.play(FadeIn(sin_dots))
        self.play(Create(sin_curve), Write(lbl_sin_fn), run_time=2)
        self.wait(1.5)

        # Key 5 points for Cosine: (0,1), (pi/2, 0), (pi, -1), (3pi/2, 0), (2pi, 1)
        cos_curve = axes.plot(lambda x: np.cos(x), x_range=[0, 2*np.pi], color=BLUE_B, stroke_width=4)
        lbl_cos_fn = MathTex(r"y = \cos x", font_size=26, color=BLUE_B).next_to(axes.c2p(0, 1), UP, buff=0.2)

        self.play(FadeOut(sin_dots), sin_curve.animate.set_stroke(opacity=0.35))
        self.play(Create(cos_curve), Write(lbl_cos_fn), run_time=2)
        self.wait(2)

        self.play(
            FadeOut(axes), FadeOut(grid_lines), FadeOut(box_rect),
            FadeOut(sin_curve), FadeOut(cos_curve), FadeOut(lbl_sin_fn),
            FadeOut(lbl_cos_fn), FadeOut(part1_label)
        )

        # ==============================================================
        # PART 2: 파라미터 변환 공식 요약 y = a sin(bx + c) + d
        # ==============================================================
        part2_label = Text("Part 2. 일반형의 4대 핵심 분석 공식", font_size=24, color=GOLD).to_edge(UP, buff=1.0)
        self.play(FadeIn(part2_label))

        formula_card = VGroup(
            MathTex(r"\mathbf{y = a\sin(bx + c) + d = a\sin\left(b\left(x + \frac{c}{b}\right)\right) + d}", font_size=28, color=GOLD),
            MathTex(r"\text{1. 최댓값 } M = |a| + d, \quad \text{최솟값 } m = -|a| + d", font_size=24, color=WHITE),
            MathTex(r"\text{2. 진폭 } |a| = \frac{M - m}{2}, \quad \text{중심선 } d = \frac{M + m}{2}", font_size=24, color=TEAL),
            MathTex(r"\text{3. 주기 } T = \frac{2\pi}{|b|} \quad \left(x\text{축 방향 } \frac{1}{|b|}\text{배 압축}\right)", font_size=24, color=YELLOW),
            MathTex(r"\text{4. 평행이동: } x\text{축으로 } -\frac{c}{b}, \quad y\text{축으로 } +d", font_size=24, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).center().shift(DOWN * 0.2)

        surr_box = SurroundingRectangle(formula_card, color=GOLD, buff=0.3, stroke_width=1.5)

        self.play(Create(surr_box), Write(formula_card))
        self.wait(3)

        final_msg = Text("사오수학의 비법: 8칸 박스만 그리면 어떤 삼각함수도 10초 컷!", font_size=22, color=YELLOW)
        final_msg.to_edge(DOWN, buff=0.4)
        self.play(Write(final_msg))
        self.wait(2)
