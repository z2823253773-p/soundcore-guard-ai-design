#!/usr/bin/env python3
"""Soundcore Guard 数据可视化 — 全套图表生成"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Arc
import matplotlib.patches as mpatches
from matplotlib.font_manager import FontProperties
import warnings
warnings.filterwarnings('ignore')

# ── 全局样式 ──────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica'],
    'axes.unicode_minus': False,
    'figure.dpi': 150,
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.2,
})

OUT = os.path.dirname(os.path.abspath(__file__))

# ── 品牌色板 ──────────────────────────────────────────
C = {
    'primary':   '#1A56DB',   # 深蓝 - 主色
    'secondary': '#0EA5E9',   # 天蓝 - 辅色
    'accent':    '#F59E0B',   # 琥珀 - 强调
    'success':   '#10B981',   # 翠绿
    'danger':    '#EF4444',   # 红色
    'warning':   '#F97316',   # 橙色
    'purple':    '#8B5CF6',   # 紫色
    'dark':      '#111827',   # 近黑
    'gray':      '#6B7280',   # 灰色
    'light':     '#F3F4F6',   # 浅灰
    'white':     '#FFFFFF',
    'sky':       '#38BDF8',
    'teal':      '#14B8A6',
    'pink':      '#EC4899',
    'indigo':    '#6366F1',
}

PALETTE_6 = [C['primary'], C['secondary'], C['accent'], C['success'], C['purple'], C['danger']]
PALETTE_8 = [C['primary'], C['secondary'], C['teal'], C['accent'], C['purple'], C['danger'], C['sky'], C['indigo']]
PALETTE_GRADIENT = ['#1A56DB', '#2563EB', '#3B82F6', '#60A5FA', '#93C5FD', '#BFDBFE']

# ── 中文字体fallback ──────────────────────────────────
def setup_cn_font():
    """尝试加载中文字体"""
    cn_fonts = [
        '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',
        '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
        '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
        '/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',
    ]
    for fp in cn_fonts:
        if os.path.exists(fp):
            return FontProperties(fname=fp)
    return None

CN_FONT = setup_cn_font()

def cn(text):
    """中文标签包装"""
    return text  # 直接用英文或简单字符

# ── 图表生成函数 ──────────────────────────────────────

def fig1_methodology_comparison():
    """图1: AI原生 vs 传统方法 — 工作流对比流程图"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    
    # --- 传统方法 ---
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title('Traditional Experience-Driven', fontsize=16, fontweight='bold', color=C['dark'], pad=15)
    
    steps_trad = [
        ('PM\nExperience', 'Limited personal\nknowledge base', C['gray']),
        ('Small Sample\nSurvey', '30-100 surveys\n5-10 interviews', C['gray']),
        ('Manual\nCompetitor Tracking', 'What PM happens\nto notice', C['gray']),
        ('Boss\nDecides', 'Intuition-based\nhard to trace', C['danger']),
    ]
    
    for i, (title, desc, color) in enumerate(steps_trad):
        x = 1.5
        y = 8.5 - i * 2.2
        box = FancyBboxPatch((x-1.3, y-0.85), 2.6, 1.7, boxstyle="round,pad=0.15",
                             facecolor=color, edgecolor='white', linewidth=2, alpha=0.85)
        ax1.add_patch(box)
        ax1.text(x, y+0.35, title, ha='center', va='center', fontsize=12, fontweight='bold', color='white')
        ax1.text(x, y-0.4, desc, ha='center', va='center', fontsize=8, color='white', alpha=0.85)
        
        if i < 3:
            ax1.annotate('', xy=(x, y-1.1), xytext=(x, y-1.5),
                        arrowprops=dict(arrowstyle='->', color=C['gray'], lw=2.5))
    
    # Bottleneck callout
    ax1.text(7, 5, 'Bottleneck:\nPM capability = \nProduct ceiling', 
             ha='center', va='center', fontsize=11, fontweight='bold',
             color=C['danger'], bbox=dict(boxstyle='round,pad=0.5', facecolor='#FEE2E2', edgecolor=C['danger'], lw=1.5))
    ax1.annotate('', xy=(3.9, 5), xytext=(6.2, 5),
                arrowprops=dict(arrowstyle='->', color=C['danger'], lw=2, connectionstyle='arc3,rad=0.2'))
    
    # --- AI原生方法 ---
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('AI-Native Method', fontsize=16, fontweight='bold', color=C['primary'], pad=15)
    
    steps_ai = [
        ('Phase 0\nHuman PM', 'Define JTBD\n& constraints', C['indigo']),
        ('Phase 1\nAI Brain Trust', 'Full web search\nMillion-level data', C['primary']),
        ('Phase 2\nAI User Avatars', 'N user types\nAdversarial challenge', C['secondary']),
        ('Phase 3\nAI Expert Panel', 'Multi-domain\nparallel assessment', C['teal']),
        ('Phase 4\nPM + Red Team', 'Human verdict\nAI stress test', C['success']),
    ]
    
    for i, (title, desc, color) in enumerate(steps_ai):
        x = 1.5
        y = 9 - i * 1.75
        box = FancyBboxPatch((x-1.3, y-0.7), 2.6, 1.4, boxstyle="round,pad=0.12",
                             facecolor=color, edgecolor='white', linewidth=2, alpha=0.9)
        ax2.add_patch(box)
        ax2.text(x, y+0.2, title, ha='center', va='center', fontsize=11, fontweight='bold', color='white')
        ax2.text(x, y-0.35, desc, ha='center', va='center', fontsize=7.5, color='white', alpha=0.85)
        
        if i < 4:
            ax2.annotate('', xy=(x, y-0.9), xytext=(x, y-1.2),
                        arrowprops=dict(arrowstyle='->', color=C['primary'], lw=2.5))
    
    # Result callout
    ax2.text(7, 5, 'PM becomes\n"Director"\nnot "Processor"', 
             ha='center', va='center', fontsize=11, fontweight='bold',
             color=C['primary'], bbox=dict(boxstyle='round,pad=0.5', facecolor='#DBEAFE', edgecolor=C['primary'], lw=1.5))
    
    # Loop arrow
    ax2.annotate('Iterate', xy=(3.6, 0.8), xytext=(6.8, 0.8),
                fontsize=9, color=C['purple'], ha='center',
                arrowprops=dict(arrowstyle='->', color=C['purple'], lw=1.5, connectionstyle='arc3,rad=-0.4'))
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/01-methodology-comparison.png', facecolor='white')
    plt.close()
    print('✓ 图1: 方法论对比')


