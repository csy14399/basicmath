"""
解析几何可视化

生成 Part 5 Chapter 2 所需的两张图：
  1. 直线的各种形式 (p05-ch02-line-forms.png)
  2. 直线与圆的位置关系 (p05-ch02-line-circle-positions.png)
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


def plot_line_forms():
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle("直线方程的三种形式", fontsize=14, fontweight="bold")

    x = np.linspace(-1, 6, 300)

    ax = axes[0]
    ax.set_title("斜截式：$y = mx + b$", fontsize=12)
    for m, b, col, label in [(1, 1, "#e74c3c", "$m=1, b=1$"),
                              (2, 0, "#2980b9", "$m=2, b=0$"),
                              (-0.5, 3, "#27ae60", "$m=-0.5, b=3$")]:
        ax.plot(x, m * x + b, "-", color=col, lw=2, label=label)
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_xlim(-1, 6)
    ax.set_ylim(-2, 7)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.set_title("点斜式：$y - y_0 = m(x - x_0)$", fontsize=12)
    px, py = 2, 3
    ax.plot(px, py, "o", color="#2c3e50", ms=8, zorder=5)
    ax.annotate("$(x_0, y_0) = (2, 3)$", (px + 0.2, py + 0.3), fontsize=10)
    for m, col in [(1, "#e74c3c"), (0, "#3498db"), (-2, "#27ae60")]:
        ax.plot(x, py + m * (x - px), "-", color=col, lw=2, label=f"$m={m}$")
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_xlim(-1, 6)
    ax.set_ylim(-2, 7)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    ax = axes[2]
    ax.set_title("截距式：$\\frac{x}{a} + \\frac{y}{b} = 1$", fontsize=12)
    for a, b, col in [(4, 3, "#e74c3c"), (2, 5, "#2980b9"), (5, 2, "#27ae60")]:
        ax.plot([0, a], [b, 0], "-", color=col, lw=2.5,
                label=f"$a={a}, b={b}$")
        ax.plot(a, 0, "o", color=col, ms=6)
        ax.plot(0, b, "o", color=col, ms=6)
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-0.5, 6)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch02-line-forms.png"), dpi=DPI)
    plt.close(fig)


def plot_line_circle_positions():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("直线与圆的三种位置关系", fontsize=14, fontweight="bold")

    R = 2
    theta = np.linspace(0, 2 * np.pi, 300)

    titles = ["相离 ($d > r$)", "相切 ($d = r$)", "相交 ($d < r$)"]
    d_vals = [3.0, 2.0, 1.0]
    colors = ["#e74c3c", "#f39c12", "#2980b9"]

    for ax, title, d, col in zip(axes, titles, d_vals, colors):
        ax.set_title(title, fontsize=12)
        ax.plot(R * np.cos(theta), R * np.sin(theta), "-", color="#2c3e50", lw=2)
        ax.plot(0, 0, "o", color="#2c3e50", ms=5)
        ax.annotate("O", (0.15, 0.15), fontsize=10)

        x = np.linspace(-3.5, 3.5, 300)
        ax.plot(x, np.zeros_like(x) + d, "-", color=col, lw=2.5)

        ax.plot([0, 0], [0, d], "--", color="#7f8c8d", lw=1.2)
        ax.annotate(f"$d = {d:.0f}$", (0.15, d / 2), fontsize=10, color="#7f8c8d")
        ax.annotate(f"$r = {R}$", (-1.8, 1.0), fontsize=10, color="#2c3e50")

        if d == R:
            ax.plot(0, R, "o", color=col, ms=8, zorder=5)
            ax.annotate("切点", (0.2, R + 0.2), fontsize=10, color=col)
        elif d < R:
            xint = np.sqrt(R**2 - d**2)
            ax.plot(xint, d, "o", color=col, ms=7, zorder=5)
            ax.plot(-xint, d, "o", color=col, ms=7, zorder=5)

        ax.set_aspect("equal")
        ax.set_xlim(-3.5, 3.5)
        ax.set_ylim(-3, 4)
        ax.grid(True, alpha=0.2)

    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch02-line-circle-positions.png"), dpi=DPI)
    plt.close(fig)


if __name__ == "__main__":
    print("Generating ch02 images...")
    plot_line_forms()
    print("  ✓ line-forms")
    plot_line_circle_positions()
    print("  ✓ line-circle-positions")
    print("All ch02 images generated.")
