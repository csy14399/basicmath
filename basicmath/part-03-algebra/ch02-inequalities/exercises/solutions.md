# 第 2 章 不等式 — 练习题解答

## §1 基本不等式

**1.** $3x + 7 > 2x - 5$

$x > -12$

解集：$(-12, +\infty)$。

---

**2.** $-2x + 4 \leq 3x + 9$

$-5x \leq 5$

$x \geq -1$

解集：$[-1, +\infty)$。

---

**3.** 第一个不等式：$x > 1$。第二个：$x < 4$。交集：$(1, 4)$。

---

**4.** $x^2 - 3x - 10 > 0$

$(x - 5)(x + 2) > 0$

根 $x_1 = -2, x_2 = 5$。$a = 1 > 0$，"大于零取两边"。

解集：$(-\infty, -2) \cup (5, +\infty)$。

---

**5.** $2x^2 + 5x - 3 \leq 0$

$\Delta = 25 + 24 = 49$。根：$x = \frac{-5 \pm 7}{4}$，即 $x_1 = -3, x_2 = \frac{1}{2}$。

$a = 2 > 0$，"小于等于零取中间"。

解集：$\left[-3, \frac{1}{2}\right]$。

---

**6.** $|x - 4| < 3 \iff 1 < x < 7$。解集：$(1, 7)$。

---

**7.** $|2x + 1| \geq 7$

$2x + 1 \geq 7$ 或 $2x + 1 \leq -7$

$x \geq 3$ 或 $x \leq -4$

解集：$(-\infty, -4] \cup [3, +\infty)$。

---

**8.** $x^2 - 2x + 3 > 0$

$\Delta = 4 - 12 = -8 < 0$。$a = 1 > 0$。

配方：$(x-1)^2 + 2 \geq 2 > 0$。对所有实数成立。

解集：$\mathbb{R}$。

---

**9.** $\frac{x-1}{x+2} > 0$

分子分母同号时分式为正：

- $x - 1 > 0$ 且 $x + 2 > 0$：$x > 1$
- $x - 1 < 0$ 且 $x + 2 < 0$：$x < -2$

解集：$(-\infty, -2) \cup (1, +\infty)$。

---

**10.** 令 $u = a - b$，$v = b - c$。则 $a - c = u + v$。

由三角不等式：$|a - c| = |u + v| \leq |u| + |v| = |a - b| + |b - c|$。$\blacksquare$

---

**11.** $|2x^2 - 2| = 2|x^2 - 1| = 2|x - 1| \cdot |x + 1|$。

由 $|x - 1| < \frac{1}{2}$：$\frac{1}{2} < x < \frac{3}{2}$，所以 $\frac{3}{2} < x + 1 < \frac{5}{2}$，$|x + 1| < \frac{5}{2}$。

$|2x^2 - 2| < 2 \cdot \frac{1}{2} \cdot \frac{5}{2} = \frac{5}{2}$。

---

**12.** 分三个区间讨论：

**区间 1**（$x \geq 1$）：$(x-1) + (x+2) > 5$，$2x + 1 > 5$，$x > 2$。与 $x \geq 1$ 交集：$x > 2$。

**区间 2**（$-2 \leq x < 1$）：$(1-x) + (x+2) > 5$，$3 > 5$，不成立。无解。

**区间 3**（$x < -2$）：$(1-x) + (-x-2) > 5$，$-2x - 1 > 5$，$x < -3$。与 $x < -2$ 交集：$x < -3$。

解集：$(-\infty, -3) \cup (2, +\infty)$。

---

**13.** 三角形条件：$a < b + c$，$b < a + c$，$c < a + b$。

$a < b + c \implies a^2 < a(b + c) = ab + ac$

$b < a + c \implies b^2 < ab + bc$

$c < a + b \implies c^2 < ac + bc$

三式相加：$a^2 + b^2 + c^2 < 2(ab + bc + ac)$。$\blacksquare$

---

## §2 经典不等式

**1.** 由 AM-GM：$x + \frac{4}{x} \geq 2\sqrt{x \cdot \frac{4}{x}} = 2\sqrt{4} = 4$。

等号当 $x = \frac{4}{x}$，即 $x = 2$（因为 $x > 0$）。

最小值为 $4$。

---

**2.** 由 AM-GM：$\frac{a+b}{2} \geq \sqrt{ab}$，$2 \geq \sqrt{ab}$，$ab \leq 4$。

