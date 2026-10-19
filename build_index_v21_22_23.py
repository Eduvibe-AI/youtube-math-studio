# -*- coding: utf-8 -*-
"""
Build script to cleanly register Lectures 21, 22, 23 into index.html
"""

import re

def main():
    html_path = 'index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read manim codes
    with open('trig_ratio_relations_manim.py', 'r', encoding='utf-8') as f:
        manim_21 = f.read().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    with open('composite_function_n_axis_manim.py', 'r', encoding='utf-8') as f:
        manim_22 = f.read().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    with open('parabola_seven_properties_manim.py', 'r', encoding='utf-8') as f:
        manim_23 = f.read().replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # Read views
    with open('view_lecture21.html', 'r', encoding='utf-8') as f:
        v21 = f.read().replace('__MANIM_CODE_21__', manim_21)

    with open('view_lecture22.html', 'r', encoding='utf-8') as f:
        v22 = f.read().replace('__MANIM_CODE_22__', manim_22)

    with open('view_lecture23.html', 'r', encoding='utf-8') as f:
        v23 = f.read().replace('__MANIM_CODE_23__', manim_23)

    # Read JS
    with open('js_lecture21_22_23.js', 'r', encoding='utf-8') as f:
        js_code = f.read()

    # 1. Update Navigation Tabs Badges
    # Total badge: 20 -> 23
    html = re.sub(
        r'(<button type="button" class="subj-tab(?: active)?" data-subject="all"[^>]*>[\s\S]*?<span class="tab-badge">)20(</span>)',
        r'\g<1>23\g<2>',
        html
    )
    # Math-ha badge: 6 -> 7
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math-ha"[^>]*>[\s\S]*?<span class="tab-badge">)6(</span>)',
        r'\g<1>7\g<2>',
        html
    )
    # Math1 badge: 5 -> 6
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="math1"[^>]*>[\s\S]*?<span class="tab-badge">)5(</span>)',
        r'\g<1>6\g<2>',
        html
    )
    # Geom badge: 3 -> 4
    html = re.sub(
        r'(<button type="button" class="subj-tab" data-subject="geom"[^>]*>[\s\S]*?<span class="tab-badge">)3(</span>)',
        r'\g<1>4\g<2>',
        html
    )

    # Special summary link text: 1~20 -> 1~23
    html = html.replace('사진 1~20 요약집', '사진 1~23 요약집')
    html = html.replace('사진 1~20 핵심 전용 페이지', '사진 1~23 핵심 전용 페이지')

    # De-activate btnLec20
    html = html.replace('id="btnLec20" onclick="setLecture(20)" class="lecture-btn active"', 'id="btnLec20" onclick="setLecture(20)" class="lecture-btn"')
    html = html.replace('class="lecture-btn active" id="btnLec20"', 'class="lecture-btn" id="btnLec20"')

    # 2. Insert Navigation Buttons
    # In group-math1: insert btnLec21 (active)
    if 'id="btnLec21"' not in html:
        old_btn20 = '<button type="button" class="lecture-btn" id="btnLec20" onclick="setLecture(20)" data-subj="math1">'
        new_btn21 = '''<button type="button" class="lecture-btn active" id="btnLec21" onclick="setLecture(21)" data-subj="math1">
              <span class="lec-num">21</span>
              <span class="badge-pill-sm">⚡ 필수</span>
              <span class="lec-title">삼각함수 비율관계</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec20" onclick="setLecture(20)" data-subj="math1">'''
        html = html.replace(old_btn20, new_btn21, 1)
        print("Inserted btnLec21 into group-math1.")

    # In group-math-ha: insert btnLec22
    if 'id="btnLec22"' not in html:
        old_btn18 = '<button type="button" class="lecture-btn" id="btnLec18" onclick="setLecture(18)" data-subj="math-ha">'
        new_btn22 = '''<button type="button" class="lecture-btn" id="btnLec22" onclick="setLecture(22)" data-subj="math-ha">
              <span class="lec-num">22</span>
              <span class="badge-pill-sm">⚡ 꿀팁</span>
              <span class="lec-title">합성함수 그래프 그리기 (N축 스킬)</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec18" onclick="setLecture(18)" data-subj="math-ha">'''
        html = html.replace(old_btn18, new_btn22, 1)
        print("Inserted btnLec22 into group-math-ha.")

    # In group-geom: insert btnLec23
    if 'id="btnLec23"' not in html:
        old_btn12 = '<button type="button" class="lecture-btn" id="btnLec12" onclick="setLecture(12)" data-subj="geom">'
        new_btn23 = '''<button type="button" class="lecture-btn" id="btnLec23" onclick="setLecture(23)" data-subj="geom">
              <span class="lec-num">23</span>
              <span class="badge-pill-sm">⚡ 수능</span>
              <span class="lec-title">포물선의 기하학적 성질 7가지</span>
            </button>
            <button type="button" class="lecture-btn" id="btnLec12" onclick="setLecture(12)" data-subj="geom">'''
        html = html.replace(old_btn12, new_btn23, 1)
        print("Inserted btnLec23 into group-geom.")

    # Update Status banner default
    html = re.sub(
        r'<span class="status-subj" id="statusSubjText">[^<]+</span>\s*<span class="status-sep">/</span>\s*<span class="status-title" id="statusTitleText">[^<]+</span>',
        r'<span class="status-subj" id="statusSubjText">수학 I · 삼각함수 비율관계</span>\n        <span class="status-sep">/</span>\n        <span class="status-title" id="statusTitleText">제21강 · 삼각함수 비율관계 (8칸 박스와 $1:2$ 분할의 마법)</span>',
        html
    )

    # Hide lecture20View by default
    html = html.replace('<div id="lecture20View">', '<div id="lecture20View" style="display: none;">')

    # 3. Insert Views before lecture20View
    if '<div id="lecture21View">' not in html:
        target_lec20_view = '<div id="lecture20View"'
        new_views = v21 + '\n' + v22 + '\n' + v23 + '\n' + target_lec20_view
        html = html.replace(target_lec20_view, new_views, 1)
        print("Inserted lecture21View, lecture22View, lecture23View into HTML.")

    # 4. Update JS Metadata & Handlers
    old_meta_start = 'const LECTURE_META = {'
    new_meta_entries = '''const LECTURE_META = {
      23: { subj: 'geom',    subjName: '기하 · 이차곡선 (포물선)', title: '제23강 · 포물선의 기하학적 성질 7가지' },
      22: { subj: 'math-ha', subjName: '수학(하) · 합성함수와 N축', title: '제22강 · 합성함수 그래프 그리기 (N축 스킬)' },
      21: { subj: 'math1',   subjName: '수학 I · 삼각함수 비율관계', title: '제21강 · 삼각함수 비율관계 (8칸 박스와 $1:2$ 분할의 마법)' },'''
    html = html.replace(old_meta_start, new_meta_entries, 1)

    # Loop 20 -> 23 in setLecture and selectSubject
    html = re.sub(r'for \(let i = 1; i <= 20; i\+\+\)', r'for (let i = 1; i <= 23; i++)', html)

    # setLecture num handling
    old_set_num20 = 'if (num === 20) setTimeout(renderL20, 50);'
    new_set_nums = '''if (num === 23) setTimeout(renderL23, 50);
      else if (num === 22) setTimeout(renderL22, 50);
      else if (num === 21) setTimeout(renderL21, 50);
      else if (num === 20) setTimeout(renderL20, 50);'''
    html = html.replace(old_set_num20, new_set_nums, 1)

    # 5. Insert JS Logic before window.addEventListener('load')
    target_window_load = "window.addEventListener('load', () => {"
    html = html.replace(target_window_load, js_code + '\n    ' + target_window_load, 1)

    # In window.addEventListener('load'), setLecture(21) and renderL21()
    html = html.replace("setLecture(20);\n      renderL20();", "setLecture(21);\n      renderL21();")
    html = html.replace("setLecture(20);", "setLecture(21);")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done! Successfully built index.html with Lectures 21, 22, 23.")

if __name__ == '__main__':
    main()
