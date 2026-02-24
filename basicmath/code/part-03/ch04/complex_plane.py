"""
复数平面可视化

生成 Part 3 Chapter 4 所需的三张图：
  1. 复平面上的运算可视化（加法向量、乘以 i 的旋转）
  2. 单位根（3, 4, 5, 6 次）
  3. De Moivre 旋转（(1+i)^k 的轨迹）
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


def plot_complex_operations():
    """复平面上的基本运算：加法（平行四边形法则）和乘以 i（旋转 90°）。"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("复平面上的运算", fontsize=15, fontweight="bold")

    ax = axes[0]
    ax.set_title("加法：平行四边形法则", fontsize=12, pad=10)
    z1 = 3 + 1j
    z2 = 1 + 2j
    zs = z1 + z2

    ax.annotate("", xy=(z1.real, z1.imag), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="#2980b9", lw=2))
    ax.annotate("", xy=(z2.real, z2.imag), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="#e74c3c", lw=2))
    ax.annotate("", xy=(zs.real, zs.imag), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color="#27ae60", lw=2.5))

    ax.plot([z1.real, zs.real], [z1.imag, zs.imag], "--", color="#aaa", lw=1)
    ax.plot([z2.real, zs.real], [z2.imag, zs.imag], "--", color="#aaa", lw=1)

    offset = 0.2
    ax.text(z1.real + offset, z1.imag, f"$z_1 = {z1.real:.0f}+{z1.imag:.0f}i$",
            fontsize=10, color="#2980b9", fontweight="bold")
    ax.text(z2.real - 0.3, z2.imag + offset, f"$z_2 = {z2.real:.0f}+{z2.imag:.0f}i$",
            fontsize=10, color="#e74c3c", fontweight="bold")
    ax.text(zs.real + offset, zs.imag, f"$z_1+z_2 = {zs.real:.0f}+{zs.imag:.0f}i$",
            fontsize=10, color="#27ae60", fontweight="bold")

    ax.axhline(0, color="#7f8c8d", lw=0.8)
    ax.axvline(0, color="#7f8c8d", lw=0.8)
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-0.5, 4.5)
    ax.set_xlabel("实轴 (Re)", fontsize=11)
    ax.set_ylabel("虚轴 (Im)", fontsize=11)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)

    ax2 = axes[1]
    ax2.set_title("乘以 $i$：逆时针旋转 $90°$", fontsize=12, pad=10)

    z = 3 - 1j
    zi = z * 1j
    zi2 = zi * 1j
    zi3 = zi2 * 1j

    points = [z, zi, zi2, zi3]
    labels = ["$z$", "$iz$", "$i^2 z$", "$i^3 z$"]
    colors = ["#2980b9", "#e74c3c", "#27ae60", "#8e44ad"]

    for pt, lbl, clr in zip(points, labels, colors):
        ax2.annotate("", xy=(pt.real, pt.imag), xytext=(0, 0),
                     arrowprops=dict(arrowstyle="-|>", color=clr, lw=2))
        ax2.plot(pt.real, pt.imag, "o", color=clr, markersize=8, zorder=5)
        ax2.text(pt.real + 0.2 * np.sign(pt.real + 0.01),
                 pt.imag + 0.2 * np.sign(pt.imag + 0.01),
                 lbl, fontsize=11, color=clr, fontweight="bold")

    for i_step in range(4):
        angle1 = np.angle(points[i_step])
        angle2 = np.angle(points[(i_step + 1) % 4])
        if angle2 < angle1:
            angle2 += 2 * np.pi
        arc_angles = np.linspace(angle1, angle2, 30)
        r_arc = 0.7 + i_step * 0.15
        ax2.plot(r_arc * np.cos(arc_angles), r_arc * np.sin(arc_angles),
                 "--", color="#aaa", lw=0.8)

    ax2.axhline(0, color="#7f8c8d", lw=0.8)
    ax2.axvline(0, color="#7f8c8d", lw=0.8)
    lim = 4
    ax2.set_xlim(-lim, lim)
    ax2.set_ylim(-lim, lim)
    ax2.set_xlabel("实轴 (Re)", fontsize=11)
    ax2.set_ylabel("虚轴 (Im)", fontsize=11)
    ax2.set_aspect("equal")
    ax2.grid(True, alpha=0.3)

    fig.tight_layout(rect=[0, 0, 1, 0.93])
    out = os.path.join(ABS_OUT, "p03-ch04-complex-operations.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ {out}")


