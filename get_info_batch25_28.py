# -*- coding: utf-8 -*-
import subprocess, json

urls = [
    (25, 'https://youtu.be/OP2qIiPfKJo'),
    (26, 'https://youtu.be/YHl5jqL-yZA'),
    (27, 'https://youtu.be/Jw8F2akj_T0'),
    (28, 'https://youtu.be/hRpteAyG2Ts')
]

for num, url in urls:
    cmd = ['yt-dlp', '--dump-json', '--no-playlist', url]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if res.returncode == 0:
        info = json.loads(res.stdout)
        data = {
            'num': num,
            'id': info.get('id'),
            'title': info.get('title'),
            'uploader': info.get('uploader'),
            'channel': info.get('channel'),
            'duration': info.get('duration'),
            'description': info.get('description', '')[:400],
            'tags': info.get('tags', [])
        }
        with open(f'video_info_v{num}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"V{num}: {data['title']} | {data['channel']} | {data['duration']}s")
    else:
        print(f"V{num} Error:", res.stderr[:200])
