# -*- coding: utf-8 -*-
"""
Download videos 25, 26, 27, 28
"""
import subprocess

videos = [
    (25, 'https://youtu.be/OP2qIiPfKJo'),
    (26, 'https://youtu.be/YHl5jqL-yZA'),
    (27, 'https://youtu.be/Jw8F2akj_T0'),
    (28, 'https://youtu.be/hRpteAyG2Ts')
]

for num, url in videos:
    print(f"Starting download for video {num}...")
    cmd = [
        'yt-dlp',
        '-f', 'bestvideo[height<=720]+bestaudio/best[height<=720]/best',
        '--merge-output-format', 'mp4',
        '--write-sub', '--write-auto-sub', '--sub-lang', 'ko',
        '-o', f'lecture_video{num}.mp4',
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    print(f"Video {num} finished with code {res.returncode}")
    if res.returncode != 0:
        print(f"Error for {num}:", res.stderr[:300])

print("All downloads complete!")
