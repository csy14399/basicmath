# §2 数列的极限（Sequence Limits）

**前置知识**：[本章 §1 数列的概念](01-sequence-concepts.md)（数列的定义、有界性、单调性）、[Part 1 第 1 章 逻辑](../../part-01-foundations/ch01-logic/README.md)（量词 $\forall$, $\exists$）、[Part 1 第 3 章 证明方法](../../part-01-foundations/ch03-proofs/README.md)（反证法）、[Part 3 第 2 章 不等式](../../part-03-algebra/ch02-inequalities/README.md)（绝对值不等式）

**全景图**：本节是分析学的真正起点。我们将回答一个看似简单实则深刻的问题：**一个数列"趋向"某个值，到底是什么意思？** 先从直觉出发——$1/n$ 趋向 $0$ 是"显然"的——然后引入 Weierstrass 的 $\epsilon$-$N$ 定义，将这个直觉转化为绝对精确的数学语言。接着我们学会用这个定义证明极限，建立极限的基本性质（唯一性、有界性、四则运算），掌握两个强大的求极限工具（夹逼定理和单调有界定理），最后研究数学中最重要的常数之一——$e$ 的定义。

**预估学习时间**：约 5–6 小时

---

## 动机

考虑数列 $a_n = \dfrac{1}{n}$：

$$1, \; \frac{1}{2}, \; \frac{1}{3}, \; \frac{1}{4}, \; \frac{1}{5}, \; \ldots$$

"显然"这个数列趋向 $0$。但**为什么**它趋向 $0$？什么叫"趋向"？

你可能会说："因为 $1/n$ 越来越小，最终无限接近 $0$。" 但"无限接近"是什么意思？$1/n$ 永远不等于 $0$——它只是越来越小。在它到达 $0$ 之前，它还要经过 $0.001$，$0.0001$，$0.00001$，……永远到不了终点。

这种困惑困扰了数学家两千年。Zeno 的悖论（Achilles 追龟）本质上就是在问：**无穷多个越来越小的步骤能否完成一个有限的过程？**

19 世纪，Cauchy 和 Weierstrass 用一个巧妙的定义终结了这个困惑。他们不说"$a_n$ 最终到达 $L$"——而说"$a_n$ 可以与 $L$ 任意接近"。具体地：

**无论你给我多小的正数 $\epsilon$（容差），我都能找到一个位置 $N$，使得从第 $N$ 项开始，数列的每一项都在 $L$ 的 $\epsilon$ 范围内。**

这就是 $\epsilon$-$N$ 定义的核心思想。

---

## 1. 直觉引入——什么是"趋近"？

### 1.1 几个例子

**例 1**：$a_n = \dfrac{1}{n}$ "趋向" $0$。

| $n$ | $a_n$ | 与 $0$ 的距离 |
|-----|-------|-------------|
| $10$ | $0.1$ | $0.1$ |
| $100$ | $0.01$ | $0.01$ |
| $1000$ | $0.001$ | $0.001$ |
| $10^6$ | $10^{-6}$ | $10^{-6}$ |

距离越来越小，但永远不为零。

**例 2**：$a_n = \dfrac{3n+1}{2n+5}$ "趋向" $\dfrac{3}{2}$。

$$a_n = \frac{3n+1}{2n+5} = \frac{3 + 1/n}{2 + 5/n} \xrightarrow{n \to \infty} \frac{3 + 0}{2 + 0} = \frac{3}{2}$$

**例 3**：$a_n = \left(1 + \dfrac{1}{n}\right)^n$ "趋向"某个常数。

| $n$ | $a_n$ |
|-----|-------|
| $1$ | $2$ |
| $2$ | $2.25$ |
| $5$ | $2.48832$ |
| $10$ | $2.59374\ldots$ |
| $100$ | $2.70481\ldots$ |
| $1000$ | $2.71692\ldots$ |
| $\to \infty$ | $\to e = 2.71828\ldots$ |

