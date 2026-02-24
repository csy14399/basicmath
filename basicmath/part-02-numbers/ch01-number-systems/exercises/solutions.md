# 第 1 章 数系 — 练习题解答

## §1 自然数与整数（Natural Numbers and Integers）

**1.** 利用自然数加法的递归定义计算 $3 + 2$。

加法的递归定义：$m + 0 = m$；$m + S(n) = S(m + n)$。

$$3 + 2 = 3 + S(1) = S(3 + 1) = S(3 + S(0)) = S(S(3 + 0)) = S(S(3)) = S(4) = 5$$

使用的规则依次为：递归步（$n = 1$）→ 递归步（$n = 0$）→ 基础步 → 取后继 → 取后继。

---

**2.** 利用自然数乘法的递归定义计算 $3 \times 2$。

乘法的递归定义：$m \times 0 = 0$；$m \times S(n) = m \times n + m$。

$$3 \times 2 = 3 \times S(1) = 3 \times 1 + 3 = (3 \times S(0) + 3) = (3 \times 0 + 3) + 3 = (0 + 3) + 3 = 3 + 3 = 6$$

---

**3.** 将整数写成有序对的等价类形式。

(a) $5 = [(5, 0)]$（或 $[(6, 1)]$、$[(7, 2)]$ 等均可）

(b) $-3 = [(0, 3)]$（或 $[(1, 4)]$、$[(2, 5)]$ 等均可）

(c) $0 = [(0, 0)]$（或 $[(1, 1)]$、$[(2, 2)]$ 等均可）

---

**4.** 计算 $[(4, 1)] + [(2, 5)]$。

$$[(4, 1)] + [(2, 5)] = [(4 + 2, 1 + 5)] = [(6, 6)]$$

$[(6, 6)]$ 表示 $6 - 6 = 0$。验证：$(6, 6) \sim (0, 0)$，因为 $6 + 0 = 6 + 0$。✓

直觉：$3 + (-3) = 0$。

---

**5.** 计算 $[(3, 7)] \times [(2, 0)]$。

$$[(3, 7)] \times [(2, 0)] = [(3 \cdot 2 + 7 \cdot 0, 3 \cdot 0 + 7 \cdot 2)] = [(6, 14)]$$

$[(6, 14)]$ 表示 $6 - 14 = -8$。

直觉：$(-4) \times 2 = -8$。✓

---

**6.** 证明整数加法的交换律。

$$[(a,b)] + [(c,d)] = [(a+c, b+d)]$$
$$[(c,d)] + [(a,b)] = [(c+a, d+b)]$$

由自然数加法的交换律，$a + c = c + a$ 且 $b + d = d + b$。

因此 $[(a+c, b+d)] = [(c+a, d+b)]$，即 $[(a,b)] + [(c,d)] = [(c,d)] + [(a,b)]$。$\blacksquare$

---

**7.** 证明 $n(n+1)$ 是偶数。

**方法一**（分情况讨论）：

**情况 1**：$n$ 是偶数，设 $n = 2k$。则 $n(n+1) = 2k(2k+1)$，含因子 $2$，是偶数。

**情况 2**：$n$ 是奇数，设 $n = 2k + 1$。则 $n + 1 = 2k + 2 = 2(k+1)$，所以 $n(n+1) = (2k+1) \cdot 2(k+1)$，含因子 $2$，是偶数。

**方法二**（归纳法）：

基础步骤：$n = 0$，$0 \cdot 1 = 0 = 2 \cdot 0$，是偶数。✓

归纳步骤：假设 $k(k+1) = 2m$。则 $(k+1)(k+2) = k(k+1) + 2(k+1) = 2m + 2(k+1) = 2(m + k + 1)$，是偶数。✓

由归纳法，对所有 $n \in \mathbb{N}$，$n(n+1)$ 是偶数。$\blacksquare$

---

**8.** 利用良序原理证明有限非空集 $S \subseteq \mathbb{N}$ 有最大元素。

