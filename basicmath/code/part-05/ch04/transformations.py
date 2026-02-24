"""
变换几何可视化

生成 Part 5 Chapter 4 所需的两张图：
  1. 四种基本变换效果 (p05-ch04-transformation-effects.png)
  2. 变换的复合 (p05-ch04-transformation-composition.png)
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import numpy as np

_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

ABS_OUT = "/workspace/basicmath/images/code-generated"
os.makedirs(ABS_OUT, exist_ok=True)
DPI = 200


def _draw_shape(ax, pts, color, label=None, fill_alpha=0.15, lw=2, ls="-"):
    xs = [p[0] for p in pts] + [pts[0][0]]
    ys = [p[1] for p in pts] + [pts[0][1]]
    ax.fill(xs, ys, alpha=fill_alpha, color=color)
    ax.plot(xs, ys, ls, color=color, lw=lw, label=label)
    for p in pts:
        ax.plot(*p, "o", color=color, ms=4)


def plot_transformation_effects():
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    fig.suptitle("四种基本几何变换", fontsize=15, fontweight="bold")

    original = np.array([(1, 1), (3, 1), (3, 3), (1, 3)])
    letter_F = np.array([(1.3, 1.2), (1.3, 2.8), (2.5, 2.8), (2.5, 2.4),
                          (1.7, 2.4), (1.7, 2.1), (2.2, 2.1), (2.2, 1.8),
                          (1.7, 1.8), (1.7, 1.2)])

    # Translation
    ax = axes[0, 0]
    ax.set_title("平移（Translation）：$(x,y) \\mapsto (x+3, y+2)$", fontsize=11)
    _draw_shape(ax, original, "#3498db", "原图形")
    _draw_shape(ax, letter_F, "#3498db", fill_alpha=0.3)
    translated = original + np.array([3, 2])
    letter_F_t = letter_F + np.array([3, 2])
    _draw_shape(ax, translated, "#e74c3c", "像")
    _draw_shape(ax, letter_F_t, "#e74c3c", fill_alpha=0.3)
    for o, t in zip(original, translated):
        ax.annotate("", xy=t, xytext=o,
                     arrowprops=dict(arrowstyle="->", color="#95a5a6", lw=1))
    ax.set_xlim(-0.5, 8)
    ax.set_ylim(-0.5, 7)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.legend(fontsize=9)

    # Rotation
    ax = axes[0, 1]
    ax.set_title("旋转（Rotation）：绕原点逆时针 $60°$", fontsize=11)
    _draw_shape(ax, original, "#3498db", "原图形")
    _draw_shape(ax, letter_F, "#3498db", fill_alpha=0.3)
    theta = np.radians(60)
    R = np.array([[np.cos(theta), -np.sin(theta)],
                   [np.sin(theta), np.cos(theta)]])
    rotated = (R @ original.T).T
    letter_F_r = (R @ letter_F.T).T
    _draw_shape(ax, rotated, "#e74c3c", "像")
    _draw_shape(ax, letter_F_r, "#e74c3c", fill_alpha=0.3)
    ax.plot(0, 0, "ko", ms=6)
    ax.annotate("O (旋转中心)", (0.1, -0.4), fontsize=9)
    arc = np.linspace(0, theta, 30)
    ax.plot(0.7 * np.cos(arc), 0.7 * np.sin(arc), "-", color="#f39c12", lw=2)
    ax.annotate("60°", (0.5, 0.5), fontsize=10, color="#f39c12")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1.5, 5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.legend(fontsize=9)

    # Reflection
    ax = axes[1, 0]
    ax.set_title("反射（Reflection）：关于 $y$ 轴", fontsize=11)
    _draw_shape(ax, original, "#3498db", "原图形")
    _draw_shape(ax, letter_F, "#3498db", fill_alpha=0.3)
    reflected = original * np.array([-1, 1])
    letter_F_ref = letter_F * np.array([-1, 1])
    _draw_shape(ax, reflected, "#e74c3c", "像（手性反转）")
    _draw_shape(ax, letter_F_ref, "#e74c3c", fill_alpha=0.3)
    ax.axvline(0, color="#27ae60", lw=2, ls="--", label="反射轴 ($y$ 轴)")
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.legend(fontsize=9, loc="lower left")

    # Dilation
    ax = axes[1, 1]
    ax.set_title("缩放（Dilation）：以原点为中心，$k=1.5$", fontsize=11)
    _draw_shape(ax, original, "#3498db", "原图形")
    _draw_shape(ax, letter_F, "#3498db", fill_alpha=0.3)
    k = 1.5
    scaled = original * k
    letter_F_s = letter_F * k
    _draw_shape(ax, scaled, "#e74c3c", "像")
    _draw_shape(ax, letter_F_s, "#e74c3c", fill_alpha=0.3)
    ax.plot(0, 0, "ko", ms=6)
    ax.annotate("O (缩放中心)", (0.1, -0.4), fontsize=9)
    for o, s in zip(original, scaled):
        ax.plot([0, s[0]], [0, s[1]], "--", color="#95a5a6", lw=0.8, alpha=0.5)
    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-1, 6)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.legend(fontsize=9)

    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch04-transformation-effects.png"), dpi=DPI)
    plt.close(fig)


def plot_transformation_composition():
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle("两次反射 = 旋转（交于一点的两反射轴，夹角 α → 旋转 2α）",
                  fontsize=13, fontweight="bold")

    original = np.array([(1.5, 0.5), (2.5, 0.5), (2.5, 2), (1.5, 1.5)])
    letter_pts = np.array([(1.7, 0.7), (1.7, 1.8), (2.3, 1.8), (2.3, 1.5), (1.9, 1.5),
                            (1.9, 1.3), (2.2, 1.3), (2.2, 1.0), (1.9, 1.0), (1.9, 0.7)])

    alpha = np.radians(30)

    def reflect_line(pts, angle):
        c2, s2 = np.cos(2 * angle), np.sin(2 * angle)
        M = np.array([[c2, s2], [s2, -c2]])
        return (M @ pts.T).T

    ax = axes[0]
    ax.set_title("第一步：关于 $\\ell_1$（$x$ 轴）反射", fontsize=11)
    _draw_shape(ax, original, "#3498db", "原图形")
    _draw_shape(ax, letter_pts, "#3498db", fill_alpha=0.3)
    step1 = reflect_line(original, 0)
    letter_s1 = reflect_line(letter_pts, 0)
    _draw_shape(ax, step1, "#f39c12", "反射 1 后")
    _draw_shape(ax, letter_s1, "#f39c12", fill_alpha=0.3)
    ax.axhline(0, color="#27ae60", lw=2.5, label="$\\ell_1$: $x$ 轴")
    x_line = np.linspace(-1, 4, 100)
    ax.plot(x_line, np.tan(alpha) * x_line, "--", color="#8e44ad", lw=2,
            label=f"$\\ell_2$: 角度 {int(np.degrees(alpha))}°")
    ax.set_xlim(-1, 4)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.legend(fontsize=9)

    ax = axes[1]
    ax.set_title(f"第二步：关于 $\\ell_2$（{int(np.degrees(alpha))}° 线）反射", fontsize=11)
    _draw_shape(ax, step1, "#f39c12", "反射 1 后")
    _draw_shape(ax, letter_s1, "#f39c12", fill_alpha=0.3)
    step2 = reflect_line(step1, alpha)
    letter_s2 = reflect_line(letter_s1, alpha)
    _draw_shape(ax, step2, "#e74c3c", "反射 2 后")
    _draw_shape(ax, letter_s2, "#e74c3c", fill_alpha=0.3)
    ax.axhline(0, color="#27ae60", lw=2.5, label="$\\ell_1$")
    ax.plot(x_line, np.tan(alpha) * x_line, "--", color="#8e44ad", lw=2, label="$\\ell_2$")
    ax.set_xlim(-1, 4)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.legend(fontsize=9)

    ax = axes[2]
    ax.set_title(f"等价：绕原点旋转 $2\\alpha = {int(2 * np.degrees(alpha))}°$", fontsize=11)
    _draw_shape(ax, original, "#3498db", "原图形")
    _draw_shape(ax, letter_pts, "#3498db", fill_alpha=0.3)
    _draw_shape(ax, step2, "#e74c3c", "两次反射 = 旋转")
    _draw_shape(ax, letter_s2, "#e74c3c", fill_alpha=0.3)

    rot_angle = 2 * alpha
    R_mat = np.array([[np.cos(rot_angle), -np.sin(rot_angle)],
                       [np.sin(rot_angle), np.cos(rot_angle)]])
    direct_rot = (R_mat @ original.T).T
    _draw_shape(ax, direct_rot, "#27ae60", f"直接旋转 {int(np.degrees(rot_angle))}°", ls="--", lw=1.5)

    ax.plot(0, 0, "ko", ms=6)
    arc_t = np.linspace(0, rot_angle, 30)
    ax.plot(0.5 * np.cos(arc_t), 0.5 * np.sin(arc_t), "-", color="#f39c12", lw=2.5)
    ax.annotate(f"2α={int(np.degrees(rot_angle))}°", (0.6, 0.4), fontsize=10, color="#f39c12")
    ax.set_xlim(-1, 4)
    ax.set_ylim(-3, 3)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.legend(fontsize=9)

    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch04-transformation-composition.png"), dpi=DPI)
    plt.close(fig)


if __name__ == "__main__":
    print("Generating ch04 images...")
    plot_transformation_effects()
    print("  ✓ transformation-effects")
    plot_transformation_composition()
    print("  ✓ transformation-composition")
    print("All ch04 images generated.")
