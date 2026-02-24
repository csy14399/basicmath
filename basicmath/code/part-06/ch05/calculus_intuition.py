"""
微积分直觉可视化

生成 Part 6 Chapter 5 所需的四张图：
  1. 割线趋近切线 (p06-ch05-secant-to-tangent.png)
  2. 函数与导数对比 (p06-ch05-function-derivative-comparison.png)
  3. Riemann 和 (p06-ch05-riemann-sums.png)
  4. Euler 公式 (p06-ch05-euler-formula.png)
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


def plot_secant_to_tangent():
    """割线趋近切线"""
    fig, ax = plt.subplots(figsize=(10, 7))

    x = np.linspace(-0.5, 3.5, 300)
    f = lambda t: 0.5 * t ** 2 + 0.3
    a = 1.0
    fa = f(a)
    fprime = a

    ax.plot(x, f(x), color="#2c3e50", lw=2.5, label="$f(x) = 0.5x^2 + 0.3$")
    ax.plot(a, fa, "o", color="#2c3e50", ms=8, zorder=5)

    tangent_x = np.linspace(-0.5, 3.5, 100)
    tangent_y = fa + fprime * (tangent_x - a)
    ax.plot(tangent_x, tangent_y, color="#e74c3c", lw=2.5, ls="-",
            label="切线", zorder=4)

    h_values = [2.0, 1.5, 1.0, 0.5]
    alphas = [0.3, 0.4, 0.5, 0.7]
    for h, alpha in zip(h_values, alphas):
        xq = a + h
        fq = f(xq)
        slope = (fq - fa) / h
        sec_y = fa + slope * (tangent_x - a)
        ax.plot(tangent_x, sec_y, color="#3498db", lw=1.2, ls="--",
                alpha=alpha)
        ax.plot(xq, fq, "s", color="#3498db", ms=6, alpha=alpha)
        ax.annotate(f"$h={h}$", xy=(xq + 0.05, fq + 0.1), fontsize=9,
                    color="#3498db", alpha=alpha + 0.2)

    ax.annotate("$P = (a, f(a))$", xy=(a - 0.1, fa - 0.3), fontsize=11,
                color="#2c3e50")
    ax.annotate("$Q \\to P$", xy=(2.5, 3.5), fontsize=13, color="#3498db",
                arrowprops=dict(arrowstyle="->", color="#3498db"),
                xytext=(2.8, 4.2))

    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$f(x)$", fontsize=12)
    ax.set_title("割线（蓝色虚线）趋近切线（红色实线）",
                 fontsize=13, fontweight="bold")
    ax.legend(fontsize=11, loc="upper left")
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-0.5, 6.5)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch05-secant-to-tangent.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch05-secant-to-tangent.png")


def plot_function_derivative_comparison():
    """函数及其导数对比"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    x = np.linspace(-2, 2, 300)

    # (a) x^3
    ax = axes[0, 0]
    ax.plot(x, x ** 3, color="#3498db", lw=2.5, label="$f(x) = x^3$")
    ax.plot(x, 3 * x ** 2, color="#e74c3c", lw=2, ls="--",
            label="$f'(x) = 3x^2$")
    ax.set_title("$x^3$ 和 $3x^2$", fontsize=12, fontweight="bold")
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    # (b) sin x
    ax = axes[0, 1]
    x2 = np.linspace(-2 * np.pi, 2 * np.pi, 300)
    ax.plot(x2, np.sin(x2), color="#3498db", lw=2.5, label="$\\sin x$")
    ax.plot(x2, np.cos(x2), color="#e74c3c", lw=2, ls="--",
            label="$\\cos x$")
    ax.set_title("$\\sin x$ 和 $(\\sin x)' = \\cos x$", fontsize=12,
                 fontweight="bold")
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    # (c) e^x
    ax = axes[1, 0]
    x3 = np.linspace(-2, 2, 300)
    ax.plot(x3, np.exp(x3), color="#3498db", lw=2.5, label="$e^x$")
    ax.plot(x3, np.exp(x3), color="#e74c3c", lw=2, ls="--",
            label="$(e^x)' = e^x$")
    ax.annotate("$f = f'$ — 唯一！", xy=(1.3, 3), fontsize=12, color="#27ae60")
    ax.set_title("$e^x$：自身的导数", fontsize=12, fontweight="bold")
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    # (d) |x| — not differentiable
    ax = axes[1, 1]
    ax.plot(x, np.abs(x), color="#3498db", lw=2.5, label="$|x|$（连续）")
    x_neg = x[x < 0]
    x_pos = x[x > 0]
    ax.plot(x_neg, -np.ones_like(x_neg), color="#e74c3c", lw=2, ls="--")
    ax.plot(x_pos, np.ones_like(x_pos), color="#e74c3c", lw=2, ls="--",
            label="\"导数\"（$x=0$ 处不存在）")
    ax.plot(0, 0, "o", color="#e74c3c", ms=10, markerfacecolor="white",
            markeredgewidth=2, zorder=5)
    ax.annotate("不可导！", xy=(0.1, -0.5), fontsize=12, color="#e74c3c")
    ax.set_title("$|x|$：连续但在 $x=0$ 不可导", fontsize=12, fontweight="bold")
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    for ax in axes.flat:
        ax.set_xlabel("$x$", fontsize=11)
        ax.set_ylabel("$y$", fontsize=11)

    plt.suptitle("函数与导数的关系", fontsize=14, fontweight="bold", y=1.01)
    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch05-function-derivative-comparison.png"),
                dpi=DPI, bbox_inches="tight")
    plt.close()
    print("  ✓ p06-ch05-function-derivative-comparison.png")


