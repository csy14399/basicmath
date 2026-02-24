# §1 无穷级数（Infinite Series）

**前置知识**：[Part 6 第 1 章 §2 数列的极限](../ch01-sequences/02-sequence-limits.md)（$\epsilon$-$N$ 定义、单调有界定理）、[Part 6 第 2 章 §1 函数的极限](../ch02-limits/01-function-limits.md)（极限运算法则）

**全景图**：从"有限求和"到"无穷求和"是数学中最关键的推广之一。本节定义无穷级数为部分和数列的极限，然后深入研究两个基本原型——几何级数（能求和）和调和级数（发散）。这两个例子建立了我们对收敛与发散的直觉。接着我们证明收敛的必要条件（通项趋于零）、级数的线性性，以及 $p$-级数的收敛判据。

**预估学习时间**：约 2–3 小时

---

## 动机

考虑 Achilles 追乌龟的问题（Zeno 悖论的变形）：

Achilles 在乌龟身后 1 米处出发。他先跑完 $1/2$ 米，再跑 $1/4$ 米，再跑 $1/8$ 米……

他总共跑了多远？直觉上，答案应该是 $1$ 米：

$$\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \cdots = 1$$

但这个等式的**精确含义**是什么？左边有**无穷多个**加数——我们不能像有限求和那样逐个相加。我们需要一个严格的定义。

另一方面，考虑：

$$1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots$$

每一项都趋于零，但（令人惊讶地）这个"和"却趋于无穷——它**发散**了。

这两个例子——一个收敛、一个发散——构成了本节的核心故事。

---

## 1. 部分和与级数收敛（Partial Sums and Convergence）

### 1.1 无穷级数的定义

> **定义 1**（无穷级数 / infinite series）
>
> 给定数列 $\{a_n\}_{n=1}^{\infty}$，**无穷级数**（或简称**级数**）
>
> $$\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \cdots$$
>
> 定义为部分和数列 $\{S_n\}$ 的极限，其中第 $n$ 个**部分和**（partial sum）为：
>
> $$S_n = \sum_{k=1}^{n} a_k = a_1 + a_2 + \cdots + a_n$$

> **定义 2**（收敛与发散）
>
> - 若部分和数列 $\{S_n\}$ 收敛，即 $\lim_{n \to \infty} S_n = S$ 存在且有限，则称级数 $\sum a_n$ **收敛**（converges），$S$ 称为级数的**和**（sum），记作 $\sum_{n=1}^{\infty} a_n = S$。
> - 若 $\{S_n\}$ 发散，则称级数 $\sum a_n$ **发散**（diverges）。

**关键洞察**：无穷级数**不是**真正的无穷次加法——它是一个**极限过程**。级数的"和"是部分和序列的极限。这是将无穷操作严格化的标准方法：用有限近似的极限来定义无穷操作。

### 1.2 伸缩级数（Telescoping Series）

有些级数可以直接计算部分和。

**例 1**：求 $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n(n+1)}$ 的和。

**解**：用部分分式分解：

$$\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$$

部分和：

$$S_n = \sum_{k=1}^{n}\left(\frac{1}{k} - \frac{1}{k+1}\right) = \left(\frac{1}{1} - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \cdots + \left(\frac{1}{n} - \frac{1}{n+1}\right)$$

中间项全部"消去"（telescope），留下：

$$S_n = 1 - \frac{1}{n+1} = \frac{n}{n+1}$$

因此：

$$\sum_{n=1}^{\infty}\frac{1}{n(n+1)} = \lim_{n \to \infty}\frac{n}{n+1} = 1$$

**例 2**：求 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(n+2)}$。

**解**：$\dfrac{1}{n(n+2)} = \dfrac{1}{2}\left(\dfrac{1}{n} - \dfrac{1}{n+2}\right)$。

$$S_n = \frac{1}{2}\sum_{k=1}^{n}\left(\frac{1}{k} - \frac{1}{k+2}\right) = \frac{1}{2}\left(1 + \frac{1}{2} - \frac{1}{n+1} - \frac{1}{n+2}\right)$$

$$\sum_{n=1}^{\infty}\frac{1}{n(n+2)} = \frac{1}{2}\left(1 + \frac{1}{2}\right) = \frac{3}{4}$$

---

## 2. 几何级数（Geometric Series）

### 2.1 有限几何级数回顾

