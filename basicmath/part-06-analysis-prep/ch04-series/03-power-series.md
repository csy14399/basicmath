# §3 幂级数初步（Introduction to Power Series）[Bridge]

**前置知识**：[本章 §1 无穷级数](01-series.md)（级数收敛的定义、几何级数）、[本章 §2 收敛判别法](02-convergence-tests.md)（比值判别法、根值判别法、绝对收敛）、[Part 4 第 2 章 指数与对数](../../part-04-functions/ch02-exp-log/README.md)（$e^x$ 的定义）、[Part 4 第 3 章 三角函数](../../part-04-functions/ch03-trigonometry/README.md)（$\sin x$, $\cos x$）

**全景图**：前两节研究了数值级数——每一项都是一个固定的数。本节进入**幂级数**的世界：每一项含有变量 $x$，级数的和成为 $x$ 的函数。幂级数是连接代数与分析的桥梁——它让我们用多项式（最简单的函数）去逼近复杂的函数。Taylor 展开把 $e^x$、$\sin x$、$\ln(1+x)$ 等超越函数表示为无穷多项式，这是微积分和分析学最强大的工具之一。

**预估学习时间**：约 2–3 小时

> 🌉 **Bridge 标记**：幂级数和 Taylor 展开的严格理论属于大学分析学。本节提供直觉和核心结论，不给出所有证明。

---

## 动机

回顾几何级数：

$$\frac{1}{1-x} = 1 + x + x^2 + x^3 + \cdots = \sum_{n=0}^{\infty}x^n, \quad |x| < 1$$

右边是一个无穷多项式（幂级数）。令人惊奇的是，许多函数都可以写成这样的形式：

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$$

这些展开式（Taylor 级数）不仅在理论上揭示了函数的深层结构，在实际计算中也极其有用——计算器就是用 Taylor 多项式来计算 $e^x$、$\sin x$ 等值的。

---

## 1. 幂级数（Power Series）

### 1.1 定义

> **定义 1**（幂级数 / power series）
>
> 形如
>
> $$\sum_{n=0}^{\infty}a_n x^n = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \cdots$$
>
> 的级数称为以 $0$ 为中心（centered at $0$）的**幂级数**，其中 $a_0, a_1, a_2, \ldots$ 为给定的常数（称为**系数**），$x$ 是变量。
>
> 更一般地，以 $c$ 为中心的幂级数为：
>
> $$\sum_{n=0}^{\infty}a_n(x-c)^n$$

对于固定的 $x$ 值，幂级数变成一个数值级数，可能收敛也可能发散。因此，核心问题是：**对哪些 $x$ 值，幂级数收敛？**

### 1.2 几何级数作为幂级数

最简单的幂级数就是几何级数 $\sum x^n$（$a_n = 1$）：

$$\sum_{n=0}^{\infty}x^n = \frac{1}{1-x}, \quad |x| < 1$$

- $x = 0.5$：$\sum (0.5)^n = 2$ ✓
- $x = -0.3$：$\sum (-0.3)^n = 1/1.3 \approx 0.769$ ✓
- $x = 1$：$\sum 1^n = 1 + 1 + 1 + \cdots$ 发散 ✗
- $x = -1$：$\sum (-1)^n = 1 - 1 + 1 - \cdots$ 发散 ✗

收敛范围是开区间 $(-1, 1)$。数 $R = 1$ 称为**收敛半径**。

---

## 2. 收敛半径（Radius of Convergence）

### 2.1 Cauchy-Hadamard 定理

> **定理 1**（Cauchy-Hadamard 定理）
>
> 对幂级数 $\sum a_n x^n$，存在一个数 $R \in [0, \infty]$（**收敛半径**），使得：
>
> - $|x| < R$ 时级数**绝对收敛**；
> - $|x| > R$ 时级数**发散**；
> - $|x| = R$ 时**不确定**（需逐点判断）。
>
> 收敛半径由 Cauchy-Hadamard 公式给出：
>
> $$\frac{1}{R} = \limsup_{n \to \infty}|a_n|^{1/n}$$

直觉：幂级数在以 $0$ 为中心、$R$ 为半径的**收敛区间** $(-R, R)$ 内绝对收敛，在 $(-R, R)$ 外发散，在端点 $x = \pm R$ 处需要单独分析。

![收敛半径示意图](../../images/p06-ch04-convergence-radius.png)

### 2.2 用比值法求收敛半径

在实际应用中，比值法更常用：

