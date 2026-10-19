"""
=============================================================================
Manim Animation: Euclid's Proof of the Pythagorean Theorem (유클리드 증명법)
Inspired by 3Blue1Brown Style Geometric Animations
Source Short: https://youtube.com/shorts/mHLirHeKkiQ (@yisrisri_math)
Formula: a^2 + b^2 = c^2 (Area(AHGI) + Area(GDEF) = Area(ABCD))
=============================================================================
Run with:
    manim -pql pythagorean_euclid_manim.py PythagoreanEuclidProof
=============================================================================
"""

from manim import *
import numpy as np

class PythagoreanEuclidProof(Scene):
    def construct(self):
        # 1. Title & Introduction
        title = Title(
            r"\textbf{피타고라스의 정리 — 유클리드 증명 (Euclid's Proof)}",
            font_size=38,
            color=BLUE_B
        )
        subtitle = Text(
            "유클리드 원론 제1권 47번 명제: a² + b² = c²",
            font_size=20,
            color=GRAY_B
        ).next_to(title, DOWN, buff=0.2)

        self.play(Write(title), FadeIn(subtitle, shift=UP))
        self.wait(1)
        self.play(FadeOut(subtitle), title.animate.scale(0.75).to_corner(UL))

        # 2. Coordinates Setup for Right Triangle AGD with hypotenuse AD at bottom
        # Let A = (-1.6, 0.5, 0), D = (1.6, 0.5, 0)
        # Right angle vertex G above AD. 
        # Using 3-4-5 proportion: a=2.4, b=3.2, c=4.0
        c_len = 3.2
        A = np.array([-c_len / 2, 0.2, 0])
        D = np.array([c_len / 2, 0.2, 0])
        
        # In standard 3-4-5 right triangle:
        # cos(angle_A) = 3/5 = 0.6, sin(angle_A) = 4/5 = 0.8
        # AG = 0.6 * c = 1.92, GD = 0.8 * c = 2.56
        # G relative to A: (AG * cos(theta), AG * sin(theta))
        theta = np.arccos(0.6) # approx 53.13 deg
        G = A + np.array([1.92 * np.cos(theta), 1.92 * np.sin(theta), 0])

        # Bottom square ABCD (side c): A -> B -> C -> D
        # Vector AD is (c_len, 0, 0), downward normal is (0, -1, 0)
        B = A + np.array([0, -c_len, 0])
        C = D + np.array([0, -c_len, 0])

        # Left square AHGI on AG (side a):
        # Vector AG:
        v_AG = G - A
        # perpendicular vector outward from hypotenuse:
        # AG rotated 90 deg counter-clockwise: (-v_AG[1], v_AG[0], 0)
        v_perp_AG = np.array([-v_AG[1], v_AG[0], 0])
        I = A + v_perp_AG
        H = G + v_perp_AG

        # Right square GDEF on GD (side b):
        v_GD = D - G
        # GD rotated 90 deg clockwise (outward): (v_GD[1], -v_GD[0], 0)
        v_perp_GD = np.array([v_GD[1], -v_GD[0], 0])
        E = D + v_perp_GD
        F = G + v_perp_GD

        # Perpendicular from G to BC: intersects AD at K, BC at J
        K = np.array([G[0], A[1], 0])
        J = np.array([G[0], B[1], 0])

        # 3. Draw Geometry
        tri_AGD = Polygon(A, G, D, color=WHITE, stroke_width=2.5, fill_color=DARK_BLUE, fill_opacity=0.3)
        sq_ABCD = Polygon(A, B, C, D, color=BLUE_D, stroke_width=2)
        sq_AHGI = Polygon(A, H, G, I, color=TEAL_D, stroke_width=2)
        sq_GDEF = Polygon(G, F, E, D, color=PURPLE_D, stroke_width=2)

        # Labels for vertices
        labels_dict = {
            "A": (A, DL), "D": (D, DR), "G": (G, UP),
            "B": (B, DL), "C": (C, DR), "J": (J, DOWN), "K": (K, UR*0.5),
            "H": (H, UL), "I": (I, LEFT), "E": (E, RIGHT), "F": (F, UR)
        }
        labels = VGroup(*[
            MathTex(k, font_size=20, color=YELLOW_B).next_to(pt, dir_vec, buff=0.12)
            for k, (pt, dir_vec) in labels_dict.items()
        ])

        line_GJ = DashedLine(G, J, color=YELLOW, stroke_width=2)

        self.play(Create(tri_AGD), run_time=1)
        self.play(Create(sq_ABCD), Create(sq_AHGI), Create(sq_GDEF), run_time=1.5)
        self.play(Create(line_GJ), Write(labels), run_time=1)
        self.wait(1)

        # 4. Step 1: Area of Triangle IAG = 1/2 Area(Square AHGI)
        tri_IAG = Polygon(I, A, G, color=TEAL_A, fill_color=TEAL, fill_opacity=0.55)
        step1_text = MathTex(
            r"\triangle IAG = \frac{1}{2} \square AHGI \quad (\text{밑변 } IA, \text{ 높이 } AG)",
            font_size=24, color=TEAL_B
        ).to_edge(DOWN)

        self.play(FadeIn(tri_IAG), Write(step1_text))
        self.wait(1.5)

        # 5. Step 2: Shear tri_IAG -> tri_IAD (Base IA parallel to GH, vertex moves G -> D)
        tri_IAD = Polygon(I, A, D, color=TEAL_A, fill_color=TEAL, fill_opacity=0.55)
        step2_text = MathTex(
            r"\triangle IAG = \triangle IAD \quad (\because \overline{IA} \parallel \overline{GH},\, \text{밑변 } IA \text{ 공통})",
            font_size=24, color=TEAL_B
        ).to_edge(DOWN)

        self.play(Transform(tri_IAG, tri_IAD), Transform(step1_text, step2_text))
        self.wait(1.5)

        # 6. Step 3: SAS Congruence: tri_IAD === tri_GAB (Rotation around A by 90 deg)
        tri_GAB = Polygon(G, A, B, color=GREEN_B, fill_color=GREEN, fill_opacity=0.55)
        step3_text = MathTex(
            r"\triangle IAD \equiv \triangle GAB \quad (\text{SAS 합동: } \overline{IA}=\overline{GA},\, \overline{AD}=\overline{AB},\, \angle IAD=\angle GAB)",
            font_size=23, color=GREEN_B
        ).to_edge(DOWN)

        self.play(Transform(tri_IAG, tri_GAB), Transform(step1_text, step3_text))
        self.wait(1.8)

        # 7. Step 4: Shear tri_GAB -> tri_JAB (Base AB parallel to line GJ, vertex moves G -> J)
        tri_JAB = Polygon(J, A, B, color=GREEN_B, fill_color=GREEN, fill_opacity=0.55)
        step4_text = MathTex(
            r"\triangle GAB = \triangle JAB = \frac{1}{2} \text{직사각형 } ABJK \quad (\because \overline{AB} \parallel \overline{GJ})",
            font_size=24, color=GREEN_B
        ).to_edge(DOWN)

        self.play(Transform(tri_IAG, tri_JAB), Transform(step1_text, step4_text))
        self.wait(1.5)

        # 8. Step 5: Area(Square AHGI) = Area(Rectangle ABJK) = a^2
        rect_ABJK = Polygon(A, B, J, K, color=TEAL, fill_color=TEAL, fill_opacity=0.6)
        sq_AHGI_filled = Polygon(A, H, G, I, color=TEAL, fill_color=TEAL, fill_opacity=0.6)
        step5_text = MathTex(
            r"\therefore \square AHGI = \text{직사각형 } ABJK = a^2",
            font_size=28, color=TEAL_B
        ).to_edge(DOWN)

        self.play(
            FadeOut(tri_IAG),
            FadeIn(sq_AHGI_filled),
            FadeIn(rect_ABJK),
            Transform(step1_text, step5_text)
        )
        self.wait(2)

        # 9. Step 6: Similarly for the Right Side: Square GDEF = Rectangle JKCD = b^2
        rect_JKCD = Polygon(K, J, C, D, color=PURPLE, fill_color=PURPLE, fill_opacity=0.6)
        sq_GDEF_filled = Polygon(G, F, E, D, color=PURPLE, fill_color=PURPLE, fill_opacity=0.6)
        step6_text = MathTex(
            r"\text{마찬가지로 우측도 } \square GDEF = \text{직사각형 } JKCD = b^2",
            font_size=28, color=PURPLE_B
        ).to_edge(DOWN)

        self.play(
            FadeIn(sq_GDEF_filled),
            FadeIn(rect_JKCD),
            Transform(step1_text, step6_text)
        )
        self.wait(2)

        # 10. Conclusion: a^2 + b^2 = c^2
        final_formula = MathTex(
            r"\mathbf{a^2 + b^2 = c^2}",
            font_size=46, color=YELLOW
        ).move_to(DOWN * 2.8)

        self.play(
            FadeOut(step1_text),
            Write(final_formula)
        )
        self.play(Circumscribe(final_formula, color=GOLD, stroke_width=4))
        self.wait(3)