$S$ 有限，设 $|S| = k$。$S$ 有上界：因为 $S$ 有限，取 $M = \sum_{s \in S} s$，则对所有 $s \in S$，$s \leq M$（因为 $S$ 中所有元素都是非负整数）。

令 $T = \{M - s : s \in S\} \subseteq \mathbb{N}$（$M - s \geq 0$，因为 $s \leq M$）。$T$ 非空。

由良序原理，$T$ 有最小元素 $M - s_0$。

$M - s_0$ 是 $T$ 中最小的，意味着 $s_0$ 是 $S$ 中最大的（因为 $M$ 是常数，$M - s$ 越小等价于 $s$ 越大）。

因此 $s_0 = \max S$。$\blacksquare$

---

**9.** 验证整数乘法的良定义性。

设 $(a, b) \sim (a', b')$，即 $a + b' = b + a'$ ……①

需证对任意 $(c, d)$：$(ac + bd, ad + bc) \sim (a'c + b'd, a'd + b'c)$。

即需证 $(ac + bd) + (a'd + b'c) = (ad + bc) + (a'c + b'd)$。

重排：需证 $ac + bd + a'd + b'c = ad + bc + a'c + b'd$。

即 $c(a - a') + d(b' - b) + a'd - b'c + bd - ad = ?$

更系统地：由 ① 得 $a - a' = b - b'$（移项），设 $a + b' = b + a'$，即 $a - b = a' - b'$。

$$\text{LHS} - \text{RHS} = (ac + bd + a'd + b'c) - (ad + bc + a'c + b'd)$$
$$= c(a - a') + d(b' - b) - d(a - a') - c(b' - b)$$

等等，让我更仔细地计算：

$$\text{LHS} - \text{RHS} = ac - ad + bd - bc + a'd - a'c + b'c - b'd$$
$$= a(c - d) - b(c - d) + a'(d - c) - b'(d - c)$$
$$= (a - b)(c - d) + (a' - b')(d - c)$$
$$= (a - b)(c - d) - (a' - b')(c - d)$$
$$= [(a - b) - (a' - b')](c - d)$$

由 ①：$a + b' = b + a'$，即 $a - b = a' - b'$，所以 $(a - b) - (a' - b') = 0$。

因此 $\text{LHS} - \text{RHS} = 0$，即 $\text{LHS} = \text{RHS}$。$\blacksquare$

---

**10.** 证明整数的消去律。

设 $a \cdot c = b \cdot c$，$c \neq 0$。

在等价类表示下，设 $a = [(p, q)]$，$b = [(r, s)]$，$c = [(u, v)]$，且 $c \neq [(0, 0)]$（即 $u \neq v$）。

$a \cdot c = [(pu + qv, pv + qu)]$，$b \cdot c = [(ru + sv, rv + su)]$。

$a \cdot c = b \cdot c$ 意味着 $(pu + qv) + (rv + su) = (pv + qu) + (ru + sv)$。

整理：$(p - q)(u - v) = (r - s)(u - v)$（通过与题 9 类似的计算）。

因为 $c \neq 0$，即 $u \neq v$（$u - v \neq 0$），可以消去 $u - v$：

$$p - q = r - s$$

即 $p + s = q + r$，即 $(p, q) \sim (r, s)$，即 $a = b$。$\blacksquare$

---

## §2 有理数（Rational Numbers）

**1.** 验证 $\frac{3}{4} = \frac{-6}{-8}$。

需要 $(3, 4) \sim (-6, -8)$，即 $3 \times (-8) = 4 \times (-6)$。

$3 \times (-8) = -24$，$4 \times (-6) = -24$。$-24 = -24$。✓

---

**2.** 计算 $\frac{2}{3} + \frac{5}{7}$。

$$\frac{2}{3} + \frac{5}{7} = \frac{2 \times 7 + 5 \times 3}{3 \times 7} = \frac{14 + 15}{21} = \frac{29}{21}$$