def fig2_opportunity_signals():
    """图2: 五大信号交叉验证 — 雷达图风格"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    signals = ['WHO Data\n(1B+ youth at risk)', 'Apple Action\n(FDA OTC hearing aid)', 
               'Market Growth\n($1.26B → $3.25B)', 'Social Sentiment\n(#hearing damage trending)',
               'User Pain\n(72% discomfort)']
    strengths = [5, 5, 4, 4, 3]
    colors_sig = [C['primary'], C['danger'], C['success'], C['warning'], C['purple']]
    
    x = np.arange(len(signals))
    bars = ax.bar(x, strengths, color=colors_sig, width=0.6, edgecolor='white', linewidth=1.5)
    
    for bar, val in zip(bars, strengths):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                '★' * val + '☆' * (5-val), ha='center', fontsize=11, color=C['dark'])
    
    ax.set_ylim(0, 6.5)
    ax.set_xticks(x)
    ax.set_xticklabels(signals, fontsize=10)
    ax.set_ylabel('Signal Strength', fontsize=13, fontweight='bold', color=C['dark'])
    ax.set_title('Five Independent Signals Converge → High-Confidence Opportunity', 
                 fontsize=15, fontweight='bold', color=C['dark'], pad=15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(C['gray'])
    ax.spines['bottom'].set_color(C['gray'])
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.tick_params(axis='y', colors=C['gray'])
    ax.tick_params(axis='x', colors=C['dark'])
    ax.axhline(y=3.5, color=C['gray'], linestyle='--', alpha=0.5, linewidth=1)
    ax.text(4.5, 3.7, 'Confidence Threshold', fontsize=9, color=C['gray'], ha='right')
    
    # Cross-verification badge
    ax.text(2, 6.0, '✓ Multi-source Cross-validated Opportunity', fontsize=12, 
            fontweight='bold', color=C['success'], ha='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#D1FAE5', edgecolor=C['success'], lw=1.5))
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/02-opportunity-signals.png', facecolor='white')
    plt.close()
    print('✓ 图2: 机会信号')


def fig3_competitive_matrix():
    """图3: 竞品定位矩阵"""
    fig, ax = plt.subplots(figsize=(13, 8))
    
    # 竞品数据: (x=价格, y=听力健康深度, 名称, 气泡大小)
    competitors = [
        (249, 9.5, 'Apple\nAirPods Pro', 800, C['dark']),
        (199, 3.0, 'Samsung\nGalaxy Buds3', 500, C['gray']),
        (279, 1.5, 'Sony\nWF-1000XM5', 450, C['gray']),
        (299, 1.0, 'Bose\nQC Ultra', 350, C['gray']),
        (169, 1.0, 'Huawei\nFreeBuds Pro', 300, C['gray']),
        (149, 0.5, 'iFLYTEK\nNano+', 200, C['gray']),
        (79, 0.0, 'Xiaomi\nAir 2 Pro', 250, C['gray']),
        (99, 8.0, '★ Soundcore\nGuard', 600, C['primary']),
        (129, 8.5, '★ Soundcore\nGuard Pro', 500, C['accent']),
    ]
    
    for px, py, name, size, color in competitors:
        alpha = 1.0 if 'Guard' in name else 0.55
        edge_color = C['primary'] if 'Guard' in name else 'white'
        edge_width = 3 if 'Guard' in name else 1.5
        ax.scatter(px, py, s=size, c=color, alpha=alpha, edgecolors=edge_color, 
                  linewidth=edge_width, zorder=5 if 'Guard' in name else 3)
        
        offset_y = 0.55 if 'Guard' not in name else -0.65
        ax.annotate(name, (px, py), textcoords="offset points", xytext=(0, offset_y*20),
                   ha='center', fontsize=8.5, fontweight='bold' if 'Guard' in name else 'normal',
                   color=C['primary'] if 'Guard' in name else C['dark'],
                   bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.85, edgecolor='none') if 'Guard' in name else None)
    
    # 分区标注
    ax.axhline(y=5, xmin=0, xmax=0.48, color=C['gray'], linestyle='--', alpha=0.5)
    ax.axvline(x=160, ymin=0, ymax=0.5, color=C['gray'], linestyle='--', alpha=0.5)
    
    ax.text(110, 8.8, 'White Space:\nHearing Health\nat Mass Price', ha='center', fontsize=11,
            fontweight='bold', color=C['primary'],
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#DBEAFE', edgecolor=C['primary'], lw=2, alpha=0.9))
    
    ax.text(260, 9, 'Premium &\nMedical-grade', ha='center', fontsize=8, color=C['gray'])
    ax.text(110, 1, 'No Health\nFeatures', ha='center', fontsize=8, color=C['gray'])
    
    ax.set_xlabel('Price (USD)', fontsize=13, fontweight='bold', color=C['dark'])
    ax.set_ylabel('Hearing Health Depth', fontsize=13, fontweight='bold', color=C['dark'])
    ax.set_title('Competitive Positioning: Hearing Health × Price', fontsize=15, fontweight='bold', pad=15)
    ax.set_xlim(50, 330)
    ax.set_ylim(-0.5, 10.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.2, linestyle='--')
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/03-competitive-matrix.png', facecolor='white')
    plt.close()
    print('✓ 图3: 竞品矩阵')


def fig4_user_insights():
    """图4: 用户洞察 — 购买意愿 + NPS + 功能优先级"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # --- 子图1: 购买意愿 by 价格点 ---
    ax = axes[0]
    prices = ['$79', '$99', '$129', '$179']
    overall = [68, 54, 38, 18]
    high_concern = [82, 76, 63, 35]
    
    x = np.arange(len(prices))
    w = 0.35
    bars1 = ax.bar(x - w/2, overall, w, label='Overall', color=C['primary'], edgecolor='white', linewidth=1)
    bars2 = ax.bar(x + w/2, high_concern, w, label='Hearing-Concerned', color=C['accent'], edgecolor='white', linewidth=1)
    
    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f'{bar.get_height():.0f}%', 
                ha='center', fontsize=9, fontweight='bold', color=C['primary'])
    for bar in bars2:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f'{bar.get_height():.0f}%', 
                ha='center', fontsize=9, fontweight='bold', color=C['accent'])
    
    ax.set_xticks(x)
    ax.set_xticklabels(prices, fontsize=12, fontweight='bold')
    ax.set_ylabel('Purchase Intent (%)', fontsize=11, fontweight='bold')
    ax.set_title('Purchase Intent by Price', fontsize=13, fontweight='bold')
    ax.legend(fontsize=9, loc='upper right')
    ax.set_ylim(0, 95)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.2)
    
    # Sweet spot annotation
    ax.annotate('Sweet Spot', xy=(1, 54), xytext=(1, 70),
               fontsize=10, ha='center', color=C['success'], fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=C['success'], lw=2))
    
    # --- 子图2: NPS by User Segment ---
    ax = axes[1]
    segments = ['Elderly\nChildren', 'Hearing\nConcerned', 'Commuter', 'Gamer', 'Student', 'Privacy\nSensitive']
    nps_vals = [72, 68, 51, 35, 28, 15]
    nps_colors = [C['success'] if v >= 50 else C['accent'] if v >= 30 else C['warning'] for v in nps_vals]
    
    bars = ax.barh(segments, nps_vals, color=nps_colors, edgecolor='white', linewidth=1.5, height=0.6)
    for bar, val in zip(bars, nps_vals):
        ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2, f'+{val}', 
                va='center', fontsize=10, fontweight='bold', color=C['dark'])
    
    ax.axvline(x=42, color=C['primary'], linestyle='--', linewidth=1.5, alpha=0.7)
    ax.text(44, 5.3, 'Overall NPS +42', fontsize=9, color=C['primary'], fontweight='bold')
    ax.set_title('NPS by User Segment', fontsize=13, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(0, 85)
    
    # --- 子图3: 功能优先级 ---
    ax = axes[2]
    features = ['Real-time\nSPL Monitor', 'Hearing Profile\n+ EQ', 'Context\nANC', 'Hearing\nTrend Report', 
                'Remote\nFamily Setup', 'AI Translate\n/ Meeting']
    importance = [32.4, 24.7, 18.3, 13.1, 7.2, 4.3]
    feat_colors = [C['primary'], C['secondary'], C['teal'], C['accent'], C['purple'], C['gray']]
    
    wedges, texts, autotexts = ax.pie(importance, labels=features, autopct='%1.1f%%',
                                       colors=feat_colors, startangle=90, pctdistance=0.6,
                                       explode=(0.05, 0.03, 0, 0, 0, 0))
    for t in autotexts:
        t.set_fontsize(9)
        t.set_fontweight('bold')
    for t in texts:
        t.set_fontsize(9)
    
    ax.set_title('Feature Priority (Weighted)', fontsize=13, fontweight='bold')
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/04-user-insights.png', facecolor='white')
    plt.close()
    print('✓ 图4: 用户洞察')


def fig5_tech_architecture():
    """图5: 技术架构图"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('Soundcore Guard — Technical Architecture', fontsize=16, fontweight='bold', 
                 color=C['dark'], pad=20)
    
    # Layer 1: Sensors
    sensors = [
        (2, 8.5, 'Dual MEMS\nMicrophones\n(Ambient + In-ear)', C['primary']),
        (5.5, 8.5, 'Bone Conduction\nSensors ×2', C['secondary']),
        (9, 8.5, 'IR In-ear\nDetection', C['teal']),
    ]
    for x, y, label, color in sensors:
        box = FancyBboxPatch((x-1.3, y-0.65), 2.6, 1.3, boxstyle="round,pad=0.15",
                             facecolor=color, edgecolor='white', linewidth=2, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=9, fontweight='bold', color='white')
    
    # Arrows down
    for x, _, _, _ in sensors:
        ax.annotate('', xy=(x, 7.0), xytext=(x, 7.5),
                   arrowprops=dict(arrowstyle='->', color=C['dark'], lw=2))
    
    # Layer 2: DSP
    ax.text(7, 7.2, '10-Sensor Fusion Data Stream', ha='center', fontsize=9, color=C['gray'], style='italic')
    
    dsp_box = FancyBboxPatch((1.5, 5.2), 11, 1.6, boxstyle="round,pad=0.2",
                             facecolor='#1E293B', edgecolor=C['primary'], linewidth=2.5, alpha=0.95)
    ax.add_patch(dsp_box)
    ax.text(7, 6.3, 'Low-Power DSP Co-processor (always-on, <0.5mA)', ha='center', fontsize=13, 
            fontweight='bold', color='white')
    ax.text(7, 5.7, 'SPL Estimation  |  Noise Classification  |  Threshold Alert Logic  |  A-Weighting Filter', 
            ha='center', fontsize=8.5, color='#93C5FD')
    
    ax.annotate('', xy=(7, 5.0), xytext=(7, 5.1),
               arrowprops=dict(arrowstyle='->', color=C['dark'], lw=2.5))
    
    # Layer 3: Thus™ AI Chip
    thus_box = FancyBboxPatch((1.5, 2.5), 11, 2.2, boxstyle="round,pad=0.2",
                              facecolor=C['primary'], edgecolor='white', linewidth=3, alpha=0.95)
    ax.add_patch(thus_box)
    ax.text(7, 4.1, 'Thus™ AI Chip Platform (CIM Architecture)', ha='center', fontsize=14, 
            fontweight='bold', color='white')
    ax.text(7, 3.5, 'Dynamic EQ Compensation (DNN)  |  Context ANC 4.0  |  Hearing Profile Engine', 
            ha='center', fontsize=8.5, color='#BFDBFE')
    ax.text(7, 3.0, 'Bluetooth 6.1  |  LE Audio / LC3  |  3-Device Multipoint  |  On-Device Privacy', 
            ha='center', fontsize=8.5, color='#BFDBFE')
    
    # Output
    ax.annotate('', xy=(7, 2.2), xytext=(7, 2.3),
               arrowprops=dict(arrowstyle='->', color=C['dark'], lw=2.5))
    
    outputs = [
        (3, 1.3, 'Hearing\nProtection', C['success']),
        (7, 1.3, 'Personalized\nAudio', C['accent']),
        (11, 1.3, 'Context\nAwareness', C['purple']),
    ]
    for x, y, label, color in outputs:
        box = FancyBboxPatch((x-1.3, y-0.55), 2.6, 1.1, boxstyle="round,pad=0.12",
                             facecolor=color, edgecolor='white', linewidth=2, alpha=0.9)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    
    # Privacy badge
    ax.text(13.5, 1.3, '🔒\nLocal\nOnly', ha='center', fontsize=8, color=C['success'], fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#D1FAE5', edgecolor=C['success'], lw=1))
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/05-tech-architecture.png', facecolor='white')
    plt.close()
    print('✓ 图5: 技术架构')


def fig6_business_model():
    """图6: 商业模式 — 收入预测 + 单位经济"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 6.5))
    
    # --- 子图1: 3年收入预测 ---
    ax = axes[0]
    years = ['Year 1', 'Year 2', 'Year 3']
    hardware = [55, 88, 132]
    subscription = [1.9, 5.5, 11.5]
    
    x = np.arange(len(years))
    w = 0.5
    bars_hw = ax.bar(x, hardware, w, label='Hardware Revenue', color=C['primary'], edgecolor='white', linewidth=1.5)
    bars_sub = ax.bar(x, subscription, w, bottom=hardware, label='Subscription Revenue', 
                      color=C['accent'], edgecolor='white', linewidth=1.5)
    
    totals = [h + s for h, s in zip(hardware, subscription)]
    for i, (h, s, t) in enumerate(zip(hardware, subscription, totals)):
        ax.text(i, t + 3, f'${t:.1f}M', ha='center', fontsize=12, fontweight='bold', color=C['dark'])
        ax.text(i, h/2, f'${h}M', ha='center', fontsize=10, color='white', fontweight='bold')
        if s > 2:
            ax.text(i, h + s/2, f'${s}M', ha='center', fontsize=10, color='white', fontweight='bold')
    
    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=13, fontweight='bold')
    ax.set_ylabel('Revenue (Million USD)', fontsize=12, fontweight='bold')
    ax.set_title('3-Year Revenue Forecast (Base Case)', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10, loc='upper left')
    ax.set_ylim(0, 160)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.2)
    
    # --- 子图2: Unit Economics ---
    ax = axes[1]
    metrics = ['CAC\n(User Acquisition)', 'Hardware\nMargin (Pro)', 'Subscription\nARPU/yr', 'LTV\n(3-Year)', 'LTV/CAC\nRatio']
    values = [14, 27, 36, 146, 10.4]
    bar_colors = [C['secondary'], C['primary'], C['accent'], C['success'], C['purple']]
    
    bars = ax.bar(metrics, values, color=bar_colors, edgecolor='white', linewidth=1.5, width=0.55)
    
    # Add value labels with $ or x
    labels = ['$14', '27%', '$36', '$146', '10.4x']
    for bar, label in zip(bars, labels):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, label,
                ha='center', fontsize=12, fontweight='bold', color=C['dark'])
    
    ax.axhline(y=42, color=C['gray'], linestyle='--', alpha=0.5, linewidth=1)
    ax.text(4.3, 44, 'Healthy LTV/CAC > 3x', fontsize=9, color=C['gray'], ha='right')
    
    ax.set_title('Unit Economics', fontsize=14, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='x', labelsize=9)
    ax.set_ylim(0, 170)
    ax.grid(axis='y', alpha=0.2)
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/06-business-model.png', facecolor='white')
    plt.close()
    print('✓ 图6: 商业模式')