> **公式**：若 $\displaystyle\lim_{n \to \infty}\left|\frac{a_{n+1}}{a_n}\right|$ 存在，则
>
> $$R = \lim_{n \to \infty}\left|\frac{a_n}{a_{n+1}}\right|$$

**推导**：对 $\sum a_n x^n$，由比值判别法，级数收敛当

$$\lim\left|\frac{a_{n+1}x^{n+1}}{a_n x^n}\right| = |x| \cdot \lim\left|\frac{a_{n+1}}{a_n}\right| < 1$$

即 $|x| < 1/\lim|a_{n+1}/a_n| = \lim|a_n/a_{n+1}|$。

**例 1**：求 $\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{n!}$ 的收敛半径。

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{1/(n+1)!}{1/n!} = \frac{1}{n+1} \to 0$$

$R = 1/0 = \infty$。级数对**所有** $x$ 收敛。

**例 2**：求 $\displaystyle\sum_{n=0}^{\infty}n! \cdot x^n$ 的收敛半径。

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{(n+1)!}{n!} = n + 1 \to \infty$$

$R = 0$。级数仅在 $x = 0$ 处收敛。

**例 3**：求 $\displaystyle\sum_{n=1}^{\infty}\frac{x^n}{n}$ 的收敛半径和收敛区间。

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{n}{n+1} \to 1$$

$R = 1$。收敛区间为 $(-1, 1)$，但端点需另外检查：

- $x = 1$：$\sum 1/n$（调和级数），发散。
- $x = -1$：$\sum (-1)^n/n$（交错调和级数），收敛。

所以收敛域为 $[-1, 1)$。

**例 4**：求 $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n}}{(2n)!}$ 的收敛半径。

这不是标准形式（含 $x^{2n}$ 而非 $x^n$）。令 $u = x^2$，级数变为 $\sum (-1)^n u^n/(2n)!$。

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{(2n)!}{(2n+2)!} = \frac{1}{(2n+1)(2n+2)} \to 0$$

$R_u = \infty$，即 $|u| = |x^2| < \infty$，$R = \infty$。级数对所有 $x$ 收敛。

---

## 3. Taylor 展开的直觉（Intuition for Taylor Expansion）

### 3.1 用多项式逼近函数

如果一个函数 $f(x)$ 在 $x = 0$ 处"足够光滑"（各阶导数存在），我们可以用多项式来逼近它。

**零阶逼近**：$P_0(x) = f(0)$（水平线）
**一阶逼近**：$P_1(x) = f(0) + f'(0)x$（切线）
**二阶逼近**：$P_2(x) = f(0) + f'(0)x + \frac{f''(0)}{2}x^2$（抛物线）

一般地，$n$ 阶 Taylor 多项式为：

$$P_n(x) = \sum_{k=0}^{n}\frac{f^{(k)}(0)}{k!}x^k$$

当 $n \to \infty$ 时，如果 $P_n(x) \to f(x)$，我们就得到了 $f$ 的 **Taylor 级数**：

$$f(x) = \sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n$$

### 3.2 为什么系数是 $f^{(n)}(0)/n!$？

如果 $f(x) = \sum a_n x^n$，逐次对 $x$ 求导并令 $x = 0$：

- $f(0) = a_0$
- $f'(0) = a_1$
- $f''(0) = 2a_2$，所以 $a_2 = f''(0)/2!$
- $f'''(0) = 6a_3$，所以 $a_3 = f'''(0)/3!$
- 一般地：$a_n = f^{(n)}(0)/n!$

这就是 Taylor 系数的由来。

---

## 4. 重要的 Taylor 展开

以下是最重要的 Taylor 级数（以 $x = 0$ 为中心，即 Maclaurin 级数）：

### 4.1 指数函数

$$e^x = \sum_{n=0}^{\infty}\frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots, \quad R = \infty$$

**验证**：$f(x) = e^x$ 满足 $f^{(n)}(x) = e^x$，所以 $f^{(n)}(0) = 1$。

$$a_n = \frac{f^{(n)}(0)}{n!} = \frac{1}{n!}$$

取 $x = 1$：$e = 1 + 1 + 1/2 + 1/6 + 1/24 + \cdots \approx 2.71828\ldots$

### 4.2 正弦函数

$$\sin x = \sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots, \quad R = \infty$$

**验证**：$\sin^{(k)}(0)$ 的循环模式为 $0, 1, 0, -1, 0, 1, \ldots$，只有奇数阶导数非零。

### 4.3 余弦函数

$$\cos x = \sum_{n=0}^{\infty}\frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots, \quad R = \infty$$

### 4.4 几何级数