$\gcd(29, 21) = 1$（$29$ 是质数），所以 $\frac{29}{21}$ 已是最简分数。

---

**3.** 将循环小数转化为分数。

**(a)** $x = 0.\overline{3}$。$10x = 3.\overline{3}$。$10x - x = 3$。$9x = 3$。$x = \frac{1}{3}$。

**(b)** $x = 0.\overline{12}$。$100x = 12.\overline{12}$。$100x - x = 12$。$99x = 12$。$x = \frac{12}{99} = \frac{4}{33}$。

**(c)** $x = 0.1\overline{6} = 0.1666\ldots$

$10x = 1.\overline{6}$。

设 $y = 0.\overline{6}$，则 $10y = 6.\overline{6}$，$9y = 6$，$y = \frac{2}{3}$。

$10x = 1 + y = 1 + \frac{2}{3} = \frac{5}{3}$。$x = \frac{5}{30} = \frac{1}{6}$。

---

**4.** 判断有限小数还是循环小数。

**(a)** $\frac{7}{40}$：$40 = 2^3 \times 5$，质因子只有 $2$ 和 $5$。**有限小数**。（$\frac{7}{40} = 0.175$）

**(b)** $\frac{11}{30}$：$30 = 2 \times 3 \times 5$，含质因子 $3$。**循环小数**。

**(c)** $\frac{1}{125}$：$125 = 5^3$，质因子只有 $5$。**有限小数**。（$\frac{1}{125} = 0.008$）

---

**5.** 证明 $\frac{1}{3}$ 和 $\frac{1}{2}$ 之间有无穷多个有理数。

构造方法：对 $n = 1, 2, 3, \ldots$，定义

$$r_n = \frac{1}{3} + \frac{1}{n+6}$$

当 $n$ 充分大时（$n \geq 1$），$\frac{1}{n + 6} \leq \frac{1}{7} < \frac{1}{6} = \frac{1}{2} - \frac{1}{3}$，所以 $r_n < \frac{1}{2}$。✓

而 $r_n > \frac{1}{3}$（因为 $\frac{1}{n+6} > 0$）。✓

不同的 $n$ 给出不同的 $r_n$（因为 $\frac{1}{n+6}$ 严格递减）。因此 $\{r_1, r_2, r_3, \ldots\}$ 是无穷多个位于 $\frac{1}{3}$ 和 $\frac{1}{2}$ 之间的有理数。$\blacksquare$

另一种更简单的方法：反复取中点。$r_1 = \frac{5}{12}$，$r_2 = \frac{1/3 + 5/12}{2} = \frac{3}{8}$，以此类推，永远得不到重复。

---

**6.** 证明 $\sqrt{3}$ 是无理数。

假设 $\sqrt{3} = \frac{p}{q}$，$\gcd(p, q) = 1$。则 $3q^2 = p^2$。

$p^2$ 被 $3$ 整除，所以 $p$ 被 $3$ 整除（因为 $3$ 是素数）。设 $p = 3k$。

代入：$3q^2 = 9k^2$，即 $q^2 = 3k^2$。

$q^2$ 被 $3$ 整除，所以 $q$ 被 $3$ 整除。

$p$ 和 $q$ 都被 $3$ 整除，矛盾于 $\gcd(p, q) = 1$。

因此 $\sqrt{3} \notin \mathbb{Q}$。$\blacksquare$

---

**7.** 证明 $\sqrt{2} + \sqrt{3}$ 是无理数。

假设 $\sqrt{2} + \sqrt{3} = r \in \mathbb{Q}$。

则 $\sqrt{3} = r - \sqrt{2}$。两边平方：

$$3 = r^2 - 2r\sqrt{2} + 2$$

$$2r\sqrt{2} = r^2 - 1$$

若 $r \neq 0$（显然 $r > 0$），则 $\sqrt{2} = \frac{r^2 - 1}{2r}$。

右边是有理数（有理数的运算封闭），所以 $\sqrt{2}$ 是有理数，矛盾。

