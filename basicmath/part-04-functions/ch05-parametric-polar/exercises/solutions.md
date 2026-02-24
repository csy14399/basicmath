# 第 5 章 参数方程与极坐标 — 练习题解答

## §1 参数方程

**1.** 从 $(-1, 2)$ 到 $(3, -6)$：

$$x = -1 + 4t, \quad y = 2 - 8t, \quad t \in [0, 1]$$

验证：$t=0 \to (-1, 2)$ ✓；$t=1 \to (3, -6)$ ✓。

---

**2.** 消参。

(a) $t = \frac{x+1}{3}$，$y = 2\cdot\frac{x+1}{3} + 5 = \frac{2x+2}{3} + 5 = \frac{2x + 17}{3}$。即 $y = \frac{2}{3}x + \frac{17}{3}$（直线）。

(b) $t = x^{1/2}$（$x \geq 0$），$y = (x^{1/2})^3 = x^{3/2}$。即 $y = x^{3/2}$（$x \geq 0$）。

(c) $t = \ln x$（$x > 0$），$y = e^{2t} = (e^t)^2 = x^2$。即 $y = x^2$（$x > 0$）。

---

**3.** $\cos t = x/4$，$\sin t = y/3$。$\cos^2 t + \sin^2 t = 1$：

$$\frac{x^2}{16} + \frac{y^2}{9} = 1$$

这是长半轴 $a = 4$（沿 $x$ 轴）、短半轴 $b = 3$（沿 $y$ 轴）的椭圆。

---

**4.** $x - 1 = 2\cos t$，$y + 3 = 2\sin t$。$(x-1)^2 + (y+3)^2 = 4$。

圆心 $(1, -3)$，半径 $2$ 的圆。

---

**5.** $\sec^2 t - \tan^2 t = 1$，即 $x^2 - y^2 = 1$。

这是双曲线（$t \in (-\pi/2, \pi/2)$ 时 $x = \sec t > 0$，所以只有右支 $x > 0$）。

---

**6.** 摆线坐标。

(a) $t = 0$：$x = 0, y = 0$。即 $(0, 0)$。

(b) $t = \pi/2$：$x = 3(\frac{\pi}{2} - 1) = \frac{3\pi}{2} - 3 \approx 1.71$，$y = 3(1 - 0) = 3$。

(c) $t = \pi$：$x = 3\pi, y = 6$（拱形最高点）。

(d) $t = 2\pi$：$x = 6\pi, y = 0$（回到底部）。

---

**7.** 两者消参后都得到 $y = x^2$。

区别：(A) 的范围是 $x \in \mathbb{R}$，覆盖整条抛物线。(B) 中 $x = \sin t \in [-1, 1]$，所以只覆盖 $x \in [-1, 1]$ 的部分。此外，(A) 中 $x$ 单调递增，(B) 中点在 $[-1, 1]$ 间来回振荡。

---

**8.** 频率比为 $3:2$。因为 $3/2$ 是有理数，当 $t$ 增加 $2\pi$ 时，$\sin(3t)$ 完成 3 个周期，$\sin(2t)$ 完成 2 个周期，曲线回到起点。所以曲线闭合。

---

**9.** 星形线的消参。

$\cos t = (x/a)^{1/3}$，$\sin t = (y/a)^{1/3}$。

$\cos^2 t + \sin^2 t = 1$：

$$(x/a)^{2/3} + (y/a)^{2/3} = 1 \implies x^{2/3} + y^{2/3} = a^{2/3}$$

$\blacksquare$

---

## §2 极坐标

**10.** 极坐标 → 直角坐标。

(a) $x = 2\cos\frac{\pi}{6} = 2\cdot\frac{\sqrt{3}}{2} = \sqrt{3}$，$y = 2\sin\frac{\pi}{6} = 1$。即 $(\sqrt{3}, 1)$。