这个极限就是自然对数的底 $e$——数学中最重要的常数之一。

### 1.2 "趋近"的三个层次

1. **模糊直觉**："$a_n$ 越来越接近 $L$。" ——太模糊，$a_n = 2 + 1/n$ "越来越接近 $3$"也成立，但极限是 $2$ 不是 $3$。
2. **改进直觉**："$a_n$ 与 $L$ 的距离可以任意小。" ——更好，但需要精确化"任意小"。
3. **$\epsilon$-$N$ 定义**：精确的数学语言。——见下文。

---

## 2. $\epsilon$-$N$ 定义（The $\epsilon$-$N$ Definition）

> **定义 1**（数列极限）
>
> 设 $\{a_n\}$ 是一个数列，$L \in \mathbb{R}$。如果对**任意** $\epsilon > 0$，**存在**正整数 $N$ 使得对**所有** $n > N$：
>
> $$|a_n - L| < \epsilon$$
>
> 则称数列 $\{a_n\}$ **收敛于** $L$（converges to $L$），记为
>
> $$\lim_{n \to \infty} a_n = L \quad \text{或} \quad a_n \to L \; (n \to \infty)$$
>
> $L$ 称为数列的**极限**（limit）。如果数列不收敛于任何实数，则称其**发散**（diverges）。

用逻辑符号：

$$\lim_{n \to \infty} a_n = L \quad \Longleftrightarrow \quad \forall \epsilon > 0, \; \exists N \in \mathbb{N}^*, \; \forall n > N: \; |a_n - L| < \epsilon$$

![epsilon-N 定义的几何图示](../../images/p06-ch01-epsilon-N-definition.png)

### 2.1 解读定义

这个定义的每个部分都至关重要：

- **$\forall \epsilon > 0$**："任意正数 $\epsilon$"——你可以选择任意小的容差（$0.1$, $0.001$, $10^{-100}$, ……），我的结论都成立。这就是"任意接近"的精确含义。

- **$\exists N \in \mathbb{N}^*$**："存在一个位置 $N$"——$N$ 的选取依赖于 $\epsilon$。$\epsilon$ 越小，$N$ 通常越大。我们有时写 $N(\epsilon)$ 来强调这种依赖。

- **$\forall n > N$**："从第 $N$ 项之后的所有项"——不只是某一项，而是**所有**后续项都必须满足条件。有限多项的"违规"不影响极限。

- **$|a_n - L| < \epsilon$**："$a_n$ 与 $L$ 的距离小于 $\epsilon$"——即 $a_n \in (L - \epsilon, L + \epsilon)$，$a_n$ 落在以 $L$ 为中心、半径为 $\epsilon$ 的开区间内。

### 2.2 直觉比喻

想象一个"挑战-回应"游戏：

1. **挑战者**给出一个正数 $\epsilon$（无论多小）。
2. **回应者**必须找到一个位置 $N$，使得第 $N$ 项之后所有项都在 $L$ 的 $\epsilon$ 邻域内。

如果对**每一个**挑战，回应者都能成功应答，那么 $\lim a_n = L$。

---

## 3. 用定义证明极限

### 3.1 证明策略

用 $\epsilon$-$N$ 定义证明 $\lim a_n = L$ 的步骤：

1. **设** $\epsilon > 0$ 为任意正数（"设挑战"）
2. **分析** $|a_n - L|$，将其简化或放大为关于 $n$ 的简单表达式
3. **找到** $N$ 使得当 $n > N$ 时 $|a_n - L| < \epsilon$（"构造回应"）
4. **验证**：对所有 $n > N$，确认 $|a_n - L| < \epsilon$ 成立

> **例题 1**：证明 $\displaystyle\lim_{n \to \infty} \frac{1}{n} = 0$。

