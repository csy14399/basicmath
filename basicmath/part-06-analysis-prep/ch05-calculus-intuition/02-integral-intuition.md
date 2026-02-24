# §2 积分的直觉（Integral Intuition）[Bridge]

**前置知识**：[本章 §1 导数的直觉](01-derivative-intuition.md)（导数定义、基本求导）、[Part 6 第 2 章 §1 函数的极限](../ch02-limits/01-function-limits.md)（函数极限）、[Part 6 第 1 章 §1 数列的概念](../ch01-sequences/01-sequence-concepts.md)（求和符号 $\sum$）

**全景图**：导数回答了"曲线有多陡"。积分回答了"曲线下面有多少面积"。这两个问题看似无关，但微积分基本定理揭示了它们之间的深刻联系：微分和积分互为逆运算。本节从面积问题出发，通过 Riemann 和引入定积分的概念，然后给出微积分基本定理的直觉，最后介绍不定积分（反导数）。

**预估学习时间**：约 2–3 小时

> 🌉 本节为 Bridge 内容。严格的 Riemann 积分理论（包括可积条件、Darboux 上下和等）属于大学实分析课程。

---

## 动机

一辆汽车的速度随时间变化，你有一张速度-时间图 $v(t)$。它走过的**总距离**是多少？

如果速度恒定 $v(t) = v_0$，总距离就是 $v_0 \cdot T$——速度乘时间，在图上就是一个**矩形的面积**。

如果速度变化怎么办？关键思路：把时间分成很多小段 $\Delta t$，每段中速度大约不变，距离大约是 $v(t_i)\Delta t$。总距离约为：

$$\text{距离} \approx \sum_{i} v(t_i)\,\Delta t$$

这些小矩形的总面积近似曲线下方的面积。分段越细，近似越精确。取极限——这就是**积分**。

---

## 1. 面积问题（The Area Problem）

### 1.1 什么是"曲线下的面积"？

给定 $f(x) \geq 0$ 在 $[a, b]$ 上的图像，$f$ 的图像、$x$ 轴和两条竖直线 $x = a$, $x = b$ 围成的区域的面积是多少？

对于矩形、三角形，面积有现成的公式。但对一般的曲线——比如 $y = x^2$——如何定义和计算面积？

### 1.2 Archimedes 的思路

Archimedes（前 287–前 212）用**穷竭法**计算了抛物线弓形的面积。他的核心思想是：用越来越精细的多边形（由矩形组成）来逼近曲线区域，当多边形的个数趋于无穷时，多边形的面积趋向曲线区域的面积。

这正是 2000 年后 Riemann 严格化的思路。

---

## 2. Riemann 和（Riemann Sums）

### 2.1 分划与采样

> **定义 1**（分划 / partition）
>
> 区间 $[a, b]$ 的一个**分划** $P$ 是一组点：
>
> $$a = x_0 < x_1 < x_2 < \cdots < x_n = b$$
>
> 它将 $[a, b]$ 分成 $n$ 个子区间 $[x_{i-1}, x_i]$，宽度为 $\Delta x_i = x_i - x_{i-1}$。

> **定义 2**（Riemann 和）
>
> 在每个子区间 $[x_{i-1}, x_i]$ 中选取一个**采样点** $x_i^*$。**Riemann 和** 为：
>
> $$R(f, P) = \sum_{i=1}^{n} f(x_i^*)\,\Delta x_i$$

几何上，$f(x_i^*)\,\Delta x_i$ 是以 $[x_{i-1}, x_i]$ 为底、$f(x_i^*)$ 为高的矩形的面积。Riemann 和是所有这些矩形面积的总和——它近似曲线下的面积。

![Riemann 和示意图](../../images/p06-ch05-riemann-sums.png)

### 2.2 三种常见的 Riemann 和

