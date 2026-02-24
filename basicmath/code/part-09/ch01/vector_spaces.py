"""
向量空间可视化

生成 Part 9 Chapter 1 所需的两张图：
  1. 线性相关 vs 线性无关 (p09-ch01-linear-independence-2d.png)
  2. 三维空间中的基 (p09-ch01-basis-3d.png)
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


def plot_linear_independence_2d():
    """线性相关 vs 线性无关的向量 — 2D"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: linearly dependent (collinear)
    ax = axes[0]
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color="k", lw=0.5)
    ax.axvline(0, color="k", lw=0.5)

    u = np.array([1, 2])
    v = np.array([2, 4])

    ax.annotate("", xy=u, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="#e74c3c", lw=2.5))
    ax.annotate("", xy=v, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="#3498db", lw=2.5))

    ax.text(u[0] - 0.3, u[1] + 0.2, r"$\mathbf{u}=(1,2)$", fontsize=12,
            color="#e74c3c", fontweight="bold")
    ax.text(v[0] + 0.1, v[1] + 0.2, r"$\mathbf{v}=(2,4)=2\mathbf{u}$",
            fontsize=12, color="#3498db", fontweight="bold")

    t = np.linspace(-0.5, 2.5, 50)
    ax.plot(t * 1, t * 2, "--", color="gray", alpha=0.5, lw=1)

    ax.set_title("线性相关（共线）", fontsize=15, fontweight="bold")
    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$y$", fontsize=12)

    # Right: linearly independent
    ax = axes[1]
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 4)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color="k", lw=0.5)
    ax.axvline(0, color="k", lw=0.5)

    u = np.array([3, 1])
    v = np.array([1, 2])

    ax.annotate("", xy=u, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="#e74c3c", lw=2.5))
    ax.annotate("", xy=v, xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="#3498db", lw=2.5))

    parallelogram = plt.Polygon([
        (0, 0), u, u + v, v
    ], alpha=0.15, color="#27ae60", edgecolor="#27ae60", lw=1.5)
    ax.add_patch(parallelogram)

    ax.text(u[0] + 0.1, u[1] - 0.3, r"$\mathbf{u}=(3,1)$", fontsize=12,
            color="#e74c3c", fontweight="bold")
    ax.text(v[0] - 0.8, v[1] + 0.1, r"$\mathbf{v}=(1,2)$", fontsize=12,
            color="#3498db", fontweight="bold")
    ax.text((u[0] + v[0]) / 2, (u[1] + v[1]) / 2 + 0.2,
            r"$\mathrm{span}\{\mathbf{u},\mathbf{v}\}=\mathbb{R}^2$",
            fontsize=11, ha="center", color="#27ae60", fontweight="bold")

    ax.set_title("线性无关（不共线）", fontsize=15, fontweight="bold")
    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$y$", fontsize=12)

    fig.suptitle("$\\mathbb{R}^2$ 中的线性相关与线性无关", fontsize=17,
                 fontweight="bold", y=1.02)
    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p09-ch01-linear-independence-2d.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"[OK] {out}")


def plot_basis_3d():
    """三维空间中的标准基和线性组合"""
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection="3d")

    origin = np.array([0, 0, 0])
    e1 = np.array([1, 0, 0])
    e2 = np.array([0, 1, 0])
    e3 = np.array([0, 0, 1])

    colors = ["#e74c3c", "#3498db", "#27ae60"]
    labels = [r"$\mathbf{e}_1=(1,0,0)$", r"$\mathbf{e}_2=(0,1,0)$",
              r"$\mathbf{e}_3=(0,0,1)$"]
    vecs = [e1, e2, e3]

    for vec, color, label in zip(vecs, colors, labels):
        ax.quiver(*origin, *vec, color=color, arrow_length_ratio=0.12,
                  lw=3, alpha=0.9)
        ax.text(*(vec * 1.15), label, fontsize=11, color=color,
                fontweight="bold")

    target = np.array([2, 3, 1])
    ax.quiver(*origin, *target, color="#8e44ad", arrow_length_ratio=0.08,
              lw=2.5, alpha=0.8)
    ax.text(*(target * 1.1), r"$\mathbf{v}=(2,3,1)$", fontsize=12,
            color="#8e44ad", fontweight="bold")

    ax.plot([0, 2], [0, 0], [0, 0], "--", color="#e74c3c", alpha=0.4, lw=1)
    ax.plot([2, 2], [0, 3], [0, 0], "--", color="#3498db", alpha=0.4, lw=1)
    ax.plot([2, 2], [3, 3], [0, 1], "--", color="#27ae60", alpha=0.4, lw=1)

    ax.text(1, -0.3, -0.15, r"$2\mathbf{e}_1$", fontsize=10, color="#e74c3c")
    ax.text(2.1, 1.5, -0.15, r"$3\mathbf{e}_2$", fontsize=10, color="#3498db")
    ax.text(2.15, 3.1, 0.5, r"$1\mathbf{e}_3$", fontsize=10, color="#27ae60")

    ax.set_xlim(0, 3)
    ax.set_ylim(0, 4)
    ax.set_zlim(0, 2)
    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$y$", fontsize=12)
    ax.set_zlabel("$z$", fontsize=12)
    ax.set_title(r"$\mathbb{R}^3$ 的标准基: $\mathbf{v} = 2\mathbf{e}_1 + 3\mathbf{e}_2 + 1\mathbf{e}_3$",
                 fontsize=15, fontweight="bold", pad=15)
    ax.view_init(elev=20, azim=30)

    out = os.path.join(ABS_OUT, "p09-ch01-basis-3d.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"[OK] {out}")


if __name__ == "__main__":
    plot_linear_independence_2d()
    plot_basis_3d()
    print("Ch01 images generated successfully.")
