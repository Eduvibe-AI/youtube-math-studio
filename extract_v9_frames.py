import os, sys
import cv2

timestamps = [
    ("01_parabola_x_axis_problem.jpg", 17.0),
    ("02_integral_negative_area.jpg", 55.0),
    ("03_concept_general_split.jpg", 100.0),
    ("04_formula_summary_split.jpg", 140.0),
    ("05_example2_cubic_both_sides.jpg", 205.0),
    ("06_example2_solution.jpg", 255.0),
    ("07_two_curves_intersection.jpg", 305.0),
    ("08_diff_function_concept.jpg", 360.0),
    ("09_diff_function_area_invariance.jpg", 410.0),
    ("10_example3_diff_factorization.jpg", 505.0),
    ("11_example3_area_calculation.jpg", 550.0),
    ("12_example4_parabola_line.jpg", 610.0),
]

out_dir = "captures_v9"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture("lecture_video9.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps

print(f"Video FPS: {fps}, Total Frames: {total_frames}, Duration: {duration:.2f}s")

for name, sec in timestamps:
    frame_idx = int(sec * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ret, frame = cap.read()
    if ret:
        out_path = os.path.join(out_dir, name)
        cv2.imwrite(out_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
        print(f"Saved {name} at {sec}s (frame {frame_idx})")
    else:
        print(f"FAILED to read frame at {sec}s")

cap.release()
print("Done extracting frames!")
