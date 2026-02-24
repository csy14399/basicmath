# §1 导数的直觉（Derivative Intuition）[Bridge]

**前置知识**：[Part 6 第 2 章 §1 函数的极限](../ch02-limits/01-function-limits.md)（函数极限的定义与计算）、[Part 6 第 3 章 §1 连续函数](../ch03-continuity/01-continuity.md)（连续性的定义）、[Part 4 第 1–4 章](../../part-04-functions/README.md)（初等函数）

**全景图**：导数是微积分的第一个核心概念。直觉上，导数回答了一个简单的几何问题：**曲线在某一点的斜率是多少？** 这个看似简单的问题导向了一个深刻的数学概念——它是极限的一个特殊应用，也是物理学中"瞬时变化率"的数学表达。本节从几何直觉出发定义导数，推导基本函数的导数，陈述求导法则，最后探讨可导与连续的关系。

**预估学习时间**：约 2–3 小时

> 🌉 本节为 Bridge 内容，提供直觉和核心结论。严格的导数理论（包括中值定理、L'Hôpital 法则等）属于大学微积分/分析学课程。

---

## 动机

考虑一辆汽车沿直线行驶。你知道它在每个时刻 $t$ 的位置 $s(t)$。如何计算它在某一时刻的**速度**？

如果汽车匀速运动，$s(t) = vt$，速度就是位移除以时间：$v = s/t$。但现实中的运动不是匀速的——速度在变化。

你可以计算从 $t$ 到 $t + h$ 的**平均速度**：

$$v_{\text{avg}} = \frac{s(t+h) - s(t)}{h}$$

$h$ 越小，平均速度越接近 $t$ 时刻的**瞬时速度**。当 $h \to 0$ 时：

$$v(t) = \lim_{h \to 0}\frac{s(t+h) - s(t)}{h}$$

这就是**导数**——它将"瞬时变化率"这个直觉概念转化为精确的极限定义。

---

## 1. 切线问题（The Tangent Problem）

### 1.1 从割线到切线

给定曲线 $y = f(x)$，过点 $P = (a, f(a))$ 和 $Q = (a+h, f(a+h))$ 的**割线**（secant line）斜率为：

$$k_{\text{sec}} = \frac{f(a+h) - f(a)}{h}$$

这个比值称为 $f$ 在 $a$ 和 $a+h$ 之间的**差商**（difference quotient）。

当 $Q$ 沿曲线趋近 $P$（即 $h \to 0$）时，割线趋近于**切线**（tangent line）。如果极限存在：

$$k_{\text{tan}} = \lim_{h \to 0}\frac{f(a+h) - f(a)}{h}$$

则这就是切线的斜率。

![割线趋近切线](../../images/p06-ch05-secant-to-tangent.png)

### 1.2 几何直觉

- **割线**穿过曲线上的**两个点**，给出区间上的平均变化率
- **切线**只"触碰"曲线在**一个点**，给出该点的瞬时变化率
- 切线是割线的极限位置

---

## 2. 变化率（Rate of Change）

导数不只是几何概念——它度量**任何量的瞬时变化率**：

| 领域 | $f(x)$ | $f'(x)$ |
|------|--------|---------|
| 运动学 | 位置 $s(t)$ | 速度 $v(t)$ |
| 运动学 | 速度 $v(t)$ | 加速度 $a(t)$ |
| 经济学 | 成本 $C(q)$ | 边际成本 |
| 人口学 | 人口 $P(t)$ | 增长率 |
| 温度 | 温度 $T(x)$ | 温度梯度 |

**核心思想**：导数是"变化的变化率"。只要一个量随另一个量变化，就可以谈论它的导数。

---

## 3. 导数的定义（Definition of the Derivative）

> **定义 1**（导数）
>
> 函数 $f$ 在点 $a$ 的**导数**（derivative）定义为：
>
> $$f'(a) = \lim_{h \to 0}\frac{f(a+h) - f(a)}{h}$$
>
> 若此极限存在，则称 $f$ 在 $a$ 处**可导**（differentiable at $a$）。

