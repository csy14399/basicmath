# §1 数学期望（Expectation）

**前置知识**：[Part 8 第 3 章 随机变量与分布](../ch03-random-variables/README.md)（随机变量、PMF、常见离散分布）

**全景图**：期望（expectation）是随机变量的"平均值"——如果你重复实验无穷多次，观测值的平均值会趋近期望。本节定义期望，推导其最重要的性质——线性性，并介绍 LOTUS（无意识统计学家定律）——一个计算 $g(X)$ 期望的快捷方法。期望的线性性是概率论中最常用的工具之一。

**预估学习时间**：约 3–4 小时

---

## 动机

赌场游戏：掷一个骰子，掷出 $k$ 点赢 $k$ 元。平均每次能赢多少？

$$\frac{1+2+3+4+5+6}{6} = \frac{21}{6} = 3.5 \text{ 元}$$

这个"平均值" $3.5$ 就是随机变量 $X$（骰子点数）的**期望**。注意 $3.5$ 不是 $X$ 的任何一个可能取值——期望是一个**理论量**，表示长期平均。

---

## 1. 期望的定义

### 1.1 定义

> **定义 1**（数学期望 / 均值）
>
> 离散随机变量 $X$（取值 $x_1, x_2, \ldots$）的**数学期望**（mathematical expectation）或**均值**（mean）定义为
>
> $$E[X] = \sum_{i} x_i \cdot P(X = x_i) = \sum_{i} x_i \cdot p_X(x_i)$$
>
> 前提是级数**绝对收敛**（$\sum |x_i| p_X(x_i) < \infty$）。

也常记作 $\mu$、$\mu_X$ 或 $\langle X \rangle$。

### 1.2 直觉

期望是各取值的**加权平均**，权重就是相应的概率。概率大的取值对期望的贡献大。

### 1.3 基本例子

> **例 1**（掷骰子）
>
> $X \sim$ 均匀分布于 $\{1, 2, 3, 4, 5, 6\}$。
>
> $E[X] = \frac{1}{6}(1+2+3+4+5+6) = \frac{21}{6} = 3.5$

> **例 2**（Bernoulli 分布）
>
> $X \sim \text{Bernoulli}(p)$。$E[X] = 0 \cdot (1-p) + 1 \cdot p = p$。

> **例 3**（有偏骰子）
>
> $P(X = 6) = 1/2$，$P(X = k) = 1/10$（$k = 1,2,3,4,5$）。
>
> $E[X] = \frac{1}{10}(1+2+3+4+5) + \frac{1}{2} \times 6 = \frac{15}{10} + 3 = 4.5$
>
> 有偏骰子的期望（$4.5$）比公平骰子的期望（$3.5$）大，因为大点数 $6$ 出现的概率更高。

---

## 2. 期望的线性性（Linearity of Expectation）

### 2.1 基本性质

> **定理 1**（线性性）
>
> 对任意随机变量 $X, Y$ 和常数 $a, b, c$：
>
> **(a) 常数的期望**：$E[c] = c$
>
> **(b) 齐次性**：$E[aX] = aE[X]$
>
> **(c) 可加性**：$E[X + Y] = E[X] + E[Y]$
>
> **(d) 仿射变换**：$E[aX + b] = aE[X] + b$

### 2.2 可加性的证明（有限情况）

设 $X, Y$ 在有限样本空间 $\Omega = \{\omega_1, \ldots, \omega_N\}$ 上。

$$E[X + Y] = \sum_{i=1}^{N} (X(\omega_i) + Y(\omega_i)) \cdot P(\{\omega_i\})$$

$$= \sum_{i=1}^{N} X(\omega_i) P(\{\omega_i\}) + \sum_{i=1}^{N} Y(\omega_i) P(\{\omega_i\}) = E[X] + E[Y] \quad \blacksquare$$

### 2.3 关键特性：不需要独立性

> **定理 1 的可加性对任意随机变量成立——即使 $X$ 和 $Y$ 不独立！**

这是期望线性性最强大的方面。无论 $X$ 和 $Y$ 之间有多复杂的相关关系，$E[X+Y] = E[X] + E[Y]$ 总是成立。

### 2.4 推广到多个随机变量

