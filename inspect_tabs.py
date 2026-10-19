import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<button[^>]*class="[^"]*subj-tab[^"]*"[^>]*>[\s\S]*?</button>', text)
print(f"Found {len(matches)} subj-tab buttons:")
for m in matches:
    print(m)
    print("-" * 40)

# Check all buttons
btns = re.findall(r'<button[^>]*id="btnLec\d+"[^>]*>', text)
print(f"Found {len(btns)} lecture buttons (btnLec):")
for b in btns[:5]:
    print(b)
print("...")
for b in btns[-5:]:
    print(b)

# Check summary links
summary_matches = re.findall(r'사진 [^<]+', text)
print("Summary mentions:", set(summary_matches))
