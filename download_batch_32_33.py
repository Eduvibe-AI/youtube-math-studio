import sys
import subprocess
import os

sys.stdout.reconfigure(encoding='utf-8')

videos = [
    (32, 'https://youtube.com/shorts/-YYxMu2u-4I'),
    (33, 'https://youtu.be/ihZz5SwynTM')
]

for num, url in videos:
    target = f'lecture_video{num}.mp4'
    print(f"Downloading Video {num} ({url}) to {target}...")
    cmd = [
        'yt-dlp',
        '--js-runtimes', 'node',
        '-f', 'bestvideo[height<=720]+bestaudio/best[height<=720]/best',
        '--merge-output-format', 'mp4',
        '--force-overwrites',
        '-o', target,
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if res.returncode == 0 and os.path.exists(target):
        print(f"[SUCCESS] Video {num} saved: {os.path.getsize(target):,} bytes")
    else:
        # Fallback if specific height filter failed
        print(f"Retrying Video {num} with default best format...")
        cmd_fallback = [
            'yt-dlp',
            '--js-runtimes', 'node',
            '--merge-output-format', 'mp4',
            '--force-overwrites',
            '-o', target,
            url
        ]
        res2 = subprocess.run(cmd_fallback, capture_output=True, text=True, encoding='utf-8')
        if res2.returncode == 0 and os.path.exists(target):
            print(f"[SUCCESS-FALLBACK] Video {num} saved: {os.path.getsize(target):,} bytes")
        else:
            print(f"[ERROR] Video {num} failed: {res2.stderr[:300]}")