等价形式（令 $x = a + h$）：

$$f'(a) = \lim_{x \to a}\frac{f(x) - f(a)}{x - a}$$

若 $f$ 在定义域中每一点都可导，则 $f' : x \mapsto f'(x)$ 本身是一个函数，称为 $f$ 的**导函数**（derivative function）。

常用记号：$f'(x)$, $\dfrac{df}{dx}$, $\dfrac{d}{dx}f(x)$, $\dot{f}$（Newton 记号，物理中常用）。

---

## 4. 基本求导（Basic Derivatives）

### 4.1 常数函数

$f(x) = c$。

$$f'(x) = \lim_{h \to 0}\frac{c - c}{h} = 0$$

常数不变化，导数为零。

### 4.2 幂函数

> **定理 1**（幂法则 / power rule）
>
> $(x^n)' = nx^{n-1}$，对所有正整数 $n$ 成立。

**证明**（利用二项式定理）：

$$\frac{(x+h)^n - x^n}{h} = \frac{\sum_{k=0}^{n}\binom{n}{k}x^{n-k}h^k - x^n}{h}$$

$$= \frac{nx^{n-1}h + \binom{n}{2}x^{n-2}h^2 + \cdots + h^n}{h} = nx^{n-1} + \binom{n}{2}x^{n-2}h + \cdots + h^{n-1}$$

令 $h \to 0$，只剩下 $nx^{n-1}$。$\blacksquare$

**例**：$(x^2)' = 2x$，$(x^3)' = 3x^2$，$(x^{100})' = 100x^{99}$。

> 这个公式对**所有实数** $n$ 都成立（$n$ 可以是负数、分数、甚至无理数），但一般情况的证明需要对数微分法，超出本节范围。

### 4.3 正弦函数

> **定理 2**
>
> $(\sin x)' = \cos x$

**证明**：

$$\frac{\sin(x+h) - \sin x}{h} = \frac{\sin x \cos h + \cos x \sin h - \sin x}{h}$$

$$= \sin x \cdot \frac{\cos h - 1}{h} + \cos x \cdot \frac{\sin h}{h}$$

利用 Part 6 Ch02 中的重要极限：$\lim_{h \to 0}\dfrac{\sin h}{h} = 1$ 和 $\lim_{h \to 0}\dfrac{\cos h - 1}{h} = 0$。

$$(\sin x)' = \sin x \cdot 0 + \cos x \cdot 1 = \cos x \qquad \blacksquare$$

类似地可证 $(\cos x)' = -\sin x$。

### 4.4 指数函数

> **定理 3**
>
> $(e^x)' = e^x$

$e^x$ 是唯一（在常数倍意义下）等于自身导数的函数。这个性质也可以作为 $e$ 的定义方式之一。

**证明思路**：

$$\frac{e^{x+h} - e^x}{h} = e^x \cdot \frac{e^h - 1}{h}$$

可以证明 $\lim_{h \to 0}\dfrac{e^h-1}{h} = 1$（利用 $e$ 的定义 $e = \lim(1+1/n)^n$，或 Taylor 展开 $e^h = 1 + h + h^2/2 + \cdots$）。因此 $(e^x)' = e^x$。$\blacksquare$

### 4.5 汇总表

| $f(x)$ | $f'(x)$ | 注释 |
|--------|---------|------|
| $c$（常数） | $0$ | 常数无变化 |
| $x^n$ | $nx^{n-1}$ | 幂法则 |
| $\sin x$ | $\cos x$ | |
| $\cos x$ | $-\sin x$ | 注意负号 |
| $e^x$ | $e^x$ | 自身的导数 |
| $\ln x$ | $1/x$ | $x > 0$ |
| $\tan x$ | $\sec^2 x = 1/\cos^2 x$ | |

---

