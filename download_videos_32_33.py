import sys
import subprocess
import os

sys.stdout.reconfigure(encoding='utf-8')

tasks = [
    (32, 'https://youtube.com/shorts/-YYxMu2u-4I?si=omSZOH0unI_YxTNg'),
    (33, 'https://youtu.be/ihZz5SwynTM?si=8m8sMA3_2x8sYH__')
]

for idx, url in tasks:
    out_file = f"lecture_video{idx}.mp4"
    print(f"Downloading video {idx} to {out_file}...")
    # Best format up to 720p/1080p compatible with browser mp4
    cmd = [
        'yt-dlp',
        '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        '-o', out_file,
        '--force-overwrites',
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if res.returncode == 0 and os.path.exists(out_file):
        print(f"[SUCCESS] Downloaded {out_file}: {os.path.getsize(out_file):,} bytes")
    else:
        print(f"[ERROR] Failed download for {idx}: {res.stderr[:200]}")