(b) $x = 5\cos\frac{3\pi}{4} = -\frac{5\sqrt{2}}{2}$，$y = 5\sin\frac{3\pi}{4} = \frac{5\sqrt{2}}{2}$。

(c) $x = \cos\pi = -1$，$y = \sin\pi = 0$。即 $(-1, 0)$。

(d) $x = 3\cos(-\frac{\pi}{3}) = \frac{3}{2}$，$y = 3\sin(-\frac{\pi}{3}) = -\frac{3\sqrt{3}}{2}$。

---

**11.** 直角坐标 → 极坐标。

(a) $r = \sqrt{2}$，$\theta = \arctan\frac{1}{1} = \frac{\pi}{4}$。即 $(\sqrt{2}, \frac{\pi}{4})$。

(b) $r = 3$，$\theta = \pi$（点在负 $x$ 轴上）。即 $(3, \pi)$。

(c) $r = 4$，$\theta = \frac{3\pi}{2}$（点在负 $y$ 轴上）。即 $(4, \frac{3\pi}{2})$。

(d) $r = \sqrt{1+3} = 2$。$x < 0, y > 0$（第二象限），$\theta = \pi - \arctan\sqrt{3} = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$。即 $(2, \frac{2\pi}{3})$。

---

**12.** 极坐标 → 直角坐标。

(a) $r = 5 \Rightarrow x^2 + y^2 = 25$。圆心原点、半径 $5$ 的圆。

(b) $\theta = \frac{\pi}{3} \Rightarrow y/x = \tan\frac{\pi}{3} = \sqrt{3} \Rightarrow y = \sqrt{3}\,x$（$x > 0$）。过原点的射线。

(c) $r = 4\cos\theta$，$r^2 = 4r\cos\theta$，$x^2+y^2 = 4x$，$(x-2)^2 + y^2 = 4$。圆心 $(2, 0)$、半径 $2$ 的圆。

(d) $r = \frac{3}{1-\sin\theta}$，$r(1-\sin\theta) = 3$，$r - r\sin\theta = 3$，$\sqrt{x^2+y^2} - y = 3$，$\sqrt{x^2+y^2} = y+3$。

两边平方（要求 $y + 3 \geq 0$）：$x^2+y^2 = y^2+6y+9$，$x^2 = 6y+9 = 6(y+\frac{3}{2})$。

这是顶点在 $(0, -\frac{3}{2})$、开口向上的抛物线。

---

**13.** 直角坐标 → 极坐标。

(a) $r^2 = 16$，$r = 4$。

(b) $r\cos\theta = 3$，$r = \frac{3}{\cos\theta} = 3\sec\theta$。

(c) $r\sin\theta = r\cos\theta$，$\theta = \frac{\pi}{4}$。

(d) $r^2 + 4r\sin\theta = 0$，$r + 4\sin\theta = 0$，$r = -4\sin\theta$。

---

**14.** 对称性分析。

(a) $r = 2 + 2\cos\theta$：$f(-\theta) = 2 + 2\cos(-\theta) = 2+2\cos\theta$ ✓。关于极轴对称。

(b) $r = \sin 2\theta$：
- $f(-\theta) = \sin(-2\theta) = -\sin 2\theta \neq f(\theta)$。不关于极轴对称。
- $f(\pi-\theta) = \sin(2\pi-2\theta) = -\sin 2\theta \neq f(\theta)$。不关于 $y$ 轴对称。
- $f(\theta+\pi) = \sin(2\theta+2\pi) = \sin 2\theta = f(\theta)$ ✓。关于原点对称。

(c) $r = 3 + \sin\theta$：
- $f(\pi - \theta) = 3 + \sin(\pi-\theta) = 3 + \sin\theta = f(\theta)$ ✓。关于 $y$ 轴对称。

---

**15.** 心形线 $r = 1 + \cos\theta$ 上的点。

$\theta = 0$：$r = 2$，$(x,y) = (2, 0)$。

