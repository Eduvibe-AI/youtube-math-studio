import json
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

cat_path = '509-401-math--helper/public/workbook_data/catalog.js'
base_data = '509-401-math--helper/public/workbook_data'

with open(cat_path, 'r', encoding='utf-8') as f:
    text = f.read()

json_str = text.split('=', 1)[1].strip().rstrip(';')
catalog = json.loads(json_str)

print(f"=== catalog.js 전체 {len(catalog)}종 교재 정답 및 풀이 메타데이터 전수 동기화 ===")

updated_books = 0

for b in catalog:
    bid = b.get('id', '')
    sol_file = os.path.join(base_data, f"sol_{bid}.js")
    
    if not os.path.exists(sol_file):
        continue
        
    try:
        with open(sol_file, 'r', encoding='utf-8') as sf:
            s_content = sf.read()
            
        # extract json
        # match window.WB_SOL[...] = window.SOL_DATA[...] = { ... } or window.WB_SOL[...] = { ... }
        m = re.search(rf'window\.WB_SOL\[[\'\"]{bid}[\'\"]\]\s*=\s*(?:window\.SOL_DATA\[[\'\"]{bid}[\'\"]\]\s*=\s*)?', s_content)
        if not m:
            continue
            
        json_part = s_content[m.end():].strip().rstrip(';')
        sol_data = json.loads(json_part)
        
        # count valid answers and solved
        valid_ans_keys = set()
        for k, entry in sol_data.items():
            ans = entry[0]
            if ans and str(ans).strip() and str(ans).strip() != '?':
                valid_ans_keys.add(int(k))
                
        actual_ans_count = len(valid_ans_keys)
        actual_solved_count = len(sol_data)
        
        # check if update needed
        old_ans = b.get('ans', 0)
        old_solved = b.get('solved', 0)
        
        if old_ans != actual_ans_count or old_solved != actual_solved_count:
            print(f"🔄 [{bid}] {b.get('name', '')}: ans {old_ans} -> {actual_ans_count}, solved {old_solved} -> {actual_solved_count}")
            b['ans'] = actual_ans_count
            b['solved'] = actual_solved_count
            
            # update units
            units = b.get('units', [])
            for u in units:
                u_start = u.get('start', 1)
                u_end = u.get('end', u_start + u.get('count', 0) - 1)
                u_ans = sum(1 for q in range(u_start, u_end + 1) if q in valid_ans_keys)
                u['ans'] = u_ans
                u['solved'] = u.get('count', 0)
                
            updated_books += 1
            
    except Exception as e:
        # print(f"Error parsing {bid}: {e}")
        pass

# 백업 후 저장
bak_path = cat_path + '.bak'
with open(bak_path, 'w', encoding='utf-8') as f:
    f.write(text)

new_cat_content = 'window.WB_CATALOG = ' + json.dumps(catalog, ensure_ascii=False, indent=2) + ';\n'
with open(cat_path, 'w', encoding='utf-8') as f:
    f.write(new_cat_content)

print(f"\n🎉 catalog.js 메타데이터 동기화 완료! 총 {updated_books}종 교재 갱신됨.")

