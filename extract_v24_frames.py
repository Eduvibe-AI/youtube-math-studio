# -*- coding: utf-8 -*-
"""
Extract keyframe captures from lecture_video24.mp4
"""

import os
import cv2

def main():
    video_path = 'lecture_video24.mp4'
    out_dir = 'captures_v24'
    os.makedirs(out_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening {video_path}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps if fps > 0 else 0
    print(f"FPS: {fps}, Total Frames: {total_frames}, Duration: {duration:.1f}s")

    # Key timestamps to capture (in seconds)
    timestamps = [
        (30, "01_intro_csat13_analysis.jpg"),
        (90, "02_problem_setup_diagram.jpg"),
        (160, "03_why_cosine_rule.jpg"),
        (230, "04_s1_two_choices_ac_vs_beta.jpg"),
        (310, "05_common_chord_information.jpg"),
        (380, "06_non_included_angle_quadratic.jpg"),
        (450, "07_factoring_to_find_length.jpg"),
        (510, "08_sine_rule_circumcircle_link.jpg"),
        (570, "09_final_ratio_answer.jpg"),
        (620, "10_top_tier_thinking_process.jpg"),
    ]

    for sec, fname in timestamps:
        frame_idx = int(sec * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if ret:
            out_path = os.path.join(out_dir, fname)
            cv2.imwrite(out_path, frame)
            print(f"Captured {sec}s -> {out_path}")
        else:
            print(f"Failed to capture frame at {sec}s")

    cap.release()
    print("Frame extraction complete!")

if __name__ == '__main__':
    main()
