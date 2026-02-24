# §2 收敛判别法（Convergence Tests）

**前置知识**：[本章 §1 无穷级数](01-series.md)（部分和定义、几何级数、$p$-级数）、[Part 6 第 1 章 §2 数列的极限](../ch01-sequences/02-sequence-limits.md)（单调有界定理、夹逼定理）

**全景图**：上一节我们学会了用部分和的极限定义级数的收敛，并掌握了几何级数和 $p$-级数这两个基准。但对一般级数，直接计算部分和往往不可行。本节建立一套系统的"判别法工具箱"——通过与已知级数比较、检查通项的比值或根号、利用交错结构——来判断级数的敛散性。最后我们区分绝对收敛与条件收敛，引出令人震惊的 Riemann 重排定理。

**预估学习时间**：约 2–3 小时

---

## 动机

面对一个陌生的级数 $\sum a_n$，我们需要判断它是收敛还是发散。直接计算部分和 $S_n$ 并取极限通常很困难。好消息是：我们可以不必求出和的精确值，只需判断和是否有限。

策略：**与已知级数比较**。如果 $a_n$ 比某个收敛级数的通项还小，那么 $\sum a_n$ 也收敛。如果 $a_n$ 比某个发散级数的通项还大，那么 $\sum a_n$ 也发散。

这就是"比较判别法"的核心思想。接下来的比值判别法和根值判别法本质上是与几何级数比较。

---

## 1. 比较判别法（Comparison Test）

### 1.1 直接比较

> **定理 1**（比较判别法 / comparison test）
>
> 设 $0 \leq a_n \leq b_n$ 对所有 $n \geq N_0$ 成立。
>
> 1. 若 $\sum b_n$ 收敛，则 $\sum a_n$ 收敛。
> 2. 若 $\sum a_n$ 发散，则 $\sum b_n$ 发散。

**证明**（第 1 部分）：

$\sum a_n$ 的部分和 $A_n = \sum_{k=1}^{n}a_k$ 单调递增（因 $a_n \geq 0$）。由 $a_k \leq b_k$：

$$A_n = \sum_{k=1}^{n}a_k \leq \sum_{k=1}^{n}b_k \leq \sum_{k=1}^{\infty}b_k = B < \infty$$

$\{A_n\}$ 单调递增且有上界 $B$，由单调有界定理，$\{A_n\}$ 收敛。$\blacksquare$

第 2 部分是第 1 部分的逆否命题。

**例 1**：$\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2 + 1}$ 收敛吗？

**解**：$\dfrac{1}{n^2+1} < \dfrac{1}{n^2}$，而 $\sum 1/n^2$ 收敛（$p = 2 > 1$）。由比较判别法，$\sum \dfrac{1}{n^2+1}$ 收敛。

**例 2**：$\displaystyle\sum_{n=1}^{\infty}\frac{1}{\sqrt{n} - 1/2}$（$n \geq 1$）发散吗？

**解**：对 $n \geq 1$，$\sqrt{n} - 1/2 < \sqrt{n}$，所以 $\dfrac{1}{\sqrt{n}-1/2} > \dfrac{1}{\sqrt{n}}$。而 $\sum 1/\sqrt{n}$ 发散（$p = 1/2 \leq 1$）。由比较判别法，原级数发散。

### 1.2 极限比较判别法

直接比较有时不方便——我们可能不容易建立不等式。极限比较法更灵活：

> **定理 2**（极限比较判别法 / limit comparison test）
>
> 设 $a_n > 0$，$b_n > 0$，且
>
> $$L = \lim_{n \to \infty}\frac{a_n}{b_n}$$
>
> 存在。
>
> 1. 若 $0 < L < \infty$，则 $\sum a_n$ 与 $\sum b_n$ **同敛散**。
> 2. 若 $L = 0$ 且 $\sum b_n$ 收敛，则 $\sum a_n$ 收敛。
> 3. 若 $L = \infty$ 且 $\sum b_n$ 发散，则 $\sum a_n$ 发散。

**证明**（第 1 部分）：设 $0 < L < \infty$。取 $\epsilon = L/2$。存在 $N$ 使 $n \geq N$ 时 $|a_n/b_n - L| < L/2$，即：

$$\frac{L}{2}\,b_n < a_n < \frac{3L}{2}\,b_n$$

由比较判别法，$\sum a_n$ 收敛 $\Leftrightarrow$ $\sum b_n$ 收敛。$\blacksquare$

**例 3**：$\displaystyle\sum_{n=1}^{\infty}\frac{n}{n^3+1}$ 收敛吗？

