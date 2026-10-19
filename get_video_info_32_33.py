import sys
import subprocess
import json

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    'https://youtube.com/shorts/-YYxMu2u-4I?si=omSZOH0unI_YxTNg',
    'https://youtu.be/ihZz5SwynTM?si=8m8sMA3_2x8sYH__'
]

results = {}
for idx, url in enumerate(urls, start=32):
    print(f"Fetching metadata for Lecture {idx}: {url}...")
    cmd = ['yt-dlp', '--dump-json', url]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if res.returncode == 0:
        data = json.loads(res.stdout)
        info = {
            'id': data.get('id'),
            'title': data.get('title'),
            'channel': data.get('channel'),
            'duration': data.get('duration'),
            'description': data.get('description', '')[:500],
            'url': url
        }
        with open(f'video_info_v{idx}.json', 'w', encoding='utf-8') as f:
            json.dump(info, f, ensure_ascii=False, indent=2)
        results[idx] = info
        print(f"[SUCCESS] Lecture {idx}: {info['title']} | Channel: {info['channel']} | Duration: {info['duration']}s")
    else:
        print(f"[ERROR] Failed to fetch {url}: {res.stderr[:200]}")

with open('video_info_batch32_33.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
