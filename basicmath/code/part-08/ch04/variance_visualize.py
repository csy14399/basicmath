"""
方差比较可视化

生成 Part 8 Chapter 4 所需的图：
  p08-ch04-variance-comparison.png
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

ABS_OUT = "/workspace/basicmath/images/code-generated"
os.makedirs(ABS_OUT, exist_ok=True)
DPI = 200


def plot_variance_comparison():
    """比较三个均值相同但方差不同的分布"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Distribution A: constant = 100
    ax = axes[0]
    ax.bar([100], [1.0], width=2, color="#27ae60", alpha=0.8, edgecolor="#27ae60")
    ax.set_title("分布 A：常数\nVar = 0, σ = 0", fontsize=13, fontweight="bold")
    ax.set_xlabel("值", fontsize=12)
    ax.set_ylabel("概率", fontsize=12)
    ax.set_xlim(60, 140)
    ax.set_ylim(0, 1.15)
    ax.axvline(100, color="black", ls="--", lw=1.5, alpha=0.5)
    ax.text(100, 1.05, "μ = 100", ha="center", fontsize=10, fontweight="bold")

    # Distribution B: {0, 200} each with prob 0.5
    ax = axes[1]
    ax.bar([0, 200], [0.5, 0.5], width=8, color="#3498db", alpha=0.8,
           edgecolor="#3498db")
    ax.set_title("分布 B：{0, 200}，各 50%\nVar = 10000, σ = 100",
                 fontsize=13, fontweight="bold")
    ax.set_xlabel("值", fontsize=12)
    ax.set_ylabel("概率", fontsize=12)
    ax.set_xlim(-50, 250)
    ax.set_ylim(0, 0.65)
    ax.axvline(100, color="black", ls="--", lw=1.5, alpha=0.5)
    ax.text(100, 0.55, "μ = 100", ha="center", fontsize=10, fontweight="bold")
    ax.annotate("", xy=(0, 0.45), xytext=(200, 0.45),
                arrowprops=dict(arrowstyle="<->", color="#e74c3c", lw=2))
    ax.text(100, 0.48, "σ = 100", ha="center", fontsize=10, color="#e74c3c",
            fontweight="bold")

    # Distribution C: {-100, 300} each with prob 0.5
    ax = axes[2]
    ax.bar([-100, 300], [0.5, 0.5], width=8, color="#e74c3c", alpha=0.8,
           edgecolor="#e74c3c")
    ax.set_title("分布 C：{−100, 300}，各 50%\nVar = 40000, σ = 200",
                 fontsize=13, fontweight="bold")
    ax.set_xlabel("值", fontsize=12)
    ax.set_ylabel("概率", fontsize=12)
    ax.set_xlim(-200, 400)
    ax.set_ylim(0, 0.65)
    ax.axvline(100, color="black", ls="--", lw=1.5, alpha=0.5)
    ax.text(100, 0.55, "μ = 100", ha="center", fontsize=10, fontweight="bold")
    ax.annotate("", xy=(-100, 0.45), xytext=(300, 0.45),
                arrowprops=dict(arrowstyle="<->", color="#9b59b6", lw=2))
    ax.text(100, 0.48, "σ = 200", ha="center", fontsize=10, color="#9b59b6",
            fontweight="bold")

    fig.suptitle("三个均值相同 (μ=100) 但方差不同的分布", fontsize=16,
                 fontweight="bold", y=1.03)
    plt.tight_layout()
    path = os.path.join(ABS_OUT, "p08-ch04-variance-comparison.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {path}")


if __name__ == "__main__":
    plot_variance_comparison()
    print("All Ch04 figures generated.")