**解**：$a_n = \dfrac{n}{n^3+1}$，与 $b_n = \dfrac{1}{n^2}$ 比较。

$$\lim_{n \to \infty}\frac{a_n}{b_n} = \lim\frac{n \cdot n^2}{n^3+1} = \lim\frac{n^3}{n^3+1} = 1 \in (0, \infty)$$

$\sum 1/n^2$ 收敛，由极限比较判别法，$\sum \dfrac{n}{n^3+1}$ 收敛。

**例 4**：$\displaystyle\sum_{n=2}^{\infty}\frac{1}{\ln n}$ 收敛吗？

**解**：与 $b_n = 1/n$ 比较。$\lim \dfrac{1/\ln n}{1/n} = \lim \dfrac{n}{\ln n} = \infty$。$\sum 1/n$ 发散且 $L = \infty$，由极限比较判别法，$\sum 1/\ln n$ 发散。

---

## 2. 比值判别法（Ratio Test）

> **定理 3**（比值判别法 / ratio test / d'Alembert 判别法）
>
> 设 $a_n \neq 0$，令
>
> $$L = \lim_{n \to \infty}\left|\frac{a_{n+1}}{a_n}\right|$$
>
> 1. 若 $L < 1$，则 $\sum a_n$ **绝对收敛**（从而收敛）。
> 2. 若 $L > 1$（包括 $L = \infty$），则 $\sum a_n$ **发散**。
> 3. 若 $L = 1$，**判别法失效**——无法判断。

**证明**（第 1 部分）：

设 $L < 1$。选 $r$ 使 $L < r < 1$。由极限定义，存在 $N$ 使 $n \geq N$ 时 $|a_{n+1}/a_n| < r$。

于是 $|a_{N+k}| < r^k |a_N|$（归纳）。因此：

$$\sum_{n=N}^{\infty}|a_n| = |a_N| + |a_{N+1}| + |a_{N+2}| + \cdots \leq |a_N|\sum_{k=0}^{\infty}r^k = \frac{|a_N|}{1-r} < \infty$$

级数的尾部绝对收敛，从而整个级数绝对收敛。$\blacksquare$

**第 2 部分**：若 $L > 1$，则最终 $|a_{n+1}| > |a_n|$，所以 $|a_n| \not\to 0$，由发散判别法发散。

**$L = 1$ 时失效**：$\sum 1/n$（$L = 1$，发散）和 $\sum 1/n^2$（$L = 1$，收敛）都给出 $L = 1$。

**例 5**：$\displaystyle\sum_{n=0}^{\infty}\frac{n!}{3^n}$。

$$\frac{a_{n+1}}{a_n} = \frac{(n+1)!}{3^{n+1}} \cdot \frac{3^n}{n!} = \frac{n+1}{3} \to \infty$$

$L = \infty > 1$，发散。

**例 6**：$\displaystyle\sum_{n=0}^{\infty}\frac{2^n}{n!}$。

$$\frac{a_{n+1}}{a_n} = \frac{2^{n+1}}{(n+1)!} \cdot \frac{n!}{2^n} = \frac{2}{n+1} \to 0$$

$L = 0 < 1$，绝对收敛。（事实上这就是 $e^2 = \sum 2^n/n!$。）

**例 7**：$\displaystyle\sum_{n=1}^{\infty}\frac{n^2}{2^n}$。

$$\frac{a_{n+1}}{a_n} = \frac{(n+1)^2}{2^{n+1}} \cdot \frac{2^n}{n^2} = \frac{1}{2}\left(\frac{n+1}{n}\right)^2 \to \frac{1}{2}$$

$L = 1/2 < 1$，收敛。

> **经验法则**：比值判别法特别适合含有**阶乘** $n!$ 或**指数** $a^n$ 的级数。

---

## 3. 根值判别法（Root Test）

> **定理 4**（根值判别法 / root test / Cauchy 判别法）
>
> 令
>
> $$L = \lim_{n \to \infty}\sqrt[n]{|a_n|} = \lim_{n \to \infty}|a_n|^{1/n}$$
>
> 1. 若 $L < 1$，则 $\sum a_n$ 绝对收敛。
> 2. 若 $L > 1$，则 $\sum a_n$ 发散。
> 3. 若 $L = 1$，判别法失效。

**证明**（第 1 部分）：

设 $L < 1$。选 $r$，$L < r < 1$。存在 $N$ 使 $n \geq N$ 时 $|a_n|^{1/n} < r$，即 $|a_n| < r^n$。