def fig7_product_roadmap():
    """图7: 产品路线图"""
    fig, ax = plt.subplots(figsize=(16, 6))
    
    phases = [
        ('2026 Q4\nFoundation', [
            ('Tech Validation', 'Q4'),
            ('Supply Chain Lock', 'Q4'),
            ('Thus™ Adaptation', 'Q4'),
        ], C['indigo']),
        ('2027 Q1-Q2\nDevelopment', [
            ('SPL Algorithm', 'Q1-Q2'),
            ('App Development', 'Q1-Q2'),
            ('Beta Testing', 'Q2'),
        ], C['primary']),
        ('2027 Q3-Q4\nMVP Launch', [
            ('Guard $99 Launch', 'Q3'),
            ('Guard Pro $129', 'Q3'),
            ('Hearing Profile', 'Q4'),
        ], C['success']),
        ('2028\nScale & V2/V3', [
            ('Dynamic EQ Comp.', 'H1'),
            ('Annual Report', 'H1'),
            ('Elder Mode', 'H2'),
            ('Enterprise Ed.', 'H2'),
        ], C['accent']),
    ]
    
    y_positions = [7, 5.5, 3.5, 1.5]
    
    for (title, items, color), y in zip(phases, y_positions):
        # Phase block
        box = FancyBboxPatch((0.3, y-0.7), 2.2, 1.9, boxstyle="round,pad=0.15",
                             facecolor=color, edgecolor='white', linewidth=2, alpha=0.9)
        ax.add_patch(box)
        ax.text(1.4, y+0.5, title, ha='center', va='center', fontsize=11, fontweight='bold', color='white')
        
        # Timeline bar
        ax.barh(y, 13.2, 0.05, left=2.8, color=color, alpha=0.3)
        
        # Items
        for j, (item, period) in enumerate(items):
            ix = 3.2 + j * 2.8
            item_box = FancyBboxPatch((ix-1.1, y-0.45), 2.2, 0.9, boxstyle="round,pad=0.08",
                                      facecolor='white', edgecolor=color, linewidth=1.5, alpha=0.95)
            ax.add_patch(item_box)
            ax.text(ix, y+0.05, item, ha='center', va='center', fontsize=9, fontweight='bold', color=C['dark'])
            ax.text(ix, y-0.3, period, ha='center', va='center', fontsize=7.5, color=C['gray'])
        
        # Arrow between phases
        if y > 2:
            ax.annotate('', xy=(14.2, y-0.9), xytext=(14.2, y-1.3),
                       arrowprops=dict(arrowstyle='->', color=C['gray'], lw=2))
    
    # MVP marker
    ax.axvline(x=8.6, ymin=0.42, ymax=0.72, color=C['success'], linestyle='-', linewidth=3, alpha=0.7)
    ax.text(8.6, 8.7, '▲ MVP\nLaunch', ha='center', fontsize=10, color=C['success'], fontweight='bold')
    
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 8.5)
    ax.axis('off')
    ax.set_title('Soundcore Guard — Product Roadmap', fontsize=16, fontweight='bold', color=C['dark'], pad=15)
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/07-product-roadmap.png', facecolor='white')
    plt.close()
    print('✓ 图7: 产品路线图')


