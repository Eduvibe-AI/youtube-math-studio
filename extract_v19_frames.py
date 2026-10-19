import os
import cv2

timestamps = [
    ("01_title_intro.jpg", 0.8),
    ("02_exp_log_inverse_setup.jpg", 1.5),
    ("03_line_y_equals_x_symmetry.jpg", 2.3),
    ("04_curve_intersection_concept.jpg", 3.2),
    ("05_base_value_comparison.jpg", 4.1),
    ("06_tangent_critical_point.jpg", 5.0),
    ("07_intersection_count_cases.jpg", 5.8),
    ("08_exam_key_takeaway.jpg", 6.7),
    ("09_final_summary_screen.jpg", 7.4),
]

out_dir = "captures_v19"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture("lecture_video19.mp4")
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
print("Done extracting frames for Lecture 19!")
