import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = pymupdf.open(r'C:\Users\Admin\Downloads\RPM Pro 중학 2-2 정답 (1).pdf')

with open('rpm_answers_56_59.txt', 'w', encoding='utf-8') as out:
    for p in range(37, 41): # 0-indexed: 37 = page 38, 38 = page 39, etc.
        out.write(f"=== ANSWER PAGE {p+1} ===\n")
        out.write(doc[p].get_text())
        out.write("\n\n")

print("Saved rpm_answers_56_59.txt successfully!")
