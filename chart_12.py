# -*- coding: utf-8 -*-
"""
图12: 菱形走势图
折线图：菱形(diamond)标记，无可见连线，数据标签显示完成率
背景: 深藏青色 #1A1E43, 文字: 白色
"""
import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = 'charts_output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ========== 数据 ==========
months =     ['1月',  '2月',  '3月',  '4月',  '5月',  '6月',  '7月',  '8月']
completion = [0.536,  0.498,  0.527,  0.708,  0.609,  0.496,  0.586,  0.704]

# ========== 绘图 ==========
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#1A1E43')
ax.set_facecolor('#1A1E43')

x = np.arange(len(months))

# 菱形标记，无连线
ax.plot(x, completion, 'D', color='#0070C0', markersize=12,
        markeredgecolor='#0070C0', markerfacecolor='#0070C0', zorder=3)

# 数据标签显示在顶部
for xi, yi in zip(x, completion):
    ax.text(xi, yi + 0.025, f'{yi:.1%}', ha='center', va='bottom',
            fontsize=10, color='white')

# 坐标轴设置
ax.set_xticks(x)
ax.set_xticklabels(months, color='white', fontsize=11)
ax.set_ylim(0.4, 0.8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#FFFFFF')
ax.tick_params(axis='y', which='both', left=False, labelleft=False)
ax.tick_params(axis='x', which='both', bottom=False)

# ========== 文字标注 ==========
fig.text(0.05, 0.93, '2022年1-8月公司计划完成率', fontsize=20, fontweight='bold',
         color='white', ha='left', va='top')
fig.text(0.05, 0.88, '公司整体完成率55%，4月和8月超过70%，2月和6月较低未过半',
         fontsize=12, color='white', ha='left', va='top')
fig.text(0.05, 0.03, '*注：数据来源于公司销售系统，统计日期截至2022.08.31',
         fontsize=8, color='white', ha='left', va='bottom')

plt.subplots_adjust(left=0.06, right=0.96, top=0.83, bottom=0.08)

save_path = os.path.join(OUTPUT_DIR, '12_菱形走势图.png')
plt.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='#1A1E43')
print(f"图片已保存至: {os.path.abspath(save_path)}")

plt.show()
plt.close()
