"""
数列收敛可视化

生成 Part 6 Chapter 1 所需的三张图：
  1. 等差数列与等比数列 (p06-ch01-arithmetic-geometric.png)
  2. ε-N 定义 (p06-ch01-epsilon-N-definition.png)
  3. 夹逼定理 (p06-ch01-squeeze-theorem.png)
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


def plot_arithmetic_geometric():
    """等差数列与等比数列对比图"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    n = np.arange(1, 16)

    # 等差数列
    ax = axes[0]
    for d, color, label in [(2, "#e74c3c", "d=2"), (1, "#3498db", "d=1"),
                             (-1, "#2ecc71", "d=−1")]:
        a = 3 + (n - 1) * d
        ax.plot(n, a, "o-", color=color, ms=5, lw=1.5, label=f"$a_1=3,\\;d={d}$")
    ax.set_xlabel("$n$", fontsize=12)
    ax.set_ylabel("$a_n$", fontsize=12)
    ax.set_title("等差数列 $a_n = a_1 + (n-1)d$", fontsize=13, fontweight="bold")
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color="k", lw=0.5)

    # 等比数列
    ax = axes[1]
    for r, color, label in [(0.8, "#e74c3c", "r=0.8"),
                             (1.1, "#3498db", "r=1.1"),
                             (-0.7, "#2ecc71", "r=−0.7")]:
        a = 4 * r ** (n - 1)
        ax.plot(n, a, "o-", color=color, ms=5, lw=1.5,
                label=f"$a_1=4,\\;r={r}$")
    ax.set_xlabel("$n$", fontsize=12)
    ax.set_ylabel("$a_n$", fontsize=12)
    ax.set_title("等比数列 $a_n = a_1 \\cdot r^{n-1}$", fontsize=13, fontweight="bold")
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color="k", lw=0.5)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch01-arithmetic-geometric.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch01-arithmetic-geometric.png")


def plot_epsilon_N():
    """ε-N 定义的可视化"""
    fig, ax = plt.subplots(figsize=(10, 6))

    n = np.arange(1, 51)
    a_n = 1 / n + 2
    L = 2.0
    eps = 0.15

    ax.plot(n, a_n, "o", color="#3498db", ms=4, label="$a_n = 1/n + 2$")
    ax.axhline(y=L, color="#2c3e50", lw=2, label="$L = 2$")
    ax.axhline(y=L + eps, color="#e74c3c", lw=1.5, ls="--", label=f"$L + \\varepsilon = {L+eps}$")
    ax.axhline(y=L - eps, color="#e74c3c", lw=1.5, ls="--", label=f"$L - \\varepsilon = {L-eps}$")

    ax.fill_between(n, L - eps, L + eps, alpha=0.1, color="#e74c3c")

    N = int(np.ceil(1 / eps))
    ax.axvline(x=N, color="#27ae60", lw=2, ls=":", label=f"$N = {N}$")

    ax.annotate(f"$N = \\lceil 1/\\varepsilon \\rceil = {N}$",
                xy=(N, L - eps - 0.02), fontsize=11, color="#27ae60",
                ha="center", va="top")

    ax.set_xlabel("$n$", fontsize=12)
    ax.set_ylabel("$a_n$", fontsize=12)
    ax.set_title("$\\varepsilon$-$N$ 定义：$n > N$ 时 $|a_n - L| < \\varepsilon$",
                 fontsize=13, fontweight="bold")
    ax.legend(loc="upper right", fontsize=10)
    ax.set_xlim(0, 52)
    ax.set_ylim(1.7, 3.2)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch01-epsilon-N-definition.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch01-epsilon-N-definition.png")


def plot_squeeze_theorem():
    """夹逼定理可视化"""
    fig, ax = plt.subplots(figsize=(10, 6))

    n = np.arange(1, 41)
    lower = -1.0 / n
    upper = 1.0 / n
    middle = np.sin(n) / n

    ax.fill_between(n, lower, upper, alpha=0.15, color="#3498db", label="夹逼区域")
    ax.plot(n, upper, "s-", color="#e74c3c", ms=3, lw=1.2, label="$c_n = 1/n$")
    ax.plot(n, lower, "s-", color="#e74c3c", ms=3, lw=1.2, label="$a_n = -1/n$")
    ax.plot(n, middle, "o", color="#2c3e50", ms=4, label="$b_n = \\sin(n)/n$")
    ax.axhline(y=0, color="#27ae60", lw=2, ls="--", label="$L = 0$")

    ax.set_xlabel("$n$", fontsize=12)
    ax.set_ylabel("值", fontsize=12)
    ax.set_title("夹逼定理：$-1/n \\leq \\sin(n)/n \\leq 1/n$，故 $\\sin(n)/n \\to 0$",
                 fontsize=13, fontweight="bold")
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(ABS_OUT, "p06-ch01-squeeze-theorem.png"), dpi=DPI)
    plt.close()
    print("  ✓ p06-ch01-squeeze-theorem.png")


if __name__ == "__main__":
    print("Part 6 Ch01: 数列收敛可视化")
    plot_arithmetic_geometric()
    plot_epsilon_N()
    plot_squeeze_theorem()
    print("完成！")
