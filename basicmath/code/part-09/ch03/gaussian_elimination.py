"""
Gauss 消元法与解的几何可视化

生成 Part 9 Chapter 3 所需的两张图：
  1. Gauss 消元步骤 (p09-ch03-gaussian-steps.png)
  2. 解的几何解释 (p09-ch03-solution-geometry.png)
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

ABS_OUT = "/workspace/basicmath/images/code-generated"
os.makedirs(ABS_OUT, exist_ok=True)
DPI = 200


def draw_augmented(ax, mat, title, x0, y0, cell=0.7, highlight_rows=None,
                   pivot_cells=None):
    """Draw an augmented matrix on axes at position (x0, y0)."""
    m, n = mat.shape
    sep_col = n - 1
    if highlight_rows is None:
        highlight_rows = []
    if pivot_cells is None:
        pivot_cells = []

    for i in range(m):
        for j in range(n):
            bg = "white"
            if (i, j) in pivot_cells:
                bg = "#fadbd8"
            elif i in highlight_rows:
                bg = "#d5f5e3"

            rect = plt.Rectangle((x0 + j * cell, y0 - i * cell), cell, cell,
                                 facecolor=bg, edgecolor="black", lw=0.8)
            ax.add_patch(rect)
            val = mat[i, j]
            txt = str(int(val)) if val == int(val) else f"{val:.1f}"
            ax.text(x0 + j * cell + cell / 2, y0 - i * cell + cell / 2,
                    txt, ha="center", va="center", fontsize=10)

    lx = x0 + sep_col * cell
    ax.plot([lx, lx], [y0 + cell, y0 - (m - 1) * cell], color="red",
            lw=2, alpha=0.7)

    ax.text(x0 + n * cell / 2, y0 + cell + 0.15, title, ha="center",
            fontsize=11, fontweight="bold", color="#2c3e50")


def plot_gaussian_steps():
    """Gauss 消元的步骤示意"""
    fig, ax = plt.subplots(figsize=(18, 7))
    ax.set_xlim(-0.5, 21)
    ax.set_ylim(-3.5, 3.5)
    ax.set_aspect("equal")
    ax.axis("off")

    step0 = np.array([
        [1, 1, 1, 6],
        [2, 3, 1, 14],
        [1, 2, -1, 2]
    ], dtype=float)

    step1 = np.array([
        [1, 1, 1, 6],
        [0, 1, -1, 2],
        [0, 1, -2, -4]
    ], dtype=float)

    step2 = np.array([
        [1, 1, 1, 6],
        [0, 1, -1, 2],
        [0, 0, -1, -6]
    ], dtype=float)

    step3 = np.array([
        [1, 0, 0, -8],
        [0, 1, 0, 8],
        [0, 0, 1, 6]
    ], dtype=float)

    cell = 0.7
    y0 = 1.5

    draw_augmented(ax, step0, "原始增广矩阵", 0, y0, cell)
    draw_augmented(ax, step1, "$R_2-2R_1,\\ R_3-R_1$", 4.5, y0, cell,
                   highlight_rows=[1, 2])
    draw_augmented(ax, step2, "$R_3-R_2$ → REF", 9, y0, cell,
                   highlight_rows=[2], pivot_cells=[(0, 0), (1, 1), (2, 2)])
    draw_augmented(ax, step3, "RREF", 13.5, y0, cell,
                   pivot_cells=[(0, 0), (1, 1), (2, 2)])

    for x_arr in [3.3, 7.8, 12.3]:
        ax.annotate("", xy=(x_arr + 0.8, y0 - 0.3),
                    xytext=(x_arr, y0 - 0.3),
                    arrowprops=dict(arrowstyle="->", color="#3498db", lw=2.5))

    ax.text(10.5, -2.5,
            r"解: $x=-8,\ y=8,\ z=6$",
            fontsize=15, ha="center", fontweight="bold", color="#c0392b")

    ax.text(10.5, -3.2,
            r"验证: $(-8)+8+6=6$  ✓,  $2(-8)+3(8)+6=14$  ✓,  $(-8)+2(8)-6=2$  ✓",
            fontsize=11, ha="center", color="#7f8c8d")

    fig.suptitle("Gauss 消元法: 从增广矩阵到 RREF", fontsize=17,
                 fontweight="bold", y=0.97)

    out = os.path.join(ABS_OUT, "p09-ch03-gaussian-steps.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"[OK] {out}")


def plot_solution_geometry():
    """三种解况的几何解释 — R^3 中平面的交集"""
    fig = plt.figure(figsize=(18, 6))

    xx, yy = np.meshgrid(np.linspace(-3, 3, 20), np.linspace(-3, 3, 20))

    # Panel 1: Unique solution (3 planes, 1 point)
    ax1 = fig.add_subplot(131, projection="3d")
    planes = [
        (1, 1, 1, 6, "#e74c3c"),
        (2, 3, 1, 14, "#3498db"),
        (1, 2, -1, 2, "#27ae60"),
    ]
    for a, b, c, d, color in planes:
        zz = (d - a * xx - b * yy) / c if c != 0 else np.zeros_like(xx)
        mask = np.abs(zz) < 10
        zz_plot = np.where(mask, zz, np.nan)
        ax1.plot_surface(xx, yy, zz_plot, alpha=0.25, color=color)

    ax1.scatter([-8], [8], [6], color="black", s=80, zorder=10)
    ax1.text(-8, 8, 6.5, "解", fontsize=11, fontweight="bold")
    ax1.set_title("唯一解\n（三平面交于一点）", fontsize=13, fontweight="bold")
    ax1.set_xlabel("$x$")
    ax1.set_ylabel("$y$")
    ax1.set_zlabel("$z$")
    ax1.view_init(elev=20, azim=30)

    # Panel 2: Infinitely many solutions (3 planes, 1 line)
    ax2 = fig.add_subplot(132, projection="3d")
    planes2 = [
        (1, 1, -1, 2, "#e74c3c"),
        (2, 1, 1, 5, "#3498db"),
        (3, 2, 0, 7, "#27ae60"),
    ]
    for a, b, c, d, color in planes2:
        if c != 0:
            zz = (d - a * xx - b * yy) / c
        else:
            zz = np.zeros_like(xx)
        mask = np.abs(zz) < 10
        zz_plot = np.where(mask, zz, np.nan)
        ax2.plot_surface(xx, yy, zz_plot, alpha=0.25, color=color)

    t = np.linspace(-2, 4, 50)
    line_x = 3 - 2 * t
    line_y = -1 + 3 * t
    line_z = t
    mask_l = (np.abs(line_x) < 4) & (np.abs(line_y) < 4) & (np.abs(line_z) < 4)
    ax2.plot(line_x[mask_l], line_y[mask_l], line_z[mask_l],
             color="black", lw=3, zorder=10)
    ax2.set_title("无穷多解\n（三平面交于一线）", fontsize=13, fontweight="bold")
    ax2.set_xlabel("$x$")
    ax2.set_ylabel("$y$")
    ax2.set_zlabel("$z$")
    ax2.view_init(elev=20, azim=30)

    # Panel 3: No solution (2 parallel planes + 1 crossing)
    ax3 = fig.add_subplot(133, projection="3d")
    zz1 = 3 - xx - yy
    zz2 = 4 - xx - yy
    zz3 = (5 - xx + yy) / 2
    for zz, color in [(zz1, "#e74c3c"), (zz2, "#3498db"), (zz3, "#27ae60")]:
        mask = np.abs(zz) < 8
        zz_plot = np.where(mask, zz, np.nan)
        ax3.plot_surface(xx, yy, zz_plot, alpha=0.25, color=color)

    ax3.set_title("无解\n（含平行平面）", fontsize=13, fontweight="bold")
    ax3.set_xlabel("$x$")
    ax3.set_ylabel("$y$")
    ax3.set_zlabel("$z$")
    ax3.view_init(elev=20, azim=30)

    fig.suptitle("$\\mathbb{R}^3$ 中线性方程组解的几何解释",
                 fontsize=16, fontweight="bold", y=1.02)
    plt.tight_layout()

    out = os.path.join(ABS_OUT, "p09-ch03-solution-geometry.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"[OK] {out}")


if __name__ == "__main__":
    plot_gaussian_steps()
    plot_solution_geometry()
    print("Ch03 images generated successfully.")
