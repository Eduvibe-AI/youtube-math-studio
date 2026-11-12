import json
import re

cat_path = '509-401-math--helper/public/workbook_data/catalog.js'

with open(cat_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'window\.WB_CATALOG\s*=\s*(\[[\s\S]*\]);?', text)
data = json.loads(m.group(1))

updated = 0
for b in data:
    bid = b.get('id', '')
    if bid == 'rpm_hwaktong':
        print(f"Updating rpm_hwaktong: imgP {b.get('imgP')} -> 596, imgS {b.get('imgS')} -> 596")
        b['imgP'] = 596
        b['imgS'] = 596
        updated += 1
    elif bid == 'rpm_2022_mid2_2':
        print(f"Updating rpm_2022_mid2_2: imgP {b.get('imgP')} -> 957, imgS {b.get('imgS')} -> 957")
        b['imgP'] = 957
        b['imgS'] = 957
        updated += 1
    elif bid == 'ssen_2022_mid1_1':
        print(f"Checking ssen_2022_mid1_1: imgP {b.get('imgP')}, imgS {b.get('imgS')}")
        b['imgP'] = 1199
        b['imgS'] = 1199
        updated += 1

new_content = 'window.WB_CATALOG=' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n'
with open(cat_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated {updated} entries in {cat_path}")

