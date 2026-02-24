"""
函数性质可视化

生成 Part 4 Chapter 1 所需的两张图：
  1. 函数性质示例（单调性、奇偶性）
  2. 函数与反函数关于 y=x 的对称
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


def plot_function_properties():
    """单调性和奇偶性示例。"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle("函数的基本性质", fontsize=15, fontweight="bold")

    x = np.linspace(-3, 3, 500)

    # Monotone increasing
    ax = axes[0]
    ax.set_title("严格递增：$f(x) = x^3$", fontsize=11, pad=8)
    ax.plot(x, x**3, color="#2980b9", lw=2.5)
    ax.axhline(0, color="#7f8c8d", lw=0.6)
    ax.axvline(0, color="#7f8c8d", lw=0.6)
    x1, x2 = -1.5, 1.0
    ax.plot([x1, x1], [0, x1**3], "--", color="#e74c3c", lw=1, alpha=0.7)
    ax.plot([x2, x2], [0, x2**3], "--", color="#e74c3c", lw=1, alpha=0.7)
    ax.plot(x1, x1**3, "o", color="#e74c3c", ms=6)
    ax.plot(x2, x2**3, "o", color="#e74c3c", ms=6)
    ax.annotate("$x_1 < x_2$", xy=(x1, -5), fontsize=9, ha="center", color="#e74c3c")
    ax.annotate("$f(x_1) < f(x_2)$", xy=(0.3, -2), fontsize=9, color="#e74c3c")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-10, 10)
    ax.grid(True, alpha=0.3)

    # Even function
    ax = axes[1]
    ax.set_title("偶函数：$f(x) = x^2$\n$f(-x) = f(x)$", fontsize=11, pad=8)
    ax.plot(x, x**2, color="#27ae60", lw=2.5)
    ax.axhline(0, color="#7f8c8d", lw=0.6)
    ax.axvline(0, color="#7f8c8d", lw=0.6, ls="--")
    xp = 1.8
    ax.plot([xp, xp], [0, xp**2], "--", color="#e74c3c", lw=1, alpha=0.7)
    ax.plot([-xp, -xp], [0, xp**2], "--", color="#e74c3c", lw=1, alpha=0.7)
    ax.plot(xp, xp**2, "o", color="#e74c3c", ms=6)
    ax.plot(-xp, xp**2, "o", color="#e74c3c", ms=6)
    ax.annotate("关于 $y$ 轴对称", xy=(0, 6), fontsize=9, ha="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="#eafaf1", alpha=0.8))
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 9)
    ax.grid(True, alpha=0.3)

    # Odd function
    ax = axes[2]
    ax.set_title("奇函数：$f(x) = x^3$\n$f(-x) = -f(x)$", fontsize=11, pad=8)
    ax.plot(x, x**3, color="#8e44ad", lw=2.5)
    ax.axhline(0, color="#7f8c8d", lw=0.6)
    ax.axvline(0, color="#7f8c8d", lw=0.6)
    xp = 1.3
    ax.plot(xp, xp**3, "o", color="#e74c3c", ms=6)
    ax.plot(-xp, -(xp**3), "o", color="#e74c3c", ms=6)
    ax.plot([xp, -xp], [xp**3, -(xp**3)], "--", color="#e74c3c", lw=1, alpha=0.5)
    ax.annotate("关于原点对称", xy=(0, 5), fontsize=9, ha="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="#f5eef8", alpha=0.8))
    ax.set_xlim(-3, 3)
    ax.set_ylim(-10, 10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch01-function-properties.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


def plot_inverse_symmetry():
    """函数与反函数关于 y=x 的对称性。"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("函数与反函数：关于 $y = x$ 的对称", fontsize=15, fontweight="bold")

    # f(x) = x^2 and its inverse sqrt(x)
    ax = axes[0]
    ax.set_title("$f(x) = x^2$ (限制 $x \\geq 0$)  与  $f^{-1}(x) = \\sqrt{x}$", fontsize=11, pad=8)
    x_pos = np.linspace(0, 3, 300)
    ax.plot(x_pos, x_pos**2, color="#2980b9", lw=2.5, label="$f(x) = x^2$")
    x_inv = np.linspace(0, 9, 300)
    ax.plot(x_inv, np.sqrt(x_inv), color="#e74c3c", lw=2.5, label="$f^{-1}(x) = \\sqrt{x}$")
    line_x = np.linspace(0, 4, 100)
    ax.plot(line_x, line_x, "--", color="#7f8c8d", lw=1.5, label="$y = x$")
    pts = [(1, 1), (2, 4)]
    for px, py in pts:
        ax.plot([px, py], [py, px], ":", color="#27ae60", lw=1.2, alpha=0.7)
        ax.plot(px, py, "o", color="#2980b9", ms=5)
        ax.plot(py, px, "s", color="#e74c3c", ms=5)
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-0.5, 6)
    ax.set_aspect("equal")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # f(x) = e^x and ln(x)
    ax = axes[1]
    ax.set_title("$f(x) = e^x$  与  $f^{-1}(x) = \\ln x$", fontsize=11, pad=8)
    x_exp = np.linspace(-2, 2, 300)
    ax.plot(x_exp, np.exp(x_exp), color="#2980b9", lw=2.5, label="$f(x) = e^x$")
    x_log = np.linspace(0.05, 7, 300)
    ax.plot(x_log, np.log(x_log), color="#e74c3c", lw=2.5, label="$f^{-1}(x) = \\ln x$")
    line_x = np.linspace(-1, 4, 100)
    ax.plot(line_x, line_x, "--", color="#7f8c8d", lw=1.5, label="$y = x$")
    pts_e = [(0, 1), (1, np.e)]
    for px, py in pts_e:
        ax.plot([px, py], [py, px], ":", color="#27ae60", lw=1.2, alpha=0.7)
        ax.plot(px, py, "o", color="#2980b9", ms=5)
        ax.plot(py, px, "s", color="#e74c3c", ms=5)
    ax.set_xlim(-2, 5)
    ax.set_ylim(-2, 5)
    ax.set_aspect("equal")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch01-inverse-symmetry.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    plot_function_properties()
    plot_inverse_symmetry()
    print("All ch01 plots generated.")
