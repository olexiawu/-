# -*- coding: utf-8 -*-
"""
图14: 单值圆环图
圆环图：完成率85%(紫色#7030A0) + 占位15%(灰色)
中心显示"85%"和"目标完成率"
背景: 深藏青色 #1A1E43, 文字: 白色
"""
import matplotlib.pyplot as plt
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

OUTPUT_DIR = 'charts_output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ========== 数据 ==========
completion = 0.85
placeholder = 0.15

# ========== 绘图 ==========
fig, ax = plt.subplots(figsize=(10, 8))
fig.patch.set_facecolor('#1A1E43')
ax.set_facecolor('#1A1E43')

# 圆环图
sizes = [completion, placeholder]
colors = ['#7030A0', '#3D3D5C']  # 紫色 + 深灰(背景融合色)
ax.pie(sizes, colors=colors, startangle=90, counterclock=False,
       wedgeprops=dict(width=0.1, edgecolor='#1A1E43', linewidth=2),
       radius=1.0)

# 中心文字
ax.text(0, 0.05, '85%', ha='center', va='center', fontsize=36, fontweight='bold', color='white')
ax.text(0, -0.12, '目标完成率', ha='center', va='center', fontsize=11, color='white')

ax.set_aspect('equal')

# ========== 文字标注 ==========
fig.text(0.05, 0.93, '2022年上半年目标完成率', fontsize=18, fontweight='bold',
         color='white', ha='left', va='top')
fig.text(0.05, 0.88, '截至6月30日销售目标总体完成率达到85%',
         fontsize=12, color='white', ha='left', va='top')
fig.text(0.05, 0.03, '*注：数据来源于公司销售系统',
         fontsize=8, color='white', ha='left', va='bottom')

plt.subplots_adjust(left=0.05, right=0.95, top=0.83, bottom=0.05)

save_path = os.path.join(OUTPUT_DIR, '14_单值圆环图.png')
plt.savefig(save_path, dpi=150, bbox_inches='tight', facecolor='#1A1E43')
print(f"图片已保存至: {os.path.abspath(save_path)}")

plt.show()
plt.close()
