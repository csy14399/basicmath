# 第 3 章 三角函数 — 挑战题（Challenge Problems）

以下挑战题综合运用三角函数和三角恒等式的知识，难度超出常规练习。

---

## 挑战题 1：连乘积

证明对所有正整数 $n$：

$$\prod_{k=1}^{n-1} \sin\frac{k\pi}{n} = \frac{n}{2^{n-1}}$$

### 提示

利用 $n$ 次单位根：$z^n - 1 = \prod_{k=0}^{n-1}(z - e^{2\pi i k/n})$。令 $z = 1$ 后适当处理。

### 解答

考虑多项式 $z^n - 1 = (z-1)(z^{n-1} + z^{n-2} + \cdots + 1)$。

$n$ 次单位根 $\omega_k = e^{2\pi i k/n}$（$k = 0, 1, \ldots, n-1$），$z^n - 1 = \prod_{k=0}^{n-1}(z - \omega_k)$。

因此 $\frac{z^n-1}{z-1} = \prod_{k=1}^{n-1}(z-\omega_k)$。

令 $z = 1$：$\lim_{z \to 1}\frac{z^n-1}{z-1} = n$（由 $z^n - 1 = (z-1)(z^{n-1}+\cdots+1)$，代入 $z=1$ 得 $n$）。

$$n = \prod_{k=1}^{n-1}(1 - \omega_k) = \prod_{k=1}^{n-1}\left(1 - e^{2\pi i k/n}\right)$$

取模：$|1 - e^{i\theta}| = 2\left|\sin\frac{\theta}{2}\right|$。

$$n = \left|\prod_{k=1}^{n-1}(1 - e^{2\pi i k/n})\right| = \prod_{k=1}^{n-1} 2\left|\sin\frac{k\pi}{n}\right| = 2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}$$

（最后一步利用了 $\sin\frac{k\pi}{n} > 0$（$1 \leq k \leq n-1$）。）

因此 $\prod_{k=1}^{n-1}\sin\frac{k\pi}{n} = \frac{n}{2^{n-1}}$。$\blacksquare$

**验证**（$n=3$）：$\sin\frac{\pi}{3}\sin\frac{2\pi}{3} = \frac{\sqrt{3}}{2}\cdot\frac{\sqrt{3}}{2} = \frac{3}{4} = \frac{3}{2^2}$。✓

---

## 挑战题 2：Morrie 定律

证明：

$$\cos 20° \cos 40° \cos 80° = \frac{1}{8}$$

### 解答

设 $P = \cos 20°\cos 40°\cos 80°$。

乘以 $\sin 20°$：

$$P \sin 20° = \sin 20°\cos 20°\cos 40°\cos 80° = \frac{1}{2}\sin 40°\cos 40°\cos 80°$$

$$= \frac{1}{4}\sin 80°\cos 80° = \frac{1}{8}\sin 160° = \frac{1}{8}\sin 20°$$

因此 $P = \frac{1}{8}$。$\blacksquare$

**推广**（Morrie 定律）：

$$\prod_{k=0}^{n-1}\cos(2^k \alpha) = \frac{\sin(2^n\alpha)}{2^n\sin\alpha}$$

---

## 挑战题 3：无穷乘积

利用 Morrie 定律的推广，证明 Euler 的无穷乘积：

$$\frac{\sin x}{x} = \prod_{k=1}^{\infty}\cos\frac{x}{2^k}$$

### 解答

由 $\sin x = 2\sin\frac{x}{2}\cos\frac{x}{2}$，迭代 $n$ 次：

$$\sin x = 2^n \sin\frac{x}{2^n}\prod_{k=1}^{n}\cos\frac{x}{2^k}$$

因此

$$\prod_{k=1}^{n}\cos\frac{x}{2^k} = \frac{\sin x}{2^n\sin\frac{x}{2^n}}$$

当 $n \to \infty$：$2^n\sin\frac{x}{2^n} \to x$（因为 $\lim_{t \to 0}\frac{\sin t}{t} = 1$）。

$$\prod_{k=1}^{\infty}\cos\frac{x}{2^k} = \frac{\sin x}{x}$$

特别地，令 $x = \frac{\pi}{2}$：

$$\frac{2}{\pi} = \cos\frac{\pi}{4}\cos\frac{\pi}{8}\cos\frac{\pi}{16}\cdots = \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{2+\sqrt{2}}}{2}\cdot\frac{\sqrt{2+\sqrt{2+\sqrt{2}}}}{2}\cdots$$

这是 Vieta 在 1593 年发现的关于 $\pi$ 的最早的无穷乘积公式。$\blacksquare$

---

## 挑战题 4：三角不等式

证明：对所有 $x \in (0, \frac{\pi}{2})$，

$$\frac{2}{\pi}x < \sin x < x$$

### 提示

右半部分可以通过单位圆的几何论证（弧长与弦长的比较）得到。左半部分用 $\sin x$ 在 $(0, \pi/2)$ 上是凸函数（concave）的事实。

### 解答

**$\sin x < x$（$x > 0$）**：在单位圆中，角 $x$（弧度）对应弧长 $x$。$\sin x$ 是从圆上对应点到 $x$ 轴的垂直距离，即弦（的一部分）。弧长 > 弦长（直线是两点间最短路径），因此 $x > \sin x$。

更严格地，可以用面积比较：对 $0 < x < \pi/2$，$\sin x = $ 单位圆内角 $x$ 对应的"竖直投影"$< x = $ 弧长。

**$\sin x > \frac{2}{\pi}x$**：$f(x) = \sin x$ 在 $[0, \pi/2]$ 上是凹函数（$f'' = -\sin x < 0$），因此图像在连接 $(0, 0)$ 和 $(\pi/2, 1)$ 的弦的上方：

$$\sin x > \frac{1-0}{\pi/2-0}(x-0) = \frac{2}{\pi}x \qquad (0 < x < \pi/2)$$

$\blacksquare$
