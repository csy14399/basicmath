"""
对称群可视化

生成 Part 3 Chapter 5 所需的一张图：
  等边三角形的 6 个对称变换
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


def equilateral_triangle(center=(0, 0), radius=1.0, rotation_deg=0):
    """Return vertices of equilateral triangle."""
    angles = np.array([90, 210, 330]) + rotation_deg
    angles_rad = np.deg2rad(angles)
    xs = center[0] + radius * np.cos(angles_rad)
    ys = center[1] + radius * np.sin(angles_rad)
    return list(zip(xs, ys))


def draw_triangle(ax, verts, labels, face_color, edge_color, alpha=0.3):
    """Draw triangle with vertex labels."""
    tri = patches.Polygon(verts, closed=True, facecolor=face_color,
                          edgecolor=edge_color, linewidth=2, alpha=alpha, zorder=2)
    ax.add_patch(tri)
    for (x, y), lbl in zip(verts, labels):
        dx = x - np.mean([v[0] for v in verts])
        dy = y - np.mean([v[1] for v in verts])
        norm = np.sqrt(dx**2 + dy**2) + 1e-9
        ox = x + 0.18 * dx / norm
        oy = y + 0.18 * dy / norm
        ax.text(ox, oy, lbl, fontsize=13, fontweight="bold", ha="center", va="center",
                color=edge_color, zorder=6)
    xs = [v[0] for v in verts] + [verts[0][0]]
    ys = [v[1] for v in verts] + [verts[0][1]]
    ax.plot(xs, ys, "-", color=edge_color, lw=2, zorder=3)


def plot_symmetry_group():
    """等边三角形的 6 个对称变换。"""
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle("等边三角形的对称群 $D_3 \\cong S_3$（6 个对称变换）",
                 fontsize=15, fontweight="bold")

    base_verts = equilateral_triangle(radius=0.85)
    v1, v2, v3 = base_verts

    transformations = [
        {
            "name": "$e$（恒等）",
            "labels": ["1", "2", "3"],
            "desc": "$1 \\to 1,\\; 2 \\to 2,\\; 3 \\to 3$",
            "extra": None,
        },
        {
            "name": "$r$（旋转 $120°$）",
            "labels": ["2", "3", "1"],
            "desc": "$1 \\to 2,\\; 2 \\to 3,\\; 3 \\to 1$",
            "extra": "rotation",
        },
        {
            "name": "$r^2$（旋转 $240°$）",
            "labels": ["3", "1", "2"],
            "desc": "$1 \\to 3,\\; 2 \\to 1,\\; 3 \\to 2$",
            "extra": "rotation2",
        },
        {
            "name": "$s_1$（过顶点 1 的反射）",
            "labels": ["1", "3", "2"],
            "desc": "$1 \\to 1,\\; 2 \\leftrightarrow 3$",
            "extra": "reflect1",
        },
        {
            "name": "$s_2$（过顶点 2 的反射）",
            "labels": ["3", "2", "1"],
            "desc": "$2 \\to 2,\\; 1 \\leftrightarrow 3$",
            "extra": "reflect2",
        },
        {
            "name": "$s_3$（过顶点 3 的反射）",
            "labels": ["2", "1", "3"],
            "desc": "$3 \\to 3,\\; 1 \\leftrightarrow 2$",
            "extra": "reflect3",
        },
    ]

    colors = ["#2c3e50", "#2980b9", "#27ae60", "#e74c3c", "#8e44ad", "#e67e22"]

    for ax, trans, clr in zip(axes.flat, transformations, colors):
        ax.set_xlim(-1.4, 1.4)
        ax.set_ylim(-1.2, 1.3)
        ax.set_aspect("equal")
        ax.axis("off")

        draw_triangle(ax, base_verts, trans["labels"], clr, clr, alpha=0.15)

        for v in base_verts:
            ax.plot(v[0], v[1], "o", color=clr, markersize=7, zorder=5)

        center = (0, np.mean([v[1] for v in base_verts]))
        cx = np.mean([v[0] for v in base_verts])
        cy = np.mean([v[1] for v in base_verts])

        extra = trans["extra"]
        if extra == "rotation":
            arc_theta = np.linspace(np.pi/2, np.pi/2 - 2*np.pi/3, 30)
            r_arc = 0.35
            ax.plot(cx + r_arc * np.cos(arc_theta), cy + r_arc * np.sin(arc_theta),
                    color=clr, lw=1.5)
            ax.annotate("", xy=(cx + r_arc * np.cos(arc_theta[-1]),
                                cy + r_arc * np.sin(arc_theta[-1])),
                        xytext=(cx + r_arc * np.cos(arc_theta[-3]),
                                cy + r_arc * np.sin(arc_theta[-3])),
                        arrowprops=dict(arrowstyle="->", color=clr, lw=1.5))
        elif extra == "rotation2":
            arc_theta = np.linspace(np.pi/2, np.pi/2 - 4*np.pi/3, 40)
            r_arc = 0.35
            ax.plot(cx + r_arc * np.cos(arc_theta), cy + r_arc * np.sin(arc_theta),
                    color=clr, lw=1.5)
            ax.annotate("", xy=(cx + r_arc * np.cos(arc_theta[-1]),
                                cy + r_arc * np.sin(arc_theta[-1])),
                        xytext=(cx + r_arc * np.cos(arc_theta[-3]),
                                cy + r_arc * np.sin(arc_theta[-3])),
                        arrowprops=dict(arrowstyle="->", color=clr, lw=1.5))
        elif extra and extra.startswith("reflect"):
            idx = int(extra[-1]) - 1
            vx, vy = base_verts[idx]
            opp_x = (base_verts[(idx+1) % 3][0] + base_verts[(idx+2) % 3][0]) / 2
            opp_y = (base_verts[(idx+1) % 3][1] + base_verts[(idx+2) % 3][1]) / 2
            ext = 0.25
            dx, dy = vx - opp_x, vy - opp_y
            norm_d = np.sqrt(dx**2 + dy**2) + 1e-9
            dx, dy = dx / norm_d, dy / norm_d
            ax.plot([opp_x - ext * dx, vx + ext * dx],
                    [opp_y - ext * dy, vy + ext * dy],
                    "--", color=clr, lw=1.5, alpha=0.7)

        ax.set_title(trans["name"], fontsize=12, fontweight="bold", color=clr, pad=8)
        ax.text(0, -1.1, trans["desc"], ha="center", fontsize=9, color="#555",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=clr, alpha=0.7))

    fig.tight_layout(rect=[0, 0, 1, 0.93])
    out = os.path.join(ABS_OUT, "p03-ch05-symmetry-group.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ {out}")


if __name__ == "__main__":
    print("Part 3 Ch05: 对称群可视化")
    plot_symmetry_group()
    print("  完成！")