def plot_roots_of_unity():
    """3, 4, 5, 6 次单位根。"""
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    fig.suptitle("$n$ 次单位根：$z^n = 1$ 的解", fontsize=15, fontweight="bold")

    ns = [3, 4, 5, 6]
    colors = ["#e74c3c", "#2980b9", "#27ae60", "#8e44ad"]

    for ax, n, clr in zip(axes.flat, ns, colors):
        ax.set_title(f"$n = {n}$", fontsize=13, pad=8)

        theta_circle = np.linspace(0, 2 * np.pi, 200)
        ax.plot(np.cos(theta_circle), np.sin(theta_circle), color="#bdc3c7", lw=1.5)

        roots = [np.exp(2j * np.pi * k / n) for k in range(n)]
        xs = [z.real for z in roots]
        ys = [z.imag for z in roots]
        xs_closed = xs + [xs[0]]
        ys_closed = ys + [ys[0]]
        ax.fill(xs_closed, ys_closed, color=clr, alpha=0.1)
        ax.plot(xs_closed, ys_closed, "-", color=clr, lw=1.5, alpha=0.6)

        for k, z in enumerate(roots):
            ax.plot(z.real, z.imag, "o", color=clr, markersize=9, zorder=5)
            offset_r = 0.22
            angle_k = 2 * np.pi * k / n
            lx = z.real + offset_r * np.cos(angle_k)
            ly = z.imag + offset_r * np.sin(angle_k)
            label = f"$\\omega^{{{k}}}$" if k > 0 else "$1$"
            ax.text(lx, ly, label, fontsize=10, ha="center", va="center",
                    color=clr, fontweight="bold")

        ax.axhline(0, color="#7f8c8d", lw=0.6)
        ax.axvline(0, color="#7f8c8d", lw=0.6)
        ax.set_xlim(-1.6, 1.6)
        ax.set_ylim(-1.6, 1.6)
        ax.set_aspect("equal")
        ax.set_xlabel("Re", fontsize=10)
        ax.set_ylabel("Im", fontsize=10)
        ax.grid(True, alpha=0.2)

    fig.tight_layout(rect=[0, 0, 1, 0.94])
    out = os.path.join(ABS_OUT, "p03-ch04-roots-of-unity.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ {out}")


def plot_demoivre_rotation():
    """De Moivre 定理可视化：(1+i)^k 的轨迹，展示旋转与缩放。"""
    fig, ax = plt.subplots(figsize=(9, 9))
    ax.set_title("De Moivre 定理：$(1+i)^k$ 的轨迹", fontsize=14, fontweight="bold", pad=12)

    z_base = 1 + 1j
    r_base = abs(z_base)
    theta_base = np.angle(z_base)

    powers = range(0, 9)
    zs = [z_base ** k for k in powers]

    cmap = plt.cm.viridis
    norm = plt.Normalize(0, 8)

    for k, z in zip(powers, zs):
        color = cmap(norm(k))
        ax.annotate("", xy=(z.real, z.imag), xytext=(0, 0),
                     arrowprops=dict(arrowstyle="-|>", color=color, lw=1.5, alpha=0.7))
        ax.plot(z.real, z.imag, "o", color=color, markersize=8, zorder=5)

        sign_x = 1 if z.real >= 0 else -1
        sign_y = 1 if z.imag >= 0 else -1
        ax.text(z.real + sign_x * 0.5, z.imag + sign_y * 0.5,
                f"$k={k}$", fontsize=9, color=color, fontweight="bold",
                ha="center", va="center")

    for k in range(9):
        r_k = r_base ** k
        circle_theta = np.linspace(0, 2 * np.pi, 200)
        ax.plot(r_k * np.cos(circle_theta), r_k * np.sin(circle_theta),
                "--", color="#ddd", lw=0.5, zorder=1)

    trail_t = np.linspace(0, 8, 500)
    trail_z = r_base ** trail_t * np.exp(1j * theta_base * trail_t)
    ax.plot(trail_z.real, trail_z.imag, "-", color="#e74c3c", lw=1, alpha=0.4, zorder=2)

    ax.axhline(0, color="#7f8c8d", lw=0.8)
    ax.axvline(0, color="#7f8c8d", lw=0.8)

    info_text = (
        "$z = 1 + i = \\sqrt{2}\\,\\mathrm{cis}\\,(\\pi/4)$\n"
        "$z^k = (\\sqrt{2})^k\\,\\mathrm{cis}\\,(k\\pi/4)$\n"
        "模：每步乘以 $\\sqrt{2}$\n"
        "辐角：每步加 $45°$"
    )
    ax.text(0.02, 0.98, info_text, transform=ax.transAxes, fontsize=10,
            verticalalignment="top",
            bbox=dict(boxstyle="round,pad=0.5", fc="#eaf2f8", ec="#2980b9", alpha=0.95))

    lim = 18
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_xlabel("实轴 (Re)", fontsize=12)
    ax.set_ylabel("虚轴 (Im)", fontsize=12)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)

    fig.tight_layout()
    out = os.path.join(ABS_OUT, "p03-ch04-demoivre-rotation.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ {out}")


if __name__ == "__main__":
    print("Part 3 Ch04: 复平面可视化")
    plot_complex_operations()
    plot_roots_of_unity()
    plot_demoivre_rotation()
    print("  完成！")
