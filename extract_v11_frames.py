import os, cv2

timestamps = [
    ("01_intro_problem_statement.jpg", 3.0),
    ("02_y_equals_x_symmetry.jpg", 6.5),
    ("03_starting_point_3_k.jpg", 10.0),
    ("04_k_equals_3_preview.jpg", 14.0),
    ("05_inverse_curve_sketch.jpg", 20.0),
    ("06_replace_inverse_with_y_x.jpg", 28.0),
    ("07_single_intersection_fail.jpg", 35.0),
    ("08_slide_down_to_y_x.jpg", 42.0),
    ("09_two_intersections_valid.jpg", 48.0),
    ("10_maximum_k_equals_3.jpg", 55.0),
]

out_dir = "captures_v11"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture("lecture_video11.mp4")
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
print("Done extracting frames for Lecture 11!")
