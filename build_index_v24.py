# -*- coding: utf-8 -*-
"""
Build script to register Lecture 24 into index.html
Lecture 24: 사오수학 - 도형 문제를 풀 때 최상위권들이 '반드시' 하는 생각 1가지 (1등급의 시선 ep6)
"""

import re

def main():
    html_path = 'index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read manim code
    with open('sine_cosine_rule_necessity_manim.py', 'r', encoding='utf-8') as f:
        manim_24 = f.read().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # Read view
    with open('view_lecture24.html', 'r', encoding='utf-8') as f:
        v24 = f.read().replace('__MANIM_CODE_24__', manim_24)

    # Read JS
    with open('js_lecture24.js', 'r', encoding='utf-8') as f:
        js_code = f.read()

    # 1. Update Navigation Tabs Badges
    # Total badge: 23 -> 24
    html = re.sub(
        r'(<button type="button" class="subj-tab(?: active)?" data-subject="all"[^>]*>[\s\S]*?<span class="tab-badge">)23(</span>)',
        r'\g<1>24\g<2>',
        html
    )
    # Math1 badge: 6 -> 7
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math1"[^>]*>[\s\S]*?<span class="tab-badge">)6(</span>)',
        r'\g<1>7\g<2>',
        html
    )

    # Special summary link text: 1~23 -> 1~24
    html = html.replace('사진 1~23 요약집', '사진 1~24 요약집')
    html = html.replace('사진 1~23 핵심 전용 페이지', '사진 1~24 핵심 전용 페이지')

    # De-activate btnLec21
    html = html.replace('id="btnLec21" onclick="setLecture(21)" class="lecture-btn active"', 'id="btnLec21" onclick="setLecture(21)" class="lecture-btn"')
    html = html.replace('class="lecture-btn active" id="btnLec21"', 'class="lecture-btn" id="btnLec21"')

    # 2. Insert btnLec24 into group-math1
    if 'id="btnLec24"' not in html:
        old_btn21 = '<button type="button" class="lecture-btn" id="btnLec21" onclick="setLecture(21)" data-subj="math1">'
        new_btn24 = '''<button type="button" class="lecture-btn active" id="btnLec24" onclick="setLecture(24)" data-subj="math1">
              <span class="lec-num">24</span>
              <span class="badge-pill-sm">⚡ 킬러</span>
              <span class="lec-title">도형 문제 최상위권의 시선 (삼각함수 활용)</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec21" onclick="setLecture(21)" data-subj="math1">'''
        html = html.replace(old_btn21, new_btn24, 1)
        print("Inserted btnLec24 into group-math1.")

    # Update Status banner default
    html = re.sub(
        r'<span class="status-subj" id="statusSubjText">[^<]+</span>\s*<span class="status-sep">/</span>\s*<span class="status-title" id="statusTitleText">[^<]+</span>',
        r'<span class="status-subj" id="statusSubjText">수학 I · 삼각함수의 활용</span>\n        <span class="status-sep">/</span>\n        <span class="status-title" id="statusTitleText">제24강 · 도형 문제를 풀 때 최상위권들이 반드시 하는 생각 (사인·코사인법칙의 필연성)</span>',
        html
    )

    # Hide lecture21View by default
    html = html.replace('<div id="lecture21View">', '<div id="lecture21View" style="display: none;">')

    # 3. Insert lecture24View before lecture21View
    if '<div id="lecture24View">' not in html:
        target_lec21_view = '<div id="lecture21View"'
        html = html.replace(target_lec21_view, v24 + '\n' + target_lec21_view, 1)
        print("Inserted lecture24View into HTML.")

    # 4. Update JS Metadata & Handlers
    old_meta_start = 'const LECTURE_META = {'
    new_meta_entries = '''const LECTURE_META = {
      24: { subj: 'math1',   subjName: '수학 I · 삼각함수의 활용', title: '제24강 · 도형 문제를 풀 때 최상위권들이 반드시 하는 생각 (사인·코사인법칙의 필연성)' },'''
    html = html.replace(old_meta_start, new_meta_entries, 1)

    # Loop 23 -> 24 in setLecture and selectSubject
    html = re.sub(r'for \(let i = 1; i <= 23; i\+\+\)', r'for (let i = 1; i <= 24; i++)', html)

    # setLecture num handling
    old_set_num23 = 'if (num === 23) setTimeout(renderL23, 50);'
    new_set_nums = '''if (num === 24) setTimeout(renderL24, 50);
      else if (num === 23) setTimeout(renderL23, 50);'''
    html = html.replace(old_set_num23, new_set_nums, 1)

    # 5. Insert JS Logic before window.addEventListener('load')
    target_window_load = "window.addEventListener('load', () => {"
    html = html.replace(target_window_load, js_code + '\n    ' + target_window_load, 1)

    # In window.addEventListener('load'), setLecture(24) and renderL24()
    html = html.replace("setLecture(21);\n      renderL21();", "setLecture(24);\n      renderL24();")
    html = html.replace("setLecture(21);", "setLecture(24);")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done! Successfully built index.html with Lecture 24.")

if __name__ == '__main__':
    main()
