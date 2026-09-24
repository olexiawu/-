import matplotlib.pyplot as plt
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = 'charts_output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ========== 数据 ==========
products =  ['口红', '面膜', '隔离', '防晒', '精华']
sales_2021 = [3568, 4135, 4436, 4106, 4936]
sales_2022 = [2569, 3241, 2965, 3209, 3541]
diff =       [999,  894,  1471, 897,  1395]  # 差值 = 2021 - 2022

# ========== 绘图 ==========
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#1A1E43')
ax.set_facecolor('#1A1E43')

x = np.arange(len(products))
width = 0.35

bars1 = ax.bar(x - width/2, sales_2021, width, color='#0070C0', edgecolor='none', label='2021销量')
bars2 = ax.bar(x + width/2, sales_2022, width, color='#82ADD7', edgecolor='none', label='2022销量')

# 误差线：从2022柱子顶部向上延伸，显示差值
ax.errorbar(x + width/2, sales_2022, yerr=[np.zeros(len(diff)), diff],
            fmt='none', ecolor='white', capsize=0, lw=1.5, zorder=5)

# 差值标签（在误差线顶部）
for i, (d, s2) in enumerate(zip(diff, sales_2022)):
    ax.text(x[i] + width/2, s2 + d + 50, str(d), ha='center', va='bottom',
            fontsize=10, color='white', fontweight='bold')

# 数据标签：2021在柱子外侧顶部，2022在柱子内侧顶部
for bar in bars1:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h + 30,
            f'{int(h)}', ha='center', va='bottom', fontsize=9, color='white')
for bar in bars2:
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., h - 120,
            f'{int(h)}', ha='center', va='top', fontsize=9, color='white')

# 坐标轴设置
ax.set_xticks(x)
ax.set_xticklabels(products, color='white', fontsize=11)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#FFFFFF')
ax.tick_params(axis='y', which='both', left=False, labelleft=False)
ax.tick_params(axis='x', which='both', bottom=False)

# 图例
ax.legend(loc='lower right', frameon=False, fontsize=10, labelcolor='white')

# ========== 文字标注 ==========
fig.text(0.05, 0.93, '2022年商品对比去年销售情况', fontsize=20, fontweight='bold',
         color='white', ha='left', va='top')
fig.text(0.05, 0.88, '商品整体比去年销量有所下降，其中隔离下降最多，下降33%',
         fontsize=12, color='white', ha='left', va='top')
fig.text(0.05, 0.03, '*注：数据来源于公司销售系统，统计日期截至2022.01.01',
         fontsize=8, color='white', ha='left', va='bottom')

plt.subplots_adjust(left=0.06, right=0.96, top=0.83, bottom=0.08)

save_path = os.path.join(OUTPUT_DIR, '09_对比柱形图.png')
plt.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='#1A1E43')
print(f"图片已保存至: {os.path.abspath(save_path)}")

plt.show()
plt.close()