$$\sum_{n=N}^{\infty}|a_n| < \sum_{n=N}^{\infty}r^n = \frac{r^N}{1-r} < \infty$$

由比较判别法（与几何级数），级数绝对收敛。$\blacksquare$

**例 8**：$\displaystyle\sum_{n=1}^{\infty}\left(\frac{n}{2n+1}\right)^n$。

$$|a_n|^{1/n} = \frac{n}{2n+1} \to \frac{1}{2}$$

$L = 1/2 < 1$，收敛。

**例 9**：$\displaystyle\sum_{n=1}^{\infty}\left(\frac{1}{\ln n}\right)^n$（$n \geq 2$）。

$$|a_n|^{1/n} = \frac{1}{\ln n} \to 0$$

$L = 0 < 1$，收敛。

> **比值判别法 vs 根值判别法**：根值判别法"更强"——当比值判别法给出 $L$ 时，根值判别法给出的 $L$ 相同或更优。但在实践中，比值判别法对阶乘更方便，根值判别法对 $n$ 次方更方便。

---

## 4. 交错级数判别法（Leibniz Test）

前三个判别法主要处理正项级数。对于正负交替的级数，有一个特别优雅的判别法。

> **定理 5**（交错级数判别法 / Leibniz test / alternating series test）
>
> 设 $\{b_n\}$ 满足：
> 1. $b_n > 0$（正）
> 2. $b_{n+1} \leq b_n$（单调递减）
> 3. $\lim_{n \to \infty} b_n = 0$
>
> 则交错级数 $\displaystyle\sum_{n=1}^{\infty}(-1)^{n+1}b_n = b_1 - b_2 + b_3 - b_4 + \cdots$ **收敛**。
>
> 而且，余项估计：$|S - S_n| \leq b_{n+1}$（误差不超过被舍掉的第一项）。

**证明**：

**偶数部分和递增**：

$$S_{2n} = (b_1 - b_2) + (b_3 - b_4) + \cdots + (b_{2n-1} - b_{2n})$$

每个括号 $b_{2k-1} - b_{2k} \geq 0$（因为 $b_n$ 递减），所以 $S_{2n} \leq S_{2n+2}$，即 $\{S_{2n}\}$ 递增。

**偶数部分和有上界**：

$$S_{2n} = b_1 - (b_2 - b_3) - (b_4 - b_5) - \cdots - (b_{2n-2} - b_{2n-1}) - b_{2n} \leq b_1$$

每个括号 $b_{2k} - b_{2k+1} \geq 0$，所以 $S_{2n} \leq b_1$。

由单调有界定理，$\{S_{2n}\}$ 收敛，设极限为 $S$。

**奇数部分和**：$S_{2n+1} = S_{2n} + b_{2n+1} \to S + 0 = S$。

$\{S_{2n}\}$ 和 $\{S_{2n+1}\}$ 都收敛于 $S$，所以 $\{S_n\} \to S$。$\blacksquare$

**余项估计**：$|S - S_n| = |b_{n+1} - b_{n+2} + b_{n+3} - \cdots|$。用同样的分析，这个值 $\leq b_{n+1}$。

**例 10**：交错调和级数 $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots$。

$b_n = 1/n$：正、递减、$\to 0$。由 Leibniz 判别法，收敛。（可以证明其和为 $\ln 2$。）

**例 11**：$\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{\sqrt{n}}$ 收敛。（$b_n = 1/\sqrt{n}$：正、递减、$\to 0$。）

---

## 5. 绝对收敛与条件收敛（Absolute and Conditional Convergence）

### 5.1 定义

> **定义 1**（绝对收敛与条件收敛）
>
> - 若 $\sum |a_n|$ 收敛，则称 $\sum a_n$ **绝对收敛**（absolutely convergent）。
> - 若 $\sum a_n$ 收敛但 $\sum |a_n|$ 发散，则称 $\sum a_n$ **条件收敛**（conditionally convergent）。

### 5.2 绝对收敛蕴含收敛

> **定理 6**（绝对收敛 $\Rightarrow$ 收敛）
>
> 若 $\sum |a_n|$ 收敛，则 $\sum a_n$ 收敛。

**证明**：注意 $0 \leq a_n + |a_n| \leq 2|a_n|$。

若 $\sum |a_n|$ 收敛，则 $\sum 2|a_n| = 2\sum |a_n|$ 收敛。由比较判别法，$\sum (a_n + |a_n|)$ 收敛。

