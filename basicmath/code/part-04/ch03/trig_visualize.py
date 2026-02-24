"""
三角函数可视化

生成 Part 4 Chapter 3 所需的五张图：
  1. 单位圆与三角函数定义
  2. 弧度与角度对照
  3. 六个三角函数的图像
  4. 三角函数图像变换 A sin(Bx+C)+D
  5. 和角公式的几何证明示意
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as patches
import numpy as np

_zh_font_path = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"
if os.path.exists(_zh_font_path):
    _zh_prop = fm.FontProperties(fname=_zh_font_path)
    plt.rcParams["font.family"] = _zh_prop.get_name()
    plt.rcParams["axes.unicode_minus"] = False

ABS_OUT = "/workspace/basicmath/images/code-generated"
os.makedirs(ABS_OUT, exist_ok=True)

DPI = 200


def plot_unit_circle_trig():
    """单位圆上的三角函数。"""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_title("单位圆与三角函数", fontsize=14, fontweight="bold", pad=10)

    theta_circle = np.linspace(0, 2*np.pi, 300)
    ax.plot(np.cos(theta_circle), np.sin(theta_circle), color="#2c3e50", lw=2)

    angle = np.pi / 3
    cx, cy = np.cos(angle), np.sin(angle)

    ax.plot([0, cx], [0, cy], color="#2980b9", lw=2.5)
    ax.plot(cx, cy, "o", color="#e74c3c", ms=8, zorder=5)

    ax.plot([cx, cx], [0, cy], "--", color="#e74c3c", lw=2, label="$\\sin\\theta$")
    ax.plot([0, cx], [0, 0], "-", color="#27ae60", lw=2, label="$\\cos\\theta$")

    ax.plot([1, 1], [0, np.tan(angle)], "--", color="#8e44ad", lw=2, label="$\\tan\\theta$")
    ax.plot([0, 1], [0, np.tan(angle)], ":", color="#8e44ad", lw=1, alpha=0.5)

    arc = patches.Arc((0, 0), 0.4, 0.4, angle=0, theta1=0, theta2=np.degrees(angle),
                       color="#e67e22", lw=2)
    ax.add_patch(arc)
    ax.annotate("$\\theta = \\pi/3$", xy=(0.25, 0.12), fontsize=11, color="#e67e22")

    ax.annotate(f"$P = (\\cos\\theta, \\sin\\theta)$", xy=(cx+0.05, cy+0.08),
                fontsize=11, color="#e74c3c")
    ax.annotate("$\\sin\\theta$", xy=(cx+0.05, cy/2), fontsize=11, color="#e74c3c")
    ax.annotate("$\\cos\\theta$", xy=(cx/2, -0.12), fontsize=11, color="#27ae60")
    ax.annotate("$\\tan\\theta$", xy=(1.08, np.tan(angle)/2), fontsize=11, color="#8e44ad")

    ax.axhline(0, color="#7f8c8d", lw=0.8)
    ax.axvline(0, color="#7f8c8d", lw=0.8)
    ax.set_xlim(-1.5, 1.8)
    ax.set_ylim(-1.5, 2.2)
    ax.set_aspect("equal")
    ax.legend(fontsize=10, loc="lower left")
    ax.grid(True, alpha=0.2)

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch03-unit-circle-trig.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


def plot_radian_degree():
    """弧度与角度对照。"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("弧度与角度", fontsize=14, fontweight="bold")

    # Left: visual circle with radian markings
    ax = axes[0]
    ax.set_title("单位圆上的常用角", fontsize=11, pad=8)
    theta_c = np.linspace(0, 2*np.pi, 300)
    ax.plot(np.cos(theta_c), np.sin(theta_c), color="#2c3e50", lw=2)

    special_angles = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2,
                      2*np.pi/3, 3*np.pi/4, 5*np.pi/6, np.pi,
                      7*np.pi/6, 5*np.pi/4, 4*np.pi/3, 3*np.pi/2,
                      5*np.pi/3, 7*np.pi/4, 11*np.pi/6]
    labels_rad = ["$0$", "$\\frac{\\pi}{6}$", "$\\frac{\\pi}{4}$", "$\\frac{\\pi}{3}$",
                  "$\\frac{\\pi}{2}$", "$\\frac{2\\pi}{3}$", "$\\frac{3\\pi}{4}$",
                  "$\\frac{5\\pi}{6}$", "$\\pi$", "$\\frac{7\\pi}{6}$",
                  "$\\frac{5\\pi}{4}$", "$\\frac{4\\pi}{3}$", "$\\frac{3\\pi}{2}$",
                  "$\\frac{5\\pi}{3}$", "$\\frac{7\\pi}{4}$", "$\\frac{11\\pi}{6}$"]

    for ang, lab in zip(special_angles, labels_rad):
        cx, cy = np.cos(ang), np.sin(ang)
        ax.plot(cx, cy, "o", color="#e74c3c", ms=4)
        ax.plot([0, cx], [0, cy], "-", color="#bdc3c7", lw=0.5, alpha=0.5)
        offset = 1.25
        ax.text(offset*cx, offset*cy, lab, fontsize=7, ha="center", va="center")

    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect("equal")

    # Right: conversion table
    ax = axes[1]
    ax.axis("off")
    ax.set_title("角度 ↔ 弧度 对照", fontsize=11, pad=8)
    table_data = [
        ["角度 (°)", "弧度 (rad)"],
        ["0°", "0"],
        ["30°", "π/6"],
        ["45°", "π/4"],
        ["60°", "π/3"],
        ["90°", "π/2"],
        ["120°", "2π/3"],
        ["135°", "3π/4"],
        ["150°", "5π/6"],
        ["180°", "π"],
        ["270°", "3π/2"],
        ["360°", "2π"],
    ]
    table = ax.table(cellText=table_data[1:], colLabels=table_data[0],
                     loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor("#3498db")
            cell.set_text_props(color="white", fontweight="bold")
        elif row % 2 == 0:
            cell.set_facecolor("#eaf2f8")

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch03-radian-degree.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


def plot_trig_graphs():
    """六个三角函数的图像。"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle("六个三角函数的图像", fontsize=15, fontweight="bold")

    x = np.linspace(-2*np.pi, 2*np.pi, 1000)
    funcs = [
        (np.sin, "$y = \\sin x$", "#2980b9", (-1.5, 1.5)),
        (np.cos, "$y = \\cos x$", "#27ae60", (-1.5, 1.5)),
        (np.tan, "$y = \\tan x$", "#e74c3c", (-6, 6)),
        (lambda x: 1/np.sin(x), "$y = \\csc x$", "#8e44ad", (-6, 6)),
        (lambda x: 1/np.cos(x), "$y = \\sec x$", "#e67e22", (-6, 6)),
        (lambda x: np.cos(x)/np.sin(x), "$y = \\cot x$", "#1abc9c", (-6, 6)),
    ]

    for ax, (func, title, color, ylim) in zip(axes.flat, funcs):
        ax.set_title(title, fontsize=12, pad=8)
        y = func(x)
        y_clipped = np.where(np.abs(y) > 20, np.nan, y)
        ax.plot(x, y_clipped, color=color, lw=2)
        ax.axhline(0, color="#7f8c8d", lw=0.6)
        ax.axvline(0, color="#7f8c8d", lw=0.6)
        ax.set_xlim(-2*np.pi, 2*np.pi)
        ax.set_ylim(*ylim)
        ax.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
        ax.set_xticklabels(["$-2\\pi$", "$-\\pi$", "$0$", "$\\pi$", "$2\\pi$"])
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch03-trig-graphs.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


def plot_trig_transformations():
    """图像变换 A sin(Bx + C) + D。"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("$y = A\\sin(Bx + C) + D$ 的各参数效果", fontsize=14, fontweight="bold")

    x = np.linspace(-2*np.pi, 4*np.pi, 1000)

    # A: amplitude
    ax = axes[0, 0]
    ax.set_title("振幅 $A$", fontsize=12, pad=8)
    for A, color in [(1, "#2980b9"), (2, "#e74c3c"), (0.5, "#27ae60")]:
        ax.plot(x, A*np.sin(x), color=color, lw=2, label=f"$A = {A}$")
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-2*np.pi, 4*np.pi)

    # B: period
    ax = axes[0, 1]
    ax.set_title("周期 $T = 2\\pi/B$", fontsize=12, pad=8)
    for B, color in [(1, "#2980b9"), (2, "#e74c3c"), (0.5, "#27ae60")]:
        ax.plot(x, np.sin(B*x), color=color, lw=2, label=f"$B = {B}$, $T = {2*np.pi/B:.2f}$")
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-2*np.pi, 4*np.pi)

    # C: phase shift
    ax = axes[1, 0]
    ax.set_title("相移 $C$（水平平移 $-C/B$）", fontsize=12, pad=8)
    for C, color, lab in [(0, "#2980b9", "$C=0$"),
                           (np.pi/2, "#e74c3c", "$C=\\pi/2$"),
                           (-np.pi/3, "#27ae60", "$C=-\\pi/3$")]:
        ax.plot(x, np.sin(x + C), color=color, lw=2, label=lab)
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-2*np.pi, 4*np.pi)

    # D: vertical shift
    ax = axes[1, 1]
    ax.set_title("垂直平移 $D$", fontsize=12, pad=8)
    for D, color in [(0, "#2980b9"), (2, "#e74c3c"), (-1, "#27ae60")]:
        ax.plot(x, np.sin(x) + D, color=color, lw=2, label=f"$D = {D}$")
    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-2*np.pi, 4*np.pi)

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch03-trig-transformations.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