$\theta = \pi/4$：$r = 1 + \frac{\sqrt{2}}{2}$，$x = r\cos\frac{\pi}{4} = (1+\frac{\sqrt{2}}{2})\frac{\sqrt{2}}{2} = \frac{\sqrt{2}}{2} + \frac{1}{2}$，$y = r\sin\frac{\pi}{4} = \frac{\sqrt{2}}{2} + \frac{1}{2}$。

$\theta = \pi/2$：$r = 1$，$(x,y) = (0, 1)$。

$\theta = \pi$：$r = 0$，$(x,y) = (0, 0)$。

---

**16.** $r = \cos 4\theta$：$n = 4$（偶数），有 $2 \times 4 = 8$ 瓣。

瓣尖端：$r = 1$ 时 $\cos 4\theta = 1$，$4\theta = 2k\pi$，$\theta = \frac{k\pi}{2}$（$k = 0, 1, 2, 3$）。

但还有 $r = -1$ 时（负极径 $\cos 4\theta = -1$），$4\theta = (2k+1)\pi$，$\theta = \frac{(2k+1)\pi}{4}$。

所以所有 $8$ 个瓣尖端对应 $\theta = 0, \frac{\pi}{4}, \frac{\pi}{2}, \frac{3\pi}{4}, \pi, \frac{5\pi}{4}, \frac{3\pi}{2}, \frac{7\pi}{4}$。

---

**17.** 双纽线 $r^2 = 4\cos 2\theta$。

(a) 要求 $\cos 2\theta \geq 0$，即 $2\theta \in [-\frac{\pi}{2}+2k\pi, \frac{\pi}{2}+2k\pi]$，即 $\theta \in [-\frac{\pi}{4}, \frac{\pi}{4}] \cup [\frac{3\pi}{4}, \frac{5\pi}{4}]$（取主值区间）。

(b) $r^2 = 4\cos 2\theta = 4(\cos^2\theta - \sin^2\theta) = 4\frac{x^2-y^2}{r^2}$。$r^4 = 4(x^2-y^2)$，$(x^2+y^2)^2 = 4(x^2-y^2)$。

(c) 对称性：
- $f(-\theta)$：$\cos(-2\theta) = \cos 2\theta$ ✓。关于极轴对称。
- $f(\pi-\theta)$：$\cos(2\pi-2\theta) = \cos 2\theta$ ✓。关于 $y$ 轴对称。
- $f(\theta+\pi)$：$\cos(2\theta+2\pi) = \cos 2\theta$ ✓。关于原点对称。

三种对称性全有。

---

**18.** $r = \frac{ed}{1 + e\cos\theta}$。$r + er\cos\theta = ed$，$r = ed - ex$。

$r^2 = (ed-ex)^2$，$x^2+y^2 = e^2(d-x)^2 = e^2d^2 - 2e^2dx + e^2x^2$。

$(1-e^2)x^2 + 2e^2dx + y^2 = e^2d^2$。

- $e < 1$：$1-e^2 > 0$，$x^2$ 和 $y^2$ 项系数同号正 → 椭圆。
- $e = 1$：$x^2$ 项消失，剩下 $2dx + y^2 = d^2$，即 $y^2 = d^2 - 2dx = -2d(x-d/2)$ → 抛物线。
- $e > 1$：$1-e^2 < 0$，$x^2$ 和 $y^2$ 项系数异号 → 双曲线（只有一支，因为 $r > 0$）。

$\blacksquare$

---

**19.** $\theta = 0$ 时：$r = e^0 = 1$，$(x, y) = (1, 0)$。

$\theta = 2\pi$ 时：$r = e^{2\pi/5}$，$(x, y) = (e^{2\pi/5}\cos 2\pi, e^{2\pi/5}\sin 2\pi) = (e^{2\pi/5}, 0)$。

距离 $= |e^{2\pi/5} - 1| = e^{2\pi/5} - 1 \approx 3.513 - 1 = 2.513$。

（注意：这是两点之间的**直线距离**，不是沿螺旋的弧长。）