def fig8_comparison_table():
    """图8: AI原生 vs 传统方法 对比表"""
    fig, ax = plt.subplots(figsize=(16, 5))
    ax.axis('off')
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 6)
    
    # Title
    ax.text(8, 5.6, 'Same Brief, Different Outcomes: AI-Native vs Traditional', 
            ha='center', fontsize=15, fontweight='bold', color=C['dark'])
    
    # Table
    col_w = [2.8, 5.5, 5.5]
    col_x = [0.8]
    for w in col_w[:-1]:
        col_x.append(col_x[-1] + w)
    
    headers = ['Dimension', 'Traditional → Soundcore Pro', 'AI-Native → Soundcore Guard']
    header_colors = [C['dark'], C['danger'], C['primary']]
    
    # Header
    for j, (hdr, hc) in enumerate(zip(headers, header_colors)):
        box = FancyBboxPatch((col_x[j], 4.6), col_w[j], 0.7, boxstyle="round,pad=0.08",
                             facecolor=hc, edgecolor='white', linewidth=1.5, alpha=0.9)
        ax.add_patch(box)
        ax.text(col_x[j] + col_w[j]/2, 4.95, hdr, ha='center', va='center', fontsize=10, 
                fontweight='bold', color='white')
    
    rows = [
        ('Core Value Prop', 'Better ANC + AI Translate', 'Personal Hearing Guardian'),
        ('Differentiation', 'Parameter upgrade (me-too)', 'Category innovation (hearing wellness)'),
        ('Price', '$149–179', '$99–129'),
        ('Business Model', 'One-time hardware', 'Hardware + Subscription + Data Flywheel'),
        ('Key Insight Source', 'PM experience + 50 surveys', 'WHO data + 500 AI avatars + 5 signals'),
        ('Moat', 'Specs (catchable)', 'Hearing data flywheel (hard to copy)'),
    ]
    
    for i, row in enumerate(rows):
        y = 4.3 - i * 0.65
        bg_color = C['light'] if i % 2 == 0 else 'white'
        for j, (cell, cw, cx) in enumerate(zip(row, col_w, col_x)):
            box = FancyBboxPatch((cx, y-0.25), cw, 0.55, boxstyle="round,pad=0.05",
                                 facecolor=bg_color, edgecolor='#E5E7EB', linewidth=0.5)
            ax.add_patch(box)
            font_weight = 'bold' if j == 0 else 'normal'
            font_color = C['dark'] if j == 0 else (C['danger'] if j == 1 else C['primary'])
            ax.text(cx + cw/2, y, cell, ha='center', va='center', fontsize=8.5, 
                    fontweight=font_weight, color=font_color)
    
    # Bottom verdict
    verdict_box = FancyBboxPatch((0.8, -0.1), 14.2, 0.55, boxstyle="round,pad=0.1",
                                  facecolor=C['primary'], edgecolor='white', linewidth=2, alpha=0.12)
    ax.add_patch(verdict_box)
    ax.text(8, 0.15, 'Verdict: Method changes outcome. AI-native found a category-defining white space that experience-driven method missed.',
            ha='center', fontsize=10, fontweight='bold', color=C['primary'])
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/08-comparison-table.png', facecolor='white')
    plt.close()
    print('✓ 图8: 对比表')


