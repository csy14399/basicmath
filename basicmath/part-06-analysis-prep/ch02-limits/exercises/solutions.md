# 第 2 章 极限 — 练习题解答

## §1 函数的极限

**1.** 设 $\epsilon > 0$。$|(2x+3) - 5| = |2x-2| = 2|x-1|$。取 $\delta = \epsilon/2$。对 $0 < |x-1| < \delta$：$|2x+3-5| = 2|x-1| < 2\delta = \epsilon$。$\blacksquare$

---

**2.**
(a) $\dfrac{x^2-4}{x-2} = \dfrac{(x-2)(x+2)}{x-2} = x + 2$（$x \neq 2$）。$\lim_{x \to 2}(x+2) = 4$。

(b) $\dfrac{x^2+3x+2}{x+1} = \dfrac{(x+1)(x+2)}{x+1} = x + 2$（$x \neq -1$）。$\lim_{x \to -1}(x+2) = 1$。

(c) $\dfrac{(1+x)^2 - 1}{x} = \dfrac{1+2x+x^2-1}{x} = \dfrac{2x+x^2}{x} = 2 + x$（$x \neq 0$）。$\lim_{x \to 0}(2+x) = 2$。

---

**3.**
(a) $\dfrac{\sin 4x}{x} = 4 \cdot \dfrac{\sin 4x}{4x} \to 4 \cdot 1 = 4$。

(b) $\dfrac{\sin x}{2x} = \dfrac{1}{2} \cdot \dfrac{\sin x}{x} \to \dfrac{1}{2}$。

(c) $\dfrac{\tan x}{\sin x} = \dfrac{1}{\cos x} \to \dfrac{1}{1} = 1$。

---

**4.**
(a) $\lim_{x \to 0^+}\frac{1}{x} = +\infty$，$\lim_{x \to 0^-}\frac{1}{x} = -\infty$。

(b) $x \to 3^+$ 时 $x > 0$，$x-3 \to 0^+$，所以 $\frac{x}{x-3} \to +\infty$。$x \to 3^-$ 时 $x > 0$，$x-3 \to 0^-$，所以 $\frac{x}{x-3} \to -\infty$。

(c) $\lim_{x \to 0^+}\sqrt{x} = 0$。

---

**5.** 设 $\epsilon > 0$。$|x^2 - 1| = |x-1||x+1|$。限制 $|x-1| < 1$（即 $0 < x < 2$），则 $|x+1| < 3$。取 $\delta = \min(1, \epsilon/3)$。对 $0 < |x-1| < \delta$：$|x^2-1| = |x-1||x+1| < (\epsilon/3) \cdot 3 = \epsilon$。$\blacksquare$

---

**6.**
$$\frac{1-\cos x}{x\sin x} = \frac{1-\cos x}{x^2} \cdot \frac{x}{\sin x} \cdot x \cdot \frac{1}{x}$$

不，更简洁：

$$\frac{1-\cos x}{x\sin x} = \frac{1-\cos x}{x^2} \cdot \frac{x}{\sin x}$$

$\lim \frac{1-\cos x}{x^2} = \frac{1}{2}$，$\lim \frac{x}{\sin x} = 1$。

答案：$\dfrac{1}{2}$。

---

**7.**
$$\frac{\sqrt{1+x}-1}{x} = \frac{(\sqrt{1+x}-1)(\sqrt{1+x}+1)}{x(\sqrt{1+x}+1)} = \frac{x}{x(\sqrt{1+x}+1)} = \frac{1}{\sqrt{1+x}+1}$$

$\lim_{x \to 0}\dfrac{1}{\sqrt{1+x}+1} = \dfrac{1}{1+1} = \dfrac{1}{2}$。

---

**8.**
(a) $\lim_{x \to 0^+}\frac{|x|}{x} = 1$，$\lim_{x \to 0^-}\frac{|x|}{x} = -1$。左右极限不等，极限不存在。

(b) $|x\cos(1/x)| \leq |x| \to 0$。由夹逼定理，$\lim_{x \to 0}x\cos(1/x) = 0$。存在。

(c) 取 $x_n = 1/(2n\pi)$，$\cos(1/x_n) = \cos(2n\pi) = 1$。取 $y_n = 1/((2n+1)\pi/2)$，$\cos(1/y_n) = \cos((2n+1)\pi/2) = 0$。不同子列给出不同极限，极限不存在。

---

**9.** $\dfrac{e^{3x}-1}{x} = 3 \cdot \dfrac{e^{3x}-1}{3x} \to 3 \cdot 1 = 3$。

---

**10.** $\dfrac{\ln(1+2x)}{\sin x} = \dfrac{\ln(1+2x)}{2x} \cdot \dfrac{2x}{\sin x} \cdot 1 \to 1 \cdot 2 = 2$。

或用等价无穷小：$\ln(1+2x) \sim 2x$，$\sin x \sim x$，$\lim = 2x/x = 2$。

---

**11.** 设 $\epsilon > 0$。$|x^2\sin(1/x)| \leq |x^2| \cdot 1 = x^2$。取 $\delta = \sqrt{\epsilon}$。对 $0 < |x| < \delta$：$|x^2\sin(1/x)| \leq x^2 < \delta^2 = \epsilon$。$\blacksquare$

---

**12.** 设 $\epsilon > 0$。对 $x \neq 0$：$|f(x) - 0| = |x\sin(1/x)| \leq |x|$。取 $\delta = \epsilon$。对 $0 < |x| < \delta$：$|f(x)| \leq |x| < \delta = \epsilon$。$\blacksquare$