回顾 Part 6 Ch01 中的结果：对 $r \neq 1$，

$$\sum_{k=0}^{n-1} ar^k = a \cdot \frac{1 - r^n}{1 - r}$$

### 2.2 无穷几何级数

> **定理 1**（几何级数的收敛性）
>
> 设 $a \neq 0$。几何级数
>
> $$\sum_{n=0}^{\infty} ar^n = a + ar + ar^2 + ar^3 + \cdots$$
>
> - 当 $|r| < 1$ 时收敛，和为 $\dfrac{a}{1 - r}$；
> - 当 $|r| \geq 1$ 时发散。

**证明**：

部分和为：

$$S_n = \sum_{k=0}^{n-1} ar^k = a \cdot \frac{1 - r^n}{1 - r}$$

**情况 1：$|r| < 1$**。由 Ch01 的结果，$r^n \to 0$（$|r| < 1$ 时 $|r^n| = |r|^n \to 0$）。因此：

$$\lim_{n \to \infty} S_n = a \cdot \frac{1 - 0}{1 - r} = \frac{a}{1 - r}$$

**情况 2：$|r| > 1$**。$|r^n| = |r|^n \to \infty$，$S_n$ 发散。

**情况 3：$r = 1$**。$S_n = na \to \pm\infty$（因 $a \neq 0$），发散。

**情况 4：$r = -1$**。$S_n = a(1 - (-1)^n)/2$，在 $0$ 和 $a$ 之间振荡，不收敛。$\blacksquare$

![几何级数的部分和](../../images/p06-ch04-geometric-series.png)

**例 3**：$\displaystyle\sum_{n=0}^{\infty}\frac{1}{2^n} = \frac{1}{1 - 1/2} = 2$。

**例 4**：$\displaystyle\sum_{n=0}^{\infty}\left(-\frac{1}{3}\right)^n = \frac{1}{1 - (-1/3)} = \frac{1}{4/3} = \frac{3}{4}$。

**例 5**：将循环小数 $0.999\ldots$ 表示为级数：

$$0.999\ldots = \frac{9}{10} + \frac{9}{100} + \frac{9}{1000} + \cdots = \sum_{n=1}^{\infty}\frac{9}{10^n} = \frac{9/10}{1 - 1/10} = \frac{9/10}{9/10} = 1$$

这是"$0.999\ldots = 1$"的严格证明。

**例 6**：将 $0.\overline{142857}$ 转化为分数：

$$0.\overline{142857} = \sum_{n=1}^{\infty}\frac{142857}{10^{6n}} = \frac{142857/10^6}{1 - 1/10^6} = \frac{142857}{999999} = \frac{1}{7}$$

---

## 3. 调和级数（Harmonic Series）

### 3.1 调和级数发散

调和级数是分析学中最重要的发散级数。

> **定理 2**（调和级数发散）
>
> 调和级数 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots$ **发散**。

**证明**（Oresme 分组论证，约 1350 年）：

将各项按 $2$ 的幂次分组：

$$\begin{aligned}
S &= 1 + \frac{1}{2} + \left(\frac{1}{3} + \frac{1}{4}\right) + \left(\frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8}\right) + \left(\frac{1}{9} + \cdots + \frac{1}{16}\right) + \cdots
\end{aligned}$$

对每一组，用该组的最小项来下界估计：

- 第 2 组：$\dfrac{1}{3} + \dfrac{1}{4} > \dfrac{1}{4} + \dfrac{1}{4} = \dfrac{1}{2}$
- 第 3 组：$\dfrac{1}{5} + \dfrac{1}{6} + \dfrac{1}{7} + \dfrac{1}{8} > 4 \cdot \dfrac{1}{8} = \dfrac{1}{2}$
- 第 4 组：$\dfrac{1}{9} + \cdots + \dfrac{1}{16} > 8 \cdot \dfrac{1}{16} = \dfrac{1}{2}$
- 一般地，第 $k$ 组（$k \geq 2$）包含 $2^{k-2}$ 项，每项 $\geq 1/2^{k-1}$，所以组和 $> 2^{k-2} \cdot 1/2^{k-1} = 1/2$。

因此：

$$S_n \geq 1 + \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + \cdots$$

包含无穷多个 $1/2$，所以 $S_n \to \infty$。调和级数发散。$\blacksquare$