> **证明**
>
> 设 $\epsilon > 0$ 为任意正数。我们需要找 $N$ 使得 $n > N$ 时 $\left|\dfrac{1}{n} - 0\right| < \epsilon$。
>
> $$\left|\frac{1}{n}\right| = \frac{1}{n}$$
>
> 要使 $\dfrac{1}{n} < \epsilon$，只需 $n > \dfrac{1}{\epsilon}$。
>
> 取 $N = \left\lceil \dfrac{1}{\epsilon} \right\rceil$（大于等于 $1/\epsilon$ 的最小正整数）。则对所有 $n > N$：
>
> $$\frac{1}{n} < \frac{1}{N} \leq \epsilon$$
>
> 故 $\left|\dfrac{1}{n} - 0\right| < \epsilon$。
>
> 由 $\epsilon$ 的任意性，$\displaystyle\lim_{n \to \infty} \frac{1}{n} = 0$。$\blacksquare$

**示例**：若 $\epsilon = 0.01$，则 $N = 100$；若 $\epsilon = 10^{-6}$，则 $N = 10^6$。$\epsilon$ 越小，$N$ 越大——这正是直觉的量化。

> **例题 2**：证明 $\displaystyle\lim_{n \to \infty} \frac{3n+1}{2n+5} = \frac{3}{2}$。

> **证明**
>
> 设 $\epsilon > 0$。计算：
>
> $$\left|\frac{3n+1}{2n+5} - \frac{3}{2}\right| = \left|\frac{2(3n+1) - 3(2n+5)}{2(2n+5)}\right| = \left|\frac{6n+2-6n-15}{2(2n+5)}\right| = \frac{13}{2(2n+5)}$$
>
> 要使此式 $< \epsilon$，只需：
>
> $$\frac{13}{2(2n+5)} < \epsilon \iff 2n+5 > \frac{13}{2\epsilon} \iff n > \frac{13 - 10\epsilon}{4\epsilon}$$
>
> 简化起见，注意 $\dfrac{13}{2(2n+5)} < \dfrac{13}{4n}$（因为 $2n + 5 > 2n$），所以只需 $\dfrac{13}{4n} < \epsilon$，即 $n > \dfrac{13}{4\epsilon}$。
>
> 取 $N = \left\lceil \dfrac{13}{4\epsilon} \right\rceil$。对所有 $n > N$：
>
> $$\left|\frac{3n+1}{2n+5} - \frac{3}{2}\right| = \frac{13}{2(2n+5)} < \frac{13}{4n} < \frac{13}{4N} \leq \epsilon$$
>
> 故 $\displaystyle\lim_{n \to \infty} \frac{3n+1}{2n+5} = \frac{3}{2}$。$\blacksquare$

> **例题 3**：证明 $\displaystyle\lim_{n \to \infty} \frac{n^2}{2n^2 + 1} = \frac{1}{2}$。

> **证明**
>
> 设 $\epsilon > 0$。
>
> $$\left|\frac{n^2}{2n^2+1} - \frac{1}{2}\right| = \left|\frac{2n^2 - (2n^2+1)}{2(2n^2+1)}\right| = \frac{1}{2(2n^2+1)} < \frac{1}{4n^2} \leq \frac{1}{4n}$$
>
> 取 $N = \left\lceil \dfrac{1}{4\epsilon} \right\rceil$。对所有 $n > N$：
>
> $$\left|\frac{n^2}{2n^2+1} - \frac{1}{2}\right| < \frac{1}{4n} < \frac{1}{4N} \leq \epsilon$$
>
> $\blacksquare$

---

## 4. 极限的性质（Properties of Limits）

### 4.1 极限的唯一性

> **定理 1**（极限的唯一性）
>
> 如果数列 $\{a_n\}$ 收敛，则其极限是唯一的。

