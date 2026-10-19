from manim import *
import numpy as np

class ProductOfDivisorsScene(Scene):
    def construct(self):
        # Dark modern background
        self.camera.background_color = "#0f172a"

        # 1. Main Title Banner
        title = Text("자연수 N의 모든 약수의 총곱과 기하평균", font="Malgun Gothic", font_size=36, color=YELLOW)
        subtitle = Text("배상면 선생님의 명쾌한 원리: 짝(Pairing)과 기하평균", font="Malgun Gothic", font_size=20, color=BLUE_B)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2).to_edge(UP, buff=0.5)

        self.play(Write(title), FadeIn(subtitle, shift=UP))
        self.wait(1)

        # 2. Formula Teaser
        formula_box = Rectangle(width=9.0, height=1.4, color=YELLOW, fill_color="#1e293b", fill_opacity=0.9)
        formula_box.next_to(title_group, DOWN, buff=0.4)
        
        formula_text = MathTex(
            r"\prod_{d \mid N} d", r"=", r"\left(\sqrt{N}\right)^{d(N)}", r"=", r"N^{\frac{d(N)}{2}}"
        ).scale(1.1)
        formula_text.set_color_by_tex(r"\left(\sqrt{N}\right)^{d(N)}", YELLOW)
        formula_text.move_to(formula_box)

        self.play(Create(formula_box), Write(formula_text))
        self.wait(1.5)
        self.play(FadeOut(formula_box), FadeOut(formula_text))

        # 3. Case 1: N = 12 (Symmetric Pairing)
        case1_label = Text("예시 1: N = 12의 약수 (짝수 개 = 6개)", font="Malgun Gothic", font_size=24, color=TEAL_A)
        case1_label.next_to(title_group, DOWN, buff=0.5)
        self.play(FadeIn(case1_label))

        divisors_12 = [1, 2, 3, 4, 6, 12]
        div_mobs = VGroup(*[
            VGroup(
                Circle(radius=0.45, color=BLUE, fill_color="#1e1e38", fill_opacity=0.8),
                Text(str(d), font="Consolas", font_size=24, color=WHITE)
            )
            for d in divisors_12
        ]).arrange(RIGHT, buff=0.8).move_to(UP * 0.5)

        self.play(LaggedStart(*[FadeIn(mob, scale=0.8) for mob in div_mobs], lag_ratio=0.15))
        self.wait(1)

        # Draw symmetric arcs
        pairs = [(0, 5, RED), (1, 4, GREEN), (2, 3, ORANGE)]
        arcs = VGroup()
        pair_texts = VGroup()

        for idx1, idx2, col in pairs:
            p1 = div_mobs[idx1].get_bottom()
            p2 = div_mobs[idx2].get_bottom()
            d1, d2 = divisors_12[idx1], divisors_12[idx2]
            
            # Curved arc connecting the pair
            arc = CurvedArrow(p1, p2, angle=-TAU/4, color=col)
            eq_text = MathTex(f"{d1} \\times {d2} = 12", color=col).scale(0.8)
            eq_text.next_to(arc, DOWN, buff=0.1)

            arcs.add(arc)
            pair_texts.add(eq_text)

        self.play(
            AnimationGroup(
                Create(arcs[0]), FadeIn(pair_texts[0]),
                Create(arcs[1]), FadeIn(pair_texts[1]),
                Create(arcs[2]), FadeIn(pair_texts[2]),
                lag_ratio=0.4
            )
        )
        self.wait(1.5)

        # Total product calculation
        calc_12 = MathTex(
            r"P(12) = (1 \times 12) \times (2 \times 6) \times (3 \times 4) = 12^3 = (\sqrt{12})^6 = 1,728",
            font_size=28, color=YELLOW
        ).move_to(DOWN * 2.6)

        self.play(Write(calc_12))
        self.wait(2)

        self.play(
            FadeOut(case1_label), FadeOut(div_mobs),
            FadeOut(arcs), FadeOut(pair_texts), FadeOut(calc_12)
        )

        # 4. Geometric Mean Insight
        gm_title = Text("배상면 선생님의 통찰: 약수의 기하평균", font="Malgun Gothic", font_size=26, color=YELLOW)
        gm_title.next_to(title_group, DOWN, buff=0.5)
        self.play(FadeIn(gm_title))

        gm_exp1 = MathTex(
            r"d \times \frac{N}{d} = N = (\sqrt{N})^2",
            font_size=32, color=WHITE
        ).move_to(UP * 0.8)

        gm_exp2 = MathTex(
            r"\text{기하평균 (G.M.)} = \sqrt{d \times \frac{N}{d}} = \sqrt{N}",
            font_size=32, color=GREEN_B
        ).next_to(gm_exp1, DOWN, buff=0.4)

        gm_insight = Text(
            "\"약수 1개의 곱셈적 대표값(회당 기대치)은 항상 √N이다!\"",
            font="Malgun Gothic", font_size=22, color=GOLD_A
        ).next_to(gm_exp2, DOWN, buff=0.5)

        self.play(Write(gm_exp1))
        self.wait(1)
        self.play(Write(gm_exp2))
        self.wait(1)
        self.play(FadeIn(gm_insight, shift=UP))
        self.wait(2)

        self.play(FadeOut(gm_title), FadeOut(gm_exp1), FadeOut(gm_exp2), FadeOut(gm_insight))

        # 5. Case 2: N = 36 (Square Number, Odd number of divisors)
        case2_label = Text("예시 2: 완전제곱수 N = 36 (홀수 개 = 9개)", font="Malgun Gothic", font_size=24, color=PINK)
        case2_label.next_to(title_group, DOWN, buff=0.5)
        self.play(FadeIn(case2_label))

        divisors_36 = [1, 2, 3, 4, 6, 9, 12, 18, 36]
        div_mobs_36 = VGroup(*[
            VGroup(
                Circle(radius=0.35, color=YELLOW if d == 6 else BLUE, fill_color="#2a1b40" if d == 6 else "#1e1e38", fill_opacity=0.9),
                Text(str(d), font="Consolas", font_size=20, color=YELLOW if d == 6 else WHITE)
            )
            for d in divisors_36
        ]).arrange(RIGHT, buff=0.4).move_to(UP * 0.6)

        self.play(LaggedStart(*[FadeIn(mob, scale=0.8) for mob in div_mobs_36], lag_ratio=0.1))
        self.wait(1)

        # Highlight center 6
        center_pointer = Arrow(DOWN * 0.8, div_mobs_36[4].get_bottom(), color=YELLOW, buff=0.1)
        center_label = MathTex(r"6 = \sqrt{36}\text{ (단독 약수)}", font_size=24, color=YELLOW)
        center_label.next_to(center_pointer, DOWN, buff=0.1)

        self.play(Create(center_pointer), FadeIn(center_label))
        self.wait(1)

        calc_36 = MathTex(
            r"P(36) = 36^4 \times 6 = (\sqrt{36})^8 \times (\sqrt{36})^1 = (\sqrt{36})^9 = 6^9",
            font_size=28, color=YELLOW
        ).move_to(DOWN * 2.2)

        self.play(Write(calc_36))
        self.wait(2)

        self.play(
            FadeOut(case2_label), FadeOut(div_mobs_36),
            FadeOut(center_pointer), FadeOut(center_label), FadeOut(calc_36)
        )

        # 6. Final Universal Summary
        final_box = RoundedRectangle(corner_radius=0.2, width=10.0, height=3.0, color=GOLD, fill_color="#0b1329", fill_opacity=0.95)
        final_box.move_to(DOWN * 0.5)

        final_title = Text("약수의 총곱 핵심 공식 정리", font="Malgun Gothic", font_size=26, color=GOLD_B)
        final_title.next_to(final_box.get_top(), DOWN, buff=0.3)

        final_f1 = MathTex(r"\prod_{d \mid N} d = \left(\sqrt{N}\right)^{d(N)} = N^{\frac{d(N)}{2}}", font_size=36, color=YELLOW)
        final_f1.next_to(final_title, DOWN, buff=0.3)

        final_note = Text("약수의 개수가 짝수든 홀수든 모든 자연수 N에 대해 항상 성립!", font="Malgun Gothic", font_size=20, color=WHITE)
        final_note.next_to(final_f1, DOWN, buff=0.3)

        self.play(Create(final_box), FadeIn(final_title), Write(final_f1), FadeIn(final_note))
        self.wait(3)
