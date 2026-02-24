# 第 3 章 二项式定理 — 挑战题（Challenge Problems）

以下挑战题探索二项式定理和多项式定理的深层应用。

---

## 挑战题 1：Newton 的广义二项式定理

> **题目**：Newton 将二项式定理推广到**非整数**指数。对任意实数 $\alpha$ 和 $|x| < 1$：
>
> $$(1+x)^\alpha = \sum_{k=0}^{\infty}\binom{\alpha}{k}x^k$$
>
> 其中广义二项式系数定义为
>
> $$\binom{\alpha}{k} = \frac{\alpha(\alpha-1)(\alpha-2)\cdots(\alpha-k+1)}{k!}$$
>
> (a) 取 $\alpha = 1/2$，写出 $\sqrt{1+x}$ 的前四项。
>
> (b) 取 $\alpha = -1$，验证 $(1+x)^{-1} = \sum_{k=0}^{\infty}(-x)^k = \frac{1}{1+x}$（等比级数）。

### 解答

(a) $\binom{1/2}{0} = 1$，$\binom{1/2}{1} = 1/2$，$\binom{1/2}{2} = \frac{(1/2)(-1/2)}{2!} = -1/8$，$\binom{1/2}{3} = \frac{(1/2)(-1/2)(-3/2)}{3!} = 1/16$。

$$\sqrt{1+x} \approx 1 + \frac{x}{2} - \frac{x^2}{8} + \frac{x^3}{16} - \cdots$$

验证：$\sqrt{1.04} \approx 1 + 0.02 - 0.0002 = 1.0198$。精确值 $= 1.01980...$。✓

(b) $\binom{-1}{k} = \frac{(-1)(-2)\cdots(-k)}{k!} = (-1)^k$。

$(1+x)^{-1} = \sum_{k=0}^{\infty}(-1)^k x^k = 1 - x + x^2 - x^3 + \cdots = \frac{1}{1+x}$（$|x| < 1$）。✓

---

## 挑战题 2：组合恒等式的母函数证明

> **题目**：利用 $(1+x)^m(1+x)^n = (1+x)^{m+n}$ 的系数比较法证明 **Vandermonde 恒等式**：
>
> $$\binom{m+n}{r} = \sum_{k=0}^{r}\binom{m}{k}\binom{n}{r-k}$$
>
> 然后取 $m = n = r$ 推导 $\sum_{k=0}^{n}\binom{n}{k}^2 = \binom{2n}{n}$。

### 解答

$(1+x)^m = \sum_{j}\binom{m}{j}x^j$，$(1+x)^n = \sum_{i}\binom{n}{i}x^i$。

两者相乘，$x^r$ 的系数：

左端：$\sum_{k=0}^{r}\binom{m}{k}\binom{n}{r-k}$。

右端：$(1+x)^{m+n}$ 中 $x^r$ 的系数 $= \binom{m+n}{r}$。

取 $m = n = r$：$\binom{2n}{n} = \sum_{k=0}^{n}\binom{n}{k}\binom{n}{n-k} = \sum_{k=0}^{n}\binom{n}{k}^2$。$\blacksquare$

---

## 挑战题 3：Pascal 三角形模 2

> **题目**：将 Pascal 三角形中每个数取模 $2$（奇数变 $1$，偶数变 $0$），观察图案。证明 $\binom{n}{k}$ 是奇数当且仅当 $k$ 的二进制表示的每一位都 $\leq n$ 的对应位（即 $k$ 在二进制意义下是 $n$ 的"子集"）。

### 提示

使用 Lucas 定理（$p = 2$）。

### 解答

由 Lucas 定理，$\binom{n}{k} \equiv \prod_{i}\binom{n_i}{k_i} \pmod{2}$，其中 $n_i, k_i \in \{0, 1\}$ 是 $n$ 和 $k$ 的二进制位。

$\binom{n_i}{k_i}$ 在 $\bmod 2$ 下为 $0$ 当且仅当 $k_i = 1$ 且 $n_i = 0$（即 $\binom{0}{1} = 0$）。

因此 $\binom{n}{k}$ 为奇数 $\Leftrightarrow$ 对所有 $i$，$k_i \leq n_i$ $\Leftrightarrow$ $k \mathbin{\&} n = k$（按位与）。

这解释了为什么 Pascal 三角形模 $2$ 的图案是 **Sierpiński 三角形**——一个经典的分形。$\blacksquare$
