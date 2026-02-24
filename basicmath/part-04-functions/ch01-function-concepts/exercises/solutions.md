# 第 1 章 函数概念 — 练习题解答

## §1 函数概念深化

**1.** 求自然定义域。

(a) 需 $x - 3 > 0$（分母不为零且根号内为正），定义域 $(3, +\infty)$。

(b) 需 $x^2 - 5x + 6 \geq 0$，即 $(x - 2)(x - 3) \geq 0$，解为 $x \leq 2$ 或 $x \geq 3$。定义域 $(-\infty, 2] \cup [3, +\infty)$。

(c) 需 $x + 1 > 0$（对数要求）且 $4 - x^2 > 0$（分母为正），即 $x > -1$ 且 $-2 < x < 2$。取交集：$(-1, 2)$。

---

**2.** 判断奇偶性。

(a) $f(-x) = (-x)^4 - 3(-x)^2 + 1 = x^4 - 3x^2 + 1 = f(x)$。**偶函数**。

(b) 定义域 $\mathbb{R}$，关于原点对称。$g(-x) = \frac{(-x)^3}{(-x)^2 + 1} = \frac{-x^3}{x^2 + 1} = -g(x)$。**奇函数**。

(c) $h(x)$ 的定义域需 $x + 1 \geq 0$ 且 $x - 1 \geq 0$，即 $x \geq 1$。定义域 $[1, +\infty)$ 不关于原点对称。**非奇非偶**。

---

**3.** 设 $x_1 < x_2$，$f(x_2) - f(x_1) = (2x_2 - 3) - (2x_1 - 3) = 2(x_2 - x_1) > 0$。故 $f$ 严格递增。$\blacksquare$

---

**4.** 设 $0 < x_1 < x_2$。

$$f(x_2) - f(x_1) = (x_2 - x_1) + \left(\frac{1}{x_2} - \frac{1}{x_1}\right) = (x_2 - x_1) - \frac{x_2 - x_1}{x_1 x_2}$$

$$= (x_2 - x_1)\left(1 - \frac{1}{x_1 x_2}\right)$$

$x_2 - x_1 > 0$。当 $x_1 x_2 < 1$（即 $0 < x_1 < x_2 < 1$）时，$1 - \frac{1}{x_1 x_2} < 0$，故 $f(x_2) - f(x_1) < 0$，$f$ 递减。

当 $x_1 x_2 > 1$（即 $1 < x_1 < x_2$）时，$1 - \frac{1}{x_1 x_2} > 0$，故 $f(x_2) - f(x_1) > 0$，$f$ 递增。$\blacksquare$

---

**5.** 对 $x \geq 0$：$|f(x)| = \frac{x}{x+1} = 1 - \frac{1}{x+1} < 1$。

对 $x < 0$：$|f(x)| = \frac{|x|}{|x|+1} = 1 - \frac{1}{|x|+1} < 1$。

所以 $|f(x)| < 1$，$f$ 有界。

当 $x \to +\infty$ 时 $f(x) \to 1$，当 $x \to -\infty$ 时 $f(x) \to -1$。但 $f$ 无法取到 $\pm 1$。因此 $\sup f = 1$，$\inf f = -1$（均取不到）。

---

**6.** 设 $x_1 < x_2 \leq 0$，则 $0 \leq -x_2 < -x_1$。由 $f$ 在 $[0, +\infty)$ 上严格递增：$f(-x_2) < f(-x_1)$。由偶函数性质：$f(x_2) < f(x_1)$。故 $f$ 在 $(-\infty, 0]$ 上严格递减。$\blacksquare$

---

**7.** $f(x+1)$ 是偶函数意味着 $f(-x+1) = f(x+1)$。令 $t = x$，得 $f(1-t) = f(1+t)$。这就是 $f$ 关于 $x = 1$ 对称。$\blacksquare$

---

**8.** 需证 $g(x) = f(x+1)$ 是偶函数，即 $g(-x) = g(x)$。

$g(-x) = f(-x + 1)$。由偶函数 $f(-x+1) = f(x-1)$。由周期性 $f(x-1) = f(x-1+2) = f(x+1) = g(x)$。$\blacksquare$

---

**9.** （概要）先证 $f(0) = 0$（令 $x = y = 0$），再证 $f(nx) = nf(x)$（归纳法），推出 $f(r) = cr$（$c = f(1)$）对有理数 $r$ 成立。有界性条件保证 $f$ 在 $(a,b)$ 上有界，进而由稠密性推出 $f(x) = cx$ 对所有实数 $x$ 成立。

---

**10.** 

$$f_e(x) = \frac{f(x) + f(-x)}{2} = \frac{(e^x + x) + (e^{-x} - x)}{2} = \frac{e^x + e^{-x}}{2} = \cosh x$$

$$f_o(x) = \frac{f(x) - f(-x)}{2} = \frac{(e^x + x) - (e^{-x} - x)}{2} = \frac{e^x - e^{-x}}{2} + x = \sinh x + x$$

验证：$\cosh x + \sinh x + x = e^x + x = f(x)$。✓

---

## §2 复合函数与反函数

