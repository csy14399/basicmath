"""
计数原理可视化

生成 Part 7 Chapter 1 所需的两张图：
  1. 乘法原理树形图 (p07-ch01-multiplication-tree.png)
  2. 容斥原理 Venn 图 (p07-ch01-inclusion-exclusion-venn.png)
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import numpy as np

_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

ABS_OUT = "/workspace/basicmath/images/code-generated"
os.makedirs(ABS_OUT, exist_ok=True)
DPI = 200


def plot_multiplication_tree():
    """乘法原理树形图：3件上衣 × 2条裤子 = 6种搭配"""
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-0.5, 7)
    ax.axis("off")
    ax.set_title("乘法原理树形图：3 件上衣 × 2 条裤子 = 6 种搭配",
                 fontsize=14, fontweight="bold", pad=15)

    tops = ["红上衣", "蓝上衣", "白上衣"]
    bottoms = ["黑裤", "灰裤"]
    top_colors = ["#e74c3c", "#3498db", "#ecf0f1"]
    top_text_colors = ["white", "white", "black"]
    bottom_colors = ["#2c3e50", "#95a5a6"]

    root_x, root_y = 1.5, 6
    ax.annotate("选择", (root_x, root_y), fontsize=13, fontweight="bold",
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.4", fc="#f39c12", ec="none", alpha=0.9),
                color="white")

    top_positions = [(1.5, 4.2), (5, 4.2), (8.5, 4.2)]
    for i, (tx, ty) in enumerate(top_positions):
        ax.annotate("", xy=(tx, ty + 0.4), xytext=(root_x, root_y - 0.4),
                     arrowprops=dict(arrowstyle="->,head_width=0.15",
                                    color="#7f8c8d", lw=1.5))
        ax.annotate(tops[i], (tx, ty), fontsize=11, ha="center", va="center",
                     bbox=dict(boxstyle="round,pad=0.35", fc=top_colors[i],
                               ec="none", alpha=0.9),
                     color=top_text_colors[i], fontweight="bold")

        for j, bot in enumerate(bottoms):
            bx = tx - 0.8 + j * 1.6
            by = 2.2
            ax.annotate("", xy=(bx, by + 0.4), xytext=(tx, ty - 0.4),
                         arrowprops=dict(arrowstyle="->,head_width=0.12",
                                        color="#bdc3c7", lw=1.2))
            ax.annotate(bot, (bx, by), fontsize=10, ha="center", va="center",
                         bbox=dict(boxstyle="round,pad=0.3", fc=bottom_colors[j],
                                   ec="none", alpha=0.85),
                         color="white")

            result = f"({tops[i][:1]},{bot[:1]})"
            ax.annotate(result, (bx, 0.8), fontsize=9, ha="center", va="center",
                         bbox=dict(boxstyle="round,pad=0.25", fc="#27ae60",
                                   ec="none", alpha=0.8),
                         color="white")
            ax.annotate("", xy=(bx, 0.8 + 0.35), xytext=(bx, by - 0.35),
                         arrowprops=dict(arrowstyle="->,head_width=0.1",
                                        color="#bdc3c7", lw=1))

    ax.text(5, -0.1, "共 3 × 2 = 6 种搭配", fontsize=12, ha="center",
            style="italic", color="#2c3e50")

    plt.tight_layout()
    path = os.path.join(ABS_OUT, "p07-ch01-multiplication-tree.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  ✓ {path}")


def plot_inclusion_exclusion_venn():
    """容斥原理 Venn 图：|A∪B| = |A| + |B| - |A∩B|"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    for idx, ax in enumerate(axes):
        ax.set_xlim(-3.5, 3.5)
        ax.set_ylim(-2.5, 3)
        ax.set_aspect("equal")
        ax.axis("off")

    # Left panel: two-set inclusion-exclusion
    ax = axes[0]
    ax.set_title("两集合容斥原理", fontsize=13, fontweight="bold", pad=10)

    circle_a = plt.Circle((-0.7, 0), 1.5, fill=True, fc="#3498db",
                           ec="#2c3e50", lw=2, alpha=0.35)
    circle_b = plt.Circle((0.7, 0), 1.5, fill=True, fc="#e74c3c",
                           ec="#2c3e50", lw=2, alpha=0.35)
    ax.add_patch(circle_a)
    ax.add_patch(circle_b)

    ax.text(-1.5, 0, "$A$", fontsize=18, fontweight="bold", ha="center",
            va="center", color="#2980b9")
    ax.text(1.5, 0, "$B$", fontsize=18, fontweight="bold", ha="center",
            va="center", color="#c0392b")
    ax.text(0, 0, "$A \\cap B$", fontsize=12, ha="center", va="center",
            color="#8e44ad", fontweight="bold")
    ax.text(0, -2.2, "$|A \\cup B| = |A| + |B| - |A \\cap B|$",
            fontsize=13, ha="center", va="center", color="#2c3e50",
            bbox=dict(boxstyle="round,pad=0.3", fc="#f9e79f", ec="#f39c12"))

    # Right panel: three-set inclusion-exclusion
    ax = axes[1]
    ax.set_title("三集合容斥原理", fontsize=13, fontweight="bold", pad=10)

    r = 1.3
    offset = 0.65
    centers = [(0, offset), (-offset * np.sqrt(3) / 1.15, -offset * 0.5),
               (offset * np.sqrt(3) / 1.15, -offset * 0.5)]
    colors = ["#3498db", "#e74c3c", "#2ecc71"]
    labels = ["$A$", "$B$", "$C$"]
    label_offsets = [(0, 1.4), (-1.4, -0.8), (1.4, -0.8)]

    for i in range(3):
        circle = plt.Circle(centers[i], r, fill=True, fc=colors[i],
                             ec="#2c3e50", lw=2, alpha=0.25)
        ax.add_patch(circle)
        ax.text(centers[i][0] + label_offsets[i][0],
                centers[i][1] + label_offsets[i][1],
                labels[i], fontsize=16, fontweight="bold", ha="center",
                va="center", color=colors[i])

    formula = "$|A \\cup B \\cup C| = \\sum|\\cdot| - \\sum|\\cdot\\cap\\cdot| + |A\\cap B\\cap C|$"
    ax.text(0, -2.2, formula, fontsize=11, ha="center", va="center",
            color="#2c3e50",
            bbox=dict(boxstyle="round,pad=0.3", fc="#f9e79f", ec="#f39c12"))

    plt.tight_layout()
    path = os.path.join(ABS_OUT, "p07-ch01-inclusion-exclusion-venn.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  ✓ {path}")


if __name__ == "__main__":
    print("生成 Part 7 Ch01 图片...")
    plot_multiplication_tree()
    plot_inclusion_exclusion_venn()
    print("完成！")