> **证明**（反证法）
>
> 假设 $a_n \to L_1$ 且 $a_n \to L_2$，其中 $L_1 \neq L_2$。不妨设 $L_1 < L_2$。
>
> 取 $\epsilon = \dfrac{L_2 - L_1}{2} > 0$。
>
> 由 $a_n \to L_1$，存在 $N_1$ 使得 $n > N_1$ 时 $|a_n - L_1| < \epsilon$。
>
> 由 $a_n \to L_2$，存在 $N_2$ 使得 $n > N_2$ 时 $|a_n - L_2| < \epsilon$。
>
> 取 $N = \max(N_1, N_2)$。对 $n > N$：
>
> $$L_2 - L_1 = |(L_2 - a_n) + (a_n - L_1)| \leq |a_n - L_2| + |a_n - L_1| < \epsilon + \epsilon = 2\epsilon = L_2 - L_1$$
>
> 这给出 $L_2 - L_1 < L_2 - L_1$，矛盾。故 $L_1 = L_2$。$\blacksquare$

### 4.2 收敛数列是有界的

> **定理 2**（收敛 $\Longrightarrow$ 有界）
>
> 如果数列 $\{a_n\}$ 收敛，则 $\{a_n\}$ 有界。

> **证明**
>
> 设 $a_n \to L$。取 $\epsilon = 1$，存在 $N$ 使得 $n > N$ 时 $|a_n - L| < 1$，即 $|a_n| < |L| + 1$。
>
> 令 $M = \max\{|a_1|, |a_2|, \ldots, |a_N|, |L| + 1\}$。
>
> 则对所有 $n \geq 1$，$|a_n| \leq M$。故 $\{a_n\}$ 有界。$\blacksquare$

**注意**：逆命题不成立。$a_n = (-1)^n$ 有界但不收敛。

### 4.3 极限的四则运算

> **定理 3**（极限的四则运算）
>
> 设 $\lim a_n = L$，$\lim b_n = M$。则：
>
> 1. $\displaystyle\lim_{n\to\infty} (a_n \pm b_n) = L \pm M$
> 2. $\displaystyle\lim_{n\to\infty} (a_n \cdot b_n) = L \cdot M$
> 3. $\displaystyle\lim_{n\to\infty} (c \cdot a_n) = c \cdot L$（$c$ 为常数）
> 4. $\displaystyle\lim_{n\to\infty} \frac{a_n}{b_n} = \frac{L}{M}$（要求 $M \neq 0$ 且 $b_n \neq 0$）

> **证明**（以加法为例）
>
> 设 $\epsilon > 0$。由 $a_n \to L$，存在 $N_1$ 使得 $n > N_1$ 时 $|a_n - L| < \epsilon/2$。由 $b_n \to M$，存在 $N_2$ 使得 $n > N_2$ 时 $|b_n - M| < \epsilon/2$。
>
> 取 $N = \max(N_1, N_2)$。对 $n > N$：
>
> $$|(a_n + b_n) - (L + M)| = |(a_n - L) + (b_n - M)| \leq |a_n - L| + |b_n - M| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$
>
> 故 $\lim(a_n + b_n) = L + M$。$\blacksquare$

> **证明**（乘法）
>
> 设 $\epsilon > 0$。由定理 2，$\{a_n\}$ 收敛故有界，设 $|a_n| \leq K$ 对所有 $n$。
>
> $$|a_n b_n - LM| = |a_n b_n - a_n M + a_n M - LM| = |a_n(b_n - M) + M(a_n - L)|$$
>
> $$\leq |a_n||b_n - M| + |M||a_n - L| \leq K|b_n - M| + |M||a_n - L|$$
>
> 取 $N_1$ 使得 $n > N_1$ 时 $|a_n - L| < \dfrac{\epsilon}{2(|M|+1)}$。
>
> 取 $N_2$ 使得 $n > N_2$ 时 $|b_n - M| < \dfrac{\epsilon}{2(K+1)}$。
>
> 令 $N = \max(N_1, N_2)$。对 $n > N$：
>
> $$|a_n b_n - LM| < K \cdot \frac{\epsilon}{2(K+1)} + |M| \cdot \frac{\epsilon}{2(|M|+1)} < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$
>
> $\blacksquare$

---

## 5. 夹逼定理（Squeeze Theorem）

