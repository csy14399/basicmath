"""
数论可视化

生成 Part 2 Chapter 3 所需的四张图：
  1. Eratosthenes 筛法过程
  2. 因式分解树
  3. 模运算时钟（mod 12）
  4. 勾股数可视化
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import numpy as np

# ── 配置中文字体 ──
_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

# ── 输出路径 ──
ABS_OUT = "/workspace/basicmath/images/code-generated"
os.makedirs(ABS_OUT, exist_ok=True)

DPI = 200


# ═══════════════════════════════════════════
# 图 1: Eratosthenes 筛法
# ═══════════════════════════════════════════
def plot_sieve_eratosthenes():
    N = 50
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.axis("off")
    fig.suptitle("Eratosthenes 筛法 (N = 50)", fontsize=15, fontweight="bold")

    is_prime = [False, False] + [True] * (N - 1)
    sieve_colors = {2: "#e74c3c", 3: "#3498db", 5: "#27ae60", 7: "#9b59b6"}

    composite_by = {}
    for p in [2, 3, 5, 7]:
        for mult in range(p * p, N + 1, p):
            if is_prime[mult]:
                is_prime[mult] = False
                composite_by[mult] = p

    for mult in range(4, N + 1):
        if not is_prime[mult] and mult not in composite_by:
            for p in [2, 3, 5, 7]:
                if mult % p == 0:
                    composite_by[mult] = p
                    break

    cols = 10
    rows = (N + cols - 1) // cols

    for num in range(1, N + 1):
        col = (num - 1) % cols
        row = (num - 1) // cols
        x = col * 1.3 + 0.5
        y = (rows - 1 - row) * 1.0 + 0.5

        if is_prime[num]:
            circle = plt.Circle((x, y), 0.4, fc="#f9e79f", ec="#f39c12", lw=2)
            ax.add_patch(circle)
            ax.text(x, y, str(num), ha="center", va="center",
                    fontsize=10, fontweight="bold", color="#2c3e50")
        elif num == 1:
            circle = plt.Circle((x, y), 0.4, fc="#d5dbdb", ec="#7f8c8d", lw=1)
            ax.add_patch(circle)
            ax.text(x, y, "1", ha="center", va="center",
                    fontsize=10, color="#7f8c8d")
        else:
            p_color = sieve_colors.get(composite_by.get(num, 2), "#bdc3c7")
            circle = plt.Circle((x, y), 0.4, fc="#f2f3f4", ec=p_color, lw=1.5,
                                linestyle="--")
            ax.add_patch(circle)
            ax.text(x, y, str(num), ha="center", va="center",
                    fontsize=9, color="#95a5a6")
            ax.plot([x - 0.25, x + 0.25], [y - 0.15, y + 0.15],
                    color=p_color, lw=1.5, alpha=0.7)

    legend_items = [
        mpatches.Patch(fc="#f9e79f", ec="#f39c12", label="质数 (Prime)"),
        mpatches.Patch(fc="#f2f3f4", ec="#e74c3c", label="被 2 筛掉", linestyle="--"),
        mpatches.Patch(fc="#f2f3f4", ec="#3498db", label="被 3 筛掉", linestyle="--"),
        mpatches.Patch(fc="#f2f3f4", ec="#27ae60", label="被 5 筛掉", linestyle="--"),
        mpatches.Patch(fc="#f2f3f4", ec="#9b59b6", label="被 7 筛掉", linestyle="--"),
    ]
    ax.legend(handles=legend_items, loc="lower center", ncol=5, fontsize=9,
              frameon=True, bbox_to_anchor=(0.5, -0.02))

    ax.set_xlim(-0.2, cols * 1.3 + 0.2)
    ax.set_ylim(-0.5, rows * 1.0 + 0.5)

    fname = "p02-ch03-sieve-eratosthenes.png"
    fig.savefig(os.path.join(ABS_OUT, fname), dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  已生成: {fname}")


# ═══════════════════════════════════════════
# 图 2: 因式分解树 (Factor Tree for 360)
# ═══════════════════════════════════════════
def plot_factor_tree():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis("off")
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 9)
    fig.suptitle("因式分解树: 360 = 2³ × 3² × 5", fontsize=15, fontweight="bold")

    nodes = {
        360:  (5, 8),
        2:    (3, 6.5),
        180:  (7, 6.5),
        "2b": (5.5, 5),
        90:   (8.5, 5),
        "2c": (7, 3.5),
        45:   (10, 3.5),
        "3a": (8.5, 2),
        15:   (11, 2),  # shift to avoid overlap... let me redo
        "3b": (9.5, 0.5),
        "5a": (12, 0.5),
    }

    tree = [
        (360, (5, 8), [(2, (3, 6.5)), (180, (7, 6.5))]),
    ]

    def draw_node(x, y, val, is_prime=False):
        color = "#e74c3c" if is_prime else "#3498db"
        fc = "#fadbd8" if is_prime else "#d6eaf8"
        circle = plt.Circle((x, y), 0.4, fc=fc, ec=color, lw=2, zorder=5)
        ax.add_patch(circle)
        ax.text(x, y, str(val), ha="center", va="center",
                fontsize=11, fontweight="bold", color=color, zorder=6)

    def draw_edge(x1, y1, x2, y2):
        ax.plot([x1, x2], [y1 - 0.4, y2 + 0.4], color="#7f8c8d", lw=1.5, zorder=1)

    positions = {
        360: (5, 7.5),
        "2a": (3, 6), 180: (7, 6),
        "2b": (5.5, 4.5), 90: (8.5, 4.5),
        "2c": (7, 3), 45: (10, 3),
        "3a": (8.5, 1.5), 15: (11.5, 1.5),
        "3b": (10, 0), "5": (13, 0),
    }

    # Redraw with better layout
    ax.set_xlim(0, 14)
    ax.set_ylim(-1.5, 9)

    pos = {
        360:  (7, 8),
        "2a": (4, 6), 180: (10, 6),
        "2b": (8, 4), 90: (12, 4),
        "2c": (10, 2), 45: (14, 2),  # too wide
    }

    # Simpler balanced layout
    ax.set_xlim(-1, 15)
    ax.set_ylim(-1, 9)

    lv0 = (7, 8)           # 360
    lv1 = [(4, 6.2), (10, 6.2)]  # 2, 180
    lv2 = [(8, 4.4), (12, 4.4)]  # 2, 90
    lv3 = [(10, 2.6), (14, 2.6)] # 2, 45
    lv4 = [(12, 0.8), (16, 0.8)] # but too wide

    # Let's use a narrower approach
    ax.set_xlim(0, 12)

    nodes_data = [
        (360, 6, 7.5, False),
        (2,   3.5, 6, True),
        (180, 8.5, 6, False),
        (2,   6.5, 4.5, True),
        (90,  10.5, 4.5, False),
        (2,   9, 3, True),
        (45,  12, 3, False),  # shift ax limits
        (9,   10.5, 1.5, False),
        (5,   13.5, 1.5, True),  # shift
        (3,   9, 0, True),
        (3,   12, 0, True),
    ]
    ax.set_xlim(0, 15)
    ax.set_ylim(-1, 9)

    # Simpler: use a cleaner tree
    ax.clear()
    ax.axis("off")
    ax.set_xlim(0, 14)
    ax.set_ylim(-1, 9)

    # 360 = 2 × 180 = 2 × 2 × 90 = 2 × 2 × 2 × 45 = 2 × 2 × 2 × 9 × 5
    #                                                  = 2³ × 3² × 5
    tree_nodes = [
        # (value, x, y, is_prime)
        (360,  7, 8, False),
        (2,    4, 6.3, True),
        (180,  10, 6.3, False),
        (2,    8, 4.8, True),
        (90,   12, 4.8, False),
        (2,    10, 3.3, True),
        (45,   14, 3.3, False),  # actually let me limit x
    ]

    # Better approach: narrower, shift children less
    ax.set_xlim(0, 13)

    tree_n = [
        (360,  6,   7.5, False),
        (2,    3.5, 6,   True),
        (180,  8.5, 6,   False),
        (2,    7,   4.5, True),
        (90,   10,  4.5, False),
        (2,    8.5, 3,   True),
        (45,   11.5, 3,  False),
        (9,    10,  1.5, False),
        (5,    13,  1.5, True),  # shift
        (3,    8.5, 0,   True),
        (3,    11.5, 0,  True),
    ]
    ax.set_xlim(0, 14)

    edges = [
        (0, 1), (0, 2),  # 360 -> 2, 180
        (2, 3), (2, 4),  # 180 -> 2, 90
        (4, 5), (4, 6),  # 90 -> 2, 45
        (6, 7), (6, 8),  # 45 -> 9, 5
        (7, 9), (7, 10), # 9 -> 3, 3
    ]

    for parent_i, child_i in edges:
        _, x1, y1, _ = tree_n[parent_i]
        _, x2, y2, _ = tree_n[child_i]
        draw_edge(x1, y1, x2, y2)

    for val, x, y, is_p in tree_n:
        draw_node(x, y, val, is_prime=is_p)

    ax.text(7, -0.7, "$360 = 2^3 \\times 3^2 \\times 5$",
            ha="center", fontsize=13, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", fc="#eaf2f8", ec="#3498db"))

    legend_items = [
        mpatches.Patch(fc="#fadbd8", ec="#e74c3c", label="质数 (Prime)"),
        mpatches.Patch(fc="#d6eaf8", ec="#3498db", label="合数 (Composite)"),
    ]
    ax.legend(handles=legend_items, loc="upper left", fontsize=10, frameon=True)

    fname = "p02-ch03-factor-tree.png"
    fig.savefig(os.path.join(ABS_OUT, fname), dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  已生成: {fname}")


# ═══════════════════════════════════════════
# 图 3: 模运算时钟 (mod 12)
# ═══════════════════════════════════════════
def plot_modular_clock():
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    fig.suptitle("模运算时钟", fontsize=15, fontweight="bold")

    # ── 左: mod 12 时钟 ──
    ax = axes[0]
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.8, 1.8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("$\\mathbb{Z}/12\\mathbb{Z}$ — 12 小时制", fontsize=12)

    theta_vals = np.linspace(0, 2 * np.pi, 100)
    ax.plot(1.3 * np.cos(theta_vals), 1.3 * np.sin(theta_vals),
            color="#bdc3c7", lw=2)

    for i in range(12):
        angle = np.pi / 2 - 2 * np.pi * i / 12
        x = 1.3 * np.cos(angle)
        y = 1.3 * np.sin(angle)
        ax.plot(x, y, "o", color="#2c3e50", markersize=14, zorder=5)
        ax.text(x * 1.18, y * 1.18, str(i), ha="center", va="center",
                fontsize=11, fontweight="bold", color="white", zorder=6)

    def draw_arrow(ax, start, end, color, mod=12, label=""):
        a1 = np.pi / 2 - 2 * np.pi * start / mod
        a2 = np.pi / 2 - 2 * np.pi * end / mod
        r = 1.0
        x1, y1 = r * np.cos(a1), r * np.sin(a1)
        x2, y2 = r * np.cos(a2), r * np.sin(a2)
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->,head_width=0.15",
                                    color=color, lw=2,
                                    connectionstyle="arc3,rad=0.3"))
        if label:
            mx = (x1 + x2) / 2 * 0.6
            my = (y1 + y2) / 2 * 0.6
            ax.text(mx, my, label, ha="center", va="center",
                    fontsize=9, color=color, fontweight="bold")

    draw_arrow(ax, 7, 11, "#e74c3c", label="+4")
    ax.text(0, -1.6, "7 + 4 ≡ 11 (mod 12)",
            ha="center", fontsize=10, color="#e74c3c")

    draw_arrow(ax, 10, 2, "#3498db", label="+4")
    ax.text(0, -1.85, "10 + 4 ≡ 2 (mod 12)",
            ha="center", fontsize=10, color="#3498db")

    # ── 右: mod 7 时钟 ──
    ax = axes[1]
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.8, 1.8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("$\\mathbb{Z}/7\\mathbb{Z}$ — 一周七天", fontsize=12)

    ax.plot(1.3 * np.cos(theta_vals), 1.3 * np.sin(theta_vals),
            color="#bdc3c7", lw=2)

    days = ["0\n(日)", "1\n(一)", "2\n(二)", "3\n(三)",
            "4\n(四)", "5\n(五)", "6\n(六)"]
    for i in range(7):
        angle = np.pi / 2 - 2 * np.pi * i / 7
        x = 1.3 * np.cos(angle)
        y = 1.3 * np.sin(angle)
        ax.plot(x, y, "o", color="#27ae60", markersize=18, zorder=5)
        ax.text(x * 1.18, y * 1.18, days[i], ha="center", va="center",
                fontsize=8, fontweight="bold", color="white", zorder=6)

    draw_arrow(ax, 1, 4, "#e74c3c", mod=7, label="+3")
    ax.text(0, -1.6, "周一 $+ 3$ 天 $=$ 周四",
            ha="center", fontsize=10, color="#e74c3c")

    draw_arrow(ax, 5, 1, "#9b59b6", mod=7, label="+3")
    ax.text(0, -1.85, "周五 $+ 3$ 天 $=$ 周一",
            ha="center", fontsize=10, color="#9b59b6")

    plt.tight_layout()
    fname = "p02-ch03-modular-clock.png"
    fig.savefig(os.path.join(ABS_OUT, fname), dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  已生成: {fname}")


# ═══════════════════════════════════════════
# 图 4: 勾股数 (Pythagorean Triples)
# ═══════════════════════════════════════════
def plot_pythagorean_triples():
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    fig.suptitle("勾股数 (Pythagorean Triples)", fontsize=15, fontweight="bold")

    # ── 左: 3-4-5 三角形 ──
    ax = axes[0]
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-0.5, 4.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("经典勾股数: (3, 4, 5)", fontsize=12)

    triangle = plt.Polygon([(0, 0), (4, 0), (0, 3)],
                           fill=True, fc="#d5f5e3", ec="#27ae60", lw=2)
    ax.add_patch(triangle)

    ax.text(2, -0.3, "$a = 4$", ha="center", fontsize=12, fontweight="bold", color="#2c3e50")
    ax.text(-0.4, 1.5, "$b = 3$", ha="center", fontsize=12, fontweight="bold", color="#2c3e50",
            rotation=90)
    ax.text(2.3, 1.8, "$c = 5$", ha="center", fontsize=12, fontweight="bold", color="#e74c3c",
            rotation=-37)

    sq = plt.Rectangle((0, 0), 0.3, 0.3, fill=False, ec="#7f8c8d", lw=1)
    ax.add_patch(sq)

    ax.text(2.5, 3.5, "$3^2 + 4^2 = 9 + 16 = 25 = 5^2$",
            fontsize=11, ha="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="#fadbd8", ec="#e74c3c", alpha=0.8))

    # ── 右: 参数化列表 ──
    ax = axes[1]
    ax.axis("off")
    ax.set_title("本原勾股数 ($m > n > 0$, $\\gcd(m,n)=1$, 奇偶不同)", fontsize=11)

    data = []
    for m in range(2, 8):
        for n in range(1, m):
            if np.gcd(m, n) == 1 and (m - n) % 2 == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                if c <= 100:
                    data.append([str(m), str(n), str(a), str(b), str(c)])

    col_labels = ["$m$", "$n$", "$a = m^2-n^2$", "$b = 2mn$", "$c = m^2+n^2$"]

    table = ax.table(cellText=data, colLabels=col_labels,
                     loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.0, 1.6)

    for j in range(5):
        cell = table[0, j]
        cell.set_facecolor("#2c3e50")
        cell.set_text_props(color="white", fontweight="bold", fontsize=10)

    for i in range(1, len(data) + 1):
        for j in range(5):
            cell = table[i, j]
            cell.set_facecolor("#ecf0f1" if i % 2 == 0 else "#ffffff")
            if j >= 2:
                cell.set_text_props(color="#2980b9", fontweight="bold")

    plt.tight_layout()
    fname = "p02-ch03-pythagorean-triples.png"
    fig.savefig(os.path.join(ABS_OUT, fname), dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  已生成: {fname}")


# ═══════════════════════════════════════════
if __name__ == "__main__":
    print("Part 2 Ch03 — 数论可视化")
    plot_sieve_eratosthenes()
    plot_factor_tree()
    plot_modular_clock()
    plot_pythagorean_triples()
    print("全部完成！")
