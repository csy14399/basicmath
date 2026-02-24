# §2 无穷大与无穷小（Infinity and Infinitesimal）

**前置知识**：[本章 §1 函数的极限](01-function-limits.md)（$\epsilon$-$\delta$ 定义、极限运算法则）、[Part 6 第 1 章 §1 数列的概念](../ch01-sequences/01-sequence-concepts.md)（数列的有界性）

**全景图**：上一节研究了"有限"的极限——$f(x) \to L$（有限数）。本节扩展视野：当 $f(x)$ 趋向 $0$ 或趋向 $\pm\infty$ 时会怎样？当 $x$ 本身趋向 $\pm\infty$ 时又会怎样？我们将引入无穷小量和无穷大量的概念及其比较，讨论 $x \to \infty$ 时的极限，初步介绍渐近分析（增长率比较、大 $O$ 记号），最后研究函数的水平渐近线和垂直渐近线。

**预估学习时间**：约 3–4 小时

---

## 动机

在上一节中，我们总假设极限 $L$ 是一个有限数。但数学中经常需要处理两种"极端"情况：

1. **无穷小**：函数值趋向 $0$（例如 $1/x$ 在 $x \to \infty$ 时）
2. **无穷大**：函数值"增长到无穷"（例如 $1/x$ 在 $x \to 0^+$ 时）

此外，我们还需要 $x \to \infty$ 时的极限（数列极限可以看作 $n \to \infty$ 时的特殊情况），以及比较不同函数增长快慢的工具。

---

## 1. 无穷小量（Infinitesimal）

> **定义 1**（无穷小量）
>
> 如果 $\displaystyle\lim_{x \to a} f(x) = 0$（或 $\lim_{x \to \infty} f(x) = 0$），则称 $f(x)$ 在 $x \to a$（或 $x \to \infty$）时是**无穷小量**（infinitesimal）。

**注意**：无穷小量不是一个"无穷小的数"——它是一个**极限为零的函数**。这与历史上 Leibniz 的"无穷小"概念有本质区别：我们用 $\epsilon$-$\delta$ 语言严格化了它。

### 1.1 无穷小量的性质

> **定理 1**（无穷小量的运算）
>
> 设 $f(x)$ 和 $g(x)$ 在 $x \to a$ 时都是无穷小量。则：
>
> 1. $f(x) + g(x)$ 是无穷小量
> 2. $f(x) \cdot g(x)$ 是无穷小量
> 3. 若 $h(x)$ 有界，则 $f(x) \cdot h(x)$ 是无穷小量
> 4. $f(x) / g(x)$ **不一定**是无穷小量——它可能是任何值

性质 3 解释了为什么 $x \sin(1/x) \to 0$（$x$ 是无穷小量，$\sin(1/x)$ 有界）。

性质 4 警告我们：$0/0$ 型极限需要逐个分析。

### 1.2 无穷小量的阶——比较

当两个函数都趋向零时，它们趋向零的"速度"可能不同。

> **定义 2**（无穷小量的比较）
>
> 设 $f(x), g(x)$ 在 $x \to a$ 时都是无穷小量且 $g(x) \neq 0$。
>
> 1. 若 $\displaystyle\lim_{x \to a}\frac{f(x)}{g(x)} = 0$，称 $f$ 是 $g$ 的**高阶无穷小**（$f$ 比 $g$ 更快趋于零），记 $f(x) = o(g(x))$
> 2. 若 $\displaystyle\lim_{x \to a}\frac{f(x)}{g(x)} = c \neq 0$（有限非零），称 $f$ 和 $g$ 是**同阶无穷小**
> 3. 若 $\displaystyle\lim_{x \to a}\frac{f(x)}{g(x)} = 1$，称 $f$ 和 $g$ 是**等价无穷小**，记 $f(x) \sim g(x)$

**重要等价无穷小**（$x \to 0$ 时）：

$$\sin x \sim x, \quad \tan x \sim x, \quad \arcsin x \sim x, \quad \arctan x \sim x$$

$$1 - \cos x \sim \frac{x^2}{2}, \quad e^x - 1 \sim x, \quad \ln(1+x) \sim x$$

$$(1+x)^\alpha - 1 \sim \alpha x \quad (\alpha \neq 0)$$

> **定理 2**（等价无穷小替换）
>
> 若 $f_1(x) \sim f_2(x)$，$g_1(x) \sim g_2(x)$（$x \to a$），则：
>
> $$\lim_{x \to a}\frac{f_1(x)}{g_1(x)} = \lim_{x \to a}\frac{f_2(x)}{g_2(x)}$$
>
> （前提是右边的极限存在）。

