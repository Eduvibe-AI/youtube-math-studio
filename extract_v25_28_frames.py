# -*- coding: utf-8 -*-
"""
Extract keyframe captures for Lectures 25, 26, 27, 28
"""
import os
import cv2

TASKS = [
    {
        'num': 25,
        'video': 'lecture_video25.mp4',
        'out_dir': 'captures_v25',
        'timestamps': [
            (20, "01_seq_expression.jpg"),
            (100, "02_ap_gp_basic.jpg"),
            (180, "03_big4_overview.jpg"),
            (330, "04_big3_difference.jpg"),
            (500, "05_big4_ratio.jpg"),
            (700, "06_alpha_technique.jpg"),
            (900, "07_three_term_linear.jpg"),
            (1100, "08_fractional_inverse.jpg"),
            (1300, "09_exp_log_transformation.jpg"),
            (1470, "10_master_summary.jpg"),
        ]
    },
    {
        'num': 26,
        'video': 'lecture_video26.mp4',
        'out_dir': 'captures_v26',
        'timestamps': [
            (15, "01_transcendental_vs_polynomial.jpg"),
            (60, "02_tangent_first_order.jpg"),
            (120, "03_curvature_second_order.jpg"),
            (180, "04_factorial_generalization.jpg"),
            (230, "05_exp_expansion.jpg"),
            (280, "06_sin_odd_powers.jpg"),
            (320, "07_cos_even_powers.jpg"),
            (360, "08_euler_link_summary.jpg"),
        ]
    },
    {
        'num': 27,
        'video': 'lecture_video27.mp4',
        'out_dir': 'captures_v27',
        'timestamps': [
            (60, "01_poly_intro.jpg"),
            (210, "02_factors_behavior.jpg"),
            (360, "03_cubic_point_symmetry.jpg"),
            (540, "04_tangent_ratio_two_to_one.jpg"),
            (720, "05_height_difference_formula.jpg"),
            (930, "06_diff_function_magic.jpg"),
            (1080, "07_quartic_double_tangent.jpg"),
            (1230, "08_quartic_triple_root.jpg"),
            (1370, "09_csat_killer_one_line.jpg"),
            (1480, "10_poly_master_map.jpg"),
        ]
    },
    {
        'num': 28,
        'video': 'lecture_video28.mp4',
        'out_dir': 'captures_v28',
        'timestamps': [
            (30, "01_14graphs_intro.jpg"),
            (180, "02_polynomial_four.jpg"),
            (450, "03_cubic_quartic_symmetry.jpg"),
            (720, "04_rational_hyperbola.jpg"),
            (960, "05_irrational_curve.jpg"),
            (1200, "06_exp_log_duality.jpg"),
            (1470, "07_trig_periodic_wave.jpg"),
            (1740, "08_circle_parabola.jpg"),
            (2100, "09_ellipse_hyperbola.jpg"),
            (2460, "10_14graphs_master_chart.jpg"),
        ]
    }
]

def process_task(task):
    vpath = task['video']
    out_dir = task['out_dir']
    os.makedirs(out_dir, exist_ok=True)
    if not os.path.exists(vpath):
        print(f"File not found: {vpath}")
        return
    cap = cv2.VideoCapture(vpath)
    if not cap.isOpened():
        print(f"Cannot open {vpath}")
        return
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"[{task['num']}] {vpath} - FPS: {fps:.2f}, Frames: {total_frames}")

    for sec, fname in task['timestamps']:
        frame_idx = min(int(sec * fps), total_frames - 1)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if ret:
            out_file = os.path.join(out_dir, fname)
            cv2.imwrite(out_file, frame)
            print(f"Saved: {out_file}")
        else:
            print(f"Failed at {sec}s for {vpath}")
    cap.release()

def main():
    for t in TASKS:
        process_task(t)
    print("All captures completed successfully!")

if __name__ == '__main__':
    main()