由级数的线性性：

$$\sum a_n = \sum (a_n + |a_n|) - \sum |a_n|$$

两个收敛级数之差仍收敛。$\blacksquare$

> ⚠️ **逆命题不成立**：收敛不蕴含绝对收敛。

### 5.3 条件收敛的例子

**交错调和级数**是条件收敛的经典例子：

- $\sum (-1)^{n+1}/n$ 收敛（Leibniz 判别法）
- $\sum |(-1)^{n+1}/n| = \sum 1/n$ 发散（调和级数）

所以 $\sum (-1)^{n+1}/n$ 是**条件收敛**的。

类似地，$\sum (-1)^{n+1}/\sqrt{n}$ 条件收敛。

而 $\sum (-1)^{n+1}/n^2$ 是**绝对收敛**的（因为 $\sum 1/n^2$ 收敛）。

### 5.4 绝对收敛 vs 条件收敛——核心区别

| 性质 | 绝对收敛 | 条件收敛 |
|------|---------|---------|
| $\sum \|a_n\|$ | 收敛 | 发散 |
| $\sum a_n$ | 收敛 | 收敛 |
| 重排不变性 | ✔ 和不变 | ✘ 和可变 |
| 正项之和 | 有限 | $+\infty$ |
| 负项之和 | 有限 | $-\infty$ |

---

## 6. Riemann 重排定理 [Bridge]

> **定理 7**（Riemann 重排定理，1867——陈述）
>
> 设 $\sum a_n$ **条件收敛**。则对**任意**实数 $L$（包括 $\pm\infty$），都存在 $\{a_n\}$ 的一个重排 $\{a_{\sigma(n)}\}$（即 $\sigma: \mathbb{N} \to \mathbb{N}$ 是双射），使得：
>
> $$\sum_{n=1}^{\infty}a_{\sigma(n)} = L$$

这个定理令人震惊：通过重新排列一个条件收敛级数的各项（不改变任何一项，也不增减项），可以使级数收敛于**任意预设的值**！

**为什么？** 条件收敛意味着正项之和 $= +\infty$，负项之和 $= -\infty$，但总和有限（正负项的无穷大刚好"抵消"到一个有限值）。通过调整正项和负项出现的顺序——先加入足够多的正项超过 $L$，再加入足够多的负项低于 $L$，如此往复——可以使部分和收敛于任何目标值。

**对比**：绝对收敛的级数就不会有这个问题。Dirichlet 定理保证：绝对收敛级数的任何重排都收敛于相同的和。

这就是为什么**绝对收敛比条件收敛"好得多"**——绝对收敛级数的和不依赖于求和顺序。

> 💡 完整证明需要仔细构造重排 $\sigma$，超出本书范围。核心思路是交替积累正项和负项来"引导"部分和到目标值。

---

## 例题

**例题 1**：判断以下级数的敛散性，并说明是绝对收敛还是条件收敛。

(a) $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{n^3}$

(b) $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n \cdot n}{n+1}$

(c) $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^{2/3}}$

**解**：

(a) $\sum |a_n| = \sum 1/n^3$，$p = 3 > 1$，收敛。所以原级数**绝对收敛**。

(b) $a_n = (-1)^n \cdot n/(n+1)$。$|a_n| = n/(n+1) \to 1 \neq 0$。由发散判别法，$\sum a_n$ **发散**。

(c) $b_n = 1/n^{2/3}$：正、递减、$\to 0$。由 Leibniz 判别法，$\sum (-1)^{n+1}/n^{2/3}$ 收敛。$\sum 1/n^{2/3}$ 发散（$p = 2/3 \leq 1$）。所以**条件收敛**。

---

**例题 2**：用比值判别法判断 $\displaystyle\sum_{n=1}^{\infty}\frac{3^n}{n!}$ 的敛散性。

**解**：

$$\frac{a_{n+1}}{a_n} = \frac{3^{n+1}}{(n+1)!} \cdot \frac{n!}{3^n} = \frac{3}{n+1} \to 0$$

$L = 0 < 1$，绝对收敛。（实际上 $\sum 3^n/n! = e^3$。）

---

**例题 3**：用根值判别法判断 $\displaystyle\sum_{n=1}^{\infty}\frac{n^3}{3^n}$ 的敛散性。

**解**：

$$|a_n|^{1/n} = \frac{n^{3/n}}{3}$$

$n^{3/n} = e^{3\ln n/n} \to e^0 = 1$（因为 $\ln n/n \to 0$）。所以 $L = 1/3 < 1$，收敛。

