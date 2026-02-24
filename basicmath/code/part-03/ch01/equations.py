"""
方程可视化

生成 Part 3 Chapter 1 所需的两张图：
  1. 二次方程判别式可视化（三条抛物线：Δ>0, Δ=0, Δ<0）
  2. 二元一次方程组的几何——两直线相交
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


def plot_quadratic_discriminant():
    """三条抛物线展示判别式 Δ 的三种情况。"""
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5), sharey=True)
    fig.suptitle("一元二次方程 $ax^2 + bx + c = 0$ 的判别式", fontsize=14, fontweight="bold")

    x = np.linspace(-4, 4, 400)

    configs = [
        {"a": 1, "b": 0, "c": -3, "title": "$\\Delta > 0$：两个不等实根",
         "color": "#27ae60", "desc": "$x^2 - 3 = 0$"},
        {"a": 1, "b": -4, "c": 4, "title": "$\\Delta = 0$：一个重根",
         "color": "#e67e22", "desc": "$x^2 - 4x + 4 = 0$"},
        {"a": 1, "b": 0, "c": 2, "title": "$\\Delta < 0$：无实根",
         "color": "#e74c3c", "desc": "$x^2 + 2 = 0$"},
    ]

    for ax, cfg in zip(axes, configs):
        a, b, c = cfg["a"], cfg["b"], cfg["c"]
        y = a * x**2 + b * x + c
        disc = b**2 - 4 * a * c

        ax.axhline(0, color="#7f8c8d", lw=0.8, zorder=1)
        ax.axvline(0, color="#7f8c8d", lw=0.8, zorder=1)
        ax.plot(x, y, color=cfg["color"], lw=2.5, zorder=3)

        if disc > 0:
            r1 = (-b - np.sqrt(disc)) / (2 * a)
            r2 = (-b + np.sqrt(disc)) / (2 * a)
            ax.plot([r1, r2], [0, 0], "o", color=cfg["color"], markersize=8, zorder=4)
            ax.annotate(f"$x_1 \\approx {r1:.2f}$", (r1, 0), textcoords="offset points",
                        xytext=(-10, 15), fontsize=9, color=cfg["color"])
            ax.annotate(f"$x_2 \\approx {r2:.2f}$", (r2, 0), textcoords="offset points",
                        xytext=(5, 15), fontsize=9, color=cfg["color"])
        elif disc == 0:
            r = -b / (2 * a)
            ax.plot(r, 0, "o", color=cfg["color"], markersize=8, zorder=4)
            ax.annotate(f"$x = {r:.0f}$ (重根)", (r, 0), textcoords="offset points",
                        xytext=(10, 15), fontsize=9, color=cfg["color"])

        ax.set_title(cfg["title"], fontsize=12, pad=10)
        ax.set_xlabel("$x$", fontsize=11)
        ax.set_ylim(-5, 10)
        ax.set_xlim(-4, 4)
        ax.text(0.05, 0.92, cfg["desc"], transform=ax.transAxes, fontsize=10,
                verticalalignment="top", bbox=dict(boxstyle="round,pad=0.3",
                fc="white", ec=cfg["color"], alpha=0.9))
        ax.grid(True, alpha=0.3)

    axes[0].set_ylabel("$y = f(x)$", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    out = os.path.join(ABS_OUT, "p03-ch01-quadratic-discriminant.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ {out}")


def plot_system_intersection():
    """两条直线相交，展示二元一次方程组的几何意义。"""
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.set_title("二元一次方程组的几何解释", fontsize=14, fontweight="bold", pad=12)

    x = np.linspace(-1, 6, 400)

    y1 = 2 * x - 1
    y2 = -x + 5

    ax.plot(x, y1, color="#2980b9", lw=2.5, label="$2x - y = 1$", zorder=3)
    ax.plot(x, y2, color="#e74c3c", lw=2.5, label="$x + y = 5$", zorder=3)

    ix, iy = 2, 3
    ax.plot(ix, iy, "ko", markersize=10, zorder=5)
    ax.plot(ix, iy, "o", color="#f1c40f", markersize=7, zorder=6)
    ax.annotate(f"  交点 $(2, 3)$", (ix, iy), fontsize=12, fontweight="bold",
                textcoords="offset points", xytext=(10, 10),
                arrowprops=dict(arrowstyle="->", color="#2c3e50", lw=1.5),
                bbox=dict(boxstyle="round,pad=0.4", fc="#fef9e7", ec="#f39c12"))

    ax.axhline(0, color="#7f8c8d", lw=0.8)
    ax.axvline(0, color="#7f8c8d", lw=0.8)
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-1.5, 6.5)
    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$y$", fontsize=12)
    ax.legend(fontsize=11, loc="upper right")
    ax.grid(True, alpha=0.3)

    ax.text(0.02, 0.02, "方程组的解 = 两条直线的交点",
            transform=ax.transAxes, fontsize=10, style="italic",
            bbox=dict(boxstyle="round,pad=0.4", fc="#eaf2f8", ec="#2980b9", alpha=0.9))

    fig.tight_layout()
    out = os.path.join(ABS_OUT, "p03-ch01-system-intersection.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ {out}")


if __name__ == "__main__":
    print("Part 3 Ch01: 方程可视化")
    plot_quadratic_discriminant()
    plot_system_intersection()
    print("  完成！")
