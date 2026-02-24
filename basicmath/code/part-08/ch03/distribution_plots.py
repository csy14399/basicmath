"""
常见离散分布可视化

生成 Part 8 Chapter 3 所需的两张图：
  1. 二项分布 PMF (p08-ch03-binomial-distribution.png)
  2. Poisson 分布 PMF (p08-ch03-poisson-distribution.png)
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from math import comb, factorial, exp

_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

ABS_OUT = "/workspace/basicmath/images/code-generated"
os.makedirs(ABS_OUT, exist_ok=True)
DPI = 200


def binom_pmf(k, n, p):
    return comb(n, k) * p**k * (1-p)**(n-k)


def poisson_pmf(k, lam):
    return lam**k * exp(-lam) / factorial(k)


def plot_binomial():
    """二项分布 B(n,p) 的 PMF — 不同参数对比"""
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    configs = [
        (20, 0.3, "#3498db", "B(20, 0.3)"),
        (20, 0.5, "#e74c3c", "B(20, 0.5)"),
        (20, 0.7, "#27ae60", "B(20, 0.7)"),
    ]

    for ax, (n, p, color, label) in zip(axes, configs):
        ks = np.arange(0, n + 1)
        probs = [binom_pmf(k, n, p) for k in ks]
        bars = ax.bar(ks, probs, color=color, alpha=0.7, edgecolor=color, lw=0.8)
        ax.set_title(label, fontsize=14, fontweight="bold")
        ax.set_xlabel("k", fontsize=12)
        ax.set_ylabel("P(X = k)", fontsize=12)
        ax.set_ylim(0, max(probs) * 1.25)

        mu = n * p
        ax.axvline(mu, color="black", ls="--", lw=1.5, alpha=0.6)
        ax.text(mu + 0.5, max(probs) * 1.1, f"E[X] = {mu:.0f}",
                fontsize=10, va="center")
        ax.set_xticks(range(0, n+1, 2))

    fig.suptitle("二项分布 B(n, p) 的概率质量函数", fontsize=16, fontweight="bold",
                 y=1.02)
    plt.tight_layout()
    path = os.path.join(ABS_OUT, "p08-ch03-binomial-distribution.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {path}")


def plot_poisson():
    """Poisson 分布的 PMF — 不同 λ 值"""
    fig, ax = plt.subplots(figsize=(12, 6))

    lambdas = [1, 3, 5, 10]
    colors = ["#3498db", "#e74c3c", "#27ae60", "#9b59b6"]
    max_k = 22
    ks = np.arange(0, max_k + 1)
    width = 0.18

    for i, (lam, color) in enumerate(zip(lambdas, colors)):
        probs = [poisson_pmf(k, lam) for k in ks]
        offset = (i - 1.5) * width
        ax.bar(ks + offset, probs, width=width, color=color, alpha=0.7,
               edgecolor=color, lw=0.5, label=f"Poi({lam})")

    ax.set_xlabel("k", fontsize=13)
    ax.set_ylabel("P(X = k)", fontsize=13)
    ax.set_title("Poisson 分布 Poi(λ)：不同 λ 的比较\n（E[X] = Var(X) = λ）",
                 fontsize=15, fontweight="bold")
    ax.legend(fontsize=12, loc="upper right")
    ax.set_xlim(-0.8, max_k + 0.5)
    ax.set_xticks(range(0, max_k + 1, 2))

    plt.tight_layout()
    path = os.path.join(ABS_OUT, "p08-ch03-poisson-distribution.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {path}")


if __name__ == "__main__":
    plot_binomial()
    plot_poisson()
    print("All Ch03 figures generated.")
