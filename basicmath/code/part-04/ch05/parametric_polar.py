"""
参数方程与极坐标可视化

生成 Part 4 Chapter 5 所需的两张图：
  1. 经典参数曲线（圆、椭圆、摆线、Lissajous）
  2. 经典极坐标曲线（心形线、玫瑰线、螺旋线、双纽线）
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


def plot_parametric_examples():
    """经典参数曲线：圆、椭圆、摆线、Lissajous。"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    fig.suptitle("经典参数曲线", fontsize=15, fontweight="bold")

    # Circle
    ax = axes[0, 0]
    ax.set_title("圆：$x = \\cos t, \\; y = \\sin t$", fontsize=12, pad=8)
    t = np.linspace(0, 2*np.pi, 500)
    ax.plot(np.cos(t), np.sin(t), color="#2980b9", lw=2.5)
    arrow_idx = 100
    ax.annotate("", xy=(np.cos(t[arrow_idx+5]), np.sin(t[arrow_idx+5])),
                xytext=(np.cos(t[arrow_idx]), np.sin(t[arrow_idx])),
                arrowprops=dict(arrowstyle="-|>", color="#e74c3c", lw=2))
    ax.annotate("逆时针", xy=(0.3, 0.8), fontsize=10, color="#e74c3c")
    angle = np.pi/4
    ax.plot([0, np.cos(angle)], [0, np.sin(angle)], "--", color="#27ae60", lw=1.5)
    ax.plot(np.cos(angle), np.sin(angle), "o", color="#e74c3c", ms=6)
    ax.annotate(f"$t = \\pi/4$", xy=(np.cos(angle)+0.08, np.sin(angle)+0.05),
                fontsize=10, color="#e74c3c")
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    # Ellipse
    ax = axes[0, 1]
    ax.set_title("椭圆：$x = 3\\cos t, \\; y = 2\\sin t$", fontsize=12, pad=8)
    a_e, b_e = 3, 2
    ax.plot(a_e*np.cos(t), b_e*np.sin(t), color="#e74c3c", lw=2.5)
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    c_e = np.sqrt(a_e**2 - b_e**2)
    ax.plot(c_e, 0, "x", color="#27ae60", ms=10, mew=2)
    ax.plot(-c_e, 0, "x", color="#27ae60", ms=10, mew=2)
    ax.annotate("焦点", xy=(c_e+0.1, -0.3), fontsize=9, color="#27ae60")
    ax.annotate(f"$a = {a_e}, b = {b_e}$", xy=(0, -2.6), fontsize=10, ha="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="#fdedec", alpha=0.9))
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-3, 3)

    # Cycloid
    ax = axes[1, 0]
    ax.set_title("摆线：$x = t - \\sin t, \\; y = 1 - \\cos t$", fontsize=12, pad=8)
    t_cyc = np.linspace(0, 4*np.pi, 1000)
    r = 1
    ax.plot(r*(t_cyc - np.sin(t_cyc)), r*(1 - np.cos(t_cyc)), color="#8e44ad", lw=2.5)

    for k in range(5):
        t_center = 2*np.pi*k + np.pi
        if r*(2*np.pi*k) < r*4*np.pi:
            circle_theta = np.linspace(0, 2*np.pi, 100)
            cx = r*2*np.pi*k + r*np.pi
            if cx <= r*4*np.pi:
                pass

    cusps_t = [0, 2*np.pi, 4*np.pi]
    for ct in cusps_t:
        ax.plot(r*(ct-np.sin(ct)), r*(1-np.cos(ct)), "o", color="#e74c3c", ms=6)
    ax.annotate("尖点 (cusp)", xy=(0.2, 0.2), fontsize=9, color="#e74c3c")

    top_t = np.pi
    ax.plot(r*(top_t-np.sin(top_t)), r*(1-np.cos(top_t)), "s", color="#27ae60", ms=7)
    ax.annotate("最高点", xy=(np.pi+0.2, 2.1), fontsize=9, color="#27ae60")

    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-0.5, 13)
    ax.set_ylim(-0.5, 3)

    # Lissajous curves
    ax = axes[1, 1]
    ax.set_title("Lissajous 曲线", fontsize=12, pad=8)
    t_lis = np.linspace(0, 2*np.pi, 2000)
    configs = [
        (1, 2, 0, "#2980b9", "$1:2$"),
        (2, 3, np.pi/2, "#e74c3c", "$2:3$"),
        (3, 4, 0, "#27ae60", "$3:4$"),
    ]
    for a, b, delta, color, label in configs:
        ax.plot(np.sin(a*t_lis + delta), np.sin(b*t_lis),
                color=color, lw=1.8, label=f"频率比 {label}", alpha=0.85)
    ax.set_aspect("equal")
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch05-parametric-examples.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