$$E[a_1 X_1 + a_2 X_2 + \cdots + a_n X_n] = a_1 E[X_1] + a_2 E[X_2] + \cdots + a_n E[X_n]$$

> **例 4**（指示器变量法求二项分布均值）
>
> 设 $X \sim B(n, p)$。$X = X_1 + X_2 + \cdots + X_n$，其中 $X_i \sim \text{Bernoulli}(p)$。
>
> $E[X] = E[X_1] + E[X_2] + \cdots + E[X_n] = np$
>
> 不需要任何复杂计算！

> **例 5**（帽子问题 / 匹配问题）
>
> $n$ 个人随机拿回帽子（每人等可能拿到任一顶帽子）。$X$ = 拿到自己帽子的人数。求 $E[X]$。

**解**：设 $X_i = 1$ 当第 $i$ 个人拿到自己的帽子，$X_i = 0$ 否则。

$E[X_i] = P(\text{第 $i$ 人拿对}) = 1/n$。

$X = X_1 + X_2 + \cdots + X_n$。

$$E[X] = \sum_{i=1}^{n} E[X_i] = n \cdot \frac{1}{n} = 1$$

不论 $n$ 多大，平均恰好有 $1$ 人拿到自己的帽子！

注意 $X_i$ 之间**不独立**（一个人拿了某顶帽子影响其他人），但线性性仍然适用。$\blacksquare$

---

## 3. LOTUS（Law of the Unconscious Statistician）

### 3.1 问题

如果 $Y = g(X)$，如何计算 $E[Y]$？

**直接方法**：先求 $Y$ 的 PMF，再用定义。这可能很麻烦。

**LOTUS**：不需要求 $Y$ 的 PMF！

### 3.2 定理

> **定理 2**（LOTUS / 无意识统计学家定律）
>
> 设 $X$ 是离散随机变量，$g: \mathbb{R} \to \mathbb{R}$。则
>
> $$E[g(X)] = \sum_{x} g(x) \cdot p_X(x)$$

名字的来历：很多人"无意识地"使用这个公式，以为它是期望的定义——但它其实是一个需要证明的定理。

> **例 6**（LOTUS 应用）
>
> $X$ 均匀分布于 $\{1, 2, 3, 4\}$。求 $E[X^2]$。

**解**：$E[X^2] = \frac{1}{4}(1^2 + 2^2 + 3^2 + 4^2) = \frac{1+4+9+16}{4} = \frac{30}{4} = 7.5$

注意 $E[X^2] = 7.5 \neq (E[X])^2 = 2.5^2 = 6.25$。一般来说，$E[g(X)] \neq g(E[X])$。$\blacksquare$

### 3.3 两个变量的 LOTUS

$$E[g(X, Y)] = \sum_{x} \sum_{y} g(x, y) \cdot p_{X,Y}(x, y)$$

### 3.4 独立随机变量乘积的期望

> **定理 3**：若 $X$ 和 $Y$ **独立**，则
>
> $$E[XY] = E[X] \cdot E[Y]$$

**证明**：

$$E[XY] = \sum_x \sum_y xy \cdot p_{X,Y}(x,y) = \sum_x \sum_y xy \cdot p_X(x) p_Y(y) = \left(\sum_x x \cdot p_X(x)\right)\left(\sum_y y \cdot p_Y(y)\right) = E[X] \cdot E[Y]$$

**注意**：$E[XY] = E[X]E[Y]$ 需要独立性（或更弱的不相关性）。不独立时一般不成立。

---

## 4. 条件期望（简介）

> **定义 2**（条件期望）
>
> $$E[X \mid B] = \sum_x x \cdot P(X = x \mid B)$$

**全期望公式**（Law of Total Expectation）：

$$E[X] = \sum_i E[X \mid B_i] \cdot P(B_i)$$

（$B_1, B_2, \ldots$ 是划分。）

> **例 7**
>
> 掷一枚公平硬币。正面赢 $10$ 元，反面再掷一个骰子，赢骰子点数的元。求期望赢利。

**解**：$E[\text{赢利} \mid H] = 10$，$E[\text{赢利} \mid T] = E[\text{骰子}] = 3.5$。

