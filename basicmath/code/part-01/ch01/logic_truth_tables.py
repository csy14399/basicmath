"""
逻辑联结词真值表可视化

生成五个基本联结词（否定、合取、析取、蕴含、双条件）的真值表，
以清晰的表格形式呈现，用于 Part 1 Chapter 1 的配图。
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# ── 配置中文字体 ──
_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

# ── 输出路径 ──
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REL_OUT = os.path.join(SCRIPT_DIR, "..", "..", "..", "images", "code-generated")
ABS_OUT = "/workspace/basicmath/images/code-generated"

for d in (REL_OUT, ABS_OUT):
    os.makedirs(d, exist_ok=True)

FILENAME = "p01-ch01-truth-table-connectives.png"

# ── 真值表数据 ──
# P 和 Q 的所有取值组合
P_vals = [True, True, False, False]
Q_vals = [True, False, True, False]

def fmt(v):
    """将布尔值格式化为 T/F"""
    return "T" if v else "F"

# 五个联结词的计算与标签
connectives = [
    {
        "name": "否定 (¬)",
        "symbol": "¬P",
        "cols": ["P", "¬P"],
        "rows": [[fmt(p), fmt(not p)] for p in P_vals],
        "unary": True,
    },
    {
        "name": "合取 (∧)",
        "symbol": "P ∧ Q",
        "cols": ["P", "Q", "P ∧ Q"],
        "rows": [[fmt(p), fmt(q), fmt(p and q)] for p, q in zip(P_vals, Q_vals)],
        "unary": False,
    },
    {
        "name": "析取 (∨)",
        "symbol": "P ∨ Q",
        "cols": ["P", "Q", "P ∨ Q"],
        "rows": [[fmt(p), fmt(q), fmt(p or q)] for p, q in zip(P_vals, Q_vals)],
        "unary": False,
    },
    {
        "name": "蕴含 (→)",
        "symbol": "P → Q",
        "cols": ["P", "Q", "P → Q"],
        # 蕴含：P → Q 仅在 P 为真且 Q 为假时为假
        "rows": [[fmt(p), fmt(q), fmt((not p) or q)] for p, q in zip(P_vals, Q_vals)],
        "unary": False,
    },
    {
        "name": "双条件 (↔)",
        "symbol": "P ↔ Q",
        "cols": ["P", "Q", "P ↔ Q"],
        # 双条件：P ↔ Q 在 P 和 Q 同真或同假时为真
        "rows": [[fmt(p), fmt(q), fmt(p == q)] for p, q in zip(P_vals, Q_vals)],
        "unary": False,
    },
]

# ── 绘图 ──
fig, axes = plt.subplots(1, 5, figsize=(18, 4.5))
fig.suptitle("逻辑联结词真值表 (Truth Tables for Logical Connectives)",
             fontsize=16, fontweight="bold", y=0.98)

for ax, conn in zip(axes, connectives):
    ax.set_axis_off()
    ax.set_title(conn["name"], fontsize=13, fontweight="bold", pad=12)

    n_cols = len(conn["cols"])
    n_rows = len(conn["rows"])

    table = ax.table(
        cellText=conn["rows"],
        colLabels=conn["cols"],
        loc="center",
        cellLoc="center",
    )

    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.0, 1.8)

    # 样式：表头加深
    for j in range(n_cols):
        cell = table[0, j]
        cell.set_facecolor("#2c3e50")
        cell.set_text_props(color="white", fontweight="bold", fontsize=12)

    # 数据行交替着色
    for i in range(1, n_rows + 1):
        for j in range(n_cols):
            cell = table[i, j]
            if i % 2 == 0:
                cell.set_facecolor("#ecf0f1")
            else:
                cell.set_facecolor("#ffffff")

            # 结果列（最后一列）用蓝色高亮 T，用灰色标记 F
            if j == n_cols - 1:
                val = conn["rows"][i - 1][j]
                if val == "T":
                    cell.set_text_props(color="#2980b9", fontweight="bold")
                else:
                    cell.set_text_props(color="#95a5a6")

plt.tight_layout(rect=[0, 0, 1, 0.92])

# 保存到两个路径
for out_dir in (REL_OUT, ABS_OUT):
    path = os.path.join(out_dir, FILENAME)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")

plt.close(fig)

print(f"已生成: {FILENAME}")
print(f"  相对路径: {os.path.join(REL_OUT, FILENAME)}")
print(f"  绝对路径: {os.path.join(ABS_OUT, FILENAME)}")