| 类型 | 采样点 | 特点 |
|------|--------|------|
| **左 Riemann 和** | $x_i^* = x_{i-1}$（左端点） | 对递增函数，是面积的下界 |
| **右 Riemann 和** | $x_i^* = x_i$（右端点） | 对递增函数，是面积的上界 |
| **中点 Riemann 和** | $x_i^* = (x_{i-1}+x_i)/2$ | 通常最精确 |

### 2.3 等距分划

最简单的情况：$n$ 等分，$\Delta x = (b-a)/n$，$x_i = a + i\Delta x$。

**例 1**：用左 Riemann 和估计 $\int_0^1 x^2\,dx$，$n = 4$。

$\Delta x = 1/4$。$x_0 = 0, x_1 = 1/4, x_2 = 1/2, x_3 = 3/4$。

$$L_4 = f(0) \cdot \frac{1}{4} + f(1/4) \cdot \frac{1}{4} + f(1/2) \cdot \frac{1}{4} + f(3/4) \cdot \frac{1}{4}$$

$$= \frac{1}{4}\left(0 + \frac{1}{16} + \frac{1}{4} + \frac{9}{16}\right) = \frac{1}{4} \cdot \frac{14}{16} = \frac{14}{64} = \frac{7}{32} = 0.21875$$

精确值是 $1/3 \approx 0.333$。近似还不太好——需要更多矩形。

$n = 100$ 时，$L_{100} \approx 0.32835$，$R_{100} \approx 0.33835$，中点和 $M_{100} \approx 0.33333$。

---

## 3. 定积分（The Definite Integral）

### 3.1 定义

> **定义 3**（定积分 / definite integral）
>
> 若对所有分划 $P$ 和所有采样点的选择，当分划的最大宽度 $\|P\| = \max_i \Delta x_i \to 0$ 时，Riemann 和收敛于同一个值，则称 $f$ 在 $[a, b]$ 上 **Riemann 可积**，该极限值称为 $f$ 在 $[a, b]$ 上的**定积分**：
>
> $$\int_a^b f(x)\,dx = \lim_{\|P\| \to 0}\sum_{i=1}^{n}f(x_i^*)\,\Delta x_i$$

**记号**：$\int$ 是拉长的 S（Summa），$dx$ 表示无穷小宽度。这是 Leibniz 的天才记号——它暗示积分是"无穷多个无穷小矩形的求和"。

### 3.2 可积性

哪些函数是 Riemann 可积的？大学课程会证明：

> **定理**（Riemann 可积条件——预览）
>
> - 连续函数在闭区间上一定 Riemann 可积。
> - 有界且只有有限多个间断点的函数也是可积的。

### 3.3 定积分的基本性质

| 性质 | 公式 |
|------|------|
| **线性性** | $\int_a^b[cf(x)+g(x)]\,dx = c\int_a^b f\,dx + \int_a^b g\,dx$ |
| **区间可加性** | $\int_a^c f\,dx = \int_a^b f\,dx + \int_b^c f\,dx$（$a < b < c$） |
| **方向** | $\int_b^a f\,dx = -\int_a^b f\,dx$ |
| **保序性** | 若 $f(x) \leq g(x)$，则 $\int_a^b f\,dx \leq \int_a^b g\,dx$ |

---

## 4. 微积分基本定理（Fundamental Theorem of Calculus）

这是微积分最深刻的结果——它将**微分**（导数）和**积分**（面积）联系起来。

### 4.1 FTC 第一部分：导数消除积分

> **定理 1**（FTC Part 1）
>
> 设 $f$ 在 $[a, b]$ 上连续。定义**累积面积函数**：
>
> $$F(x) = \int_a^x f(t)\,dt, \quad x \in [a, b]$$
>
> 则 $F$ 可导，且 $F'(x) = f(x)$。即：
>
> $$\frac{d}{dx}\int_a^x f(t)\,dt = f(x)$$

**直觉**：$F(x)$ 是从 $a$ 到 $x$ 的面积。当 $x$ 增加一点点 $\Delta x$ 时，面积增加大约 $f(x) \cdot \Delta x$（一个薄矩形）。因此：

