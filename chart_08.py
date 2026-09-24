# -*- coding: utf-8 -*-
"""
图8: 数值百分比
水平堆叠柱形图：深蓝=销量，浅蓝=占位填充，红色=间隔(显示同比百分比)
背景: 深藏青色 #1A1E43, 文字: 白色

Excel样式细节:
- Series 0 (销量): #09387E, 数据标签 inEnd (深蓝段右端内侧), 10pt
- Series 1 (占位1): #82ADD7, 无标签
- Series 2 (占位2): #9B3D4F, 自定义标签(同比百分比) 居中, 10pt
- gapWidth=30, overlap=100
- 绘图区: x=0.127, y=0.281, w=0.817, h=0.609
- Y轴(数值)删除, X轴(类别)左侧显示, 9pt
"""
import matplotlib.pyplot as plt
import numpy as np
import os

# 中文字体设置
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 输出目录
OUTPUT_DIR = 'charts_output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ========== 数据 ==========
regions = ['华北', '华南', '东北', '西北', '西南', '华东']
sales =    [4321, 1946, 1536, 1872, 1369, 2109]
yoy =      [-0.136, -0.208, -0.093, -0.159, -0.179, -0.058]  # 同比去年

max_val = max(sales)                              # 4321
placeholder1 = [max_val - s for s in sales]       # 占位1 = MAX - 销量
placeholder2 = [max_val / 4] * len(sales)          # 占位2 = MAX / 4 = 1080.25

# ========== 绘图 ==========
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#1A1E43')
ax.set_facecolor('#1A1E43')

y_pos = np.arange(len(regions))

# 堆叠水平柱形图 (gapWidth=30 → 柱子较粗)
bar_height = 0.72
ax.barh(y_pos, sales, color='#09387E', edgecolor='none', height=bar_height)
ax.barh(y_pos, placeholder1, left=sales, color='#82ADD7', edgecolor='none', height=bar_height)
ax.barh(y_pos, placeholder2, left=[s + p for s, p in zip(sales, placeholder1)],
        color='#9B3D4F', edgecolor='none', height=bar_height)

# 数据标签：深蓝段右端内侧 (inEnd)，10pt白色
for i, (s, y) in enumerate(zip(sales, y_pos)):
    ax.text(s - 30, y, str(s), ha='right', va='center',
            color='white', fontsize=10, fontweight='bold')

# 红色间隔区域居中显示同比百分比 (ctr)，10pt白色
for i, (y, pct) in enumerate(zip(y_pos, yoy)):
    x_pos = max_val + placeholder2[i] / 2  # 红色段中心
    ax.text(x_pos, y, f'{pct:.1%}', ha='center', va='center',
            color='white', fontsize=10)

# X轴范围：留少量右边距
ax.set_xlim(0, max_val + placeholder2[0] + 50)

# 坐标轴设置
ax.set_yticks(y_pos)
ax.set_yticklabels(regions, color='white', fontsize=10)
ax.invert_yaxis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
ax.tick_params(axis='y', which='both', left=False, length=0)

# ========== 文字标注（匹配Excel绘图区比例） ==========
# Excel绘图区: x=0.127, y=0.281, w=0.817, h=0.609
# 标题在绘图区上方
fig.text(0.05, 0.95, '2021年各区域销量及同比情况', fontsize=18, fontweight='bold',
         color='white', ha='left', va='top')
# 描述在标题下方
fig.text(0.05, 0.89, '各区域商品销量同比去年均有下降，其中华南下降最多，同比下降20.8%',
         fontsize=11, color='white', ha='left', va='top')
# 脚注在底部
fig.text(0.05, 0.04, '*注：数据来源于公司销售系统，统计日期截至2022.01.01',
         fontsize=8, color='white', ha='left', va='bottom')

# 绘图区域边距（匹配Excel: x=0.127, y=0.281, w=0.817, h=0.609）
plt.subplots_adjust(left=0.07, right=0.96, top=0.82, bottom=0.10)

# 保存图片
save_path = os.path.join(OUTPUT_DIR, '08_数值百分比.png')
plt.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='#1A1E43')
print(f"图片已保存至: {os.path.abspath(save_path)}")

# 显示图表
plt.show()
plt.close()
