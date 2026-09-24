# -*- coding: utf-8 -*-
"""
图10: 甘特图
水平堆叠柱形图：开始日期(透明占位) + 项目天数(蓝色)
背景: 深藏青色 #1A1E43, 文字: 白色
"""
import matplotlib.pyplot as plt
import datetime
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = 'charts_output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ========== 数据 ==========
projects = ['制定计划', '方案设计', '资源调配', '第一阶段', '第二阶段', '第三阶段', '项目总结']
start_dates = [
    datetime.date(2022, 3, 1),  datetime.date(2022, 3, 13), datetime.date(2022, 3, 22),
    datetime.date(2022, 4, 2),  datetime.date(2022, 4, 16), datetime.date(2022, 5, 11),
    datetime.date(2022, 5, 26)
]
durations = [11, 8, 10, 13, 24, 14, 7]

# 转换为相对于最早日期的天数
base_date = min(start_dates)
start_offsets = [(d - base_date).days for d in start_dates]

# ========== 绘图 ==========
fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('#1A1E43')
ax.set_facecolor('#1A1E43')

y_pos = np.arange(len(projects))

# 透明占位（开始日期偏移）+ 蓝色项目天数
ax.barh(y_pos, start_offsets, color='none', edgecolor='none', height=0.5)
ax.barh(y_pos, durations, left=start_offsets, color='#0070C0', edgecolor='none', height=0.5)

# 数据标签：在蓝色柱子中间显示天数
for i, (offset, dur) in enumerate(zip(start_offsets, durations)):
    ax.text(offset + dur / 2, i, f'{dur}天', ha='center', va='center',
            color='white', fontsize=10, fontweight='bold')

# 坐标轴设置
ax.set_yticks(y_pos)
ax.set_yticklabels(projects, color='white', fontsize=11)
ax.invert_yaxis()

# X轴显示日期
max_day = max(s + d for s, d in zip(start_offsets, durations)) + 5
ax.set_xlim(0, max_day)
tick_days = list(range(0, int(max_day) + 1, 10))
tick_dates = [(base_date + datetime.timedelta(days=int(t))).strftime('%Y/%m/%d') for t in tick_days]
ax.set_xticks(tick_days)
ax.set_xticklabels(tick_dates, color='white', fontsize=9, rotation=30, ha='right')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('#FFFFFF')
ax.spines['left'].set_color('#FFFFFF')
ax.tick_params(axis='both', which='both', length=0)

# ========== 文字标注 ==========
fig.text(0.05, 0.93, '2022年化妆品类目采购项目进度', fontsize=16, fontweight='bold',
         color='white', ha='left', va='top')

plt.subplots_adjust(left=0.08, right=0.96, top=0.88, bottom=0.12)

save_path = os.path.join(OUTPUT_DIR, '10_甘特图.png')
plt.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='#1A1E43')
print(f"图片已保存至: {os.path.abspath(save_path)}")

plt.show()
plt.close()
