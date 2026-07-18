#!/usr/bin/env python3
"""
Soundcore Guard — 数据叙事海报最终版
统一大标题、清晰叙事、不重叠、字号合理
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle
import os, warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'axes.unicode_minus': False,
    'figure.dpi': 200,
    'savefig.dpi': 200,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15,
})

OUT = os.path.dirname(os.path.abspath(__file__))

DARK    = '#111827'
GRAY    = '#6B7280'
LIGHT   = '#F8FAFC'
WHITE   = '#FFFFFF'
BLUE    = '#1A56DB'
SKY     = '#0EA5E9'
GREEN   = '#10B981'
AMBER   = '#F59E0B'
ORANGE  = '#F97316'
PURPLE  = '#8B5CF6'
RED     = '#EF4444'
BLUE_L  = '#DBEAFE'
GREEN_L = '#D1FAE5'

# 创建画布
fig = plt.figure(figsize=(24, 40), facecolor=LIGHT)
ax = fig.add_subplot(111)
ax.set_xlim(0, 24)
ax.set_ylim(0, 40)
ax.axis('off')

# ═══════════════════════════════════
# 1. 大标题
# ═══════════════════════════════════
ax.add_patch(FancyBboxPatch((0.5, 38.0), 23, 1.8, boxstyle="round,pad=0.15", facecolor=DARK, edgecolor='none'))
ax.text(12, 39.1, 'Soundcore Guard', fontsize=48, fontweight='bold', color=WHITE, ha='center', va='center')
ax.text(12, 38.35, 'An AI-Native Product Design Experiment for Anker Soundcore', fontsize=15, color='#93C5FD', ha='center', va='center')

# ═══════════════════════════════════
# 2. 核心问题
# ═══════════════════════════════════
ax.text(12, 37.3, 'The Core Question', fontsize=20, fontweight='bold', color=DARK, ha='center')
ax.add_patch(FancyBboxPatch((1.5, 35.5), 21, 1.5, boxstyle="round,pad=0.15", facecolor=BLUE_L, edgecolor=BLUE, linewidth=2, alpha=0.8))
ax.text(12, 36.35, 'What happens when we replace "PM intuition + small surveys" with AI acting as', fontsize=14, color=DARK, ha='center', style='italic')
ax.text(12, 35.85, 'Brain Trust, User Avatars, and Expert Panel — and let them define a product from scratch?', fontsize=14, color=DARK, ha='center', style='italic')
ax.text(12, 35.05, 'A product direction that experience-driven methods alone would not have found.', fontsize=15, fontweight='bold', color=BLUE, ha='center')

# ═══════════════════════════════════
# 3. 方法论对比
# ═══════════════════════════════════
ax.text(12, 34.3, 'Method Changed the Answer', fontsize=20, fontweight='bold', color=DARK, ha='center')

# 传统方法
ax.add_patch(FancyBboxPatch((1.5, 32.0), 10.5, 2.0, boxstyle="round,pad=0.15", facecolor='#FEF2F2', edgecolor=RED, linewidth=1.5))
ax.text(6.75, 33.7, 'Traditional Experience-Driven', fontsize=13, fontweight='bold', color=RED, ha='center')
steps_t = ['PM\nExperience', 'Small\nSurvey', 'Manual\nTracking', 'Boss\nDecides']
for i, s in enumerate(steps_t):
    x = 2.4 + i * 1.9
    ax.add_patch(FancyBboxPatch((x-0.7, 32.3), 1.4, 0.9, boxstyle="round,pad=0.06", facecolor=RED, edgecolor=WHITE, linewidth=1.2))
    ax.text(x, 32.75, s, fontsize=8, fontweight='bold', color=WHITE, ha='center', va='center')
    if i < 3:
        ax.annotate('', xy=(x+0.85, 32.75), xytext=(x+0.75, 32.75), arrowprops=dict(arrowstyle='->', color=RED, lw=1.5))
ax.add_patch(FancyBboxPatch((8.2, 32.25), 3.2, 1.0, boxstyle="round,pad=0.1", facecolor=RED, edgecolor=WHITE, linewidth=1.5, alpha=0.18))
ax.text(9.8, 32.75, '→ "Better ANC +\nAI Translate"\n(Me-too)', fontsize=8.5, fontweight='bold', color=RED, ha='center', va='center')

# AI原生方法
ax.add_patch(FancyBboxPatch((12, 32.0), 10.5, 2.0, boxstyle="round,pad=0.15", facecolor=BLUE_L, edgecolor=BLUE, linewidth=1.5))
ax.text(17.25, 33.7, 'AI-Native Method', fontsize=13, fontweight='bold', color=BLUE, ha='center')
steps_ai = ['AI Brain\nTrust', 'AI User\nAvatars', 'AI Expert\nPanel', 'PM\nVerdict']
colors_ai = [BLUE, SKY, GREEN, PURPLE]
ai_xs = [13.0, 14.8, 16.4, 18.0, 20.6]
for i, (step, ax_) in enumerate(zip(steps_ai, ai_xs)):
    if i < 4:
        ax.add_patch(FancyBboxPatch((ax_-0.7, 32.3), 1.4, 0.9, boxstyle="round,pad=0.06", facecolor=colors_ai[i], edgecolor=WHITE, linewidth=1.2))
        ax.text(ax_, 32.75, step, fontsize=8, fontweight='bold', color=WHITE, ha='center', va='center')
        if i < 3:
            ax.annotate('', xy=(ax_+0.85, 32.75), xytext=(ax_+0.75, 32.75), arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.5))
    else:
        ax.add_patch(FancyBboxPatch((ax_-1.25, 32.25), 2.5, 1.0, boxstyle="round,pad=0.1", facecolor=BLUE, edgecolor=WHITE, linewidth=1.5, alpha=0.18))
        ax.text(ax_, 32.75, '→ "Personal Hearing\nGuardian" (New\nCategory)', fontsize=8.5, fontweight='bold', color=BLUE, ha='center', va='center')

ax.text(12, 31.45, 'Key Difference: Experience-driven → "Better specs" (me-too)  |  AI-native → "New category" (preventive hearing guardian)', fontsize=10, color=DARK, ha='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor=LIGHT, edgecolor=GRAY, lw=0.5))

# ═══════════════════════════════════
# 4. 五大信号
# ═══════════════════════════════════
ax.text(12, 30.6, 'How AI Found the White Space: Five Converging Signals', fontsize=20, fontweight='bold', color=DARK, ha='center')

signals = [
    ('WHO Report', '1B+ youth at risk of hearing loss', '★★★★★', BLUE),
    ('Apple\'s Move', 'AirPods Pro → FDA OTC Hearing Aid', '★★★★★', RED),
    ('Market Data', 'Smart hearing protection $1.26B → $3.25B', '★★★★☆', GREEN),
    ('Social Trend', '#HearingDamage trending on Weibo', '★★★★☆', ORANGE),
    ('User Pain', '72% discomfort from long earbud use', '★★★☆☆', PURPLE),
]
for i, (title, desc, stars, color) in enumerate(signals):
    x = 2.5 + i * 4.2
    ax.add_patch(FancyBboxPatch((x-1.8, 27.8), 3.6, 2.5, boxstyle="round,pad=0.12", facecolor=color, edgecolor=WHITE, linewidth=2, alpha=0.08))
    ax.text(x, 29.8, title, fontsize=12, fontweight='bold', color=color, ha='center')
    ax.text(x, 28.85, desc, fontsize=9, color=DARK, ha='center', va='center', wrap=True)
    ax.text(x, 28.0, stars, fontsize=11, color=color, ha='center')

ax.add_patch(FancyBboxPatch((2, 26.8), 20, 0.7, boxstyle="round,pad=0.1", facecolor=GREEN_L, edgecolor=GREEN, linewidth=2))
ax.text(12, 27.15, '✦  Five independent signals converge → High-confidence opportunity: "Affordable preventive hearing guardian"',
        fontsize=11, fontweight='bold', color=GREEN, ha='center')

# ═══════════════════════════════════
# 5. 竞品矩阵（左侧）
# ═══════════════════════════════════
ax4 = fig.add_axes([0.03, 0.395, 0.45, 0.23])
ax4.set_xlim(50, 340)
ax4.set_ylim(-0.5, 10.5)
comps = [
    (249, 9.5, 'Apple\nAirPods Pro', 600, DARK),
    (199, 3.0, 'Samsung\nBuds3', 350, GRAY),
    (279, 1.5, 'Sony\nWF-1000XM5', 300, GRAY),
    (299, 1.0, 'Bose\nQC Ultra', 280, GRAY),
    (169, 1.0, 'Huawei\nFreeBuds', 250, GRAY),
    (149, 0.5, 'iFLYTEK\nNano+', 180, GRAY),
    (79, 0.0, 'Xiaomi\nAir 2', 180, GRAY),
    (99, 8.0, '★ Guard', 500, BLUE),
    (129, 8.5, '★ Guard Pro', 400, AMBER),
]
for px, py, name, size, color in comps:
    is_guard = 'Guard' in name
    ax4.scatter(px, py, s=size, c=color, alpha=1.0 if is_guard else 0.4,
               edgecolors=BLUE if is_guard else WHITE, linewidth=2.5 if is_guard else 1, zorder=10 if is_guard else 2)
    off = -16 if is_guard else 13
    ax4.annotate(name, (px, py), textcoords="offset points", xytext=(0, off),
                ha='center', fontsize=7, fontweight='bold' if is_guard else 'normal',
                color=BLUE if is_guard else GRAY)

ws_rect = Rectangle((75, 4.5), 85, 5.5, facecolor=BLUE, alpha=0.06, edgecolor=BLUE, linestyle='--', linewidth=1.5, zorder=0)
ax4.add_patch(ws_rect)
ax4.text(117, 9.3, 'WHITE SPACE\n$99-129 Hearing Health\n→ Zero Competition', ha='center', fontsize=9, fontweight='bold', color=BLUE)
ax4.text(270, 10, 'Medical-grade\n$249+ iOS only', fontsize=7, color=GRAY, ha='center')
ax4.text(120, 1, 'No hearing features\nPrice war zone', fontsize=7, color=GRAY, ha='center')
ax4.set_xlabel('Retail Price (USD)', fontsize=11, fontweight='bold', color=DARK)
ax4.set_ylabel('Hearing Health Capability →', fontsize=11, fontweight='bold', color=DARK)
ax4.set_title('Competitive Landscape: Where is the White Space?', fontsize=14, fontweight='bold', color=DARK, pad=10)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.grid(True, alpha=0.1, linestyle='--')
ax4.tick_params(labelsize=8)

# ═══════════════════════════════════
# 6. 用户洞察（右侧）—— 单列布局，避免拥挤
# ═══════════════════════════════════
ax5 = fig.add_axes([0.51, 0.395, 0.46, 0.23])
ax5.set_xlim(0, 10)
ax5.set_ylim(0, 10)
ax5.axis('off')
ax5.set_title('User Insights from AI-Simulated 500 Respondents', fontsize=14, fontweight='bold', color=DARK, pad=10)

# 购买意愿 - 单列显示
ax5.text(0.5, 9.2, '1. Purchase Intent by Price (Sweet Spot: $99)', fontsize=11, fontweight='bold', color=DARK)
prices = ['$79', '$99', '$129', '$179']
intent_all = [68, 54, 38, 18]
intent_hc = [82, 76, 63, 35]
bar_x = [1.5, 3.3, 5.1, 6.9]
bar_w = 0.55
for i, (px, o, h) in enumerate(zip(bar_x, intent_all, intent_hc)):
    ax5.add_patch(FancyBboxPatch((px-bar_w/2, 6.8), bar_w, o/12, boxstyle="round,pad=0.02", facecolor=BLUE, edgecolor=WHITE, linewidth=0.5, alpha=0.9))
    ax5.add_patch(FancyBboxPatch((px+bar_w/2+0.05, 6.8), bar_w, h/12, boxstyle="round,pad=0.02", facecolor=AMBER, edgecolor=WHITE, linewidth=0.5, alpha=0.9))
    ax5.text(px, 6.7, prices[i], fontsize=10, fontweight='bold', color=DARK, ha='center')
    ax5.text(px, 6.8+o/12+0.15, f'{o}%', fontsize=8.5, fontweight='bold', color=BLUE, ha='center')
    ax5.text(px+bar_w/2+0.05, 6.8+h/12+0.15, f'{h}%', fontsize=8.5, fontweight='bold', color=AMBER, ha='center')
ax5.text(8.5, 8.7, '■ Overall', fontsize=8, color=BLUE)
ax5.text(8.5, 8.2, '■ Hearing-Concerned', fontsize=8, color=AMBER)
ax5.annotate('Sweet Spot\n$99', xy=(3.3, 6.8+54/12), xytext=(1.5, 8.5), fontsize=9, fontweight='bold', color=GREEN, ha='center',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

# NPS 横向柱状图
ax5.text(0.5, 6.2, '2. NPS by User Segment', fontsize=11, fontweight='bold', color=DARK)
segments = ['Elderly children', 'Hearing-concerned', 'Commuter', 'Gamer', 'Student', 'Privacy-sensitive']
nps_vals = [72, 68, 51, 35, 28, 15]
nps_colors = [GREEN if v >= 50 else AMBER if v >= 30 else ORANGE for v in nps_vals]
for i, (seg, val, nc) in enumerate(zip(segments, nps_vals, nps_colors)):
    y = 5.6 - i * 0.75
    ax5.add_patch(FancyBboxPatch((0.5, y-0.22), val/8, 0.45, boxstyle="round,pad=0.04", facecolor=nc, edgecolor=WHITE, linewidth=0.8, alpha=0.9))
    ax5.text(val/8 + 0.55, y, f'+{val}', fontsize=8.5, fontweight='bold', color=DARK, va='center')
    ax5.text(0.5, y-0.35, seg, fontsize=8, color=GRAY, va='center')
ax5.axvline(x=42/8, ymin=0.1, ymax=0.55, color=BLUE, linestyle='--', linewidth=1, alpha=0.6)
ax5.text(5.5, 5.6, 'Overall\nNPS +42', fontsize=8, color=BLUE, fontweight='bold')

# 功能优先级 - 只在右侧放一列，避免双列拥挤
ax5.text(6.2, 6.2, '3. Feature Priority', fontsize=11, fontweight='bold', color=DARK)
feats = ['Real-time SPL Monitor', 'Hearing Profile + EQ', 'Context ANC', 'Trend Report', 'Remote Family Setup', 'AI Translate']
feat_vals = [32.4, 24.7, 18.3, 13.1, 7.2, 4.3]
feat_colors = [BLUE, SKY, GREEN, AMBER, PURPLE, GRAY]
for i, (f, v, fc) in enumerate(zip(feats, feat_vals, feat_colors)):
    y = 5.6 - i * 0.75
    ax5.add_patch(FancyBboxPatch((6.2, y-0.22), v/4.2, 0.45, boxstyle="round,pad=0.04", facecolor=fc, edgecolor=WHITE, linewidth=0.8, alpha=0.9))
    ax5.text(6.2 + v/4.2 + 0.15, y, f'{v}%', fontsize=8.5, fontweight='bold', color=DARK, va='center')
    ax5.text(6.2, y-0.35, f, fontsize=7.5, color=GRAY, va='center')

# ═══════════════════════════════════
# 7. 技术架构（左侧）
# ═══════════════════════════════════
ax6 = fig.add_axes([0.03, 0.07, 0.45, 0.31])
ax6.set_xlim(0, 12)
ax6.set_ylim(0, 10)
ax6.axis('off')
ax6.set_title('Technical Architecture: Built on Soundcore\'s Thus™ AI Chip', fontsize=14, fontweight='bold', color=DARK, pad=10)

sensors = [('Dual MEMS Mics\n(Ambient + In-ear)', BLUE, 2.5), ('Bone Conduction\nSensors ×2', SKY, 6.0), ('IR In-ear\nDetection', GREEN, 9.5)]
for label, color, x in sensors:
    ax6.add_patch(FancyBboxPatch((x-1.2, 8.6), 2.4, 1.0, boxstyle="round,pad=0.08", facecolor=color, edgecolor=WHITE, linewidth=1.5, alpha=0.9))
    ax6.text(x, 9.1, label, ha='center', va='center', fontsize=8, fontweight='bold', color=WHITE)
    ax6.annotate('', xy=(x, 8.45), xytext=(x, 8.55), arrowprops=dict(arrowstyle='->', color=DARK, lw=1.2))

ax6.text(6, 8.5, '10-Sensor Fusion', fontsize=7.5, color=GRAY, ha='center', style='italic')
ax6.add_patch(FancyBboxPatch((1.0, 6.2), 10, 1.6, boxstyle="round,pad=0.12", facecolor='#1E293B', edgecolor=BLUE, linewidth=2))
ax6.text(6, 7.4, 'Low-Power DSP Co-processor', fontsize=12, fontweight='bold', color=WHITE, ha='center')
ax6.text(6, 6.7, 'Always-on SPL Estimation (<0.5mA)  |  Noise Classification  |  Alert Logic  |  A-Weighting', fontsize=8, color='#93C5FD', ha='center')
ax6.annotate('', xy=(6, 6.05), xytext=(6, 6.15), arrowprops=dict(arrowstyle='->', color=DARK, lw=1.5))

ax6.add_patch(FancyBboxPatch((1.0, 2.8), 10, 2.9, boxstyle="round,pad=0.12", facecolor=BLUE, edgecolor=WHITE, linewidth=2.5))
ax6.text(6, 5.15, 'Thus™ AI Chip (CIM Architecture)', fontsize=13, fontweight='bold', color=WHITE, ha='center')
ax6.text(6, 4.4, 'Dynamic EQ (DNN)  |  Context ANC 4.0  |  Hearing Profile Engine  |  Bluetooth 6.1', fontsize=8, color='#BFDBFE', ha='center')
ax6.text(6, 3.85, '10-Sensor Fusion  |  On-Device Privacy — No Audio Uploaded', fontsize=8, color='#BFDBFE', ha='center')
ax6.annotate('', xy=(6, 2.65), xytext=(6, 2.75), arrowprops=dict(arrowstyle='->', color=DARK, lw=1.5))

outs = [('Real-time\nHearing Protection', GREEN, 2.5), ('Personalized\nAudio Profile', AMBER, 6.0), ('Context\nAwareness', PURPLE, 9.5)]
for label, color, x in outs:
    ax6.add_patch(FancyBboxPatch((x-1.2, 1.3), 2.4, 0.95, boxstyle="round,pad=0.06", facecolor=color, edgecolor=WHITE, linewidth=1.5, alpha=0.9))
    ax6.text(x, 1.77, label, ha='center', va='center', fontsize=8, fontweight='bold', color=WHITE)

# ═══════════════════════════════════
# 8. 商业模式（右侧）
# ═══════════════════════════════════
ax7 = fig.add_axes([0.51, 0.07, 0.46, 0.31])
ax7.set_xlim(0, 10)
ax7.set_ylim(0, 10)
ax7.axis('off')
ax7.set_title('Business Model: Hardware + Subscription + Data Flywheel', fontsize=14, fontweight='bold', color=DARK, pad=10)

ax7.text(5, 9.2, '3-Year Revenue Forecast (Base Case)', fontsize=11, fontweight='bold', color=DARK, ha='center')
years = ['Year 1', 'Year 2', 'Year 3']
hw = [55, 88, 132]
sub = [1.9, 5.5, 11.5]
for i, (yr, h, s) in enumerate(zip(years, hw, sub)):
    x = 1.6 + i * 2.8
    ax7.add_patch(FancyBboxPatch((x-0.8, 5.5), 1.6, h/15, boxstyle="round,pad=0.04", facecolor=BLUE, edgecolor=WHITE, linewidth=0.8, alpha=0.9))
    ax7.add_patch(FancyBboxPatch((x-0.8, 5.5+h/15), 1.6, s/15, boxstyle="round,pad=0.04", facecolor=AMBER, edgecolor=WHITE, linewidth=0.8, alpha=0.9))
    ax7.text(x, 5.5+(h+s)/15+0.2, f'${h+s:.0f}M', fontsize=9, fontweight='bold', color=DARK, ha='center')
    ax7.text(x, 5.2, yr, fontsize=10, fontweight='bold', color=DARK, ha='center')
ax7.text(8.5, 8.7, '■ Hardware', fontsize=8, color=BLUE)
ax7.text(8.5, 8.2, '■ Subscription', fontsize=8, color=AMBER)

ax7.text(5, 4.8, 'Unit Economics', fontsize=11, fontweight='bold', color=DARK, ha='center')
kpis = [('CAC', '$14', BLUE), ('HW Margin\n(Pro)', '27%', SKY), ('Sub ARPU\n/yr', '$36', AMBER), ('3-Year\nLTV', '$146', GREEN), ('LTV / CAC', '10.4×', PURPLE)]
for i, (label, val, color) in enumerate(kpis):
    x = 1.0 + i * 1.8
    ax7.add_patch(FancyBboxPatch((x-0.75, 3.2), 1.5, 1.2, boxstyle="round,pad=0.08", facecolor=color, edgecolor=WHITE, linewidth=1.5, alpha=0.1))
    ax7.text(x, 3.85, val, fontsize=15, fontweight='bold', color=color, ha='center')
    ax7.text(x, 3.35, label, fontsize=7, color=DARK, ha='center')

ax7.text(5, 2.7, 'The Moat: Data Flywheel', fontsize=11, fontweight='bold', color=DARK, ha='center')
fw_items = ['Users wear\nGuard daily', 'Hearing profile\ngets more accurate', 'Switching\ncost rises', 'Users stay\n& recommend']
fw_colors = [BLUE, SKY, GREEN, AMBER]
for i, (item, fc) in enumerate(zip(fw_items, fw_colors)):
    x = 1.2 + i * 2.2
    ax7.add_patch(FancyBboxPatch((x-0.95, 0.8), 1.9, 1.5, boxstyle="round,pad=0.1", facecolor=fc, edgecolor=WHITE, linewidth=1.5, alpha=0.85))
    ax7.text(x, 1.55, item, ha='center', va='center', fontsize=8, fontweight='bold', color=WHITE)
    if i < 3:
        ax7.annotate('', xy=(x+1.05, 1.55), xytext=(x+0.95, 1.55), arrowprops=dict(arrowstyle='->', color=DARK, lw=1.5))
ax7.text(0.9, 1.8, '↻', fontsize=24, color=GRAY, ha='center')

# ═══════════════════════════════════
# 9. 底部信息条
# ═══════════════════════════════════
ax.add_patch(FancyBboxPatch((0.5, 0.2), 23, 0.55, boxstyle="round,pad=0.06", facecolor=WHITE, edgecolor='#E5E7EB', linewidth=1))
ax.text(12, 0.47, 'Soundcore Guard — AI-Native Product Design Experiment  |  Method: Expand → Challenge → Converge  |  All data anchored to public sources  |  Hearing wellness — not a medical device',
        fontsize=8, color=GRAY, ha='center')

# 保存
output_path = f'{OUT}/soundcore-guard-poster.png'
fig.savefig(output_path, facecolor=LIGHT, dpi=200)
plt.close()
size_kb = os.path.getsize(output_path) / 1024
print(f'✅ 最终数据海报已生成')
print(f'   路径: {output_path}')
print(f'   大小: {size_kb:.0f} KB')