> **定理 4**（夹逼定理 / 三明治定理）
>
> 设三个数列 $\{a_n\}$, $\{b_n\}$, $\{c_n\}$ 满足：
>
> 1. 存在 $N_0$ 使得 $n > N_0$ 时 $a_n \leq b_n \leq c_n$
> 2. $\lim a_n = \lim c_n = L$
>
> 则 $\lim b_n = L$。

![夹逼定理示意图](../../images/p06-ch01-squeeze-theorem.png)

> **证明**
>
> 设 $\epsilon > 0$。
>
> 由 $a_n \to L$，存在 $N_1$ 使得 $n > N_1$ 时 $|a_n - L| < \epsilon$，即 $L - \epsilon < a_n$。
>
> 由 $c_n \to L$，存在 $N_2$ 使得 $n > N_2$ 时 $|c_n - L| < \epsilon$，即 $c_n < L + \epsilon$。
>
> 取 $N = \max(N_0, N_1, N_2)$。对 $n > N$：
>
> $$L - \epsilon < a_n \leq b_n \leq c_n < L + \epsilon$$
>
> 因此 $|b_n - L| < \epsilon$。由 $\epsilon$ 的任意性，$\lim b_n = L$。$\blacksquare$

> **例题 4**：求 $\displaystyle\lim_{n \to \infty} \frac{\sin n}{n}$。

> **解**
>
> 由 $|\sin n| \leq 1$，有 $-\dfrac{1}{n} \leq \dfrac{\sin n}{n} \leq \dfrac{1}{n}$。
>
> 而 $\lim \left(-\dfrac{1}{n}\right) = 0$ 且 $\lim \dfrac{1}{n} = 0$。
>
> 由夹逼定理，$\displaystyle\lim_{n \to \infty} \frac{\sin n}{n} = 0$。

> **例题 5**：证明 $\displaystyle\lim_{n \to \infty} \frac{1}{n!} = 0$。

> **解**
>
> 对 $n \geq 2$：
>
> $$0 < \frac{1}{n!} = \frac{1}{1 \cdot 2 \cdot 3 \cdots n} \leq \frac{1}{2^{n-1}}$$
>
> （因为 $n!$ 中除了因子 $1$ 外每个因子都 $\geq 2$）
>
> 由 $|r| < 1$ 时 $r^n \to 0$（可由 $\epsilon$-$N$ 定义证明），$\dfrac{1}{2^{n-1}} \to 0$。
>
> 由夹逼定理，$\dfrac{1}{n!} \to 0$。

---

## 6. 单调有界定理（Monotone Convergence Theorem）

夹逼定理要求我们已经知道（或猜到）极限值。但如果我们不知道极限值怎么办？**单调有界定理**告诉我们：在某些条件下，极限一定存在——即使我们不知道它的值。

> **定理 5**（单调有界定理）
>
> 单调递增且有上界的数列一定收敛。单调递减且有下界的数列一定收敛。

> **证明**（以单调递增的情况为例，使用上确界原理）
>
> 设 $\{a_n\}$ 单调递增且有上界。令 $S = \{a_n : n \in \mathbb{N}^*\}$ 为数列各项组成的集合。$S$ 非空（至少包含 $a_1$）且有上界，由实数的完备性（上确界原理），$S$ 有上确界。设 $L = \sup S$。
>
> 我们证明 $a_n \to L$。
>
> 设 $\epsilon > 0$。由上确界的定义，$L - \epsilon$ 不是 $S$ 的上界（否则 $L$ 不是最小上界）。因此存在 $N$ 使得 $a_N > L - \epsilon$。
>
> 由于 $\{a_n\}$ 单调递增，对所有 $n > N$：
>
> $$L - \epsilon < a_N \leq a_n$$
>
> 又因为 $a_n \leq L$（$L$ 是上界），故：
>
> $$L - \epsilon < a_n \leq L < L + \epsilon$$
>
> 因此 $|a_n - L| < \epsilon$。由 $\epsilon$ 的任意性，$a_n \to L$。$\blacksquare$

