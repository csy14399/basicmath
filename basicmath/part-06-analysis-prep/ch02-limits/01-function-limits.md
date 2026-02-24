# §1 函数的极限（Function Limits）

**前置知识**：[Part 6 第 1 章 §2 数列的极限](../ch01-sequences/02-sequence-limits.md)（$\epsilon$-$N$ 定义）、[Part 4 第 1 章 函数概念](../../part-04-functions/ch01-concepts/README.md)（函数的定义）、[Part 3 第 2 章 不等式](../../part-03-algebra/ch02-inequalities/README.md)（绝对值不等式）

**全景图**：本节将数列极限的思想从离散推广到连续——从 $n \to \infty$ 推广到 $x \to a$。核心是 $\epsilon$-$\delta$ 定义：Weierstrass 的杰作，分析学中最重要的定义。我们先建立直觉，然后给出精确定义，学会用定义证明极限，讨论单侧极限和极限运算法则，最后推导两个贯穿整个微积分的重要极限。

**预估学习时间**：约 5–8 小时

---

## 动机

在第一章中，我们研究了当 $n \to \infty$ 时数列 $a_n$ 的行为。但在微积分中，我们更关心的是：

**当 $x$ 趋近于某个有限值 $a$ 时，$f(x)$ 的行为。**

例如：

$$f(x) = \frac{x^2 - 1}{x - 1}$$

$f(1)$ 没有定义（分母为零）。但当 $x$ 接近 $1$ 时，$f(x)$ 趋向什么值？

$$f(x) = \frac{(x-1)(x+1)}{x-1} = x + 1 \quad (x \neq 1)$$

所以当 $x \to 1$ 时，$f(x) \to 2$。但这个"趋向"需要精确定义——这就是 $\epsilon$-$\delta$ 语言的用武之地。

---

## 1. 函数极限的直觉

> **直觉描述**
>
> $\displaystyle\lim_{x \to a} f(x) = L$ 意味着：当 $x$ 充分接近 $a$（但不等于 $a$）时，$f(x)$ 可以任意接近 $L$。

**关键要点**：

1. 我们不关心 $f(a)$ 的值——甚至 $f(a)$ 可以没有定义。极限只关心 $x$ **接近** $a$ 时 $f(x)$ 的行为。
2. $x$ 可以从 $a$ 的左侧或右侧接近 $a$。
3. "任意接近"需要 $\epsilon$-$\delta$ 定义来精确化。

---

## 2. $\epsilon$-$\delta$ 定义 [Bridge]

> **定义 1**（函数极限的 $\epsilon$-$\delta$ 定义）
>
> 设函数 $f$ 在 $a$ 的某个去心邻域内有定义。如果对**任意** $\epsilon > 0$，**存在** $\delta > 0$，使得对**所有**满足 $0 < |x - a| < \delta$ 的 $x$：
>
> $$|f(x) - L| < \epsilon$$
>
> 则称当 $x$ 趋近于 $a$ 时 $f(x)$ 的极限为 $L$，记为
>
> $$\lim_{x \to a} f(x) = L$$

用逻辑符号：

$$\lim_{x \to a} f(x) = L \quad \Longleftrightarrow \quad \forall \epsilon > 0, \; \exists \delta > 0, \; \forall x: \; 0 < |x-a| < \delta \Rightarrow |f(x) - L| < \epsilon$$

![epsilon-delta 定义的几何图示](../../images/p06-ch02-epsilon-delta.png)

### 2.1 与数列极限的对比

| | 数列极限 ($\epsilon$-$N$) | 函数极限 ($\epsilon$-$\delta$) |
|--|--------------------------|-------------------------------|
| 变量 | $n \in \mathbb{N}^*$ | $x \in \mathbb{R}$ |
| 趋向 | $n \to \infty$ | $x \to a$ |
| "充分接近"的表达 | $n > N$ | $0 < \|x - a\| < \delta$ |
| 结论 | $\|a_n - L\| < \epsilon$ | $\|f(x) - L\| < \epsilon$ |
| 排除点 | 无（$n$ 总在 $N$ 之后） | $x = a$（去心邻域） |

核心思想完全相同：**挑战-回应** 模式。

### 2.2 去心邻域

$0 < |x - a| < \delta$ 定义了 $a$ 的**去心 $\delta$-邻域**（deleted $\delta$-neighborhood）：

