"""
图论可视化

生成 Part 7 Chapter 4 所需的两张图：
  1. 常见图类型 (p07-ch04-graph-types.png)
  2. Königsberg 七桥问题 (p07-ch04-konigsberg-bridges.png)
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import numpy as np
import networkx as nx

_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

ABS_OUT = "/workspace/basicmath/images/code-generated"
os.makedirs(ABS_OUT, exist_ok=True)
DPI = 200

NODE_COLOR = "#3498db"
EDGE_COLOR = "#7f8c8d"
FONT_COLOR = "white"


def plot_graph_types():
    """常见图类型：K5, K_{3,3}, C6, P5, 树, 二部图"""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle("常见图类型", fontsize=16, fontweight="bold", y=0.98)

    # K5
    ax = axes[0, 0]
    ax.set_title("$K_5$（完全图）", fontsize=12, fontweight="bold")
    G = nx.complete_graph(5)
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos, ax=ax, node_color=NODE_COLOR, edge_color=EDGE_COLOR,
                     node_size=500, font_color=FONT_COLOR, font_weight="bold",
                     width=1.5)
    ax.text(0, -1.35, f"$V=5, E={G.number_of_edges()}$", fontsize=10,
            ha="center", color="#2c3e50")
    ax.axis("off")

    # K_{3,3}
    ax = axes[0, 1]
    ax.set_title("$K_{3,3}$（完全二部图）", fontsize=12, fontweight="bold")
    G = nx.complete_bipartite_graph(3, 3)
    pos = nx.bipartite_layout(G, nodes=range(3))
    colors = ["#e74c3c"] * 3 + ["#3498db"] * 3
    nx.draw_networkx(G, pos, ax=ax, node_color=colors, edge_color=EDGE_COLOR,
                     node_size=500, font_color=FONT_COLOR, font_weight="bold",
                     width=1.5)
    ax.text(0.5, -0.15, f"$V=6, E={G.number_of_edges()}$", fontsize=10,
            ha="center", color="#2c3e50")
    ax.axis("off")

    # C6
    ax = axes[0, 2]
    ax.set_title("$C_6$（环）", fontsize=12, fontweight="bold")
    G = nx.cycle_graph(6)
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos, ax=ax, node_color="#2ecc71", edge_color=EDGE_COLOR,
                     node_size=500, font_color=FONT_COLOR, font_weight="bold",
                     width=2)
    ax.text(0, -1.35, f"$V=6, E={G.number_of_edges()}$, 每顶点度=2",
            fontsize=10, ha="center", color="#2c3e50")
    ax.axis("off")

    # P5
    ax = axes[1, 0]
    ax.set_title("$P_5$（路径）", fontsize=12, fontweight="bold")
    G = nx.path_graph(5)
    pos = {i: (i, 0) for i in range(5)}
    nx.draw_networkx(G, pos, ax=ax, node_color="#9b59b6", edge_color=EDGE_COLOR,
                     node_size=500, font_color=FONT_COLOR, font_weight="bold",
                     width=2)
    ax.set_ylim(-0.6, 0.6)
    ax.text(2, -0.45, f"$V=5, E={G.number_of_edges()}$", fontsize=10,
            ha="center", color="#2c3e50")
    ax.axis("off")

    # Tree
    ax = axes[1, 1]
    ax.set_title("树（Tree）", fontsize=12, fontweight="bold")
    G = nx.Graph()
    G.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (3, 6)])
    pos = {0: (2, 2), 1: (1, 1), 2: (2, 1), 3: (3, 1),
           4: (0.5, 0), 5: (1.5, 0), 6: (3, 0)}
    nx.draw_networkx(G, pos, ax=ax, node_color="#f39c12", edge_color=EDGE_COLOR,
                     node_size=500, font_color=FONT_COLOR, font_weight="bold",
                     width=2)
    ax.text(2, -0.5, f"$V=7, E=6=V-1$, 连通无环",
            fontsize=10, ha="center", color="#2c3e50")
    ax.axis("off")

    # Petersen graph
    ax = axes[1, 2]
    ax.set_title("Petersen 图", fontsize=12, fontweight="bold")
    G = nx.petersen_graph()
    pos = nx.shell_layout(G, nlist=[range(5), range(5, 10)])
    nx.draw_networkx(G, pos, ax=ax, node_color="#e74c3c", edge_color=EDGE_COLOR,
                     node_size=400, font_color=FONT_COLOR, font_weight="bold",
                     font_size=8, width=1.5)
    ax.text(0, -1.4, f"$V=10, E=15$, 3-正则, 非平面",
            fontsize=10, ha="center", color="#2c3e50")
    ax.axis("off")

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    path = os.path.join(ABS_OUT, "p07-ch04-graph-types.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  ✓ {path}")


def plot_konigsberg_bridges():
    """Königsberg 七桥问题"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left panel: schematic map
    ax = axes[0]
    ax.set_title("Königsberg 七桥示意图", fontsize=13, fontweight="bold", pad=10)
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.5, 5.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Draw land masses
    land_colors = ["#a8d8ea", "#aa96da", "#fcbad3", "#ffffd2"]
    land_positions = [(3, 4.2, "北岸 (A)"), (3, 0.8, "南岸 (B)"),
                       (1.2, 2.5, "西岛 (C)"), (4.8, 2.5, "东岛 (D)")]
    for i, (lx, ly, label) in enumerate(land_positions):
        ellipse = mpatches.Ellipse((lx, ly), 2.2, 1.2, fc=land_colors[i],
                                    ec="#2c3e50", lw=2, alpha=0.7)
        ax.add_patch(ellipse)
        ax.text(lx, ly, label, fontsize=10, ha="center", va="center",
                fontweight="bold", color="#2c3e50")

    # Draw bridges
    bridges = [
        ((1.2, 3.1), (3, 3.6), "1"),   # C-A
        ((1.2, 1.9), (3, 1.4), "2"),   # C-B
        ((1.8, 2.5), (2.4, 3.8), "3"), # C-A (second)
        ((1.8, 2.5), (2.4, 1.2), "4"), # C-B (second)
        ((4.8, 3.1), (3, 3.6), "5"),   # D-A
        ((4.8, 1.9), (3, 1.4), "6"),   # D-B
        ((3.6, 2.5), (4.2, 2.5), "7"), # between islands
    ]
    for (x1, y1), (x2, y2), label in bridges:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                     arrowprops=dict(arrowstyle="-", color="#e74c3c",
                                    lw=3, connectionstyle="arc3,rad=0.1"))
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mx, my, label, fontsize=8, ha="center", va="center",
                color="white", fontweight="bold",
                bbox=dict(boxstyle="circle,pad=0.15", fc="#e74c3c", ec="none"))

    ax.text(3, -0.2, "能否走遍所有 7 座桥恰好一次？", fontsize=11,
            ha="center", color="#c0392b", style="italic")

    # Right panel: graph abstraction
    ax = axes[1]
    ax.set_title("图论抽象", fontsize=13, fontweight="bold", pad=10)

    G = nx.MultiGraph()
    G.add_nodes_from(["A", "B", "C", "D"])
    G.add_edges_from([("A", "C"), ("A", "C"), ("A", "D"),
                       ("B", "C"), ("B", "C"), ("B", "D"),
                       ("C", "D")])

    pos = {"A": (1, 2), "B": (1, 0), "C": (0, 1), "D": (2, 1)}
    node_colors = ["#a8d8ea", "#fcbad3", "#aa96da", "#ffffd2"]

    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=node_colors,
                           node_size=1200, edgecolors="#2c3e50", linewidths=2)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=14, font_weight="bold",
                            font_color="#2c3e50")

    edge_styles = [("A", "C", 0.2), ("A", "C", -0.2), ("A", "D", 0),
                   ("B", "C", 0.2), ("B", "C", -0.2), ("B", "D", 0),
                   ("C", "D", 0)]
    for u, v, rad in edge_styles:
        ax.annotate("", xy=pos[v], xytext=pos[u],
                     arrowprops=dict(arrowstyle="-", color="#e74c3c", lw=2.5,
                                    connectionstyle=f"arc3,rad={rad}"))

    deg_text = "度数: A=3, B=3, C=5, D=3\n所有度数均为奇数\n奇度顶点 = 4 > 2"
    ax.text(1, -0.8, deg_text, fontsize=10, ha="center", va="center",
            color="#2c3e50",
            bbox=dict(boxstyle="round,pad=0.4", fc="#f9e79f", ec="#f39c12"))

    conclusion = "结论：不存在 Euler 路径\n（需要 0 或 2 个奇度顶点）"
    ax.text(1, -1.6, conclusion, fontsize=11, ha="center", va="center",
            color="#c0392b", fontweight="bold")

    ax.set_xlim(-0.8, 2.8)
    ax.set_ylim(-2.1, 2.5)
    ax.axis("off")

    plt.tight_layout()
    path = os.path.join(ABS_OUT, "p07-ch04-konigsberg-bridges.png")
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  ✓ {path}")


if __name__ == "__main__":
    print("生成 Part 7 Ch04 图片...")
    plot_graph_types()
    plot_konigsberg_bridges()
    print("完成！")
