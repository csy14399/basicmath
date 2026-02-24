"""
欧氏几何可视化

生成 Part 5 Chapter 1 所需的五张图：
  1. 三角形五心 (p05-ch01-triangle-centers.png)
  2. 全等条件 (p05-ch01-congruence-conditions.png)
  3. 圆内接角 (p05-ch01-inscribed-angle.png)
  4. 圆幂定理 (p05-ch01-power-of-a-point.png)
  5. 正多面体 2D 投影 (p05-ch01-platonic-solids.png)
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


def _circle(ax, cx, cy, r, **kwargs):
    theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(cx + r * np.cos(theta), cy + r * np.sin(theta), **kwargs)


def plot_triangle_centers():
    A = np.array([0, 0])
    B = np.array([6, 0])
    C = np.array([2, 5])

    fig, ax = plt.subplots(figsize=(8, 7))
    ax.set_title("三角形的五心", fontsize=14, fontweight="bold")

    tri_x = [A[0], B[0], C[0], A[0]]
    tri_y = [A[1], B[1], C[1], A[1]]
    ax.plot(tri_x, tri_y, "k-", lw=2)

    G = (A + B + C) / 3
    ax.plot(*G, "o", color="#e74c3c", ms=8, zorder=5)
    ax.annotate("重心 G", G + np.array([0.15, 0.15]), fontsize=10, color="#e74c3c")

    ab = B - A
    ac = C - A
    D = np.array([
        [2 * ab[0], 2 * ab[1]],
        [2 * ac[0], 2 * ac[1]]
    ])
    rhs = np.array([ab @ ab, ac @ ac])
    uv = np.linalg.solve(D, rhs)
    O = A + uv
    R = np.linalg.norm(O - A)
    _circle(ax, O[0], O[1], R, color="#3498db", lw=1.2, ls="--", alpha=0.6)
    ax.plot(*O, "o", color="#3498db", ms=8, zorder=5)
    ax.annotate("外心 O", O + np.array([-0.8, 0.2]), fontsize=10, color="#3498db")

    a_len = np.linalg.norm(B - C)
    b_len = np.linalg.norm(A - C)
    c_len = np.linalg.norm(A - B)
    I = (a_len * A + b_len * B + c_len * C) / (a_len + b_len + c_len)
    s = (a_len + b_len + c_len) / 2
    r_in = np.sqrt((s - a_len) * (s - b_len) * (s - c_len) / s)
    _circle(ax, I[0], I[1], r_in, color="#27ae60", lw=1.2, ls="--", alpha=0.6)
    ax.plot(*I, "o", color="#27ae60", ms=8, zorder=5)
    ax.annotate("内心 I", I + np.array([0.15, -0.5]), fontsize=10, color="#27ae60")

    H = A + B + C - 2 * O
    ax.plot(*H, "o", color="#8e44ad", ms=8, zorder=5)
    ax.annotate("垂心 H", H + np.array([0.15, 0.15]), fontsize=10, color="#8e44ad")

    N = (O + H) / 2
    ax.plot(*N, "s", color="#f39c12", ms=7, zorder=5)
    ax.annotate("九点圆心 N", N + np.array([0.15, -0.45]), fontsize=10, color="#f39c12")

    euler_pts = np.array([O, G, N, H])
    ax.plot(euler_pts[:, 0], euler_pts[:, 1], "--", color="#95a5a6", lw=1.5, alpha=0.7)
    ax.annotate("Euler 线", (euler_pts[0] + euler_pts[-1]) / 2 + np.array([0.2, 0.3]),
                fontsize=9, color="#95a5a6", style="italic")

    for pt, name in [(A, "A"), (B, "B"), (C, "C")]:
        ax.annotate(name, pt + np.array([-0.3, -0.35]), fontsize=11, fontweight="bold")

    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.set_xlim(-1.5, 8)
    ax.set_ylim(-1.5, 6.5)
    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch01-triangle-centers.png"), dpi=DPI)
    plt.close(fig)


def plot_congruence_conditions():
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    fig.suptitle("三角形全等条件", fontsize=14, fontweight="bold")

    conditions = [
        ("SSS", [(0, 0), (3, 0), (1.5, 2.5)], [(4, 0), (7, 0), (5.5, 2.5)],
         {"sides": True}),
        ("SAS", [(0, 0), (3, 0), (1, 2.5)], [(4, 0), (7, 0), (5, 2.5)],
         {"sides_partial": [0, 1], "angle": 0}),
        ("ASA", [(0, 0), (3, 0), (1, 2)], [(4, 0), (7, 0), (5, 2)],
         {"angles": [0, 1]}),
        ("AAS", [(0, 0), (3, 0), (1, 2)], [(4, 0), (7, 0), (5, 2)],
         {"angles": [0, 2]}),
    ]

    colors = ["#2980b9", "#e74c3c"]
    for ax, (name, tri1, tri2, _) in zip(axes, conditions):
        ax.set_title(name, fontsize=13, fontweight="bold")
        for tri, c in [(tri1, colors[0]), (tri2, colors[1])]:
            xs = [p[0] for p in tri] + [tri[0][0]]
            ys = [p[1] for p in tri] + [tri[0][1]]
            ax.fill(xs, ys, alpha=0.15, color=c)
            ax.plot(xs, ys, "-", color=c, lw=2)
        ax.set_aspect("equal")
        ax.set_xlim(-0.5, 8)
        ax.set_ylim(-0.5, 3.5)
        ax.axis("off")

    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch01-congruence-conditions.png"), dpi=DPI)
    plt.close(fig)


def plot_inscribed_angle():
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_title("圆周角定理：圆周角 = 圆心角 / 2", fontsize=13, fontweight="bold")

    R = 3
    _circle(ax, 0, 0, R, color="#2c3e50", lw=2)
    ax.plot(0, 0, "o", color="#2c3e50", ms=5)
    ax.annotate("O", (0.15, 0.15), fontsize=11, fontweight="bold")

    a_ang, b_ang = np.radians(200), np.radians(320)
    A = R * np.array([np.cos(a_ang), np.sin(a_ang)])
    B = R * np.array([np.cos(b_ang), np.sin(b_ang)])

    for p_ang, label, col in [(np.radians(70), "P₁", "#e74c3c"),
                               (np.radians(120), "P₂", "#2980b9")]:
        P = R * np.array([np.cos(p_ang), np.sin(p_ang)])
        ax.plot([P[0], A[0]], [P[1], A[1]], "-", color=col, lw=1.8)
        ax.plot([P[0], B[0]], [P[1], B[1]], "-", color=col, lw=1.8)
        ax.plot(*P, "o", color=col, ms=7)
        ax.annotate(label, P + np.array([0.15, 0.15]), fontsize=11, color=col)

    ax.plot([0, A[0]], [0, A[1]], "-", color="#f39c12", lw=2)
    ax.plot([0, B[0]], [0, B[1]], "-", color="#f39c12", lw=2)

    central = np.abs(b_ang - a_ang)
    arc_r = 0.6
    arc_angles = np.linspace(a_ang, b_ang, 50) if b_ang > a_ang else np.linspace(a_ang, b_ang + 2 * np.pi, 50)
    ax.plot(arc_r * np.cos(arc_angles), arc_r * np.sin(arc_angles), "-", color="#f39c12", lw=2)
    ax.annotate("2α", (0.45 * np.cos((a_ang + b_ang) / 2), 0.45 * np.sin((a_ang + b_ang) / 2)),
                fontsize=11, color="#f39c12", fontweight="bold")

    for pt, name in [(A, "A"), (B, "B")]:
        ax.plot(*pt, "o", color="#2c3e50", ms=7)
        off = pt / np.linalg.norm(pt) * 0.35
        ax.annotate(name, pt + off, fontsize=11, fontweight="bold")

    ax.annotate("圆周角 α 不依赖 P 的位置", xy=(0, -R - 0.8), fontsize=10,
                ha="center", style="italic",
                bbox=dict(boxstyle="round,pad=0.3", fc="#fef9e7", alpha=0.9))

    ax.set_aspect("equal")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4.5, 4)
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch01-inscribed-angle.png"), dpi=DPI)
    plt.close(fig)


def plot_power_of_point():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("圆幂定理", fontsize=14, fontweight="bold")

    R = 2.5
    for idx, (ax, case) in enumerate(zip(axes, ["inside", "outside"])):
        _circle(ax, 0, 0, R, color="#2c3e50", lw=2)
        ax.plot(0, 0, "o", color="#2c3e50", ms=4)

        if case == "inside":
            ax.set_title("点在圆内：PA·PB = PC·PD", fontsize=11)
            P = np.array([0.5, 0.3])
            angles_1 = [np.radians(30), np.radians(210)]
            angles_2 = [np.radians(100), np.radians(300)]
        else:
            ax.set_title("点在圆外：PA·PB = PC·PD", fontsize=11)
            P = np.array([4.0, 0.0])
            angles_1 = [np.radians(25), np.radians(-25)]
            angles_2 = [np.radians(50), np.radians(-50)]

        for angs, col, labels in [(angles_1, "#e74c3c", ["A", "B"]),
                                   (angles_2, "#2980b9", ["C", "D"])]:
            pts = [R * np.array([np.cos(a), np.sin(a)]) for a in angs]
            ax.plot([pts[0][0], pts[1][0]], [pts[0][1], pts[1][1]],
                    "-", color=col, lw=2, alpha=0.8)
            if case == "outside":
                ax.plot([P[0], pts[0][0]], [P[1], pts[0][1]], "-", color=col, lw=2, alpha=0.8)
                ax.plot([P[0], pts[1][0]], [P[1], pts[1][1]], "-", color=col, lw=2, alpha=0.8)
            for pt, lb in zip(pts, labels):
                ax.plot(*pt, "o", color=col, ms=6)
                off = pt / np.linalg.norm(pt) * 0.35
                ax.annotate(lb, pt + off, fontsize=10, color=col, fontweight="bold")

        ax.plot(*P, "o", color="#2c3e50", ms=7, zorder=5)
        ax.annotate("P", P + np.array([0.15, 0.15]), fontsize=11, fontweight="bold")
        ax.set_aspect("equal")
        ax.grid(True, alpha=0.2)
        ax.set_xlim(-3.5, 5.5 if case == "outside" else 3.5)
        ax.set_ylim(-3.5, 3.5)

    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch01-power-of-a-point.png"), dpi=DPI)
    plt.close(fig)


def plot_platonic_solids():
    fig, axes = plt.subplots(1, 5, figsize=(20, 4))
    fig.suptitle("五种正多面体（2D 投影）", fontsize=14, fontweight="bold")

    solids = [
        ("正四面体\nTetrahedron", 3, [(0, 0), (2, 0), (1, np.sqrt(3)),
         (1, np.sqrt(3) / 3)]),
        ("正六面体\nCube", 4, None),
        ("正八面体\nOctahedron", 3, None),
        ("正十二面体\nDodecahedron", 5, None),
        ("正二十面体\nIcosahedron", 3, None),
    ]

    def draw_regular_polygon(ax, n, R=1.2, cx=0, cy=0, rot=np.pi / 2):
        angles = [rot + 2 * np.pi * k / n for k in range(n)]
        pts = [(cx + R * np.cos(a), cy + R * np.sin(a)) for a in angles]
        xs = [p[0] for p in pts] + [pts[0][0]]
        ys = [p[1] for p in pts] + [pts[0][1]]
        return pts, xs, ys

    colors = ["#e74c3c", "#3498db", "#27ae60", "#f39c12", "#8e44ad"]

    ax = axes[0]
    ax.set_title("正四面体\n(4面, 4顶点, 6棱)", fontsize=10)
    pts = [(0, -0.3), (2, -0.3), (1, np.sqrt(3) - 0.3)]
    center = (1, np.sqrt(3) / 3 - 0.1)
    for i in range(3):
        for j in range(i + 1, 3):
            ax.plot([pts[i][0], pts[j][0]], [pts[i][1], pts[j][1]], "-", color=colors[0], lw=2)
        ax.plot([pts[i][0], center[0]], [pts[i][1], center[1]], "--", color=colors[0], lw=1.5, alpha=0.6)
    for p in pts:
        ax.plot(*p, "o", color=colors[0], ms=6)
    ax.plot(*center, "o", color=colors[0], ms=6)

    ax = axes[1]
    ax.set_title("正六面体（立方体）\n(6面, 8顶点, 12棱)", fontsize=10)
    front = [(-0.8, -0.8), (0.8, -0.8), (0.8, 0.8), (-0.8, 0.8)]
    off = (0.5, 0.5)
    back = [(p[0] + off[0], p[1] + off[1]) for p in front]
    for sq, ls in [(front, "-"), (back, "--")]:
        xs = [p[0] for p in sq] + [sq[0][0]]
        ys = [p[1] for p in sq] + [sq[0][1]]
        ax.plot(xs, ys, ls, color=colors[1], lw=2)
    for f, b in zip(front, back):
        ax.plot([f[0], b[0]], [f[1], b[1]], "-", color=colors[1], lw=1.5, alpha=0.6)

    ax = axes[2]
    ax.set_title("正八面体\n(8面, 6顶点, 12棱)", fontsize=10)
    top = (0, 1.5)
    bottom = (0, -1.5)
    mid = [(1.2, 0), (0, 0.6), (-1.2, 0), (0, -0.6)]
    for p in mid:
        ax.plot([top[0], p[0]], [top[1], p[1]], "-", color=colors[2], lw=2)
        ax.plot([bottom[0], p[0]], [bottom[1], p[1]], "-", color=colors[2], lw=2)
    for i in range(4):
        ax.plot([mid[i][0], mid[(i + 1) % 4][0]], [mid[i][1], mid[(i + 1) % 4][1]],
                "-", color=colors[2], lw=2)
    for p in [top, bottom] + mid:
        ax.plot(*p, "o", color=colors[2], ms=5)

    ax = axes[3]
    ax.set_title("正十二面体\n(12面, 20顶点, 30棱)", fontsize=10)
    pts_outer, xs, ys = draw_regular_polygon(ax, 10, R=1.4, rot=np.pi / 2)
    ax.plot(xs, ys, "-", color=colors[3], lw=2)
    pts_inner, xs2, ys2 = draw_regular_polygon(ax, 10, R=0.7, rot=np.pi / 2 + np.pi / 10)
    ax.plot(xs2, ys2, "--", color=colors[3], lw=1.5, alpha=0.7)
    for po, pi_ in zip(pts_outer, pts_inner):
        ax.plot([po[0], pi_[0]], [po[1], pi_[1]], "-", color=colors[3], lw=1, alpha=0.5)

    ax = axes[4]
    ax.set_title("正二十面体\n(20面, 12顶点, 30棱)", fontsize=10)
    pts_outer, xs, ys = draw_regular_polygon(ax, 6, R=1.4, rot=np.pi / 2)
    ax.plot(xs, ys, "-", color=colors[4], lw=2)
    pts_inner, xs2, ys2 = draw_regular_polygon(ax, 6, R=0.7, rot=np.pi / 2 + np.pi / 6)
    ax.plot(xs2, ys2, "--", color=colors[4], lw=1.5, alpha=0.7)
    for po, pi_ in zip(pts_outer, pts_inner):
        ax.plot([po[0], pi_[0]], [po[1], pi_[1]], "-", color=colors[4], lw=1.5, alpha=0.6)
    top = (0, 1.7)
    bottom = (0, -1.7)
    for p in pts_outer[:3]:
        ax.plot([top[0], p[0]], [top[1], p[1]], "-", color=colors[4], lw=1, alpha=0.5)
    for p in pts_outer[3:]:
        ax.plot([bottom[0], p[0]], [bottom[1], p[1]], "-", color=colors[4], lw=1, alpha=0.5)
    ax.plot(*top, "o", color=colors[4], ms=5)
    ax.plot(*bottom, "o", color=colors[4], ms=5)

    for ax in axes:
        ax.set_aspect("equal")
        ax.axis("off")

    fig.tight_layout()
    fig.savefig(os.path.join(ABS_OUT, "p05-ch01-platonic-solids.png"), dpi=DPI)
    plt.close(fig)


if __name__ == "__main__":
    print("Generating ch01 images...")
    plot_triangle_centers()
    print("  ✓ triangle-centers")
    plot_congruence_conditions()
    print("  ✓ congruence-conditions")
    plot_inscribed_angle()
    print("  ✓ inscribed-angle")
    plot_power_of_point()
    print("  ✓ power-of-a-point")
    plot_platonic_solids()
    print("  ✓ platonic-solids")
    print("All ch01 images generated.")
