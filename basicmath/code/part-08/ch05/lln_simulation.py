"""
大数定律与中心极限定理可视化

生成 Part 8 Chapter 5 所需的图：
  p08-ch05-lln-simulation.png
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


def plot_lln_simulation():
    """大数定律模拟 + CLT 直方图"""
    np.random.seed(42)
    fig = plt.figure(figsize=(16, 10))

    # Top: LLN — sample mean vs n
    ax1 = fig.add_subplot(2, 1, 1)
    N = 10000
    coin_flips = np.random.binomial(1, 0.5, N)
    cumulative_mean = np.cumsum(coin_flips) / np.arange(1, N + 1)

    ax1.plot(range(1, N + 1), cumulative_mean, color="#3498db", lw=1.2, alpha=0.8)
    ax1.axhline(0.5, color="#e74c3c", ls="--", lw=2, label="理论值 μ = 0.5")
    ax1.set_xlabel("掷硬币次数 n", fontsize=13)
    ax1.set_ylabel("正面比例 (样本均值)", fontsize=13)
    ax1.set_title("大数定律模拟：掷硬币正面比例趋近 0.5", fontsize=15,
                  fontweight="bold")
    ax1.set_ylim(0.3, 0.7)
    ax1.set_xscale("log")
    ax1.legend(fontsize=12, loc="upper right")
    ax1.fill_between(range(1, N+1), 0.3, 0.7, alpha=0.03, color="#3498db")

    # Annotations
    for n_val in [10, 100, 1000]:
        idx = n_val - 1
        ax1.annotate(f"n={n_val}: {cumulative_mean[idx]:.3f}",
                     xy=(n_val, cumulative_mean[idx]),
                     xytext=(n_val * 2, cumulative_mean[idx] + 0.06),
                     fontsize=9, ha="left",
                     arrowprops=dict(arrowstyle="->", color="#2c3e50", lw=1),
                     bbox=dict(boxstyle="round,pad=0.3", facecolor="#f9e79f",
                              alpha=0.8))

    # Bottom: CLT — histograms of sample means for different n
    sample_sizes = [1, 2, 5, 30]
    n_simulations = 10000

    for i, n in enumerate(sample_sizes):
        ax = fig.add_subplot(2, 4, 5 + i)
        sample_means = np.array([
            np.mean(np.random.randint(1, 7, n)) for _ in range(n_simulations)
        ])

        mu = 3.5
        sigma = np.sqrt(35/12)
        se = sigma / np.sqrt(n)

        ax.hist(sample_means, bins=30, density=True, color="#3498db", alpha=0.6,
                edgecolor="white", lw=0.5)

        if n >= 2:
            x_range = np.linspace(mu - 4*se, mu + 4*se, 200)
            normal_pdf = (1 / (se * np.sqrt(2*np.pi))) * np.exp(
                -(x_range - mu)**2 / (2*se**2))
            ax.plot(x_range, normal_pdf, color="#e74c3c", lw=2, label="正态近似")

        ax.axvline(mu, color="#2c3e50", ls="--", lw=1.5, alpha=0.6)
        ax.set_title(f"n = {n} 个骰子的均值", fontsize=11, fontweight="bold")
        ax.set_xlabel("样本均值", fontsize=10)
        if i == 0:
            ax.set_ylabel("密度", fontsize=10)

        if n >= 2:
            ax.legend(fontsize=8, loc="upper right")

    fig.suptitle("大数定律与中心极限定理", fontsize=18, fontweight="bold", y=1.02)
    plt.tight_layout()
    path = os.path.join(ABS_OUT, "p08-ch05-lln-simulation.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {path}")


if __name__ == "__main__":
    plot_lln_simulation()
    print("All Ch05 figures generated.")