## 5. 求导法则（Differentiation Rules）

### 5.1 线性性

> $(cf + g)' = cf' + g'$

导数是一个**线性算子**——"求导"与"加法"和"数乘"可交换。

### 5.2 乘积法则（Product Rule / Leibniz Rule）

> $(fg)' = f'g + fg'$

**直觉**：如果 $f$ 和 $g$ 都在变化，$fg$ 的变化来自两部分——$f$ 变化而 $g$ 不动，加上 $g$ 变化而 $f$ 不动。

**例**：$(x^2 \sin x)' = 2x \sin x + x^2 \cos x$。

### 5.3 商法则（Quotient Rule）

> $\displaystyle\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$（$g \neq 0$）

**例**：$(\tan x)' = \left(\dfrac{\sin x}{\cos x}\right)' = \dfrac{\cos x \cdot \cos x - \sin x \cdot (-\sin x)}{\cos^2 x} = \dfrac{1}{\cos^2 x} = \sec^2 x$。

### 5.4 链式法则（Chain Rule）

> 若 $y = f(g(x))$，则 $y' = f'(g(x)) \cdot g'(x)$。
>
> Leibniz 记号：$\dfrac{dy}{dx} = \dfrac{dy}{du} \cdot \dfrac{du}{dx}$（其中 $u = g(x)$）。

**直觉**：如果 $x$ 变化 $\Delta x$，则 $u$ 变化约 $g'(x)\,\Delta x$，然后 $y$ 变化约 $f'(u) \cdot g'(x)\,\Delta x$。

**例**：$(\sin(x^2))' = \cos(x^2) \cdot 2x = 2x\cos(x^2)$。

**例**：$(e^{3x})' = e^{3x} \cdot 3 = 3e^{3x}$。

**例**：$(\ln(\sin x))' = \dfrac{1}{\sin x} \cdot \cos x = \cot x$。

---

## 6. 可导与连续的关系（Differentiability vs Continuity）

### 6.1 可导蕴含连续

> **定理 4**（可导 $\Rightarrow$ 连续）
>
> 若 $f$ 在 $a$ 处可导，则 $f$ 在 $a$ 处连续。

**证明**：

$$\lim_{x \to a}[f(x) - f(a)] = \lim_{x \to a}\frac{f(x)-f(a)}{x-a} \cdot (x-a) = f'(a) \cdot 0 = 0$$

因此 $\lim_{x \to a}f(x) = f(a)$，即 $f$ 在 $a$ 连续。$\blacksquare$

### 6.2 连续不蕴含可导

> ⚠️ 逆命题**不成立**：连续函数不一定可导。

**例**：$f(x) = |x|$ 在 $x = 0$ 处连续但不可导。

**证明**：

$$\lim_{h \to 0^+}\frac{|0+h| - |0|}{h} = \lim_{h \to 0^+}\frac{h}{h} = 1$$

$$\lim_{h \to 0^-}\frac{|0+h| - |0|}{h} = \lim_{h \to 0^-}\frac{-h}{h} = -1$$

左导数 $\neq$ 右导数，极限不存在，$f$ 在 $0$ 处不可导。

几何上，$|x|$ 在 $x = 0$ 处有一个"尖角"——无法唯一定义切线。

![函数及其导数的对比](../../images/p06-ch05-function-derivative-comparison.png)

### 6.3 性质阶梯

$$\text{可导} \implies \text{连续} \implies \text{有极限}$$

每个蕴含都是严格的（不可逆）。在 thinkers-corner 中我们已经看到，Weierstrass 构造了**处处连续但处处不可微**的函数——连续性和可微性之间有巨大的鸿沟。

---

## 例题

**例题 1**：求 $f(x) = x^3 - 4x + 2$ 的导数，并求切线在 $x = 1$ 处的方程。

**解**：$f'(x) = 3x^2 - 4$。$f'(1) = 3 - 4 = -1$。$f(1) = 1 - 4 + 2 = -1$。

