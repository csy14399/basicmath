"""
Pascal 三角形与二项式系数可视化

生成 Part 7 Chapter 3 所需的两张图：
  1. Pascal 三角形 (p07-ch03-pascal-triangle.png)
  2. 二项式系数可视化 (p07-ch03-binomial-coefficients.png)
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from math import comb

_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

ABS_OUT = "/workspace/basicmath/images/code-generated"
os.makedirs(ABS_OUT, exist_ok=True)
DPI = 200


def plot_pascal_triangle():
    """Pascal 三角形的前 10 行"""
    n_rows = 10
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.axis("off")
    ax.set_title("Pascal 三角形（杨辉三角）前 10 行",
                 fontsize=15, fontweight="bold", pad=15)

    max_val = comb(n_rows - 1, (n_rows - 1) // 2)
    cmap = plt.cm.YlOrRd

    for n in range(n_rows):
        for k in range(n + 1):
            x = k - n / 2
            y = -n
            val = comb(n, k)
            intensity = val / max_val if max_val > 0 else 0
            color = cmap(0.15 + 0.7 * intensity)
            circle = plt.Circle((x, y), 0.42, fc=color, ec="#7f8c8d",
                                 lw=1, alpha=0.9)
            ax.add_patch(circle)
            fontsize = 11 if val < 100 else (9 if val < 1000 else 7)
            ax.text(x, y, str(val), fontsize=fontsize, ha="center",
                    va="center", fontweight="bold",
                    color="white" if intensity > 0.5 else "#2c3e50")

    ax.set_xlim(-(n_rows) / 2 - 0.8, (n_rows) / 2 + 0.8)
    ax.set_ylim(-n_rows + 0.2, 1.2)
    ax.set_aspect("equal")

    ax.text(0, 0.85, "$n = 0$", fontsize=9, ha="center", color="#7f8c8d")
    ax.text(-(n_rows - 1) / 2 - 0.9, -(n_rows - 1),
            f"$n = {n_rows - 1}$", fontsize=9, ha="right", color="#7f8c8d")

    props = [
        "$\\binom{n}{k} = \\binom{n-1}{k-1} + \\binom{n-1}{k}$  (Pascal 恒等式)",
        "每行之和 $= 2^n$",
        "左右对称 $\\binom{n}{k} = \\binom{n}{n-k}$",
    ]
    for i, p in enumerate(props):
        ax.text((n_rows) / 2 + 0.5, -1.5 - i * 0.9, p,
                fontsize=10, ha="left", va="center", color="#34495e")

    plt.tight_layout()
    path = os.path.join(ABS_OUT, "p07-ch03-pascal-triangle.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  ✓ {path}")


def plot_binomial_coefficients():
    """二项式系数 C(n,k) 的可视化：柱状图 + 二项式定理"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: bar chart of C(n,k) for several n
    ax = axes[0]
    ax.set_title("$\\binom{n}{k}$ 的分布", fontsize=13, fontweight="bold")

    ns = [4, 6, 8, 10]
    colors = ["#3498db", "#e74c3c", "#2ecc71", "#9b59b6"]
    width = 0.18

    for idx, n in enumerate(ns):
        ks = list(range(n + 1))
        vals = [comb(n, k) for k in ks]
        offset = (idx - 1.5) * width
        bars = ax.bar([k + offset for k in ks], vals, width=width,
                      label=f"$n = {n}$", color=colors[idx], alpha=0.8,
                      edgecolor="white", linewidth=0.5)

    ax.set_xlabel("$k$", fontsize=12)
    ax.set_ylabel("$\\binom{n}{k}$", fontsize=12)
    ax.legend(fontsize=10, loc="upper right")
    ax.set_xticks(range(11))
    ax.grid(axis="y", alpha=0.3)

    # Right: (1+x)^n curves
    ax = axes[1]
    ax.set_title("$(1+x)^n$ 的图像", fontsize=13, fontweight="bold")

    x = np.linspace(-0.8, 1.5, 300)
    for idx, n in enumerate(ns):
        y = (1 + x) ** n
        ax.plot(x, y, color=colors[idx], lw=2, label=f"$n = {n}$")

    ax.axhline(y=0, color="#bdc3c7", lw=0.8)
    ax.axvline(x=0, color="#bdc3c7", lw=0.8)
    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$(1+x)^n$", fontsize=12)
    ax.legend(fontsize=10)
    ax.set_ylim(-1, 8)
    ax.grid(alpha=0.3)

    ax.annotate("$x=0$: 所有曲线经过 $(0, 1)$",
                xy=(0, 1), xytext=(0.4, 3),
                fontsize=9, color="#2c3e50",
                arrowprops=dict(arrowstyle="->", color="#7f8c8d"))

    plt.tight_layout()
    path = os.path.join(ABS_OUT, "p07-ch03-binomial-coefficients.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  ✓ {path}")


if __name__ == "__main__":
    print("生成 Part 7 Ch03 图片...")
    plot_pascal_triangle()
    plot_binomial_coefficients()
    print("完成！")