def fig9_pricing_strategy():
    """图9: 定价策略 — 价格 vs 购买意愿曲线 + 价格段分布"""
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # --- 子图1: 价格-需求曲线 ---
    ax = axes[0]
    prices_detailed = [59, 79, 99, 119, 129, 149, 179, 199, 249]
    purchase_intent = [82, 68, 54, 44, 38, 28, 18, 12, 5]
    
    ax.plot(prices_detailed, purchase_intent, 'o-', color=C['primary'], linewidth=3, markersize=10, 
            markerfacecolor='white', markeredgewidth=2.5)
    ax.fill_between(prices_detailed, purchase_intent, alpha=0.1, color=C['primary'])
    
    # Annotations
    ax.annotate('Sweet Spot\n$99 • 54% Intent', xy=(99, 54), xytext=(120, 68),
               fontsize=11, ha='center', color=C['success'], fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=C['success'], lw=2, connectionstyle='arc3,rad=-0.2'),
               bbox=dict(boxstyle='round,pad=0.3', facecolor='#D1FAE5', edgecolor=C['success'], alpha=0.9))
    
    ax.annotate('Too Cheap\nLow Margin', xy=(59, 82), xytext=(40, 92),
               fontsize=9, ha='center', color=C['gray'],
               arrowprops=dict(arrowstyle='->', color=C['gray'], lw=1.5))
    
    ax.annotate('Competitive Zone\nApple/Sony/Bose', xy=(249, 5), xytext=(230, 18),
               fontsize=9, ha='center', color=C['danger'],
               arrowprops=dict(arrowstyle='->', color=C['danger'], lw=1.5))
    
    # Shaded zones
    ax.axvspan(79, 129, alpha=0.08, color=C['success'])
    ax.text(104, 88, 'Target\nRange', ha='center', fontsize=10, fontweight='bold', color=C['success'])
    
    ax.set_xlabel('Price (USD)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Purchase Intent (%)', fontsize=12, fontweight='bold')
    ax.set_title('Price-Demand Curve', fontsize=14, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.15)
    
    # --- 子图2: TWS价格段分布 ---
    ax = axes[1]
    segments_labels = ['<$50', '$50–100', '$100–150', '$150–250', '$250+']
    segments_share = [35, 25, 18, 12, 10]
    seg_colors = [C['gray'], C['secondary'], C['primary'], C['accent'], C['dark']]
    
    wedges, texts, autotexts = ax.pie(segments_share, labels=segments_labels, autopct='%1.0f%%',
                                       colors=seg_colors, startangle=90,
                                       explode=(0, 0, 0.1, 0, 0),
                                       wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2))
    
    for t in autotexts:
        t.set_fontsize(10)
        t.set_fontweight('bold')
    for t in texts:
        t.set_fontsize(10)
    
    # Center text
    ax.text(0, 0, 'TWS Market\nby Price', ha='center', va='center', fontsize=12, fontweight='bold', color=C['dark'])
    
    ax.set_title('TWS Market Price Distribution (2024-25)', fontsize=14, fontweight='bold')
    
    # Callout
    ax.annotate('$100-150: $2.9B market\nNO hearing health products', xy=(0.5, 0.6), xytext=(1.3, 0.7),
               fontsize=10, ha='center', color=C['primary'], fontweight='bold',
               arrowprops=dict(arrowstyle='->', color=C['primary'], lw=2),
               bbox=dict(boxstyle='round,pad=0.4', facecolor='#DBEAFE', edgecolor=C['primary'], alpha=0.95))
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/09-pricing-strategy.png', facecolor='white')
    plt.close()
    print('✓ 图9: 定价策略')


