"""
实数性质可视化

生成 Part 2 Chapter 2 所需的两张图：
  1. 区间套定理示意图
  2. 上确界与下确界示意图
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
ABS_OUT = "/workspace/basicmath/images/code-generated"
os.makedirs(ABS_OUT, exist_ok=True)

DPI = 200


# ═══════════════════════════════════════════
# 图 1: 区间套定理 (Nested Intervals Theorem)
# ═══════════════════════════════════════════
def plot_nested_intervals():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-1, 8)
    ax.axis("off")
    fig.suptitle("区间套定理 (Nested Intervals Theorem)", fontsize=15, fontweight="bold")

    c = np.sqrt(2)

    n_intervals = 7
    for k in range(n_intervals):
        a_k = c - 1.5 / (2 ** k)
        b_k = c + 1.5 / (2 ** k)
        y = n_intervals - k - 1

        ax.plot([a_k, b_k], [y, y], color="#3498db", lw=3, solid_capstyle="round")
        ax.plot(a_k, y, "o", color="#2c3e50", markersize=8, zorder=5)
        ax.plot(b_k, y, "o", color="#2c3e50", markersize=8, zorder=5)

        ax.text(a_k - 0.1, y, f"$a_{{{k+1}}}$", ha="right", va="center", fontsize=9,
                color="#2c3e50")
        ax.text(b_k + 0.1, y, f"$b_{{{k+1}}}$", ha="left", va="center", fontsize=9,
                color="#2c3e50")

        label = f"$[a_{{{k+1}}}, b_{{{k+1}}}]$"
        ax.text(4.2, y, label, va="center", fontsize=9, color="#7f8c8d")

    ax.plot(c, -0.5, "^", color="#e74c3c", markersize=14, zorder=10)
    ax.text(c, -0.9, "$c$ (唯一公共点)", ha="center", fontsize=11,
            color="#e74c3c", fontweight="bold")

    ax.plot([c, c], [-0.3, n_intervals - 0.7], "--", color="#e74c3c", alpha=0.5, lw=1)

    ax.text(0.0, 7.3,
            "条件: (i) 嵌套  (ii) $b_n - a_n \\to 0$\n"
            "结论: $\\bigcap [a_n, b_n] = \\{c\\}$",
            fontsize=11, va="top",
            bbox=dict(boxstyle="round,pad=0.5", fc="#eaf2f8", ec="#3498db", alpha=0.9))

    fname = "p02-ch02-nested-intervals.png"
    fig.savefig(os.path.join(ABS_OUT, fname), dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  已生成: {fname}")


# ═══════════════════════════════════════════
# 图 2: 上确界与下确界 (Supremum and Infimum)
# ═══════════════════════════════════════════
def plot_supremum_infimum():
    fig, axes = plt.subplots(2, 1, figsize=(12, 7))
    fig.suptitle("上确界与下确界 (Supremum & Infimum)", fontsize=15, fontweight="bold")

    # ── 例 1: S = {1 - 1/n : n >= 1} ──
    ax = axes[0]
    ax.set_xlim(-0.3, 1.5)
    ax.set_ylim(-0.8, 1.0)
    ax.axis("off")
    ax.set_title("$S = \\{1 - 1/n : n \\in \\mathbb{N}^+\\} = \\{0, 1/2, 2/3, 3/4, \\ldots\\}$",
                 fontsize=11)

    ax.annotate("", xy=(1.4, 0), xytext=(-0.2, 0),
                arrowprops=dict(arrowstyle="->", lw=1, color="#7f8c8d"))

    pts = [1 - 1/n for n in range(1, 16)]
    for p in pts:
        ax.plot(p, 0, "o", color="#3498db", markersize=6, zorder=5)

    ax.plot(0, 0, "o", color="#3498db", markersize=10, zorder=6)
    ax.text(0, -0.3, "$0 = \\inf S$\n(最小元素)", ha="center", fontsize=9, color="#27ae60")
    ax.plot(0, -0.15, "^", color="#27ae60", markersize=10, zorder=6)

    ax.plot(1, 0, "x", color="#e74c3c", markersize=12, markeredgewidth=2.5, zorder=6)
    ax.text(1, -0.3, "$1 = \\sup S$\n($1 \\notin S$)", ha="center", fontsize=9, color="#e74c3c")

    ax.annotate("趋近但不到达", xy=(0.92, 0.05), xytext=(0.7, 0.5),
                fontsize=9, color="#e74c3c",
                arrowprops=dict(arrowstyle="->", color="#e74c3c", lw=1))

    upper_bounds_x = [1.0, 1.1, 1.2, 1.3]
    for ub in upper_bounds_x:
        ax.plot(ub, 0.6, "v", color="#e67e22", markersize=7, alpha=0.6)
    ax.text(1.15, 0.8, "上界们", ha="center", fontsize=9, color="#e67e22")
    ax.annotate("sup = 最小上界", xy=(1.0, 0.55), xytext=(0.4, 0.75),
                fontsize=9, color="#e74c3c", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#e74c3c", lw=1))

    # ── 例 2: S = (0, 2) ──
    ax = axes[1]
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-0.8, 1.0)
    ax.axis("off")
    ax.set_title("$S = (0, 2)$ — 开区间", fontsize=11)

    ax.annotate("", xy=(3.3, 0), xytext=(-0.3, 0),
                arrowprops=dict(arrowstyle="->", lw=1, color="#7f8c8d"))

    x_fill = np.linspace(0.01, 1.99, 200)
    ax.fill_between(x_fill, -0.1, 0.1, color="#3498db", alpha=0.3)
    ax.plot([0.01, 1.99], [0, 0], color="#3498db", lw=3)

    ax.plot(0, 0, "o", color="#27ae60", markersize=10, mfc="white", mew=2, zorder=6)
    ax.text(0, -0.35, "$0 = \\inf S$\n($0 \\notin S$)", ha="center", fontsize=9, color="#27ae60")

    ax.plot(2, 0, "o", color="#e74c3c", markersize=10, mfc="white", mew=2, zorder=6)
    ax.text(2, -0.35, "$2 = \\sup S$\n($2 \\notin S$)", ha="center", fontsize=9, color="#e74c3c")

    ax.text(1, 0.5, "sup 和 inf 都不属于 $S$（开区间!）",
            ha="center", fontsize=10, style="italic", color="#7f8c8d",
            bbox=dict(boxstyle="round,pad=0.3", fc="#f9f9f9", ec="#bdc3c7"))

    plt.tight_layout()
    fname = "p02-ch02-supremum-infimum.png"
    fig.savefig(os.path.join(ABS_OUT, fname), dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  已生成: {fname}")


# ═══════════════════════════════════════════
if __name__ == "__main__":
    print("Part 2 Ch02 — 实数性质可视化")
    plot_nested_intervals()
    plot_supremum_infimum()
    print("全部完成！")
