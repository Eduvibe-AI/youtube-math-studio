import sys
import subprocess
import os

sys.stdout.reconfigure(encoding='utf-8')

videos = [
    (34, 'https://youtu.be/UU60Klvyl3g'),
    (35, 'https://youtu.be/blXSMMZ9Sak'),
    (36, 'https://youtu.be/zbEzSVWluV8'),
    (37, 'https://youtu.be/W0NgWPHcDLM')
]

for num, url in videos:
    target = f'lecture_video{num}.mp4'
    print(f"Downloading Video {num} ({url}) to {target}...")
    # Best single mp4 or direct video stream for web playback
    cmd = [
        'yt-dlp',
        '--js-runtimes', 'node',
        '-f', 'best[ext=mp4]/bestvideo[ext=mp4]+bestaudio/best',
        '--force-overwrites',
        '-o', target,
        url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if os.path.exists(target) and os.path.getsize(target) > 50000:
        print(f"[SUCCESS] Video {num} saved: {os.path.getsize(target):,} bytes")
    else:
        # Check if a partial or stream file was created
        candidates = [f for f in os.listdir('.') if f.startswith(f'lecture_video{num}.') and os.path.getsize(f) > 50000]
        if candidates:
            # Pick largest video candidate
            best_cand = max(candidates, key=lambda f: os.path.getsize(f))
            import shutil
            shutil.copyfile(best_cand, target)
            print(f"[SUCCESS-FALLBACK] Copied {best_cand} to {target}: {os.path.getsize(target):,} bytes")
        else:
            print(f"[ERROR] Video {num} failed: {res.stderr[:300]}")