**深刻性**：此定理的证明依赖**实数的完备性**（上确界原理）。在有理数系 $\mathbb{Q}$ 上，此定理不成立。例如，数列 $1, 1.4, 1.41, 1.414, 1.4142, \ldots$（$\sqrt{2}$ 的十进制逼近）在 $\mathbb{Q}$ 中单调递增有上界（上界 $2$），但它的极限 $\sqrt{2} \notin \mathbb{Q}$——在 $\mathbb{Q}$ 中它不收敛。

---

## 7. 重要极限——$e$ 的定义

> **定理 6**（$e$ 的定义）
>
> 数列 $a_n = \left(1 + \dfrac{1}{n}\right)^n$ 收敛。其极限定义为 $e$：
>
> $$e = \lim_{n \to \infty}\left(1 + \frac{1}{n}\right)^n = 2.71828182845\ldots$$

> **证明思路**（单调递增且有上界）
>
> **第一步：$\{a_n\}$ 单调递增。**
>
> 利用 AM-GM 不等式（算术-几何均值不等式）：
>
> 考虑 $n+1$ 个正数中 $n$ 个为 $1 + \dfrac{1}{n}$，$1$ 个为 $1$：
>
> $$\frac{n \cdot \left(1 + \frac{1}{n}\right) + 1}{n+1} \geq \left[\left(1 + \frac{1}{n}\right)^n \cdot 1\right]^{1/(n+1)}$$
>
> 左边 $= \dfrac{n + 1 + 1}{n+1} = 1 + \dfrac{1}{n+1}$，因此：
>
> $$\left(1 + \frac{1}{n+1}\right)^{n+1} \geq \left(1 + \frac{1}{n}\right)^n$$
>
> 即 $a_{n+1} \geq a_n$。
>
> **第二步：$\{a_n\}$ 有上界。**
>
> 利用二项式定理展开：
>
> $$\left(1 + \frac{1}{n}\right)^n = \sum_{k=0}^{n} \binom{n}{k} \frac{1}{n^k}$$
>
> 其中 $\binom{n}{k}\dfrac{1}{n^k} = \dfrac{1}{k!}\cdot\dfrac{n(n-1)\cdots(n-k+1)}{n^k} \leq \dfrac{1}{k!}$。因此：
>
> $$\left(1 + \frac{1}{n}\right)^n \leq \sum_{k=0}^{n} \frac{1}{k!} \leq 1 + 1 + \frac{1}{2} + \frac{1}{4} + \cdots + \frac{1}{2^{n-1}} < 1 + \frac{1}{1 - 1/2} = 3$$
>
> 最后一步用了 $k! \geq 2^{k-1}$（对 $k \geq 1$）和无穷等比级数求和。
>
> **结论**：$\{a_n\}$ 单调递增且有上界（$a_n < 3$），由单调有界定理，$\{a_n\}$ 收敛。其极限定义为 $e$。$\blacksquare$

**$e$ 的其他表示**：

$$e = \sum_{k=0}^{\infty} \frac{1}{k!} = 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \frac{1}{4!} + \cdots$$

这将在第四章（级数）讨论。

**$e$ 的地位**：$e$ 是数学中最重要的常数之一。它是自然对数的底，是指数函数 $e^x$ 的底，出现在复利计算、概率论、物理学等各个领域。

---

## 例题（综合）

> **例题 6**：用极限的四则运算法则求 $\displaystyle\lim_{n \to \infty} \frac{5n^2 - 3n + 1}{2n^2 + 7n - 4}$。

**解**：分子分母同除以 $n^2$：

$$\frac{5n^2 - 3n + 1}{2n^2 + 7n - 4} = \frac{5 - 3/n + 1/n^2}{2 + 7/n - 4/n^2}$$

由极限的四则运算，$\lim 1/n = 0$，$\lim 1/n^2 = 0$（乘法法则），故：