![调和级数部分和的增长](../../images/p06-ch04-harmonic-series.png)

### 3.2 调和级数的增长速度

虽然调和级数发散，但它增长得极其缓慢。可以证明：

$$\sum_{k=1}^{n}\frac{1}{k} \approx \ln n + \gamma$$

其中 $\gamma \approx 0.5772$ 是 **Euler-Mascheroni 常数**。直觉：$\sum 1/k$ 大约等于 $\int_1^n 1/x\,dx = \ln n$。

这意味着要使部分和超过 $10$，需要约 $e^{10} \approx 22026$ 项；超过 $100$ 需要约 $e^{100} \approx 2.69 \times 10^{43}$ 项。调和级数发散得"太慢了"。

---

## 4. 发散的必要条件（Divergence Test）

级数收敛是否要求通项趋于零？

> **定理 3**（收敛的必要条件 / 发散判别法）
>
> 若级数 $\sum_{n=1}^{\infty} a_n$ 收敛，则 $\lim_{n \to \infty} a_n = 0$。
>
> 等价地（逆否命题）：若 $\lim_{n \to \infty} a_n \neq 0$（包括极限不存在），则 $\sum a_n$ 发散。

**证明**：设 $\sum a_n$ 收敛于 $S$，即 $S_n \to S$。注意 $a_n = S_n - S_{n-1}$。由极限的线性性：

$$\lim_{n \to \infty} a_n = \lim_{n \to \infty}(S_n - S_{n-1}) = S - S = 0 \qquad \blacksquare$$

> ⚠️ **警告：逆命题不成立！**
>
> $a_n \to 0$ **不保证** $\sum a_n$ 收敛。反例就是调和级数：$1/n \to 0$，但 $\sum 1/n$ 发散。
>
> 这是初学者最常犯的错误之一。$a_n \to 0$ 是收敛的**必要**条件但**不是充分**条件。

**例 7**：$\displaystyle\sum_{n=1}^{\infty}\frac{n}{2n+1}$。$\lim \dfrac{n}{2n+1} = \dfrac{1}{2} \neq 0$。由发散判别法，级数发散。

**例 8**：$\displaystyle\sum_{n=1}^{\infty}(-1)^n$。$a_n = (-1)^n$ 不收敛于 $0$（振荡）。发散。

**例 9**：$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n}$。$a_n = 1/n \to 0$，但级数发散。发散判别法在此无法判断——需要更精细的工具（下一节）。

---

## 5. 级数的线性性（Linearity of Series）

> **定理 4**（级数的线性性）
>
> 若 $\sum a_n = A$ 和 $\sum b_n = B$ 都收敛，$c, d \in \mathbb{R}$，则：
>
> $$\sum_{n=1}^{\infty}(ca_n + db_n) = cA + dB$$

**证明**：直接由部分和的线性性和极限的线性性得到：

$$\sum_{k=1}^{n}(ca_k + db_k) = c\sum_{k=1}^{n}a_k + d\sum_{k=1}^{n}b_k \to cA + dB \qquad \blacksquare$$

> ⚠️ **注意**：若 $\sum a_n$ 和 $\sum b_n$ 中有一个发散，不能使用线性性。特别地，$\sum a_n$ 收敛且 $\sum b_n$ 发散则 $\sum(a_n + b_n)$ 一定发散（反证法：若它收敛，则 $\sum b_n = \sum(a_n + b_n) - \sum a_n$ 也收敛，矛盾）。

**例 10**：$\displaystyle\sum_{n=0}^{\infty}\left(\frac{3}{2^n} + \frac{2}{3^n}\right) = 3 \cdot \frac{1}{1-1/2} + 2 \cdot \frac{1}{1-1/3} = 6 + 3 = 9$。

---

## 6. $p$-级数（$p$-Series）

几何级数和调和级数都是更一般的 $p$-级数的特例。

> **定理 5**（$p$-级数的收敛性）
>
> $p$-级数
>
> $$\sum_{n=1}^{\infty}\frac{1}{n^p}$$
>
> - 当 $p > 1$ 时**收敛**；
> - 当 $p \leq 1$ 时**发散**。

**$p \leq 1$ 时发散**：若 $0 < p \leq 1$，则 $1/n^p \geq 1/n$，由调和级数发散和比较（$S_n \geq$ 调和部分和），$\sum 1/n^p$ 发散。若 $p \leq 0$，则 $1/n^p = n^{|p|} \not\to 0$，由发散判别法，级数发散。