$$F'(x) = \lim_{\Delta x \to 0}\frac{F(x+\Delta x) - F(x)}{\Delta x} \approx \lim_{\Delta x \to 0}\frac{f(x)\Delta x}{\Delta x} = f(x)$$

**含义**：累积面积函数的变化率就是原函数——微分"撤销"了积分。

### 4.2 FTC 第二部分：积分消除导数

> **定理 2**（FTC Part 2 / Newton-Leibniz 公式）
>
> 设 $f$ 在 $[a, b]$ 上连续，$F$ 是 $f$ 的任意一个**原函数**（即 $F' = f$）。则：
>
> $$\int_a^b f(x)\,dx = F(b) - F(a)$$

**含义**：要计算定积分（面积），只需找到原函数 $F$，然后计算 $F(b) - F(a)$——不需要用 Riemann 和取极限！

这就是微积分的威力：把一个**极限问题**（Riemann 和的极限）转化为一个**代数问题**（找原函数并代入端点）。

记号：$F(b) - F(a)$ 常写作 $F(x)\Big|_a^b$ 或 $[F(x)]_a^b$。

### 4.3 例题

**例 2**：计算 $\displaystyle\int_0^1 x^2\,dx$。

**解**：$f(x) = x^2$ 的原函数 $F(x) = x^3/3$（因为 $(x^3/3)' = x^2$）。

$$\int_0^1 x^2\,dx = \frac{x^3}{3}\bigg|_0^1 = \frac{1}{3} - 0 = \frac{1}{3}$$

验证：这与我们在 Riemann 和中猜测的值一致！

**例 3**：计算 $\displaystyle\int_0^{\pi} \sin x\,dx$。

**解**：$\sin x$ 的原函数是 $-\cos x$。

$$\int_0^{\pi}\sin x\,dx = -\cos x\Big|_0^{\pi} = -\cos\pi - (-\cos 0) = -(-1) + 1 = 2$$

这是半周期正弦波下的面积。

**例 4**：计算 $\displaystyle\int_1^e \frac{1}{x}\,dx$。

**解**：$1/x$ 的原函数是 $\ln x$。

$$\int_1^e \frac{1}{x}\,dx = \ln x\Big|_1^e = \ln e - \ln 1 = 1 - 0 = 1$$

---

## 5. 不定积分（Antiderivatives）

### 5.1 定义

> **定义 4**（不定积分 / antiderivative）
>
> 若 $F'(x) = f(x)$，则称 $F$ 是 $f$ 的**原函数**（antiderivative）。
>
> $f$ 的所有原函数构成的集合记为：
>
> $$\int f(x)\,dx = F(x) + C$$
>
> 其中 $C$ 是任意常数（**积分常数**）。

为什么有 $+C$？如果 $F' = f$，则 $(F + C)' = f$ 对任意常数 $C$ 成立。反过来，若 $F' = G'$，则 $(F-G)' = 0$，所以 $F - G = C$（常数）。因此 $f$ 的所有原函数只差一个常数。

### 5.2 基本不定积分表

| $f(x)$ | $\int f(x)\,dx$ |
|--------|-----------------|
| $x^n$（$n \neq -1$） | $\dfrac{x^{n+1}}{n+1} + C$ |
| $1/x$ | $\ln\|x\| + C$ |
| $e^x$ | $e^x + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |

### 5.3 FTC 的统一视角

FTC 告诉我们微分和积分互为逆运算：

$$\frac{d}{dx}\int_a^x f(t)\,dt = f(x) \quad \text{（微分消除积分）}$$

$$\int_a^b F'(x)\,dx = F(b) - F(a) \quad \text{（积分消除微分）}$$

这就像加法和减法、乘法和除法一样——它们是一对互逆操作。这个发现是 Newton 和 Leibniz 对数学最深刻的贡献。