def plot_angle_addition_proof():
    """和角公式的几何证明示意。"""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_title("和角公式 $\\sin(\\alpha+\\beta)$ 的几何示意", fontsize=13, fontweight="bold", pad=10)

    theta_c = np.linspace(0, 2*np.pi, 300)
    ax.plot(np.cos(theta_c), np.sin(theta_c), color="#bdc3c7", lw=1.5)

    alpha = np.pi / 6
    beta = np.pi / 4
    total = alpha + beta

    P = (np.cos(total), np.sin(total))
    Q = (np.cos(alpha), np.sin(alpha))

    ax.plot([0, 1], [0, 0], color="#7f8c8d", lw=1.5)
    ax.plot([0, Q[0]], [0, Q[1]], color="#27ae60", lw=2.5, label="角 $\\alpha$")
    ax.plot([0, P[0]], [0, P[1]], color="#2980b9", lw=2.5, label="角 $\\alpha+\\beta$")

    arc_a = patches.Arc((0, 0), 0.4, 0.4, angle=0, theta1=0, theta2=np.degrees(alpha),
                         color="#27ae60", lw=2)
    ax.add_patch(arc_a)
    ax.text(0.28, 0.06, "$\\alpha$", fontsize=12, color="#27ae60")

    arc_b = patches.Arc((0, 0), 0.5, 0.5, angle=0, theta1=np.degrees(alpha),
                         theta2=np.degrees(total), color="#e74c3c", lw=2)
    ax.add_patch(arc_b)
    ax.text(0.22, 0.25, "$\\beta$", fontsize=12, color="#e74c3c")

    ax.plot(P[0], P[1], "o", color="#2980b9", ms=8, zorder=5)
    ax.annotate("$P = (\\cos(\\alpha+\\beta), \\sin(\\alpha+\\beta))$",
                xy=P, xytext=(P[0]-0.3, P[1]+0.15), fontsize=10, color="#2980b9")

    ax.plot([P[0], P[0]], [0, P[1]], "--", color="#e74c3c", lw=1.5)
    ax.plot([0, P[0]], [0, 0], "-", color="#27ae60", lw=1)

    ax.annotate("$\\sin(\\alpha+\\beta)$", xy=(P[0]+0.05, P[1]/2),
                fontsize=10, color="#e74c3c")
    ax.annotate("$\\cos(\\alpha+\\beta)$", xy=(P[0]/2, -0.1),
                fontsize=10, color="#27ae60")

    ax.axhline(0, color="#7f8c8d", lw=0.5)
    ax.axvline(0, color="#7f8c8d", lw=0.5)
    ax.set_xlim(-0.3, 1.5)
    ax.set_ylim(-0.3, 1.3)
    ax.set_aspect("equal")
    ax.legend(fontsize=10, loc="upper right")
    ax.grid(True, alpha=0.2)

    plt.tight_layout()
    out = os.path.join(ABS_OUT, "p04-ch03-angle-addition-proof.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    plot_unit_circle_trig()
    plot_radian_degree()
    plot_trig_graphs()
    plot_trig_transformations()
    plot_angle_addition_proof()
    print("All ch03 plots generated.")
