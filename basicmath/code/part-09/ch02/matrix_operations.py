"""
矩阵运算可视化

生成 Part 9 Chapter 2 所需的一张图：
  1. 矩阵乘法示意图 (p09-ch02-matrix-multiplication.png)
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


def draw_matrix_cell(ax, x, y, w, h, text, bg_color="white", text_color="black",
                     fontsize=14, bold=False):
    rect = plt.Rectangle((x, y), w, h, facecolor=bg_color, edgecolor="black",
                          lw=1.2, alpha=0.85)
    ax.add_patch(rect)
    weight = "bold" if bold else "normal"
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, color=text_color, fontweight=weight)


def plot_matrix_multiplication():
    """矩阵乘法的行乘列示意图"""
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.set_xlim(-1, 22)
    ax.set_ylim(-2, 9)
    ax.set_aspect("equal")
    ax.axis("off")

    cell = 1.2

    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 10], [8, 11], [9, 12]])
    C = A @ B

    x0_a, y0_a = 0, 4
    ax.text(x0_a + 1.5 * cell, y0_a + 2.5 * cell, "$A$  (2×3)",
            ha="center", fontsize=14, fontweight="bold", color="#2c3e50")

    for i in range(2):
        for j in range(3):
            bg = "#fadbd8" if i == 0 else "white"
            draw_matrix_cell(ax, x0_a + j * cell, y0_a + (1 - i) * cell,
                             cell, cell, str(A[i, j]), bg_color=bg)

    x0_b, y0_b = 5, 4
    ax.text(x0_b + cell, y0_b + 3.5 * cell, "$B$  (3×2)",
            ha="center", fontsize=14, fontweight="bold", color="#2c3e50")

    for i in range(3):
        for j in range(2):
            bg = "#d4efdf" if j == 0 else "white"
            draw_matrix_cell(ax, x0_b + j * cell, y0_b + (2 - i) * cell,
                             cell, cell, str(B[i, j]), bg_color=bg)

    ax.text(9.2, 5.5, "=", fontsize=28, ha="center", va="center",
            fontweight="bold")

    x0_c, y0_c = 10.5, 4
    ax.text(x0_c + cell, y0_c + 2.5 * cell, "$C = AB$  (2×2)",
            ha="center", fontsize=14, fontweight="bold", color="#2c3e50")

    for i in range(2):
        for j in range(2):
            bg = "#fdebd0" if (i == 0 and j == 0) else "white"
            draw_matrix_cell(ax, x0_c + j * cell, y0_c + (1 - i) * cell,
                             cell, cell, str(C[i, j]), bg_color=bg,
                             bold=(i == 0 and j == 0))

    y_explain = 1.8
    ax.text(6, y_explain + 1, "计算 $c_{11}$（第1行 × 第1列）：",
            fontsize=13, fontweight="bold", color="#2c3e50")

    formula = (r"$c_{11} = 1 \times 7 + 2 \times 8 + 3 \times 9"
               r" = 7 + 16 + 27 = \mathbf{50}$")
    ax.text(6, y_explain, formula, fontsize=13, color="#c0392b")

    ax.annotate("", xy=(x0_a, y0_a + cell + cell / 2),
                xytext=(x0_a - 0.6, y0_a + cell + cell / 2),
                arrowprops=dict(arrowstyle="->", color="#e74c3c", lw=2))
    ax.text(x0_a - 0.8, y0_a + cell + cell / 2, "行1",
            fontsize=11, ha="right", color="#e74c3c", fontweight="bold")

    ax.annotate("", xy=(x0_b + cell / 2, y0_b + 3 * cell),
                xytext=(x0_b + cell / 2, y0_b + 3 * cell + 0.6),
                arrowprops=dict(arrowstyle="->", color="#27ae60", lw=2))
    ax.text(x0_b + cell / 2, y0_b + 3 * cell + 0.7, "列1",
            fontsize=11, ha="center", color="#27ae60", fontweight="bold")

    ax.text(6, y_explain - 1.2,
            r"一般地: $c_{ik} = \sum_{j=1}^{p} a_{ij}\,b_{jk}$  (A的第$i$行 · B的第$k$列)",
            fontsize=13, color="#7f8c8d")

    fig.suptitle("矩阵乘法: 行乘列法则", fontsize=18, fontweight="bold",
                 y=0.97)

    out = os.path.join(ABS_OUT, "p09-ch02-matrix-multiplication.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"[OK] {out}")


if __name__ == "__main__":
    plot_matrix_multiplication()
    print("Ch02 images generated successfully.")
