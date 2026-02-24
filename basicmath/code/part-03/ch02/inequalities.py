"""
不等式可视化

生成 Part 3 Chapter 2 所需的三张图：
  1. 数轴不等式可视化
  2. 二次不等式与抛物线
  3. AM-GM 不等式的几何证明
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as patches
import numpy as np

_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

ABS_OUT = "/workspace/basicmath/images/code-generated"
os.makedirs(ABS_OUT, exist_ok=True)

DPI = 200


def plot_inequality_number_line():
    """数轴上展示不等式的解集。"""
    fig, axes = plt.subplots(4, 1, figsize=(12, 6))
    fig.suptitle("数轴上的不等式解集", fontsize=14, fontweight="bold")

    cases = [
        {"label": "$x > 2$", "intervals": [(2, 8)], "points": [(2, "open")],
         "color": "#27ae60"},
        {"label": "$x \\leq -1$", "intervals": [(-8, -1)], "points": [(-1, "closed")],
         "color": "#2980b9"},
        {"label": "$-3 < x \\leq 4$", "intervals": [(-3, 4)],
         "points": [(-3, "open"), (4, "closed")], "color": "#8e44ad"},
        {"label": "$x < -2 \\;\\text{or}\\; x > 3$",
         "intervals": [(-8, -2), (3, 8)],
         "points": [(-2, "open"), (3, "open")], "color": "#e74c3c"},
    ]

    for ax, case in zip(axes, cases):
        ax.set_xlim(-7, 7)
        ax.set_ylim(-0.5, 0.8)
        ax.set_aspect("equal")
        ax.axis("off")

        ax.annotate("", xy=(6.8, 0), xytext=(-6.8, 0),
                    arrowprops=dict(arrowstyle="->", lw=1.2, color="#2c3e50"))

        for i in range(-6, 7):
            ax.plot(i, 0, "|", color="#2c3e50", markersize=5)
            if i % 2 == 0:
                ax.text(i, -0.3, str(i), ha="center", fontsize=8, color="#7f8c8d")

        for a, b in case["intervals"]:
            a_c = max(a, -6.5)
            b_c = min(b, 6.5)
            ax.plot([a_c, b_c], [0, 0], lw=5, color=case["color"], alpha=0.6, zorder=3,
                    solid_capstyle="butt")

        for pt, style in case["points"]:
            if style == "open":
                ax.plot(pt, 0, "o", color=case["color"], markersize=9, zorder=5,
                        markerfacecolor="white", markeredgewidth=2)
            else:
                ax.plot(pt, 0, "o", color=case["color"], markersize=9, zorder=5)

        ax.text(-6.8, 0.4, case["label"], fontsize=12, fontweight="bold",
                color=case["color"])

    fig.tight_layout(rect=[0, 0, 1, 0.93])
    out = os.path.join(ABS_OUT, "p03-ch02-inequality-number-line.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ {out}")


def plot_quadratic_inequality():
    """二次不等式 x² - 2x - 3 ≤ 0 的图形解法。"""
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_title("二次不等式 $x^2 - 2x - 3 \\leq 0$ 的解集",
                 fontsize=14, fontweight="bold", pad=12)

    x = np.linspace(-3, 5, 500)
    y = x**2 - 2 * x - 3

    ax.fill_between(x, y, 0, where=(y <= 0), color="#27ae60", alpha=0.25, zorder=2,
                    label="$f(x) \\leq 0$ 的区域")

    ax.plot(x, y, color="#2c3e50", lw=2.5, zorder=3, label="$f(x) = x^2 - 2x - 3$")

    ax.axhline(0, color="#7f8c8d", lw=0.8, zorder=1)
    ax.axvline(0, color="#7f8c8d", lw=0.8, zorder=1)

    ax.plot(-1, 0, "o", color="#e74c3c", markersize=10, zorder=5)
    ax.plot(3, 0, "o", color="#e74c3c", markersize=10, zorder=5)
    ax.annotate("$x_1 = -1$", (-1, 0), textcoords="offset points", xytext=(-15, 15),
                fontsize=11, color="#e74c3c", fontweight="bold")
    ax.annotate("$x_2 = 3$", (3, 0), textcoords="offset points", xytext=(10, 15),
                fontsize=11, color="#e74c3c", fontweight="bold")

    ax.annotate("", xy=(3, -4.5), xytext=(-1, -4.5),
                arrowprops=dict(arrowstyle="<->", color="#27ae60", lw=2))
    ax.text(1, -5, "解集：$-1 \\leq x \\leq 3$", ha="center", fontsize=12,
            color="#27ae60", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#27ae60"))

    ax.plot(1, -4, "v", color="#2c3e50", markersize=8, zorder=5)
    ax.annotate("顶点 $(1, -4)$", (1, -4), textcoords="offset points", xytext=(15, -10),
                fontsize=10, color="#2c3e50")

    ax.set_xlim(-3, 5)
    ax.set_ylim(-6, 8)
    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$y$", fontsize=12)
    ax.legend(fontsize=10, loc="upper left")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    out = os.path.join(ABS_OUT, "p03-ch02-quadratic-inequality.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ {out}")


def plot_am_gm_geometric():
    """AM-GM 不等式的经典几何证明（半圆法）。"""
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_title("AM-GM 不等式的几何证明", fontsize=14, fontweight="bold", pad=12)

    a_val, b_val = 5, 2
    total = a_val + b_val
    am = total / 2.0
    gm = np.sqrt(a_val * b_val)

    theta = np.linspace(0, np.pi, 200)
    cx, cy = am, 0
    rx = am
    semicircle_x = cx + rx * np.cos(theta)
    semicircle_y = rx * np.sin(theta)
    ax.plot(semicircle_x, semicircle_y, color="#2c3e50", lw=2, zorder=3)

    ax.plot([0, total], [0, 0], color="#2c3e50", lw=2, zorder=3)

    ax.plot(0, 0, "o", color="#2c3e50", markersize=8, zorder=5)
    ax.plot(a_val, 0, "o", color="#2c3e50", markersize=8, zorder=5)
    ax.plot(total, 0, "o", color="#2c3e50", markersize=8, zorder=5)
    ax.plot(am, 0, "o", color="#e67e22", markersize=8, zorder=5)

    ax.text(0, -0.4, "$A$", ha="center", va="top", fontsize=12, fontweight="bold")
    ax.text(a_val, -0.4, "$C$", ha="center", va="top", fontsize=12, fontweight="bold")
    ax.text(total, -0.4, "$B$", ha="center", va="top", fontsize=12, fontweight="bold")
    ax.text(am, -0.4, "$M$", ha="center", va="top", fontsize=12, fontweight="bold",
            color="#e67e22")

    ax.plot([a_val, a_val], [0, gm], "--", color="#e74c3c", lw=1.5, zorder=3)
    ax.plot(a_val, gm, "o", color="#e74c3c", markersize=8, zorder=5)
    ax.text(a_val + 0.15, gm / 2, f"$\\sqrt{{ab}}={gm:.2f}$", fontsize=11,
            color="#e74c3c", fontweight="bold")
    ax.text(a_val, gm + 0.3, "$D$", ha="center", fontsize=12, fontweight="bold",
            color="#e74c3c")

    ax.plot([am, am], [0, am], "--", color="#e67e22", lw=1.5, zorder=3)
    ax.plot(am, am, "o", color="#e67e22", markersize=8, zorder=5)
    ax.text(am + 0.15, am / 2, f"$\\frac{{a+b}}{{2}}={am:.1f}$", fontsize=11,
            color="#e67e22", fontweight="bold")

    ax.annotate("", xy=(a_val, -0.9), xytext=(0, -0.9),
                arrowprops=dict(arrowstyle="<->", color="#2980b9", lw=1.5))
    ax.text(a_val / 2, -1.3, f"$a = {a_val}$", ha="center", fontsize=11, color="#2980b9")

    ax.annotate("", xy=(total, -0.9), xytext=(a_val, -0.9),
                arrowprops=dict(arrowstyle="<->", color="#8e44ad", lw=1.5))
    ax.text(a_val + b_val / 2, -1.3, f"$b = {b_val}$", ha="center", fontsize=11,
            color="#8e44ad")

    ax.text(0.5, 0.95,
            "$CD = \\sqrt{AC \\cdot CB} = \\sqrt{ab}$ (GM)\n"
            "$ME = \\frac{AB}{2} = \\frac{a+b}{2}$ (AM)\n"
            "半径 $\\geq$ 弦高 $\\Rightarrow$ AM $\\geq$ GM",
            transform=ax.transAxes, fontsize=10, verticalalignment="top",
            bbox=dict(boxstyle="round,pad=0.5", fc="#fef9e7", ec="#f39c12", alpha=0.95))

    ax.set_xlim(-1, total + 1)
    ax.set_ylim(-2, am + 1.5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.set_xlabel("$x$", fontsize=12)
    fig.tight_layout()
    out = os.path.join(ABS_OUT, "p03-ch02-am-gm-geometric.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ {out}")


if __name__ == "__main__":
    print("Part 3 Ch02: 不等式可视化")
    plot_inequality_number_line()
    plot_quadratic_inequality()
    plot_am_gm_geometric()
    print("  完成！")