$$\lim_{n \to \infty} \frac{5n^2 - 3n + 1}{2n^2 + 7n - 4} = \frac{5 - 0 + 0}{2 + 0 - 0} = \frac{5}{2}$$

---

> **例题 7**：用夹逼定理证明 $\displaystyle\lim_{n \to \infty} \sqrt[n]{n} = 1$。

> **证明**
>
> 令 $h_n = \sqrt[n]{n} - 1$，则 $n = (1 + h_n)^n$。对 $n \geq 2$，$\sqrt[n]{n} > 1$，故 $h_n > 0$。
>
> 由二项式定理：
>
> $$n = (1 + h_n)^n \geq 1 + \binom{n}{2}h_n^2 = 1 + \frac{n(n-1)}{2}h_n^2$$
>
> 因此：
>
> $$\frac{n(n-1)}{2}h_n^2 \leq n - 1$$
>
> $$h_n^2 \leq \frac{2(n-1)}{n(n-1)} = \frac{2}{n}$$
>
> 故 $0 \leq h_n \leq \sqrt{2/n}$。
>
> 由 $\lim \sqrt{2/n} = 0$（可由 $\lim 1/n = 0$ 推出），由夹逼定理 $h_n \to 0$，即 $\sqrt[n]{n} \to 1$。$\blacksquare$

---

> **例题 8**：证明数列 $a_n = \dfrac{2^n}{n!}$ 收敛于 $0$。

> **证明**
>
> 对 $n \geq 3$：
>
> $$0 < \frac{2^n}{n!} = \frac{2 \cdot 2 \cdot 2 \cdots 2}{1 \cdot 2 \cdot 3 \cdots n} = \frac{2}{1} \cdot \frac{2}{2} \cdot \frac{2}{3} \cdot \frac{2}{4} \cdots \frac{2}{n} \leq 2 \cdot 1 \cdot \frac{2}{3} \cdot \left(\frac{2}{4}\right)^{n-3}$$
>
> 更简洁地，对 $n \geq 3$：
>
> $$\frac{2^n}{n!} = \frac{4}{2} \cdot \frac{2^{n-2}}{n!/2!} = 2 \cdot \prod_{k=3}^{n} \frac{2}{k} \leq 2 \cdot \left(\frac{2}{3}\right)^{n-2}$$
>
> 因为每个因子 $\dfrac{2}{k} \leq \dfrac{2}{3}$（$k \geq 3$）。
>
> 而 $\left(\dfrac{2}{3}\right)^{n-2} \to 0$（因为 $|2/3| < 1$）。
>
> 由夹逼定理（$0 \leq \dfrac{2^n}{n!} \leq 2 \cdot (2/3)^{n-2}$），$\dfrac{2^n}{n!} \to 0$。$\blacksquare$

---

## 要点回顾

| 概念 | 要点 |
|------|------|
| $\epsilon$-$N$ 定义 | $\forall \epsilon > 0, \exists N, \forall n > N: \|a_n - L\| < \epsilon$ |
| 直觉 | "任意接近"——任意小的容差 $\epsilon$ 下，从某项起所有后续项都在 $L$ 的 $\epsilon$ 邻域内 |
| 唯一性 | 收敛数列的极限唯一 |
| 有界性 | 收敛 $\Rightarrow$ 有界（反之不然） |
| 四则运算 | 收敛数列的和、差、积、商的极限等于极限的和、差、积、商 |
| 夹逼定理 | 若 $a_n \leq b_n \leq c_n$ 且 $\lim a_n = \lim c_n = L$，则 $\lim b_n = L$ |
| 单调有界定理 | 单调 + 有界 $\Rightarrow$ 收敛（依赖实数完备性） |
| $e$ | $e = \lim(1+1/n)^n$，由单调有界定理保证存在 |

---

## 进度检查点

完成本节后，你应该能够：

