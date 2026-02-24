"""
级数可视化

生成 Part 6 Chapter 4 所需的四张图：
  1. 几何级数的部分和 (p06-ch04-geometric-series.png)
  2. 调和级数的增长 (p06-ch04-harmonic-series.png)
  3. Taylor 多项式逼近 (p06-ch04-taylor-approximation.png)
  4. 收敛半径示意图 (p06-ch04-convergence-radius.png)
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from math import factorial

_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

ABS_OUT = "/workspace/basicmath/images/code-generated"
os.makedirs(ABS_OUT, exist_ok=True)
DPI = 200


def plot_geometric_series():
    """几何级数部分和"""
    fig, ax = plt.subplots(figsize=(10, 6))

    n = np.arange(1, 21)

    configs = [
        (0.5, "#3498db", "$r = 1/2$, 和 $= 2$"),
        (0.7, "#27ae60", "$r = 0.7$, 和 $\\approx 3.33$"),
        (-0.5, "#9b59b6", "$r = -1/2$, 和 $= 2/3$"),
    ]

    for r, color, label in configs:
        S_n = np.cumsum(r ** np.arange(0, len(n)))
        limit = 1.0 / (1.0 - r)
        ax.plot(n, S_n, "o-", color=color, ms=4, lw=1.5, label=label)
        ax.axhline(y=limit, color=color, lw=1, ls="--", alpha=0.5)

    ax.set_xlabel("$n$（项数）", fontsize=12)
    ax.set_ylabel("部分和 $S_n$", fontsize=12)
    ax.set_title("几何级数 $\\sum_{k=0}^{n-1} r^k$ 的部分和", fontsize=13,
                 fontweight="bold")
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch04-geometric-series.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch04-geometric-series.png")


def plot_harmonic_series():
    """调和级数部分和的增长"""
    fig, ax = plt.subplots(figsize=(10, 6))

    N = 1000
    n = np.arange(1, N + 1)
    H_n = np.cumsum(1.0 / n)

    ax.plot(n, H_n, color="#e74c3c", lw=2, label="$H_n = \\sum_{k=1}^n 1/k$")
    ax.plot(n, np.log(n) + 0.5772, color="#3498db", lw=1.5, ls="--",
            label="$\\ln n + \\gamma$（近似）")

    milestones = [10, 50, 100, 500, 1000]
    for m in milestones:
        ax.plot(m, H_n[m - 1], "o", color="#2c3e50", ms=5, zorder=5)
        ax.annotate(f"$H_{{{m}}} \\approx {H_n[m-1]:.2f}$",
                    xy=(m, H_n[m - 1]), xytext=(m + 30, H_n[m - 1] - 0.3),
                    fontsize=9, color="#2c3e50")

    ax.set_xlabel("$n$", fontsize=12)
    ax.set_ylabel("$H_n$", fontsize=12)
    ax.set_title("调和级数 $\\sum 1/n$ 的部分和：缓慢增长到 $\\infty$",
                 fontsize=13, fontweight="bold")
    ax.legend(fontsize=11, loc="lower right")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch04-harmonic-series.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch04-harmonic-series.png")


def plot_taylor_approximation():
    """Taylor 多项式逐步逼近 sin(x)"""
    fig, ax = plt.subplots(figsize=(12, 7))

    x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    ax.plot(x, np.sin(x), color="#2c3e50", lw=3, label="$\\sin(x)$", zorder=10)

    colors = ["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#3498db", "#9b59b6"]
    orders = [1, 3, 5, 7, 9, 11]

    for order, color in zip(orders, colors):
        T = np.zeros_like(x)
        for k in range((order + 1) // 2):
            n = 2 * k + 1
            T += (-1) ** k * x ** n / factorial(n)
        ax.plot(x, T, color=color, lw=1.5, ls="--",
                label=f"$P_{{{order}}}(x)$", alpha=0.8)

    ax.set_ylim(-3, 3)
    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$y$", fontsize=12)
    ax.set_title("$\\sin(x)$ 的 Taylor 多项式逼近：阶数越高越精确",
                 fontsize=13, fontweight="bold")
    ax.legend(fontsize=10, loc="upper left", ncol=2)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch04-taylor-approximation.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch04-taylor-approximation.png")


def plot_convergence_radius():
    """收敛半径示意图"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # 左：ln(1+x) = sum (-1)^{n+1} x^n/n, R=1
    ax = axes[0]
    x = np.linspace(-0.99, 0.99, 300)
    x_ext = np.linspace(-1.5, 1.5, 300)
    ax.plot(x_ext, np.log(1 + np.clip(x_ext, -0.999, None)),
            color="#2c3e50", lw=2.5, label="$\\ln(1+x)$")

    for N, color, ls in [(2, "#e74c3c", "--"), (5, "#e67e22", "-."),
                          (10, "#3498db", ":"), (20, "#27ae60", "-")]:
        T = np.zeros_like(x)
        for n in range(1, N + 1):
            T += (-1) ** (n + 1) * x ** n / n
        ax.plot(x, T, color=color, lw=1.5, ls=ls, label=f"$N = {N}$", alpha=0.8)

    ax.axvline(x=-1, color="#e74c3c", lw=2, ls="--", alpha=0.5)
    ax.axvline(x=1, color="#e74c3c", lw=2, ls="--", alpha=0.5)
    ax.annotate("$R = 1$", xy=(1.05, 0.5), fontsize=12, color="#e74c3c")

    ax.fill_betweenx([-3, 3], -1, 1, alpha=0.05, color="#27ae60")
    ax.set_ylim(-3, 2)
    ax.set_xlim(-1.5, 1.5)
    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$y$", fontsize=12)
    ax.set_title("$\\ln(1+x)$：$R = 1$", fontsize=13, fontweight="bold")
    ax.legend(fontsize=9, loc="lower right")
    ax.grid(True, alpha=0.3)

    # 右：概念图
    ax = axes[1]
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1.5, 1.5)

    theta = np.linspace(0, 2 * np.pi, 100)
    R = 1.5
    ax.plot(R * np.cos(theta), R * np.sin(theta), color="#3498db", lw=2.5)
    ax.fill(R * np.cos(theta), R * np.sin(theta), alpha=0.1, color="#3498db")

    ax.plot(0, 0, "o", color="#2c3e50", ms=8, zorder=5)
    ax.annotate("中心 $c$", xy=(0.1, 0.1), fontsize=12, color="#2c3e50")

    ax.annotate("", xy=(R, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="<->", color="#e74c3c", lw=2))
    ax.annotate("$R$", xy=(R / 2, 0.15), fontsize=14, color="#e74c3c",
                fontweight="bold")

    ax.text(0, -0.5, "绝对收敛", fontsize=12, ha="center", color="#3498db")
    ax.text(2.3, 0.8, "发散", fontsize=12, color="#e74c3c")
    ax.text(R * np.cos(np.pi / 4) + 0.1, R * np.sin(np.pi / 4) + 0.1,
            "端点需\n单独判断", fontsize=10, color="#e67e22", ha="center")

    ax.set_xlabel("(数轴或复平面)", fontsize=11)
    ax.set_title("收敛半径 $R$ 的概念", fontsize=13, fontweight="bold")
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch04-convergence-radius.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch04-convergence-radius.png")


if __name__ == "__main__":
    print("Part 6 Ch04: 级数可视化")
    plot_geometric_series()
    plot_harmonic_series()
    plot_taylor_approximation()
    plot_convergence_radius()
    print("完成！")
