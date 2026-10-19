import re, sys

def clean_vtt(vtt_file, out_file):
    with open(vtt_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    cues = []
    time_pat = re.compile(r'(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})')
    tag_pat = re.compile(r'<[^>]+>')
    
    current_time = None
    current_texts = []
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('WEBVTT') or line.startswith('NOTE') or line.startswith('STYLE'):
            continue
        
        m = time_pat.search(line)
        if m:
            if current_time and current_texts:
                clean_t = ' '.join(current_texts)
                clean_t = tag_pat.sub('', clean_t).strip()
                if clean_t and (not cues or cues[-1][1] != clean_t):
                    cues.append((current_time, clean_t))
            current_time = m.group(1)[:8] # HH:MM:SS
            current_texts = []
        elif current_time:
            # text line
            clean_line = tag_pat.sub('', line).strip()
            if clean_line and clean_line not in current_texts:
                current_texts.append(clean_line)
                
    if current_time and current_texts:
        clean_t = ' '.join(current_texts)
        clean_t = tag_pat.sub('', clean_t).strip()
        if clean_t and (not cues or cues[-1][1] != clean_t):
            cues.append((current_time, clean_t))
            
    # Deduplicate consecutive lines that are subsets
    filtered = []
    for t, txt in cues:
        if not filtered:
            filtered.append((t, txt))
        else:
            prev_t, prev_txt = filtered[-1]
            if txt == prev_txt:
                continue
            if txt.startswith(prev_txt) and len(txt) > len(prev_txt):
                filtered[-1] = (t, txt)
            else:
                filtered.append((t, txt))
                
    with open(out_file, 'w', encoding='utf-8') as f:
        for t, txt in filtered:
            f.write(f"[{t}] {txt}\n")
            
    print(f"Extracted {len(filtered)} cues into {out_file}")

if __name__ == '__main__':
    clean_vtt('sub_video9.ko.vtt', 'clean_transcript_video9.txt')
