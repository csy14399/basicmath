"""
集合论可视化

为 Part 1 Chapter 2 生成以下图形：
  1. Venn 图：并集、交集、差集、对称差
  2. 笛卡尔积（网格点）
  3. 单射/满射/双射（箭头图）
  4. 等价类（模 3 划分数轴）
  5. Hasse 图（{1,2,3,4,6,12} 上的整除关系）
  6. Cantor 对角线论证
  7. 幂集结构
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
from matplotlib.patches import FancyArrowPatch, Circle
import numpy as np

# ── 配置中文字体 ──
_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

# ── 输出目录 ──
OUT_DIR = "/workspace/basicmath/images/code-generated"
os.makedirs(OUT_DIR, exist_ok=True)


def save(fig, name):
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  已生成: {name}")


# ═══════════════════════════════════════════════════════════════
# 1. Venn 图：∪, ∩, \, △
# ═══════════════════════════════════════════════════════════════

def draw_venn_base(ax, title):
    """绘制两个交叉圆的基础 Venn 图框架"""
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2, 2)
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=14, fontweight="bold", pad=10)
    ax.axis("off")
    return (-0.6, 0), (0.6, 0), 1.2  # 左圆心、右圆心、半径


def venn_circles(ax, fill_left=False, fill_right=False, fill_inter=False,
                 fill_only_left=False, fill_only_right=False):
    """根据参数填充 Venn 图区域"""
    lc, rc, r = (-0.6, 0), (0.6, 0), 1.2
    theta = np.linspace(0, 2 * np.pi, 300)

    # 生成区域点集
    xx, yy = np.meshgrid(np.linspace(-2.5, 2.5, 500), np.linspace(-2, 2, 400))
    in_left = (xx - lc[0])**2 + (yy - lc[1])**2 <= r**2
    in_right = (xx - rc[0])**2 + (yy - rc[1])**2 <= r**2

    if fill_left and fill_right:  # 并集
        region = in_left | in_right
        ax.contourf(xx, yy, region.astype(float), levels=[0.5, 1.5],
                    colors=["#3498db"], alpha=0.35)
    elif fill_inter:  # 交集
        region = in_left & in_right
        ax.contourf(xx, yy, region.astype(float), levels=[0.5, 1.5],
                    colors=["#e74c3c"], alpha=0.4)
    elif fill_only_left:  # 差集 A \ B
        region = in_left & ~in_right
        ax.contourf(xx, yy, region.astype(float), levels=[0.5, 1.5],
                    colors=["#2ecc71"], alpha=0.4)
    elif fill_only_right:  # 差集 B \ A（对称差用）
        region = (in_left & ~in_right) | (~in_left & in_right)
        ax.contourf(xx, yy, region.astype(float), levels=[0.5, 1.5],
                    colors=["#9b59b6"], alpha=0.35)

    # 圆的边界
    for center in (lc, rc):
        circle = plt.Circle(center, r, fill=False, edgecolor="#2c3e50",
                            linewidth=2)
        ax.add_patch(circle)

    ax.text(lc[0] - 0.55, 1.05, "A", fontsize=15, fontweight="bold",
            ha="center", color="#2c3e50")
    ax.text(rc[0] + 0.55, 1.05, "B", fontsize=15, fontweight="bold",
            ha="center", color="#2c3e50")


fig, axes = plt.subplots(1, 4, figsize=(18, 4.5))
fig.suptitle("集合运算 Venn 图 (Set Operations)", fontsize=16,
             fontweight="bold", y=1.02)

titles = ["A ∪ B （并集）", "A ∩ B （交集）", "A \\ B （差集）", "A △ B （对称差）"]
for ax, title in zip(axes, titles):
    draw_venn_base(ax, title)

venn_circles(axes[0], fill_left=True, fill_right=True)
venn_circles(axes[1], fill_inter=True)
venn_circles(axes[2], fill_only_left=True)
venn_circles(axes[3], fill_only_right=True)

plt.tight_layout()
save(fig, "p01-ch02-venn-operations.png")


# ═══════════════════════════════════════════════════════════════
# 2. 笛卡尔积（网格点）
# ═══════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(7, 6))
ax.set_title("笛卡尔积 A × B (Cartesian Product)", fontsize=15, fontweight="bold")

A = [1, 2, 3]
B = ["a", "b", "c", "d"]

for i, a in enumerate(A):
    for j, b in enumerate(B):
        ax.plot(i, j, "o", color="#2980b9", markersize=12, zorder=5)
        ax.annotate(f"({a}, {b})", (i, j), textcoords="offset points",
                    xytext=(8, 6), fontsize=9, color="#2c3e50")

ax.set_xticks(range(len(A)))
ax.set_xticklabels([str(a) for a in A], fontsize=13)
ax.set_yticks(range(len(B)))
ax.set_yticklabels(B, fontsize=13)
ax.set_xlabel("A = {1, 2, 3}", fontsize=13)
ax.set_ylabel("B = {a, b, c, d}", fontsize=13)
ax.set_xlim(-0.5, len(A) - 0.5)
ax.set_ylim(-0.5, len(B) - 0.5)
ax.grid(True, linestyle="--", alpha=0.3)
ax.set_axisbelow(True)

plt.tight_layout()
save(fig, "p01-ch02-cartesian-product.png")


# ═══════════════════════════════════════════════════════════════
# 3. 单射/满射/双射箭头图
# ═══════════════════════════════════════════════════════════════

def draw_arrow_diagram(ax, title, left_labels, right_labels, mappings, subtitle=""):
    """
    绘制从左集合到右集合的箭头映射图。
    mappings: list of (left_idx, right_idx)
    """
    ax.set_xlim(-1, 5)
    n_left = len(left_labels)
    n_right = len(right_labels)
    max_n = max(n_left, n_right)
    ax.set_ylim(-0.5, max_n + 0.5)
    ax.set_aspect("equal")
    ax.set_title(f"{title}\n{subtitle}", fontsize=12, fontweight="bold", pad=8)
    ax.axis("off")

    left_x, right_x = 0.8, 3.2
    left_ys = np.linspace(max_n - 0.5, 0.5, n_left)
    right_ys = np.linspace(max_n - 0.5, 0.5, n_right)

    # 椭圆框
    from matplotlib.patches import Ellipse
    ell_h = max_n * 0.55 + 0.3
    ax.add_patch(Ellipse((left_x, max_n / 2), 1.3, max_n + 0.8,
                         fill=False, edgecolor="#3498db", linewidth=2))
    ax.add_patch(Ellipse((right_x, max_n / 2), 1.3, max_n + 0.8,
                         fill=False, edgecolor="#e74c3c", linewidth=2))

    ax.text(left_x, -0.3, "A", fontsize=13, ha="center", fontweight="bold",
            color="#3498db")
    ax.text(right_x, -0.3, "B", fontsize=13, ha="center", fontweight="bold",
            color="#e74c3c")

    for i, (label, y) in enumerate(zip(left_labels, left_ys)):
        ax.plot(left_x, y, "o", color="#3498db", markersize=10, zorder=5)
        ax.text(left_x - 0.35, y, label, fontsize=11, ha="right", va="center")

    for i, (label, y) in enumerate(zip(right_labels, right_ys)):
        ax.plot(right_x, y, "o", color="#e74c3c", markersize=10, zorder=5)
        ax.text(right_x + 0.35, y, label, fontsize=11, ha="left", va="center")

    for li, ri in mappings:
        y_start = left_ys[li]
        y_end = right_ys[ri]
        ax.annotate("", xy=(right_x - 0.12, y_end),
                    xytext=(left_x + 0.12, y_start),
                    arrowprops=dict(arrowstyle="->", color="#2c3e50",
                                    lw=1.5, connectionstyle="arc3,rad=0.1"))


fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("函数类型 (Types of Functions)", fontsize=16, fontweight="bold",
             y=1.02)

# 单射 (Injection)：不同元素映到不同元素，但 B 中可能有元素不被映到
draw_arrow_diagram(
    axes[0], "单射 (Injection)", ["1", "2", "3"], ["a", "b", "c", "d"],
    [(0, 0), (1, 2), (2, 3)],
    subtitle="一对一，但不满"
)

# 满射 (Surjection)：B 中每个元素都被映到，但可能多对一
draw_arrow_diagram(
    axes[1], "满射 (Surjection)", ["1", "2", "3", "4"], ["a", "b", "c"],
    [(0, 0), (1, 1), (2, 2), (3, 1)],
    subtitle="满，但不一对一"
)

# 双射 (Bijection)：一一对应
draw_arrow_diagram(
    axes[2], "双射 (Bijection)", ["1", "2", "3"], ["a", "b", "c"],
    [(0, 0), (1, 1), (2, 2)],
    subtitle="一一对应"
)

plt.tight_layout()
save(fig, "p01-ch02-injection-surjection-bijection.png")


# ═══════════════════════════════════════════════════════════════
# 4. 等价类（模 3 划分数轴）
# ═══════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(14, 4))
ax.set_title("等价类：模 3 的划分 (Equivalence Classes: Partition by mod 3)",
             fontsize=15, fontweight="bold")

colors = ["#3498db", "#e74c3c", "#2ecc71"]
class_labels = ["[0]₃ = {0, 3, 6, 9, …}", "[1]₃ = {1, 4, 7, 10, …}",
                "[2]₃ = {2, 5, 8, 11, …}"]

numbers = range(0, 13)
for n in numbers:
    cls = n % 3
    ax.plot(n, 0, "o", color=colors[cls], markersize=18, zorder=5)
    ax.text(n, 0, str(n), fontsize=10, ha="center", va="center",
            color="white", fontweight="bold", zorder=6)

ax.axhline(0, color="#bdc3c7", linewidth=1, zorder=1)
ax.text(12.8, 0, "…", fontsize=16, va="center")

# 图例
patches = [mpatches.Patch(color=c, label=l) for c, l in zip(colors, class_labels)]
ax.legend(handles=patches, loc="upper center", fontsize=11, ncol=3,
          bbox_to_anchor=(0.5, -0.08), frameon=False)

ax.set_xlim(-0.8, 13.5)
ax.set_ylim(-0.6, 0.6)
ax.axis("off")

plt.tight_layout()
save(fig, "p01-ch02-equivalence-classes.png")


# ═══════════════════════════════════════════════════════════════
# 5. Hasse 图：{1,2,3,4,6,12} 上的整除关系
# ═══════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(7, 8))
ax.set_title("Hasse 图：{1,2,3,4,6,12} 上的整除偏序\n(Hasse Diagram: Divisibility on {1,2,3,4,6,12})",
             fontsize=13, fontweight="bold")

# 节点位置（手动布局使图美观）
positions = {
    1:  (0, 0),
    2:  (-1, 1),
    3:  (1, 1),
    4:  (-1.5, 2),
    6:  (0.5, 2),
    12: (0, 3),
}

# 覆盖关系（a covers b 当且仅当 b | a 且不存在 b | c | a）
covers = [(1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 12), (6, 12)]

for a, b in covers:
    x0, y0 = positions[a]
    x1, y1 = positions[b]
    ax.plot([x0, x1], [y0, y1], "-", color="#7f8c8d", linewidth=2, zorder=1)

for val, (x, y) in positions.items():
    ax.plot(x, y, "o", color="#2980b9", markersize=28, zorder=3)
    ax.text(x, y, str(val), fontsize=14, ha="center", va="center",
            color="white", fontweight="bold", zorder=4)

ax.set_xlim(-2.5, 2)
ax.set_ylim(-0.8, 3.8)
ax.set_aspect("equal")
ax.axis("off")

ax.text(0, -0.6, "a — b 表示 a | b（a 整除 b），较大元素在上方",
        fontsize=10, ha="center", color="#7f8c8d", style="italic")

plt.tight_layout()
save(fig, "p01-ch02-hasse-diagram.png")


# ═══════════════════════════════════════════════════════════════
# 6. Cantor 对角线论证
# ═══════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(8, 7))
ax.set_title("Cantor 对角线论证 (Cantor's Diagonal Argument)",
             fontsize=15, fontweight="bold")

# 模拟一个假设的自然数→{0,1}序列的映射表
np.random.seed(42)
N = 7
table = np.random.randint(0, 2, size=(N, N))

# 绘制表格
for i in range(N):
    for j in range(N):
        color = "#ecf0f1"
        text_color = "#2c3e50"
        if i == j:
            color = "#e74c3c"
            text_color = "white"
        ax.add_patch(plt.Rectangle((j, N - 1 - i), 1, 1, facecolor=color,
                                    edgecolor="#bdc3c7", linewidth=1))
        ax.text(j + 0.5, N - 0.5 - i, str(table[i, j]),
                ha="center", va="center", fontsize=14,
                fontweight="bold" if i == j else "normal",
                color=text_color)

# 对角线元素构造新序列（取反）
diag = [table[i, i] for i in range(N)]
new_seq = [1 - d for d in diag]

# 在底部显示新序列
ax.text(N / 2, -0.8, "对角线元素：" + " ".join(str(d) for d in diag),
        ha="center", fontsize=11, color="#e74c3c")
ax.text(N / 2, -1.4, "取反得新序列：" + " ".join(str(d) for d in new_seq),
        ha="center", fontsize=11, fontweight="bold", color="#2980b9")
ax.text(N / 2, -2.0, "此序列不在表中 → 映射不是满射 → R 不可数",
        ha="center", fontsize=10, color="#7f8c8d", style="italic")

# 行/列标签
for i in range(N):
    ax.text(-0.3, N - 0.5 - i, f"f({i+1})", ha="right", va="center",
            fontsize=11, color="#2c3e50")
    ax.text(i + 0.5, N + 0.3, f"第{i+1}位", ha="center", va="bottom",
            fontsize=10, color="#2c3e50")

ax.set_xlim(-1, N + 0.5)
ax.set_ylim(-2.5, N + 0.8)
ax.set_aspect("equal")
ax.axis("off")

plt.tight_layout()
save(fig, "p01-ch02-cantor-diagonal.png")


# ═══════════════════════════════════════════════════════════════
# 7. 幂集结构
# ═══════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title("幂集结构：P({a, b, c}) 的 Hasse 图\n"
             "(Power Set Structure: Hasse Diagram of P({a, b, c}))",
             fontsize=14, fontweight="bold")

# 𝒫({a,b,c}) 按层排列
layers = [
    [("∅", (0, 0))],
    [("{a}", (-2.5, 1.5)), ("{b}", (0, 1.5)), ("{c}", (2.5, 1.5))],
    [("{a,b}", (-2.5, 3)), ("{a,c}", (0, 3)), ("{b,c}", (2.5, 3))],
    [("{a,b,c}", (0, 4.5))],
]

# 包含关系的边
edges = [
    ("∅", "{a}"), ("∅", "{b}"), ("∅", "{c}"),
    ("{a}", "{a,b}"), ("{a}", "{a,c}"),
    ("{b}", "{a,b}"), ("{b}", "{b,c}"),
    ("{c}", "{a,c}"), ("{c}", "{b,c}"),
    ("{a,b}", "{a,b,c}"), ("{a,c}", "{a,b,c}"), ("{b,c}", "{a,b,c}"),
]

pos = {}
for layer in layers:
    for label, p in layer:
        pos[label] = p

layer_colors = ["#95a5a6", "#3498db", "#e67e22", "#e74c3c"]

for e in edges:
    x0, y0 = pos[e[0]]
    x1, y1 = pos[e[1]]
    ax.plot([x0, x1], [y0, y1], "-", color="#bdc3c7", linewidth=1.5, zorder=1)

for li, layer in enumerate(layers):
    for label, (x, y) in layer:
        ax.plot(x, y, "o", color=layer_colors[li], markersize=20, zorder=3)
        ax.text(x, y - 0.55, label, ha="center", va="top", fontsize=11,
                fontweight="bold", color="#2c3e50")

# 层标签
ax.text(4.2, 0, "|S| = 0", fontsize=10, color="#7f8c8d", va="center")
ax.text(4.2, 1.5, "|S| = 1", fontsize=10, color="#7f8c8d", va="center")
ax.text(4.2, 3, "|S| = 2", fontsize=10, color="#7f8c8d", va="center")
ax.text(4.2, 4.5, "|S| = 3", fontsize=10, color="#7f8c8d", va="center")

ax.text(0, -1.0, "共 2³ = 8 个子集，按包含关系排列",
        ha="center", fontsize=11, color="#7f8c8d", style="italic")

ax.set_xlim(-4, 5.5)
ax.set_ylim(-1.5, 5.5)
ax.set_aspect("equal")
ax.axis("off")

plt.tight_layout()
save(fig, "p01-ch02-power-set.png")


print("\n全部图形生成完毕。")
