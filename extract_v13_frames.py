import os
import cv2

timestamps = [
    ("01_intro_y_vs_fx_question.jpg", 2.5),
    ("02_original_curve_setup.jpg", 7.5),
    ("03_abs_y_equals_fx_definition.jpg", 11.0),
    ("04_abs_y_symmetric_graph.jpg", 17.5),
    ("05_y_equals_abs_fx_definition.jpg", 22.0),
    ("06_y_equals_abs_fx_fold_up.jpg", 26.5),
    ("07_common_doubt_same_equation.jpg", 29.8),
    ("08_territory_vs_resident_concept.jpg", 34.5),
    ("09_earth_equator_analogy.jpg", 41.5),
    ("10_final_epiphany_y_is_territory.jpg", 47.5),
]

out_dir = "captures_v13"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture("lecture_video13.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps
print(f"Video FPS: {fps:.2f}, Total Frames: {total_frames}, Duration: {duration:.2f}s")

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
print("Done extracting frames for Lecture 13!")
