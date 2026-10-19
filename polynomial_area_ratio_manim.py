"""
다항함수의 넓이의 비 (Polynomial Area Ratio) - 3Blue1Brown 스타일 Manim 스크립트
실행 방법: manim -pql polynomial_area_ratio_manim.py PolynomialAreaRatio
"""

from manim import *

class PolynomialAreaRatio(Scene):
    def construct(self):
        # 1. 제목 타이틀
        title = Title("수학II 적분법의 활용: 다항함수 넓이의 비", include_underline=True)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait(1)

        # 2. 좌표축 설정
        axes = Axes(
            x_range=[0, 1.4, 0.5],
            y_range=[0, 1.4, 0.5],
            x_length=5,
            y_length=5,
            axis_config={"color": BLUE_D, "include_numbers": True},
        ).to_edge(LEFT, buff=0.8)

        # (1, 1) 박스 (직사각형 영역)
        box = Polygon(
            axes.c2p(0, 0),
            axes.c2p(1, 0),
            axes.c2p(1, 1),
            axes.c2p(0, 1),
            stroke_color=WHITE,
            stroke_width=2,
            stroke_opacity=0.8,
            fill_opacity=0
        )
        box_label = MathTex("1 \\times 1 = 1", font_size=28).next_to(box, UP)

        self.play(Create(axes), Create(box), Write(box_label))
        self.wait(0.5)

        # 3. y = x^n 함수 그래프 초기화 (n=2)
        curve_n2 = axes.plot(lambda x: x**2, x_range=[0, 1.15], color=GREEN_B)
        curve_label = MathTex("y = x^n", font_size=34, color=GREEN_B).next_to(axes.c2p(1.1, 1.1), UP)

        # 영역 S1, S2 색칠
        area_s1 = axes.get_area(curve_n2, x_range=[0, 1], color=BLUE_C, opacity=0.6)
        
        # S2 영역 폴리곤 (상단 영역)
        points_s2 = [
            axes.c2p(0, 0),
            *[axes.c2p(x, x**2) for x in np.linspace(0, 1, 30)],
            axes.c2p(0, 1)
        ]
        area_s2 = Polygon(*points_s2, color=ORANGE, fill_opacity=0.6, stroke_width=0)

        label_s1 = MathTex("S_1", font_size=36, color=BLUE_C).move_to(axes.c2p(0.7, 0.2))
        label_s2 = MathTex("S_2", font_size=36, color=ORANGE).move_to(axes.c2p(0.3, 0.7))

        self.play(Create(curve_n2), Write(curve_label))
        self.play(FadeIn(area_s1), Write(label_s1))
        self.play(FadeIn(area_s2), Write(label_s2))
        self.wait(1)

        # 4. 수식 유도 파트 (우측 패널)
        formula_group = VGroup().to_edge(RIGHT, buff=0.8)

        f1 = MathTex(
            "S_1 = \\int_0^1 x^n dx = \\left[ \\frac{1}{n+1} x^{n+1} \\right]_0^1 = \\frac{1}{n+1}",
            font_size=32,
            color=BLUE_B
        )
        f2 = MathTex(
            "S_2 = 1 - S_1 = 1 - \\frac{1}{n+1} = \\frac{n}{n+1}",
            font_size=32,
            color=ORANGE
        )
        ratio_box = MathTex(
            "S_1 : S_2 = \\frac{1}{n+1} : \\frac{n}{n+1} = 1 : n",
            font_size=38,
            color=YELLOW
        )
        rect_surround = SurroundingRectangle(ratio_box, color=YELLOW, buff=0.2)

        f1.next_to(title, DOWN, buff=1.2).to_edge(RIGHT, buff=0.8)
        f2.next_to(f1, DOWN, buff=0.6, aligned_edge=LEFT)
        ratio_box.next_to(f2, DOWN, buff=0.8, aligned_edge=LEFT)
        rect_surround.move_to(ratio_box)

        self.play(Write(f1))
        self.wait(1)
        self.play(Write(f2))
        self.wait(1)
        self.play(Write(ratio_box), Create(rect_surround))
        self.wait(1.5)

        # 5. 차수별 적용 예시
        examples_title = Text("다항함수 차수별 적용", font_size=24, color=WHITE).next_to(rect_surround, DOWN, buff=0.6, aligned_edge=LEFT)
        ex2 = MathTex("n=2 \\; (2\\text{차}): \\; S_1 : S_2 = 1 : 2", font_size=30, color=GREEN_A).next_to(examples_title, DOWN, buff=0.3, aligned_edge=LEFT)
        ex3 = MathTex("n=3 \\; (3\\text{차}): \\; S_1 : S_2 = 1 : 3", font_size=30, color=GREEN_B).next_to(ex2, DOWN, buff=0.25, aligned_edge=LEFT)
        ex4 = MathTex("n=4 \\; (4\\text{차}): \\; S_1 : S_2 = 1 : 4", font_size=30, color=GREEN_C).next_to(ex3, DOWN, buff=0.25, aligned_edge=LEFT)

        self.play(Write(examples_title))
        self.play(FadeIn(ex2))
        self.wait(0.8)
        self.play(FadeIn(ex3))
        self.wait(0.8)
        self.play(FadeIn(ex4))
        self.wait(2)

        # 6. 마무리 페이드아웃
        self.play(FadeOut(Group(*self.mobjects)))