---

## 例题

**例题 1**：一物体从静止出发，加速度为 $a(t) = 6t$。求 $t = 3$ 时的速度和位移。

**解**：$v(t) = \int a(t)\,dt = \int 6t\,dt = 3t^2 + C$。$v(0) = 0 \Rightarrow C = 0$。$v(3) = 27$。

$s(t) = \int v(t)\,dt = \int 3t^2\,dt = t^3 + C'$。$s(0) = 0 \Rightarrow C' = 0$。$s(3) = 27$。

---

**例题 2**：计算 $\displaystyle\int_0^2 (3x^2 - 2x + 1)\,dx$。

**解**：$F(x) = x^3 - x^2 + x$。

$$\int_0^2 = F(2) - F(0) = (8 - 4 + 2) - 0 = 6$$

---

**例题 3**：求曲线 $y = x^2$ 与 $y = x$ 之间的面积。

**解**：交点：$x^2 = x \Rightarrow x(x-1) = 0$，$x = 0$ 或 $x = 1$。在 $[0, 1]$ 上 $x \geq x^2$。

$$A = \int_0^1 (x - x^2)\,dx = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$$

---

## 要点回顾

| 概念 | 要点 |
|------|------|
| **Riemann 和** | $\sum f(x_i^*)\Delta x_i$——用矩形近似面积 |
| **定积分** | $\int_a^b f\,dx = \lim \sum f(x_i^*)\Delta x_i$ |
| **FTC Part 1** | $\dfrac{d}{dx}\int_a^x f(t)\,dt = f(x)$ |
| **FTC Part 2** | $\int_a^b f(x)\,dx = F(b) - F(a)$（$F' = f$） |
| **不定积分** | $\int f(x)\,dx = F(x) + C$，$F' = f$ |
| **核心联系** | 微分与积分互为逆运算 |

---

## 进度检查点

在继续下一节之前，确认你能够：

- [ ] 用 Riemann 和的语言描述定积分的含义
- [ ] 计算简单函数的左/右 Riemann 和
- [ ] 陈述微积分基本定理的两个部分
- [ ] 用 FTC 计算基本的定积分
- [ ] 解释为什么不定积分有 $+C$
- [ ] 用积分解决面积和物理问题

---

## 自测题

**自测 1**：计算 $\displaystyle\int_1^4 \sqrt{x}\,dx$。

<details>
<summary>答案</summary>

$\sqrt{x} = x^{1/2}$。原函数 $F(x) = \dfrac{x^{3/2}}{3/2} = \dfrac{2}{3}x^{3/2}$。

$$\int_1^4 \sqrt{x}\,dx = \frac{2}{3}(4^{3/2} - 1^{3/2}) = \frac{2}{3}(8 - 1) = \frac{14}{3}$$
</details>

**自测 2**：计算 $\displaystyle\int_0^1 e^x\,dx$。

<details>
<summary>答案</summary>

$$\int_0^1 e^x\,dx = e^x\Big|_0^1 = e - 1 \approx 1.718$$
</details>

**自测 3**：如果 $F(x) = \displaystyle\int_0^x \cos(t^2)\,dt$，求 $F'(x)$。

<details>
<summary>答案</summary>

由 FTC Part 1：$F'(x) = \cos(x^2)$。
</details>

**自测 4**：为什么 $\displaystyle\int_{-1}^{1}\frac{1}{x}\,dx$ 不能直接用 FTC 计算？

<details>
<summary>答案</summary>

$f(x) = 1/x$ 在 $x = 0$ 处无定义（且趋于 $\pm\infty$）。FTC 要求 $f$ 在 $[a, b]$ 上连续，但 $1/x$ 在 $[-1, 1]$ 上不连续。这是一个**瑕积分**（improper integral），需要特殊处理。
</details>

---

## 习题引用

本节的练习题见 [练习题](exercises/exercises.md) 的 §2 部分。