$E[\text{赢利}] = 10 \times 0.5 + 3.5 \times 0.5 = 6.75$ 元。$\blacksquare$

---

## 例题

> **例题 1**
>
> $X$ 的 PMF 为 $p(-1) = 0.2$，$p(0) = 0.3$，$p(1) = 0.4$，$p(2) = 0.1$。求 $E[X]$ 和 $E[3X - 2]$。

**解**：$E[X] = (-1)(0.2) + 0(0.3) + 1(0.4) + 2(0.1) = -0.2 + 0 + 0.4 + 0.2 = 0.4$。

$E[3X - 2] = 3E[X] - 2 = 3(0.4) - 2 = -0.8$。$\blacksquare$

> **例题 2**
>
> 从 $52$ 张牌中随机抽 $13$ 张。设 $X$ = 抽到的 A 的张数。用指示器变量法求 $E[X]$。

**解**：$X = X_1 + X_2 + X_3 + X_4$，其中 $X_i = 1$ 当第 $i$ 张 A 在抽到的 $13$ 张中。

$P(X_i = 1) = 13/52 = 1/4$（对称性：任意一张牌在 $13$ 张中的概率都是 $13/52$）。

$E[X] = 4 \times 1/4 = 1$。$\blacksquare$

> **例题 3**
>
> $X \sim \text{Poi}(\lambda)$。用 LOTUS 计算 $E[X(X-1)]$。

**解**：

$$E[X(X-1)] = \sum_{k=0}^{\infty} k(k-1) \frac{\lambda^k e^{-\lambda}}{k!} = \sum_{k=2}^{\infty} \frac{\lambda^k e^{-\lambda}}{(k-2)!} = \lambda^2 e^{-\lambda} \sum_{j=0}^{\infty} \frac{\lambda^j}{j!} = \lambda^2$$

因此 $E[X^2] = E[X(X-1)] + E[X] = \lambda^2 + \lambda$。$\blacksquare$

---

## 要点回顾

| 概念 | 要点 |
|------|------|
| 期望 $E[X]$ | 取值的加权平均，权重为概率 |
| 线性性 | $E[aX+bY+c] = aE[X]+bE[Y]+c$，**不需要独立** |
| LOTUS | $E[g(X)] = \sum g(x) p_X(x)$，不需要求 $g(X)$ 的分布 |
| 独立时 | $E[XY] = E[X]E[Y]$ |
| $E[g(X)] \neq g(E[X])$ | 一般情况下成立（Jensen 不等式的根源） |

---

## 进度检查点

完成本节后，你应该能够：

- [ ] 从 PMF 计算期望
- [ ] 运用线性性简化多个随机变量之和的期望
- [ ] 使用指示器变量法解决计数类期望问题
- [ ] 用 LOTUS 计算 $g(X)$ 的期望
- [ ] 区分何时可以使用 $E[XY] = E[X]E[Y]$

---

## 自测题

**题 1**：$X \sim B(100, 0.3)$。$E[X]$？

<details>
<summary>答案</summary>

$E[X] = np = 100 \times 0.3 = 30$。
</details>

**题 2**：$X$ 均匀取 $\{1, 2, \ldots, n\}$。$E[X]$？

<details>
<summary>答案</summary>

$E[X] = \frac{1}{n} \sum_{k=1}^{n} k = \frac{1}{n} \cdot \frac{n(n+1)}{2} = \frac{n+1}{2}$。
</details>

**题 3**：$X_1, X_2, X_3$ 独立，$E[X_i] = 2$。$E[X_1 + 2X_2 - X_3]$？

<details>
<summary>答案</summary>

$E[X_1 + 2X_2 - X_3] = E[X_1] + 2E[X_2] - E[X_3] = 2 + 4 - 2 = 4$。
</details>

**题 4**：$X$ 均匀取 $\{-2, -1, 0, 1, 2\}$。$E[X]$ 和 $E[X^2]$？

<details>
<summary>答案</summary>

$E[X] = (-2-1+0+1+2)/5 = 0$（对称分布）。

$E[X^2] = (4+1+0+1+4)/5 = 10/5 = 2$。
</details>

---

## 习题引用

本节的练习见 [exercises/exercises.md](exercises/exercises.md)。