---

## §2 无穷大与无穷小

**1.**
(a) $\lim_{x \to 0}x^2 = 0$。是。
(b) $\lim_{x \to 0}\sin x = 0$。是。
(c) $\lim_{x \to 0}(1+x) = 1 \neq 0$。不是。
(d) $\lim_{x \to 0}(x+x^2) = 0$。是。
(e) $\lim_{x \to 0}(e^x - 1) = 0$。是。

---

**2.**
(a) $\dfrac{3x^2+1}{x^2-x} = \dfrac{3+1/x^2}{1-1/x} \to \dfrac{3}{1} = 3$。

(b) 指数增长快于幂增长，$\dfrac{x}{e^x} \to 0$。

(c) $\dfrac{\ln x}{x^2} \to 0$（对数增长远慢于幂增长）。

---

**3.** 垂直渐近线：$x = 1$（$\lim_{x \to 1}\frac{1}{x-1} = \pm\infty$）。水平渐近线：$y = 0$（$\lim_{x \to \pm\infty}\frac{1}{x-1} = 0$）。

---

**4.** $\lim_{x \to 0}\dfrac{x^3}{\sin x} = \lim_{x \to 0}\dfrac{x^3}{x} \cdot \dfrac{x}{\sin x} = \lim x^2 \cdot 1 = 0$。是，$x^3 = o(\sin x)$。

由于 $\sin x \sim x$，这等价于说 $x^3 = o(x)$（$x^3$ 比 $x$ 高阶），显然成立。

---

**5.**
(a) $\sin 2x \sim 2x$，$e^x - 1 \sim x$。$\lim = \dfrac{2x}{x} = 2$。

(b) $\arctan x \sim x$，$\ln(1+x) \sim x$。$\lim = \dfrac{x}{x} = 1$。

(c) $1 - \cos 3x \sim \dfrac{(3x)^2}{2} = \dfrac{9x^2}{2}$，$\sin 2x \sim 2x$。$\lim = \dfrac{9x^2/2}{x \cdot 2x} = \dfrac{9x^2/2}{2x^2} = \dfrac{9}{4}$。

---

**6.** $f(x) = \dfrac{x^2-1}{x^2-4} = \dfrac{(x-1)(x+1)}{(x-2)(x+2)}$。

垂直渐近线：$x = 2$，$x = -2$（分母为零处）。

水平渐近线：$\lim_{x \to \pm\infty}\dfrac{x^2-1}{x^2-4} = \dfrac{1-1/x^2}{1-4/x^2} \to 1$。$y = 1$。

---

**7.** $f(x) = \dfrac{2x^2+x-1}{x+1}$。长除法：$f(x) = 2x - 1 + \dfrac{0}{x+1} = 2x - 1$（实际上分子 $2x^2+x-1 = (2x-1)(x+1)$，所以 $f(x) = 2x - 1$（$x \neq -1$））。

垂直渐近线：$x = -1$（但实际上可以消去，需检查）。$\dfrac{2x^2+x-1}{x+1} = \dfrac{(2x-1)(x+1)}{x+1} = 2x-1$（$x \neq -1$）。$\lim_{x \to -1}f(x) = -3$。无垂直渐近线（可去间断点）。

也无斜渐近线——$f$ 就是 $2x-1$（去掉一个点）。$\lim_{x \to \pm\infty}[f(x) - (2x-1)] = 0$，但 $f$ 本身就是线性的。

---

**8.** 设 $a = 1 + h$（$h > 0$）。对 $x$ 为正整数 $m$（一般情况由此推出）：

$$a^m = (1+h)^m \geq \binom{m}{n+1}h^{n+1} = \frac{m!}{(n+1)!(m-n-1)!}h^{n+1}$$

对 $m > n+1$，此式 $\geq \dfrac{h^{n+1}}{(n+1)!} \cdot m^{n+1} \cdot \dfrac{(m-1)\cdots(m-n)}{m^n}$。

更简单地，对 $m > 2(n+1)$：

$$a^m > \binom{m}{n+1}h^{n+1} \geq \frac{m^{n+1}h^{n+1}}{2^{n+1}(n+1)!}$$

因此 $\dfrac{m^n}{a^m} < \dfrac{m^n \cdot 2^{n+1}(n+1)!}{m^{n+1}h^{n+1}} = \dfrac{2^{n+1}(n+1)!}{m \cdot h^{n+1}} \to 0$（$m \to \infty$）。

由此 $\lim_{m \to \infty}\dfrac{m^n}{a^m} = 0$。将结果从整数推广到实数可用夹逼。$\blacksquare$

---

**9.** 分子分母同除以 $x^m$：

$$\frac{P(x)}{Q(x)} = \frac{a_n x^{n-m} + \cdots + a_0/x^m}{b_m + b_{m-1}/x + \cdots + b_0/x^m}$$

- 若 $n > m$：分子 $\to \pm\infty$（首项 $a_n x^{n-m}$ 主导），分母 $\to b_m$。极限为 $\pm\infty$（符号取决于 $a_n/b_m$ 的符号）。
- 若 $n = m$：$\lim = a_n / b_m$（最高次系数之比）。
- 若 $n < m$：分子 $\to 0$（所有项含 $x$ 的负幂），分母 $\to b_m$。$\lim = 0$。
