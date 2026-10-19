# -*- coding: utf-8 -*-
"""
Build script to register Lectures 32 and 33 into index.html
Lecture 32: 지수·로그 함수의 확대·축소 & 실전 비율 관계 (math1)
Lecture 33: 정적분의 본질 · 넓이 vs 함숫값의 이중성 (math2)
"""

import re
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

def main():
    html_path = 'index.html'
    backup_path = 'index_backup_v31.html'
    shutil.copyfile(html_path, backup_path)
    print(f"Backed up index.html to {backup_path}")

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Read Manim scripts with escaping
    def load_manim(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            return f.read().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    m32 = load_manim('exp_log_scaling_ratio_manim.py')
    m33 = load_manim('integral_signed_area_vs_height_manim.py')

    # 2. Read Views
    with open('view_lecture32.html', 'r', encoding='utf-8') as f:
        v32 = f.read().replace('__MANIM_CODE_32__', m32)
    with open('view_lecture33.html', 'r', encoding='utf-8') as f:
        v33 = f.read().replace('__MANIM_CODE_33__', m33)

    # 3. Read JS files
    with open('js_lecture32.js', 'r', encoding='utf-8') as f:
        js32 = f.read()
    with open('js_lecture33.js', 'r', encoding='utf-8') as f:
        js33 = f.read()

    # 4. Update Navigation Tabs Badges
    # Total: 31 -> 33
    html = re.sub(
        r'(<button type="button" class="subj-tab(?: active)?" data-subject="all"[^>]*>[\s\S]*?<span class="tab-badge">)31(</span>)',
        r'\g<1>33\g<2>',
        html
    )
    # Math1: 10 -> 11 (Lecture 32 added)
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math1"[^>]*>[\s\S]*?<span class="tab-badge">)10(</span>)',
        r'\g<1>11\g<2>',
        html
    )
    # Math2: 8 -> 9 (Lecture 33 added)
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math2"[^>]*>[\s\S]*?<span class="tab-badge">)8(</span>)',
        r'\g<1>9\g<2>',
        html
    )

    # Summary link text
    html = html.replace('사진 1~31 요약집', '사진 1~33 요약집')
    html = html.replace('사진 1~31 핵심 전용 페이지', '사진 1~33 핵심 전용 페이지')

    # 5. Insert Lecture Buttons
    # Insert btnLec32 into group-math1 before btnLec31
    if 'id="btnLec32"' not in html:
        old_btn31 = '<button type="button" class="lecture-btn" id="btnLec31"'
        new_btn32 = '''<button type="button" class="lecture-btn" id="btnLec32" onclick="setLecture(32)" data-subj="math1">
              <span class="lec-num">32</span>
              <span class="badge-pill-sm">⚡ 실전팁</span>
              <span class="lec-title">지수·로그 확대·축소 &amp; 실전 비율 관계</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec31"'''
        html = html.replace(old_btn31, new_btn32, 1)
        print("Inserted btnLec32 into group-math1.")

    # Insert btnLec33 into group-math2 before btnLec29
    if 'id="btnLec33"' not in html:
        old_btn29 = '<button type="button" class="lecture-btn" id="btnLec29"'
        new_btn33 = '''<button type="button" class="lecture-btn" id="btnLec33" onclick="setLecture(33)" data-subj="math2">
              <span class="lec-num">33</span>
              <span class="badge-pill-sm">⚡ 본질</span>
              <span class="lec-title">정적분의 본질 · 넓이 vs 함숫값의 이중성</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec29"'''
        html = html.replace(old_btn29, new_btn33, 1)
        print("Inserted btnLec33 into group-math2.")

    # 6. Insert Views 33, 32 before lecture31View
    combined_views = f"{v33}\n{v32}"
    if '<div id="lecture32View">' not in html:
        target_lec31_view = '<div id="lecture31View"'
        html = html.replace(target_lec31_view, combined_views + '\n    ' + target_lec31_view, 1)
        print("Inserted lecture views 32, 33 into HTML.")

    # 7. Update JS Metadata
    old_meta_start = 'const LECTURE_META = {'
    new_meta_entries = '''const LECTURE_META = {
      33: { subj: 'math2',   subjName: '수학 II · 다항함수의 적분법', title: '제33강 · 정적분의 본질 · 넓이 vs 함숫값의 이중성' },
      32: { subj: 'math1',   subjName: '수학 I · 지수함수와 로그함수', title: '제32강 · 지수·로그 함수의 확대·축소 & 실전 비율 관계' },'''
    html = html.replace(old_meta_start, new_meta_entries, 1)

    # 8. Loop 31 -> 33
    html = re.sub(r'for \(let i = 1; i <= 31; i\+\+\)', r'for (let i = 1; i <= 33; i++)', html)

    # 9. setLecture num dispatch
    old_set_num31 = 'if (num === 31) setTimeout(renderL31, 50);'
    new_set_nums = '''if (num === 33) setTimeout(renderL33, 50);
      else if (num === 32) setTimeout(renderL32, 50);
      else if (num === 31) setTimeout(renderL31, 50);'''
    html = html.replace(old_set_num31, new_set_nums, 1)

    # 10. Insert JS Logic before window.addEventListener('load')
    target_window_load = "window.addEventListener('load', () => {"
    combined_js = f"{js32}\n\n{js33}"
    html = html.replace(target_window_load, combined_js + '\n    ' + target_window_load, 1)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully registered Lectures 32 and 33 into index.html!")

if __name__ == '__main__':
    main()