$$\{x \in \mathbb{R} : 0 < |x - a| < \delta\} = (a - \delta, a) \cup (a, a + \delta)$$

它包含 $a$ 附近的所有点但**排除 $a$ 本身**。这就是为什么极限与 $f(a)$ 的值无关。

---

## 3. 用定义证明极限

### 3.1 证明策略

与 $\epsilon$-$N$ 证明类似：

1. 设 $\epsilon > 0$
2. 分析 $|f(x) - L|$，将其表示为 $|x - a|$ 的函数
3. 找到 $\delta > 0$ 使得 $0 < |x - a| < \delta$ 时 $|f(x) - L| < \epsilon$
4. 验证

> **例题 1**：证明 $\displaystyle\lim_{x \to 2} (3x - 1) = 5$。

> **证明**
>
> 设 $\epsilon > 0$。
>
> $$|f(x) - L| = |(3x - 1) - 5| = |3x - 6| = 3|x - 2|$$
>
> 要使 $3|x - 2| < \epsilon$，只需 $|x - 2| < \epsilon/3$。
>
> 取 $\delta = \epsilon/3$。对所有满足 $0 < |x - 2| < \delta$ 的 $x$：
>
> $$|(3x-1) - 5| = 3|x-2| < 3\delta = 3 \cdot \frac{\epsilon}{3} = \epsilon$$
>
> $\blacksquare$

> **例题 2**：证明 $\displaystyle\lim_{x \to 3} x^2 = 9$。

> **证明**
>
> 设 $\epsilon > 0$。
>
> $$|x^2 - 9| = |x-3||x+3|$$
>
> 需要控制 $|x+3|$。若限制 $|x - 3| < 1$（即 $2 < x < 4$），则 $|x + 3| < 7$。
>
> 因此在 $|x - 3| < 1$ 的条件下：
>
> $$|x^2 - 9| = |x-3| \cdot |x+3| < 7|x-3|$$
>
> 要使 $7|x-3| < \epsilon$，需 $|x-3| < \epsilon/7$。
>
> 取 $\delta = \min(1, \epsilon/7)$。对 $0 < |x-3| < \delta$：
>
> - $|x-3| < 1$，所以 $|x+3| < 7$
> - $|x-3| < \epsilon/7$
>
> 因此 $|x^2 - 9| < 7 \cdot \epsilon/7 = \epsilon$。$\blacksquare$

**技巧总结**：对于非线性函数，先限制 $\delta \leq 1$（或其他方便的常数）以控制"多余因子"，然后取 $\delta = \min(1, \text{所需值})$。

> **例题 3**：证明 $\displaystyle\lim_{x \to 4} \sqrt{x} = 2$。

> **证明**
>
> 设 $\epsilon > 0$。
>
> $$|\sqrt{x} - 2| = \frac{|x - 4|}{|\sqrt{x} + 2|}$$
>
> 由于 $\sqrt{x} + 2 > 2$（$x > 0$ 时），故 $|\sqrt{x} - 2| < \dfrac{|x-4|}{2}$。
>
> 更精确地，若限制 $|x - 4| < 4$（即 $0 < x < 8$），则 $\sqrt{x} > 0$，故 $\sqrt{x} + 2 > 2$。
>
> 取 $\delta = \min(4, 2\epsilon)$。对 $0 < |x - 4| < \delta$：
>
> $$|\sqrt{x} - 2| = \frac{|x-4|}{\sqrt{x}+2} < \frac{\delta}{2} \leq \frac{2\epsilon}{2} = \epsilon$$
>
> $\blacksquare$

---

## 4. 单侧极限（One-sided Limits）

> **定义 2**（右极限）
>
> $\displaystyle\lim_{x \to a^+} f(x) = L$（或 $f(a^+) = L$）意味着：
>
> $$\forall \epsilon > 0, \; \exists \delta > 0, \; \forall x: \; 0 < x - a < \delta \Rightarrow |f(x) - L| < \epsilon$$

> **定义 3**（左极限）
>
> $\displaystyle\lim_{x \to a^-} f(x) = L$（或 $f(a^-) = L$）意味着：
>
> $$\forall \epsilon > 0, \; \exists \delta > 0, \; \forall x: \; 0 < a - x < \delta \Rightarrow |f(x) - L| < \epsilon$$

