"""
y와 f(x)의 본질적 차이: 영토(Territory) vs 사람(Resident)
3Blue1Brown 스타일 Manim 애니메이션 스크립트

포함 주제:
1. 오리지널 함수 y = f(x) 그래프 세팅
2. |y| = f(x): y ≥ 0 영역 유지 + x축 대칭 복사 (상하 대칭형)
3. y = |f(x)|: f(x) < 0 곡선 꺾어 올리기 (V-Fold)
4. 배상면 선생님의 지구-적도 비유: y는 영토, f(x)는 사람!
5. 4대 절댓값 함수 그래프 핵심 정리

실행 방법:
manim -pql y_vs_fx_absolute_value_manim.py YVsFxAbsoluteValueScene
"""

from manim import *
import numpy as np

class YVsFxAbsoluteValueScene(Scene):
    def construct(self):
        # 1. Title
        title = Title("y와 f(x)의 차이: 영토 vs 사람 & 절댓값 그래프", include_underline=True)
        title.set_color(GOLD)
        subtitle = Text("매스프레소 배상면 선생님 / 절댓값 기하학 마스터", font_size=20, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        # ==============================================================
        # PART 1: 오리지널 곡선 y = f(x)
        # ==============================================================
        part1_label = Text("Part 1. 오리지널 함수 y = f(x)와 좌표평면", font_size=24, color=BLUE_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part1_label))

        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-2.5, 3.5, 1],
            x_length=7.5,
            y_length=4.5,
            axis_config={"color": GRAY_C, "include_numbers": False}
        ).shift(DOWN * 0.3)

        x_lbl = MathTex("x", font_size=22).next_to(axes.x_axis, RIGHT)
        y_lbl = MathTex("y", font_size=22).next_to(axes.y_axis, UP)
        origin_lbl = MathTex("O", font_size=22).next_to(axes.c2p(0, 0), DL, buff=0.1)

        self.play(Create(axes), Write(x_lbl), Write(y_lbl), Write(origin_lbl))

        # Original curve: cubic curve f(x) = 0.3 * (x + 2.5) * x * (x - 2.2)
        def func_f(x):
            return 0.28 * (x + 2.3) * x * (x - 2.0)

        curve_orig = axes.plot(func_f, x_range=[-2.7, 2.5], color=YELLOW, stroke_width=3)
        lbl_orig = MathTex(r"y = f(x)", font_size=24, color=YELLOW).next_to(axes.c2p(2.2, func_f(2.2)), UR)

        self.play(Create(curve_orig), Write(lbl_orig))
        self.wait(1.5)

        # ==============================================================
        # PART 2: |y| = f(x) 영토의 상하 대칭 복사
        # ==============================================================
        self.play(FadeOut(part1_label))
        part2_label = Text("Part 2. |y| = f(x) : 영토(y)의 상하 대칭 복사", font_size=24, color=TEAL_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part2_label))

        # Highlight y >= 0 and y < 0 zones
        rect_north = Polygon(
            axes.c2p(-3.5, 0), axes.c2p(3.5, 0), axes.c2p(3.5, 3.5), axes.c2p(-3.5, 3.5),
            fill_color=YELLOW, fill_opacity=0.12, stroke_width=0
        )
        rect_south = Polygon(
            axes.c2p(-3.5, -2.5), axes.c2p(3.5, -2.5), axes.c2p(3.5, 0), axes.c2p(-3.5, 0),
            fill_color=TEAL, fill_opacity=0.12, stroke_width=0
        )
        lbl_north = MathTex(r"y \ge 0 \text{ (북반구 영토)}", font_size=20, color=YELLOW).next_to(axes.c2p(-2.8, 2.8), RIGHT)
        lbl_south = MathTex(r"y < 0 \text{ (남반구 영토)}", font_size=20, color=TEAL).next_to(axes.c2p(-2.8, -1.8), RIGHT)

        self.play(FadeIn(rect_north), FadeIn(rect_south), Write(lbl_north), Write(lbl_south))
        self.wait(1)

        # Reflect y >= 0 curve across x-axis into y < 0
        # Positive intervals: x in [-2.3, 0] and x in [2.0, 2.5]
        def func_refl(x):
            val = func_f(x)
            return -val if val >= 0 else np.nan

        curve_pos_left = axes.plot(func_f, x_range=[-2.3, 0], color=YELLOW, stroke_width=3)
        curve_pos_right = axes.plot(func_f, x_range=[2.0, 2.5], color=YELLOW, stroke_width=3)

        curve_sym_left = axes.plot(lambda x: -func_f(x), x_range=[-2.3, 0], color=TEAL, stroke_width=3)
        curve_sym_right = axes.plot(lambda x: -func_f(x), x_range=[2.0, 2.5], color=TEAL, stroke_width=3)

        formula_abs_y = MathTex(
            r"|y| = f(x) \implies \begin{cases} y = f(x) & (y \ge 0) \\ y = -f(x) & (y < 0) \end{cases}",
            font_size=22, color=GOLD
        ).to_edge(RIGHT, buff=0.5).shift(UP * 1.5)

        badge_sym = Text("상하 대칭형 (함수 아님!)", font_size=20, color=TEAL_A).next_to(formula_abs_y, DOWN, buff=0.3)

        self.play(
            FadeOut(curve_orig),
            Create(curve_pos_left), Create(curve_pos_right),
            Create(curve_sym_left), Create(curve_sym_right),
            Write(formula_abs_y), FadeIn(badge_sym)
        )
        self.wait(2)

        # ==============================================================
        # PART 3: y = |f(x)| 사람(곡선)의 꺾어 올리기
        # ==============================================================
        self.play(
            FadeOut(part2_label), FadeOut(rect_north), FadeOut(rect_south),
            FadeOut(lbl_north), FadeOut(lbl_south),
            FadeOut(curve_sym_left), FadeOut(curve_sym_right),
            FadeOut(curve_pos_left), FadeOut(curve_pos_right),
            FadeOut(formula_abs_y), FadeOut(badge_sym)
        )

        part3_label = Text("Part 3. y = |f(x)| : 사람(함숫값)의 꺾어 올리기", font_size=24, color=RED_B).to_edge(UP, buff=1.0)
        self.play(FadeIn(part3_label))

        # Show original again with negative part highlighted
        curve_orig2 = axes.plot(func_f, x_range=[-2.7, 2.5], color=GRAY, stroke_width=1.8)
        curve_neg = axes.plot(func_f, x_range=[0, 2.0], color=RED, stroke_width=3.5)
        lbl_neg = MathTex(r"f(x) < 0 \text{ (남쪽 사람)}", font_size=20, color=RED).next_to(axes.c2p(1.0, -1.0), DOWN)

        self.play(Create(curve_orig2), Create(curve_neg), Write(lbl_neg))
        self.wait(1)

        # V-fold up: reflect negative part across x-axis
        curve_folded = axes.plot(lambda x: -func_f(x), x_range=[0, 2.0], color=YELLOW, stroke_width=3.5)
        lbl_vfold = Text("꺾어 올리기! (V-Fold)", font_size=20, color=YELLOW).next_to(axes.c2p(1.0, 1.2), UP)

        formula_abs_fx = MathTex(
            r"y = |f(x)| \implies \begin{cases} f(x) & (f(x) \ge 0) \\ -f(x) & (f(x) < 0) \end{cases}",
            font_size=22, color=YELLOW
        ).to_edge(RIGHT, buff=0.5).shift(UP * 1.5)

        self.play(
            Transform(curve_neg, curve_folded),
            FadeOut(lbl_neg),
            FadeIn(lbl_vfold),
            Write(formula_abs_fx)
        )
        self.wait(2)

        # ==============================================================
        # PART 4: 지구-적도 비유 & 결론
        # ==============================================================
        self.play(
            FadeOut(part3_label), FadeOut(curve_orig2), FadeOut(curve_neg),
            FadeOut(lbl_vfold), FadeOut(formula_abs_fx),
            FadeOut(lbl_orig), FadeOut(axes), FadeOut(x_lbl), FadeOut(y_lbl), FadeOut(origin_lbl)
        )

        epiphany_box = VGroup(
            Text("배상면 선생님의 촌철살인 정리:", font_size=22, color=GRAY_B),
            MathTex(r"\text{지구가 스케치북이면 } x\text{축은 적도!}", font_size=26, color=BLUE_B),
            MathTex(r"\mathbf{y\text{는 영토 (Territory)}, \quad f(x)\text{는 사람 (Resident)}}", font_size=32, color=GOLD),
            Text("• |y| = f(x) : 남반구 영토에 북반구 지도를 복사 (상하 대칭)", font_size=20, color=TEAL_A),
            Text("• y = |f(x)| : 남쪽에 사는 사람만 북쪽으로 이주 (꺾어 올리기)", font_size=20, color=YELLOW_A)
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        box_border = SurroundingRectangle(epiphany_box, color=GOLD, buff=0.3)

        self.play(Write(epiphany_box), Create(box_border))
        self.wait(3)

        self.play(FadeOut(epiphany_box), FadeOut(box_border))
        final_text = Text("y와 f(x)의 차이 마스터 완료!", font_size=30, color=YELLOW)
        self.play(Write(final_text))
        self.wait(2)
