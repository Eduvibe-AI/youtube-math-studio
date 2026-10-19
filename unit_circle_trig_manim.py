from manim import *
import numpy as np

class UnitCircleTrigScene(Scene):
    def construct(self):
        # Dark modern background
        self.camera.background_color = "#0b1120"

        # 1. Title Banner
        title = Text("단위원(Unit Circle)으로 조지는 삼각함수", font="Malgun Gothic", font_size=34, color=YELLOW)
        subtitle = Text("배상면 선생님의 통찰: 정의 · 대칭성 · 그래프 · 삼각부등식", font="Malgun Gothic", font_size=20, color=BLUE_B)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.4)

        self.play(Write(title), FadeIn(subtitle, shift=UP))
        self.wait(1)

        # 2. Setup Unit Circle & Coordinates (Left side)
        plane = NumberPlane(
            x_range=[-1.8, 1.8, 1],
            y_range=[-1.8, 1.8, 1],
            x_length=4.5,
            y_length=4.5,
            background_line_style={"stroke_color": "#1e293b", "stroke_width": 1.5}
        ).move_to(LEFT * 3 + DOWN * 0.5)

        circle = Circle(radius=plane.c2p(1, 0)[0] - plane.c2p(0, 0)[0], color=WHITE, stroke_width=2.5)
        circle.move_to(plane.c2p(0, 0))

        eq_circle = MathTex(r"x^2 + y^2 = 1", font_size=24, color=GRAY_B)
        eq_circle.next_to(circle, UP, buff=0.15)

        self.play(Create(plane), Create(circle), FadeIn(eq_circle))
        self.wait(1)

        # 3. Rotating Angle theta = 50 degrees
        theta_val = 50 * DEGREES
        p_coords = np.array([np.cos(theta_val), np.sin(theta_val), 0])
        p_pt = plane.c2p(p_coords[0], p_coords[1])
        origin_pt = plane.c2p(0, 0)
        x_proj_pt = plane.c2p(p_coords[0], 0)

        # Ray & Angle Arc
        op_ray = Line(origin_pt, p_pt, color=YELLOW, stroke_width=3.5)
        dot_p = Dot(p_pt, color=YELLOW, radius=0.08)
        label_p = MathTex(r"P(\cos\theta, \sin\theta)", font_size=26, color=YELLOW)
        label_p.next_to(p_pt, UR, buff=0.1)

        angle_arc = Angle(Line(origin_pt, plane.c2p(1, 0)), op_ray, radius=0.6, color=TEAL)
        label_theta = MathTex(r"\theta", font_size=22, color=TEAL).next_to(angle_arc, RIGHT, buff=0.1)

        # Projections: cos (x) and sin (y)
        line_cos = Line(origin_pt, x_proj_pt, color=BLUE, stroke_width=4)
        line_sin = Line(x_proj_pt, p_pt, color=GREEN, stroke_width=4)

        label_cos = MathTex(r"\cos\theta\text{ (x좌표)}", font_size=20, color=BLUE).next_to(line_cos, DOWN, buff=0.1)
        label_sin = MathTex(r"\sin\theta\text{ (y좌표)}", font_size=20, color=GREEN).next_to(line_sin, RIGHT, buff=0.1)

        self.play(Create(op_ray), Create(dot_p), FadeIn(label_p), Create(angle_arc), FadeIn(label_theta))
        self.wait(0.5)
        self.play(Create(line_cos), FadeIn(label_cos), Create(line_sin), FadeIn(label_sin))
        self.wait(1)

        # Right side explanation panel
        info_box = RoundedRectangle(corner_radius=0.15, width=5.5, height=4.5, color=BLUE_D, fill_color="#0f172a", fill_opacity=0.9)
        info_box.move_to(RIGHT * 3.2 + DOWN * 0.5)

        info_title = Text("1. 단위원과 삼각함수의 본질", font="Malgun Gothic", font_size=22, color=YELLOW)
        info_title.next_to(info_box.get_top(), DOWN, buff=0.3)

        info_t1 = MathTex(r"\bullet\ \text{x좌표} = \cos\theta", font_size=24, color=BLUE).next_to(info_title, DOWN, buff=0.3).align_to(info_box, LEFT).shift(RIGHT * 0.5)
        info_t2 = MathTex(r"\bullet\ \text{y좌표} = \sin\theta", font_size=24, color=GREEN).next_to(info_t1, DOWN, buff=0.25).align_to(info_t1, LEFT)
        info_t3 = MathTex(r"\bullet\ \text{기울기} = \tan\theta = \frac{\sin\theta}{\cos\theta}", font_size=24, color=PINK).next_to(info_t2, DOWN, buff=0.25).align_to(info_t1, LEFT)
        info_t4 = MathTex(r"\bullet\ \cos^2\theta + \sin^2\theta = 1", font_size=26, color=YELLOW).next_to(info_t3, DOWN, buff=0.3).align_to(info_t1, LEFT)

        self.play(Create(info_box), FadeIn(info_title), LaggedStart(Write(info_t1), Write(info_t2), Write(info_t3), Write(info_t4), lag_ratio=0.3))
        self.wait(2)

        # 4. Symmetries: Negative Angle (-theta) & pi - theta
        self.play(
            FadeOut(info_t1), FadeOut(info_t2), FadeOut(info_t3), FadeOut(info_t4),
            FadeOut(label_cos), FadeOut(label_sin)
        )

        sym_title = Text("2. 대칭성과 각변환 공식", font="Malgun Gothic", font_size=22, color=YELLOW)
        sym_title.move_to(info_title)

        # Point Q: x-axis symmetry -> -theta
        q_pt = plane.c2p(p_coords[0], -p_coords[1])
        dot_q = Dot(q_pt, color=RED, radius=0.08)
        op_q = Line(origin_pt, q_pt, color=RED, stroke_width=2.5)
        label_q = MathTex(r"Q(\cos\theta, -\sin\theta)", font_size=22, color=RED).next_to(q_pt, DR, buff=0.1)

        sym_t1 = MathTex(r"\text{x축 대칭 } (-\theta):", font_size=22, color=RED).next_to(sym_title, DOWN, buff=0.3).align_to(info_box, LEFT).shift(RIGHT * 0.4)
        sym_t2 = MathTex(r"\cos(-\theta) = \cos\theta", font_size=22, color=WHITE).next_to(sym_t1, DOWN, buff=0.15).align_to(sym_t1, LEFT)
        sym_t3 = MathTex(r"\sin(-\theta) = -\sin\theta", font_size=22, color=WHITE).next_to(sym_t2, DOWN, buff=0.15).align_to(sym_t1, LEFT)

        sym_t4 = MathTex(r"\text{y축 대칭 } (\pi - \theta):", font_size=22, color=TEAL).next_to(sym_t3, DOWN, buff=0.3).align_to(sym_t1, LEFT)
        sym_t5 = MathTex(r"\sin(\pi - \theta) = \sin\theta\text{ (높이 동일)}", font_size=22, color=WHITE).next_to(sym_t4, DOWN, buff=0.15).align_to(sym_t1, LEFT)
        sym_t6 = MathTex(r"\cos(\pi - \theta) = -\cos\theta", font_size=22, color=WHITE).next_to(sym_t5, DOWN, buff=0.15).align_to(sym_t1, LEFT)

        self.play(
            Transform(info_title, sym_title),
            Create(op_q), Create(dot_q), FadeIn(label_q),
            Write(sym_t1), Write(sym_t2), Write(sym_t3),
            Write(sym_t4), Write(sym_t5), Write(sym_t6)
        )
        self.wait(2)

        # 5. Trigonometric Inequality: sin(theta) < cos(theta)
        self.play(
            FadeOut(sym_t1), FadeOut(sym_t2), FadeOut(sym_t3),
            FadeOut(sym_t4), FadeOut(sym_t5), FadeOut(sym_t6),
            FadeOut(op_q), FadeOut(dot_q), FadeOut(label_q),
            FadeOut(op_ray), FadeOut(dot_p), FadeOut(label_p),
            FadeOut(angle_arc), FadeOut(label_theta),
            FadeOut(line_cos), FadeOut(line_sin)
        )

        ineq_title = Text("3. 삼각부등식 초고속 킬러 스킬", font="Malgun Gothic", font_size=22, color=YELLOW)
        ineq_title.move_to(info_title)

        # Draw line y = x across plane
        line_yx = Line(plane.c2p(-1.3, -1.3), plane.c2p(1.3, 1.3), color=PINK, stroke_width=3)
        label_yx = MathTex(r"y = x", font_size=24, color=PINK).next_to(plane.c2p(1.2, 1.2), UR, buff=0.1)

        # Intersections at 45 deg and 225 deg
        pt_45 = plane.c2p(np.sqrt(2)/2, np.sqrt(2)/2)
        pt_225 = plane.c2p(-np.sqrt(2)/2, -np.sqrt(2)/2)
        dot_45 = Dot(pt_45, color=YELLOW, radius=0.08)
        dot_225 = Dot(pt_225, color=YELLOW, radius=0.08)
        lbl_45 = MathTex(r"45^\circ\ (\frac{\pi}{4})", font_size=20, color=YELLOW).next_to(pt_45, UR, buff=0.1)
        lbl_225 = MathTex(r"225^\circ\ (\frac{5\pi}{4})", font_size=20, color=YELLOW).next_to(pt_225, DL, buff=0.1)

        # Highlight solution arcs (where y < x, below the line)
        r_circ = circle.radius
        arc1 = Arc(radius=r_circ, start_angle=0, angle=45*DEGREES, color=YELLOW, stroke_width=6, arc_center=plane.c2p(0, 0))
        arc2 = Arc(radius=r_circ, start_angle=225*DEGREES, angle=135*DEGREES, color=YELLOW, stroke_width=6, arc_center=plane.c2p(0, 0))

        iq_t1 = MathTex(r"\sin\theta < \cos\theta \iff y < x", font_size=24, color=YELLOW).next_to(ineq_title, DOWN, buff=0.3).align_to(info_box, LEFT).shift(RIGHT * 0.4)
        iq_t2 = Text("직선 y = x 의 아래쪽(y < x) 단위원 영역!", font="Malgun Gothic", font_size=18, color=WHITE).next_to(iq_t1, DOWN, buff=0.25).align_to(iq_t1, LEFT)
        iq_t3 = MathTex(r"\text{교점: } \theta = 45^\circ, 225^\circ", font_size=22, color=PINK).next_to(iq_t2, DOWN, buff=0.25).align_to(iq_t1, LEFT)
        iq_t4 = MathTex(r"\therefore\ 0 \le \theta < \frac{\pi}{4}\ \cup\ \frac{5\pi}{4} < \theta < 2\pi", font_size=22, color=GREEN_B).next_to(iq_t3, DOWN, buff=0.3).align_to(iq_t1, LEFT)

        self.play(
            Transform(info_title, ineq_title),
            Create(line_yx), FadeIn(label_yx),
            Create(dot_45), FadeIn(lbl_45),
            Create(dot_225), FadeIn(lbl_225)
        )
        self.wait(1)

        self.play(
            Write(iq_t1), FadeIn(iq_t2),
            Create(arc1), Create(arc2)
        )
        self.wait(1)
        self.play(Write(iq_t3), Write(iq_t4))
        self.wait(3)
