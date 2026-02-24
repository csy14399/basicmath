"""
反三角函数可视化

生成 Part 4 Chapter 4 所需的一张图：
  反三角函数图像（arcsin, arccos, arctan 及对应原函数）
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


def plot_inverse_trig_graphs():
    """三个主要反三角函数及其对应原函数。"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle("反三角函数的图像", fontsize=15, fontweight="bold")

    # arcsin
    ax = axes[0]
    ax.set_title("$y = \\arcsin x$", fontsize=13, pad=8)
    x_as = np.linspace(-1, 1, 500)
    ax.plot(x_as, np.arcsin(x_as), color="#2980b9", lw=2.5, label="$y = \\arcsin x$")
    t_sin = np.linspace(-np.pi/2, np.pi/2, 300)
    ax.plot(np.sin(t_sin), t_sin, color="#2980b9", lw=2.5, alpha=0.3)
    full_sin_t = np.linspace(-2*np.pi, 2*np.pi, 500)
    ax.plot(np.sin(full_sin_t), full_sin_t, color="#bdc3c7", lw=1, alpha=0.4,
            label="$x = \\sin y$（全部）")
    line_x = np.linspace(-1.5, 1.5, 100)
    ax.plot(line_x, line_x, "--", color="#7f8c8d", lw=1, alpha=0.5, label="$y = x$")
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_yticks([-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2])
    ax.set_yticklabels(["$-\\frac{\\pi}{2}$", "$-\\frac{\\pi}{4}$", "$0$",
                        "$\\frac{\\pi}{4}$", "$\\frac{\\pi}{2}$"])
    ax.set_aspect("equal")
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(True, alpha=0.3)
    ax.annotate("定义域 $[-1, 1]$\n值域 $[-\\frac{\\pi}{2}, \\frac{\\pi}{2}]$",
                xy=(0.5, -1.2), fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", fc="#eaf2f8", alpha=0.9))

    # arccos
    ax = axes[1]
    ax.set_title("$y = \\arccos x$", fontsize=13, pad=8)
    x_ac = np.linspace(-1, 1, 500)
    ax.plot(x_ac, np.arccos(x_ac), color="#e74c3c", lw=2.5, label="$y = \\arccos x$")
    t_cos = np.linspace(0, np.pi, 300)
    ax.plot(np.cos(t_cos), t_cos, color="#e74c3c", lw=2.5, alpha=0.3)
    ax.axhline(np.pi/2, color="#27ae60", lw=1, ls=":", alpha=0.6)
    ax.annotate("$y = \\pi/2$", xy=(0.5, np.pi/2+0.15), fontsize=9, color="#27ae60")
    line_x = np.linspace(-1.5, 3.5, 100)
    ax.plot(line_x, line_x, "--", color="#7f8c8d", lw=1, alpha=0.5, label="$y = x$")
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-0.5, 3.5)
    ax.set_yticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
    ax.set_yticklabels(["$0$", "$\\frac{\\pi}{4}$", "$\\frac{\\pi}{2}$",
                        "$\\frac{3\\pi}{4}$", "$\\pi$"])
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3)
    ax.annotate("定义域 $[-1, 1]$\n值域 $[0, \\pi]$\n严格递减",
                xy=(0.3, 2.5), fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", fc="#fdedec", alpha=0.9))

    # arctan
    ax = axes[2]
    ax.set_title("$y = \\arctan x$", fontsize=13, pad=8)
    x_at = np.linspace(-10, 10, 1000)
    ax.plot(x_at, np.arctan(x_at), color="#8e44ad", lw=2.5, label="$y = \\arctan x$")
    ax.axhline(np.pi/2, color="#e74c3c", lw=1.5, ls="--", alpha=0.7)
    ax.axhline(-np.pi/2, color="#e74c3c", lw=1.5, ls="--", alpha=0.7)
    ax.annotate("$y = \\frac{\\pi}{2}$（渐近线）", xy=(3, np.pi/2+0.15),
                fontsize=9, color="#e74c3c")
    ax.annotate("$y = -\\frac{\\pi}{2}$（渐近线）", xy=(3, -np.pi/2-0.25),
                fontsize=9, color="#e74c3c")
    line_x = np.linspace(-2, 2, 100)
    ax.plot(line_x, line_x, "--", color="#7f8c8d", lw=1, alpha=0.5, label="$y = x$")
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_xlim(-6, 6)
    ax.set_ylim(-2.5, 2.5)
    ax.set_yticks([-np.pi/2, -np.pi/4, 0, np.pi/4, np.pi/2])
    ax.set_yticklabels(["$-\\frac{\\pi}{2}$", "$-\\frac{\\pi}{4}$", "$0$",
                        "$\\frac{\\pi}{4}$", "$\\frac{\\pi}{2}$"])
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(True, alpha=0.3)
    ax.annotate("定义域 $\\mathbb{R}$\n值域 $(-\\frac{\\pi}{2}, \\frac{\\pi}{2})$\n奇函数",
                xy=(2.5, -1.5), fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", fc="#f5eef8", alpha=0.9))

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch04-inverse-trig-graphs.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    plot_inverse_trig_graphs()
    print("All ch04 plots generated.")
