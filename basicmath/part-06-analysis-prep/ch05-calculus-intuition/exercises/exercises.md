# 第 5 章 微积分直觉 — 练习题

## §1 导数的直觉

1. ★☆☆ 用导数定义 $f'(a) = \lim_{h\to 0}\frac{f(a+h)-f(a)}{h}$ 计算以下导数：
   (a) $f(x) = 3x + 5$，求 $f'(x)$
   (b) $f(x) = x^2 - 2x$，求 $f'(1)$
   (c) $f(x) = 1/(x+1)$，求 $f'(x)$

2. ★☆☆ 用求导法则计算以下函数的导数：
   (a) $f(x) = 5x^4 - 3x^2 + 7x - 1$
   (b) $f(x) = x^2 \cos x$
   (c) $f(x) = \dfrac{x}{x+1}$
   (d) $f(x) = e^{x^2}$

3. ★☆☆ 求曲线 $y = x^3$ 在点 $(1, 1)$ 处切线的方程。

4. ★★☆ 求 $f(x) = \sin(e^x)$ 的导数。

5. ★★☆ 设 $f(x) = x|x|$。用导数定义证明 $f'(0) = 0$。

6. ★★☆ 设 $f(x) = \begin{cases}x^2\sin(1/x) & x \neq 0 \\ 0 & x = 0\end{cases}$。证明 $f'(0) = 0$。$f'$ 在 $x = 0$ 处连续吗？

7. ★★☆ 一个自由下落的物体位置为 $s(t) = \frac{1}{2}gt^2$（$g \approx 9.8\,\text{m/s}^2$）。
   (a) 求 $t$ 时刻的速度 $v(t) = s'(t)$。
   (b) 求 $t$ 时刻的加速度 $a(t) = v'(t)$。

---

## §2 积分的直觉

1. ★☆☆ 计算以下定积分：
   (a) $\displaystyle\int_0^3 (2x + 1)\,dx$
   (b) $\displaystyle\int_0^{\pi/2}\cos x\,dx$
   (c) $\displaystyle\int_1^e \frac{2}{x}\,dx$

2. ★☆☆ 用 $n = 4$ 等距分划，计算 $\displaystyle\int_0^2 x^3\,dx$ 的左 Riemann 和和右 Riemann 和。与精确值比较。

3. ★☆☆ 计算以下不定积分：
   (a) $\displaystyle\int (x^3 - 4x + 2)\,dx$
   (b) $\displaystyle\int \frac{1}{\sqrt{x}}\,dx$（$x > 0$）
   (c) $\displaystyle\int (3e^x - \sin x)\,dx$

4. ★★☆ 求曲线 $y = x^2$ 与 $y = 2x$ 之间的面积。

5. ★★☆ 设 $F(x) = \displaystyle\int_0^x \frac{\sin t}{t}\,dt$（$t \neq 0$ 时；$\sin t/t$ 在 $t = 0$ 定义为 $1$）。求 $F'(x)$。

6. ★★☆ 用定积分证明 $\displaystyle\int_0^1 x^n\,dx = \frac{1}{n+1}$（$n \geq 0$ 为整数）。

7. ★★★ 一物体的速度为 $v(t) = t^2 - 4t + 3$。
   (a) 在 $[0, 5]$ 上求物体的位移 $\int_0^5 v(t)\,dt$。
   (b) 在 $[0, 5]$ 上求物体经过的总路程 $\int_0^5 |v(t)|\,dt$。

---

## §3 Euler 公式

1. ★☆☆ 计算以下复数指数：
   (a) $e^{i\pi/4}$
   (b) $e^{i\pi/6}$
   (c) $e^{-i\pi/2}$
   (d) $e^{2+i\pi}$

2. ★☆☆ 将以下复数写成指数形式 $re^{i\theta}$：
   (a) $1 + i$
   (b) $-2$
   (c) $3i$
   (d) $-1 - \sqrt{3}\,i$

3. ★★☆ 用 Euler 公式推导以下三角恒等式：
   (a) $\cos 3\theta = 4\cos^3\theta - 3\cos\theta$
   (b) $\sin 3\theta = 3\sin\theta - 4\sin^3\theta$

4. ★★☆ 证明 $\overline{e^{i\theta}} = e^{-i\theta}$（其中 $\overline{\cdot}$ 表示复共轭）。

5. ★★☆ 利用 $e^{i\theta}$ 计算 $\displaystyle\sum_{k=0}^{n-1}\cos\frac{2\pi k}{n}$ 和 $\displaystyle\sum_{k=0}^{n-1}\sin\frac{2\pi k}{n}$。

6. ★★★ 证明 $\displaystyle\sum_{k=0}^{n}\cos(k\theta) = \frac{\sin((n+1/2)\theta)}{2\sin(\theta/2)}$（$\theta \neq 2m\pi$）。
   （提示：$\sum_{k=0}^{n}\cos(k\theta) = \text{Re}\sum_{k=0}^{n}e^{ik\theta}$，用几何级数公式。）
