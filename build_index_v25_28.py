# -*- coding: utf-8 -*-
"""
Build script to register Lectures 25, 26, 27, 28 into index.html
Default active lecture: Lecture 28 (교과서 14개 그래프 총정리)
"""

import re
import shutil

def main():
    html_path = 'index.html'
    backup_path = 'index_backup_v24.html'

    # Always restore from clean v24 backup to avoid duplicated inserts
    with open(backup_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Read Manim scripts with escaping
    def load_manim(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            return f.read().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    m25 = load_manim('recurrence_relation_big4_manim.py')
    m26 = load_manim('taylor_series_approximation_manim.py')
    m27 = load_manim('polynomial_roots_symmetry_manim.py')
    m28 = load_manim('textbook_14_graphs_master_manim.py')

    # 2. Read Views
    with open('view_lecture25.html', 'r', encoding='utf-8') as f:
        v25 = f.read().replace('__MANIM_CODE_25__', m25)
    with open('view_lecture26.html', 'r', encoding='utf-8') as f:
        v26 = f.read().replace('__MANIM_CODE_26__', m26)
    with open('view_lecture27.html', 'r', encoding='utf-8') as f:
        v27 = f.read().replace('__MANIM_CODE_27__', m27)
    with open('view_lecture28.html', 'r', encoding='utf-8') as f:
        v28 = f.read().replace('__MANIM_CODE_28__', m28)

    # 3. Read JS files
    with open('js_lecture25.js', 'r', encoding='utf-8') as f:
        js25 = f.read()
    with open('js_lecture26.js', 'r', encoding='utf-8') as f:
        js26 = f.read()
    with open('js_lecture27.js', 'r', encoding='utf-8') as f:
        js27 = f.read()
    with open('js_lecture28.js', 'r', encoding='utf-8') as f:
        js28 = f.read()

    # 4. Update Navigation Tabs Badges
    # Total: 24 -> 28
    html = re.sub(
        r'(<button type="button" class="subj-tab(?: active)?" data-subject="all"[^>]*>[\s\S]*?<span class="tab-badge">)24(</span>)',
        r'\g<1>28\g<2>',
        html
    )
    # Math-Ha: 7 -> 8
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math-ha"[^>]*>[\s\S]*?<span class="tab-badge">)7(</span>)',
        r'\g<1>8\g<2>',
        html
    )
    # Math1: 7 -> 8
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math1"[^>]*>[\s\S]*?<span class="tab-badge">)7(</span>)',
        r'\g<1>8\g<2>',
        html
    )
    # Math2: 6 -> 7
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math2"[^>]*>[\s\S]*?<span class="tab-badge">)6(</span>)',
        r'\g<1>7\g<2>',
        html
    )
    # Geom: 4 -> 5
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="geom"[^>]*>[\s\S]*?<span class="tab-badge">)4(</span>)',
        r'\g<1>5\g<2>',
        html
    )

    # Summary link text
    html = html.replace('사진 1~24 요약집', '사진 1~28 요약집')
    html = html.replace('사진 1~24 핵심 전용 페이지', '사진 1~28 핵심 전용 페이지')

    # 5. Insert Lecture Buttons
    # De-activate btnLec24
    html = html.replace('id="btnLec24" onclick="setLecture(24)" class="lecture-btn active"', 'id="btnLec24" onclick="setLecture(24)" class="lecture-btn"')
    html = html.replace('class="lecture-btn active" id="btnLec24"', 'class="lecture-btn" id="btnLec24"')

    # Insert btnLec28 into group-math-ha before btnLec22 (Set ACTIVE)
    if 'id="btnLec28"' not in html:
        old_btn22 = '<button type="button" class="lecture-btn" id="btnLec22" onclick="setLecture(22)" data-subj="math-ha">'
        new_btn28 = '''<button type="button" class="lecture-btn active" id="btnLec28" onclick="setLecture(28)" data-subj="math-ha">
              <span class="lec-num">28</span>
              <span class="badge-pill-sm">⚡ 마스터</span>
              <span class="lec-title">교과서 14개 그래프 총정리</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec22" onclick="setLecture(22)" data-subj="math-ha">'''
        html = html.replace(old_btn22, new_btn28, 1)
        print("Inserted btnLec28 into group-math-ha.")

    # Insert btnLec25 into group-math1 before btnLec24
    if 'id="btnLec25"' not in html:
        old_btn24 = '<button type="button" class="lecture-btn" id="btnLec24" onclick="setLecture(24)" data-subj="math1">'
        new_btn25 = '''<button type="button" class="lecture-btn" id="btnLec25" onclick="setLecture(25)" data-subj="math1">
              <span class="lec-num">25</span>
              <span class="badge-pill-sm">⚡ 꿀팁</span>
              <span class="lec-title">점화식 25분 아작내기 (Big 4 &amp; 응용 6)</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec24" onclick="setLecture(24)" data-subj="math1">'''
        html = html.replace(old_btn24, new_btn25, 1)
        print("Inserted btnLec25 into group-math1.")

    # Insert btnLec27 into group-math2 before btnLec14
    if 'id="btnLec27"' not in html:
        old_btn14 = '<button type="button" class="lecture-btn" id="btnLec14" onclick="setLecture(14)" data-subj="math2">'
        new_btn27 = '''<button type="button" class="lecture-btn" id="btnLec27" onclick="setLecture(27)" data-subj="math2">
              <span class="lec-num">27</span>
              <span class="badge-pill-sm">⚡ 킬러</span>
              <span class="lec-title">다항함수를 보는 눈 (인수와 대칭성)</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec14" onclick="setLecture(14)" data-subj="math2">'''
        html = html.replace(old_btn14, new_btn27, 1)
        print("Inserted btnLec27 into group-math2.")

    # Insert btnLec26 into group-geom before btnLec23
    if 'id="btnLec26"' not in html:
        old_btn23 = '<button type="button" class="lecture-btn" id="btnLec23" onclick="setLecture(23)" data-subj="geom">'
        new_btn26 = '''<button type="button" class="lecture-btn" id="btnLec26" onclick="setLecture(26)" data-subj="geom">
              <span class="lec-num">26</span>
              <span class="badge-pill-sm">⚡ 심화</span>
              <span class="lec-title">테일러 급수 (초월함수의 다항식 근사)</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec23" onclick="setLecture(23)" data-subj="geom">'''
        html = html.replace(old_btn23, new_btn26, 1)
        print("Inserted btnLec26 into group-geom.")

    # 6. Update Status banner default to Lecture 28
    html = re.sub(
        r'<span class="status-subj" id="statusSubjText">[^<]+</span>\s*<span class="status-sep">/</span>\s*<span class="status-title" id="statusTitleText">[^<]+</span>',
        r'<span class="status-subj" id="statusSubjText">수학(하) · 함수와 그래프</span>\n        <span class="status-sep">/</span>\n        <span class="status-title" id="statusTitleText">제28강 · 대한민국 고교 교과서 14개 그래프 총정리</span>',
        html
    )

    # 7. Hide lecture24View by default
    html = html.replace('<div id="lecture24View">', '<div id="lecture24View" style="display: none;">')

    # 8. Insert Views 25, 26, 27, 28 before lecture24View
    # Note: v28 has display: block; v25, v26, v27 have display: none;
    combined_views = f"{v28}\n{v27}\n{v26}\n{v25}"
    if '<div id="lecture25View">' not in html:
        target_lec24_view = '<div id="lecture24View"'
        html = html.replace(target_lec24_view, combined_views + '\n    ' + target_lec24_view, 1)
        print("Inserted lecture views 25, 26, 27, 28 into HTML.")

    # 9. Update JS Metadata
    old_meta_start = 'const LECTURE_META = {'
    new_meta_entries = '''const LECTURE_META = {
      28: { subj: 'math-ha', subjName: '수학(하) · 함수와 그래프', title: '제28강 · 대한민국 고교 교과서 14개 그래프 총정리' },
      27: { subj: 'math2',   subjName: '수학 II · 다항함수의 미분', title: '제27강 · 다항함수를 보는 눈 (인수와 대칭성, 8칸 박스법)' },
      26: { subj: 'geom',    subjName: '기하 & 미적분 · 급수 근사', title: '제26강 · 테일러 급수 (초월함수가 다항함수로 바뀌는 기적)' },
      25: { subj: 'math1',   subjName: '수학 I · 수열의 귀납적 정의', title: '제25강 · 점화식 25분 아작내기 (등차·등비 Big 4 & 응용 6대 점화식)' },'''
    html = html.replace(old_meta_start, new_meta_entries, 1)

    # 10. Loop 24 -> 28
    html = re.sub(r'for \(let i = 1; i <= 24; i\+\+\)', r'for (let i = 1; i <= 28; i++)', html)

    # 11. setLecture num dispatch
    old_set_num24 = 'if (num === 24) setTimeout(renderL24, 50);'
    new_set_nums = '''if (num === 28) setTimeout(renderL28, 50);
      else if (num === 27) setTimeout(renderL27, 50);
      else if (num === 26) setTimeout(renderL26, 50);
      else if (num === 25) setTimeout(renderL25, 50);
      else if (num === 24) setTimeout(renderL24, 50);'''
    html = html.replace(old_set_num24, new_set_nums, 1)

    # 12. Insert JS Logic before window.addEventListener('load')
    target_window_load = "window.addEventListener('load', () => {"
    combined_js = f"{js25}\n\n{js26}\n\n{js27}\n\n{js28}"
    html = html.replace(target_window_load, combined_js + '\n    ' + target_window_load, 1)

    # In window.addEventListener('load'), setLecture(28) and renderL28()
    html = html.replace("setLecture(24);\n      renderL24();", "setLecture(28);\n      renderL28();")
    html = html.replace("setLecture(24);", "setLecture(28);")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully rebuilt index.html with Lecture 28 active on load!")

if __name__ == '__main__':
    main()