---

## 判别法选择指南

面对级数 $\sum a_n$，按以下顺序思考：

```
1. 通项 a_n → 0 ?
   ├── 否 → 发散（发散判别法）
   └── 是 → 继续
       2. 能直接识别吗？
          ├── 几何级数 → 直接判断
          ├── p-级数 → 直接判断
          ├── 伸缩级数 → 直接求和
          └── 否 → 继续
              3. 含阶乘或指数？ → 比值判别法
              4. 含 n 次方？ → 根值判别法
              5. 与已知级数形式相近？ → 比较/极限比较判别法
              6. 正负交替？ → Leibniz 判别法
```

---

## 要点回顾

| 判别法 | 条件 | 结论 |
|--------|------|------|
| **比较判别法** | $0 \leq a_n \leq b_n$，$\sum b_n$ 收敛 | $\sum a_n$ 收敛 |
| **极限比较** | $a_n, b_n > 0$，$\lim a_n/b_n = L \in (0,\infty)$ | 同敛散 |
| **比值判别法** | $\lim\|a_{n+1}/a_n\| = L$ | $L<1$ 收敛，$L>1$ 发散 |
| **根值判别法** | $\lim\|a_n\|^{1/n} = L$ | $L<1$ 收敛，$L>1$ 发散 |
| **Leibniz** | 正、递减、$\to 0$ | 交错级数收敛 |
| **绝对收敛** | $\sum\|a_n\|$ 收敛 | $\sum a_n$ 收敛 |

---

## 进度检查点

在继续下一节之前，确认你能够：

- [ ] 用比较判别法和极限比较判别法判断正项级数的敛散性
- [ ] 用比值判别法判断含阶乘/指数的级数
- [ ] 用根值判别法判断含 $n$ 次方的级数
- [ ] 用 Leibniz 判别法判断交错级数
- [ ] 区分绝对收敛和条件收敛
- [ ] 说出 Riemann 重排定理的核心结论

---

## 自测题

**自测 1**：用比较判别法证明 $\displaystyle\sum_{n=1}^{\infty}\frac{\sin^2 n}{n^2}$ 收敛。

<details>
<summary>答案</summary>

$0 \leq \dfrac{\sin^2 n}{n^2} \leq \dfrac{1}{n^2}$。$\sum 1/n^2$ 收敛（$p = 2 > 1$）。由比较判别法，$\sum \sin^2 n / n^2$ 收敛。
</details>

**自测 2**：$\displaystyle\sum_{n=1}^{\infty}\frac{n!}{n^n}$ 收敛还是发散？

<details>
<summary>答案</summary>

比值判别法：
$$\frac{a_{n+1}}{a_n} = \frac{(n+1)!}{(n+1)^{n+1}} \cdot \frac{n^n}{n!} = \frac{n^n}{(n+1)^n} = \left(\frac{n}{n+1}\right)^n = \frac{1}{(1+1/n)^n} \to \frac{1}{e}$$

$L = 1/e < 1$，**收敛**。
</details>

**自测 3**：$\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1} \ln n}{n}$ 收敛吗？绝对收敛还是条件收敛？

<details>
<summary>答案</summary>

$b_n = \ln n / n$：正（$n \geq 1$），最终递减（$b_n' = (1-\ln n)/n^2 < 0$ 当 $n \geq 3$），$\to 0$。由 Leibniz 判别法，级数**收敛**。

$\sum |\ln n / n|$：与 $\sum 1/n$ 比较。$\ln n / n \geq 1/n$ 当 $n \geq e$，但更精确地，$\ln n / n \geq 1/(2\sqrt{n})$ 对大 $n$ 成立。
实际上，由极限比较：$\lim \frac{\ln n / n}{1/n} = \lim \ln n = \infty$。所以 $\sum \ln n / n$ 发散。

因此**条件收敛**。
</details>

**自测 4**：给出一个级数，使得比值判别法失效（$L = 1$），但你可以用其他方法判断敛散性。

<details>
<summary>答案</summary>

$\sum 1/n^2$：$\dfrac{a_{n+1}}{a_n} = \dfrac{n^2}{(n+1)^2} \to 1$（比值判别法失效）。但它是 $p = 2 > 1$ 的 $p$-级数，**收敛**。

$\sum 1/n$：同样 $L = 1$（失效），但这是 $p = 1$ 的 $p$-级数，**发散**。
</details>

---

## 习题引用

本节的练习题见 [练习题](exercises/exercises.md) 的 §2 部分。