因此 $\sqrt{2} + \sqrt{3} \notin \mathbb{Q}$。$\blacksquare$

---

**8.** 证明有理数加法的良定义性。

设 $(a,b) \sim (a',b')$ 且 $(c,d) \sim (c',d')$，即 $ad' = ba'$（条件 ①）且 $cd' = dc'$（条件 ②）。

（注意此处 $b, d, b', d' \neq 0$。）

加法定义：$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$。

需证 $(ad + bc, bd) \sim (a'd' + b'c', b'd')$，即 $(ad + bc) \cdot b'd' = bd \cdot (a'd' + b'c')$。

LHS $= adb'd' + bcb'd'$。

RHS $= bda'd' + bdb'c'$。

由 ①：$ab' = ba'$（因为 $ad' = ba' \Leftrightarrow \frac{a}{b} = \frac{a'}{b'}$，即 $ab' = a'b$）。

等等，让我重新整理。条件是 $(a,b) \sim (a',b')$ 意味着 $ab' = a'b$，$(c,d) \sim (c',d')$ 意味着 $cd' = c'd$。

需证 $(ad + bc) \cdot b'd' = bd \cdot (a'd' + b'c')$。

LHS $= adb'd' + bcb'd'$。

RHS $= bda'd' + bdb'c'$。