def fig10_data_flywheel():
    """图10: 数据飞轮 + 北极星指标"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis('off')
    ax.set_title('The Data Flywheel — Soundcore Guard Moat', fontsize=16, fontweight='bold', 
                 color=C['dark'], pad=15)
    
    # Flywheel circles
    flywheel = [
        (6, 8.5, 2.5, 'Users Wear\nGuard Daily', C['primary']),
        (9, 6, 2.2, 'Hearing Profile\nGets More Accurate', C['secondary']),
        (6, 3.5, 2.2, 'Switching Cost\nIncreases', C['success']),
        (3, 6, 2.2, 'Users Stay\n& Recommend', C['accent']),
    ]
    
    for x, y, r, label, color in flywheel:
        circle = plt.Circle((x, y), r, facecolor=color, edgecolor='white', linewidth=3, alpha=0.85, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, label, ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    
    # Arrows between circles
    arrow_params = [
        ((8.2, 7.8), (8.2, 7.0)),
        ((8.2, 5.0), (8.2, 4.2)),
        ((4.5, 4.2), (4.5, 5.0)),
        ((3.8, 7.0), (3.8, 7.8)),
    ]
    for start, end in arrow_params:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', color=C['dark'], lw=3, connectionstyle='arc3,rad=0.3'))
    
    # Center: North Star
    center_circle = plt.Circle((6, 6), 1.1, facecolor='white', edgecolor=C['primary'], linewidth=3, zorder=5)
    ax.add_patch(center_circle)
    ax.text(6, 6, 'North Star\nMetric', ha='center', va='center', fontsize=9, fontweight='bold', color=C['primary'])
    ax.text(6, 5.5, 'Weekly Active\n"Guard Sessions"', ha='center', va='center', fontsize=8, color=C['dark'])
    
    # Side annotations
    ax.text(11.5, 10, 'Moat Depth:', fontsize=11, fontweight='bold', color=C['dark'])
    ax.text(11.5, 9.3, '• Data improves\n  with usage', fontsize=9, color=C['gray'])
    ax.text(11.5, 8.6, '• Switching cost\n  increases over time', fontsize=9, color=C['gray'])
    ax.text(11.5, 7.9, '• Annual reports\n  = viral loop', fontsize=9, color=C['gray'])
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/10-data-flywheel.png', facecolor='white')
    plt.close()
    print('✓ 图10: 数据飞轮')


def fig11_bom_waterfall():
    """图11: BOM成本瀑布图"""
    fig, ax = plt.subplots(figsize=(13, 7))
    
    components = ['Thus™\nAI Chip', 'MEMS Mics\n×8', 'Bone Cond.\n×2', 'Battery\n60mAh', 
                  'Charging\nCase', 'Driver\nUnits', 'PCB +\nPassive', 'Assembly\n+ Test',
                  'Algorithm\nLicense', 'Marketing\n(15-20%)', 'Channel\n(25-30%)']
    costs = [9, 3.5, 2.5, 1.8, 6, 3.5, 2.5, 5, 1.5, 17.5, 27.5]
    
    cumulative = np.cumsum(costs)
    colors_waterfall = [C['primary']] * 9 + [C['warning'], C['secondary']]
    
    # Bars
    prev = 0
    for i, (comp, cost, cum, color) in enumerate(zip(components, costs, cumulative, colors_waterfall)):
        bar = ax.bar(i, cost, bottom=prev, color=color, edgecolor='white', linewidth=1.5, width=0.65)
        if cost > 3:
            ax.text(i, prev + cost/2, f'${cost:.1f}', ha='center', va='center', fontsize=8.5, 
                    fontweight='bold', color='white')
        ax.text(i, prev + cost + 1.2, comp, ha='center', va='bottom', fontsize=8, color=C['dark'])
        prev = cum
    
    # Total
    total = sum(costs)
    ax.text(10.5, total + 3, f'Total Cost\n~${total:.0f}', ha='center', fontsize=13, 
            fontweight='bold', color=C['primary'])
    
    # Price line
    ax.axhline(y=99, color=C['success'], linestyle='--', linewidth=2.5, alpha=0.7)
    ax.text(10.5, 101, f'Retail Price\n$99', ha='center', fontsize=11, fontweight='bold', color=C['success'])
    
    # Margin zone
    ax.fill_between([-0.5, 10.5], total, 99, alpha=0.06, color=C['success'])
    ax.text(5, total + (99-total)/2, f'Gross Margin\n${99-total:.0f} ({(99-total)/99*100:.0f}%)', 
            ha='center', fontsize=10, fontweight='bold', color=C['success'])
    
    ax.set_xticks([])
    ax.set_ylabel('Cost (USD)', fontsize=12, fontweight='bold')
    ax.set_title('Soundcore Guard — Cost Structure ($99 SKU)', fontsize=14, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(0, 120)
    ax.grid(axis='y', alpha=0.15)
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/11-bom-waterfall.png', facecolor='white')
    plt.close()
    print('✓ 图11: BOM成本')


def fig12_conjoint_analysis():
    """图12: Conjoint Analysis 效用值"""
    fig, ax = plt.subplots(figsize=(13, 6))
    
    combos = [
        'Full Suite @ $99',
        'Guard+Profile @ $79',
        'Full Suite @ $129',
        'Basic Alert @ $79',
        'Context ANC @ $99',
        'No Health @ $79',
    ]
    utilities = [0.82, 0.71, 0.65, 0.42, 0.31, 0.12]
    combo_colors = [C['primary'], C['success'], C['secondary'], C['warning'], C['gray'], '#D1D5DB']
    
    bars = ax.barh(combos, utilities, color=combo_colors, edgecolor='white', linewidth=1.5, height=0.6)
    
    for bar, val in zip(bars, utilities):
        ax.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height()/2, f'{val:.2f}',
                va='center', fontsize=11, fontweight='bold', color=C['dark'])
    
    # Winner
    ax.text(0.85, 5, '← Highest Utility', fontsize=10, color=C['primary'], fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#DBEAFE', edgecolor=C['primary'], alpha=0.9))
    
    ax.set_xlabel('Utility Score', fontsize=12, fontweight='bold')
    ax.set_title('Conjoint Analysis: Feature × Price Combination Utility\n(AI-Simulated 500 Respondents)',
                 fontsize=13, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(0, 1.05)
    ax.grid(axis='x', alpha=0.15)
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/12-conjoint-analysis.png', facecolor='white')
    plt.close()
    print('✓ 图12: Conjoint分析')


def fig13_market_growth():
    """图13: 市场增长 — Smart Hearing Protection + TWS"""
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # --- 子图1: Smart Hearing Protection Market ---
    ax = axes[0]
    years_market = ['2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032', '2033', '2034']
    # CAGR 11.2% from $1.26B to $3.25B
    base = 1.26
    cagr = 0.112
    values = [base * (1 + cagr) ** i for i in range(10)]
    
    ax.fill_between(range(10), values, alpha=0.15, color=C['primary'])
    ax.plot(range(10), values, 'o-', color=C['primary'], linewidth=3, markersize=7, markerfacecolor='white')
    
    for i, v in enumerate(values):
        if i % 2 == 0:
            ax.text(i, v + 0.1, f'${v:.1f}B', ha='center', fontsize=8, fontweight='bold', color=C['dark'])
    
    ax.set_xticks(range(10))
    ax.set_xticklabels(years_market, rotation=45, fontsize=8)
    ax.set_ylabel('Market Size (Billion USD)', fontsize=11, fontweight='bold')
    ax.set_title('Smart Hearing Protection Market\nCAGR 11.2% | $1.26B → $3.25B', fontsize=13, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.15)
    
    # --- 子图2: TWS Market by Region ---
    ax = axes[1]
    regions = ['Asia\nPacific', 'North\nAmerica', 'Europe', 'Latin\nAmerica', 'MEA']
    region_shares = [42.3, 31.2, 18.6, 5.1, 2.8]
    region_cagrs = [12.8, 9.5, 10.2, 7.5, 8.1]
    
    x = np.arange(len(regions))
    w = 0.35
    
    bars1 = ax.bar(x - w/2, region_shares, w, label='Market Share (%)', color=C['primary'], edgecolor='white', linewidth=1.5)
    ax2_twin = ax.twinx()
    bars2 = ax2_twin.bar(x + w/2, region_cagrs, w, label='CAGR (%)', color=C['accent'], edgecolor='white', linewidth=1.5)
    
    for bar in bars1:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f'{bar.get_height():.1f}%',
                ha='center', fontsize=9, fontweight='bold', color=C['primary'])
    for bar in bars2:
        ax2_twin.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, f'{bar.get_height():.1f}%',
                ha='center', fontsize=9, fontweight='bold', color=C['accent'])
    
    ax.set_xticks(x)
    ax.set_xticklabels(regions, fontsize=9)
    ax.set_ylabel('Market Share (%)', fontsize=11, fontweight='bold', color=C['primary'])
    ax2_twin.set_ylabel('CAGR (%)', fontsize=11, fontweight='bold', color=C['accent'])
    ax.set_title('Smart Hearing Protection by Region (2025)', fontsize=13, fontweight='bold')
    
    # Combined legend
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2_twin.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='upper right')
    
    ax.spines['top'].set_visible(False)
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/13-market-growth.png', facecolor='white')
    plt.close()
    print('✓ 图13: 市场增长')


def fig14_hearing_risk_awareness():
    """图14: 听力风险认知 — 信息图风格"""
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('The Silent Crisis: Hearing Loss Risk Landscape', fontsize=17, fontweight='bold', 
                 color=C['dark'], pad=20)
    
    # Key stats boxes
    stats = [
        (2, 5.5, '1B+', 'Youth at risk of\nirreversible hearing loss', C['danger'], 'WHO'),
        (5.5, 5.5, '2.5B', 'People projected with\nhearing loss by 2050', C['warning'], 'WHO'),
        (9, 5.5, '74%', 'Users replace earbuds\nevery 2+ years', C['primary'], 'Market'),
        (12.5, 5.5, '50%', 'Ages 12-35 exposed\nto damaging noise', C['purple'], 'WHO'),
    ]
    
    for x, y, big, desc, color, source in stats:
        box = FancyBboxPatch((x-1.4, y-1.3), 2.8, 2.6, boxstyle="round,pad=0.2",
                             facecolor=color, edgecolor='white', linewidth=2.5, alpha=0.12)
        ax.add_patch(box)
        ax.text(x, y+0.6, big, ha='center', fontsize=28, fontweight='bold', color=color)
        ax.text(x, y-0.2, desc, ha='center', fontsize=9, color=C['dark'])
        ax.text(x, y-0.9, f'Source: {source}', ha='center', fontsize=7, color=C['gray'], style='italic')
    
    # The gap visualization
    ax.text(7, 3.2, 'THE GAP', ha='center', fontsize=14, fontweight='bold', color=C['dark'])
    
    # Left: Problem
    prob_box = FancyBboxPatch((0.5, 1.0), 5.5, 1.8, boxstyle="round,pad=0.2",
                               facecolor='#FEE2E2', edgecolor=C['danger'], linewidth=2, alpha=0.7)
    ax.add_patch(prob_box)
    ax.text(3.25, 2.4, 'The Problem', ha='center', fontsize=12, fontweight='bold', color=C['danger'])
    ax.text(3.25, 1.8, 'Massive hearing risk + No affordable\nprevention tool for non-Apple users', 
            ha='center', fontsize=10, color=C['dark'])
    
    # Right: Solution
    sol_box = FancyBboxPatch((8, 1.0), 5.5, 1.8, boxstyle="round,pad=0.2",
                              facecolor='#D1FAE5', edgecolor=C['success'], linewidth=2, alpha=0.7)
    ax.add_patch(sol_box)
    ax.text(10.75, 2.4, 'Soundcore Guard', ha='center', fontsize=12, fontweight='bold', color=C['success'])
    ax.text(10.75, 1.8, '$99 preventive hearing guardian\nCross-platform • Wellness • Data flywheel', 
            ha='center', fontsize=10, color=C['dark'])
    
    # Arrow between
    ax.annotate('', xy=(7.5, 1.9), xytext=(6.5, 1.9),
               arrowprops=dict(arrowstyle='->', color=C['primary'], lw=3))
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/14-hearing-risk.png', facecolor='white')
    plt.close()
    print('✓ 图14: 听力风险')


def fig15_subscription_model():
    """图15: 订阅模型收入增长"""
    fig, ax = plt.subplots(figsize=(12, 7))
    
    months = list(range(1, 37))
    # Hardware sales drive install base, then subscription grows
    install_base = [min(m * 4.2, 120) for m in months]  # Thousands
    sub_revenue = [b * 0.08 * 2.99 for b in install_base]  # 8% conversion × $2.99
    # Gradual conversion increase
    for i in range(len(sub_revenue)):
        if i > 6:
            sub_revenue[i] *= (1 + min((i-6) * 0.02, 0.3))
    
    ax.fill_between(months, sub_revenue, alpha=0.2, color=C['accent'])
    ax.plot(months, sub_revenue, color=C['accent'], linewidth=3)
    
    # Year markers
    for yr, label in [(12, 'Year 1\n$1.9M ARR'), (24, 'Year 2\n$5.5M ARR'), (36, 'Year 3\n$11.5M ARR')]:
        idx = yr - 1
        ax.scatter([yr], [sub_revenue[idx]], s=120, color=C['accent'], edgecolors='white', linewidth=2, zorder=5)
        ax.annotate(label, (yr, sub_revenue[idx]), textcoords="offset points", xytext=(10, 20),
                   fontsize=10, ha='center', color=C['accent'], fontweight='bold',
                   arrowprops=dict(arrowstyle='->', color=C['accent'], lw=1.5))
    
    ax.set_xlabel('Months Since Launch', fontsize=12, fontweight='bold')
    ax.set_ylabel('Monthly Subscription Revenue ($K)', fontsize=12, fontweight='bold')
    ax.set_title('Subscription Revenue Ramp: The "Second Engine"', fontsize=14, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(True, alpha=0.15)
    ax.set_xlim(0, 38)
    
    # Annotation
    ax.text(30, sub_revenue[-1] * 0.7, 'Hardware drives\ninstall base\n→ Subscription\ncompounds', 
            fontsize=10, color=C['dark'], ha='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=C['accent'], alpha=0.9))
    
    plt.tight_layout()
    fig.savefig(f'{OUT}/15-subscription-model.png', facecolor='white')
    plt.close()
    print('✓ 图15: 订阅模型')


# ── 主程序 ──────────────────────────────────────────
if __name__ == '__main__':
    print('🎨 Generating Soundcore Guard data visualizations...\n')
    
    fig1_methodology_comparison()
    fig2_opportunity_signals()
    fig3_competitive_matrix()
    fig4_user_insights()
    fig5_tech_architecture()
    fig6_business_model()
    fig7_product_roadmap()
    fig8_comparison_table()
    fig9_pricing_strategy()
    fig10_data_flywheel()
    fig11_bom_waterfall()
    fig12_conjoint_analysis()
    fig13_market_growth()
    fig14_hearing_risk_awareness()
    fig15_subscription_model()
    
    # Summary
    import glob
    charts = sorted(glob.glob(f'{OUT}/*.png'))
    total_size = sum(os.path.getsize(c) for c in charts)
    print(f'\n✅ All {len(charts)} charts generated!')
    print(f'📁 Location: {OUT}/')
    print(f'📦 Total size: {total_size/1024:.0f} KB')
    for c in charts:
        size_kb = os.path.getsize(c) / 1024
        print(f'   {os.path.basename(c):40s} {size_kb:6.0f} KB')
