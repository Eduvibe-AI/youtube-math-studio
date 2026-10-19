# -*- coding: utf-8 -*-
"""
Extract keyframe captures for Lectures 29, 30, 31
"""
import os
import cv2

TASKS = [
    {
        'num': 29,
        'video': 'lecture_video29.mp4',
        'out_dir': 'captures_v29',
        'timestamps': [
            (20, "01_limit_properties_intro.jpg"),
            (70, "02_basic_arithmetic_rule.jpg"),
            (140, "03_denominator_nonzero_caution.jpg"),
            (210, "04_substitution_method_core.jpg"),
            (280, "05_example1_f_plus_g_converge.jpg"),
            (350, "06_example2_f_times_g_caution.jpg"),
            (420, "07_example3_fraction_numerator.jpg"),
            (490, "08_composite_limit_pitfall.jpg"),
            (560, "09_real_exam_three_second_solution.jpg"),
            (620, "10_truth_test_flowchart.jpg"),
        ]
    },
    {
        'num': 30,
        'video': 'lecture_video30.mp4',
        'out_dir': 'captures_v30',
        'timestamps': [
            (20, "01_cosine_rule_intro.jpg"),
            (70, "02_when_to_use_cosine_rule.jpg"),
            (140, "03_standard_formula_derivation.jpg"),
            (220, "04_sas_case_example.jpg"),
            (300, "05_sss_case_cos_formula.jpg"),
            (380, "06_triangle_obtuse_acute_test.jpg"),
            (450, "07_sine_vs_cosine_decision.jpg"),
            (520, "08_csat_applied_problem.jpg"),
            (580, "09_calculation_shortcut_tip.jpg"),
            (625, "10_cosine_rule_master_summary.jpg"),
        ]
    },
    {
        'num': 31,
        'video': 'lecture_video31.mp4',
        'out_dir': 'captures_v31',
        'timestamps': [
            (2, "01_exp_log_concept_intro.jpg"),
            (6, "02_base_cases_increase_decrease.jpg"),
            (11, "03_asymptotes_and_fixed_points.jpg"),
            (16, "04_inverse_symmetry_y_equals_x.jpg"),
            (21, "05_final_exam_checklist.jpg"),
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
    print("All captures for 29, 30, 31 completed!")

if __name__ == '__main__':
    main()
