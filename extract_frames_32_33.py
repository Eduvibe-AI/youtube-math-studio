import cv2
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_keyframes(video_path, output_dir, target_count=10, prefix="frame"):
    if not os.path.exists(video_path):
        print(f"[ERROR] Video file not found: {video_path}")
        return False
    
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"[ERROR] Failed to open video: {video_path}")
        return False
        
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = total_frames / fps if fps > 0 else 0
    print(f"Processing {video_path}: {total_frames} frames, {fps:.1f} fps, {duration:.1f}s")
    
    # Select evenly spaced timestamps, avoiding the first 2% and last 2%
    start_f = int(total_frames * 0.05)
    end_f = int(total_frames * 0.95)
    step = max(1, (end_f - start_f) // (target_count - 1)) if target_count > 1 else 1
    
    saved = 0
    for i in range(target_count):
        f_idx = min(end_f, start_f + i * step)
        cap.set(cv2.CAP_PROP_POS_FRAMES, f_idx)
        ret, frame = cap.read()
        if ret:
            out_name = f"{i+1:02d}_{prefix}_{f_idx}.jpg"
            out_path = os.path.join(output_dir, out_name)
            cv2.imwrite(out_path, frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
            saved += 1
            
    cap.release()
    print(f"[SUCCESS] Extracted {saved} frames to {output_dir}")
    return True

if __name__ == '__main__':
    # 32: 지수로그 핫한 문제 풀이 (shorts, ~42s)
    extract_keyframes('lecture_video32.mp4', 'captures_v32', target_count=6, prefix="exp_log_trick")
    # 33: 적분을 넓이로 본다? 당신은 하수입니다 (수능 정적분의 본질, ~403s)
    extract_keyframes('lecture_video33.mp4', 'captures_v33', target_count=10, prefix="integral_concept")