$$\frac{1}{1-x} = \sum_{n=0}^{\infty}x^n = 1 + x + x^2 + x^3 + \cdots, \quad R = 1$$

### 4.5 自然对数

$$\ln(1+x) = \sum_{n=1}^{\infty}\frac{(-1)^{n+1}x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots, \quad R = 1$$

收敛域为 $(-1, 1]$（$x = 1$ 处收敛于 $\ln 2$，$x = -1$ 处发散）。

**推导思路**：注意 $\dfrac{d}{dx}\ln(1+x) = \dfrac{1}{1+x} = \dfrac{1}{1-(-x)} = \sum (-x)^n = \sum (-1)^n x^n$。逐项积分得 $\ln(1+x) = \sum (-1)^n x^{n+1}/(n+1)$。

### 4.6 汇总表

| 函数 | Taylor 展开 | 收敛半径 |
|------|------------|----------|
| $e^x$ | $\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{n!}$ | $R = \infty$ |
| $\sin x$ | $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{(2n+1)!}$ | $R = \infty$ |
| $\cos x$ | $\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n}}{(2n)!}$ | $R = \infty$ |
| $\dfrac{1}{1-x}$ | $\displaystyle\sum_{n=0}^{\infty}x^n$ | $R = 1$ |
| $\ln(1+x)$ | $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}x^n}{n}$ | $R = 1$ |

---

## 5. Taylor 多项式逼近（Taylor Polynomial Approximation）

Taylor 多项式 $P_n(x)$ 是函数 $f(x)$ 在 $x = 0$ 附近的 $n$ 阶逼近。$n$ 越大，逼近越精确。

![Taylor 多项式逐步逼近](../../images/p06-ch04-taylor-approximation.png)

**$\sin x$ 的逐步逼近**：

| $n$（阶数） | $P_n(x)$ | 在 $x = 1$ 处的值 | $\sin 1 \approx 0.84147$ |
|------------|----------|-------------------|--------------------------|
| 1 | $x$ | $1.000$ | 误差 $0.159$ |
| 3 | $x - x^3/6$ | $0.833$ | 误差 $0.008$ |
| 5 | $x - x^3/6 + x^5/120$ | $0.8417$ | 误差 $0.0002$ |
| 7 | 含 $x^7$ 项 | $0.841471$ | 误差 $< 10^{-5}$ |

逼近速度惊人！只需几项就能得到高精度的近似值。

### 5.1 为什么 Taylor 逼近如此有效？

Taylor 多项式 $P_n(x)$ 被设计为在 $x = 0$ 处与 $f(x)$ 共享前 $n$ 阶导数。这意味着 $P_n$ 不仅在 $x = 0$ 处的值正确，而且"弯曲方式"也尽可能接近 $f$。

形式化地，误差（余项）满足：

$$|f(x) - P_n(x)| \leq \frac{M_{n+1}}{(n+1)!}|x|^{n+1}$$

其中 $M_{n+1} = \max|f^{(n+1)}|$。分母的 $(n+1)!$ 增长极快，使得误差迅速衰减。

### 5.2 应用：近似计算

**例 5**：用 Taylor 多项式估计 $e^{0.1}$。

$$e^{0.1} \approx 1 + 0.1 + \frac{0.01}{2} + \frac{0.001}{6} = 1 + 0.1 + 0.005 + 0.000167 = 1.105167$$

精确值 $e^{0.1} \approx 1.10517$，误差 $< 10^{-6}$。

**例 6**：用 Taylor 多项式估计 $\cos(0.5)$。

$$\cos(0.5) \approx 1 - \frac{0.25}{2} + \frac{0.0625}{24} = 1 - 0.125 + 0.00260 = 0.87760$$

精确值 $\approx 0.87758$，误差 $< 10^{-4}$。

---

## 例题

**例题 1**：求 $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}x^n}{n \cdot 2^n}$ 的收敛半径和收敛域。

**解**：$a_n = \dfrac{(-1)^{n+1}}{n \cdot 2^n}$。

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{n}{(n+1)} \cdot \frac{1}{2} \to \frac{1}{2}$$

$R = 2$。检查端点：
- $x = 2$：$\sum (-1)^{n+1}/n$ 收敛（交错调和级数）。
- $x = -2$：$\sum (-1)^{n+1}(-1)^n/n = \sum -1/n$ 发散。

收敛域为 $(-2, 2]$。

级数实际上是 $\ln(1+x/2)$（将 $\ln(1+t)$ 中的 $t$ 换为 $x/2$）。

---

**例题 2**：证明 $\displaystyle e = \sum_{n=0}^{\infty}\frac{1}{n!}$，并估计前 $10$ 项近似值的精度。