- [ ] 精确陈述数列极限的 $\epsilon$-$N$ 定义，解释每个量词的作用
- [ ] 用 $\epsilon$-$N$ 定义证明 $\lim 1/n = 0$ 和类似的简单极限
- [ ] 证明极限的唯一性和"收敛 $\Rightarrow$ 有界"
- [ ] 运用极限的四则运算法则求有理函数型数列的极限
- [ ] 陈述并证明夹逼定理，并用它求极限
- [ ] 陈述单调有界定理，解释为什么它依赖实数的完备性
- [ ] 解释 $e = \lim(1+1/n)^n$ 的单调性和有界性论证

---

## 自测题

**自测题 1**：用你自己的话解释 $\epsilon$-$N$ 定义中 $\forall \epsilon > 0$ 的含义。

<details>
<summary>答案</summary>

"$\forall \epsilon > 0$"意味着我们的结论对**任意**正数 $\epsilon$ 成立——无论 $\epsilon$ 多小。这正是"任意接近"的精确化：不是说 $a_n$ 与 $L$ 的距离小于某个固定的值，而是对于你能想到的任何正数（$0.1$, $0.001$, $10^{-100}$, ……），我都能保证从某项起所有项都在这个范围内。

$\epsilon$ 的任意性是定义的灵魂——去掉它，整个定义就崩塌了（"$|a_n - L| < 1$ 对充分大的 $n$ 成立"是一个远弱于极限的条件）。
</details>

**自测题 2**：数列 $a_n = (-1)^n$ 有界但不收敛。用 $\epsilon$-$N$ 定义的否定说明它为什么不收敛。

<details>
<summary>答案</summary>

$\{a_n\}$ 不收敛意味着：**对任意** $L \in \mathbb{R}$，**存在** $\epsilon > 0$，使得**对任意** $N \in \mathbb{N}^*$，**存在** $n > N$ 使得 $|a_n - L| \geq \epsilon$。

取任意 $L$。选 $\epsilon = 1$。对任意 $N$：

- 若 $L \geq 0$，取 $n > N$ 为奇数，则 $a_n = -1$，$|a_n - L| = |{-1} - L| = 1 + L \geq 1 = \epsilon$。
- 若 $L < 0$，取 $n > N$ 为偶数，则 $a_n = 1$，$|a_n - L| = 1 - L > 1 = \epsilon$。

因此 $\{a_n\}$ 不收敛于任何 $L$。
</details>

**自测题 3**：为什么单调有界定理在有理数系 $\mathbb{Q}$ 上不成立？举一个例子。

<details>
<summary>答案</summary>

因为 $\mathbb{Q}$ 不完备——它有"空隙"（无理数不在 $\mathbb{Q}$ 中）。

例如，数列 $a_1 = 1, a_2 = 1.4, a_3 = 1.41, a_4 = 1.414, \ldots$（$\sqrt{2}$ 的十进制截断）。这个数列在 $\mathbb{Q}$ 中单调递增、有上界（$a_n < 2$），但它的极限 $\sqrt{2} \notin \mathbb{Q}$。在 $\mathbb{Q}$ 中它不收敛——它"收敛"的目标不在 $\mathbb{Q}$ 内。

这就是为什么分析学建立在 $\mathbb{R}$（而非 $\mathbb{Q}$）上——完备性是极限理论的根基。
</details>

**自测题 4**：$\displaystyle\lim_{n \to \infty} \frac{n^3 + 2n}{3n^3 - n^2 + 1} = ?$ 说明你用了哪个法则。

<details>
<summary>答案</summary>

分子分母同除以 $n^3$：

$$\frac{n^3 + 2n}{3n^3 - n^2 + 1} = \frac{1 + 2/n^2}{3 - 1/n + 1/n^3} \xrightarrow{n \to \infty} \frac{1+0}{3-0+0} = \frac{1}{3}$$

用到了极限的四则运算法则（加法、除法、$\lim 1/n^k = 0$）。
</details>

---

## 习题引用

本节练习见[练习题](exercises/exercises.md)第 §2 部分。
