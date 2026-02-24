"""
数系可视化

生成 Part 2 Chapter 1 所需的五张图：
  1. 整数数轴（ℕ, ℤ 标注）
  2. 有理数稠密性可视化
  3. √2 的几何构造
  4. 有理数的"空隙"（ℝ 填补）
  5. 复数平面简介
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
# 图 1: 整数数轴，标注 ℕ 和 ℤ
# ═══════════════════════════════════════════
def plot_number_line_integers():
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.set_xlim(-6.5, 6.5)
    ax.set_ylim(-1.5, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.suptitle("整数数轴上的 $\\mathbb{N}$ 与 $\\mathbb{Z}$", fontsize=14, fontweight="bold")

    ax.annotate("", xy=(6.3, 0), xytext=(-6.3, 0),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#2c3e50"))

    for i in range(-6, 7):
        ax.plot(i, 0, "o", color="#2c3e50", markersize=6, zorder=5)
        ax.text(i, -0.5, str(i), ha="center", va="top", fontsize=10)

    for i in range(0, 7):
        ax.plot(i, 0, "o", color="#e74c3c", markersize=10, zorder=4, alpha=0.5)

    ax.annotate("$\\mathbb{N}$ = {0, 1, 2, ...}", xy=(3, 0.8), fontsize=12,
                color="#e74c3c", ha="center", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", fc="#fadbd8", ec="#e74c3c", alpha=0.8))
    ax.annotate("$\\mathbb{Z}$ = {..., -2, -1, 0, 1, 2, ...}", xy=(0, 1.6), fontsize=12,
                color="#2c3e50", ha="center", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", fc="#d5dbdb", ec="#2c3e50", alpha=0.8))

    fname = "p02-ch01-number-line-integers.png"
    fig.savefig(os.path.join(ABS_OUT, fname), dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  已生成: {fname}")


# ═══════════════════════════════════════════
# 图 2: 有理数稠密性
# ═══════════════════════════════════════════
def plot_rational_density():
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(-0.5, 4.5)
    ax.axis("off")
    fig.suptitle("有理数的稠密性 (Density of $\\mathbb{Q}$)", fontsize=14, fontweight="bold")

    ax.annotate("", xy=(1.05, 0), xytext=(-0.05, 0),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#2c3e50"))
    ax.text(-0.05, -0.3, "0", ha="center", fontsize=10)
    ax.text(1.0, -0.3, "1", ha="center", fontsize=10)

    levels = [
        ("分母 = 1", [0, 1], "#e74c3c", 0),
        ("分母 = 2", [1/2], "#e67e22", 1),
        ("分母 = 3", [1/3, 2/3], "#f1c40f", 2),
        ("分母 = 4", [1/4, 3/4], "#27ae60", 3),
        ("分母 = 5", [1/5, 2/5, 3/5, 4/5], "#3498db", 4),
    ]

    for label, pts, color, row in levels:
        y = row * 0.8 + 0.3
        ax.text(-0.08, y, label, ha="right", va="center", fontsize=9, color=color)
        for p in pts:
            ax.plot(p, 0, "|", color=color, markersize=12, markeredgewidth=2)
            ax.plot(p, y, "o", color=color, markersize=5)
            ax.plot([p, p], [0.05, y - 0.05], color=color, alpha=0.3, lw=0.5)

    ax.text(0.5, 4.2, "越来越多的有理数填满 [0, 1]",
            ha="center", fontsize=11, style="italic", color="#7f8c8d")

    fname = "p02-ch01-rational-density.png"
    fig.savefig(os.path.join(ABS_OUT, fname), dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  已生成: {fname}")


# ═══════════════════════════════════════════
# 图 3: √2 的几何构造
# ═══════════════════════════════════════════
def plot_sqrt2_construction():
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 2.5)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.suptitle("√2 的几何构造", fontsize=14, fontweight="bold")

    square = plt.Polygon([(0, 0), (1, 0), (1, 1), (0, 1)],
                         fill=True, fc="#d5f5e3", ec="#27ae60", lw=2)
    ax.add_patch(square)

    ax.plot([0, 1], [0, 1], color="#e74c3c", lw=2.5, zorder=5)

    ax.text(0.5, -0.15, "1", ha="center", fontsize=13, fontweight="bold", color="#27ae60")
    ax.text(-0.15, 0.5, "1", ha="center", fontsize=13, fontweight="bold", color="#27ae60")
    ax.text(0.6, 0.6, "$\\sqrt{2}$", ha="center", fontsize=14, fontweight="bold",
            color="#e74c3c", rotation=45)

    ax.annotate("", xy=(2.2, 0), xytext=(-0.3, 0),
                arrowprops=dict(arrowstyle="->", lw=1, color="#7f8c8d"))
    for i in range(3):
        ax.plot(i, 0, "|", color="#2c3e50", markersize=10, markeredgewidth=1.5)
        ax.text(i, -0.25, str(i), ha="center", fontsize=10)

    s2 = np.sqrt(2)
    ax.plot(s2, 0, "v", color="#e74c3c", markersize=10, zorder=5)
    ax.text(s2, -0.3, f"$\\sqrt{{2}}$ $\\approx$ {s2:.4f}", ha="center", fontsize=10, color="#e74c3c")

    theta = np.linspace(0, np.arctan2(1, 1), 50)
    arc_r = 0.2
    ax.plot(arc_r * np.cos(theta), arc_r * np.sin(theta), color="#7f8c8d", lw=1)
    ax.text(0.25, 0.1, "45°", fontsize=8, color="#7f8c8d")

    ax.text(1.5, 2.0, r"$d^2 = 1^2 + 1^2 = 2$", fontsize=13,
            bbox=dict(boxstyle="round,pad=0.3", fc="#fadbd8", ec="#e74c3c", alpha=0.8))
    ax.text(1.5, 1.5, r"$d = \sqrt{2} \notin \mathbb{Q}$", fontsize=13,
            bbox=dict(boxstyle="round,pad=0.3", fc="#fadbd8", ec="#e74c3c", alpha=0.8))

    fname = "p02-ch01-sqrt2-construction.png"
    fig.savefig(os.path.join(ABS_OUT, fname), dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  已生成: {fname}")


# ═══════════════════════════════════════════
# 图 4: 有理数的空隙
# ═══════════════════════════════════════════
def plot_rational_gaps():
    fig, axes = plt.subplots(2, 1, figsize=(12, 5), sharex=True)
    fig.suptitle("有理数的空隙与实数的填补", fontsize=14, fontweight="bold")

    for ax in axes:
        ax.set_xlim(-0.5, 3.5)
        ax.set_ylim(-0.5, 0.8)
        ax.axis("off")

    ax0 = axes[0]
    ax0.set_title("$\\mathbb{Q}$: 稠密但有空隙", fontsize=12, color="#e67e22")
    ax0.annotate("", xy=(3.3, 0), xytext=(-0.3, 0),
                 arrowprops=dict(arrowstyle="->", lw=1.5, color="#7f8c8d"))

    np.random.seed(42)
    rationals = sorted(set([p/q for q in range(1, 20) for p in range(0, 4*q)
                            if p/q <= 3.2]))
    for r in rationals:
        ax0.plot(r, 0, "|", color="#3498db", markersize=6, markeredgewidth=0.5, alpha=0.7)

    gaps = [np.sqrt(2), np.pi - 1, np.e - 1, np.sqrt(3), np.sqrt(5) - 1]
    for g in gaps:
        if 0 < g < 3.2:
            ax0.plot(g, 0, "x", color="#e74c3c", markersize=8, markeredgewidth=2, zorder=6)

    ax0.plot(np.sqrt(2), 0.4, "v", color="#e74c3c", markersize=10)
    ax0.text(np.sqrt(2), 0.55, "$\\sqrt{2}$ (空隙!)", ha="center", fontsize=10, color="#e74c3c")

    ax1 = axes[1]
    ax1.set_title("$\\mathbb{R}$: 完备——没有空隙", fontsize=12, color="#27ae60")
    ax1.annotate("", xy=(3.3, 0), xytext=(-0.3, 0),
                 arrowprops=dict(arrowstyle="->", lw=1.5, color="#7f8c8d"))
    x_line = np.linspace(-0.2, 3.2, 500)
    ax1.plot(x_line, np.zeros_like(x_line), color="#27ae60", lw=3, solid_capstyle="round")

    for i in range(4):
        ax1.plot(i, 0, "|", color="#2c3e50", markersize=10, markeredgewidth=1.5)
        ax1.text(i, -0.25, str(i), ha="center", fontsize=10)
    ax1.plot(np.sqrt(2), 0, "o", color="#e74c3c", markersize=8, zorder=6)
    ax1.text(np.sqrt(2), 0.3, "$\\sqrt{2}$", ha="center", fontsize=10, color="#e74c3c")

    plt.tight_layout()
    fname = "p02-ch01-rational-gaps.png"
    fig.savefig(os.path.join(ABS_OUT, fname), dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  已生成: {fname}")


# ═══════════════════════════════════════════
# 图 5: 复数平面简介
# ═══════════════════════════════════════════
def plot_complex_plane_intro():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 3.5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    fig.suptitle("复数平面 (Complex Plane)", fontsize=14, fontweight="bold")

    ax.set_xlabel("Re (实部)", fontsize=11, labelpad=10)
    ax.set_ylabel("Im (虚部)", fontsize=11, labelpad=10)
    ax.xaxis.set_label_coords(1.0, 0.48)
    ax.yaxis.set_label_coords(0.52, 1.0)

    points = [
        (2, 1, "$2 + i$", "#e74c3c"),
        (-1, 2, "$-1 + 2i$", "#3498db"),
        (1.5, -1.5, "$1.5 - 1.5i$", "#27ae60"),
        (-2, -1, "$-2 - i$", "#9b59b6"),
        (3, 0, "$3$ (实数)", "#e67e22"),
        (0, 2.5, "$2.5i$ (纯虚数)", "#1abc9c"),
    ]

    for x, y, label, color in points:
        ax.plot(x, y, "o", color=color, markersize=10, zorder=5)
        ax.plot([0, x], [0, y], "--", color=color, alpha=0.4, lw=1)
        if y >= 0:
            ax.text(x + 0.15, y + 0.2, label, fontsize=10, color=color)
        else:
            ax.text(x + 0.15, y - 0.3, label, fontsize=10, color=color)

    z = 2 + 1j
    r = abs(z)
    theta = np.angle(z)
    arc_t = np.linspace(0, theta, 30)
    ax.plot(0.5 * np.cos(arc_t), 0.5 * np.sin(arc_t), color="#e74c3c", lw=1)
    ax.text(0.6, 0.15, "$\\theta$", fontsize=10, color="#e74c3c")
    ax.text(1.15, 0.7, "$|z| = \\sqrt{5}$", fontsize=9, color="#e74c3c", rotation=27)

    fname = "p02-ch01-complex-plane-intro.png"
    fig.savefig(os.path.join(ABS_OUT, fname), dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  已生成: {fname}")


# ═══════════════════════════════════════════
if __name__ == "__main__":
    print("Part 2 Ch01 — 数系可视化")
    plot_number_line_integers()
    plot_rational_density()
    plot_sqrt2_construction()
    plot_rational_gaps()
    plot_complex_plane_intro()
    print("全部完成！")
