"""
条件概率与 Bayes 定理可视化

生成 Part 8 Chapter 2 所需的三张图：
  1. 条件概率面积图 (p08-ch02-conditional-area.png)
  2. Bayes 更新过程图 (p08-ch02-bayes-update.png)
  3. 自然频率树形图 (p08-ch02-frequency-tree.png)
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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


def plot_conditional_area():
    """条件概率的面积图: P(A|B) = P(A∩B) / P(B)"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    for ax in axes:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 7)
        ax.set_aspect("equal")
        ax.axis("off")

    # Panel 1: Sample space with A and B
    ax = axes[0]
    ax.set_title("样本空间 Ω", fontsize=13, fontweight="bold")
    rect = mpatches.FancyBboxPatch((0.5, 0.5), 9, 6, boxstyle="round,pad=0.1",
                                    facecolor="#ecf0f1", edgecolor="black", lw=2)
    ax.add_patch(rect)
    circle_a = plt.Circle((3.5, 3.5), 2.2, facecolor="#3498db", alpha=0.4,
                           edgecolor="#2980b9", lw=2)
    circle_b = plt.Circle((6.5, 3.5), 2.2, facecolor="#e74c3c", alpha=0.4,
                           edgecolor="#c0392b", lw=2)
    ax.add_patch(circle_a)
    ax.add_patch(circle_b)
    ax.text(2.5, 3.5, "A", fontsize=18, ha="center", va="center", fontweight="bold",
            color="#2980b9")
    ax.text(7.5, 3.5, "B", fontsize=18, ha="center", va="center", fontweight="bold",
            color="#c0392b")
    ax.text(5, 3.5, "A∩B", fontsize=12, ha="center", va="center", fontweight="bold",
            color="#8e44ad")
    ax.text(9, 0.2, "Ω", fontsize=14, ha="center")

    # Panel 2: Highlight B (condition)
    ax = axes[1]
    ax.set_title("条件：已知 B 发生", fontsize=13, fontweight="bold")
    rect2 = mpatches.FancyBboxPatch((0.5, 0.5), 9, 6, boxstyle="round,pad=0.1",
                                     facecolor="#bdc3c7", alpha=0.5, edgecolor="black", lw=2)
    ax.add_patch(rect2)
    circle_b2 = plt.Circle((6.5, 3.5), 2.2, facecolor="#e74c3c", alpha=0.5,
                            edgecolor="#c0392b", lw=2)
    ax.add_patch(circle_b2)
    ax.text(6.5, 5, "新的\n样本空间 B", fontsize=11, ha="center", va="center",
            fontweight="bold", color="#c0392b")
    theta = np.linspace(0, 2 * np.pi, 200)
    xa = 3.5 + 2.2 * np.cos(theta)
    ya = 3.5 + 2.2 * np.sin(theta)
    ax.plot(xa, ya, color="#2980b9", lw=2, ls="--", alpha=0.6)
    ax.fill_between([4.3, 4.3], [0], [0], alpha=0)
    from matplotlib.patches import Wedge
    ax.text(5, 3.5, "A∩B", fontsize=12, ha="center", va="center", fontweight="bold",
            color="#8e44ad")

    # Panel 3: Result
    ax = axes[2]
    ax.set_title("P(A|B) = P(A∩B) / P(B)", fontsize=13, fontweight="bold")
    rect3 = mpatches.FancyBboxPatch((0.5, 0.5), 9, 6, boxstyle="round,pad=0.1",
                                     facecolor="#bdc3c7", alpha=0.3, edgecolor="black", lw=2)
    ax.add_patch(rect3)
    circle_b3 = plt.Circle((6.5, 3.5), 2.2, facecolor="#fadbd8", alpha=0.6,
                            edgecolor="#c0392b", lw=2)
    ax.add_patch(circle_b3)
    from matplotlib.patches import Arc
    intersect = mpatches.Wedge((5, 3.5), 2.2, -60, 60, facecolor="#8e44ad",
                                alpha=0.6, edgecolor="none")
    ax.text(5.5, 3.5, "A∩B", fontsize=14, ha="center", va="center", fontweight="bold",
            color="white",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#8e44ad", alpha=0.8))
    ax.text(5, 1.2, "P(A|B) = 紫色部分 / 红色圆", fontsize=11, ha="center",
            fontweight="bold")
    ax.text(7.5, 3.5, "B 中\n非 A 部分", fontsize=10, ha="center", va="center",
            color="#c0392b", alpha=0.8)

    plt.tight_layout()
    path = os.path.join(ABS_OUT, "p08-ch02-conditional-area.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {path}")


def plot_bayes_update():
    """Bayes 更新过程: 先验 → 似然 → 后验"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    x = np.linspace(0, 1, 500)

    # Prior: Beta(2, 5) - tilted towards low p
    from math import gamma as gamma_func
    def beta_pdf(x, a, b):
        B = gamma_func(a) * gamma_func(b) / gamma_func(a + b)
        return x**(a-1) * (1-x)**(b-1) / B

    # Prior
    ax = axes[0]
    prior = np.array([beta_pdf(xi, 2, 5) for xi in x])
    ax.fill_between(x, prior, alpha=0.3, color="#3498db")
    ax.plot(x, prior, color="#2980b9", lw=2.5)
    ax.set_title("先验分布 (Prior)", fontsize=14, fontweight="bold")
    ax.set_xlabel("参数 p", fontsize=12)
    ax.set_ylabel("密度", fontsize=12)
    ax.set_ylim(0, max(prior) * 1.3)
    ax.axvline(2/7, color="#2980b9", ls="--", alpha=0.6, label=f"先验均值 ≈ {2/7:.2f}")
    ax.legend(fontsize=10)

    # Likelihood: observed 7 successes in 10 trials
    ax = axes[1]
    likelihood = np.array([xi**7 * (1-xi)**3 for xi in x])
    likelihood = likelihood / (likelihood.max() + 1e-12) * max(prior)
    ax.fill_between(x, likelihood, alpha=0.3, color="#e74c3c")
    ax.plot(x, likelihood, color="#c0392b", lw=2.5)
    ax.set_title("似然函数 (Likelihood)\n观测：10 次中 7 次成功", fontsize=14,
                 fontweight="bold")
    ax.set_xlabel("参数 p", fontsize=12)
    ax.set_ylabel("似然（已标准化）", fontsize=12)
    ax.set_ylim(0, max(prior) * 1.3)
    ax.axvline(0.7, color="#c0392b", ls="--", alpha=0.6, label="MLE = 0.70")
    ax.legend(fontsize=10)

    # Posterior: Beta(2+7, 5+3) = Beta(9, 8)
    ax = axes[2]
    posterior = np.array([beta_pdf(xi, 9, 8) for xi in x])
    ax.fill_between(x, posterior, alpha=0.3, color="#27ae60")
    ax.plot(x, posterior, color="#27ae60", lw=2.5)
    prior_rescaled = np.array([beta_pdf(xi, 2, 5) for xi in x])
    ax.plot(x, prior_rescaled, color="#3498db", lw=1.5, ls="--", alpha=0.5,
            label="先验")
    ax.set_title("后验分布 (Posterior)\n后验 ∝ 先验 × 似然", fontsize=14,
                 fontweight="bold")
    ax.set_xlabel("参数 p", fontsize=12)
    ax.set_ylabel("密度", fontsize=12)
    ax.set_ylim(0, max(posterior) * 1.3)
    ax.axvline(9/17, color="#27ae60", ls="--", alpha=0.6,
               label=f"后验均值 ≈ {9/17:.2f}")
    ax.legend(fontsize=10)

    plt.tight_layout()
    path = os.path.join(ABS_OUT, "p08-ch02-bayes-update.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {path}")


def plot_frequency_tree():
    """自然频率树形图: 医学检测的 Bayes 分析"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(-1, 11)
    ax.set_ylim(-0.5, 8.5)
    ax.axis("off")
    ax.set_title("自然频率树形图：医学检测的 Bayes 分析", fontsize=15,
                 fontweight="bold", pad=15)

    box_style = dict(boxstyle="round,pad=0.4", facecolor="#ecf0f1", edgecolor="#2c3e50",
                     lw=1.5)
    highlight_style = dict(boxstyle="round,pad=0.4", facecolor="#fadbd8",
                           edgecolor="#c0392b", lw=2)
    green_style = dict(boxstyle="round,pad=0.4", facecolor="#d5f5e3",
                       edgecolor="#27ae60", lw=2)

    # Root
    ax.text(5, 8, "100,000 人", fontsize=14, ha="center", va="center",
            bbox=box_style, fontweight="bold")

    # Level 1
    ax.annotate("", xy=(2, 6.5), xytext=(5, 7.5),
                arrowprops=dict(arrowstyle="-|>", color="#2c3e50", lw=2))
    ax.annotate("", xy=(8, 6.5), xytext=(5, 7.5),
                arrowprops=dict(arrowstyle="-|>", color="#2c3e50", lw=2))
    ax.text(3, 7.3, "患病 0.1%", fontsize=10, ha="center", color="#c0392b")
    ax.text(7, 7.3, "健康 99.9%", fontsize=10, ha="center", color="#27ae60")

    ax.text(2, 6, "100 人\n(患病)", fontsize=12, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#fadbd8",
                      edgecolor="#c0392b", lw=1.5), fontweight="bold")
    ax.text(8, 6, "99,900 人\n(健康)", fontsize=12, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.4", facecolor="#d5f5e3",
                      edgecolor="#27ae60", lw=1.5), fontweight="bold")

    # Level 2 - patients
    ax.annotate("", xy=(0.8, 3.8), xytext=(2, 5.3),
                arrowprops=dict(arrowstyle="-|>", color="#c0392b", lw=1.5))
    ax.annotate("", xy=(3.2, 3.8), xytext=(2, 5.3),
                arrowprops=dict(arrowstyle="-|>", color="#c0392b", lw=1.5))
    ax.text(1, 4.8, "阳性 99%", fontsize=9, ha="center", color="#e74c3c")
    ax.text(3, 4.8, "阴性 1%", fontsize=9, ha="center", color="#7f8c8d")

    ax.text(0.8, 3.2, "99 人\n(真阳性)", fontsize=11, ha="center", va="center",
            bbox=highlight_style, fontweight="bold")
    ax.text(3.2, 3.2, "1 人\n(假阴性)", fontsize=10, ha="center", va="center",
            bbox=box_style)

    # Level 2 - healthy
    ax.annotate("", xy=(6.8, 3.8), xytext=(8, 5.3),
                arrowprops=dict(arrowstyle="-|>", color="#27ae60", lw=1.5))
    ax.annotate("", xy=(9.2, 3.8), xytext=(8, 5.3),
                arrowprops=dict(arrowstyle="-|>", color="#27ae60", lw=1.5))
    ax.text(7, 4.8, "阳性 2%", fontsize=9, ha="center", color="#e74c3c")
    ax.text(9.2, 4.8, "阴性 98%", fontsize=9, ha="center", color="#27ae60")

    ax.text(6.8, 3.2, "1,998 人\n(假阳性)", fontsize=11, ha="center", va="center",
            bbox=highlight_style, fontweight="bold")
    ax.text(9.2, 3.2, "97,902 人\n(真阴性)", fontsize=10, ha="center", va="center",
            bbox=green_style)

    # Bottom result
    result_box = dict(boxstyle="round,pad=0.5", facecolor="#f9e79f",
                      edgecolor="#f39c12", lw=2)
    ax.text(5, 1.0,
            "总阳性 = 99 + 1,998 = 2,097 人\n"
            "P(患病 | 阳性) = 99 / 2,097 ≈ 4.7%",
            fontsize=13, ha="center", va="center", bbox=result_box, fontweight="bold")

    ax.annotate("", xy=(3.5, 1.5), xytext=(0.8, 2.7),
                arrowprops=dict(arrowstyle="-|>", color="#f39c12", lw=1.5, ls="--"))
    ax.annotate("", xy=(6.5, 1.5), xytext=(6.8, 2.7),
                arrowprops=dict(arrowstyle="-|>", color="#f39c12", lw=1.5, ls="--"))

    path = os.path.join(ABS_OUT, "p08-ch02-frequency-tree.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {path}")


if __name__ == "__main__":
    plot_conditional_area()
    plot_bayes_update()
    plot_frequency_tree()
    print("All Ch02 figures generated.")
