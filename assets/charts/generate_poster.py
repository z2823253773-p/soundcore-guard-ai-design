#!/usr/bin/env python3
"""
Soundcore Guard — AI 原生产品设计 · 数据海报
统一设计语言：思源黑体 + 蓝/琥珀/绿配色，7板块从上至下有序展开
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
from matplotlib.font_manager import FontProperties
import numpy as np

# ============================================================
# 全局设计参数
# ============================================================
DEEP_BLUE   = '#1a237e'
TECH_BLUE   = '#1976D2'
LIGHT_BLUE  = '#42A5F5'
SKY_BLUE    = '#BBDEFB'
AMBER       = '#FF8F00'
GREEN       = '#2E7D32'
LIGHT_GREEN = '#81C784'
ORANGE      = '#E65100'
RED         = '#C62828'
DARK        = '#212121'
GRAY        = '#616161'
LIGHT_GRAY  = '#BDBDBD'
BG          = '#F5F7FA'
WHITE       = '#FFFFFF'
CARD_BG     = '#FFFFFF'

CN_REG = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
CN_BLD = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'

def cn(size=11):
    return FontProperties(fname=CN_REG, size=size)

def cnb(size=11):
    return FontProperties(fname=CN_BLD, size=size)

FIG_W, FIG_H = 20, 30.5

# ============================================================
# 辅助函数
# ============================================================
def draw_card(ax, x, y, w, h, color=CARD_BG, edge=None, zorder=1):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15", facecolor=color,
                         edgecolor=edge or LIGHT_GRAY, linewidth=0.8, zorder=zorder)
    ax.add_patch(box)

def draw_section_header(ax, y, number, title, subtitle):
    cx = 0.6
    cy = y + 0.35
    ax.add_patch(Circle((cx, cy), 0.32, facecolor=DEEP_BLUE, zorder=3))
    ax.text(cx, cy, str(number), fontproperties=cnb(12), color=WHITE, ha='center', va='center', zorder=4)
    ax.text(1.1, y+0.42, title, fontproperties=cnb(17), color=DEEP_BLUE, ha='left', va='center')
    ax.text(1.1, y+0.02, subtitle, fontproperties=cn(10), color=GRAY, ha='left', va='center')

def draw_metric_card(ax, x, y, w, h, value, label, color=TECH_BLUE):
    draw_card(ax, x, y, w, h, edge=color, color=WHITE)
    ax.text(x+w/2, y+h*0.55, str(value), fontproperties=cnb(20), color=color, ha='center', va='center')
    ax.text(x+w/2, y+h*0.22, label, fontproperties=cn(9), color=DARK, ha='center', va='center')

# ============================================================
# 创建画布
# ============================================================
fig, ax = plt.subplots(figsize=(FIG_W, FIG_H))
ax.set_xlim(0, FIG_W)
ax.set_ylim(0, FIG_H)
ax.set_aspect('equal')
ax.axis('off')
ax.add_patch(plt.Rectangle((0, 0), FIG_W, FIG_H, facecolor=BG, zorder=0))

# ============================================================
# 顶部标题栏
# ============================================================
ax.add_patch(plt.Rectangle((0, 29.6), FIG_W, 0.9, facecolor=DEEP_BLUE, zorder=1))
ax.text(0.5, 30.3, 'SOUNDCORE × AI-NATIVE DESIGN', fontproperties=cnb(10), color=LIGHT_BLUE, va='center')
ax.text(0.5, 29.95, '不止听歌——你的个人听觉管家', fontproperties=cnb(24), color=WHITE, va='center')
ax.text(0.5, 29.6, 'AI 原生产品设计方法 × Soundcore Guard 听力守护 TWS 耳机', fontproperties=cn(12), color=SKY_BLUE, va='center')

# ============================================================
# 板块 1：核心命题
# ============================================================
TOP_Y = 28.5
SEC_Y = 24.0
HEIGHT = 4.5
draw_section_header(ax, SEC_Y+HEIGHT-0.55, '01', '核心命题：方法改变答案', '同一个命题，两种方法，两个完全不同的方案')

# 传统方法卡片
T1_X, T1_W = 0.5, 8.5
T1_H = 2.2
draw_card(ax, T1_X, SEC_Y+HEIGHT-T1_H-0.55, T1_W, T1_H, edge=LIGHT_GRAY)
Y1 = SEC_Y+HEIGHT-T1_H-0.55
ax.text(T1_X+0.25, Y1+T1_H-0.3, '传统经验驱动方法', fontproperties=cnb(13), color=GRAY)
ax.text(T1_X+0.25, Y1+T1_H-0.75, 'Soundcore Pro：更好的降噪 + AI 翻译', fontproperties=cn(11), color=DARK)
ax.text(T1_X+0.25, Y1+T1_H-1.15, '本质：Me-too 跟随策略', fontproperties=cn(10), color=RED)
ax.text(T1_X+0.25, Y1+T1_H-1.5, '定价 $149–179 | 差异化靠参数（可被追上）', fontproperties=cn(9), color=GRAY)
ax.text(T1_X+0.25, Y1+T1_H-1.85, '决策依据：PM 个人经验 + 竞品对标', fontproperties=cn(9), color=GRAY)

# AI 方法卡片
T2_X = T1_X + T1_W + 0.5
T2_W = 10
draw_card(ax, T2_X, SEC_Y+HEIGHT-T1_H-0.55, T2_W, T1_H, edge=TECH_BLUE)
Y2 = SEC_Y+HEIGHT-T1_H-0.55
ax.text(T2_X+0.25, Y2+T1_H-0.3, 'AI 原生方法', fontproperties=cnb(13), color=TECH_BLUE)
ax.text(T2_X+0.25, Y2+T1_H-0.75, 'Soundcore Guard：平价预防性听力守护', fontproperties=cn(11), color=DARK)
ax.text(T2_X+0.25, Y2+T1_H-1.15, '本质：品类创新 —— 开拓 $100 听力健康新赛道', fontproperties=cn(10), color=GREEN)
ax.text(T2_X+0.25, Y2+T1_H-1.5, '定价 $99–129 | 差异化靠数据飞轮（越用越准）', fontproperties=cn(9), color=GRAY)
ax.text(T2_X+0.25, Y2+T1_H-1.85, '决策依据：AI 智囊 → AI 用户替身 → AI 专家团 → 人类 PM', fontproperties=cn(9), color=GRAY)

# 工作流独立一行
flow_y = SEC_Y + 0.35
steps = ['AI 智囊\n全网信号', 'AI 替身\n500 用户', 'AI 专家\n可行性', '人类 PM\n裁决', '产品\n方案']
for i, s in enumerate(steps):
    fx = 2.5 + i * 3.4
    draw_card(ax, fx, flow_y, 2.8, 1.0, edge=TECH_BLUE, color=SKY_BLUE)
    ax.text(fx+1.4, flow_y+0.5, s, fontproperties=cnb(9), color=DEEP_BLUE, ha='center', va='center')
    if i < len(steps)-1:
        ax.annotate('', xy=(fx+3.0, flow_y+0.5), xytext=(fx+2.8, flow_y+0.5),
                    arrowprops=dict(arrowstyle='->', color=TECH_BLUE, lw=1.5))

# ============================================================
# 板块 2：五大市场信号
# ============================================================
SEC_Y = 19.8
HEIGHT = 4.0
draw_section_header(ax, SEC_Y+HEIGHT-0.55, '02', '五大信号 -> 被忽视的市场空白', 'AI 智囊从全网数据中发现的 5 个关键信号，传统经验方法全部遗漏')

signals = [
    ('① 全球听力危机', '12 亿', '人面临听力损失风险',
     'WHO 2024：全球 1/4 人口\n2050 年前将出现听力问题'),
    ('② TWS 市场饱和', '23%', 'CAGR',
     '传统降噪/音质赛道拥挤\n"健康音频"增速远超整体'),
    ('③ Apple 已验证赛道', '$249+', '仅高端覆盖',
     'AirPods Pro 2 获 FDA\n临床级助听认证，但大众空白'),
    ('④ Z 世代健康焦虑', '+180%', '搜索增长',
     '年轻人从"被动修复"\n转向"主动预防"听力损伤'),
    ('⑤ 听力 App 缺硬件', '8000 万', '年下载量',
     '听力检测 App 需求旺盛\n但没有硬件闭环持续监测'),
]

for i, (title, big_num, unit, desc) in enumerate(signals):
    sx = 0.5 + i * 3.9
    sw = 3.6
    sh = 3.0
    draw_card(ax, sx, SEC_Y, sw, sh, edge=TECH_BLUE)
    ax.text(sx+sw/2, SEC_Y+sh-0.35, title, fontproperties=cnb(10), color=DEEP_BLUE, ha='center')
    ax.text(sx+sw/2, SEC_Y+sh-1.4, big_num, fontproperties=cnb(26), color=AMBER, ha='center')
    ax.text(sx+sw/2, SEC_Y+sh-1.95, unit, fontproperties=cn(10), color=GRAY, ha='center')
    ax.text(sx+sw/2, SEC_Y+0.55, desc, fontproperties=cn(8), color=DARK, ha='center', va='bottom')

# ============================================================
# 板块 3：竞品定位矩阵
# ============================================================
SEC_Y = 15.2
HEIGHT = 4.5
draw_section_header(ax, SEC_Y+HEIGHT-0.55, '03', '竞品定位：$100 预防级听力健康 = 真空地带', '没有品牌在平价区间提供预防性听力健康功能')

SCATTER_X, SCATTER_W = 0.5, 11.5
SCATTER_H = 3.5
draw_card(ax, SCATTER_X, SEC_Y, SCATTER_W, SCATTER_H)

px0, py0 = SCATTER_X+1.5, SEC_Y+0.7
pw, ph = 9.0, 2.2

for gy in [py0, py0+ph/2, py0+ph]:
    ax.plot([px0, px0+pw], [gy, gy], color=LIGHT_GRAY, lw=0.4, zorder=2)
for gx in [px0, px0+pw/3, px0+2*pw/3, px0+pw]:
    ax.plot([gx, gx], [py0, py0+ph], color=LIGHT_GRAY, lw=0.4, zorder=2)

ax.text(px0+pw/2, py0-0.4, '价格 ($)', fontproperties=cn(9), color=GRAY, ha='center')
ax.text(px0-0.75, py0+ph/2, '听力健康深度', fontproperties=cn(9), color=GRAY, va='center', rotation=90)
for tx, tl in [(px0, '50'), (px0+pw, '350'), (px0+pw/3, '150'), (px0+2*pw/3, '250')]:
    ax.text(tx, py0-0.18, tl, fontproperties=cn(7), color=LIGHT_GRAY, ha='center')
ax.text(px0-0.35, py0, '无', fontproperties=cn(7), color=LIGHT_GRAY, ha='right', va='center')
ax.text(px0-0.35, py0+ph, '临床级', fontproperties=cn(7), color=LIGHT_GRAY, ha='right', va='center')

competitors = [
    (50, 0.05, '杂牌耳机', GRAY),
    (279, 0.05, 'Sony WF', GRAY),
    (199, 0.2, 'Samsung Buds', LIGHT_GRAY),
    (249, 0.95, 'Apple AirPods Pro 2', DARK),
    (350, 0.9, 'Bose QC Ultra', GRAY),
    (99, 0.55, 'Soundcore Guard', TECH_BLUE),
]
for price, depth, name, color in competitors:
    cx = px0 + (price-30)/340 * pw
    cy = py0 + depth * ph
    msize = 400 if name == 'Soundcore Guard' else 120
    ax.scatter(cx, cy, s=msize, c=color, zorder=5, edgecolors=WHITE, linewidths=1)
    ax.text(cx, cy+ph*0.13, name, fontproperties=cnb(8) if name == 'Soundcore Guard' else cn(7),
            ha='center', va='bottom', color=color)

ax.annotate('★ 空白地带\n$100 预防级\n听力健康', xy=(px0+(99-30)/340*pw, py0+0.55*ph), xytext=(px0+pw*0.55, py0+ph*0.75),
            fontproperties=cnb(9), color=GREEN, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=WHITE, edgecolor=GREEN, alpha=0.95),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

# 右侧洞察
INSIGHT_X = SCATTER_X + SCATTER_W + 0.5
INSIGHT_W = 7.5
draw_card(ax, INSIGHT_X, SEC_Y, INSIGHT_W, SCATTER_H, edge=TECH_BLUE)
ax.text(INSIGHT_X+0.25, SEC_Y+SCATTER_H-0.35, '关键洞察', fontproperties=cnb(13), color=DEEP_BLUE)
insights = [
    ('市场格局', '高端市场已被 Apple/Sony 占据\n中低端全是纯音频功能竞争'),
    ('核心发现', '$100 价位没有"预防性听力健康"产品\n这是被所有人忽略的空白地带'),
    ('Soundcore 优势', '安克供应链成本优势\n可做到 $99 售价 + 60% 毛利率'),
]
for j, (label, text) in enumerate(insights):
    iy = SEC_Y+SCATTER_H-0.9 - j*1.05
    ax.text(INSIGHT_X+0.25, iy, f'· {label}', fontproperties=cnb(9), color=AMBER)
    ax.text(INSIGHT_X+0.25, iy-0.32, text, fontproperties=cn(8.5), color=DARK)

# ============================================================
# 板块 4：用户洞察
# ============================================================
SEC_Y = 10.6
HEIGHT = 4.5
draw_section_header(ax, SEC_Y+HEIGHT-0.55, '04', '用户洞察：AI 模拟 500 人大规模调研', '联合分析 + 6 类用户替身对抗式验证 -> 定价锚点 = $99')

LEFT_W = 11.5
draw_card(ax, 0.5, SEC_Y, LEFT_W, 3.5, edge=TECH_BLUE)
ax.text(0.8, SEC_Y+3.2, '付费意愿分布（Conjoint Analysis 模拟）', fontproperties=cnb(11), color=DEEP_BLUE)

prices = ['$49', '$79', '$99', '$129', '$159', '$199']
overall = [22, 45, 54, 35, 18, 8]
hearing = [12, 38, 68, 48, 25, 10]

bars_y0 = SEC_Y+0.7
bars_h = 2.0
bars_scale = bars_h / 75
for i in range(len(prices)):
    bx = 1.0 + i * 1.85
    oh = overall[i] * bars_scale
    rect = FancyBboxPatch((bx, bars_y0), 0.65, oh, boxstyle="round,pad=0.03",
                          facecolor=LIGHT_BLUE, edgecolor=TECH_BLUE, linewidth=0.5, alpha=0.85, zorder=2)
    ax.add_patch(rect)
    ax.text(bx+0.32, bars_y0+oh+0.05, f'{overall[i]}%', fontproperties=cnb(8), color=TECH_BLUE, ha='center')
    hh = hearing[i] * bars_scale
    rect2 = FancyBboxPatch((bx+0.7, bars_y0), 0.65, hh, boxstyle="round,pad=0.03",
                           facecolor=AMBER, edgecolor=AMBER, linewidth=0.5, alpha=0.7, zorder=2)
    ax.add_patch(rect2)
    ax.text(bx+1.02, bars_y0+hh+0.05, f'{hearing[i]}%', fontproperties=cnb(8), color=AMBER, ha='center')
    ax.text(bx+0.67, bars_y0-0.15, prices[i], fontproperties=cnb(9), color=DARK, ha='center')

ax.text(1.0, bars_y0+bars_h+0.25, '■ 全部用户', fontproperties=cn(8), color=TECH_BLUE)
ax.text(3.5, bars_y0+bars_h+0.25, '■ 听力焦虑用户', fontproperties=cn(8), color=AMBER)

sweet_x = 1.0 + 2*1.85 + 0.67
sweet_y = bars_y0 + hearing[2]*bars_scale
ax.annotate('Sweet Spot\n$99 -> 68%', xy=(sweet_x, sweet_y), xytext=(sweet_x+1.8, bars_y0+bars_h*0.75),
            fontproperties=cnb(9), color=GREEN, ha='center',
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=1.5))

# 右侧 NPS
RIGHT_X = 0.5 + LEFT_W + 0.5
RIGHT_W = 7.5
draw_card(ax, RIGHT_X, SEC_Y, RIGHT_W, 3.5, edge=TECH_BLUE)
ax.text(RIGHT_X+0.25, SEC_Y+3.2, 'NPS 按用户分群', fontproperties=cnb(11), color=DEEP_BLUE)

segments = ['银发子女', '听力焦虑者', '通勤族', '游戏玩家', '学生', '隐私敏感']
nps_vals = [72, 68, 51, 35, 28, 15]
nps_colors = [GREEN if v>=50 else AMBER if v>=30 else ORANGE for v in nps_vals]
for i, (seg, val, col) in enumerate(zip(segments, nps_vals, nps_colors)):
    sy = SEC_Y + 2.75 - i * 0.45
    ax.text(RIGHT_X+0.25, sy, seg, fontproperties=cn(8.5), color=DARK, va='center')
    bar_rect = FancyBboxPatch((RIGHT_X+1.8, sy-0.13), val/100*5.0, 0.26,
                              boxstyle="round,pad=0.02", facecolor=col, alpha=0.85, zorder=2)
    ax.add_patch(bar_rect)
    ax.text(RIGHT_X+1.8+val/100*5.0+0.15, sy, f'{val}', fontproperties=cnb(9), color=col, va='center')

ax.text(RIGHT_X+0.25, SEC_Y+0.25, '· 核心发现：用户不要助听器，他们要"不戴助听器的安全感"',
        fontproperties=cnb(8.5), color=DEEP_BLUE)

# ============================================================
# 板块 5：技术架构
# ============================================================
SEC_Y = 5.9
HEIGHT = 4.2
draw_section_header(ax, SEC_Y+HEIGHT-0.55, '05', '技术架构：Thus AI Chip + 三层推理', '本地 AI 推理保障隐私，云端持续学习形成数据飞轮')

layers = [
    ('感知层', ['双麦阵列 + 骨传导', 'PPG 心率 + 血氧', 'IMU 运动姿态', 'SPL 实时监测'], LIGHT_BLUE),
    ('推理层', ['Thus AI 芯片', '本地推理 <50ms', '功耗 <5mW', '片上听力模型'], TECH_BLUE),
    ('应用层', ['个性化听力报告', '安全音量建议', '环境噪声预警', '云端飞轮训练'], DEEP_BLUE),
]
for li, (layer_name, items, color) in enumerate(layers):
    lx = 0.5 + li * 6.5
    lw = 6.0
    lh = 2.0
    ly = SEC_Y + 1.0
    draw_card(ax, lx, ly, lw, lh, edge=color)
    ax.add_patch(FancyBboxPatch((lx, ly+lh-0.4), lw, 0.4,
                 boxstyle="round,pad=0.02", facecolor=color, edgecolor=color, zorder=2))
    ax.text(lx+lw/2, ly+lh-0.2, layer_name, fontproperties=cnb(11), color=WHITE, ha='center', va='center')
    for ii, item in enumerate(items):
        ix = lx + 0.2 + (ii % 2) * (lw/2)
        iy = ly+lh - 0.75 - (ii // 2) * 0.55
        ax.text(ix, iy, f'· {item}', fontproperties=cn(8.5), color=DARK)
    if li < len(layers)-1:
        ax.annotate('', xy=(lx+lw+0.35, ly+lh/2), xytext=(lx+lw, ly+lh/2),
                    arrowprops=dict(arrowstyle='->', color=GRAY, lw=2))

# 技术指标
metrics_data = [
    ('<5 mW', '芯片功耗', TECH_BLUE),
    ('<50 ms', '推理延迟', TECH_BLUE),
    ('本地推理', '隐私保护', GREEN),
    ('24/7', '持续监测', TECH_BLUE),
    ('60%+', '毛利率', GREEN),
]
for mi, (val, label, col) in enumerate(metrics_data):
    mx = 0.6 + mi * 3.9
    draw_metric_card(ax, mx, SEC_Y-0.5, 3.5, 1.3, val, label, col)

# ============================================================
# 板块 6：商业飞轮
# ============================================================
SEC_Y = 2.1
HEIGHT = 3.6
draw_section_header(ax, SEC_Y+HEIGHT-0.55, '06', '商业飞轮：数据即护城河', '越多人使用 -> 听力模型越精准 -> 产品价值越高 -> 越多人选择')

# 左侧飞轮 - 横向四步骤
FLY_X, FLY_W = 0.5, 8.5
FLY_H = 1.8
FLY_Y = SEC_Y + 0.5
draw_card(ax, FLY_X, FLY_Y, FLY_W, FLY_H, edge=TECH_BLUE)

fly_steps = [
    ('用户佩戴', '持续积累'),
    ('听力数据', '每日百万级'),
    ('AI 模型', '精度提升'),
    ('个性化守护', '口碑传播'),
]
fly_cols = [LIGHT_BLUE, TECH_BLUE, DEEP_BLUE, GREEN]
box_w = 1.8
for i, ((title, sub), col) in enumerate(zip(fly_steps, fly_cols)):
    bx = FLY_X + 0.3 + i * (box_w + 0.25)
    draw_card(ax, bx, FLY_Y+0.2, box_w, 1.35, color=col, edge=col)
    ax.text(bx+box_w/2, FLY_Y+0.95, title, fontproperties=cnb(9), color=WHITE, ha='center', va='center')
    ax.text(bx+box_w/2, FLY_Y+0.5, sub, fontproperties=cn(7.5), color=WHITE, ha='center', va='center')
    if i < len(fly_steps)-1:
        ax.annotate('', xy=(bx+box_w+0.25, FLY_Y+0.875), xytext=(bx+box_w, FLY_Y+0.875),
                    arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.5))

# 右侧财务预测
FIN_X = FLY_X + FLY_W + 0.5
FIN_W = 10.5
FIN_Y = SEC_Y + 0.5
FIN_H = 1.8
draw_card(ax, FIN_X, FIN_Y, FIN_W, FIN_H, edge=TECH_BLUE)
ax.text(FIN_X+0.25, FIN_Y+FIN_H-0.3, '财务模型摘要', fontproperties=cnb(11), color=DEEP_BLUE)
fin_items = [
    ('BOM 成本', '$32–42', '芯片+声学+电池+结构'),
    ('定价', '$99–129', '2.5-3x 成本倍率'),
    ('毛利率', '60%+', '硬件利润健康'),
    ('Year 1', '50 万台', '收入 $50-65M'),
    ('Year 3', '500 万台', '收入 $500M+'),
    ('LTV/CAC', '10.4x', '口碑驱动低获客'),
]
for fi, (label, val, note) in enumerate(fin_items):
    col_idx = fi // 3
    row_idx = fi % 3
    col_x = FIN_X + 0.3 + col_idx * 5.2
    row_y = FIN_Y + FIN_H - 0.55 - row_idx * 0.48
    ax.text(col_x, row_y, label, fontproperties=cnb(8.5), color=DARK)
    ax.text(col_x+1.5, row_y, val, fontproperties=cnb(9), color=TECH_BLUE)
    ax.text(col_x+2.8, row_y, note, fontproperties=cn(7), color=GRAY)

# ============================================================
# 底部结论栏
# ============================================================
ax.add_patch(plt.Rectangle((0, 0), FIG_W, 0.45, facecolor=DEEP_BLUE, zorder=3))
ax.text(FIG_W/2, 0.22, '用 AI 原生产品设计方法，把创新从「猜」变成了「发现」—— 传统方法产出参数竞赛，AI 方法产出品类定义',
        fontproperties=cnb(9), color=WHITE, ha='center', va='center')

# ============================================================
# 保存
# ============================================================
output_path = '/workspace/soundcore-guard-ai-design/assets/charts/soundcore-guard-poster.png'
fig.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=BG, edgecolor='none')
plt.close(fig)

import os
size_kb = os.path.getsize(output_path) / 1024
print(f'✅ 海报已生成\n   路径: {output_path}\n   大小: {size_kb:.0f} KB')