**$p > 1$ 时收敛**（Cauchy 凝聚判别法思路）：

将各项按 $2$ 的幂次分组（类似 Oresme 论证，但方向相反）：

$$\sum_{n=1}^{\infty}\frac{1}{n^p} = 1 + \left(\frac{1}{2^p} + \frac{1}{3^p}\right) + \left(\frac{1}{4^p} + \cdots + \frac{1}{7^p}\right) + \cdots$$

第 $k$ 组（$k \geq 1$）包含 $2^{k-1}$ 项，每项 $\leq 1/(2^{k-1})^p$。所以：

$$\text{第 } k \text{ 组} \leq 2^{k-1} \cdot \frac{1}{2^{p(k-1)}} = \frac{1}{2^{(p-1)(k-1)}}$$

令 $r = 1/2^{p-1}$。$p > 1$ 时 $0 < r < 1$，故：

$$\sum_{n=1}^{\infty}\frac{1}{n^p} \leq 1 + \sum_{k=1}^{\infty} r^{k-1} \cdot r^0 = 1 + \sum_{k=0}^{\infty}r^k = 1 + \frac{1}{1 - r} = \frac{2 - r}{1 - r} < \infty$$

部分和有上界且单调递增，由单调有界定理收敛。$\blacksquare$

**另一种直觉——积分判别法（预览）**：

$$\sum_{n=1}^{\infty}\frac{1}{n^p} \text{ 与 } \int_1^{\infty}\frac{1}{x^p}dx \text{ 同敛散}$$

$\displaystyle\int_1^{\infty}\frac{1}{x^p}dx = \begin{cases}\dfrac{1}{p-1} & p > 1 \\ +\infty & p \leq 1\end{cases}$

这不是严格证明（需要积分的严格定义，见 Ch05），但提供了很好的直觉。

**重要的 $p$-级数值**：

| $p$ | 级数 | 收敛/发散 | 值 |
|-----|------|-----------|-----|
| $0$ | $\sum 1$ | 发散 | — |
| $1/2$ | $\sum 1/\sqrt{n}$ | 发散 | — |
| $1$ | $\sum 1/n$ | 发散 | — |
| $2$ | $\sum 1/n^2$ | 收敛 | $\pi^2/6$ (Euler, 1734) |
| $3$ | $\sum 1/n^3$ | 收敛 | $\approx 1.202$ (Apéry 常数) |
| $4$ | $\sum 1/n^4$ | 收敛 | $\pi^4/90$ |

$\sum 1/n^2 = \pi^2/6$ 的证明（巴塞尔问题）超出本书范围，但它是数学史上最美的结果之一——Euler 在 1734 年用巧妙的（非严格的）方法发现了它。

---

## 例题

**例题 1**：判断以下级数的敛散性并求和（如果收敛）：

(a) $\displaystyle\sum_{n=1}^{\infty}\frac{2}{3^n}$

(b) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2 + 3n + 2}$

(c) $\displaystyle\sum_{n=1}^{\infty}\frac{n+1}{n}$

**解**：

(a) 这是首项 $a = 2/3$、公比 $r = 1/3$ 的几何级数。$|r| < 1$，收敛。

$$\sum_{n=1}^{\infty}\frac{2}{3^n} = \frac{2/3}{1-1/3} = \frac{2/3}{2/3} = 1$$

(b) 部分分式：$\dfrac{1}{n^2+3n+2} = \dfrac{1}{(n+1)(n+2)} = \dfrac{1}{n+1} - \dfrac{1}{n+2}$。

$$S_n = \left(\frac{1}{2} - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{4}\right) + \cdots + \left(\frac{1}{n+1} - \frac{1}{n+2}\right) = \frac{1}{2} - \frac{1}{n+2}$$

$$\sum = \lim_{n \to \infty}\left(\frac{1}{2} - \frac{1}{n+2}\right) = \frac{1}{2}$$

(c) $a_n = \dfrac{n+1}{n} = 1 + \dfrac{1}{n} \to 1 \neq 0$。由发散判别法，级数发散。

---

**例题 2**：证明 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(n+1)(n+2)} = \frac{1}{4}$。

**解**：部分分式分解：

