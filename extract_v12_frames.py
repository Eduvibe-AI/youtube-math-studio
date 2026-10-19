import os, cv2

timestamps = [
    ("01_hyperbola_problem_statement.jpg", 3.0),
    ("02_sector_area_s_definition.jpg", 6.5),
    ("03_integral_area_t_definition.jpg", 11.0),
    ("04_claim_s_equals_t.jpg", 15.0),
    ("05_four_region_decomposition.jpg", 18.0),
    ("06_red_triangle_half.jpg", 21.0),
    ("07_blue_triangle_half.jpg", 24.5),
    ("08_purple_overlap_cancellation.jpg", 28.0),
    ("09_add_yellow_curved_region.jpg", 32.0),
    ("10_final_proof_s_equals_t.jpg", 36.5),
]

out_dir = "captures_v12"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture("lecture_video12.mp4")
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
print("Done extracting frames for Lecture 12!")
