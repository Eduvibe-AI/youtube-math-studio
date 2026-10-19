import os
import cv2

timestamps = [
    ("01_transcendental_equation_limit.jpg", 10.0),
    ("02_translation_formula_setup.jpg", 45.0),
    ("03_slope_vector_alignment.jpg", 78.0),
    ("04_coefficient_log_translation.jpg", 115.0),
    ("05_symmetry_axis_y_equals_x.jpg", 150.0),
    ("06_slope_minus_one_symmetry.jpg", 172.0),
    ("07_exam_22_sep_21_intro.jpg", 195.0),
    ("08_isosceles_right_triangle_ratio.jpg", 228.0),
    ("09_coordinate_transformation_solve.jpg", 244.0),
    ("10_three_principles_summary.jpg", 258.0),
]

out_dir = "captures_v20"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture("lecture_video20.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps
print(f"Video FPS: {fps:.2f}, Total Frames: {total_frames}, Duration: {duration:.2f}s")

for name, sec in timestamps:
    frame_idx = min(int(sec * fps), total_frames - 1)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ret, frame = cap.read()
    if ret:
        out_path = os.path.join(out_dir, name)
        cv2.imwrite(out_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
        print(f"Saved {name} at {sec}s (frame {frame_idx})")
    else:
        print(f"FAILED to read frame at {sec}s")

cap.release()
print("Done extracting refined frames for Lecture 20!")