> **定理 1**（双侧极限与单侧极限的关系）
>
> $$\lim_{x \to a} f(x) = L \quad \Longleftrightarrow \quad \lim_{x \to a^+} f(x) = L \; \text{且} \; \lim_{x \to a^-} f(x) = L$$

**例**：考虑 $f(x) = |x|/x$。

- $\displaystyle\lim_{x \to 0^+} f(x) = 1$（$x > 0$ 时 $f(x) = 1$）
- $\displaystyle\lim_{x \to 0^-} f(x) = -1$（$x < 0$ 时 $f(x) = -1$）
- $\displaystyle\lim_{x \to 0} f(x)$ 不存在（左右极限不相等）

---

## 5. 极限运算法则

> **定理 2**（函数极限的运算法则）
>
> 设 $\lim_{x \to a} f(x) = L$，$\lim_{x \to a} g(x) = M$。则：
>
> 1. **加减法**：$\displaystyle\lim_{x \to a} [f(x) \pm g(x)] = L \pm M$
> 2. **乘法**：$\displaystyle\lim_{x \to a} [f(x) \cdot g(x)] = L \cdot M$
> 3. **常数倍**：$\displaystyle\lim_{x \to a} [c \cdot f(x)] = c \cdot L$
> 4. **除法**：$\displaystyle\lim_{x \to a} \dfrac{f(x)}{g(x)} = \dfrac{L}{M}$（$M \neq 0$）
> 5. **幂**：$\displaystyle\lim_{x \to a} [f(x)]^n = L^n$（$n \in \mathbb{N}^*$）
> 6. **复合**：若 $\lim_{x \to a} g(x) = b$ 且 $f$ 在 $b$ 处连续，则 $\displaystyle\lim_{x \to a} f(g(x)) = f(b)$

**推论**：多项式函数 $p(x)$ 在任何点 $a$ 处的极限就是 $p(a)$：

$$\lim_{x \to a} p(x) = p(a)$$

有理函数 $p(x)/q(x)$ 在 $q(a) \neq 0$ 时同理。

---

## 6. 重要极限

### 6.1 第一重要极限

> **定理 3**（$\sin x / x$ 的极限）
>
> $$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

![sinx/x 的几何论证](../../images/p06-ch02-sinx-over-x.png)

> **证明**（几何夹逼法）
>
> 设 $0 < x < \pi/2$。在单位圆（半径 $r = 1$）中考虑角度 $x$（弧度）。
>
> 比较三个面积：
>
> - **内接三角形** $\triangle OAB$：$A = (1,0)$，$B = (\cos x, \sin x)$，面积 $= \frac{1}{2}\sin x$
> - **扇形** $OAB$：面积 $= \frac{1}{2}x$（扇形面积 $= \frac{1}{2}r^2\theta = \frac{x}{2}$）
> - **外切三角形** $\triangle OAC$：$C = (1, \tan x)$，面积 $= \frac{1}{2}\tan x$
>
> 由面积的包含关系：
>
> $$\frac{1}{2}\sin x \leq \frac{1}{2}x \leq \frac{1}{2}\tan x$$
>
> 各项均正，除以 $\frac{1}{2}\sin x$：
>
> $$1 \leq \frac{x}{\sin x} \leq \frac{1}{\cos x}$$
>
> 取倒数（不等号翻转）：
>
> $$\cos x \leq \frac{\sin x}{x} \leq 1$$
>
> 当 $x \to 0^+$ 时，$\cos x \to 1$。由夹逼定理：
>
> $$\lim_{x \to 0^+} \frac{\sin x}{x} = 1$$
>
> 又因为 $\frac{\sin x}{x} = \frac{\sin(-x)}{-x}$（$\sin$ 是奇函数），左极限也等于 $1$。
>
> 故 $\displaystyle\lim_{x \to 0} \frac{\sin x}{x} = 1$。$\blacksquare$

**相关极限**：

$$\lim_{x \to 0} \frac{\tan x}{x} = 1, \quad \lim_{x \to 0}\frac{1 - \cos x}{x^2} = \frac{1}{2}, \quad \lim_{x \to 0}\frac{\arcsin x}{x} = 1$$

推导 $\lim\frac{1-\cos x}{x^2}$：

$$\frac{1 - \cos x}{x^2} = \frac{1 - \cos x}{x^2}\cdot\frac{1 + \cos x}{1 + \cos x} = \frac{\sin^2 x}{x^2(1+\cos x)} = \left(\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1+\cos x} \to 1 \cdot \frac{1}{2} = \frac{1}{2}$$