**例**：$\displaystyle\lim_{x \to 0}\frac{\sin 3x}{x} = \lim_{x \to 0}\frac{3x}{x} = 3$（用 $\sin 3x \sim 3x$）。

**注意**：等价替换只能在**乘除**中使用，不能在**加减**中使用。例如 $\sin x - x$ 不能替换为 $x - x = 0$——这丢失了高阶信息。实际上 $\sin x - x \sim -x^3/6$。

---

## 2. 无穷大量

> **定义 3**（函数趋向无穷）
>
> 如果对任意 $M > 0$，存在 $\delta > 0$，使得 $0 < |x - a| < \delta$ 时 $f(x) > M$，则记：
>
> $$\lim_{x \to a} f(x) = +\infty$$
>
> 类似地定义 $\lim_{x \to a} f(x) = -\infty$（$f(x) < -M$）和 $\lim_{x \to a} f(x) = \infty$（$|f(x)| > M$）。

**注意**：严格来说，$\lim_{x \to a} f(x) = \infty$ 意味着极限**不存在**——$\infty$ 不是实数。但 "$= \infty$" 这个记号给出了极限不存在的**方式**——比简单说"极限不存在"信息更丰富。

### 2.1 无穷大与无穷小的关系

> **定理 3**
>
> 若 $\lim f(x) = \infty$，则 $\lim \dfrac{1}{f(x)} = 0$（$f(x)$ 不为零时）。
>
> 反之，若 $\lim f(x) = 0$ 且 $f(x) \neq 0$，则 $\lim \dfrac{1}{f(x)} = \infty$。

**例**：$\lim_{x \to 0^+} \dfrac{1}{x} = +\infty$（因为 $\lim_{x \to 0^+} x = 0^+$）。

---

## 3. $x \to \infty$ 的极限

> **定义 4**（$x \to +\infty$ 时的极限）
>
> $$\lim_{x \to +\infty} f(x) = L \quad \Longleftrightarrow \quad \forall \epsilon > 0, \; \exists M > 0, \; \forall x > M: \; |f(x) - L| < \epsilon$$

类似地定义 $x \to -\infty$ 和 $x \to \infty$。

**例**：$\displaystyle\lim_{x \to +\infty}\frac{1}{x} = 0$，$\displaystyle\lim_{x \to +\infty}\frac{3x-1}{2x+5} = \frac{3}{2}$。

这与数列极限完全类似——事实上，数列极限是 $x \to +\infty$ 时函数极限的特殊情况（将 $x$ 限制为正整数）。

---

## 4. 渐近分析初步（Introduction to Asymptotic Analysis）

### 4.1 增长率比较

不同函数增长到无穷的速度差异极大。以下是一个重要的增长率阶梯：

> **定理 4**（增长率阶梯）
>
> 当 $x \to +\infty$ 时：
>
> $$\ln x \ll x^\alpha \ll a^x \ll x! \ll x^x$$
>
> 其中 $\alpha > 0$，$a > 1$。这里 $f \ll g$ 表示 $\displaystyle\lim_{x \to +\infty}\frac{f(x)}{g(x)} = 0$。

具体来说：

1. **对数增长 $\ll$ 幂增长**：$\displaystyle\lim_{x \to +\infty}\frac{\ln x}{x^\alpha} = 0$（$\alpha > 0$）
2. **幂增长 $\ll$ 指数增长**：$\displaystyle\lim_{x \to +\infty}\frac{x^n}{a^x} = 0$（$a > 1$，$n \in \mathbb{N}$）
3. **指数增长 $\ll$ 阶乘增长**（离散情形）

> **例题 1**：证明 $\displaystyle\lim_{x \to +\infty}\frac{\ln x}{x} = 0$。

> **证明**
>
> 令 $t = \ln x$，则 $x = e^t$，$x \to +\infty$ 时 $t \to +\infty$。
>
> $$\frac{\ln x}{x} = \frac{t}{e^t}$$
>
> 对 $t > 0$，由 $e^t > t^2/2$（因为 $e^t = 1 + t + t^2/2 + \cdots > t^2/2$）：
>
> $$0 < \frac{t}{e^t} < \frac{t}{t^2/2} = \frac{2}{t} \to 0$$
>
> 由夹逼定理，$\dfrac{t}{e^t} \to 0$。$\blacksquare$