等号当 $a = b = 2$。最大值 $4$。

---

**3.** $a_1 b_1 + a_2 b_2 = 3 + 8 = 11$。$(a_1^2 + a_2^2)(b_1^2 + b_2^2) = (1 + 4)(9 + 16) = 5 \times 25 = 125$。

$11^2 = 121 \leq 125$。✓

---

**4.** 调和平均 $H = \frac{2}{\frac{1}{a} + \frac{1}{b}} = \frac{2ab}{a+b}$。

需证 $\frac{a+b}{2} \geq \frac{2ab}{a+b}$，即 $(a+b)^2 \geq 4ab$，即 $a^2 + 2ab + b^2 \geq 4ab$，即 $(a-b)^2 \geq 0$。✓

等号当 $a = b$。$\blacksquare$

---

**5.** 由 AM-GM（三元）：$\frac{x + y + z}{3} \geq \sqrt[3]{xyz} = \sqrt[3]{8} = 2$。

$x + y + z \geq 6$。等号当 $x = y = z = 2$。最小值 $6$。

---

**6.** 取 $a_i = i$（$i = 1, \ldots, n$），$b_i = 1$。由 Cauchy-Schwarz：

$\left(\sum_{i=1}^n i \cdot 1\right)^2 \leq \left(\sum_{i=1}^n i^2\right)\left(\sum_{i=1}^n 1^2\right)$

$(1 + 2 + \cdots + n)^2 \leq n(1^2 + 2^2 + \cdots + n^2)$。$\blacksquare$

---

**7.** 对每个因子用 AM-GM：

$a + b \geq 2\sqrt{ab}$，$b + c \geq 2\sqrt{bc}$，$c + a \geq 2\sqrt{ca}$。

三式相乘：$(a+b)(b+c)(c+a) \geq 8\sqrt{ab} \cdot \sqrt{bc} \cdot \sqrt{ca} = 8\sqrt{a^2b^2c^2} = 8abc$。

等号当 $a = b = c$。$\blacksquare$

---

**8.** 由 Cauchy-Schwarz 分数形式：

$$\sum \frac{1}{x_i} = \sum \frac{1^2}{x_i} \geq \frac{n^2}{\sum x_i} = \frac{n^2}{S}$$

$\blacksquare$

---

**9.** 令 $x = b + c - a > 0$，$y = a + c - b > 0$，$z = a + b - c > 0$（三角形条件保证正性）。

则 $a = \frac{y+z}{2}$，$b = \frac{x+z}{2}$，$c = \frac{x+y}{2}$。

$$\frac{a}{x} + \frac{b}{y} + \frac{c}{z} = \frac{y+z}{2x} + \frac{x+z}{2y} + \frac{x+y}{2z}$$

$$= \frac{1}{2}\left(\frac{y}{x} + \frac{z}{x} + \frac{x}{y} + \frac{z}{y} + \frac{x}{z} + \frac{y}{z}\right)$$

$$= \frac{1}{2}\left[\left(\frac{x}{y} + \frac{y}{x}\right) + \left(\frac{y}{z} + \frac{z}{y}\right) + \left(\frac{x}{z} + \frac{z}{x}\right)\right]$$

由 AM-GM，$\frac{x}{y} + \frac{y}{x} \geq 2$，其他两对类似。

所以 $\frac{a}{x} + \frac{b}{y} + \frac{c}{z} \geq \frac{1}{2}(2 + 2 + 2) = 3$。$\blacksquare$

---

**10.** 需要证明四个不等式。

**(i) QM $\geq$ AM**：$\sqrt{\frac{a^2+b^2}{2}} \geq \frac{a+b}{2}$

两边平方：$\frac{a^2+b^2}{2} \geq \frac{(a+b)^2}{4} = \frac{a^2+2ab+b^2}{4}$

$2(a^2+b^2) \geq a^2+2ab+b^2$

$a^2 - 2ab + b^2 \geq 0$

$(a-b)^2 \geq 0$。✓

**(ii) AM $\geq$ GM**：已证（定理 1）。

**(iii) GM $\geq$ HM**：$\sqrt{ab} \geq \frac{2ab}{a+b}$

$\sqrt{ab}(a+b) \geq 2ab$

$a + b \geq 2\sqrt{ab}$（这就是 AM-GM！）✓

$\blacksquare$
