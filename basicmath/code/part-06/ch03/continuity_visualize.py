"""
连续性可视化

生成 Part 6 Chapter 3 所需的三张图：
  1. 四种间断点 (p06-ch03-discontinuity-types.png)
  2. 介值定理 (p06-ch03-intermediate-value.png)
  3. 最值定理 (p06-ch03-extreme-value.png)
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


def plot_discontinuity_types():
    """四种间断点的图示"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    titles = ["(a) 可去间断点", "(b) 跳跃间断点",
              "(c) 无穷间断点", "(d) 振荡间断点"]

    # (a) Removable
    ax = axes[0, 0]
    x1 = np.linspace(-2, 0.98, 200)
    x2 = np.linspace(1.02, 3, 200)
    ax.plot(x1, x1 + 1, color="#3498db", lw=2.5)
    ax.plot(x2, x2 + 1, color="#3498db", lw=2.5)
    ax.plot(1, 2, "o", color="#3498db", ms=9, markerfacecolor="white",
            markeredgewidth=2, zorder=5)
    ax.plot(1, 3, "o", color="#e74c3c", ms=9, zorder=5)
    ax.annotate("$f(a) \\neq \\lim f$", xy=(1.2, 2.8), fontsize=11,
                color="#e74c3c")
    ax.set_title(titles[0], fontsize=12, fontweight="bold")
    ax.grid(True, alpha=0.3)

    # (b) Jump
    ax = axes[0, 1]
    x_left = np.linspace(-2, 1, 200)
    x_right = np.linspace(1, 3, 200)
    ax.plot(x_left, 0.5 * x_left + 1, color="#3498db", lw=2.5)
    ax.plot(x_right, 0.5 * x_right + 2.5, color="#3498db", lw=2.5)
    ax.plot(1, 1.5, "o", color="#3498db", ms=9, zorder=5)
    ax.plot(1, 3.0, "o", color="#3498db", ms=9, markerfacecolor="white",
            markeredgewidth=2, zorder=5)
    ax.annotate("跳跃", xy=(1.2, 2.2), fontsize=12, color="#e74c3c",
                arrowprops=dict(arrowstyle="<->", color="#e74c3c"),
                xytext=(1.8, 2.2))
    ax.set_title(titles[1], fontsize=12, fontweight="bold")
    ax.grid(True, alpha=0.3)

    # (c) Infinite
    ax = axes[1, 0]
    x_left = np.linspace(-2, -0.05, 200)
    x_right = np.linspace(0.05, 2, 200)
    ax.plot(x_left, 1 / x_left, color="#3498db", lw=2.5)
    ax.plot(x_right, 1 / x_right, color="#3498db", lw=2.5)
    ax.axvline(x=0, color="#e74c3c", lw=1.5, ls="--", alpha=0.5)
    ax.annotate("$\\to \\pm\\infty$", xy=(0.15, 5), fontsize=12, color="#e74c3c")
    ax.set_ylim(-8, 8)
    ax.set_title(titles[2], fontsize=12, fontweight="bold")
    ax.grid(True, alpha=0.3)

    # (d) Oscillatory
    ax = axes[1, 1]
    x_neg = np.linspace(-2, -0.02, 1000)
    x_pos = np.linspace(0.02, 2, 1000)
    for xx in [x_neg, x_pos]:
        ax.plot(xx, np.sin(1 / xx), color="#3498db", lw=1.5)
    ax.axvline(x=0, color="#e74c3c", lw=1.5, ls="--", alpha=0.5)
    ax.annotate("无法稳定", xy=(0.15, 0.8), fontsize=11, color="#e74c3c")
    ax.set_ylim(-1.5, 1.5)
    ax.set_title(titles[3], fontsize=12, fontweight="bold")
    ax.grid(True, alpha=0.3)

    for ax in axes.flat:
        ax.set_xlabel("$x$", fontsize=11)
        ax.set_ylabel("$f(x)$", fontsize=11)

    plt.suptitle("四种间断点类型", fontsize=14, fontweight="bold", y=1.01)
    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch03-discontinuity-types.png"),
                dpi=DPI, bbox_inches="tight")
    plt.close()
    print("  ✓ p06-ch03-discontinuity-types.png")


