# -*- coding: utf-8 -*-
"""
图13: 对比折线图
双折线图：2021年(粉红#E74E69) vs 2022年(蓝色#0070C0)，圆形标记，选择性数据标签
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
months =     ['1月',  '2月',  '3月',  '4月',  '5月',  '6月']
data_2021 =  [1686,   1345,   1934,   1658,   1865,   1936]
data_2022 =  [1385,   1846,   1654,   1936,   2564,   2236]

# ========== 绘图 ==========
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#1A1E43')
ax.set_facecolor('#1A1E43')

x = np.arange(len(months))

# 2021年 - 粉红色线
ax.plot(x, data_2021, 'o-', color='#E74E69', linewidth=2.5, markersize=8, label='2021年', zorder=3)
# 2022年 - 蓝色线
ax.plot(x, data_2022, 'o-', color='#0070C0', linewidth=2.5, markersize=8, label='2022年', zorder=3)

# 2021年数据标签：索引1,3,4,5（位置右侧）
for idx in [1, 3, 4, 5]:
    ax.text(x[idx] + 0.12, data_2021[idx], f'{data_2021[idx]}', ha='left', va='center',
            fontsize=9, color='#E74E69')

# 2022年数据标签：索引0,2（位置右侧）
for idx in [0, 2]:
    ax.text(x[idx] + 0.12, data_2022[idx], f'{data_2022[idx]}', ha='left', va='center',
            fontsize=9, color='#0070C0')

# 坐标轴设置
ax.set_xticks(x)
ax.set_xticklabels(months, color='white', fontsize=11)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#FFFFFF')
ax.spines['left'].set_color('#FFFFFF')
ax.tick_params(axis='both', which='both', length=0)
ax.tick_params(axis='y', colors='white')

# 图例
ax.legend(loc='upper left', frameon=False, fontsize=11, labelcolor='white')

# ========== 文字标注 ==========
fig.text(0.05, 0.93, '2022年上半年各月同比去年销量', fontsize=20, fontweight='bold',
         color='white', ha='left', va='top')
fig.text(0.05, 0.88, '上半年同比去年增长明显，5月份同比增长最多，增长近40%',
         fontsize=12, color='white', ha='left', va='top')
fig.text(0.05, 0.03, '*注：数据来源于公司销售系统，统计日期截至2022.06.30',
         fontsize=8, color='white', ha='left', va='bottom')

plt.subplots_adjust(left=0.08, right=0.96, top=0.83, bottom=0.08)

save_path = os.path.join(OUTPUT_DIR, '13_对比折线图.png')
plt.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='#1A1E43')
print(f"图片已保存至: {os.path.abspath(save_path)}")

plt.show()
plt.close()
