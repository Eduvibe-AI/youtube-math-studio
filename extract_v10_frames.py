import os, cv2

timestamps = [
    ("01_intro_problem_screen.jpg", 3.0),
    ("02_target_numerator_rule.jpg", 8.0),
    ("03_denominator_zero_substitution.jpg", 13.0),
    ("04_birth_function_k_minus_3.jpg", 18.0),
    ("05_search_strategy_k_minus_3.jpg", 25.0),
    ("06_option1_test_fail.jpg", 31.0),
    ("07_option2_test_fail.jpg", 36.0),
    ("08_option3_test_match.jpg", 42.0),
    ("09_option4_option5_test.jpg", 48.0),
    ("10_final_answer_3_seconds.jpg", 54.0),
]

out_dir = "captures_v10"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture("lecture_video10.mp4")
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
