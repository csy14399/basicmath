"""
指数与对数函数可视化

生成 Part 4 Chapter 2 所需的三张图：
  1. 指数函数族 a^x（不同底数）
  2. 对数函数族 log_a(x)（不同底数）
  3. e 的极限收敛 (1+1/n)^n → e
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


def plot_exponential_family():
    """指数函数族 a^x，不同底数。"""
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_title("指数函数族 $y = a^x$", fontsize=14, fontweight="bold", pad=10)

    x = np.linspace(-3, 3, 500)
    bases = [
        (0.5, "#e74c3c", "$a = 1/2$（递减）"),
        (1/np.e, "#c0392b", "$a = 1/e$"),
        (np.e, "#2980b9", "$a = e$"),
        (2, "#27ae60", "$a = 2$"),
        (3, "#8e44ad", "$a = 3$"),
        (10, "#e67e22", "$a = 10$"),
    ]

    for base, color, label in bases:
        y = base**x
        ax.plot(x, y, color=color, lw=2.2, label=label)

    ax.axhline(1, color="#7f8c8d", lw=1, ls=":", alpha=0.6)
    ax.annotate("所有曲线过 $(0, 1)$", xy=(0.15, 1.3), fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", fc="#fef9e7", alpha=0.9))
    ax.set_xlim(-3, 3)
    ax.set_ylim(0, 15)
    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$y$", fontsize=12)
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch02-exponential-family.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


def plot_logarithm_family():
    """对数函数族 log_a(x)，不同底数。"""
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_title("对数函数族 $y = \\log_a x$", fontsize=14, fontweight="bold", pad=10)

    x = np.linspace(0.01, 10, 500)
    bases = [
        (0.5, "#e74c3c", "$a = 1/2$（递减）"),
        (np.e, "#2980b9", "$a = e$（$\\ln x$）"),
        (2, "#27ae60", "$a = 2$（$\\log_2 x$）"),
        (10, "#8e44ad", "$a = 10$（$\\lg x$）"),
    ]

    for base, color, label in bases:
        y = np.log(x) / np.log(base)
        ax.plot(x, y, color=color, lw=2.2, label=label)

    ax.axhline(0, color="#7f8c8d", lw=0.8)
    ax.axvline(1, color="#7f8c8d", lw=1, ls=":", alpha=0.6)
    ax.annotate("所有曲线过 $(1, 0)$", xy=(1.3, -1.5), fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", fc="#fef9e7", alpha=0.9))
    ax.set_xlim(-0.5, 10)
    ax.set_ylim(-5, 5)
    ax.set_xlabel("$x$", fontsize=12)
    ax.set_ylabel("$y$", fontsize=12)
    ax.legend(fontsize=9, loc="lower right")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch02-logarithm-family.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


def plot_e_convergence():
    """(1 + 1/n)^n → e 的收敛过程。"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("$e$ 的极限定义：$(1 + 1/n)^n \\to e$", fontsize=14, fontweight="bold")

    # Left: table-like bar plot
    ns = [1, 2, 5, 10, 20, 50, 100, 1000, 10000]
    vals = [(1 + 1/n)**n for n in ns]

    ax = axes[0]
    ax.set_title("各 $n$ 对应的 $(1+1/n)^n$", fontsize=11, pad=8)
    bars = ax.barh(range(len(ns)), vals, color="#3498db", alpha=0.8, height=0.6)
    ax.axvline(np.e, color="#e74c3c", lw=2, ls="--", label=f"$e \\approx {np.e:.5f}$")
    ax.set_yticks(range(len(ns)))
    ax.set_yticklabels([f"$n = {n}$" for n in ns], fontsize=9)
    ax.set_xlim(1.5, 3.0)
    for i, v in enumerate(vals):
        ax.text(v + 0.02, i, f"{v:.5f}", va="center", fontsize=8)
    ax.legend(fontsize=10)
    ax.grid(True, axis="x", alpha=0.3)

    # Right: continuous convergence curve
    ax = axes[1]
    ax.set_title("收敛过程", fontsize=11, pad=8)
    n_cont = np.arange(1, 201)
    vals_cont = (1 + 1/n_cont)**n_cont
    ax.plot(n_cont, vals_cont, "o-", color="#2980b9", ms=2, lw=1, alpha=0.8)
    ax.axhline(np.e, color="#e74c3c", lw=2, ls="--", label=f"$e \\approx {np.e:.5f}$")
    ax.set_xlabel("$n$", fontsize=12)
    ax.set_ylabel("$(1+1/n)^n$", fontsize=12)
    ax.set_ylim(2.0, 2.9)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch02-e-convergence.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    plot_exponential_family()
    plot_logarithm_family()
    plot_e_convergence()
    print("All ch02 plots generated.")
