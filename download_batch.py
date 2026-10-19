import subprocess
import sys

videos = [
    ("lecture_video21.mp4", "https://youtu.be/F_I1QJPWol8"),
    ("lecture_video22.mp4", "https://youtu.be/Cf7Wj9aFkJM"),
    ("lecture_video23.mp4", "https://youtu.be/z7SQOrKT7xY"),
]

for out_name, url in videos:
    print(f"Downloading {out_name} from {url}...")
    cmd = ["yt-dlp", "-f", "136/135/best[ext=mp4]/best", "-o", out_name, url]
    res = subprocess.run(cmd)
    if res.returncode == 0:
        print(f"Successfully downloaded {out_name}!")
    else:
        print(f"Failed downloading {out_name}, exit code: {res.returncode}")

print("All downloads complete!")
