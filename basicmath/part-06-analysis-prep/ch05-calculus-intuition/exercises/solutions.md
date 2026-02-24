# 第 5 章 微积分直觉 — 练习题解答

## §1 导数的直觉

**1.**
(a) $\dfrac{3(x+h)+5 - (3x+5)}{h} = \dfrac{3h}{h} = 3$。$f'(x) = 3$。

(b) $\dfrac{(1+h)^2 - 2(1+h) - (1-2)}{h} = \dfrac{1+2h+h^2-2-2h+1}{h} = \dfrac{h^2}{h} = h \to 0$。$f'(1) = 0$。

(c) $\dfrac{1/(x+h+1) - 1/(x+1)}{h} = \dfrac{(x+1)-(x+h+1)}{h(x+h+1)(x+1)} = \dfrac{-1}{(x+h+1)(x+1)} \to \dfrac{-1}{(x+1)^2}$。

---

**2.**
(a) $f'(x) = 20x^3 - 6x + 7$。

(b) 乘积法则：$f'(x) = 2x\cos x - x^2\sin x$。

(c) 商法则：$f'(x) = \dfrac{(x+1) - x}{(x+1)^2} = \dfrac{1}{(x+1)^2}$。

(d) 链式法则：$f'(x) = e^{x^2} \cdot 2x = 2xe^{x^2}$。

---

**3.** $y' = 3x^2$。$y'(1) = 3$。切线：$y - 1 = 3(x-1)$，即 $y = 3x - 2$。

---

**4.** 链式法则：$f'(x) = \cos(e^x) \cdot e^x = e^x\cos(e^x)$。

---

**5.** $x|x| = \begin{cases}x^2 & x \geq 0 \\ -x^2 & x < 0\end{cases}$。

$\dfrac{f(h)-f(0)}{h} = \dfrac{h|h|}{h} = |h| \to 0$。$f'(0) = 0$。$\blacksquare$

---

**6.** $\dfrac{f(h)-0}{h} = h\sin(1/h)$。$|h\sin(1/h)| \leq |h| \to 0$。由夹逼定理，$f'(0) = 0$。

$x \neq 0$ 时，$f'(x) = 2x\sin(1/x) + x^2 \cdot (-1/x^2)\cos(1/x) = 2x\sin(1/x) - \cos(1/x)$。

$\lim_{x \to 0}f'(x)$ 不存在（$\cos(1/x)$ 振荡）。$f'$ 在 $x = 0$ 处**不连续**。

---

**7.**
(a) $v(t) = s'(t) = gt = 9.8t$（m/s）。

(b) $a(t) = v'(t) = g = 9.8$（m/s²），常数加速度。

---

## §2 积分的直觉

**1.**
(a) $\int_0^3(2x+1)\,dx = [x^2+x]_0^3 = 9+3 = 12$。

(b) $\int_0^{\pi/2}\cos x\,dx = [\sin x]_0^{\pi/2} = 1 - 0 = 1$。

(c) $\int_1^e 2/x\,dx = [2\ln x]_1^e = 2\ln e - 2\ln 1 = 2$。

---

**2.** $\Delta x = 1/2$。$x_0=0, x_1=0.5, x_2=1, x_3=1.5, x_4=2$。

左 Riemann 和：$L_4 = (0^3+0.5^3+1^3+1.5^3) \cdot 0.5 = (0+0.125+1+3.375)\cdot 0.5 = 4.5 \cdot 0.5 = 2.25$。

右 Riemann 和：$R_4 = (0.5^3+1^3+1.5^3+2^3) \cdot 0.5 = (0.125+1+3.375+8)\cdot 0.5 = 12.5\cdot 0.5 = 6.25$。

精确值：$\int_0^2 x^3\,dx = [x^4/4]_0^2 = 4$。$L_4 < 4 < R_4$。

---

**3.**
(a) $\dfrac{x^4}{4} - 2x^2 + 2x + C$。

(b) $\int x^{-1/2}\,dx = \dfrac{x^{1/2}}{1/2} + C = 2\sqrt{x} + C$。

(c) $3e^x + \cos x + C$。

---

**4.** 交点：$x^2 = 2x \Rightarrow x = 0$ 或 $x = 2$。$[0,2]$ 上 $2x \geq x^2$。

$A = \int_0^2(2x-x^2)\,dx = [x^2-x^3/3]_0^2 = 4 - 8/3 = 4/3$。

---

**5.** 由 FTC Part 1：$F'(x) = \dfrac{\sin x}{x}$（$x \neq 0$），$F'(0) = 1$。

---

**6.** $\int_0^1 x^n\,dx = \left[\dfrac{x^{n+1}}{n+1}\right]_0^1 = \dfrac{1}{n+1} - 0 = \dfrac{1}{n+1}$。$\blacksquare$

---

**7.**
(a) $v(t) = t^2-4t+3 = (t-1)(t-3)$。零点 $t = 1, 3$。

$\int_0^5 v\,dt = [t^3/3 - 2t^2 + 3t]_0^5 = (125/3 - 50 + 15) - 0 = 125/3 - 35 = 20/3$。

