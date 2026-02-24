"""
向量几何可视化

生成 Part 5 Chapter 5 所需的三张图：
  1. 向量加法 (p05-ch05-vector-addition.png)
  2. 向量投影 (p05-ch05-vector-projection.png)
  3. 叉积 (p05-ch05-cross-product.png)
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


def _arrow2d(ax, origin, vec, color, label=None, lw=2.5, head_w=0.12, head_l=0.15):
    ax.annotate("", xy=(origin[0] + vec[0], origin[1] + vec[1]), xytext=origin,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=15))
    if label:
        mid = (origin[0] + vec[0] / 2, origin[1] + vec[1] / 2)
        ax.annotate(label, mid, fontsize=12, color=color, fontweight="bold",
                     ha="center", va="bottom")


def plot_vector_addition():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("向量加法：三角形法则与平行四边形法则", fontsize=14, fontweight="bold")

    u = np.array([3, 1])
    v = np.array([1, 2.5])

    ax = axes[0]
    ax.set_title("三角形法则", fontsize=12)
    _arrow2d(ax, (0, 0), u, "#2980b9", "$\\vec{u}$")
    _arrow2d(ax, u, v, "#e74c3c", "$\\vec{v}$")
    _arrow2d(ax, (0, 0), u + v, "#27ae60", "$\\vec{u}+\\vec{v}$")
    ax.plot(0, 0, "ko", ms=5)
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-0.5, 4.5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.set_title("平行四边形法则", fontsize=12)
    _arrow2d(ax, (0, 0), u, "#2980b9", "$\\vec{u}$")
    _arrow2d(ax, (0, 0), v, "#e74c3c", "$\\vec{v}$")
    ax.plot([u[0], u[0] + v[0]], [u[1], u[1] + v[1]], "--", color="#e74c3c", lw=1.5, alpha=0.5)
    ax.plot([v[0], u[0] + v[0]], [v[1], u[1] + v[1]], "--", color="#2980b9", lw=1.5, alpha=0.5)
    _arrow2d(ax, (0, 0), u + v, "#27ae60", "$\\vec{u}+\\vec{v}$")
    ax.plot(0, 0, "ko", ms=5)
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-0.5, 4.5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch05-vector-addition.png"), dpi=DPI)
    plt.close(fig)


def plot_vector_projection():
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_title("向量投影：$\\text{proj}_{\\vec{v}}\\vec{u}$",
                  fontsize=14, fontweight="bold")

    u = np.array([4, 3])
    v = np.array([5, 1])

    proj_scalar = np.dot(u, v) / np.dot(v, v)
    proj_vec = proj_scalar * v
    perp = u - proj_vec

    _arrow2d(ax, (0, 0), u, "#2980b9", "$\\vec{u}$")
    _arrow2d(ax, (0, 0), v, "#e74c3c", "$\\vec{v}$")
    _arrow2d(ax, (0, 0), proj_vec, "#27ae60", "$\\text{proj}_{\\vec{v}}\\vec{u}$")

    ax.plot([u[0], proj_vec[0]], [u[1], proj_vec[1]], "--", color="#8e44ad", lw=2)
    ax.annotate("正交分量", ((u[0] + proj_vec[0]) / 2 + 0.2, (u[1] + proj_vec[1]) / 2),
                fontsize=10, color="#8e44ad")

    angle_r = 0.4
    ax.plot([proj_vec[0] + angle_r * perp[0] / np.linalg.norm(perp),
             proj_vec[0] + angle_r * perp[0] / np.linalg.norm(perp) - angle_r * v[0] / np.linalg.norm(v),
             proj_vec[0] - angle_r * v[0] / np.linalg.norm(v)],
            [proj_vec[1] + angle_r * perp[1] / np.linalg.norm(perp),
             proj_vec[1] + angle_r * perp[1] / np.linalg.norm(perp) - angle_r * v[1] / np.linalg.norm(v),
             proj_vec[1] - angle_r * v[1] / np.linalg.norm(v)],
            "-", color="#8e44ad", lw=1.5)

    theta = np.arccos(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v)))
    arc_r = 1.0
    arc_angles = np.linspace(np.arctan2(v[1], v[0]), np.arctan2(u[1], u[0]), 30)
    ax.plot(arc_r * np.cos(arc_angles), arc_r * np.sin(arc_angles), "-", color="#f39c12", lw=2)
    ax.annotate("$\\theta$", (0.8, 0.5), fontsize=12, color="#f39c12")

    ax.annotate(
        "$\\text{proj}_{\\vec{v}}\\vec{u} = \\frac{\\vec{u}\\cdot\\vec{v}}{|\\vec{v}|^2}\\vec{v}$",
        xy=(1, 3.5), fontsize=12,
        bbox=dict(boxstyle="round,pad=0.3", fc="#eaf2f8", alpha=0.9))

    ax.plot(0, 0, "ko", ms=5)
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-0.5, 4.5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch05-vector-projection.png"), dpi=DPI)
    plt.close(fig)


def plot_cross_product():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_title("叉积：$\\vec{u} \\times \\vec{v}$ 垂直于 $\\vec{u}$ 和 $\\vec{v}$",
                  fontsize=13, fontweight="bold", pad=20)

    u = np.array([2, 0, 0])
    v = np.array([1, 2, 0])
    cross = np.cross(u, v)

    origin = np.array([0, 0, 0])

    for vec, col, lbl in [(u, "#2980b9", "$\\vec{u}$"),
                           (v, "#e74c3c", "$\\vec{v}$"),
                           (cross, "#27ae60", "$\\vec{u}\\times\\vec{v}$")]:
        ax.quiver(*origin, *vec, color=col, arrow_length_ratio=0.1, lw=3)
        ax.text(vec[0] * 1.1, vec[1] * 1.1, vec[2] * 1.1 + 0.1, lbl,
                fontsize=12, color=col, fontweight="bold")

    parallelogram = [
        [0, 0, 0],
        [u[0], u[1], u[2]],
        [u[0] + v[0], u[1] + v[1], u[2] + v[2]],
        [v[0], v[1], v[2]]
    ]
    poly = Poly3DCollection([parallelogram], alpha=0.2, facecolor="#f39c12",
                             edgecolor="#f39c12", lw=2)
    ax.add_collection3d(poly)

    area = np.linalg.norm(cross)
    ax.text(1.5, 1, -0.5,
            f"面积 = $|\\vec{{u}}\\times\\vec{{v}}| = {area:.1f}$",
            fontsize=11, color="#f39c12")

    max_val = max(np.max(np.abs(u)), np.max(np.abs(v)), np.max(np.abs(cross))) * 1.3
    ax.set_xlim([-0.5, max_val])
    ax.set_ylim([-0.5, max_val])
    ax.set_zlim([-0.5, max_val])
    ax.set_xlabel("x", fontsize=11)
    ax.set_ylabel("y", fontsize=11)
    ax.set_zlabel("z", fontsize=11)
    ax.view_init(elev=25, azim=-60)
    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch05-cross-product.png"), dpi=DPI)
    plt.close(fig)


if __name__ == "__main__":
    print("Generating ch05 images...")
    plot_vector_addition()
    print("  ✓ vector-addition")
    plot_vector_projection()
    print("  ✓ vector-projection")
    plot_cross_product()
    print("  ✓ cross-product")
    print("All ch05 images generated.")