### 6.2 第二重要极限

> **定理 4**（$e$ 的连续版本）
>
> $$\lim_{x \to \infty}\left(1 + \frac{1}{x}\right)^x = e$$
>
> 等价地：
>
> $$\lim_{x \to 0}(1 + x)^{1/x} = e$$

此极限的精确证明需要对数函数的连续性和数列极限与函数极限的关系，我们此处暂时接受这一结果。其核心思想是：当 $x$ 取正整数值时，它恰好是第一章中数列 $(1+1/n)^n$ 的值；函数极限是将此结果从整数推广到实数。

**推论**：

$$\lim_{x \to 0}\frac{\ln(1+x)}{x} = 1, \quad \lim_{x \to 0}\frac{e^x - 1}{x} = 1$$

推导第一个：令 $t = \ln(1+x)$，则 $x = e^t - 1$，$x \to 0$ 时 $t \to 0$：

$$\frac{\ln(1+x)}{x} = \frac{t}{e^t - 1}$$

推导第二个：令 $u = e^x - 1$，则 $x = \ln(1+u)$，$x \to 0$ 时 $u \to 0$：

$$\frac{e^x - 1}{x} = \frac{u}{\ln(1+u)}$$

两者互为倒数，且都等于 $1$。

---

## 7. 极限的存在与不存在

不是所有极限都存在。以下是极限不存在的几种典型情况：

### 7.1 左右极限不相等

$$\lim_{x \to 0} \frac{|x|}{x} \quad \text{不存在}$$

如上所述，$f(0^+) = 1$，$f(0^-) = -1$。

### 7.2 无界振荡

$$\lim_{x \to 0} \frac{1}{x} \quad \text{不存在（趋向} \pm\infty\text{）}$$

$x \to 0^+$ 时 $1/x \to +\infty$，$x \to 0^-$ 时 $1/x \to -\infty$。

### 7.3 有界振荡

$$\lim_{x \to 0} \sin\frac{1}{x} \quad \text{不存在}$$

当 $x \to 0$ 时，$1/x \to \infty$，$\sin(1/x)$ 在 $-1$ 和 $1$ 之间无穷次振荡，没有确定的极限值。

**对比**：$\displaystyle\lim_{x \to 0} x \sin\frac{1}{x} = 0$（由夹逼定理：$|x\sin(1/x)| \leq |x| \to 0$）。乘以 $x$ 后，振荡的幅度被压缩到零。

---

## 例题（综合）

> **例题 4**：求 $\displaystyle\lim_{x \to 1} \frac{x^3 - 1}{x - 1}$。

**解**：分子因式分解：$x^3 - 1 = (x-1)(x^2 + x + 1)$。

$$\frac{x^3 - 1}{x-1} = x^2 + x + 1 \quad (x \neq 1)$$

$$\lim_{x \to 1} (x^2 + x + 1) = 1 + 1 + 1 = 3$$

---

> **例题 5**：求 $\displaystyle\lim_{x \to 0} \frac{\sin 5x}{\sin 3x}$。

**解**：

$$\frac{\sin 5x}{\sin 3x} = \frac{\sin 5x}{5x} \cdot \frac{3x}{\sin 3x} \cdot \frac{5x}{3x} = \frac{\sin 5x}{5x} \cdot \frac{3x}{\sin 3x} \cdot \frac{5}{3}$$

当 $x \to 0$：$\dfrac{\sin 5x}{5x} \to 1$，$\dfrac{3x}{\sin 3x} \to 1$。

$$\lim_{x \to 0} \frac{\sin 5x}{\sin 3x} = 1 \cdot 1 \cdot \frac{5}{3} = \frac{5}{3}$$

---

> **例题 6**：求 $\displaystyle\lim_{x \to 0} \frac{e^{2x} - 1}{\sin x}$。

**解**：

$$\frac{e^{2x} - 1}{\sin x} = \frac{e^{2x} - 1}{2x} \cdot \frac{2x}{\sin x} \cdot 1$$

$\dfrac{e^{2x}-1}{2x} \to 1$（令 $u = 2x$，$\dfrac{e^u - 1}{u} \to 1$），$\dfrac{2x}{\sin x} = 2 \cdot \dfrac{x}{\sin x} \to 2$。