def plot_riemann_sums():
    """Riemann 和示意图"""
    f = lambda x: 0.5 * np.sin(2 * x) + 1.5

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    titles = ["左 Riemann 和 ($n=6$)", "右 Riemann 和 ($n=6$)",
              "Riemann 和 ($n=20$)"]
    ns = [6, 6, 20]
    modes = ["left", "right", "mid"]

    a, b = 0, np.pi

    for ax, title, n, mode in zip(axes, titles, ns, modes):
        x_fine = np.linspace(a, b, 300)
        ax.plot(x_fine, f(x_fine), color="#2c3e50", lw=2.5, zorder=10)
        ax.fill_between(x_fine, 0, f(x_fine), alpha=0.05, color="#3498db")

        dx = (b - a) / n
        for i in range(n):
            xi = a + i * dx
            if mode == "left":
                h = f(xi)
            elif mode == "right":
                h = f(xi + dx)
            else:
                h = f(xi + dx / 2)
            rect = plt.Rectangle((xi, 0), dx, h, edgecolor="#3498db",
                                  facecolor="#3498db", alpha=0.3, lw=1)
            ax.add_patch(rect)

        S = sum(f(a + i * dx + (0 if mode == "left" else
                                 dx if mode == "right" else dx / 2)) * dx
                for i in range(n))
        exact = 1.5 * np.pi
        ax.set_title(f"{title}\n近似 = {S:.4f}，精确 = {exact:.4f}",
                     fontsize=11, fontweight="bold")
        ax.set_xlabel("$x$", fontsize=11)
        ax.set_ylabel("$f(x)$", fontsize=11)
        ax.set_xlim(a - 0.1, b + 0.1)
        ax.set_ylim(0, 2.3)
        ax.grid(True, alpha=0.3)

    plt.suptitle("$\\int_0^{\\pi} (0.5\\sin 2x + 1.5)\\,dx$ 的 Riemann 和",
                 fontsize=13, fontweight="bold", y=1.03)
    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch05-riemann-sums.png"),
                dpi=DPI, bbox_inches="tight")
    plt.close()
    print("  ✓ p06-ch05-riemann-sums.png")


