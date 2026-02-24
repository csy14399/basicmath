# 第 1 章 概率公理 — 挑战题（Challenge Problems）

以下挑战题深入探讨概率公理的推论和应用，难度超出常规练习。

---

## 挑战题 1：概率的次可加性推广

> **题目**：设 $A_1, A_2, \ldots, A_n$ 是任意事件。证明 **Bonferroni 不等式**的下界形式：
>
> $$P\!\left(\bigcup_{i=1}^n A_i\right) \geq \sum_{i=1}^n P(A_i) - \sum_{i<j} P(A_i \cap A_j)$$

### 提示

从容斥原理出发，证明被"截断"的容斥公式交替给出上界和下界。

### 解答

由容斥原理：

$$P\!\left(\bigcup A_i\right) = S_1 - S_2 + S_3 - \cdots + (-1)^{n+1}S_n$$

其中 $S_k = \sum_{i_1 < \cdots < i_k} P(A_{i_1} \cap \cdots \cap A_{i_k})$。

考虑容斥中第三项及之后：$S_3 - S_4 + \cdots + (-1)^{n+1}S_n$。可以证明（通过对指示函数的分析），这个交替和是非负的。

具体地，对于任意 $\omega \in \Omega$，设 $\omega$ 属于 $m$ 个事件 $A_i$。则 $\omega$ 对 $S_k$ 的贡献为 $\binom{m}{k}$。

$$\omega \text{ 对右边的贡献} = \binom{m}{1} - \binom{m}{2} = m - \frac{m(m-1)}{2}$$

$$\omega \text{ 对左边（$1$ 或 $0$）的贡献} = \begin{cases} 1 & m \geq 1 \\ 0 & m = 0 \end{cases}$$

当 $m \geq 1$ 时，我们需要 $1 \geq m - m(m-1)/2$，即 $m(m-1)/2 \geq m - 1$，即 $m \geq 2$ 时 $m/2 \geq 1$ 即 $m \geq 2$。当 $m = 1$ 时两边都等于 $1$。

因此对 $m \geq 1$，$1_{m \geq 1} \geq \binom{m}{1} - \binom{m}{2}$ 恰当 $m \geq 2$ 时 $1 \geq m - m(m-1)/2$。

实际上 $m - m(m-1)/2 = m(3-m)/2$，当 $m \geq 3$ 时这可能为负，所以不等式方向需要更细致的分析。正确的做法是用截断容斥的奇偶性质：截断到奇数项（$S_1$, $S_1-S_2+S_3$, ...）给出上界，截断到偶数项（$S_1-S_2$, $S_1-S_2+S_3-S_4$, ...）给出下界。

对于 $S_1 - S_2$：$\binom{m}{1} - \binom{m}{2} = m - m(m-1)/2$。当 $m = 0$ 时为 $0$；$m = 1$ 时为 $1$；$m = 2$ 时为 $1$。当 $m \geq 1$ 时需要 $\binom{m}{1} - \binom{m}{2} \leq 1$。

由二项式定理的截断，$\sum_{k=0}^{2}(-1)^k\binom{m}{k} = 1 - m + m(m-1)/2 \geq 0$（当 $m \geq 0$），这等价于 $\binom{m}{1} - \binom{m}{2} \leq 1$。因此 $P(\bigcup A_i) \geq S_1 - S_2$。$\blacksquare$

---

## 挑战题 2：概率空间的构造

> **题目**：设 $\Omega = \{1, 2, 3, \ldots\}$。构造一个概率 $P$ 使得 $P(\{k\}) = 6/(\pi^2 k^2)$。验证这确实是一个合法的概率。

### 解答

需要验证 $\sum_{k=1}^{\infty} P(\{k\}) = 1$。

$$\sum_{k=1}^{\infty} \frac{6}{\pi^2 k^2} = \frac{6}{\pi^2} \sum_{k=1}^{\infty} \frac{1}{k^2} = \frac{6}{\pi^2} \cdot \frac{\pi^2}{6} = 1 \quad \checkmark$$

这里用到了 Euler 的著名结果 $\sum_{k=1}^{\infty} 1/k^2 = \pi^2/6$（Basel 问题）。

公理验证：
1. $P(\{k\}) = 6/(\pi^2 k^2) > 0$ ✓
2. $P(\Omega) = 1$ ✓（如上）
3. 可列可加性：对两两互斥的 $A_i$，$P(\bigcup A_i) = \sum P(A_i)$——这自然成立，因为每个事件的概率是其样本点概率之和。✓

在这个概率空间中，$P(\text{偶数}) = \sum_{k=1}^{\infty} 6/(\pi^2 (2k)^2) = \frac{6}{4\pi^2} \cdot \frac{\pi^2}{6} = 1/4$。

有趣的是，偶数的概率只有 $1/4$（而非直觉中的 $1/2$），因为小的数（更可能被选到）中偶数和奇数一样多，但概率向小数倾斜。$\blacksquare$
