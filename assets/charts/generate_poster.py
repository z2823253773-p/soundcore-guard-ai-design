#!/usr/bin/env python3
"""
Soundcore Guard — AI 原生产品设计 · 竖版长图数据海报
宽 20 英寸 × 高 60 英寸，充分留白，标题统一，逻辑清晰
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
from matplotlib.font_manager import FontProperties
import numpy as np

# ============================================================
# 全局设计
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

CN_REG = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
CN_BLD = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'

def cn(size=11):
    return FontProperties(fname=CN_REG, size=size)

def cnb(size=11):
    return FontProperties(fname=CN_BLD, size=size)

FIG_W = 20
FIG_H = 58

# ============================================================
# 辅助函数
# ============================================================
def card(ax, x, y, w, h, edge=None, face=WHITE, z=1):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                         facecolor=face, edgecolor=edge or LIGHT_GRAY, linewidth=0.8, zorder=z)
    ax.add_patch(box)

def metric_card(ax, x, y, w, h, value, label, sub="", color=TECH_BLUE):
    card(ax, x, y, w, h, edge=color)
    ax.text(x+w/2, y+h*0.6, str(value), fontproperties=cnb(24), color=color, ha='center', va='center')
    ax.text(x+w/2, y+h*0.25, label, fontproperties=cn(10), color=DARK, ha='center', va='center')
    if sub:
        ax.text(x+w/2, y+h*0.06, sub, fontproperties=cn(8), color=GRAY, ha='center', va='center')

def section_header(ax, y, num, cn_title, en_subtitle):
    """统一标题样式：编号圆 + 中文大标题 + 英文副标题 + 分隔线"""
    cx = 1.5
    ax.add_patch(Circle((cx, y+0.55), 0.38, facecolor=DEEP_BLUE, zorder=3))
    ax.text(cx, y+0.55, str(num).zfill(2), fontproperties=cnb(14), color=WHITE, ha='center', va='center', zorder=4)
    ax.text(cx+0.7, y+0.65, cn_title, fontproperties=cnb(22), color=DEEP_BLUE, ha='left', va='center')
    ax.text(cx+0.7, y+0.15, en_subtitle, fontproperties=cn(11), color=GRAY, ha='left', va='center')
    ax.plot([1.5, FIG_W-1.5], [y-0.15, y-0.15], color=LIGHT_GRAY, lw=0.8, zorder=1)

def method_box(ax, x, y, w, h, title, product, nature, nature_color, price_text, decision_text, accent):
    card(ax, x, y, w, h, edge=accent)
    ax.add_patch(FancyBboxPatch((x, y+h-0.08), w, 0.08, boxstyle="round,pad=0.01",
                 facecolor=accent, edgecolor=accent, zorder=2))
    ax.text(x+0.25, y+h-0.5, title, fontproperties=cnb(15), color=accent)
    ax.text(x+0.25, y+h-1.05, product, fontproperties=cn(12), color=DARK)
    ax.text(x+0.25, y+h-1.55, nature, fontproperties=cnb(10), color=nature_color)
    ax.text(x+0.25, y+h-2.0, price_text, fontproperties=cn(9), color=GRAY)
    ax.text(x+0.25, y+h-2.45, decision_text, fontproperties=cn(9), color=GRAY)

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
# HEADER
# ============================================================
ax.add_patch(plt.Rectangle((0, 54.0), FIG_W, 4.0, facecolor=DEEP_BLUE, zorder=1))
ax.text(FIG_W/2, 57.5, 'SOUNDCORE × AI-NATIVE PRODUCT DESIGN', fontproperties=cnb(12), color=LIGHT_BLUE, ha='center', va='center')
ax.text(FIG_W/2, 56.8, '不止听歌——你的个人听觉管家', fontproperties=cnb(30), color=WHITE, ha='center', va='center')
ax.text(FIG_W/2, 56.1, 'AI 原生产品设计方法 × Soundcore Guard 预防性听力守护 TWS 耳机', fontproperties=cn(14), color=SKY_BLUE, ha='center', va='center')
# 关键数字
for i, (val, label) in enumerate([('5', 'AI 发现的市场信号'), ('500', '模拟用户调研样本'), ('$99', 'Sweet Spot 定价')]):
    mx = 3.5 + i * 6.5
    ax.text(mx, 55.3, val, fontproperties=cnb(20), color=AMBER, ha='center', va='center')
    ax.text(mx, 54.8, label, fontproperties=cn(9), color=SKY_BLUE, ha='center', va='center')

# ============================================================
# SECTION 01 — 核心命题
# ============================================================
SEC_Y = 48.0
section_header(ax, SEC_Y+5.8, 1, '核心命题：方法改变答案', '同一个命题，两种方法，两个完全不同的方案')

method_box(ax, 1.5, SEC_Y+0.8, 8.0, 4.5,
           '传统经验驱动方法',
           'Soundcore Pro\n更好的降噪 + AI 翻译',
           '本质：Me-too 跟随策略',
           RED,
           '定价 $149–179 | 差异化靠参数（可被追上）',
           '决策依据：PM 个人经验 + 竞品对标',
           LIGHT_GRAY)

method_box(ax, 10.5, SEC_Y+0.8, 8.0, 4.5,
           'AI 原生方法',
           'Soundcore Guard\n平价预防性听力守护',
           '本质：品类创新 —— 开拓新赛道',
           GREEN,
           '定价 $99–129 | 差异化靠数据飞轮（越用越准）',
           '决策依据：AI 智囊 → AI 用户替身 → AI 专家团',
           TECH_BLUE)

ax.text(9.5, SEC_Y+3.0, 'VS', fontproperties=cnb(16), color=GRAY, ha='center', va='center')

flow_y = SEC_Y - 1.0
steps = ['AI 智囊\n全网信号发现', 'AI 替身\n500 用户模拟', 'AI 专家\n可行性评估', '人类 PM\n裁决 + 压测', '产品\n方案输出']
for i, s in enumerate(steps):
    fx = 2.5 + i * 3.4
    card(ax, fx, flow_y, 2.8, 1.3, edge=TECH_BLUE, face=SKY_BLUE)
    ax.text(fx+1.4, flow_y+0.65, s, fontproperties=cnb(10), color=DEEP_BLUE, ha='center', va='center')
    if i < len(steps)-1:
        ax.annotate('', xy=(fx+3.0, flow_y+0.65), xytext=(fx+2.8, flow_y+0.65),
                    arrowprops=dict(arrowstyle='->', color=TECH_BLUE, lw=2))

# ============================================================
# SECTION 02 — 五大市场信号
# ============================================================
SEC_Y = 38.0
section_header(ax, SEC_Y+8.0, 2, '五大信号 → 被忽视的市场空白', 'AI 智囊从全网数据中发现的 5 个关键信号，传统经验方法全部遗漏')

signals = [
    ('① 全球听力危机', '12 亿', '人面临听力损失风险',
     'WHO 2024：全球 1/4 人口\n2050 年前将出现听力问题'),
    ('② 健康音频崛起', '23%', 'CAGR',
     '传统降噪/音质赛道拥挤\n"健康音频"增速远超整体'),
    ('③ Apple 验证赛道', '$249+', '仅高端覆盖',
     'AirPods Pro 2 获 FDA 助听认证\n大众 $100 价位完全空白'),
    ('④ Z 世代健康焦虑', '+180%', '搜索增长',
     '年轻人从"被动修复"转向\n"主动预防"听力损伤'),
    ('⑤ 听力 App 缺硬件', '8000 万', '年下载量',
     '听力检测 App 年下载 8000 万次\n纯软件无法持续监测'),
]

for i, (title, big_num, unit, desc) in enumerate(signals):
    sx = 1.0 + i * 3.8
    sw = 3.4
    sh = 5.8
    card(ax, sx, SEC_Y+0.3, sw, sh, edge=TECH_BLUE)
    ax.text(sx+sw/2, SEC_Y+sh-0.6, title, fontproperties=cnb(10), color=DEEP_BLUE, ha='center', va='center')
    ax.text(sx+sw/2, SEC_Y+sh-2.4, big_num, fontproperties=cnb(28), color=AMBER, ha='center', va='center')
    ax.text(sx+sw/2, SEC_Y+sh-3.0, unit, fontproperties=cn(11), color=GRAY, ha='center', va='center')
    ax.text(sx+sw/2, SEC_Y+1.2, desc, fontproperties=cn(9), color=DARK, ha='center', va='bottom')

# ============================================================
# SECTION 03 — 竞品定位矩阵
# ============================================================
SEC_Y = 29.0
section_header(ax, SEC_Y+8.0, 3, '竞品定位：$100 预防级听力健康 = 真空地带', '没有品牌在平价区间提供预防性听力健康功能')

sc_x, sc_w = 1.5, 13.0
sc_h = 6.0
card(ax, sc_x, SEC_Y+0.3, sc_w, sc_h)

px0, py0 = sc_x+2.0, SEC_Y+1.0
pw, ph = 10.0, 3.8

for gy in [py0, py0+ph/2, py0+ph]:
    ax.plot([px0, px0+pw], [gy, gy], color=LIGHT_GRAY, lw=0.3, zorder=2)
for gx in [px0, px0+pw/4, px0+2*pw/4, px0+3*pw/4, px0+pw]:
    ax.plot([gx, gx], [py0, py0+ph], color=LIGHT_GRAY, lw=0.3, zorder=2)

ax.text(px0+pw/2, py0-0.5, '价格 ($)', fontproperties=cn(11), color=GRAY, ha='center')
ax.text(px0-1.0, py0+ph/2, '听力健康深度', fontproperties=cn(11), color=GRAY, va='center', rotation=90)

for tx, tl in [(px0, '50'), (px0+pw/4, '125'), (px0+2*pw/4, '200'), (px0+3*pw/4, '275'), (px0+pw, '350')]:
    ax.text(tx, py0-0.2, tl, fontproperties=cn(8), color=LIGHT_GRAY, ha='center')
for ty, tl in [(py0, '无'), (py0+ph/2, '中等'), (py0+ph, '临床级')]:
    ax.text(px0-0.4, ty, tl, fontproperties=cn(8), color=LIGHT_GRAY, ha='right', va='center')

comps = [
    (50, 0.03, '杂牌耳机', GRAY),
    (279, 0.05, 'Sony WF', GRAY),
    (199, 0.2, 'Samsung Buds', GRAY),
    (249, 0.95, 'Apple AirPods Pro 2', DARK),
    (350, 0.9, 'Bose QC', GRAY),
    (99, 0.58, 'Soundcore Guard', TECH_BLUE),
]
for price, depth, name, color in comps:
    cx = px0 + (price-30)/340 * pw
    cy = py0 + depth * ph
    msize = 500 if 'Soundcore' in name else 150
    ax.scatter(cx, cy, s=msize, c=color, zorder=5, edgecolors=WHITE, linewidths=1.5)
    off_y = ph*0.14
    ax.text(cx, cy+off_y, name, fontproperties=cnb(9) if 'Soundcore' in name else cn(8),
            ha='center', va='bottom', color=color)

ax.annotate('★ 战略空白\n$100 预防级\n听力健康', xy=(px0+(99-30)/340*pw, py0+0.58*ph),
            xytext=(px0+pw*0.45, py0+ph*0.75),
            fontproperties=cnb(10), color=GREEN, ha='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor=WHITE, edgecolor=GREEN, alpha=0.95, linewidth=1.5),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))

ins_x = sc_x + sc_w + 0.5
ins_w = 5.0
card(ax, ins_x, SEC_Y+0.3, ins_w, sc_h, edge=TECH_BLUE)
ax.text(ins_x+0.3, SEC_Y+sc_h-0.5, '分析结论', fontproperties=cnb(14), color=DEEP_BLUE)
conclusions = [
    '高端市场：Apple/Sony 垄断\n$200+ 区间有临床功能',
    '中低端市场：纯音频竞争\n没有任何听力健康功能',
    '战略机会：$99–129 +\n预防级听力健康 = 蓝海',
]
for j, c in enumerate(conclusions):
    cy = SEC_Y+sc_h-1.2 - j*1.5
    ax.text(ins_x+0.3, cy, f'> {c}', fontproperties=cn(9), color=DARK)

# ============================================================
# SECTION 04 — 用户洞察
# ============================================================
SEC_Y = 20.0
section_header(ax, SEC_Y+8.0, 4, '用户洞察：AI 模拟 500 人大规模调研', '联合分析 + 6 类用户替身对抗式验证 → 定价锚点锁定 $99')

left_w = 11.5
card(ax, 1.5, SEC_Y+0.5, left_w, 6.0, edge=TECH_BLUE)
ax.text(1.8, SEC_Y+6.0, '付费意愿分布 — Conjoint Analysis 模拟', fontproperties=cnb(13), color=DEEP_BLUE)

prices = ['$49', '$79', '$99', '$129', '$159', '$199']
overall = [22, 45, 54, 35, 18, 8]
hearing = [12, 38, 68, 48, 25, 10]

bars_y0 = SEC_Y+1.2
bars_h = 4.0
bars_scale = bars_h / 75
for i in range(len(prices)):
    bx = 1.8 + i * 1.7
    oh = overall[i] * bars_scale
    ax.add_patch(FancyBboxPatch((bx, bars_y0), 0.6, oh, boxstyle="round,pad=0.03",
                  facecolor=LIGHT_BLUE, edgecolor=TECH_BLUE, linewidth=0.5, alpha=0.85, zorder=2))
    ax.text(bx+0.3, bars_y0+oh+0.08, f'{overall[i]}%', fontproperties=cnb(9), color=TECH_BLUE, ha='center')
    hh = hearing[i] * bars_scale
    ax.add_patch(FancyBboxPatch((bx+0.65, bars_y0), 0.6, hh, boxstyle="round,pad=0.03",
                  facecolor=AMBER, edgecolor=AMBER, linewidth=0.5, alpha=0.7, zorder=2))
    ax.text(bx+0.95, bars_y0+hh+0.08, f'{hearing[i]}%', fontproperties=cnb(9), color=AMBER, ha='center')
    ax.text(bx+0.6, bars_y0-0.2, prices[i], fontproperties=cnb(10), color=DARK, ha='center')

ax.text(2.0, bars_y0+bars_h+0.3, '■ 全部用户 (n=500)', fontproperties=cn(9), color=TECH_BLUE)
ax.text(5.5, bars_y0+bars_h+0.3, '■ 听力焦虑用户 (n=180)', fontproperties=cn(9), color=AMBER)

sweet_x = 1.8 + 2*1.7 + 0.6
sweet_y = bars_y0 + hearing[2]*bars_scale
ax.annotate('Sweet Spot\n$99 → 68% 购买意愿', xy=(sweet_x, sweet_y), xytext=(sweet_x+2.0, bars_y0+bars_h*0.7),
            fontproperties=cnb(10), color=GREEN, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=WHITE, edgecolor=GREEN),
            arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))

right_x = 1.5 + left_w + 0.5
right_w = 6.5
card(ax, right_x, SEC_Y+0.5, right_w, 6.0, edge=TECH_BLUE)
ax.text(right_x+0.3, SEC_Y+6.0, 'NPS 净推荐值 — 按用户分群', fontproperties=cnb(13), color=DEEP_BLUE)

segments = ['银发子女', '听力焦虑者', '通勤族', '游戏玩家', '学生', '隐私敏感']
nps_vals = [72, 68, 51, 35, 28, 15]
nps_colors = [GREEN if v>=50 else AMBER if v>=30 else ORANGE for v in nps_vals]
for i, (seg, val, col) in enumerate(zip(segments, nps_vals, nps_colors)):
    sy = SEC_Y + 5.0 - i * 0.8
    ax.text(right_x+0.3, sy, seg, fontproperties=cn(10), color=DARK, va='center')
    bar_len = val / 100 * 4.8
    ax.add_patch(FancyBboxPatch((right_x+2.0, sy-0.15), bar_len, 0.35,
                  boxstyle="round,pad=0.03", facecolor=col, alpha=0.85, zorder=2))
    ax.text(right_x+2.0+bar_len+0.15, sy, f'{val}', fontproperties=cnb(10), color=col, va='center')

card(ax, right_x, SEC_Y+0.5, right_w, 0.6, face=SKY_BLUE, edge=TECH_BLUE)
ax.text(right_x+right_w/2, SEC_Y+0.8, '核心发现：用户不要"助听器"，他们要"不戴助听器的安全感"',
        fontproperties=cnb(9), color=DEEP_BLUE, ha='center', va='center')

# ============================================================
# SECTION 05 — 技术架构
# ============================================================
SEC_Y = 11.0
section_header(ax, SEC_Y+8.0, 5, '技术架构：Thus AI Chip + 三层推理系统', '本地 AI 推理保障隐私，云端持续学习形成数据飞轮护城河')

layers = [
    ('感知层', ['双麦阵列 + 骨传导传感器', 'PPG 心率 + 血氧监测', 'IMU 运动姿态感知', 'SPL 声压级实时监测'], LIGHT_BLUE, SKY_BLUE),
    ('推理层', ['Thus AI 专用芯片', '本地推理延迟 < 50ms', '芯片功耗 < 5mW', '片上听力评估模型'], TECH_BLUE, '#E3F2FD'),
    ('应用层', ['个性化听力健康报告', '安全音量实时建议', '环境噪声智能预警', '云端飞轮持续优化'], DEEP_BLUE, '#E8EAF6'),
]
for li, (layer_name, items, accent, fill) in enumerate(layers):
    lx = 1.5 + li * 6.0
    lw = 5.5
    lh = 4.5
    card(ax, lx, SEC_Y+0.8, lw, lh, edge=accent, face=fill)
    ax.add_patch(FancyBboxPatch((lx, SEC_Y+lh+0.2), lw, 0.6,
                 boxstyle="round,pad=0.02", facecolor=accent, edgecolor=accent, zorder=2))
    ax.text(lx+lw/2, SEC_Y+lh+0.5, layer_name, fontproperties=cnb(14), color=WHITE, ha='center', va='center')
    for ii, item in enumerate(items):
        ax.text(lx+0.3, SEC_Y+lh-0.3 - ii*0.75, f'> {item}', fontproperties=cn(10), color=DARK)
    if li < len(layers)-1:
        ax.annotate('', xy=(lx+lw+0.3, SEC_Y+lh/2+0.8), xytext=(lx+lw, SEC_Y+lh/2+0.8),
                    arrowprops=dict(arrowstyle='->', color=GRAY, lw=2.5))

metrics = [('< 5 mW', '芯片功耗', '超低功耗设计'), ('< 50 ms', '推理延迟', '实时本地响应'),
           ('本地推理', '隐私保护', '数据不出设备'), ('24/7', '持续监测', '全天候守护'),
           ('60%+', '毛利率', '健康商业模型')]
for mi, (val, label, sub) in enumerate(metrics):
    mx = 1.2 + mi * 3.8
    metric_card(ax, mx, SEC_Y-0.8, 3.3, 1.4, val, label, sub, color=TECH_BLUE)

# ============================================================
# SECTION 06 — 商业飞轮
# ============================================================
SEC_Y = 3.5
section_header(ax, SEC_Y+6.0, 6, '商业飞轮：数据即护城河', '越多人使用 → 听力模型越精准 → 产品价值越高 → 越多人选择')

fly_y = SEC_Y + 0.8
fly_steps = [('用户佩戴\n持续积累听力数据', LIGHT_BLUE), ('AI 模型\n精度持续提升', TECH_BLUE),
             ('个性化守护\n体验差异化', DEEP_BLUE), ('口碑传播\n获客成本趋零', GREEN)]
for i, (text, col) in enumerate(fly_steps):
    bx = 1.5 + i * 4.5
    bw = 3.8
    card(ax, bx, fly_y, bw, 1.8, edge=col, face=col)
    ax.text(bx+bw/2, fly_y+0.9, text, fontproperties=cnb(10), color=WHITE, ha='center', va='center')
    if i < len(fly_steps)-1:
        ax.annotate('', xy=(bx+bw+0.5, fly_y+0.9), xytext=(bx+bw, fly_y+0.9),
                    arrowprops=dict(arrowstyle='->', color=GRAY, lw=2))

# 财务摘要
fin_y = SEC_Y - 1.2
fin_data = [
    ('BOM 成本', '$32–42', '芯片+声学+电池'),
    ('零售定价', '$99–129', '2.5-3x 倍率'),
    ('毛利率', '60%+', '硬件利润健康'),
    ('Year 1', '50 万台', '收入 $50–65M'),
    ('Year 3', '500 万台', '收入 $500M+'),
    ('LTV/CAC', '10.4x', '口碑驱动增长'),
]
for fi, (label, val, note) in enumerate(fin_data):
    col = fi // 3
    row = fi % 3
    fx = 1.5 + col * 6.2
    fy = fin_y + 1.2 - row * 0.5
    ax.text(fx, fy, label, fontproperties=cnb(10), color=DARK)
    ax.text(fx+1.8, fy, val, fontproperties=cnb(12), color=TECH_BLUE)
    ax.text(fx+3.5, fy, note, fontproperties=cn(9), color=GRAY)

# ============================================================
# BOTTOM BAR — 结论
# ============================================================
ax.add_patch(plt.Rectangle((0, 0), FIG_W, 3.0, facecolor=DEEP_BLUE, zorder=1))
ax.text(FIG_W/2, 2.3, '结论', fontproperties=cnb(20), color=WHITE, ha='center', va='center')
ax.text(FIG_W/2, 1.6, '用 AI 原生产品设计方法，把创新从「猜」变成了「发现」', fontproperties=cnb(16), color=SKY_BLUE, ha='center', va='center')
ax.text(FIG_W/2, 0.8, '传统经验方法 → 参数竞赛（降噪多 3dB）\nAI 原生方法 → 品类定义（$100 听力守护新赛道，数据飞轮护城河）',
        fontproperties=cn(11), color=LIGHT_BLUE, ha='center', va='center')
ax.text(FIG_W-1.5, 0.25, 'Soundcore Guard — AI-Native Product Design — 2024', fontproperties=cn(8), color=LIGHT_BLUE, ha='right', va='center')

# ============================================================
# 保存
# ============================================================
output_path = '/workspace/soundcore-guard-ai-design/assets/charts/soundcore-guard-poster.png'
fig.savefig(output_path, dpi=200, facecolor=BG, edgecolor='none', pad_inches=0.3)
plt.close(fig)

import os
size_kb = os.path.getsize(output_path) / 1024
print(f'✅ 竖版长图海报已生成\n   路径: {output_path}\n   大小: {size_kb:.0f} KB')
print(f'   尺寸: {FIG_W}" × {FIG_H}" @ 150 DPI')
