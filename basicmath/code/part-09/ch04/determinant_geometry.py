"""
行列式几何意义可视化

生成 Part 9 Chapter 4 所需的两张图：
  1. 行列式与面积 (p09-ch04-determinant-area.png)
  2. 行列式与体积 (p09-ch04-determinant-volume.png)
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


def plot_determinant_area():
    """2x2 行列式 = 有符号面积"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    configs = [
        {"u": (3, 0), "v": (1, 2), "title": "$\\det > 0$  (逆时针)",
         "color": "#27ae60"},
        {"u": (1, 2), "v": (3, 0), "title": "$\\det < 0$  (顺时针)",
         "color": "#e74c3c"},
        {"u": (1, 2), "v": (2, 4), "title": "$\\det = 0$  (共线)",
         "color": "#7f8c8d"},
    ]

    for ax, cfg in zip(axes, configs):
        u = np.array(cfg["u"])
        v = np.array(cfg["v"])
        det_val = u[0] * v[1] - u[1] * v[0]

        ax.set_xlim(-1, 5)
        ax.set_ylim(-1, 5.5)
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.3)
        ax.axhline(0, color="k", lw=0.5)
        ax.axvline(0, color="k", lw=0.5)

        if det_val != 0:
            pgon = plt.Polygon([
                (0, 0), u, u + v, v
            ], alpha=0.2, color=cfg["color"],
                edgecolor=cfg["color"], lw=1.5, linestyle="--")
            ax.add_patch(pgon)

        ax.annotate("", xy=u, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color="#e74c3c", lw=2.5))
        ax.annotate("", xy=v, xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", color="#3498db", lw=2.5))

        ax.text(u[0] + 0.1, u[1] - 0.35,
                f"$\\mathbf{{u}}=({u[0]},{u[1]})$",
                fontsize=11, color="#e74c3c", fontweight="bold")
        ax.text(v[0] - 0.2, v[1] + 0.2,
                f"$\\mathbf{{v}}=({v[0]},{v[1]})$",
                fontsize=11, color="#3498db", fontweight="bold")

        ax.set_title(cfg["title"], fontsize=14, fontweight="bold")
        ax.text(0.5, 5, f"det = {det_val}", fontsize=14,
                fontweight="bold", color=cfg["color"],
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                          edgecolor=cfg["color"], alpha=0.9))

        if det_val != 0:
            cx = (u[0] + v[0]) / 2
            cy = (u[1] + v[1]) / 2
            ax.text(cx, cy, f"面积 = {abs(det_val)}",
                    fontsize=12, ha="center", va="center",
                    fontweight="bold", color=cfg["color"])
        ax.set_xlabel("$x$", fontsize=12)
        ax.set_ylabel("$y$", fontsize=12)

    fig.suptitle("$2 \\times 2$ 行列式的几何意义: 有符号面积",
                 fontsize=17, fontweight="bold", y=1.02)
    plt.tight_layout()

    out = os.path.join(ABS_OUT, "p09-ch04-determinant-area.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"[OK] {out}")


def plot_determinant_volume():
    """3x3 行列式 = 平行六面体体积"""
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection="3d")

    u = np.array([2, 0, 0])
    v = np.array([1, 2, 0])
    w = np.array([0, 1, 2])

    det_val = np.linalg.det(np.column_stack([u, v, w]))

    origin = np.array([0, 0, 0])
    vertices = [
        origin, u, v, w,
        u + v, u + w, v + w,
        u + v + w
    ]

    faces = [
        [vertices[0], vertices[1], vertices[4], vertices[2]],
        [vertices[0], vertices[1], vertices[5], vertices[3]],
        [vertices[0], vertices[2], vertices[6], vertices[3]],
        [vertices[7], vertices[4], vertices[1], vertices[5]],
        [vertices[7], vertices[4], vertices[2], vertices[6]],
        [vertices[7], vertices[5], vertices[3], vertices[6]],
    ]

    face_colors = ["#e74c3c", "#3498db", "#27ae60",
                   "#e74c3c", "#3498db", "#27ae60"]

    for face, fc in zip(faces, face_colors):
        poly = Poly3DCollection([face], alpha=0.15, facecolor=fc,
                                edgecolor=fc, lw=1.5)
        ax.add_collection3d(poly)

    for vec, color, label in [
        (u, "#e74c3c", r"$\mathbf{u}=(2,0,0)$"),
        (v, "#3498db", r"$\mathbf{v}=(1,2,0)$"),
        (w, "#27ae60", r"$\mathbf{w}=(0,1,2)$"),
    ]:
        ax.quiver(*origin, *vec, color=color, arrow_length_ratio=0.1,
                  lw=3, alpha=0.9)
        ax.text(*(vec * 1.1), label, fontsize=12, color=color,
                fontweight="bold")

    ax.text(1.5, 1.5, 1.2,
            f"体积 = |det| = {abs(int(det_val))}",
            fontsize=15, fontweight="bold", color="#2c3e50",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                      edgecolor="#2c3e50", alpha=0.9))

    ax.set_xlim(0, 4)
    ax.set_ylim(0, 4)
    ax.set_zlim(0, 3)
    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$y$", fontsize=12)
    ax.set_zlabel("$z$", fontsize=12)
    ax.set_title("$3 \\times 3$ 行列式的几何意义: 平行六面体的有符号体积",
                 fontsize=15, fontweight="bold", pad=15)
    ax.view_init(elev=22, azim=35)

    out = os.path.join(ABS_OUT, "p09-ch04-determinant-volume.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"[OK] {out}")


if __name__ == "__main__":
    plot_determinant_area()
    plot_determinant_volume()
    print("Ch04 images generated successfully.")
