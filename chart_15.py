# -*- coding: utf-8 -*-
"""
图15: 水球图
水球图：完成率65%，蓝色圆圈+水波填充效果
中心显示"65%"
背景: 深藏青色 #1A1E43, 文字: 白色
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = 'charts_output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ========== 数据 ==========
completion = 0.65

# ========== 绘图 ==========
fig, ax = plt.subplots(figsize=(10, 8))
fig.patch.set_facecolor('#1A1E43')
ax.set_facecolor('#1A1E43')

# 水球图参数
cx, cy = 0.5, 0.45  # 圆心
radius = 0.25       # 半径

# 水面高度（从底部开始计算）
water_level = cy - radius + 2 * radius * completion

# 1. 画蓝色填充圆（水球内部）
water_circle = Circle((cx, cy), radius, facecolor='#0070C0', edgecolor='none', zorder=2)
ax.add_patch(water_circle)

# 2. 用背景色矩形覆盖水面以上部分
cover = Rectangle((cx - radius - 0.01, water_level), 2 * radius + 0.02, radius + 0.01,
                  facecolor='#1A1E43', edgecolor='none', zorder=3)
ax.add_patch(cover)

# 3. 画水波效果（水面波浪线）
x_wave = np.linspace(cx - radius, cx + radius, 200)
y_wave1 = water_level + 0.008 * np.sin(20 * (x_wave - cx) * np.pi)
y_wave2 = water_level + 0.005 * np.sin(25 * (x_wave - cx) * np.pi + 1) - 0.005
mask1 = (x_wave - cx)**2 + (y_wave1 - cy)**2 <= radius**2
mask2 = (x_wave - cx)**2 + (y_wave2 - cy)**2 <= radius**2
ax.plot(x_wave[mask1], y_wave1[mask1], color='#82ADD7', linewidth=1.5, alpha=0.8, zorder=4)
ax.plot(x_wave[mask2], y_wave2[mask2], color='#82ADD7', linewidth=1, alpha=0.5, zorder=4)

# 4. 画圆圈边框（外圈）
outer_circle = Circle((cx, cy), radius, fill=False, edgecolor='#0070C0', linewidth=2.5, zorder=5)
ax.add_patch(outer_circle)

# 5. 中心文字
ax.text(cx, cy, '65%', ha='center', va='center', fontsize=40, fontweight='bold',
        color='white', zorder=6)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# ========== 文字标注 ==========
fig.text(0.05, 0.93, '2022年上半年目标完成率', fontsize=20, fontweight='bold',
         color='white', ha='left', va='top')
fig.text(0.05, 0.88, '截至6月30日销售目标总体完成率达到65%',
         fontsize=14, color='white', ha='left', va='top')
fig.text(0.05, 0.03, '*注：数据来源于公司销售系统',
         fontsize=8, color='white', ha='left', va='bottom')

plt.subplots_adjust(left=0.05, right=0.95, top=0.83, bottom=0.05)

save_path = os.path.join(OUTPUT_DIR, '15_水球图.png')
plt.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='#1A1E43')
print(f"图片已保存至: {os.path.abspath(save_path)}")

plt.show()
plt.close()
