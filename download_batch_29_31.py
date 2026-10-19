# -*- coding: utf-8 -*-
"""
Download videos 29, 30, 31
"""
import subprocess

videos = [
    (29, 'https://youtu.be/hXRGKmErfoY'),
    (30, 'https://youtu.be/Z-uQkyyWUAQ'),
    (31, 'https://youtube.com/shorts/fYaT7Lk1FjQ')
]

for num, url in videos:
    print(f"Starting download for video {num}...")
    cmd = [
        'yt-dlp',
        '-f', 'bestvideo[height<=720]+bestaudio/best[height<=720]/best',
        '--merge-output-format', 'mp4',
        '-o', f'lecture_video{num}.mp4',
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    print(f"Video {num} finished with code {res.returncode}")
    if res.returncode != 0:
        print(f"Error for {num}:", res.stderr[:300])

print("All downloads complete!")
