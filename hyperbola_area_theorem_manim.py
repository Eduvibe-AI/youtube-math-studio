"""
직각쌍곡선(유리함수)의 기하학적 넓이 불변 정리 : S = T 증명과 자연로그의 기원
3Blue1Brown 스타일 Manim 애니메이션 스크립트

포함 주제:
1. 직각쌍곡선 xy = 1 (y = 1/x) 위의 두 점 A(a, 1/a), B(b, 1/b)
2. 부채꼴 영역 S (원점-호 AB)와 밑면 정적분 영역 T의 정의
3. 4단계 기하학적 영역 분할과 보라색 공통 삼각형 상쇄 (Inclusion-Exclusion)
4. S = T = ln(b/a)의 수학사적 의의 (1647년 그레고아 드 생뱅상 정리)

실행 방법:
manim -pql hyperbola_area_theorem_manim.py HyperbolaAreaTheoremScene
"""

from manim import *
import numpy as np

class HyperbolaAreaTheoremScene(Scene):
    def construct(self):
        # 1. Title
        title = Title("직각쌍곡선 넓이 정리: S = T 기하학적 증명", include_underline=True)
        title.set_color(GOLD)
        subtitle = Text("매스프레소 배상면 선생님 / 1647년 그레고아 드 생뱅상 정리", font_size=20, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        # ==============================================================
        # PART 1: 좌표계 및 직각쌍곡선 xy = 1 세팅
        # ==============================================================
        part1_label = Text("Part 1. 직각쌍곡선 y = 1/x 와 부채꼴 S, 적분 영역 T", font_size=24, color=BLUE_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part1_label))

        axes = Axes(
            x_range=[0, 4.5, 1],
            y_range=[0, 3.5, 1],
            x_length=7.5,
            y_length=4.5,
            axis_config={"color": GRAY_C, "include_numbers": False}
        ).shift(DOWN * 0.4 + LEFT * 1.5)

        x_lbl = MathTex("x", font_size=22).next_to(axes.x_axis, RIGHT)
        y_lbl = MathTex("y", font_size=22).next_to(axes.y_axis, UP)
        origin_lbl = MathTex("O", font_size=22).next_to(axes.c2p(0, 0), DL, buff=0.1)

        self.play(Create(axes), Write(x_lbl), Write(y_lbl), Write(origin_lbl))

        # Curve: y = 1/x for x in [0.35, 4.2]
        curve = axes.plot(lambda x: 1/x, x_range=[0.35, 4.2], color=WHITE, stroke_width=3)
        curve_lbl = MathTex(r"xy = 1 \iff y = \frac{1}{x}", font_size=24, color=YELLOW).next_to(axes.c2p(3.2, 0.4), UR)

        self.play(Create(curve), Write(curve_lbl))

        # Points A(a, 1/a) and B(b, 1/b)
        a_val = 0.8
        b_val = 2.5
        pA = axes.c2p(a_val, 1/a_val)
        pB = axes.c2p(b_val, 1/b_val)
        pO = axes.c2p(0, 0)
        pA_prime = axes.c2p(a_val, 0)
        pB_prime = axes.c2p(b_val, 0)

        dotA = Dot(pA, color=RED, radius=0.08)
        dotB = Dot(pB, color=BLUE, radius=0.08)
        lblA = MathTex(r"A\left(a, \frac{1}{a}\right)", font_size=22, color=RED).next_to(pA, UR, buff=0.1)
        lblB = MathTex(r"B\left(b, \frac{1}{b}\right)", font_size=22, color=BLUE).next_to(pB, UR, buff=0.1)

        self.play(FadeIn(dotA), Write(lblA), FadeIn(dotB), Write(lblB))
        self.wait(1)

        # Rays OA, OB and sector S
        line_OA = Line(pO, pA, color=RED_A, stroke_width=2)
        line_OB = Line(pO, pB, color=BLUE_A, stroke_width=2)
        
        # Sector polygon approximation
        xs_sector = np.linspace(a_val, b_val, 40)
        curve_pts = [axes.c2p(x, 1/x) for x in xs_sector]
        sector_poly = Polygon(pO, pA, *curve_pts, pB, fill_opacity=0.35, fill_color=PURPLE, stroke_width=0)
        lbl_S = MathTex("S", font_size=32, color=PURPLE_A).move_to(axes.c2p(0.8, 0.6))

        self.play(Create(line_OA), Create(line_OB), FadeIn(sector_poly), Write(lbl_S))
        self.wait(1.5)

        # Remove sector S, show integral area T
        self.play(FadeOut(sector_poly), FadeOut(lbl_S), FadeOut(line_OA), FadeOut(line_OB))

        # Vertical drops x=a, x=b
        line_drop_A = DashedLine(pA, pA_prime, color=RED, stroke_width=2)
        line_drop_B = DashedLine(pB, pB_prime, color=BLUE, stroke_width=2)
        lbl_a = MathTex("a", font_size=20).next_to(pA_prime, DOWN, buff=0.1)
        lbl_b = MathTex("b", font_size=20).next_to(pB_prime, DOWN, buff=0.1)

        # Area T
        integral_area = axes.get_area(curve, x_range=[a_val, b_val], color=TEAL, opacity=0.35)
        lbl_T = MathTex(r"T = \int_a^b \frac{1}{x} dx", font_size=26, color=TEAL_A).move_to(axes.c2p(1.6, 0.4))

        self.play(Create(line_drop_A), Create(line_drop_B), Write(lbl_a), Write(lbl_b), FadeIn(integral_area), Write(lbl_T))
        self.wait(2)

        # ==============================================================
        # PART 2: 4영역 분할 및 삼각형 등적변형 증명
        # ==============================================================
        self.play(
            FadeOut(part1_label),
            FadeOut(integral_area),
            FadeOut(lbl_T)
        )

        part2_label = Text("Part 2. 보라색 공통 영역 상쇄와 S = T 증명", font_size=24, color=GREEN_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part2_label))

        # Red Triangle OAA'
        tri_OAA = Polygon(pO, pA, pA_prime, fill_color=RED, fill_opacity=0.45, stroke_color=RED, stroke_width=2)
        formula_red = MathTex(
            r"\text{Area}(\triangle OAA') = \frac{1}{2} \cdot a \cdot \frac{1}{a} = \frac{1}{2}",
            font_size=22, color=RED
        ).to_edge(RIGHT, buff=0.6).shift(UP * 1.5)

        self.play(FadeIn(tri_OAA), Write(formula_red))
        self.wait(1.5)

        # Blue Triangle OBB'
        tri_OBB = Polygon(pO, pB, pB_prime, fill_color=BLUE, fill_opacity=0.4, stroke_color=BLUE, stroke_width=2)
        formula_blue = MathTex(
            r"\text{Area}(\triangle OBB') = \frac{1}{2} \cdot b \cdot \frac{1}{b} = \frac{1}{2}",
            font_size=22, color=BLUE
        ).next_to(formula_red, DOWN, buff=0.3)

        self.play(FadeIn(tri_OBB), Write(formula_blue))
        self.wait(1.5)

        # Intersection point C of line OB and vertical line x=a
        # Line OB equation: y = (1/b^2) * x  (since slope = (1/b)/b = 1/b^2)
        y_C = (1 / (b_val**2)) * a_val
        pC = axes.c2p(a_val, y_C)
        dotC = Dot(pC, color=PURPLE, radius=0.06)

        # Common purple triangle OA'C
        tri_purple = Polygon(pO, pA_prime, pC, fill_color=PURPLE, fill_opacity=0.7, stroke_color=PURPLE_A, stroke_width=1.5)
        formula_cancel = MathTex(
            r"\triangle OAA' - \text{공통} = \triangle OBB' - \text{공통}",
            font_size=22, color=PURPLE_A
        ).next_to(formula_blue, DOWN, buff=0.3)
        formula_pieces = MathTex(
            r"\implies \text{빨간 조각} = \text{파란 조각}",
            font_size=22, color=GOLD
        ).next_to(formula_cancel, DOWN, buff=0.2)

        self.play(FadeIn(tri_purple), FadeIn(dotC), Write(formula_cancel))
        self.wait(1.5)
        self.play(Write(formula_pieces))
        self.wait(1.5)

        # Add yellow curved region below arc AB
        formula_final = MathTex(
            r"+ \text{노란색 조각} \implies \mathbf{S = T}",
            font_size=28, color=YELLOW
        ).next_to(formula_pieces, DOWN, buff=0.4)

        box_final = SurroundingRectangle(formula_final, color=YELLOW, buff=0.15)

        self.play(Write(formula_final), Create(box_final))
        self.wait(2)

        # ==============================================================
        # PART 3: 결론 및 자연로그의 기원
        # ==============================================================
        conclusion = VGroup(
            MathTex(r"\mathbf{S = T = \int_a^b \frac{1}{x} dx = \ln\left(\frac{b}{a}\right)}", font_size=26, color=GOLD),
            Text("자연로그(ln)의 발견: 쌍곡선 아래 넓이의 기하학적 불변성", font_size=18, color=GRAY_B)
        ).arrange(DOWN, buff=0.2).next_to(box_final, DOWN, buff=0.4)

        self.play(Write(conclusion))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))
        final_text = Text("수학의 아름다움: 직각쌍곡선의 S = T 정리 완료", font_size=28, color=YELLOW)
        self.play(Write(final_text))
        self.wait(2)
