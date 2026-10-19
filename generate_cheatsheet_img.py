import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Set font for Korean
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(2, 2, figsize=(18, 14), facecolor='#080d17')

# Color palette
GOLD = '#fbbf24'
CYAN = '#38bdf8'
ROSE = '#f43f5e'
GREEN = '#34d399'
TEXT_COLOR = '#f8fafc'
DIM_TEXT = '#94a3b8'

# 1. Formula 1: Angle Bisector -> Isosceles Triangle (p.56 #233, #234, p.57 #242, p.58 #245, p.59 #250)
ax1 = axes[0, 0]
ax1.set_facecolor('#0f172a')
ax1.set_title('[공식 1] 엇각 + 내각 이등분선 = 무조건 이등변삼각형', fontsize=16, color=GOLD, fontweight='bold', pad=15)

# Parallelogram ABCD
pts = np.array([[1, 1], [5, 1], [7, 4], [3, 4]])
poly = patches.Polygon(pts, closed=True, edgecolor=CYAN, facecolor='none', linewidth=2.5)
ax1.add_patch(poly)

# Bisector from B to AD at E
ax1.plot([1, 4], [1, 4], color=ROSE, linewidth=2.5, linestyle='--')
ax1.plot([1, 1], [1, 1], 'o', color=GOLD)
ax1.plot([4, 4], [4, 4], 'o', color=ROSE)

ax1.text(1, 0.6, 'B', color=CYAN, fontsize=14, fontweight='bold', ha='center')
ax1.text(5, 0.6, 'C', color=CYAN, fontsize=14, fontweight='bold', ha='center')
ax1.text(7, 4.2, 'D', color=CYAN, fontsize=14, fontweight='bold', ha='center')
ax1.text(3, 4.2, 'A', color=CYAN, fontsize=14, fontweight='bold', ha='center')
ax1.text(4, 4.2, 'E', color=ROSE, fontsize=14, fontweight='bold', ha='center')

# Highlight AB = AE
ax1.text(1.7, 2.6, 'c', color=GOLD, fontsize=14, fontweight='bold')
ax1.text(3.5, 3.6, 'c', color=GOLD, fontsize=14, fontweight='bold')

desc1 = (
    "★ 3초 컷 치트키:\n"
    "• 평행선(엇각) + 각의 이등분선 => 무조건 AB = AE (이등변!)\n"
    "• ∠AEB = ∠CBE (엇각) = ∠ABE (이등분)\n"
    "• 적용 문항: 233번, 234번, 242번, 245번, 250번 올킬!"
)
ax1.text(0.5, 1.8, desc1, color=TEXT_COLOR, fontsize=12, bbox=dict(boxstyle='round,pad=0.6', facecolor='#1e293b', edgecolor=GOLD, alpha=0.9))
ax1.set_xlim(0, 8)
ax1.set_ylim(0, 5)
ax1.axis('off')

# 2. Formula 2: Paper Folding -> Isosceles Triangle (p.58 #243, #246)
ax2 = axes[0, 1]
ax2.set_facecolor('#0f172a')
ax2.set_title('[공식 2] 종이 접기 = 접은 각과 엇각으로 100% 이등변', fontsize=16, color=CYAN, fontweight='bold', pad=15)

ax2.plot([1, 6], [1, 1], color=CYAN, linewidth=2)
ax2.plot([2, 7], [4, 4], color=CYAN, linewidth=2)
# Folded line BD
ax2.plot([1, 5], [1, 4], color=GOLD, linewidth=3)
ax2.plot([1, 3.5], [1, 4.5], color=ROSE, linewidth=2.5, linestyle='--')
ax2.plot([5, 3.5], [4, 4.5], color=ROSE, linewidth=2.5, linestyle='--')

desc2 = (
    "★ 3초 컷 치트키:\n"
    "• 접은 각 = 원래 각 = x\n"
    "• 평행선 엇각 = x => △FBD는 무조건 FB = FD 이등변!\n"
    "• 243번: 86° + 2x = 180° => x = 47° 즉시 암산!\n"
    "• 246번: 정오각형 108° => 밑각 x = (180-108)/2 = 36° 즉시 암산!"
)
ax2.text(0.5, 1.8, desc2, color=TEXT_COLOR, fontsize=12, bbox=dict(boxstyle='round,pad=0.6', facecolor='#1e293b', edgecolor=CYAN, alpha=0.9))
ax2.set_xlim(0, 8)
ax2.set_ylim(0, 5)
ax2.axis('off')