### 4.2 大 $O$ 记号（Big-O Notation）——预览

> **定义 5**（大 $O$ 记号，预览）
>
> 若存在常数 $C > 0$ 和 $x_0$ 使得对所有 $x > x_0$：
>
> $$|f(x)| \leq C \cdot g(x)$$
>
> 则记 $f(x) = O(g(x))$（读作"$f$ 是 $g$ 的大 $O$"），表示 $f$ 的增长**不超过** $g$ 的常数倍。

**例**：

- $3x^2 + 5x + 1 = O(x^2)$（当 $x \to \infty$）
- $\sin x = O(1)$
- $\ln x = O(x^\epsilon)$（对任意 $\epsilon > 0$）

大 $O$ 记号在计算机科学（算法复杂度分析）和数学分析中都极为重要。完整的讨论将在后续课程中给出。

### 4.3 小 $o$ 记号

> **定义 6**（小 $o$ 记号）
>
> 若 $\displaystyle\lim_{x \to a}\frac{f(x)}{g(x)} = 0$，则记 $f(x) = o(g(x))$，表示 $f$ 的增长**严格慢于** $g$。

这与定义 2 中的高阶无穷小记号一致。$o$ 比 $O$ 更强：$o(g)$ 意味着 $O(g)$，但反之不然。

---

## 5. 水平渐近线和垂直渐近线

### 5.1 水平渐近线（Horizontal Asymptote）

> **定义 7**（水平渐近线）
>
> 若 $\displaystyle\lim_{x \to +\infty} f(x) = L$ 或 $\displaystyle\lim_{x \to -\infty} f(x) = L$，则直线 $y = L$ 是 $f(x)$ 的**水平渐近线**。

**例**：$f(x) = \dfrac{2x-1}{x+3}$。$\lim_{x \to \pm\infty} f(x) = 2$。水平渐近线为 $y = 2$。

一个函数可以有零条、一条或两条水平渐近线（$x \to +\infty$ 和 $x \to -\infty$ 的极限可能不同）。

**例**：$f(x) = \arctan x$。$\lim_{x \to +\infty}\arctan x = \pi/2$，$\lim_{x \to -\infty}\arctan x = -\pi/2$。两条水平渐近线：$y = \pi/2$ 和 $y = -\pi/2$。

### 5.2 垂直渐近线（Vertical Asymptote）

> **定义 8**（垂直渐近线）
>
> 若 $\displaystyle\lim_{x \to a^+} f(x) = \pm\infty$ 或 $\displaystyle\lim_{x \to a^-} f(x) = \pm\infty$，则直线 $x = a$ 是 $f(x)$ 的**垂直渐近线**。

**例**：$f(x) = \dfrac{1}{x-2}$。$\lim_{x \to 2^+}f(x) = +\infty$，$\lim_{x \to 2^-}f(x) = -\infty$。垂直渐近线为 $x = 2$。

**例**：$f(x) = \dfrac{x}{x^2 - 1} = \dfrac{x}{(x-1)(x+1)}$。垂直渐近线：$x = 1$ 和 $x = -1$。水平渐近线：$y = 0$（因为 $\lim_{x \to \pm\infty}f(x) = 0$）。

### 5.3 斜渐近线（Oblique Asymptote）

> **定义 9**（斜渐近线，简述）
>
> 若 $\displaystyle\lim_{x \to \pm\infty}[f(x) - (kx + b)] = 0$（$k \neq 0$），则 $y = kx + b$ 是 $f(x)$ 的**斜渐近线**。

求法：$k = \displaystyle\lim_{x \to \pm\infty}\frac{f(x)}{x}$，$b = \displaystyle\lim_{x \to \pm\infty}[f(x) - kx]$。

> **例题 2**：求 $f(x) = \dfrac{x^2 + 1}{x}$ 的渐近线。

**解**：$f(x) = x + \dfrac{1}{x}$。

垂直渐近线：$x = 0$（$\lim_{x \to 0^+}f(x) = +\infty$）。

斜渐近线：$\lim_{x \to \pm\infty}[f(x) - x] = \lim \dfrac{1}{x} = 0$。斜渐近线为 $y = x$。

---

## 例题（综合）

> **例题 3**：利用等价无穷小求 $\displaystyle\lim_{x \to 0}\frac{\arctan 2x}{\sin 3x}$。

