import sys
import subprocess
import json

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    (34, 'https://youtu.be/UU60Klvyl3g?si=Qtl2rMrxoKFjbZ7o'),
    (35, 'https://youtu.be/blXSMMZ9Sak?si=OgEM9a5u9A5rYj36'),
    (36, 'https://youtu.be/zbEzSVWluV8?si=NU5Ij_jbgxN4GfPP'),
    (37, 'https://youtu.be/W0NgWPHcDLM?si=hxKOhvTyLWdRwxDm')
]

results = {}
for idx, url in urls:
    print(f"Fetching metadata for Lecture {idx}: {url}...")
    cmd = ['yt-dlp', '--js-runtimes', 'node', '--dump-json', url]
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

with open('video_info_batch34_37.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
