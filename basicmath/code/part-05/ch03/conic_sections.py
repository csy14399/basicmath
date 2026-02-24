"""
圆锥曲线可视化

生成 Part 5 Chapter 3 所需的六张图：
  1. 椭圆 (p05-ch03-ellipse.png)
  2. 椭圆反射性质 (p05-ch03-ellipse-reflection.png)
  3. 双曲线 (p05-ch03-hyperbola.png)
  4. 抛物线 (p05-ch03-parabola.png)
  5. 圆锥曲线统一 (p05-ch03-conic-sections-unified.png)
  6. 离心率谱 (p05-ch03-eccentricity-spectrum.png)
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


def plot_ellipse():
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_title("椭圆：$\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$", fontsize=14, fontweight="bold")

    a, b = 4, 3
    c = np.sqrt(a**2 - b**2)
    t = np.linspace(0, 2 * np.pi, 500)
    ax.plot(a * np.cos(t), b * np.sin(t), "-", color="#2980b9", lw=2.5)

    ax.plot(c, 0, "o", color="#e74c3c", ms=8, zorder=5)
    ax.plot(-c, 0, "o", color="#e74c3c", ms=8, zorder=5)
    ax.annotate("$F_1(-c, 0)$", (-c - 0.2, -0.5), fontsize=10, color="#e74c3c", ha="center")
    ax.annotate("$F_2(c, 0)$", (c + 0.2, -0.5), fontsize=10, color="#e74c3c", ha="center")

    ax.plot(a, 0, "s", color="#27ae60", ms=6)
    ax.plot(-a, 0, "s", color="#27ae60", ms=6)
    ax.plot(0, b, "s", color="#27ae60", ms=6)
    ax.plot(0, -b, "s", color="#27ae60", ms=6)
    ax.annotate("$(a, 0)$", (a + 0.2, 0.3), fontsize=9, color="#27ae60")
    ax.annotate("$(0, b)$", (0.2, b + 0.2), fontsize=9, color="#27ae60")

    P_t = np.radians(55)
    P = np.array([a * np.cos(P_t), b * np.sin(P_t)])
    ax.plot(*P, "o", color="#8e44ad", ms=7, zorder=5)
    ax.annotate("$P$", P + np.array([0.15, 0.15]), fontsize=11, color="#8e44ad")
    ax.plot([P[0], -c], [P[1], 0], "--", color="#e74c3c", lw=1.2, alpha=0.7)
    ax.plot([P[0], c], [P[1], 0], "--", color="#e74c3c", lw=1.2, alpha=0.7)

    ax.annotate("$|PF_1| + |PF_2| = 2a$", xy=(0, -b - 0.8), fontsize=11,
                ha="center", bbox=dict(boxstyle="round,pad=0.3", fc="#eaf2f8", alpha=0.9))

    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_aspect("equal")
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-4.5, 4.5)
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch03-ellipse.png"), dpi=DPI)
    plt.close(fig)


def plot_ellipse_reflection():
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_title("椭圆的光学反射性质", fontsize=14, fontweight="bold")

    a, b = 4, 3
    c = np.sqrt(a**2 - b**2)
    t = np.linspace(0, 2 * np.pi, 500)
    ax.plot(a * np.cos(t), b * np.sin(t), "-", color="#2980b9", lw=2.5)
    ax.plot(c, 0, "o", color="#e74c3c", ms=8)
    ax.plot(-c, 0, "o", color="#e74c3c", ms=8)
    ax.annotate("$F_1$", (-c, -0.5), fontsize=11, ha="center", color="#e74c3c")
    ax.annotate("$F_2$", (c, -0.5), fontsize=11, ha="center", color="#e74c3c")

    for t_val in [0.4, 1.0, 1.8, 2.5, 3.2, 4.0, 4.8, 5.5]:
        P = np.array([a * np.cos(t_val), b * np.sin(t_val)])
        ax.plot([c, P[0]], [0, P[1]], "-", color="#f39c12", lw=1.3, alpha=0.7)
        ax.plot([P[0], -c], [P[1], 0], "-", color="#f39c12", lw=1.3, alpha=0.7)

    ax.annotate("从 $F_1$ 出发的光线\n经椭圆反射后\n全部汇聚到 $F_2$", xy=(0, -b - 0.6),
                fontsize=10, ha="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="#fef9e7", alpha=0.9))

    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_aspect("equal")
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-4.5, 4.5)
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch03-ellipse-reflection.png"), dpi=DPI)
    plt.close(fig)


def plot_hyperbola():
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.set_title("双曲线：$\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$",
                  fontsize=14, fontweight="bold")

    a, b = 3, 2
    c = np.sqrt(a**2 + b**2)

    t = np.linspace(-2, 2, 500)
    ax.plot(a * np.cosh(t), b * np.sinh(t), "-", color="#2980b9", lw=2.5)
    ax.plot(-a * np.cosh(t), b * np.sinh(t), "-", color="#2980b9", lw=2.5)

    x_asy = np.linspace(-6, 6, 100)
    ax.plot(x_asy, (b / a) * x_asy, "--", color="#95a5a6", lw=1.5,
            label=f"渐近线 $y = \\pm\\frac{{{b}}}{{{a}}}x$")
    ax.plot(x_asy, -(b / a) * x_asy, "--", color="#95a5a6", lw=1.5)

    ax.plot(c, 0, "o", color="#e74c3c", ms=8, zorder=5)
    ax.plot(-c, 0, "o", color="#e74c3c", ms=8, zorder=5)
    ax.annotate("$F_1$", (-c, -0.6), fontsize=11, ha="center", color="#e74c3c")
    ax.annotate("$F_2$", (c, -0.6), fontsize=11, ha="center", color="#e74c3c")

    ax.plot(a, 0, "s", color="#27ae60", ms=6)
    ax.plot(-a, 0, "s", color="#27ae60", ms=6)

    ax.annotate("$||PF_1| - |PF_2|| = 2a$", xy=(0, -5.5), fontsize=11,
                ha="center", bbox=dict(boxstyle="round,pad=0.3", fc="#eaf2f8", alpha=0.9))

    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_aspect("equal")
    ax.set_xlim(-7, 7)
    ax.set_ylim(-6, 6)
    ax.legend(fontsize=10, loc="upper left")
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch03-hyperbola.png"), dpi=DPI)
    plt.close(fig)


def plot_parabola():
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set_title("抛物线：$y^2 = 4px$", fontsize=14, fontweight="bold")

    p = 1.5
    t = np.linspace(-4, 4, 500)
    y_vals = t
    x_vals = y_vals**2 / (4 * p)
    ax.plot(x_vals, y_vals, "-", color="#2980b9", lw=2.5)

    ax.plot(p, 0, "o", color="#e74c3c", ms=8, zorder=5)
    ax.annotate("$F(p, 0)$", (p + 0.2, -0.5), fontsize=11, color="#e74c3c")

    ax.axvline(-p, color="#27ae60", lw=2, ls="--", label=f"准线 $x = -p$")
    ax.annotate("准线", (-p - 0.3, 3.5), fontsize=10, color="#27ae60", rotation=90)

    for y_p in [1.5, 3.0]:
        x_p = y_p**2 / (4 * p)
        ax.plot(x_p, y_p, "o", color="#8e44ad", ms=6, zorder=5)
        ax.plot([x_p, p], [y_p, 0], "--", color="#e74c3c", lw=1.2, alpha=0.7)
        ax.plot([x_p, -p], [y_p, y_p], "--", color="#27ae60", lw=1.2, alpha=0.7)

    for y_r in [1, 2, 3]:
        x_r = y_r**2 / (4 * p)
        ax.annotate("", xy=(p, 0), xytext=(x_r, y_r),
                     arrowprops=dict(arrowstyle="->", color="#f39c12", lw=1.2, alpha=0.5))
        ax.plot([6, x_r], [y_r, y_r], "-", color="#f39c12", lw=1.2, alpha=0.5)

    ax.annotate("平行光 → 焦点", xy=(4.5, 3.5), fontsize=10, color="#f39c12",
                bbox=dict(boxstyle="round,pad=0.3", fc="#fef9e7", alpha=0.9))

    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_xlim(-3, 7)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.legend(fontsize=10)
    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch03-parabola.png"), dpi=DPI)
    plt.close(fig)


def plot_unified():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_title("圆锥曲线的统一：焦点-准线定义", fontsize=14, fontweight="bold")

    F = np.array([0, 0])
    ax.plot(*F, "o", color="#e74c3c", ms=8, zorder=5)
    ax.annotate("$F$（焦点）", (0.2, -0.4), fontsize=11, color="#e74c3c")

    directrix_x = -2
    ax.axvline(directrix_x, color="#95a5a6", lw=2, ls="--")
    ax.annotate("准线 $\\ell$", (directrix_x - 0.3, 5.5), fontsize=10, color="#95a5a6", rotation=90)

    eccentricities = [
        (0.5, "#3498db", "椭圆 $e=0.5$"),
        (1.0, "#27ae60", "抛物线 $e=1$"),
        (1.5, "#e74c3c", "双曲线 $e=1.5$"),
    ]

    for e, col, label in eccentricities:
        thetas = np.linspace(-np.pi * 0.85, np.pi * 0.85, 800)
        d = abs(directrix_x)
        rs = []
        xs_plot = []
        ys_plot = []
        for th in thetas:
            denom = 1 - e * np.cos(th)
            if abs(denom) < 0.01:
                continue
            r = e * d / denom
            if r < 0 or r > 15:
                continue
            xs_plot.append(r * np.cos(th))
            ys_plot.append(r * np.sin(th))
        ax.plot(xs_plot, ys_plot, "-", color=col, lw=2.5, label=label)

    ax.set_xlim(-4, 8)
    ax.set_ylim(-6, 6)
    ax.set_aspect("equal")
    ax.legend(fontsize=11, loc="upper right")
    ax.grid(True, alpha=0.2)
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch03-conic-sections-unified.png"), dpi=DPI)
    plt.close(fig)


def plot_eccentricity_spectrum():
    fig, ax = plt.subplots(figsize=(12, 3.5))
    ax.set_title("离心率谱：从圆到双曲线", fontsize=14, fontweight="bold")

    e_vals = [0, 0.3, 0.6, 0.9, 1.0, 1.5, 3.0]
    labels = ["圆\n$e=0$", "椭圆\n$e=0.3$", "椭圆\n$e=0.6$", "椭圆\n$e=0.9$",
              "抛物线\n$e=1$", "双曲线\n$e=1.5$", "双曲线\n$e=3$"]
    colors_bar = ["#2980b9", "#3498db", "#5dade2", "#85c1e9",
                  "#27ae60", "#e74c3c", "#c0392b"]

    positions = np.linspace(0, 6, 7)
    ax.barh([0] * 7, [0.8] * 7, left=positions - 0.4, height=0.5,
            color=colors_bar, edgecolor="#2c3e50", lw=1)

    for pos, lbl in zip(positions, labels):
        ax.text(pos, -0.6, lbl, ha="center", fontsize=9, va="top")

    ax.arrow(0, 0.5, 5.8, 0, head_width=0.15, head_length=0.15,
             fc="#2c3e50", ec="#2c3e50")
    ax.text(3, 0.85, "离心率 $e$ 增大 →", ha="center", fontsize=11, fontweight="bold")

    ax.set_xlim(-0.8, 7)
    ax.set_ylim(-1.5, 1.3)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch03-eccentricity-spectrum.png"), dpi=DPI)
    plt.close(fig)


if __name__ == "__main__":
    print("Generating ch03 images...")
    plot_ellipse()
    print("  ✓ ellipse")
    plot_ellipse_reflection()
    print("  ✓ ellipse-reflection")
    plot_hyperbola()
    print("  ✓ hyperbola")
    plot_parabola()
    print("  ✓ parabola")
    plot_unified()
    print("  ✓ conic-sections-unified")
    plot_eccentricity_spectrum()
    print("  ✓ eccentricity-spectrum")
    print("All ch03 images generated.")