(b) $v(t) > 0$ on $[0,1)$, $v(t) < 0$ on $(1,3)$, $v(t) > 0$ on $(3,5]$。

$\int_0^1 v\,dt = [t^3/3 - 2t^2+3t]_0^1 = 1/3-2+3 = 4/3$。

$\int_1^3 v\,dt = [t^3/3-2t^2+3t]_1^3 = (9-18+9)-(1/3-2+3) = 0 - 4/3 = -4/3$。

$\int_3^5 v\,dt = [t^3/3-2t^2+3t]_3^5 = (125/3-50+15)-(9-18+9) = 20/3 - 0 = 20/3$。

总路程 $= 4/3 + 4/3 + 20/3 = 28/3$。

---

## §3 Euler 公式

**1.**
(a) $e^{i\pi/4} = \cos(\pi/4) + i\sin(\pi/4) = \dfrac{\sqrt{2}}{2} + i\dfrac{\sqrt{2}}{2}$。

(b) $e^{i\pi/6} = \cos(\pi/6) + i\sin(\pi/6) = \dfrac{\sqrt{3}}{2} + i\dfrac{1}{2}$。

(c) $e^{-i\pi/2} = \cos(-\pi/2) + i\sin(-\pi/2) = 0 - i = -i$。

(d) $e^{2+i\pi} = e^2 \cdot e^{i\pi} = -e^2 \approx -7.389$。

---

**2.**
(a) $|1+i| = \sqrt{2}$，$\arg(1+i) = \pi/4$。$1+i = \sqrt{2}\,e^{i\pi/4}$。

(b) $|-2| = 2$，$\arg(-2) = \pi$。$-2 = 2e^{i\pi}$。

(c) $|3i| = 3$，$\arg(3i) = \pi/2$。$3i = 3e^{i\pi/2}$。

(d) $|-1-\sqrt{3}i| = 2$，$\arg(-1-\sqrt{3}i) = -2\pi/3$（或 $4\pi/3$）。$-1-\sqrt{3}i = 2e^{-2i\pi/3}$。

---

**3.**
(a) $e^{3i\theta} = (e^{i\theta})^3 = (\cos\theta+i\sin\theta)^3$。

展开：$\cos^3\theta + 3i\cos^2\theta\sin\theta - 3\cos\theta\sin^2\theta - i\sin^3\theta$。

实部 $= \cos^3\theta - 3\cos\theta\sin^2\theta = \cos^3\theta - 3\cos\theta(1-\cos^2\theta) = 4\cos^3\theta - 3\cos\theta$。

所以 $\cos 3\theta = 4\cos^3\theta - 3\cos\theta$。$\blacksquare$

(b) 虚部 $= 3\cos^2\theta\sin\theta - \sin^3\theta = 3(1-\sin^2\theta)\sin\theta - \sin^3\theta = 3\sin\theta - 4\sin^3\theta$。$\blacksquare$

---

**4.** $\overline{e^{i\theta}} = \overline{\cos\theta + i\sin\theta} = \cos\theta - i\sin\theta = \cos(-\theta) + i\sin(-\theta) = e^{-i\theta}$。$\blacksquare$

---

**5.** 设 $\omega = e^{2\pi i/n}$。$\sum_{k=0}^{n-1}\omega^k = \dfrac{1-\omega^n}{1-\omega} = \dfrac{1-1}{1-\omega} = 0$（$n \geq 2$）。

$\sum\cos(2\pi k/n) = \text{Re}(0) = 0$。$\sum\sin(2\pi k/n) = \text{Im}(0) = 0$。

---

**6.** $\sum_{k=0}^{n}e^{ik\theta} = \dfrac{1-e^{i(n+1)\theta}}{1-e^{i\theta}}$。

分子分母同乘 $e^{-i\theta/2}$：

$= \dfrac{e^{-i\theta/2} - e^{i(n+1/2)\theta}}{e^{-i\theta/2} - e^{i\theta/2}} = \dfrac{e^{-i\theta/2} - e^{i(n+1/2)\theta}}{-2i\sin(\theta/2)}$。

分子 $= -(e^{i(n+1/2)\theta} - e^{-i\theta/2})$。

利用 $e^{i\alpha} - e^{i\beta} = 2i\sin\left(\dfrac{\alpha-\beta}{2}\right)\,e^{i(\alpha+\beta)/2}$：

$e^{i(n+1/2)\theta} - e^{-i\theta/2} = 2i\sin\left(\dfrac{(n+1)\theta}{2}\right)\,e^{in\theta/2}$。

所以 $\sum = \dfrac{-2i\sin((n+1)\theta/2)\,e^{in\theta/2}}{-2i\sin(\theta/2)} = \dfrac{\sin((n+1)\theta/2)}{\sin(\theta/2)}\,e^{in\theta/2}$。

取实部：$\sum\cos(k\theta) = \dfrac{\sin((n+1)\theta/2)}{\sin(\theta/2)}\cos(n\theta/2)$。

经过三角恒等式化简，可以写成 $\dfrac{\sin((n+1/2)\theta)}{2\sin(\theta/2)}$（利用 $\sin A \cos B = \frac{1}{2}[\sin(A+B)+\sin(A-B)]$）。$\blacksquare$
