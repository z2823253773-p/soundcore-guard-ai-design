#!/usr/bin/env python3
"""Soundcore Guard — 信息画报生成器（单张完整画报）"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from matplotlib.patches import FancyBboxPatch
import os, warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'axes.unicode_minus': False,
    'figure.dpi': 200,
    'savefig.dpi': 200,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
})

OUT = os.path.dirname(os.path.abspath(__file__))

# ── 品牌色板 ──
C = {
    'primary': '#1A56DB', 'secondary': '#0EA5E9', 'accent': '#F59E0B',
    'success': '#10B981', 'danger': '#EF4444', 'warning': '#F97316',
    'purple': '#8B5CF6', 'dark': '#111827', 'gray': '#6B7280',
    'light': '#F3F4F6', 'white': '#FFFFFF', 'sky': '#38BDF8',
    'teal': '#14B8A6', 'pink': '#EC4899', 'indigo': '#6366F1',
}

# ── 画报主函数 ──
def create_infographic():
    fig = plt.figure(figsize=(24, 36), facecolor='white')
    
    # === 顶部标题栏 ===
    ax_title = fig.add_axes([0.02, 0.955, 0.96, 0.04])
    ax_title.axis('off')
    ax_title.set_xlim(0, 24)
    ax_title.set_ylim(0, 1)
    
    # 背景条
    title_bg = FancyBboxPatch((0, 0), 24, 1, boxstyle="round,pad=0.02",
                               facecolor=C['dark'], edgecolor='none', transform=ax_title.transData)
    ax_title.add_patch(title_bg)
    ax_title.text(12, 0.68, 'Soundcore Guard', fontsize=28, fontweight='bold', color='white', ha='center', va='center')
    ax_title.text(12, 0.28, 'AI-Native Product Design  |  Anker Soundcore Hearing Guardian TWS Earbuds', 
                  fontsize=11, color='#93C5FD', ha='center', va='center')
    
    # === 行 1：方法论 + 机会信号（左侧2/3 + 右侧1/3）===
    
    # 1A. 方法论对比 (左2/3)
    ax1 = fig.add_axes([0.02, 0.82, 0.63, 0.125])
    ax1.set_xlim(0, 15)
    ax1.set_ylim(0, 3.5)
    ax1.axis('off')
    
    # 传统
    trad_box = FancyBboxPatch((0.1, 0.1), 6.8, 3.2, boxstyle="round,pad=0.15",
                               facecolor='#FEF2F2', edgecolor=C['danger'], linewidth=1.5)
    ax1.add_patch(trad_box)
    ax1.text(3.5, 3.0, 'Traditional: Experience-Driven', fontsize=10, fontweight='bold', color=C['danger'], ha='center')
    
    steps_t = ['PM\nExperience', 'Small\nSurvey', 'Manual\nTracking', 'Boss\nDecides']
    for i, s in enumerate(steps_t):
        x = 0.8 + i * 1.5
        box = FancyBboxPatch((x-0.55, 1.1), 1.1, 1.1, boxstyle="round,pad=0.08",
                              facecolor=C['danger'], edgecolor='white', linewidth=1.5, alpha=0.85)
        ax1.add_patch(box)
        ax1.text(x, 1.65, s, ha='center', va='center', fontsize=7.5, fontweight='bold', color='white')
        if i < 3:
            ax1.annotate('', xy=(x+0.6, 1.65), xytext=(x+0.7, 1.65),
                        arrowprops=dict(arrowstyle='->', color=C['danger'], lw=1.5))
    
    ax1.text(3.5, 0.5, 'Ceiling = PM capability  |  Black-box decisions', fontsize=7.5, color=C['danger'], ha='center', style='italic')
    
    # AI原生
    ai_box = FancyBboxPatch((8.1, 0.1), 6.8, 3.2, boxstyle="round,pad=0.15",
                             facecolor='#EFF6FF', edgecolor=C['primary'], linewidth=1.5)
    ax1.add_patch(ai_box)
    ax1.text(11.5, 3.0, 'AI-Native: Expand → Challenge → Converge', fontsize=10, fontweight='bold', color=C['primary'], ha='center')
    
    steps_ai = ['AI Brain\nTrust', 'AI User\nAvatars', 'AI Expert\nPanel', 'PM\nVerdict']
    colors_ai = [C['primary'], C['secondary'], C['teal'], C['success']]
    for i, (s, c) in enumerate(zip(steps_ai, colors_ai)):
        x = 9.1 + i * 1.5
        box = FancyBboxPatch((x-0.55, 1.1), 1.1, 1.1, boxstyle="round,pad=0.08",
                              facecolor=c, edgecolor='white', linewidth=1.5, alpha=0.9)
        ax1.add_patch(box)
        ax1.text(x, 1.65, s, ha='center', va='center', fontsize=7, fontweight='bold', color='white')
        if i < 3:
            ax1.annotate('', xy=(x+0.6, 1.65), xytext=(x+0.7, 1.65),
                        arrowprops=dict(arrowstyle='->', color=C['primary'], lw=1.5))
    
    ax1.text(11.5, 0.5, 'PM = Director  |  Traceable reasoning  |  Method changes outcome', 
             fontsize=7.5, color=C['primary'], ha='center', style='italic')
    
    # 1B. 机会信号 (右1/3)
    ax2 = fig.add_axes([0.67, 0.82, 0.31, 0.125])
    ax2.set_xlim(0, 6)
    ax2.set_ylim(0, 6)
    ax2.axis('off')
    
    signals = ['WHO: 1B+ Youth\nHearing Risk', 'Apple: FDA OTC\nHearing Aid', 
               'Market: $1.26B\n→ $3.25B', '#Hearing Damage\nTrending', '72% Users\nDiscomfort']
    strengths = [5, 5, 4, 4, 3]
    s_colors = [C['primary'], C['danger'], C['success'], C['warning'], C['purple']]
    
    for i, (sig, val, sc) in enumerate(zip(signals, strengths, s_colors)):
        y = 5.2 - i * 1.05
        bar = FancyBboxPatch((0.2, y-0.3), val*0.7, 0.6, boxstyle="round,pad=0.05",
                              facecolor=sc, edgecolor='white', linewidth=1, alpha=0.85)
        ax2.add_patch(bar)
        ax2.text(0.3 + val*0.35, y, sig, ha='left', va='center', fontsize=7, color=C['dark'])
        ax2.text(val*0.7 + 0.4, y, '★'*val, fontsize=8, color=sc)
    
    ax2.text(3, 0.1, '5 Independent Signals → High-Confidence White Space', 
             fontsize=8, fontweight='bold', color=C['success'], ha='center',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='#D1FAE5', edgecolor=C['success'], lw=1))
    
    # === 行 2：竞品矩阵 ===
    ax3 = fig.add_axes([0.02, 0.665, 0.47, 0.145])
    ax3.set_xlim(50, 330)
    ax3.set_ylim(-0.5, 10.5)
    
    competitors = [
        (249, 9.5, 'Apple\nAirPods Pro', 700, C['dark']),
        (199, 3.0, 'Samsung\nBuds3', 400, C['gray']),
        (279, 1.5, 'Sony\nXM5', 350, C['gray']),
        (299, 1.0, 'Bose\nQC Ultra', 300, C['gray']),
        (169, 1.0, 'Huawei\nFreeBuds', 250, C['gray']),
        (149, 0.5, 'iFLYTEK\nNano+', 180, C['gray']),
        (79, 0.0, 'Xiaomi', 200, C['gray']),
        (99, 8.0, '★ Guard', 550, C['primary']),
        (129, 8.5, '★ Guard Pro', 450, C['accent']),
    ]
    
    for px, py, name, size, color in competitors:
        is_guard = 'Guard' in name
        ax3.scatter(px, py, s=size, c=color, alpha=1.0 if is_guard else 0.5,
                   edgecolors=C['primary'] if is_guard else 'white', linewidth=2.5 if is_guard else 1, zorder=5 if is_guard else 2)
        off = -18 if is_guard else 14
        ax3.annotate(name, (px, py), textcoords="offset points", xytext=(0, off),
                    ha='center', fontsize=7, fontweight='bold' if is_guard else 'normal',
                    color=C['primary'] if is_guard else C['gray'])
    
    # White space
    rect = plt.Rectangle((75, 4.5), 80, 5, facecolor=C['primary'], alpha=0.08, edgecolor=C['primary'], 
                          linestyle='--', linewidth=1.5, zorder=0)
    ax3.add_patch(rect)
    ax3.text(115, 9.0, 'WHITE SPACE\nHearing Health\nat Mass Price', ha='center', fontsize=9,
            fontweight='bold', color=C['primary'])
    
    ax3.set_xlabel('Price (USD)', fontsize=9, fontweight='bold', color=C['dark'])
    ax3.set_ylabel('Hearing Health Depth', fontsize=9, fontweight='bold', color=C['dark'])
    ax3.set_title('Competitive Positioning: Hearing Health × Price', fontsize=11, fontweight='bold', pad=8)
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.grid(True, alpha=0.15, linestyle='--')
    ax3.tick_params(labelsize=7)
    
    # === 行 2 右：用户洞察 ===
    # 2A: 购买意愿
    ax4 = fig.add_axes([0.52, 0.72, 0.22, 0.09])
    prices = ['$79', '$99', '$129', '$179']
    overall = [68, 54, 38, 18]
    high_concern = [82, 76, 63, 35]
    x = np.arange(len(prices))
    w = 0.3
    ax4.bar(x - w/2, overall, w, label='Overall', color=C['primary'], edgecolor='white', linewidth=0.8)
    ax4.bar(x + w/2, high_concern, w, label='Hearing-Concerned', color=C['accent'], edgecolor='white', linewidth=0.8)
    for i, (o, h) in enumerate(zip(overall, high_concern)):
        ax4.text(i - w/2, o + 1, f'{o}%', ha='center', fontsize=6.5, fontweight='bold', color=C['primary'])
        ax4.text(i + w/2, h + 1, f'{h}%', ha='center', fontsize=6.5, fontweight='bold', color=C['accent'])
    ax4.set_xticks(x)
    ax4.set_xticklabels(prices, fontsize=8, fontweight='bold')
    ax4.set_title('Purchase Intent by Price', fontsize=9, fontweight='bold')
    ax4.legend(fontsize=6.5, loc='upper right')
    ax4.set_ylim(0, 95)
    ax4.spines['top'].set_visible(False); ax4.spines['right'].set_visible(False)
    ax4.tick_params(labelsize=7)
    ax4.annotate('Sweet Spot', xy=(1, 54), xytext=(0.5, 78), fontsize=7, ha='center', color=C['success'],
                fontweight='bold', arrowprops=dict(arrowstyle='->', color=C['success'], lw=1.2))
    
    # 2B: NPS
    ax5 = fig.add_axes([0.76, 0.72, 0.22, 0.09])
    segments = ['Elderly\nChildren', 'Hearing\nConcerned', 'Commuter', 'Gamer', 'Student', 'Privacy\nSensitive']
    nps_vals = [72, 68, 51, 35, 28, 15]
    nps_colors = [C['success'] if v >= 50 else C['accent'] if v >= 30 else C['warning'] for v in nps_vals]
    bars = ax5.barh(segments, nps_vals, color=nps_colors, edgecolor='white', linewidth=0.8, height=0.55)
    for bar, val in zip(bars, nps_vals):
        ax5.text(val + 1.5, bar.get_y() + bar.get_height()/2, f'+{val}', va='center', fontsize=7, fontweight='bold')
    ax5.axvline(x=42, color=C['primary'], linestyle='--', linewidth=1, alpha=0.7)
    ax5.text(44, 5.3, 'Avg +42', fontsize=7, color=C['primary'], fontweight='bold')
    ax5.set_title('NPS by User Segment', fontsize=9, fontweight='bold')
    ax5.spines['top'].set_visible(False); ax5.spines['right'].set_visible(False)
    ax5.set_xlim(0, 85)
    ax5.tick_params(labelsize=6.5)
    
    # 2C: 功能优先级 (小饼图)
    ax6 = fig.add_axes([0.52, 0.665, 0.22, 0.05])
    features = ['SPL Monitor', 'Hearing Profile', 'Context ANC', 'Trend Report', 'Remote Setup', 'AI Translate']
    importance = [32.4, 24.7, 18.3, 13.1, 7.2, 4.3]
    feat_colors = [C['primary'], C['secondary'], C['teal'], C['accent'], C['purple'], C['gray']]
    wedges, texts, autotexts = ax6.pie(importance, autopct='%1.1f%%', colors=feat_colors, startangle=90,
                                        pctdistance=0.78, explode=(0.05, 0.03, 0, 0, 0, 0))
    for t in autotexts: t.set_fontsize(5.5); t.set_fontweight('bold')
    ax6.set_title('Feature Priority', fontsize=8, fontweight='bold')
    
    # === 行 3：商业模式 ===
    # 3A: 收入预测
    ax7 = fig.add_axes([0.02, 0.515, 0.3, 0.14])
    years = ['Year 1', 'Year 2', 'Year 3']
    hardware = [55, 88, 132]
    subscription = [1.9, 5.5, 11.5]
    x = np.arange(len(years))
    ax7.bar(x, hardware, 0.5, label='Hardware', color=C['primary'], edgecolor='white', linewidth=1)
    ax7.bar(x, subscription, 0.5, bottom=hardware, label='Subscription', color=C['accent'], edgecolor='white', linewidth=1)
    totals = [h+s for h,s in zip(hardware, subscription)]
    for i, t in enumerate(totals):
        ax7.text(i, t+3, f'${t:.0f}M', ha='center', fontsize=9, fontweight='bold')
    ax7.set_xticks(x); ax7.set_xticklabels(years, fontsize=9, fontweight='bold')
    ax7.set_title('3-Year Revenue Forecast', fontsize=10, fontweight='bold')
    ax7.legend(fontsize=7, loc='upper left')
    ax7.set_ylim(0, 160)
    ax7.spines['top'].set_visible(False); ax7.spines['right'].set_visible(False)
    ax7.grid(axis='y', alpha=0.15)
    ax7.tick_params(labelsize=7)
    
    # 3B: Unit Economics
    ax8 = fig.add_axes([0.35, 0.515, 0.3, 0.14])
    metrics = ['CAC', 'HW Margin\n(Pro)', 'Sub ARPU\n/yr', 'LTV\n(3yr)', 'LTV/CAC']
    values = [14, 27, 36, 146, 10.4]
    bar_colors = [C['secondary'], C['primary'], C['accent'], C['success'], C['purple']]
    bars = ax8.bar(metrics, values, color=bar_colors, edgecolor='white', linewidth=1, width=0.55)
    labels_v = ['$14', '27%', '$36', '$146', '10.4×']
    for bar, label in zip(bars, labels_v):
        ax8.text(bar.get_x()+bar.get_width()/2, bar.get_height()+2, label, ha='center', fontsize=9, fontweight='bold')
    ax8.axhline(y=42, color=C['gray'], linestyle='--', alpha=0.4, linewidth=1)
    ax8.text(4.3, 44, 'Healthy >3×', fontsize=7, color=C['gray'], ha='right')
    ax8.set_title('Unit Economics', fontsize=10, fontweight='bold')
    ax8.spines['top'].set_visible(False); ax8.spines['right'].set_visible(False)
    ax8.set_ylim(0, 170)
    ax8.grid(axis='y', alpha=0.15)
    ax8.tick_params(labelsize=7)
    
    # 3C: BOM瀑布
    ax9 = fig.add_axes([0.68, 0.515, 0.3, 0.14])
    components = ['Chip', 'Mics', 'Bone', 'Bat', 'Case', 'Driver', 'PCB', 'Asm', 'Algo', 'Mktg', 'Chan']
    costs = [9, 3.5, 2.5, 1.8, 6, 3.5, 2.5, 5, 1.5, 17.5, 27.5]
    cum = np.cumsum(costs)
    c_colors = [C['primary']]*9 + [C['warning'], C['secondary']]
    prev = 0
    for i, (comp, cost, cc) in enumerate(zip(components, costs, c_colors)):
        ax9.bar(i, cost, bottom=prev, color=cc, edgecolor='white', linewidth=0.5, width=0.6)
        prev += cost
    total = sum(costs)
    ax9.axhline(y=99, color=C['success'], linestyle='--', linewidth=1.5)
    ax9.text(10, 101, 'Retail $99', fontsize=7, color=C['success'], fontweight='bold')
    ax9.text(5, 75, f'Margin {(99-total)/99*100:.0f}%', fontsize=7, fontweight='bold', color=C['success'])
    ax9.set_xticks([])
    ax9.set_title('BOM Structure → Retail $99', fontsize=10, fontweight='bold')
    ax9.spines['top'].set_visible(False); ax9.spines['right'].set_visible(False)
    ax9.set_ylim(0, 115)
    ax9.tick_params(labelsize=7)
    
    # === 行 4：技术架构 ===
    ax10 = fig.add_axes([0.02, 0.28, 0.47, 0.225])
    ax10.set_xlim(0, 14); ax10.set_ylim(0, 10)
    ax10.axis('off')
    ax10.set_title('Technical Architecture', fontsize=12, fontweight='bold', color=C['dark'], pad=10)
    
    # Sensors
    sensors = [(2, 9, 'Dual MEMS Mics\n(Ambient+In-ear)', C['primary']),
               (5.5, 9, 'Bone Conduction\nSensors ×2', C['secondary']),
               (9, 9, 'IR In-ear\nDetection', C['teal'])]
    for x, y, label, color in sensors:
        box = FancyBboxPatch((x-1.2, y-0.5), 2.4, 1.0, boxstyle="round,pad=0.1",
                              facecolor=color, edgecolor='white', linewidth=1.5, alpha=0.9)
        ax10.add_patch(box)
        ax10.text(x, y, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color='white')
        ax10.annotate('', xy=(x, 8.0), xytext=(x, 8.3), arrowprops=dict(arrowstyle='->', color=C['dark'], lw=1.5))
    
    ax10.text(7, 8.2, '10-Sensor Fusion Data Stream', ha='center', fontsize=7, color=C['gray'], style='italic')
    
    # DSP Layer
    dsp = FancyBboxPatch((1.5, 6.3), 11, 1.5, boxstyle="round,pad=0.15",
                          facecolor='#1E293B', edgecolor=C['primary'], linewidth=2, alpha=0.95)
    ax10.add_patch(dsp)
    ax10.text(7, 7.4, 'Low-Power DSP Co-processor (always-on, <0.5mA)', ha='center', fontsize=11, fontweight='bold', color='white')
    ax10.text(7, 6.7, 'SPL Estimation  |  Noise Classification  |  Threshold Alert  |  A-Weighting Filter', ha='center', fontsize=7.5, color='#93C5FD')
    ax10.annotate('', xy=(7, 6.1), xytext=(7, 6.2), arrowprops=dict(arrowstyle='->', color=C['dark'], lw=2))
    
    # Thus™ Layer
    thus = FancyBboxPatch((1.5, 3.3), 11, 2.4, boxstyle="round,pad=0.15",
                           facecolor=C['primary'], edgecolor='white', linewidth=2.5, alpha=0.95)
    ax10.add_patch(thus)
    ax10.text(7, 5.1, 'Thus™ AI Chip Platform (CIM Architecture)', ha='center', fontsize=12, fontweight='bold', color='white')
    ax10.text(7, 4.4, 'Dynamic EQ Compensation (DNN)  |  Context ANC 4.0  |  Hearing Profile Engine', ha='center', fontsize=7.5, color='#BFDBFE')
    ax10.text(7, 3.8, 'Bluetooth 6.1  |  LE Audio / LC3  |  3-Device Multipoint  |  On-Device Privacy', ha='center', fontsize=7.5, color='#BFDBFE')
    ax10.annotate('', xy=(7, 3.1), xytext=(7, 3.2), arrowprops=dict(arrowstyle='->', color=C['dark'], lw=2))
    
    # Outputs
    outs = [(2.5, 2.0, 'Hearing\nProtection', C['success']),
            (7, 2.0, 'Personalized\nAudio', C['accent']),
            (11.5, 2.0, 'Context\nAwareness', C['purple'])]
    for x, y, label, color in outs:
        box = FancyBboxPatch((x-1.2, y-0.45), 2.4, 0.9, boxstyle="round,pad=0.08",
                              facecolor=color, edgecolor='white', linewidth=1.5, alpha=0.9)
        ax10.add_patch(box)
        ax10.text(x, y, label, ha='center', va='center', fontsize=8, fontweight='bold', color='white')
    
    # Privacy badge
    ax10.text(13.5, 2.0, '🔒 Local Only', fontsize=6.5, color=C['success'], fontweight='bold', ha='center',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='#D1FAE5', edgecolor=C['success'], lw=1))
    
    # === 行 4 右：对比表 ===
    ax11 = fig.add_axes([0.52, 0.28, 0.46, 0.225])
    ax11.set_xlim(0, 12); ax11.set_ylim(0, 7)
    ax11.axis('off')
    ax11.set_title('Same Brief, Different Outcomes', fontsize=12, fontweight='bold', color=C['dark'], pad=8)
    
    # Headers
    for j, (hdr, hc, x, w) in enumerate([
        ('Dimension', C['dark'], 0.2, 2.4),
        ('Traditional → Soundcore Pro', C['danger'], 2.8, 4.2),
        ('AI-Native → Soundcore Guard', C['primary'], 7.2, 4.6),
    ]):
        box = FancyBboxPatch((x, 5.7), w, 0.6, boxstyle="round,pad=0.05",
                              facecolor=hc, edgecolor='white', linewidth=1, alpha=0.9)
        ax11.add_patch(box)
        ax11.text(x+w/2, 6.0, hdr, ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')
    
    rows = [
        ('Value Prop', 'Better ANC + AI Translate', 'Personal Hearing Guardian'),
        ('Differentiation', 'Parameter upgrade (me-too)', 'Category innovation'),
        ('Price', '$149–179', '$99–129'),
        ('Business Model', 'One-time hardware', 'Hardware + Subscription + Data'),
        ('Key Insight', 'PM experience + 50 surveys', 'WHO data + 500 AI avatars'),
        ('Moat', 'Specs (catchable)', 'Hearing data flywheel (defensible)'),
    ]
    
    for i, (dim, trad, ai_n) in enumerate(rows):
        y = 5.35 - i * 0.78
        bg = '#F9FAFB' if i % 2 == 0 else 'white'
        for j, (cell, x, w, color) in enumerate([
            (dim, 0.2, 2.4, C['dark']),
            (trad, 2.8, 4.2, C['danger']),
            (ai_n, 7.2, 4.6, C['primary']),
        ]):
            box = FancyBboxPatch((x, y-0.3), w, 0.6, boxstyle="round,pad=0.03",
                                  facecolor=bg, edgecolor='#E5E7EB', linewidth=0.5)
            ax11.add_patch(box)
            fw = 'bold' if j == 0 else 'normal'
            ax11.text(x+w/2, y, cell, ha='center', va='center', fontsize=7.5, fontweight=fw, color=color)
    
    # Verdict
    v_box = FancyBboxPatch((0.2, 0.2), 11.6, 0.55, boxstyle="round,pad=0.08",
                            facecolor=C['primary'], edgecolor=C['primary'], linewidth=1, alpha=0.1)
    ax11.add_patch(v_box)
    ax11.text(6, 0.47, 'Verdict: Method changes outcome. AI-native found a category-defining white space experience-driven missed.',
             ha='center', fontsize=8, fontweight='bold', color=C['primary'])
    
    # === 行 5：路线图 + 数据飞轮 + 风险 ===
    # 5A: 路线图
    ax12 = fig.add_axes([0.02, 0.08, 0.55, 0.19])
    ax12.set_xlim(0, 14); ax12.set_ylim(0, 6)
    ax12.axis('off')
    ax12.set_title('Product Roadmap', fontsize=12, fontweight='bold', color=C['dark'], pad=8)
    
    phases = [
        ('2026 Q4\nFoundation', ['Tech Validation', 'Supply Chain', 'Thus™ Adapt'], C['indigo'], 7.5),
        ('2027 Q1-2\nDevelopment', ['SPL Algorithm', 'App Dev', 'Beta Test'], C['primary'], 5.5),
        ('2027 Q3-4\nMVP Launch', ['Guard $99', 'Guard Pro $129', 'Hearing Profile'], C['success'], 3.5),
        ('2028\nScale V2/V3', ['Dynamic EQ', 'Annual Report', 'Elder Mode', 'Enterprise'], C['accent'], 1.5),
    ]
    
    for title, items, color, y in phases:
        box = FancyBboxPatch((0.1, y-0.6), 2.2, 1.6, boxstyle="round,pad=0.1",
                              facecolor=color, edgecolor='white', linewidth=1.5, alpha=0.9)
        ax12.add_patch(box)
        ax12.text(1.2, y+0.4, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')
        ax12.barh(y, 11.5, 0.04, left=2.5, color=color, alpha=0.2)
        for j, item in enumerate(items):
            ix = 3.0 + j * 2.5
            ibox = FancyBboxPatch((ix-1.0, y-0.35), 2.0, 0.7, boxstyle="round,pad=0.06",
                                   facecolor='white', edgecolor=color, linewidth=1)
            ax12.add_patch(ibox)
            ax12.text(ix, y, item, ha='center', va='center', fontsize=7, fontweight='bold', color=C['dark'])
    
    # MVP marker
    ax12.axvline(x=8.5, ymin=0.42, ymax=0.72, color=C['success'], linewidth=2.5, alpha=0.7)
    ax12.text(8.5, 6.5, '▲ MVP Launch', ha='center', fontsize=8, color=C['success'], fontweight='bold')
    
    # 5B: 数据飞轮
    ax13 = fig.add_axes([0.59, 0.08, 0.19, 0.19])
    ax13.set_xlim(0, 6); ax13.set_ylim(0, 6)
    ax13.axis('off')
    ax13.set_title('Data Flywheel', fontsize=11, fontweight='bold', color=C['dark'], pad=5)
    
    fw_items = [
        (3, 4.8, 1.0, 'Users Wear\nGuard Daily', C['primary']),
        (4.7, 3.3, 0.9, 'Profile Gets\nMore Accurate', C['secondary']),
        (3, 1.7, 0.9, 'Switching\nCost ↑', C['success']),
        (1.3, 3.3, 0.9, 'Stay &\nRecommend', C['accent']),
    ]
    for x, y, r, label, color in fw_items:
        circle = plt.Circle((x, y), r, facecolor=color, edgecolor='white', linewidth=2, alpha=0.85)
        ax13.add_patch(circle)
        ax13.text(x, y, label, ha='center', va='center', fontsize=7, fontweight='bold', color='white')
    
    # Center
    ax13.add_patch(plt.Circle((3, 3.25), 0.55, facecolor='white', edgecolor=C['primary'], linewidth=2))
    ax13.text(3, 3.25, 'North\nStar', ha='center', va='center', fontsize=7, fontweight='bold', color=C['primary'])
    
    # Arrows
    for s, e in [((3.8, 4.3), (4.2, 3.8)), ((4.2, 2.8), (3.8, 2.3)), ((2.2, 2.3), (1.8, 2.8)), ((1.8, 3.8), (2.2, 4.3))]:
        ax13.annotate('', xy=e, xytext=s, arrowprops=dict(arrowstyle='->', color=C['dark'], lw=1.5, connectionstyle='arc3,rad=0.3'))
    
    # 5C: 关键指标卡
    ax14 = fig.add_axes([0.80, 0.08, 0.18, 0.19])
    ax14.set_xlim(0, 4); ax14.set_ylim(0, 8)
    ax14.axis('off')
    ax14.set_title('Key Metrics', fontsize=11, fontweight='bold', color=C['dark'], pad=5)
    
    kpis = [
        ('$99', 'Sweet Spot\nPrice', C['primary']),
        ('+42', 'Predicted\nNPS', C['success']),
        ('10.4×', 'LTV / CAC\nRatio', C['purple']),
        ('$44.5M', 'Year 3\nGross Profit', C['accent']),
        ('50%', 'Users 12-35\nAt Risk', C['danger']),
        ('11.2%', 'Market\nCAGR', C['secondary']),
    ]
    
    for i, (big, desc, color) in enumerate(kpis):
        y = 7.5 - i * 1.2
        box = FancyBboxPatch((0.1, y-0.45), 3.8, 0.9, boxstyle="round,pad=0.08",
                              facecolor=color, edgecolor='white', linewidth=1, alpha=0.12)
        ax14.add_patch(box)
        ax14.text(1.0, y+0.1, big, ha='center', fontsize=14, fontweight='bold', color=color)
        ax14.text(3.0, y+0.1, desc, ha='center', va='center', fontsize=7, color=C['dark'])
    
    # === 底部信息条 ===
    ax_footer = fig.add_axes([0.02, 0.01, 0.96, 0.06])
    ax_footer.axis('off')
    ax_footer.set_xlim(0, 24); ax_footer.set_ylim(0, 1)
    footer_bg = FancyBboxPatch((0, 0), 24, 1, boxstyle="round,pad=0.02",
                                facecolor=C['light'], edgecolor='#E5E7EB', linewidth=1)
    ax_footer.add_patch(footer_bg)
    ax_footer.text(12, 0.7, 'Soundcore Guard — AI-Native Product Design for Anker Innovations', 
                   fontsize=10, fontweight='bold', color=C['dark'], ha='center')
    ax_footer.text(12, 0.3, 'Method: Expand (AI Brain Trust) → Challenge (AI User Avatars) → Converge (AI Expert Panel + PM Verdict)  |  All data anchored to public sources  |  Hearing wellness positioning — NOT medical device',
                   fontsize=7, color=C['gray'], ha='center')
    
    # ── 保存 ──
    fig.savefig(f'{OUT}/soundcore-guard-infographic.png', facecolor='white', dpi=200)
    plt.close()
    print(f'✅ 信息画报已生成: {OUT}/soundcore-guard-infographic.png')
    import os
    size_kb = os.path.getsize(f'{OUT}/soundcore-guard-infographic.png') / 1024
    print(f'   尺寸: 24×36 inches @ 200dpi  |  文件大小: {size_kb:.0f} KB')


if __name__ == '__main__':
    create_infographic()
