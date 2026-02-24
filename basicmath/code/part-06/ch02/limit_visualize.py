"""
极限可视化

生成 Part 6 Chapter 2 所需的两张图：
  1. ε-δ 定义 (p06-ch02-epsilon-delta.png)
  2. sin(x)/x 极限 (p06-ch02-sinx-over-x.png)
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


def plot_epsilon_delta():
    """ε-δ 定义的可视化：f(x) = x² 在 x=1 处"""
    fig, ax = plt.subplots(figsize=(10, 7))

    x = np.linspace(-0.5, 2.5, 500)
    f = x ** 2
    a, L = 1.0, 1.0
    eps = 0.4
    delta = 0.18

    ax.plot(x, f, color="#3498db", lw=2.5, label="$f(x) = x^2$")
    ax.plot(a, L, "o", color="#2c3e50", ms=8, zorder=5)

    ax.axhline(y=L + eps, color="#e74c3c", lw=1.5, ls="--", alpha=0.7)
    ax.axhline(y=L - eps, color="#e74c3c", lw=1.5, ls="--", alpha=0.7)
    ax.axvline(x=a + delta, color="#27ae60", lw=1.5, ls="--", alpha=0.7)
    ax.axvline(x=a - delta, color="#27ae60", lw=1.5, ls="--", alpha=0.7)

    ax.fill_between(x, L - eps, L + eps,
                    where=(x >= a - delta) & (x <= a + delta),
                    alpha=0.15, color="#e74c3c")
    ax.fill_betweenx([L - eps, L + eps], a - delta, a + delta,
                     alpha=0.15, color="#27ae60")

    ax.annotate("$L + \\varepsilon$", xy=(2.3, L + eps), fontsize=11, color="#e74c3c")
    ax.annotate("$L - \\varepsilon$", xy=(2.3, L - eps), fontsize=11, color="#e74c3c")
    ax.annotate("$a - \\delta$", xy=(a - delta, -0.15), fontsize=11,
                color="#27ae60", ha="center")
    ax.annotate("$a + \\delta$", xy=(a + delta, -0.15), fontsize=11,
                color="#27ae60", ha="center")
    ax.annotate("$(a, L) = (1, 1)$", xy=(a + 0.1, L + 0.08), fontsize=11,
                color="#2c3e50")

    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$f(x)$", fontsize=12)
    ax.set_title("$\\varepsilon$-$\\delta$ 定义：$|x - a| < \\delta \\Rightarrow |f(x) - L| < \\varepsilon$",
                 fontsize=13, fontweight="bold")
    ax.set_xlim(-0.3, 2.5)
    ax.set_ylim(-0.3, 4.0)
    ax.legend(fontsize=11, loc="upper left")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch02-epsilon-delta.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch02-epsilon-delta.png")


def plot_sinx_over_x():
    """sin(x)/x → 1 的可视化"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # 左：函数图像
    ax = axes[0]
    x = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
    x_safe = np.where(np.abs(x) < 1e-10, 1e-10, x)
    y = np.sin(x_safe) / x_safe
    y[np.abs(x) < 1e-10] = 1.0

    ax.plot(x, y, color="#3498db", lw=2, label="$f(x) = \\sin(x)/x$")
    ax.axhline(y=1, color="#e74c3c", lw=1.5, ls="--", label="$y = 1$")
    ax.plot(0, 1, "o", color="#e74c3c", ms=8, zorder=5, markerfacecolor="white",
            markeredgewidth=2)
    ax.annotate("$\\lim_{x \\to 0} \\frac{\\sin x}{x} = 1$",
                xy=(0.5, 1.05), fontsize=13, color="#e74c3c")

    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$f(x)$", fontsize=12)
    ax.set_title("$\\sin(x)/x$ 的图像", fontsize=13, fontweight="bold")
    ax.legend(fontsize=10)
    ax.set_ylim(-0.4, 1.3)
    ax.grid(True, alpha=0.3)

    # 右：放大 x=0 附近
    ax = axes[1]
    x_zoom = np.linspace(-1.5, 1.5, 500)
    x_safe = np.where(np.abs(x_zoom) < 1e-10, 1e-10, x_zoom)
    y_zoom = np.sin(x_safe) / x_safe
    y_zoom[np.abs(x_zoom) < 1e-10] = 1.0

    ax.plot(x_zoom, y_zoom, color="#3498db", lw=2.5, label="$\\sin(x)/x$")
    ax.plot(x_zoom, np.ones_like(x_zoom), color="#e74c3c", lw=1.5, ls="--")
    ax.plot(x_zoom, x_zoom * 0 + np.cos(0), color="#27ae60", lw=1, ls=":",
            alpha=0.5)

    ax.fill_between(x_zoom, 0.95, 1.05, alpha=0.1, color="#e74c3c")
    ax.plot(0, 1, "o", color="#e74c3c", ms=8, zorder=5, markerfacecolor="white",
            markeredgewidth=2)

    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$f(x)$", fontsize=12)
    ax.set_title("$x = 0$ 附近放大", fontsize=13, fontweight="bold")
    ax.set_ylim(0.8, 1.05)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch02-sinx-over-x.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch02-sinx-over-x.png")


if __name__ == "__main__":
    print("Part 6 Ch02: 极限可视化")
    plot_epsilon_delta()
    plot_sinx_over_x()
    print("完成！")
