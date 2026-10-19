import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

urls = [
    ('v21', 'https://youtu.be/F_I1QJPWol8'),
    ('v22', 'https://youtu.be/Cf7Wj9aFkJM'),
    ('v23', 'https://youtu.be/z7SQOrKT7xY')
]

for tag, url in urls:
    print(f"Fetching {tag}: {url}...")
    try:
        out = subprocess.check_output(['yt-dlp', '--dump-json', url], text=True, encoding='utf-8')
        d = json.loads(out)
        with open(f'video_info_{tag}.json', 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print(f"[{tag}] Title: {d.get('title')}")
        print(f"[{tag}] Channel: {d.get('channel')}")
        print(f"[{tag}] Duration: {d.get('duration')}s")
        print(f"[{tag}] Description: {d.get('description', '')[:120]}...\n")
    except Exception as e:
        print(f"Error fetching {tag}: {e}")