切线方程：$y - (-1) = -1 \cdot (x - 1)$，即 $y = -x$。

---

**例题 2**：求 $f(x) = e^x \sin x$ 的导数。

**解**（乘积法则）：$f'(x) = e^x \sin x + e^x \cos x = e^x(\sin x + \cos x)$。

---

**例题 3**：求 $f(x) = \sqrt{1 + x^2}$ 的导数。

**解**（链式法则）：$f(x) = (1+x^2)^{1/2}$。

$f'(x) = \dfrac{1}{2}(1+x^2)^{-1/2} \cdot 2x = \dfrac{x}{\sqrt{1+x^2}}$。

---

**例题 4**：用导数定义直接计算 $f(x) = 1/x$ 的导数。

**解**：

$$f'(x) = \lim_{h \to 0}\frac{1/(x+h) - 1/x}{h} = \lim_{h \to 0}\frac{x - (x+h)}{h \cdot x(x+h)} = \lim_{h \to 0}\frac{-1}{x(x+h)} = -\frac{1}{x^2}$$

---

## 要点回顾

| 概念 | 要点 |
|------|------|
| **导数定义** | $f'(a) = \lim_{h\to 0}(f(a+h)-f(a))/h$ |
| **几何意义** | 切线斜率 |
| **物理意义** | 瞬时变化率 |
| **幂法则** | $(x^n)' = nx^{n-1}$ |
| **三角导数** | $(\sin x)' = \cos x$, $(\cos x)' = -\sin x$ |
| **指数导数** | $(e^x)' = e^x$ |
| **乘积法则** | $(fg)' = f'g + fg'$ |
| **链式法则** | $(f(g(x)))' = f'(g(x)) \cdot g'(x)$ |
| **可导→连续** | 成立，但逆命题不成立（$\|x\|$ 在 $0$ 处） |

---

## 进度检查点

在继续下一节之前，确认你能够：

- [ ] 用极限定义写出导数
- [ ] 解释导数的几何意义（切线斜率）和物理意义（变化率）
- [ ] 用幂法则求多项式的导数
- [ ] 使用乘积法则、商法则和链式法则
- [ ] 证明可导蕴含连续
- [ ] 举出连续但不可导的例子

---

## 自测题

**自测 1**：用导数定义计算 $(x^2)' = 2x$。

<details>
<summary>答案</summary>

$$\frac{(x+h)^2 - x^2}{h} = \frac{x^2 + 2xh + h^2 - x^2}{h} = 2x + h \to 2x$$
</details>

**自测 2**：求 $f(x) = x^3 e^x$ 的导数。

<details>
<summary>答案</summary>

乘积法则：$f'(x) = 3x^2 e^x + x^3 e^x = x^2 e^x(3 + x)$。
</details>

**自测 3**：求 $f(x) = \sin(3x+1)$ 的导数。

<details>
<summary>答案</summary>

链式法则：$f'(x) = \cos(3x+1) \cdot 3 = 3\cos(3x+1)$。
</details>

**自测 4**：$f(x) = |x^3|$ 在 $x = 0$ 处可导吗？

<details>
<summary>答案</summary>

$|x^3| = x^3$（当 $x \geq 0$），$= -x^3$（当 $x < 0$）。

$$\lim_{h \to 0}\frac{|h^3|}{h} = \lim_{h \to 0}\frac{|h|^3}{h}$$

$h > 0$：$h^3/h = h^2 \to 0$。$h < 0$：$(-h)^3/h = -h^2 \to 0$（注意 $h < 0$ 时 $|h|^3/h = -h^2$）。

左右极限都为 $0$，$f'(0) = 0$。**可导**。

（与 $|x|$ 不同——$|x^3|$ 在 $0$ 处足够"平坦"，消除了尖角。）
</details>

---

## 习题引用

本节的练习题见 [练习题](exercises/exercises.md) 的 §1 部分。
