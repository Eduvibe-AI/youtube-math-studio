"""
AngleBisectorGeomManim (제34강 시각화)
중학도형 핵심: 삼각형의 내각의 이등분선 정리 AB : AC = BD : CD
무게중심 2 : 1 내분과 6개 삼각형의 넓이 등분
"""

from manim import *
import numpy as np

class AngleBisectorGeomScene(Scene):
    def construct(self):
        title = Text("중학도형 핵심 정리: 각의 이등분선 & 무게중심", font_size=36, color=YELLOW)
        subtitle = Text("내각의 이등분선 정리 AB : AC = BD : CD", font_size=22, color=BLUE_B)
        VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP)
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)

        # Triangle ABC
        pt_A = np.array([0, 1.8, 0])
        pt_B = np.array([-3.2, -1.8, 0])
        pt_C = np.array([3.6, -1.8, 0])

        c = np.linalg.norm(pt_A - pt_B)
        b = np.linalg.norm(pt_A - pt_C)
        t = c / (b + c)
        pt_D = pt_B + t * (pt_C - pt_B)

        tri = Polygon(pt_A, pt_B, pt_C, color=BLUE, stroke_width=3)
        bisector = Line(pt_A, pt_D, color=RED, stroke_width=3.5)

        lbl_A = Tex("A").scale(0.8).next_to(pt_A, UP)
        lbl_B = Tex("B").scale(0.8).next_to(pt_B, DOWN+LEFT)
        lbl_C = Tex("C").scale(0.8).next_to(pt_C, DOWN+RIGHT)
        lbl_D = Tex("D").scale(0.8).next_to(pt_D, DOWN)

        self.play(Create(tri), Write(lbl_A), Write(lbl_B), Write(lbl_C))
        self.play(Create(bisector), Write(lbl_D))

        # Angle arcs at A
        arc1 = Arc(radius=0.5, start_angle=-2.2, angle=0.6, arc_center=pt_A, color=YELLOW)
        arc2 = Arc(radius=0.5, start_angle=-1.6, angle=0.6, arc_center=pt_A, color=YELLOW)
        self.play(Create(arc1), Create(arc2))

        # Formula Callout
        formula_box = RoundedRectangle(corner_radius=0.2, width=6.2, height=1.6, color=GOLD, fill_opacity=0.15).to_edge(DOWN)
        formula = Tex(r"\frac{\overline{AB}}{\overline{AC}} = \frac{\overline{BD}}{\overline{CD}} \iff \overline{AB} : \overline{AC} = \overline{BD} : \overline{CD}", font_size=28, color=YELLOW).move_to(formula_box)

        self.play(FadeIn(formula_box), Write(formula))
        self.wait(2)
