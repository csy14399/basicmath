# 第 3 章 二项式定理 — 思考者角落（Thinker's Corner）

> 本节超越教材的核心内容，带你看看二项式定理背后更广阔的风景。这里没有考试，只有好奇心。

---

## 1. 从二项式到形式幂级数

### 多项式的"无穷版"

在代数中，**形式幂级数**（formal power series）是"无限长的多项式"：

$$f(x) = \sum_{n=0}^{\infty} a_n x^n$$

与分析学中的幂级数不同，形式幂级数不关心收敛性——它只是一种代数对象，用系数序列 $(a_0, a_1, a_2, \ldots)$ 完全确定。

形式幂级数可以做加法、乘法、甚至取逆（如果 $a_0 \neq 0$）。Newton 的广义二项式定理

$$(1+x)^\alpha = \sum_{k=0}^{\infty}\binom{\alpha}{k}x^k$$

在形式幂级数的框架下不需要讨论收敛性——它就是一个代数恒等式。

### 组合数学中的应用

形式幂级数是**生成函数**（generating function）的数学基础。许多组合恒等式可以在形式幂级数环 $\mathbb{R}[[x]]$ 中优雅地证明。

---

## 2. $q$-二项式系数

### 从计数到多项式

将二项式系数 $\binom{n}{k}$ 推广为关于参数 $q$ 的多项式：

$$\binom{n}{k}_q = \frac{[n]_q!}{[k]_q! \cdot [n-k]_q!}$$

其中 $[n]_q = 1 + q + q^2 + \cdots + q^{n-1} = \frac{q^n - 1}{q - 1}$ 是 **$q$-整数**，$[n]_q! = [1]_q [2]_q \cdots [n]_q$。

当 $q \to 1$ 时，$[n]_q \to n$，$\binom{n}{k}_q \to \binom{n}{k}$。

### 组合意义

$\binom{n}{k}_q$ 计算的是 $\mathbb{F}_q^n$（$q$ 元有限域上的 $n$ 维向量空间）中 $k$ 维子空间的个数。当 $q = 1$ 时（"$1$ 元域"，只有一种选择），退化为集合的子集计数 $\binom{n}{k}$。

$q$-二项式系数满足 $q$-Pascal 恒等式：

$$\binom{n}{k}_q = \binom{n-1}{k-1}_q + q^k \binom{n-1}{k}_q$$

以及 $q$-二项式定理：

$$\prod_{i=0}^{n-1}(1 + q^i x) = \sum_{k=0}^{n}\binom{n}{k}_q q^{\binom{k}{2}} x^k$$

---

## 3. 中心二项式系数与 $\pi$

### $\binom{2n}{n}$ 的渐近

中心二项式系数 $\binom{2n}{n}$ 是 Pascal 三角形第 $2n$ 行的最大值。由 Stirling 近似：

$$\binom{2n}{n} \sim \frac{4^n}{\sqrt{\pi n}}$$

这个结果与 $\pi$ 的联系令人惊叹——一个纯离散的组合量竟然与圆周率有关。

### Wallis 公式

$$\frac{\pi}{2} = \prod_{n=1}^{\infty}\frac{4n^2}{4n^2 - 1} = \frac{2}{1}\cdot\frac{2}{3}\cdot\frac{4}{3}\cdot\frac{4}{5}\cdot\frac{6}{5}\cdot\frac{6}{7}\cdots$$

这可以通过 $\binom{2n}{n}$ 和 Beta 函数推导——组合数学、分析学和 $\pi$ 在这里完美交融。

---

## 4. 从 Pascal 三角形到分形

### Sierpiński 三角形

将 Pascal 三角形中的每个数取模 $2$（奇数 $\to$ 黑，偶数 $\to$ 白），得到的图案趋近于 **Sierpiński 三角形**——一个自相似的分形结构。

这不是巧合：Lucas 定理告诉我们 $\binom{n}{k} \pmod{2}$ 取决于 $n$ 和 $k$ 的二进制表示的"位比较"关系，而这种关系恰好产生自相似结构。

更一般地，Pascal 三角形模 $p$（$p$ 为素数）产生的图案是 $p$ 阶 Sierpiński 三角形的推广。

---

## 5. 指数生成函数与 $e^x$

### 另一种编码方式

如果用 $a_n x^n/n!$（而非 $a_n x^n$）作为第 $n$ 项，得到的是**指数生成函数**（exponential generating function, EGF）：

$$\hat{A}(x) = \sum_{n=0}^{\infty} a_n \frac{x^n}{n!}$$

EGF 的乘法对应的是"有标签对象的组合"——这在排列计数中特别自然。

例如，$e^x = \sum x^n/n!$ 是序列 $a_n = 1$ 的 EGF。$e^{2x}$ 的 $x^n/n!$ 系数是 $2^n$，这是将 $n$ 个有标签对象分成两组的方式数。

多项式定理 $(x_1 + \cdots + x_m)^n/n!$ 的"指数版本"就是 $e^{x_1 + \cdots + x_m} = e^{x_1}\cdots e^{x_m}$——乘法分解反映了独立选择的结构。