def plot_polar_curves():
    """经典极坐标曲线：心形线、玫瑰线、螺旋线、双纽线。"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 12),
                              subplot_kw={"projection": "polar"})
    fig.suptitle("经典极坐标曲线", fontsize=15, fontweight="bold", y=1.02)

    # Cardioid
    ax = axes[0, 0]
    ax.set_title("心形线 $r = 1 + \\cos\\theta$", fontsize=12, pad=15)
    theta = np.linspace(0, 2*np.pi, 1000)
    r = 1 + np.cos(theta)
    ax.plot(theta, r, color="#e74c3c", lw=2.5)
    ax.set_rmax(2.5)

    # Rose curves
    ax = axes[0, 1]
    ax.set_title("玫瑰线", fontsize=12, pad=15)
    theta = np.linspace(0, 2*np.pi, 2000)
    r2 = np.abs(np.cos(2*theta))
    r3 = np.abs(np.cos(3*theta))
    ax.plot(theta, np.maximum(np.cos(2*theta), 0), color="#2980b9", lw=2,
            label="$r = \\cos 2\\theta$ (4瓣)")
    theta_neg = theta[np.cos(2*theta) < 0]
    r_neg = -np.cos(2*theta_neg)
    ax.plot(theta_neg + np.pi, r_neg, color="#2980b9", lw=2, alpha=0.6)
    ax.plot(theta, np.maximum(np.cos(3*theta), 0), color="#e74c3c", lw=2,
            label="$r = \\cos 3\\theta$ (3瓣)")
    ax.set_rmax(1.3)
    ax.legend(fontsize=8, loc="lower left", bbox_to_anchor=(-0.1, -0.15))

    # Archimedean spiral
    ax = axes[1, 0]
    ax.set_title("螺旋线", fontsize=12, pad=15)
    theta_sp = np.linspace(0, 6*np.pi, 2000)
    ax.plot(theta_sp, 0.2*theta_sp, color="#8e44ad", lw=2,
            label="阿基米德 $r = 0.2\\theta$")
    theta_log = np.linspace(0, 4*np.pi, 2000)
    ax.plot(theta_log, 0.3*np.exp(0.1*theta_log), color="#e67e22", lw=2,
            label="对数 $r = 0.3e^{0.1\\theta}$")
    ax.set_rmax(5)
    ax.legend(fontsize=8, loc="lower left", bbox_to_anchor=(-0.1, -0.15))

    # Lemniscate
    ax = axes[1, 1]
    ax.set_title("双纽线 $r^2 = 4\\cos 2\\theta$", fontsize=12, pad=15)
    theta_lem = np.linspace(-np.pi/4, np.pi/4, 500)
    r_lem = 2*np.sqrt(np.cos(2*theta_lem))
    ax.plot(theta_lem, r_lem, color="#1abc9c", lw=2.5)
    ax.plot(theta_lem + np.pi, r_lem, color="#1abc9c", lw=2.5)
    ax.set_rmax(3)

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch05-polar-curves.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    plot_parametric_examples()
    plot_polar_curves()
    print("All ch05 plots generated.")
