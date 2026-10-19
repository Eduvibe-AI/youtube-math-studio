import os
from PIL import Image, ImageDraw, ImageFont

def create_cheatsheet():
    width = 1600
    height = 2400
    img = Image.new('RGB', (width, height), color='#070a13')
    draw = ImageDraw.Draw(img)

    # Load fonts
    font_title = ImageFont.truetype('C:/Windows/Fonts/malgunbd.ttf', 44)
    font_sub = ImageFont.truetype('C:/Windows/Fonts/malgun.ttf', 24)
    font_card_title = ImageFont.truetype('C:/Windows/Fonts/malgunbd.ttf', 28)
    font_body_bold = ImageFont.truetype('C:/Windows/Fonts/malgunbd.ttf', 20)
    font_body = ImageFont.truetype('C:/Windows/Fonts/malgun.ttf', 18)
    font_code = ImageFont.truetype('C:/Windows/Fonts/malgunbd.ttf', 19)
    font_small = ImageFont.truetype('C:/Windows/Fonts/malgun.ttf', 16)

    # Top Header Banner
    draw.rectangle([0, 0, width, 180], fill='#0f172a')
    draw.line([0, 180, width, 180], fill='#38bdf8', width=3)

    draw.text((60, 35), "RPM Pro 중학 2-2 [56~59쪽] 평행사변형 시험만점 3초 초고속 일반화 공식집", fill='#f8fafc', font=font_title)
    draw.text((60, 95), "답지의 복잡한 합동 증명은 버려라! 어떤 변형 문제가 나와도 10초 컷으로 끝내는 8대 절대 공식", fill='#38bdf8', font=font_sub)
    draw.text((60, 135), "유튜브 수학 마스터 에디션 · 229번 ~ 252번 (총 24문항) 전수 공식화", fill='#94a3b8', font=font_small)

    formulas = [
        {
            "num": "01",
            "title": "엇각 + 내각 이등분선 100% 이등변 삼각형 공식",
            "tag": "빈출도 ★★★★★ | 적용 문항: 233, 234, 242, 245, 250",
            "rule": "평행선 사이(AD ∥ BC)에서 어느 한 각을 이등분하면(∠BAE = ∠DAE) 엇각 성질에 의해\n"
                    "반드시 ∠BAE = ∠BEA가 되어 △ABE는 무조건 AB = BE인 이등변삼각형이 된다!\n"
                    "▶ 이등분선이 보이면 각도 계산하지 말고 즉시 [AB = BE] 선분 길이부터 체크!",
            "shortcut": "• 233번: A:B = 5:4 => B=80°, DC=DE 이등변 => ∠BCE = (180°-80°)/2 = 50° (암산 3초!)\n"
                        "• 234번: 이등분선 엇각 => ∠B = 2×48° = 96° => 이웃각 합 180°로 ∠C = 180°-96° = 84°\n"
                        "• 250번: ∠C=120° => ∠B=60°, 이등분선 => △ABE 정삼각형! AE=8, AD=8+2=10, 둘레=28cm"
        },
        {
            "num": "02",
            "title": "이웃한 두 내각의 이등분선 직교(90°) & 역성질 공식",
            "tag": "빈출도 ★★★★★ | 적용 문항: 220, 245",
            "rule": "평행사변형은 이웃한 두 각의 합이 180°이므로, 두 각을 각각 이등분하면 1/2×(∠A+∠B) = 90°!\n"
                    "따라서 이등분선 교각은 무조건 90°(직각)이다.\n"
                    "▶ 역성질(245번): AP가 ∠A의 이등분선이고 ∠APB=90°이면, 선분 BP는 자동으로 ∠B의 이등분선이다!",
            "shortcut": "• 245번: ∠D=74° => ∠B=74°. BP가 ∠B의 이등분선이므로 ∠PBC = 74°/2 = 37° (계산 2초 끝!)"
        },
        {
            "num": "03",
            "title": "종이 접기(대칭) 각도 보존 & 이등변삼각형 치트키",
            "tag": "빈출도 ★★★★☆ | 적용 문항: 243, 246",
            "rule": "[접은 각 = 원래 각 = 엇각] 삼위일체 원리! 접힌 삼각형은 무조건 이등변삼각형이다.\n"
                    "평행선 사이에서 접으면: 연장선과 이루는 외각 θ에 대해 2x + θ = 180° 성립!",
            "shortcut": "• 243번: 2x + 86° = 180° => 2x = 94° => x = 47° (답지 10줄 증명 대신 3초 컷!)\n"
                        "• 246번: 접힌 정오각형 내각 = 108° => △BAE는 BA=BE인 이등변 => x = (180°-108°)/2 = 36°"
        },
        {
            "num": "04",
            "title": "대각선 교점 O = 직각삼각형 빗변 중점 = 외심 정리",
            "tag": "빈출도 ★★★★★ | 적용 문항: 247",
            "rule": "평행사변형 대각선은 서로 이등분하므로 교점 O는 대각선 AC의 정확한 '중점'이다.\n"
                    "꼭짓점 A에서 수선 AH를 내리면 △AHC는 빗변이 AC인 직각삼각형이 되고, O는 바로 '외심'!\n"
                    "따라서 OA = OC = OH 가 성립하여 △OHC는 무조건 밑각이 같은 이등변삼각형!",
            "shortcut": "• 247번: 엇각 ∠OCH = ∠DAC = 40°. O가 외심이므로 ∠OHC = 40° 자동 확정!\n"
                        "         중심각 ∠HOC = 180° - 2×40° = 100° (공식만 알면 5초 컷!)"
        },
        {
            "num": "05",
            "title": "평행사변형 내부 점 P 넓이 마주보는 합 불변식 & 밑변 공유식",
            "tag": "빈출도 ★★★★★ | 적용 문항: 248",
            "rule": "내부 임의의 점 P에 대해: S(PAB) + S(PCD) = S(PDA) + S(PBC) = 1/2 × □ABCD\n"
                    "또한 밑변 AD를 공유하고 꼭짓점이 대변 BC 위에 있는 임의의 삼각형 S(AQD) = 1/2 × □ABCD!\n"
                    "따라서 S(AQD) = S(PBC) + S(PDA) 라는 킬러 등식이 성립한다!",
            "shortcut": "• 248번: S(PDA) = x, S(PQD) = 2x => S(AQD) = 3x = 1/2□\n"
                        "         S(PBC) + S(PDA) = 24 + x = 1/2□ => 3x = 24 + x => 2x = 24 => x = 12\n"
                        "         □ABCD = 2 × (24 + 12) = 72 cm²"
        },
        {
            "num": "06",
            "title": "대변 중점 연결 사각형 1/4 격자 넓이 공식",
            "tag": "빈출도 ★★★★☆ | 적용 문항: 241",
            "rule": "평행사변형 ABCD에서 두 대변의 중점 E, F를 잡고 대각선과 교차시켜 만든 사각형 □AEGH는\n"
                    "평행사변형을 4등분한 사각 격자 조각과 넓이가 완벽히 일치한다!\n"
                    "넓이 공식: Area(□AEGH) = 1/4 × Area(□ABCD)",
            "shortcut": "• 241번: 전체 넓이 = 60 cm² => □AEGH = 60 / 4 = 15 cm² (1초 만에 바로 정답 ④ 찍기!)"
        },
        {
            "num": "07",
            "title": "변의 중점 관통선 모래시계 1:1 합동 절반 공식",
            "tag": "빈출도 ★★★★☆ | 적용 문항: 232, 252",
            "rule": "평행사변형에서 한 변의 중점을 통과하는 직선이 연장선과 만나면 1:1 모래시계 합동 발생!\n"
                    "따라서 바깥으로 뻗어나간 선분 길이는 원래 변의 길이와 같고, 밑변 전체의 정확히 1/2이 된다.",
            "shortcut": "• 232번: CD 중점 E 관통 => △AED ≡ △FEC => AD = CF = BC. 따라서 AD = 1/2 BF = 12 / 2 = 6 cm\n"
                        "• 252번: AC 중점 O 관통 => □EOCD 평행사변형 => EO = AB = 14cm => EF = 1/2 EO = 7 cm"
        },
        {
            "num": "08",
            "title": "대각선 이등분 & 둘레/각도 고속 계산 공식",
            "tag": "빈출도 ★★★★☆ | 적용 문항: 229, 231, 235, 240, 249, 251",
            "rule": "1) 대각선 둘레 공식: △OCD 둘레 = CD + 1/2(AC + BD) = AB + AO + BO\n"
                    "2) 대변 평행 엇각 공식: ∠x + ∠y = 180° - (주어진 엇각의 합)\n"
                    "3) 수선 발 대칭성: 대각선에 내린 두 수선 E, F는 대칭이므로 □EBFD는 항상 평행사변형!",
            "shortcut": "• 229번: ∠x + ∠y = 180° - (36° + 49°) = 95°\n"
                        "• 231번: x + 3 = 2x - 4 => x = 7 => BD = 3(7)-1 = 20 => BO = 10\n"
                        "• 235번: 둘레 = 12 + 5 + (18/2) = 12 + 5 + 9 = 26 cm\n"
                        "• 249번: 2x + 5 = 4x - 3 => x = 4, ∠D = 180° - 120° = 60° => y = 60 => xy = 240\n"
                        "• 251번: □EBFD 평행사변형 => ∠EBF = 90° - 55° = 35°"
        }
    ]

    card_y = 200
    card_height = 250
    gap = 22

    for f in formulas:
        # Card background
        draw.rounded_rectangle([40, card_y, width - 40, card_y + card_height], radius=14, fill='#0f172a', outline='#334155', width=1)
        
        # Left Accent pill
        draw.rounded_rectangle([55, card_y + 16, 125, card_y + 54], radius=8, fill='#1e293b', outline='#38bdf8', width=1)
        draw.text((70, card_y + 20), f"공식 {f['num']}", fill='#38bdf8', font=font_card_title)

        # Title
        draw.text((145, card_y + 22), f['title'], fill='#f8fafc', font=font_card_title)
        
        # Tag
        draw.text((width - 550, card_y + 26), f['tag'], fill='#fbbf24', font=font_small)

        # Divider line
        draw.line([55, card_y + 64, width - 55, card_y + 64], fill='#1e293b', width=1)

        # Rule Box
        draw.text((60, card_y + 75), "⚡ 핵심 일반화 원리:", fill='#34d399', font=font_body_bold)
        draw.text((60, card_y + 102), f['rule'], fill='#cbd5e1', font=font_body)

        # Shortcut Box
        draw.rounded_rectangle([55, card_y + 172, width - 55, card_y + card_height - 12], radius=8, fill='#182234', outline='#2563eb', width=1)
        draw.text((70, card_y + 176), "🚀 실전 3초 적용법:", fill='#fb7185', font=font_body_bold)
        draw.text((260, card_y + 177), f['shortcut'], fill='#f1f5f9', font=font_code)

        card_y += card_height + gap

    # Bottom Footer
    draw.rectangle([0, height - 70, width, height], fill='#0b0f19')
    draw.line([0, height - 70, width, height - 70], fill='#334155', width=1)
    draw.text((width//2 - 350, height - 48), "중등 수학 RPM Pro 2-2 평행사변형 마스터 치트시트 · 유튜브 수학 인포그래픽", fill='#64748b', font=font_sub)

    output_path = 'rpm_geometry_master_cheatsheet.png'
    img.save(output_path, 'PNG', quality=95)
    print(f"Successfully generated {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == '__main__':
    create_cheatsheet()
