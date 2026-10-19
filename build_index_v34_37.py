# -*- coding: utf-8 -*-
"""
Build script to register Lectures 34, 35, 36, 37 into index.html
Lecture 34: 중학도형 핵심 총정리 · 각의 이등분선과 닮음 (geom)
Lecture 35: 원의 성질 핵심 정리 · 원주각과 접현각 (geom)
Lecture 36: 다항함수 거리곱 공식과 고속 개형 추론 (math2)
Lecture 37: 삼차함수 비율관계와 극대·극소 높이차 공식 (math2)
"""

import re
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

def main():
    html_path = 'index.html'
    backup_path = 'index_backup_v33.html'
    shutil.copyfile(html_path, backup_path)
    print(f"Backed up index.html to {backup_path}")

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Read Manim scripts with escaping
    def load_manim(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            return f.read().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    m34 = load_manim('angle_bisector_geom_manim.py')
    m35 = load_manim('circle_inscribed_angle_manim.py')
    m36 = load_manim('distance_product_rule_manim.py')
    m37 = load_manim('cubic_ratio_height_formula_manim.py')

    # 2. Read Views
    with open('view_lecture34.html', 'r', encoding='utf-8') as f:
        v34 = f.read().replace('__MANIM_CODE_34__', m34)
    with open('view_lecture35.html', 'r', encoding='utf-8') as f:
        v35 = f.read().replace('__MANIM_CODE_35__', m35)
    with open('view_lecture36.html', 'r', encoding='utf-8') as f:
        v36 = f.read().replace('__MANIM_CODE_36__', m36)
    with open('view_lecture37.html', 'r', encoding='utf-8') as f:
        v37 = f.read().replace('__MANIM_CODE_37__', m37)

    # 3. Read JS files
    with open('js_lecture34.js', 'r', encoding='utf-8') as f:
        js34 = f.read()
    with open('js_lecture35.js', 'r', encoding='utf-8') as f:
        js35 = f.read()
    with open('js_lecture36.js', 'r', encoding='utf-8') as f:
        js36 = f.read()
    with open('js_lecture37.js', 'r', encoding='utf-8') as f:
        js37 = f.read()

    # 4. Update Navigation Tabs Badges
    # Total: 33 -> 37
    html = re.sub(
        r'(<button type="button" class="subj-tab(?: active)?" data-subject="all"[^>]*>[\s\S]*?<span class="tab-badge">)33(</span>)',
        r'\g<1>37\g<2>',
        html
    )
    # Math2: 9 -> 11 (Lectures 36 and 37 added)
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math2"[^>]*>[\s\S]*?<span class="tab-badge">)9(</span>)',
        r'\g<1>11\g<2>',
        html
    )
    # Geom: 5 -> 7 (Lectures 34 and 35 added)
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="geom"[^>]*>[\s\S]*?<span class="tab-badge">)5(</span>)',
        r'\g<1>7\g<2>',
        html
    )

    # Summary link text
    html = html.replace('사진 1~33 요약집', '사진 1~37 요약집')
    html = html.replace('사진 1~33 핵심 전용 페이지', '사진 1~37 핵심 전용 페이지')

    # 5. Insert Lecture Buttons
    # In group-math2: insert btnLec37 and btnLec36 before btnLec33
    if 'id="btnLec37"' not in html:
        old_btn33 = '<button type="button" class="lecture-btn" id="btnLec33"'
        new_btns_math2 = '''<button type="button" class="lecture-btn" id="btnLec37" onclick="setLecture(37)" data-subj="math2">
              <span class="lec-num">37</span>
              <span class="badge-pill-sm">⚡ 킬러체화</span>
              <span class="lec-title">삼차함수 비율관계와 극대·극소 높이차 공식</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec36" onclick="setLecture(36)" data-subj="math2">
              <span class="lec-num">36</span>
              <span class="badge-pill-sm">⚡ 꿀팁</span>
              <span class="lec-title">다항함수 거리곱 공식과 고속 개형 추론</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec33"'''
        html = html.replace(old_btn33, new_btns_math2, 1)
        print("Inserted btnLec37 and btnLec36 into group-math2.")

    # In group-geom: insert btnLec35 and btnLec34 before btnLec26
    if 'id="btnLec35"' not in html:
        old_btn26 = '<button type="button" class="lecture-btn" id="btnLec26"'
        new_btns_geom = '''<button type="button" class="lecture-btn" id="btnLec35" onclick="setLecture(35)" data-subj="geom">
              <span class="lec-num">35</span>
              <span class="badge-pill-sm">⚡ 필수도형</span>
              <span class="lec-title">원의 성질 핵심 정리 · 원주각과 접현각</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec34" onclick="setLecture(34)" data-subj="geom">
              <span class="lec-num">34</span>
              <span class="badge-pill-sm">⚡ 기본기</span>
              <span class="lec-title">중학도형 핵심 총정리 · 각의 이등분선과 닮음</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec26"'''
        html = html.replace(old_btn26, new_btns_geom, 1)
        print("Inserted btnLec35 and btnLec34 into group-geom.")

    # 6. Insert Views 37, 36, 35, 34 before lecture33View
    combined_views = f"{v37}\n{v36}\n{v35}\n{v34}"
    if '<div id="lecture37View">' not in html:
        target_lec33_view = '<div id="lecture33View"'
        html = html.replace(target_lec33_view, combined_views + '\n    ' + target_lec33_view, 1)
        print("Inserted lecture views 34, 35, 36, 37 into HTML.")

    # 7. Update JS Metadata
    old_meta_start = 'const LECTURE_META = {'
    new_meta_entries = '''const LECTURE_META = {
      37: { subj: 'math2',   subjName: '수학 II · 도함수의 활용', title: '제37강 · 삼차함수 비율관계와 극대·극소 높이차 공식' },
      36: { subj: 'math2',   subjName: '수학 II · 다항함수의 미분법', title: '제36강 · 다항함수 거리곱 공식과 고속 개형 추론' },
      35: { subj: 'geom',    subjName: '기하 & 미적분 · 원의 성질', title: '제35강 · 원의 성질 핵심 정리 · 원주각과 접현각' },
      34: { subj: 'geom',    subjName: '기하 & 미적분 · 중학도형 총정리', title: '제34강 · 중학도형 핵심 총정리 · 각의 이등분선과 닮음' },'''
    html = html.replace(old_meta_start, new_meta_entries, 1)

    # 8. Loop 33 -> 37
    html = re.sub(r'for \(let i = 1; i <= 33; i\+\+\)', r'for (let i = 1; i <= 37; i++)', html)

    # 9. setLecture num dispatch
    old_set_num33 = 'if (num === 33) setTimeout(renderL33, 50);'
    new_set_nums = '''if (num === 37) setTimeout(renderL37, 50);
      else if (num === 36) setTimeout(renderL36, 50);
      else if (num === 35) setTimeout(renderL35, 50);
      else if (num === 34) setTimeout(renderL34, 50);
      else if (num === 33) setTimeout(renderL33, 50);'''
    html = html.replace(old_set_num33, new_set_nums, 1)

    # 10. Insert JS Logic before window.addEventListener('load')
    target_window_load = "window.addEventListener('load', () => {"
    combined_js = f"{js34}\n\n{js35}\n\n{js36}\n\n{js37}"
    html = html.replace(target_window_load, combined_js + '\n    ' + target_window_load, 1)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully registered Lectures 34, 35, 36, 37 into index.html!")

if __name__ == '__main__':
    main()