**解**：取 $x = 1$ 代入 $e^x$ 的 Taylor 展开：$e = e^1 = \sum 1/n!$。

前 $10$ 项（$n = 0, \ldots, 9$）：

$$S_9 = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \frac{1}{24} + \frac{1}{120} + \frac{1}{720} + \frac{1}{5040} + \frac{1}{40320} + \frac{1}{362880} \approx 2.718282$$

误差 $|e - S_9| \leq \sum_{n=10}^{\infty}1/n! < 1/10! \cdot \sum_{k=0}^{\infty}(1/11)^k = \frac{1}{10!} \cdot \frac{11}{10} < 3 \times 10^{-7}$。

---

**例题 3**：利用 $\ln(1+x) = \sum (-1)^{n+1}x^n/n$ 计算 $\ln 2$ 的近似值。

**解**：取 $x = 1$：

$$\ln 2 = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \cdots$$

前 $10$ 项：$\ln 2 \approx 0.6456$。前 $100$ 项：$\ln 2 \approx 0.6882$。收敛很慢！

更好的策略：取 $x = 1/3$，计算 $\ln(4/3)$，级数收敛更快。或利用 $\ln 2 = 2\,\mathrm{arctanh}(1/3)$。

---

## 要点回顾

| 概念 | 要点 |
|------|------|
| **幂级数** | $\sum a_n x^n$，和是 $x$ 的函数 |
| **收敛半径** | $R$：$\|x\| < R$ 绝对收敛，$\|x\| > R$ 发散 |
| **比值求 $R$** | $R = \lim\|a_n/a_{n+1}\|$ |
| **Taylor 展开** | $f(x) = \sum f^{(n)}(0)/n! \cdot x^n$ |
| **五大展开** | $e^x$, $\sin x$, $\cos x$, $1/(1-x)$, $\ln(1+x)$ |
| **逼近质量** | 误差 $\sim \|x\|^{n+1}/(n+1)!$，快速衰减 |

---

## 进度检查点

在结束本章之前，确认你能够：

- [ ] 写出幂级数的定义并解释收敛半径的含义
- [ ] 用比值法或根值法计算收敛半径
- [ ] 检查端点的收敛性
- [ ] 默写五大 Taylor 展开及其收敛半径
- [ ] 用 Taylor 多项式近似计算函数值
- [ ] 解释 Taylor 逼近为什么如此有效

---

## 自测题

**自测 1**：求 $\displaystyle\sum_{n=0}^{\infty}\frac{n \cdot x^n}{3^n}$ 的收敛半径。

<details>
<summary>答案</summary>

$a_n = n/3^n$。$\left|\dfrac{a_{n+1}}{a_n}\right| = \dfrac{n+1}{n} \cdot \dfrac{1}{3} \to \dfrac{1}{3}$。

$R = 3$。
</details>

**自测 2**：写出 $e^{-x}$ 的 Taylor 展开。

<details>
<summary>答案</summary>

将 $e^x = \sum x^n/n!$ 中的 $x$ 换为 $-x$：

$$e^{-x} = \sum_{n=0}^{\infty}\frac{(-1)^n x^n}{n!} = 1 - x + \frac{x^2}{2!} - \frac{x^3}{3!} + \cdots, \quad R = \infty$$
</details>

**自测 3**：$\displaystyle\sum_{n=0}^{\infty}n!\,x^n$ 的收敛半径是多少？

<details>
<summary>答案</summary>

$\left|\dfrac{a_{n+1}}{a_n}\right| = n + 1 \to \infty$。$R = 0$。级数仅在 $x = 0$ 处收敛。
</details>

**自测 4**：用 $\sin x$ 的 Taylor 展开估计 $\sin(0.1)$，只取前两项。

<details>
<summary>答案</summary>

$\sin(0.1) \approx 0.1 - \dfrac{0.001}{6} = 0.1 - 0.000167 = 0.099833$。

精确值 $\sin(0.1) \approx 0.099833$，非常精确。
</details>

**自测 5**：$\ln(1+x)$ 的 Taylor 展开在 $x = 1$ 处收敛于什么值？

<details>
<summary>答案</summary>

$\ln(1+1) = \ln 2 \approx 0.6931$。即 $\sum_{n=1}^{\infty}(-1)^{n+1}/n = \ln 2$。

注意 $x = 1$ 是收敛域的端点——级数确实在此收敛，但收敛非常缓慢。
</details>

---

## 习题引用

本节的练习题见 [练习题](exercises/exercises.md) 的 §3 部分。