$adb'd' = (ab')dd' = (a'b)dd' = bda'd'$。（利用 $ab' = a'b$）

$bcb'd' = b(cd')b' = b(c'd)b' = bdb'c'$。（利用 $cd' = c'd$）

因此 LHS $=$ RHS。$\blacksquare$

---

**9.** 证明有理数与无理数之积（有理数不为零）是无理数。

设 $r \in \mathbb{Q}$，$r \neq 0$，$\alpha \notin \mathbb{Q}$。假设 $r\alpha = s \in \mathbb{Q}$。

则 $\alpha = \frac{s}{r}$。因为 $s, r \in \mathbb{Q}$ 且 $r \neq 0$，$\frac{s}{r} \in \mathbb{Q}$。

但 $\alpha \notin \mathbb{Q}$，矛盾。因此 $r\alpha \notin \mathbb{Q}$。$\blacksquare$

---

**10.** 反驳：两个无理数之和不一定是无理数。

反例：$\sqrt{2}$ 和 $-\sqrt{2}$ 都是无理数，但 $\sqrt{2} + (-\sqrt{2}) = 0 \in \mathbb{Q}$。

类似地，$\sqrt{2}$ 和 $(1 - \sqrt{2})$ 都是无理数，但 $\sqrt{2} + (1 - \sqrt{2}) = 1 \in \mathbb{Q}$。

因此命题为假。$\blacksquare$

---

## §3 实数（Real Numbers）

**1.** 求上确界和下确界。

**(a)** $S = \{1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \ldots\} = \{\frac{1}{n} : n \in \mathbb{Z}^+\}$。

$\sup S = 1$（$1 \in S$ 且 $1$ 是最大元素）。

$\inf S = 0$：$\frac{1}{n} > 0$ 对所有 $n$，所以 $0$ 是下界。对任意 $\epsilon > 0$，存在 $N$ 使得 $\frac{1}{N} < \epsilon$（Archimedean 性质），所以 $0$ 是最大下界。$0 \notin S$。

**(b)** $(0, 1]$。$\sup(0, 1] = 1$（$1$ 是最大元素）。$\inf(0, 1] = 0$（$0$ 不属于集合，但是最大下界）。

**(c)** $\{x \in \mathbb{R} : x^2 < 9\} = (-3, 3)$。$\sup = 3$，$\inf = -3$。两者都不属于集合。

---

**2.** 用区间记号表示集合。

**(a)** $(-2, 5]$

**(b)** $[3, +\infty)$

**(c)** $|x - 1| < 2 \iff -2 < x - 1 < 2 \iff -1 < x < 3$，即 $(-1, 3)$。

---

**3.** $[1, 4] \cap [2, 6] = [2, 4]$；$[1, 4] \cup [2, 6] = [1, 6]$。

---

**4.** 证明 Archimedean 性质的等价表述。

给定 $\epsilon > 0$，取 $x = \epsilon$，$y = 1$。由 Archimedean 性质，存在正整数 $n$ 使得 $n\epsilon > 1$，即 $\frac{1}{n} < \epsilon$。$\blacksquare$

反过来：给定 $x > 0$，$y > 0$，取 $\epsilon = \frac{x}{y} > 0$（若 $y > 0$）。由等价形式，存在正整数 $n$ 使得 $\frac{1}{n} < \frac{x}{y}$，即 $y < nx$。$\blacksquare$

---

**5.** 证明 $\sup\left\{\frac{n}{2n+1} : n \in \mathbb{N}\right\} = \frac{1}{2}$。

设 $S = \left\{\frac{n}{2n+1} : n \in \mathbb{N}\right\}$。

**上界**：$\frac{n}{2n+1} = \frac{1}{2} \cdot \frac{2n}{2n+1} = \frac{1}{2}\left(1 - \frac{1}{2n+1}\right) < \frac{1}{2}$。所以 $\frac{1}{2}$ 是上界。

**最小性**：对任意 $\epsilon > 0$，需找 $n$ 使得 $\frac{n}{2n+1} > \frac{1}{2} - \epsilon$。

$\frac{n}{2n+1} > \frac{1}{2} - \epsilon \iff \frac{1}{2} - \frac{1}{2(2n+1)} > \frac{1}{2} - \epsilon \iff \frac{1}{2(2n+1)} < \epsilon \iff n > \frac{1 - 2\epsilon}{4\epsilon}$。

由 Archimedean 性质，这样的 $n$ 存在。因此 $\frac{1}{2}$ 是最小上界。$\sup S = \frac{1}{2}$。$\blacksquare$

---

**6.** 证明 $\sup(A \cup B) = \max(\sup A, \sup B)$。

设 $M_A = \sup A$，$M_B = \sup B$，$M = \max(M_A, M_B)$。

**$M$ 是 $A \cup B$ 的上界**：对任意 $x \in A \cup B$，若 $x \in A$ 则 $x \leq M_A \leq M$；若 $x \in B$ 则 $x \leq M_B \leq M$。

**$M$ 是最小上界**：不妨设 $M = M_A$（即 $M_A \geq M_B$）。对任意 $\epsilon > 0$，由 $M_A = \sup A$，存在 $a \in A$ 使得 $a > M_A - \epsilon = M - \epsilon$。而 $a \in A \cup B$，所以 $M - \epsilon$ 不是 $A \cup B$ 的上界。

因此 $\sup(A \cup B) = M = \max(\sup A, \sup B)$。$\blacksquare$

---

**7.** 证明反三角不等式 $\big||a| - |b|\big| \leq |a - b|$。

由三角不等式：$|a| = |(a - b) + b| \leq |a - b| + |b|$，即 $|a| - |b| \leq |a - b|$。

交换 $a, b$：$|b| - |a| \leq |b - a| = |a - b|$。

因此 $-(|a - b|) \leq |a| - |b| \leq |a - b|$，即 $\big||a| - |b|\big| \leq |a - b|$。$\blacksquare$

---

**8.** 证明任意两个实数之间存在无理数。

设 $a < b$。由有理数的稠密性，存在有理数 $r$ 使得 $a - \sqrt{2} < r < b - \sqrt{2}$。

令 $\alpha = r + \sqrt{2}$。则 $a < \alpha < b$。

若 $\alpha \in \mathbb{Q}$，则 $\sqrt{2} = \alpha - r \in \mathbb{Q}$（有理数的差是有理数），矛盾于 $\sqrt{2} \notin \mathbb{Q}$。

因此 $\alpha$ 是 $a$ 和 $b$ 之间的无理数。$\blacksquare$

---

**9.** 计算 $\displaystyle\bigcup_{n=1}^{\infty} \left[0, 1 - \frac{1}{n}\right]$。

$$\bigcup_{n=1}^{\infty} \left[0, 1 - \frac{1}{n}\right] = \{x \in \mathbb{R} : \exists n \in \mathbb{Z}^+,\; 0 \leq x \leq 1 - \frac{1}{n}\}$$

$$= \{x \in \mathbb{R} : 0 \leq x < 1\} = [0, 1)$$

**证明 "$\subseteq$"**：若 $x \in \left[0, 1 - \frac{1}{n}\right]$ 对某个 $n$，则 $0 \leq x \leq 1 - \frac{1}{n} < 1$。

**证明 "$\supseteq$"**：若 $0 \leq x < 1$，令 $\epsilon = 1 - x > 0$。由 Archimedean 性质，存在正整数 $n$ 使得 $\frac{1}{n} < \epsilon = 1 - x$，即 $x < 1 - \frac{1}{n}$。因此 $x \in \left[0, 1 - \frac{1}{n}\right]$。

结果是**半开区间** $[0, 1)$——既不是开区间，也不是闭区间。$\blacksquare$

---

**10.** 证明 $\inf B = -\sup A$，其中 $B = \{-a : a \in A\}$。

设 $M = \sup A$。

**$-M$ 是 $B$ 的下界**：对任意 $-a \in B$（即 $a \in A$），有 $a \leq M$，故 $-a \geq -M$。

**$-M$ 是最大下界**：设 $L$ 是 $B$ 的任意下界。则对所有 $a \in A$，$-a \geq L$，即 $a \leq -L$。因此 $-L$ 是 $A$ 的上界。由 $\sup A = M$，有 $M \leq -L$，即 $L \leq -M$。

因此 $-M$ 是 $B$ 的最大下界，即 $\inf B = -M = -\sup A$。$\blacksquare$

---

## §4 复数引入（Introduction to Complex Numbers）

**1.** 计算实部和虚部。

**(a)** $(2 + 3i) + (4 - i) = 6 + 2i$。实部 $6$，虚部 $2$。

**(b)** $(1 + i)(1 - i) = 1 - i^2 = 1 + 1 = 2$。实部 $2$，虚部 $0$（这是一个实数）。

**(c)** $i^{100}$：$100 = 4 \times 25$，所以 $i^{100} = (i^4)^{25} = 1^{25} = 1$。实部 $1$，虚部 $0$。

---

**2.** 计算模。

$|3 + 4i| = \sqrt{9 + 16} = \sqrt{25} = 5$。

$|5 - 12i| = \sqrt{25 + 144} = \sqrt{169} = 13$。

$|1 + i| = \sqrt{1 + 1} = \sqrt{2}$。

---

**3.** 计算 $z\bar{z}$ 并验证。

$z = 2 + i$，$\bar{z} = 2 - i$。

$z\bar{z} = (2 + i)(2 - i) = 4 - i^2 = 4 + 1 = 5$。

$|z|^2 = 2^2 + 1^2 = 5$。✓

---

**4.** 计算 $\frac{1 + 2i}{3 - 4i}$。

$$\frac{1 + 2i}{3 - 4i} = \frac{(1 + 2i)(3 + 4i)}{(3 - 4i)(3 + 4i)} = \frac{3 + 4i + 6i + 8i^2}{9 + 16} = \frac{3 + 10i - 8}{25} = \frac{-5 + 10i}{25} = -\frac{1}{5} + \frac{2}{5}i$$

---

**5.** 证明 $\overline{zw} = \bar{z} \cdot \bar{w}$。

设 $z = a + bi$，$w = c + di$。

$zw = (ac - bd) + (ad + bc)i$。

$\overline{zw} = (ac - bd) - (ad + bc)i$。

$\bar{z} \cdot \bar{w} = (a - bi)(c - di) = ac - adi - bci + bdi^2 = (ac - bd) - (ad + bc)i$。

两者相等。$\blacksquare$

---

**6.** 求 $z^2 + 4z + 13 = 0$ 的复数解。

用求根公式：$z = \frac{-4 \pm \sqrt{16 - 52}}{2} = \frac{-4 \pm \sqrt{-36}}{2} = \frac{-4 \pm 6i}{2} = -2 \pm 3i$。

解为 $z = -2 + 3i$ 和 $z = -2 - 3i$。

验证：$(-2 + 3i)^2 + 4(-2 + 3i) + 13 = (4 - 12i - 9) + (-8 + 12i) + 13 = -5 - 8 + 13 = 0$。✓

---

**7.** 证明 $|zw| = |z| \cdot |w|$。

$$|zw|^2 = (zw)\overline{(zw)} = (zw)(\bar{z}\bar{w}) = (z\bar{z})(w\bar{w}) = |z|^2 |w|^2$$

两边取正平方根：$|zw| = |z| \cdot |w|$。$\blacksquare$

---

**8.** 证明 $z$ 是实数 $\iff z = \bar{z}$。

设 $z = a + bi$。

$(\Rightarrow)$ 若 $z$ 是实数，则 $b = 0$，$\bar{z} = a - 0i = a = z$。

$(\Leftarrow)$ 若 $z = \bar{z}$，则 $a + bi = a - bi$，比较虚部得 $b = -b$，即 $2b = 0$，$b = 0$。因此 $z = a$ 是实数。$\blacksquare$

---

**9.** 找出 $x^4 + 1 = 0$ 的所有复数根。

$x^4 = -1 = e^{i\pi}$。

四次根：$x = e^{i(\pi + 2k\pi)/4}$，$k = 0, 1, 2, 3$。

$k = 0$：$x = e^{i\pi/4} = \cos\frac{\pi}{4} + i\sin\frac{\pi}{4} = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i$

$k = 1$：$x = e^{i3\pi/4} = -\frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}i$

$k = 2$：$x = e^{i5\pi/4} = -\frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}i$

$k = 3$：$x = e^{i7\pi/4} = \frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}i$

即 $x = \frac{\pm\sqrt{2} \pm\sqrt{2}\,i}{2}$（四种符号组合）。

**不用极坐标的方法**：$x^4 + 1 = (x^2 + \sqrt{2}x + 1)(x^2 - \sqrt{2}x + 1)$。

对 $x^2 + \sqrt{2}x + 1 = 0$：$x = \frac{-\sqrt{2} \pm \sqrt{2 - 4}}{2} = \frac{-\sqrt{2} \pm \sqrt{-2}}{2} = \frac{-\sqrt{2} \pm \sqrt{2}\,i}{2}$。

对 $x^2 - \sqrt{2}x + 1 = 0$：$x = \frac{\sqrt{2} \pm \sqrt{2 - 4}}{2} = \frac{\sqrt{2} \pm \sqrt{2}\,i}{2}$。

结果一致。

---

**10.** 证明实系数多项式的复数根成共轭对。

设 $p(x) = a_n x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0$，其中 $a_k \in \mathbb{R}$。

**关键引理**：$\overline{p(z)} = p(\bar{z})$。

$$\overline{p(z)} = \overline{a_n z^n + \cdots + a_0} = \overline{a_n z^n} + \cdots + \overline{a_0}$$

$$= \overline{a_n}\,\overline{z^n} + \cdots + \overline{a_0} = a_n \bar{z}^n + \cdots + a_0 = p(\bar{z})$$

（用到了 $\overline{a_k} = a_k$（因为 $a_k \in \mathbb{R}$），$\overline{z^n} = \bar{z}^n$，以及共轭对加法和乘法的分配性。）

若 $z_0$ 是根：$p(z_0) = 0$。则 $p(\bar{z}_0) = \overline{p(z_0)} = \overline{0} = 0$。

因此 $\bar{z}_0$ 也是 $p(x) = 0$ 的根。$\blacksquare$