$$\frac{1}{n(n+1)(n+2)} = \frac{1}{2}\left(\frac{1}{n(n+1)} - \frac{1}{(n+1)(n+2)}\right)$$

这是一个伸缩级数：

$$S_n = \frac{1}{2}\left(\frac{1}{1 \cdot 2} - \frac{1}{(n+1)(n+2)}\right)$$

$$\sum = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4} \qquad \blacksquare$$

---

**例题 3**：求 $\displaystyle\sum_{n=0}^{\infty}\frac{2^n + 3^n}{6^n}$ 的和。

**解**：

$$\sum_{n=0}^{\infty}\frac{2^n + 3^n}{6^n} = \sum_{n=0}^{\infty}\left(\frac{1}{3}\right)^n + \sum_{n=0}^{\infty}\left(\frac{1}{2}\right)^n = \frac{1}{1-1/3} + \frac{1}{1-1/2} = \frac{3}{2} + 2 = \frac{7}{2}$$

---

## 要点回顾

| 概念 | 要点 |
|------|------|
| **部分和** | $S_n = \sum_{k=1}^{n}a_k$；级数 $\sum a_n$ 收敛 $\Leftrightarrow$ $\{S_n\}$ 收敛 |
| **几何级数** | $\sum ar^n$：$\|r\|<1$ 时收敛于 $a/(1-r)$，$\|r\|\geq 1$ 时发散 |
| **调和级数** | $\sum 1/n$ 发散（Oresme 分组论证） |
| **发散判别法** | $a_n \not\to 0 \Rightarrow \sum a_n$ 发散；但 $a_n \to 0$ 不保证收敛 |
| **线性性** | $\sum(ca_n + db_n) = c\sum a_n + d\sum b_n$（两个级数都收敛时） |
| **$p$-级数** | $\sum 1/n^p$：$p>1$ 收敛，$p\leq 1$ 发散 |

---

## 进度检查点

在继续下一节之前，确认你能够：

- [ ] 写出"级数 $\sum a_n$ 收敛于 $S$"的精确定义
- [ ] 识别并计算几何级数的和
- [ ] 用 Oresme 论证解释为什么调和级数发散
- [ ] 用发散判别法快速排除某些级数
- [ ] 判断 $p$-级数的收敛性
- [ ] 计算伸缩级数的和

---

## 自测题

**自测 1**：级数 $\displaystyle\sum_{n=1}^{\infty}\frac{5}{4^n}$ 收敛吗？如果收敛，和是多少？

<details>
<summary>答案</summary>

这是首项 $5/4$、公比 $1/4$ 的几何级数。$|r| = 1/4 < 1$，收敛。

$$\sum = \frac{5/4}{1 - 1/4} = \frac{5/4}{3/4} = \frac{5}{3}$$
</details>

**自测 2**：$\displaystyle\sum_{n=1}^{\infty}\frac{n^2}{n^2+1}$ 收敛还是发散？

<details>
<summary>答案</summary>

$\lim \dfrac{n^2}{n^2+1} = 1 \neq 0$。由发散判别法，级数**发散**。
</details>

**自测 3**：$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{3/2}}$ 收敛还是发散？

<details>
<summary>答案</summary>

这是 $p = 3/2 > 1$ 的 $p$-级数，**收敛**。
</details>

**自测 4**：求 $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n^2-1}$ 的和。

<details>
<summary>答案</summary>

$\dfrac{1}{n^2-1} = \dfrac{1}{(n-1)(n+1)} = \dfrac{1}{2}\left(\dfrac{1}{n-1} - \dfrac{1}{n+1}\right)$。

伸缩：

$$S_n = \frac{1}{2}\left(1 + \frac{1}{2} - \frac{1}{n} - \frac{1}{n+1}\right) \to \frac{1}{2} \cdot \frac{3}{2} = \frac{3}{4}$$
</details>

**自测 5**：解释为什么 $a_n \to 0$ 不足以保证 $\sum a_n$ 收敛。给出一个反例。

<details>
<summary>答案</summary>

反例：$a_n = 1/n$。$1/n \to 0$，但 $\sum 1/n$（调和级数）发散。$a_n \to 0$ 是收敛的必要条件而非充分条件：它只是说"通项不趋于零则一定发散"，但趋于零可能"太慢"，以至于求和仍然趋于无穷。
</details>

---

## 习题引用

本节的练习题见 [练习题](exercises/exercises.md) 的 §1 部分。
