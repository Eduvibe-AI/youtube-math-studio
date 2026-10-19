import os
import cv2

timestamps = [
    ("01_local_maximum_intro.jpg", 1.5),
    ("02_definition_higher_than_neighbors.jpg", 3.5),
    ("03_question_which_is_local_max.jpg", 6.0),
    ("04_four_candidate_graphs.jpg", 11.0),
    ("05_all_four_are_local_max.jpg", 14.5),
    ("06_open_interval_definition.jpg", 16.5),
    ("07_purple_dots_highest_points.jpg", 19.5),
    ("08_do_not_exclude_non_differentiable.jpg", 21.5),
    ("09_peak_and_puncture_rhymes.jpg", 27.5),
    ("10_final_definition_higher_than_neighbors.jpg", 31.5),
]

out_dir = "captures_v14"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture("lecture_video14.mp4")
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
print("Done extracting frames for Lecture 14!")