**解**：$x \to 0$ 时，$\arctan 2x \sim 2x$，$\sin 3x \sim 3x$。

$$\lim_{x \to 0}\frac{\arctan 2x}{\sin 3x} = \lim_{x \to 0}\frac{2x}{3x} = \frac{2}{3}$$

---

> **例题 4**：求 $f(x) = \dfrac{3x^2 - x + 2}{x^2 + 4}$ 的所有渐近线。

**解**：

分母 $x^2 + 4 > 0$ 恒成立，无垂直渐近线。

$$\lim_{x \to \pm\infty}\frac{3x^2 - x + 2}{x^2 + 4} = \lim_{x \to \pm\infty}\frac{3 - 1/x + 2/x^2}{1 + 4/x^2} = 3$$

水平渐近线：$y = 3$。

---

## 要点回顾

| 概念 | 要点 |
|------|------|
| 无穷小量 | $\lim f(x) = 0$，是极限为零的函数，不是"无穷小的数" |
| 等价无穷小 | $f \sim g$ 意味着 $\lim f/g = 1$，可在乘除中替换 |
| 无穷大量 | $\lim f(x) = \infty$，严格说极限不存在但指明了不存在的方式 |
| $x \to \infty$ 的极限 | 推广 $\epsilon$-$\delta$ 定义，$\delta$ 换成 $M$：$x > M$ 时 $\|f(x)-L\| < \epsilon$ |
| 增长率 | $\ln x \ll x^\alpha \ll a^x \ll x! \ll x^x$ |
| 大 $O$ / 小 $o$ | $O(g)$：增长不超过 $g$ 的常数倍；$o(g)$：增长严格慢于 $g$ |
| 水平渐近线 | $\lim_{x \to \pm\infty}f(x) = L$ 时 $y = L$ |
| 垂直渐近线 | $\lim_{x \to a}f(x) = \pm\infty$ 时 $x = a$ |

---

## 进度检查点

完成本节后，你应该能够：

- [ ] 解释无穷小量的严格含义，区分它与历史上的"无穷小"概念
- [ ] 判断两个无穷小量的阶关系（高阶、同阶、等价）
- [ ] 运用等价无穷小替换简化极限计算
- [ ] 写出 $x \to \infty$ 时极限的 $\epsilon$-$M$ 定义
- [ ] 比较对数、多项式、指数函数的增长率
- [ ] 求函数的水平渐近线和垂直渐近线

---

## 自测题

**自测题 1**：$x \to 0$ 时，$x^2$ 和 $x$ 哪个是高阶无穷小？

<details>
<summary>答案</summary>

$x^2$ 是 $x$ 的高阶无穷小，因为 $\lim_{x \to 0}\dfrac{x^2}{x} = \lim x = 0$。即 $x^2 = o(x)$。

直觉：$x^2$ 比 $x$ 更快地趋于零。当 $x = 0.01$ 时，$x = 0.01$ 而 $x^2 = 0.0001$——小了两个数量级。
</details>

**自测题 2**：用等价无穷小求 $\displaystyle\lim_{x \to 0}\frac{e^x - 1}{\sin x}$。

<details>
<summary>答案</summary>

$x \to 0$ 时，$e^x - 1 \sim x$，$\sin x \sim x$。

$$\lim_{x \to 0}\frac{e^x - 1}{\sin x} = \lim_{x \to 0}\frac{x}{x} = 1$$
</details>

**自测题 3**：$\displaystyle\lim_{x \to +\infty}\frac{x^{100}}{2^x} = ?$ 为什么？

<details>
<summary>答案</summary>

$= 0$。因为指数增长（$2^x$）远快于任何幂增长（$x^{100}$）。这是增长率阶梯 $x^n \ll a^x$（$a > 1$）的直接推论。

无论多项式的次数多高，指数函数最终都会超过它并将比值压缩到零。
</details>

**自测题 4**：$f(x) = \dfrac{x^2}{x-1}$ 有哪些渐近线？

<details>
<summary>答案</summary>

垂直渐近线：$x = 1$（$\lim_{x \to 1}f(x) = \pm\infty$）。

斜渐近线：$f(x) = x + 1 + \dfrac{1}{x-1}$（长除法）。$\lim_{x \to \pm\infty}[f(x) - (x+1)] = 0$。斜渐近线 $y = x + 1$。

没有水平渐近线（$f(x) \to \pm\infty$）。
</details>

---

## 习题引用

本节练习见[练习题](exercises/exercises.md)第 §2 部分。
