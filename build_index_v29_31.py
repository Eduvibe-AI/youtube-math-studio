# -*- coding: utf-8 -*-
"""
Build script to register Lectures 29, 30, 31 into index.html
Lecture 29: 함수의 극한의 성질 진위판단 (math2)
Lecture 30: 삼각함수 활용 · 코사인법칙 (math1)
Lecture 31: 지수함수와 로그함수 수능 요약 (math1)
"""

import re
import shutil

def main():
    html_path = 'index.html'
    backup_path = 'index_backup_v28.html'
    shutil.copyfile(html_path, backup_path)
    print(f"Backed up index.html to {backup_path}")

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Read Manim scripts with escaping
    def load_manim(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            return f.read().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    m29 = load_manim('limit_properties_truth_test_manim.py')
    m30 = load_manim('cosine_rule_geometry_manim.py')
    m31 = load_manim('exp_log_quick_summary_manim.py')

    # 2. Read Views
    with open('view_lecture29.html', 'r', encoding='utf-8') as f:
        v29 = f.read().replace('__MANIM_CODE_29__', m29)
    with open('view_lecture30.html', 'r', encoding='utf-8') as f:
        v30 = f.read().replace('__MANIM_CODE_30__', m30)
    with open('view_lecture31.html', 'r', encoding='utf-8') as f:
        v31 = f.read().replace('__MANIM_CODE_31__', m31)

    # 3. Read JS files
    with open('js_lecture29.js', 'r', encoding='utf-8') as f:
        js29 = f.read()
    with open('js_lecture30.js', 'r', encoding='utf-8') as f:
        js30 = f.read()
    with open('js_lecture31.js', 'r', encoding='utf-8') as f:
        js31 = f.read()

    # 4. Update Navigation Tabs Badges
    # Total: 28 -> 31
    html = re.sub(
        r'(<button type="button" class="subj-tab(?: active)?" data-subject="all"[^>]*>[\s\S]*?<span class="tab-badge">)28(</span>)',
        r'\g<1>31\g<2>',
        html
    )
    # Math1: 8 -> 10 (Lectures 30 and 31 added)
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math1"[^>]*>[\s\S]*?<span class="tab-badge">)8(</span>)',
        r'\g<1>10\g<2>',
        html
    )
    # Math2: 7 -> 8 (Lecture 29 added)
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math2"[^>]*>[\s\S]*?<span class="tab-badge">)7(</span>)',
        r'\g<1>8\g<2>',
        html
    )

    # Summary link text
    html = html.replace('사진 1~28 요약집', '사진 1~31 요약집')
    html = html.replace('사진 1~28 핵심 전용 페이지', '사진 1~31 핵심 전용 페이지')

    # 5. Insert Lecture Buttons
    # Insert btnLec29 into group-math2 before btnLec27
    if 'id="btnLec29"' not in html:
        old_btn27 = '<button type="button" class="lecture-btn" id="btnLec27" onclick="setLecture(27)" data-subj="math2">'
        new_btn29 = '''<button type="button" class="lecture-btn" id="btnLec29" onclick="setLecture(29)" data-subj="math2">
              <span class="lec-num">29</span>
              <span class="badge-pill-sm">⚡ 킬러</span>
              <span class="lec-title">함수의 극한 성질 진위판단 (치환법)</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec27" onclick="setLecture(27)" data-subj="math2">'''
        html = html.replace(old_btn27, new_btn29, 1)
        print("Inserted btnLec29 into group-math2.")

    # Insert btnLec31 and btnLec30 into group-math1 before btnLec25
    if 'id="btnLec31"' not in html:
        old_btn25 = '<button type="button" class="lecture-btn'
        # find btnLec25 specifically
        pos25 = html.find('id="btnLec25"')
        tag_start = html.rfind('<button', 0, pos25)
        tag_end = html.find('>', pos25) + 1
        btn25_full_start = html[tag_start:tag_end]

        new_btns_math1 = f'''<button type="button" class="lecture-btn" id="btnLec31" onclick="setLecture(31)" data-subj="math1">
              <span class="lec-num">31</span>
              <span class="badge-pill-sm">⚡ 요약</span>
              <span class="lec-title">지수함수와 로그함수 수능 요약</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec30" onclick="setLecture(30)" data-subj="math1">
              <span class="lec-num">30</span>
              <span class="badge-pill-sm">⚡ 필수</span>
              <span class="lec-title">삼각함수 활용 · 코사인법칙</span>
            </button>
            {btn25_full_start}'''
        html = html[:tag_start] + new_btns_math1 + html[tag_end:]
        print("Inserted btnLec31 and btnLec30 into group-math1.")

    # 6. Insert Views 31, 30, 29 before lecture28View
    combined_views = f"{v31}\n{v30}\n{v29}"
    if '<div id="lecture29View">' not in html:
        target_lec28_view = '<div id="lecture28View"'
        html = html.replace(target_lec28_view, combined_views + '\n    ' + target_lec28_view, 1)
        print("Inserted lecture views 29, 30, 31 into HTML.")

    # 7. Update JS Metadata
    old_meta_start = 'const LECTURE_META = {'
    new_meta_entries = '''const LECTURE_META = {
      31: { subj: 'math1',   subjName: '수학 I · 지수와 로그', title: '제31강 · 지수함수와 로그함수 (수능 직전 초스피드 개념 총정리)' },
      30: { subj: 'math1',   subjName: '수학 I · 삼각함수의 활용', title: '제30강 · 삼각함수 활용 · 코사인법칙의 원리와 기하학적 직관' },
      29: { subj: 'math2',   subjName: '수학 II · 함수의 극한과 연속', title: '제29강 · 함수의 극한의 성질 진위판단 (반례 없는 치환법)' },'''
    html = html.replace(old_meta_start, new_meta_entries, 1)

    # 8. Loop 28 -> 31
    html = re.sub(r'for \(let i = 1; i <= 28; i\+\+\)', r'for (let i = 1; i <= 31; i++)', html)

    # 9. setLecture num dispatch
    old_set_num28 = 'if (num === 28) setTimeout(renderL28, 50);'
    new_set_nums = '''if (num === 31) setTimeout(renderL31, 50);
      else if (num === 30) setTimeout(renderL30, 50);
      else if (num === 29) setTimeout(renderL29, 50);
      else if (num === 28) setTimeout(renderL28, 50);'''
    html = html.replace(old_set_num28, new_set_nums, 1)

    # 10. Insert JS Logic before window.addEventListener('load')
    target_window_load = "window.addEventListener('load', () => {"
    combined_js = f"{js29}\n\n{js30}\n\n{js31}"
    html = html.replace(target_window_load, combined_js + '\n    ' + target_window_load, 1)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully registered Lectures 29, 30, 31 into index.html!")

if __name__ == '__main__':
    main()