def plot_euler_formula():
    """Euler 公式可视化"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 左：单位圆与 e^{iθ}
    ax = axes[0]
    theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(theta), np.sin(theta), color="#3498db", lw=2)

    special = {
        0: ("$1$", (1.15, 0.05)),
        np.pi / 6: ("$e^{i\\pi/6}$", (1.0, 0.6)),
        np.pi / 4: ("$e^{i\\pi/4}$", (0.85, 0.85)),
        np.pi / 3: ("$e^{i\\pi/3}$", (0.55, 1.05)),
        np.pi / 2: ("$i$", (0.1, 1.1)),
        np.pi: ("$-1$", (-1.3, 0.1)),
        3 * np.pi / 2: ("$-i$", (0.1, -1.15)),
    }

    for ang, (label, pos) in special.items():
        x, y = np.cos(ang), np.sin(ang)
        ax.plot(x, y, "o", color="#e74c3c", ms=7, zorder=5)
        ax.annotate(label, xy=pos, fontsize=11, color="#e74c3c")

    t_demo = np.pi / 4
    ax.plot([0, np.cos(t_demo)], [0, np.sin(t_demo)], color="#27ae60", lw=2)
    ax.annotate("$\\theta$", xy=(0.2, 0.08), fontsize=12, color="#27ae60")

    ax.plot([np.cos(t_demo), np.cos(t_demo)], [0, np.sin(t_demo)],
            color="#9b59b6", lw=1.5, ls="--")
    ax.plot([0, np.cos(t_demo)], [0, 0], color="#e67e22", lw=1.5, ls="--")
    ax.annotate("$\\cos\\theta$", xy=(0.25, -0.12), fontsize=10, color="#e67e22")
    ax.annotate("$\\sin\\theta$", xy=(np.cos(t_demo) + 0.05, 0.35),
                fontsize=10, color="#9b59b6")

    ax.axhline(y=0, color="k", lw=0.5)
    ax.axvline(x=0, color="k", lw=0.5)
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect("equal")
    ax.set_xlabel("实部 (Re)", fontsize=12)
    ax.set_ylabel("虚部 (Im)", fontsize=12)
    ax.set_title("$e^{i\\theta} = \\cos\\theta + i\\sin\\theta$",
                 fontsize=14, fontweight="bold")
    ax.grid(True, alpha=0.3)

    # 右：Euler 恒等式 + 旋转
    ax = axes[1]
    ax.plot(np.cos(theta), np.sin(theta), color="#3498db", lw=1.5, alpha=0.5)

    n_points = 12
    angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    colors_cycle = plt.cm.hsv(np.linspace(0, 1, n_points))
    for i, ang in enumerate(angles):
        x, y = np.cos(ang), np.sin(ang)
        ax.plot([0, x], [0, y], color=colors_cycle[i], lw=1.5, alpha=0.6)
        ax.plot(x, y, "o", color=colors_cycle[i], ms=6, zorder=5)

    ax.annotate("$e^{i\\pi} + 1 = 0$",
                xy=(0, 0), fontsize=18, fontweight="bold",
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                          edgecolor="#2c3e50", alpha=0.9))

    ax.annotate("乘以 $e^{i\\alpha}$\n= 旋转角度 $\\alpha$",
                xy=(0.8, -0.8), fontsize=11, color="#27ae60",
                ha="center",
                bbox=dict(boxstyle="round", facecolor="#eafaf1",
                          edgecolor="#27ae60", alpha=0.8))

    ax.axhline(y=0, color="k", lw=0.5)
    ax.axvline(x=0, color="k", lw=0.5)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect("equal")
    ax.set_xlabel("实部 (Re)", fontsize=12)
    ax.set_ylabel("虚部 (Im)", fontsize=12)
    ax.set_title("Euler 恒等式与复数旋转", fontsize=14, fontweight="bold")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch05-euler-formula.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch05-euler-formula.png")


if __name__ == "__main__":
    print("Part 6 Ch05: 微积分直觉可视化")
    plot_secant_to_tangent()
    plot_function_derivative_comparison()
    plot_riemann_sums()
    plot_euler_formula()
    print("完成！")
