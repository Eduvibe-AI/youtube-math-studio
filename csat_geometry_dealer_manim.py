"""
수능 기하 총정리 (수학딜러 핵심 정리 마스터)
3Blue1Brown 스타일 Manim 애니메이션 스크립트

포함 주제:
1. 직각삼각형 엮임 & 삼각비 등비수열 체인 (a, a*tanθ, a*tan^2θ)
2. 접현각 & 공통접선에 의한 평행선 유도 (Alternate Segment & Parallel Chords)
3. 방멱의 정리 / 할선정리 3대 공식 (Power of a Point Theorem)

실행 방법:
manim -pql csat_geometry_dealer_manim.py CSATGeometryMasterScene
"""

from manim import *
import numpy as np

class CSATGeometryMasterScene(Scene):
    def construct(self):
        # 1. 인트로 타이틀
        title = Title("수능 기하 7대 핵심 정리 & 실전 태도", include_underline=True)
        title.set_color(GOLD)
        subtitle = Text("수학딜러 파이널 특강: 평행선 · 직각삼각형 체인 · 접현각 · 할선정리", font_size=20, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        # ==============================================================
        # PART 1: 직각삼각형 체인 & 등비수열
        # ==============================================================
        part1_label = Text("Part 1. 엮인 직각삼각형 & 등비수열 체인", font_size=24, color=BLUE_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part1_label))

        # 직각삼각형 1: A(0,0), B(3,0), C(3, 1.8)
        pA = np.array([-3.5, -1.5, 0])
        pB = np.array([-0.5, -1.5, 0])
        pC = np.array([-0.5, 0.3, 0])
        pD = np.array([-2.3, 1.2, 0]) # 수선의 발 or 다음 직각삼각형

        t1 = Polygon(pA, pB, pC, color=BLUE, stroke_width=3, fill_color=BLUE, fill_opacity=0.15)
        right_angle1 = RightAngle(Line(pC, pB), Line(pA, pB), length=0.3, color=YELLOW)

        lbl_a = MathTex("a", font_size=26, color=WHITE).next_to(Line(pA, pB), DOWN, buff=0.15)
        lbl_atan = MathTex("a\\tan\\theta", font_size=26, color=YELLOW).next_to(Line(pB, pC), RIGHT, buff=0.15)
        arc_theta = Arc(radius=0.7, start_angle=0, angle=np.arctan(1.8/3.0), arc_center=pA, color=GOLD)
        lbl_theta = MathTex(r"\theta", font_size=22, color=GOLD).next_to(arc_theta, RIGHT, buff=0.1)

        self.play(Create(t1), Create(right_angle1), Write(lbl_a), Write(lbl_atan), Create(arc_theta), Write(lbl_theta))
        self.wait(1)

        # 직각삼각형 2 연쇄
        line_hypo = Line(pA, pC, color=TEAL, stroke_width=3)
        lbl_next = MathTex("a\\tan^2\\theta", font_size=26, color=GREEN).shift(LEFT * 1.5 + UP * 0.8)
        geom_note = MathTex(
            r"L_0 = a \;\longrightarrow\; L_1 = a\tan\theta \;\longrightarrow\; L_2 = a\tan^2\theta \quad (\text{공비 } \tan\theta \text{ 등비수열})",
            font_size=22, color=YELLOW
        ).to_edge(DOWN, buff=0.8)

        self.play(Create(line_hypo), Write(lbl_next), Write(geom_note))
        self.wait(2)

        self.play(
            FadeOut(t1), FadeOut(right_angle1), FadeOut(lbl_a), FadeOut(lbl_atan),
            FadeOut(arc_theta), FadeOut(lbl_theta), FadeOut(line_hypo), FadeOut(lbl_next),
            FadeOut(geom_note), FadeOut(part1_label)
        )

        # ==============================================================
        # PART 2: 접현각 & 공통접선 평행선 발견
        # ==============================================================
        part2_label = Text("Part 2. 접현각 (접선과 현의 각) & 평행선 발견", font_size=24, color=YELLOW).to_edge(UP, buff=1.0)
        self.play(FadeIn(part2_label))

        c1 = Circle(radius=1.6, color=BLUE, stroke_width=3).shift(LEFT * 1.8)
        # 접점 T
        pT = c1.get_bottom()
        tan_line = Line(pT + LEFT * 2.5, pT + RIGHT * 2.5, color=GOLD, stroke_width=2.5)

        # 원 위의 삼각형 T, P1, P2
        pP1 = c1.point_at_angle(np.pi * 0.2)
        pP2 = c1.point_at_angle(np.pi * 0.75)
        inscribed_tri = Polygon(pT, pP1, pP2, color=GREEN, stroke_width=2.5, fill_color=GREEN, fill_opacity=0.1)

        thm_text = MathTex(
            r"\angle \text{접현각} = \angle \text{원주각} = \theta",
            font_size=26, color=GOLD
        ).next_to(c1, RIGHT, buff=1.0).shift(UP * 0.8)

        parallel_note = MathTex(
            r"\text{외접 두 원 공통접선} \implies \text{엇각 상등} \implies \mathbf{l_1 \parallel l_2 \text{ (평행선 발견!)}}",
            font_size=22, color=BLUE_B
        ).next_to(thm_text, DOWN, buff=0.5)

        self.play(Create(c1), Create(tan_line), Create(inscribed_tri))
        self.play(Write(thm_text), Write(parallel_note))
        self.wait(2.5)

        self.play(
            FadeOut(c1), FadeOut(tan_line), FadeOut(inscribed_tri),
            FadeOut(thm_text), FadeOut(parallel_note), FadeOut(part2_label)
        )

        # ==============================================================
        # PART 3: 방멱의 정리 / 할선정리 (Power of a Point)
        # ==============================================================
        part3_label = Text("Part 3. 할선정리 (방멱) 3대 공식 마스터", font_size=24, color=GREEN_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part3_label))

        big_circle = Circle(radius=1.8, color=BLUE_C, stroke_width=3).shift(LEFT * 2.2)
        self.play(Create(big_circle))

        # 외부 점 P
        ptP = big_circle.get_center() + LEFT * 3.2 + UP * 0.5
        dotP = Dot(ptP, color=RED)
        lblP = MathTex("P", font_size=26, color=RED).next_to(dotP, LEFT)

        # 접점 T
        ptT = big_circle.point_at_angle(np.pi * 0.6)
        linePT = Line(ptP, ptT, color=GOLD, stroke_width=3)
        dotT = Dot(ptT, color=YELLOW)
        lblT = MathTex("T", font_size=24, color=YELLOW).next_to(dotT, UP)

        # 할선 P-A-B
        ptA = big_circle.point_at_angle(np.pi * 0.95)
        ptB = big_circle.point_at_angle(np.pi * 0.05)
        linePAB = Line(ptP, ptB, color=TEAL, stroke_width=2.5)
        dotA = Dot(ptA, color=WHITE); dotB = Dot(ptB, color=WHITE)
        lblA = MathTex("A", font_size=22).next_to(dotA, UP, buff=0.1)
        lblB = MathTex("B", font_size=22).next_to(dotB, RIGHT, buff=0.1)

        self.play(
            FadeIn(dotP, lblP), Create(linePT), FadeIn(dotT, lblT),
            Create(linePAB), FadeIn(dotA, lblA, dotB, lblB)
        )

        # 3대 공식 요약 카드
        f_tangent = MathTex(r"\mathbf{1.\; PT^2 = PA \cdot PB}", font_size=24, color=GOLD)
        f_secants = MathTex(r"\mathbf{2.\; PA \cdot PB = PC \cdot PD \quad (\text{외부 두 할선})}", font_size=24, color=TEAL)
        f_chords  = MathTex(r"\mathbf{3.\; PA \cdot PB = PC \cdot PD \quad (\text{내부 두 현})}", font_size=24, color=GREEN)
        box_f = VGroup(f_tangent, f_secants, f_chords).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        box_f.next_to(big_circle, RIGHT, buff=0.8)
        surr_box = SurroundingRectangle(box_f, color=GOLD, buff=0.25, stroke_width=1.5)

        self.play(Create(surr_box), Write(box_f))
        self.wait(3)

        # 엔딩
        final_msg = Text("수능 현장: 각을 마킹하고, 닮음을 찾고, 공식을 바로 쓴다!", font_size=22, color=YELLOW)
        final_msg.to_edge(DOWN, buff=0.6)
        self.play(Write(final_msg))
        self.wait(2)
