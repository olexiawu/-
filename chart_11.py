# -*- coding: utf-8 -*-
"""
图11: 平滑折线图
平滑折线图：橙色线(#E66B4C)，仅第9个点(3782)显示数据标签
背景: 深藏青色 #1A1E43, 文字: 白色
"""
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = 'charts_output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ========== 数据 ==========
months = ['5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月', '1月', '2月', '3月']
sales =  [146,   198,   296,   412,   506,   615,    789,    1021,   3782,  3215,  2936]

# ========== 绘图 ==========
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#1A1E43')
ax.set_facecolor('#1A1E43')

x = np.arange(len(months))

# 平滑曲线 - 三次样条插值
x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = make_interp_spline(x, sales, k=3)(x_smooth)

ax.plot(x_smooth, y_smooth, color='#E66B4C', linewidth=2.5, solid_capstyle='round', zorder=3)
ax.plot(x, sales, 'o', color='#E66B4C', markersize=6, zorder=4)

# 仅第9个点(idx=8)显示数据标签
ax.annotate(f'{sales[8]}', xy=(x[8], sales[8]), xytext=(x[8], sales[8] + 350),
            ha='center', fontsize=12, fontweight='bold', color='white',
            arrowprops=dict(arrowstyle='->', color='white', lw=1.2))

# 坐标轴设置
ax.set_xticks(x)
ax.set_xticklabels(months, color='white', fontsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#FFFFFF')
ax.spines['left'].set_color('#FFFFFF')
ax.tick_params(axis='both', which='both', length=0)
ax.set_ylabel('销量', color='white', fontsize=11)
ax.tick_params(axis='y', colors='white')

# ========== 文字标注 ==========
fig.text(0.05, 0.93, '化妆品品类月度销量走势', fontsize=20, fontweight='bold',
         color='white', ha='left', va='top')
fig.text(0.05, 0.88, '2022年销量迅速增加，1月最高，销量达到3782',
         fontsize=14, color='white', ha='left', va='top')
fig.text(0.05, 0.03, '*注：数据来源于公司销售系统，统计日期截至2022.03.31',
         fontsize=8, color='white', ha='left', va='bottom')

# 年份标注
fig.text(0.35, 0.78, '2021', fontsize=10, color='white', ha='center')
fig.text(0.75, 0.78, '2022', fontsize=10, color='white', ha='center')

plt.subplots_adjust(left=0.08, right=0.96, top=0.83, bottom=0.08)

save_path = os.path.join(OUTPUT_DIR, '11_平滑折线图.png')
plt.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='#1A1E43')
print(f"图片已保存至: {os.path.abspath(save_path)}")

plt.show()
plt.close()