$$\lim_{x \to 0} \frac{e^{2x} - 1}{\sin x} = 1 \cdot 2 = 2$$

---

## 要点回顾

| 概念 | 要点 |
|------|------|
| $\epsilon$-$\delta$ 定义 | $\forall \epsilon > 0, \exists \delta > 0, 0 < \|x-a\| < \delta \Rightarrow \|f(x)-L\| < \epsilon$ |
| 与 $\epsilon$-$N$ 的关系 | 核心思想相同（挑战-回应），$N$ 换成 $\delta$，$n > N$ 换成 $0 < \|x-a\| < \delta$ |
| 去心邻域 | $0 < \|x-a\| < \delta$，不包含 $a$ 本身 |
| 单侧极限 | 左极限 $f(a^-)$ 和右极限 $f(a^+)$，两者相等时极限存在 |
| 运算法则 | 加、减、乘、除、复合——对收敛极限成立 |
| $\lim \sin x/x = 1$ | 几何夹逼证明，微积分中最常用的极限 |
| $\lim(1+1/x)^x = e$ | 数列极限 $(1+1/n)^n$ 的连续推广 |
| 极限不存在 | 左右极限不等、无界、有界振荡 |

---

## 进度检查点

完成本节后，你应该能够：

- [ ] 精确陈述 $\epsilon$-$\delta$ 定义，解释与 $\epsilon$-$N$ 的联系
- [ ] 用 $\epsilon$-$\delta$ 定义证明线性函数和简单二次函数的极限
- [ ] 区分极限存在和不存在的各种情况
- [ ] 运用极限运算法则求各种函数的极限
- [ ] 推导 $\lim_{x \to 0}\sin x/x = 1$ 的几何证明
- [ ] 用重要极限求涉及 $\sin$, $\cos$, $e^x$, $\ln$ 的极限

---

## 自测题

**自测题 1**：$\epsilon$-$\delta$ 定义中为什么要求 $0 < |x - a|$ 而不是 $|x - a| < \delta$？

<details>
<summary>答案</summary>

$0 < |x - a|$ 排除了 $x = a$ 的情况。这是因为极限只关心 $f(x)$ 在 $x$ **接近** $a$ 时的行为，而不关心 $f(a)$ 的值——$f(a)$ 甚至可以没有定义。

例如 $f(x) = (x^2-1)/(x-1)$，$f(1)$ 没有定义，但 $\lim_{x \to 1} f(x) = 2$。如果定义中不排除 $x = a$，这个极限就无法讨论。
</details>

**自测题 2**：$\displaystyle\lim_{x \to 0}\sin\frac{1}{x}$ 不存在，但 $\displaystyle\lim_{x \to 0} x\sin\frac{1}{x} = 0$。直觉上如何解释这种差异？

<details>
<summary>答案</summary>

$\sin(1/x)$ 在 $x \to 0$ 时无限振荡（频率趋于无穷），振幅始终为 $1$——振荡不会消失，所以没有极限。

$x\sin(1/x)$ 也在振荡，但振幅被因子 $|x|$ 压缩。$|x| \to 0$ 意味着振幅趋于零——虽然振荡越来越快，但幅度越来越小，被"挤压"到 $0$。这正是夹逼定理的直觉：$-|x| \leq x\sin(1/x) \leq |x|$，两侧都趋于 $0$。
</details>

**自测题 3**：$\displaystyle\lim_{x \to 0}\frac{\tan x}{x} = ?$ 用 $\sin x / x$ 的结果推导。

<details>
<summary>答案</summary>

$$\frac{\tan x}{x} = \frac{\sin x}{x} \cdot \frac{1}{\cos x} \to 1 \cdot \frac{1}{1} = 1$$

用到了极限的乘法法则和 $\cos 0 = 1$。
</details>

**自测题 4**：若 $\lim_{x \to a} f(x) = 3$，$\lim_{x \to a} g(x) = -2$，求 $\lim_{x \to a}[2f(x) - g(x)^2]$。

<details>
<summary>答案</summary>

$$\lim[2f(x) - g(x)^2] = 2 \cdot 3 - (-2)^2 = 6 - 4 = 2$$

用到了常数倍、减法和幂的运算法则。
</details>

---

## 习题引用

本节练习见[练习题](exercises/exercises.md)第 §1 部分。
