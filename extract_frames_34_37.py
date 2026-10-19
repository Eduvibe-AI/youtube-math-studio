import cv2
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_keyframes(video_path, output_dir, count=8, prefix="frame"):
    if not os.path.exists(video_path):
        print(f"[SKIP] {video_path} does not exist yet.")
        return False
    
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"[ERROR] Could not open {video_path}")
        return False
        
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Extracting {count} frames from {video_path}: total frames={total}, fps={fps:.1f}")
    
    indices = [int(total * (0.08 + 0.84 * i / (count - 1))) for i in range(count)]
    saved = 0
    for i, idx in enumerate(indices):
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = cap.read()
        if ret:
            out_file = os.path.join(output_dir, f"{i+1:02d}_{prefix}_{idx}.jpg")
            cv2.imwrite(out_file, frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
            saved += 1
    cap.release()
    print(f"[SUCCESS] Saved {saved} frames to {output_dir}")
    return True

if __name__ == '__main__':
    extract_keyframes('lecture_video34.mp4', 'captures_v34', count=8, prefix="mid_geom")
    extract_keyframes('lecture_video35.mp4', 'captures_v35', count=8, prefix="circle_geom")
    extract_keyframes('lecture_video36.mp4', 'captures_v36', count=8, prefix="topic36")
    extract_keyframes('lecture_video37.mp4', 'captures_v37', count=8, prefix="topic37")