# 3. Formula 3: Right Triangle Circumcenter on Diagonal (p.58 #247)
ax3 = axes[1, 0]
ax3.set_facecolor('#0f172a')
ax3.set_title('[공식 3] 대각선 중점 O = 직각삼각형 AHC의 외심', fontsize=16, color=ROSE, fontweight='bold', pad=15)

pts3 = np.array([[1, 1], [6, 1], [7, 4], [2, 4]])
poly3 = patches.Polygon(pts3, closed=True, edgecolor=CYAN, facecolor='none', linewidth=2)
ax3.add_patch(poly3)

# Diagonal AC
ax3.plot([2, 6], [4, 1], color=GOLD, linewidth=2)
# Altitude AH
ax3.plot([2, 2], [4, 1], color=ROSE, linewidth=2.5)
# Median OH
ax3.plot([4, 2], [2.5, 1], color=GREEN, linewidth=2.5, linestyle='--')

ax3.plot([4, 4], [2.5, 2.5], 'o', color=GOLD)
ax3.text(4, 2.8, 'O (중점=외심)', color=GOLD, fontsize=12, fontweight='bold', ha='center')
ax3.text(2, 4.2, 'A', color=CYAN, fontsize=13, fontweight='bold')
ax3.text(6, 0.7, 'C', color=CYAN, fontsize=13, fontweight='bold')
ax3.text(2, 0.6, 'H (직각)', color=ROSE, fontsize=13, fontweight='bold')

desc3 = (
    "★ 3초 컷 치트키:\n"
    "• 평행사변형 대각선 중점 O = 직각삼각형 AHC 빗변 중점!\n"
    "• 직각삼각형의 외심 성질 => OA = OC = OH (이등변!)\n"
    "• ∠OCH = 40° => ∠OHC = 40°\n"
    "• 247번: ∠HOC = 180° - (40° + 40°) = 100° (한 줄 컷!)"
)
ax3.text(0.5, 1.6, desc3, color=TEXT_COLOR, fontsize=12, bbox=dict(boxstyle='round,pad=0.6', facecolor='#1e293b', edgecolor=ROSE, alpha=0.9))
ax3.set_xlim(0, 8)
ax3.set_ylim(0, 5)
ax3.axis('off')

# 4. Formula 4: Area Conservation & Quarter Grid (p.57 #241, p.58 #248)
ax4 = axes[1, 1]
ax4.set_facecolor('#0f172a')
ax4.set_title('[공식 4] 내부점 대변 넓이 합 & 1/4 중점 격자 공식', fontsize=16, color=GREEN, fontweight='bold', pad=15)

desc4 = (
    "★ 3초 컷 치트키:\n"
    "1) 내부 임의의 점 P:\n"
    "   S(PAB) + S(PCD) = S(PDA) + S(PBC) = 1/2 □ABCD\n"
    "   • 248번: 밑변 공유 S(AQD) = 3x = 1/2 □ABCD\n"
    "     24 + x = 3x => x = 12 => □ABCD = 2*(24+12) = 72 cm²!\n\n"
    "2) 중점 연결 내부 평행사변형 넓이:\n"
    "   • 241번: □AEGH = 1/4 □ABCD = 60 / 4 = 15 cm²!\n"
    "3) 중점 관통선 절반 공식:\n"
    "   • 232번: AD = BC = 1/2 BF = 12 / 2 = 6 cm!\n"
    "   • 252번: EF = 1/2 EO = 14 / 2 = 7 cm!"
)
ax4.text(0.5, 2.5, desc4, color=TEXT_COLOR, fontsize=12, bbox=dict(boxstyle='round,pad=0.8', facecolor='#1e293b', edgecolor=GREEN, alpha=0.9), va='center')
ax4.set_xlim(0, 8)
ax4.set_ylim(0, 5)
ax4.axis('off')

plt.tight_layout()
plt.savefig('rpm_geometry_master_cheatsheet.png', dpi=180, facecolor=fig.get_facecolor(), edgecolor='none')
print("Successfully saved rpm_geometry_master_cheatsheet.png!")