**1.** (a) $(f \circ g)(x) = f(2x-3) = (2x-3)^2 + 1 = 4x^2 - 12x + 10$

(b) $(g \circ f)(x) = g(x^2+1) = 2(x^2+1) - 3 = 2x^2 - 1$

(c) $(f \circ f)(x) = f(x^2+1) = (x^2+1)^2 + 1 = x^4 + 2x^2 + 2$

---

**2.** $(f \circ g)(x) = f(\sqrt{x}) = \frac{1}{\sqrt{x} + 1}$。需 $x \in \text{dom}(g) = [0, +\infty)$ 且 $\sqrt{x} \in \text{dom}(f) = \mathbb{R} \setminus \{-1\}$。由于 $\sqrt{x} \geq 0$，自动满足 $\sqrt{x} \neq -1$。定义域 $[0, +\infty)$。

---

**3.** (a) $y = 3x - 7 \implies x = \frac{y+7}{3}$。$f^{-1}(x) = \frac{x+7}{3}$。

(b) $y = x^3 + 1 \implies x = \sqrt[3]{y-1}$。$g^{-1}(x) = \sqrt[3]{x-1}$。

(c) $y = \frac{2x+1}{x-1}$，$y(x-1) = 2x+1$，$yx - y = 2x + 1$，$x(y-2) = y+1$，$x = \frac{y+1}{y-2}$。$h^{-1}(x) = \frac{x+1}{x-2}$，$x \neq 2$。

---

**4.** $f(x) = x^2 + 2x = (x+1)^2 - 1$。$x \geq -1$ 时 $f$ 严格递增，值域 $[-1, +\infty)$。

$y = (x+1)^2 - 1 \implies (x+1)^2 = y+1 \implies x = -1 + \sqrt{y+1}$。

$f^{-1}(x) = -1 + \sqrt{x+1}$，$x \geq -1$。

---

**5.** 令 $t = e^x > 0$，$f = \frac{t-1}{t+1} = 1 - \frac{2}{t+1}$。$t \in (0, +\infty)$ 时 $\frac{2}{t+1} \in (0, 2)$，故 $f \in (-1, 1)$。值域 $(-1, 1)$。

求逆：$y = \frac{e^x - 1}{e^x + 1}$，$y(e^x + 1) = e^x - 1$，$ye^x + y = e^x - 1$，$e^x(y-1) = -1-y$，$e^x = \frac{1+y}{1-y}$，$x = \ln\frac{1+y}{1-y}$。

$f^{-1}(x) = \ln\frac{1+x}{1-x}$，$x \in (-1, 1)$。

---

**6.** 设 $x_1 < x_2$。$f$ 递增 $\implies f(x_1) < f(x_2)$。$g$ 递减 $\implies g(f(x_1)) > g(f(x_2))$。故 $(g \circ f)(x_1) > (g \circ f)(x_2)$，$g \circ f$ 递减。$\blacksquare$

---

**7.** $y = ax + b \implies x = \frac{y - b}{a}$，$f^{-1}(x) = \frac{x - b}{a}$。

验证：$f(f^{-1}(x)) = a \cdot \frac{x-b}{a} + b = x$。✓

$f = f^{-1}$ 意味着 $ax + b = \frac{x - b}{a}$ 对所有 $x$，即 $a^2 x + ab = x - b$。比较系数：$a^2 = 1$ 且 $ab = -b$。

$a = 1$ 时 $b = -b \implies b = 0$，$f(x) = x$。$a = -1$ 时 $-b = -b$（恒成立），$f(x) = -x + b$（任意 $b$）。

---

**8.** $y = \frac{ax+b}{cx+d}$，$y(cx+d) = ax+b$，$cxy + dy = ax + b$，$x(cy - a) = b - dy$，$x = \frac{b - dy}{cy - a} = \frac{dy - b}{a - cy}$。

$f^{-1}(x) = \frac{dx - b}{a - cx}$（$x \neq \frac{a}{c}$）。

若 $ad - bc = 0$，则 $\frac{a}{c} = \frac{b}{d}$（设 $cd \neq 0$），此时 $f(x) = \frac{a(x + b/a)}{c(x + d/c)} = \frac{a}{c}$（常函数），无反函数。

---

**9.** 先求 $f^{-1}$：$y = \frac{2x}{x+1}$，$yx + y = 2x$，$x(y-2) = -y$，$x = \frac{y}{2-y}$。$f^{-1}(x) = \frac{x}{2-x}$。

$f^{-1}(3) = \frac{3}{2-3} = \frac{3}{-1} = -3$。

$f^{-1}(f^{-1}(3)) = f^{-1}(-3) = \frac{-3}{2-(-3)} = \frac{-3}{5}$。

---

**10.** 由 $f \circ g = g \circ f$，两边取 $f^{-1}$ 作用于左侧：$f^{-1} \circ f \circ g = f^{-1} \circ g \circ f$，即 $g = f^{-1} \circ g \circ f$。两边右复合 $f^{-1}$：$g \circ f^{-1} = f^{-1} \circ g \circ f \circ f^{-1} = f^{-1} \circ g$。$\blacksquare$
