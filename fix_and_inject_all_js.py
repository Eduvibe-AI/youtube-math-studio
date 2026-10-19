# -*- coding: utf-8 -*-
"""
Fix index.html by:
1. Stripping any content accidentally appended after </html>
2. Extracting JS codes for Lectures 15, 16, 17, and 18 from their build scripts
3. Injecting all of them cleanly inside <script> right before window load initialization
4. Updating window load initialization to setLecture(18) and renderL18()
"""

import os

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Clean after </html>
    idx_end = html.find('</html>')
    if idx_end != -1:
        html = html[:idx_end + len('</html>')]

    # 2. Extract JS codes
    def get_js(build_file, varname):
        with open(build_file, 'r', encoding='utf-8') as f:
            t = f.read()
        target = f"{varname} = '''"
        idx = t.find(target)
        if idx == -1:
            raise ValueError(f"Could not find {target} in {build_file}")
        end_idx = t.find("'''", idx + len(target))
        return t[idx + len(target) : end_idx]

    js15 = get_js('build_index_v15.py', 'js_code_15')
    js16 = get_js('build_index_v16.py', 'js_code_16')
    js17 = get_js('build_index_v17.py', 'js_code_17')
    js18 = get_js('build_index_v18.py', 'js_code_18')

    # 3. Locate initialization block inside <script>
    target_load = "// Initialize on page load"
    idx_load = html.find(target_load)
    if idx_load == -1:
        raise ValueError("Could not find '// Initialize on page load' in index.html")

    combined_js = (
        "\n\n    " + js15.strip() +
        "\n\n    " + js16.strip() +
        "\n\n    " + js17.strip() +
        "\n\n    " + js18.strip() +
        "\n\n    "
    )

    new_load_block = """// Initialize on page load
    window.addEventListener('load', () => {
      setLecture(18);
      renderL18();
    });"""

    # Find the old load block
    end_load = html.find('</script>', idx_load)
    
    html = html[:idx_load] + combined_js + new_load_block + "\n  " + html[end_load:]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("index.html fixed and all JS 15~18 injected successfully!")

if __name__ == '__main__':
    main()