def plot_intermediate_value():
    """介值定理示意图"""
    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.linspace(0, 5, 300)
    f = 0.3 * (x - 1) * (x - 3) * (x - 4.5) + 1

    ax.plot(x, f, color="#3498db", lw=2.5, label="$f(x)$")

    a, b = 0.5, 4.8
    fa, fb = np.interp(a, x, f), np.interp(b, x, f)
    gamma = 0.5
    c_candidates = x[np.where(np.diff(np.sign(f - gamma)))[0]]

    ax.plot(a, fa, "o", color="#2c3e50", ms=8, zorder=5)
    ax.plot(b, fb, "o", color="#2c3e50", ms=8, zorder=5)
    ax.annotate(f"$f(a) = {fa:.2f}$", xy=(a, fa), xytext=(a - 0.3, fa + 0.5),
                fontsize=11, color="#2c3e50")
    ax.annotate(f"$f(b) = {fb:.2f}$", xy=(b, fb), xytext=(b + 0.1, fb + 0.3),
                fontsize=11, color="#2c3e50")

    ax.axhline(y=gamma, color="#e74c3c", lw=1.5, ls="--",
               label=f"$\\gamma = {gamma}$")

    for ci in c_candidates:
        ax.axvline(x=ci, color="#27ae60", lw=1.5, ls=":", alpha=0.7)
        ax.plot(ci, gamma, "D", color="#27ae60", ms=8, zorder=5)

    ax.annotate("$\\exists\\,c: f(c) = \\gamma$",
                xy=(c_candidates[0] + 0.2, gamma + 0.15), fontsize=12,
                color="#27ae60")

    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$f(x)$", fontsize=12)
    ax.set_title("介值定理 (IVT)：$f$ 连续，$f(a)$ 和 $f(b)$ 之间的值都取到",
                 fontsize=13, fontweight="bold")
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch03-intermediate-value.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch03-intermediate-value.png")


def plot_extreme_value():
    """最值定理示意图"""
    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.linspace(0.5, 4.5, 300)
    f = -0.5 * (x - 2) ** 2 + 0.3 * np.sin(3 * x) + 3

    ax.plot(x, f, color="#3498db", lw=2.5, label="$f(x)$ 在 $[a, b]$ 上连续")

    i_max = np.argmax(f)
    i_min = np.argmin(f)

    ax.plot(x[i_max], f[i_max], "^", color="#e74c3c", ms=12, zorder=5,
            label=f"最大值 $M = {f[i_max]:.2f}$")
    ax.plot(x[i_min], f[i_min], "v", color="#27ae60", ms=12, zorder=5,
            label=f"最小值 $m = {f[i_min]:.2f}$")

    ax.axhline(y=f[i_max], color="#e74c3c", lw=1, ls="--", alpha=0.5)
    ax.axhline(y=f[i_min], color="#27ae60", lw=1, ls="--", alpha=0.5)

    ax.axvline(x=x[0], color="#2c3e50", lw=1.5, ls=":")
    ax.axvline(x=x[-1], color="#2c3e50", lw=1.5, ls=":")
    ax.annotate("$a$", xy=(x[0], f[0] - 0.3), fontsize=12, ha="center")
    ax.annotate("$b$", xy=(x[-1], f[-1] - 0.3), fontsize=12, ha="center")

    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$f(x)$", fontsize=12)
    ax.set_title("最值定理：$f$ 在 $[a,b]$ 连续 $\\Rightarrow$ $f$ 取到最大值和最小值",
                 fontsize=13, fontweight="bold")
    ax.legend(fontsize=11, loc="lower right")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch03-extreme-value.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch03-extreme-value.png")


if __name__ == "__main__":
    print("Part 6 Ch03: 连续性可视化")
    plot_discontinuity_types()
    plot_intermediate_value()
    plot_extreme_value()
    print("完成！")
