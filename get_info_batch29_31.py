# -*- coding: utf-8 -*-
import subprocess
import json
import sys

videos = [
    (29, "https://youtu.be/hXRGKmErfoY"),
    (30, "https://youtu.be/Z-uQkyyWUAQ"),
    (31, "https://youtube.com/shorts/fYaT7Lk1FjQ")
]

results = []

for num, url in videos:
    cmd = ['yt-dlp', '--dump-json', '--no-download', url]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if res.returncode == 0:
        data = json.loads(res.stdout)
        info = {
            'num': num,
            'id': data.get('id'),
            'title': data.get('title'),
            'channel': data.get('uploader'),
            'duration': data.get('duration'),
            'description': data.get('description'),
            'tags': data.get('tags')
        }
        results.append(info)
        with open(f'video_info_v{num}.json', 'w', encoding='utf-8') as f:
            json.dump(info, f, ensure_ascii=False, indent=2)
        print(f"[{num}] Title: {info['title']}, Channel: {info['channel']}, Duration: {info['duration']}s")
    else:
        print(f"[{num}] Error:", res.stderr[:300])

with open('video_info_batch29_31.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
