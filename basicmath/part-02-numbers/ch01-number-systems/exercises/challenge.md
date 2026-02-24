# 第 1 章 数系 — 挑战题（Challenge Problems）

以下挑战题综合运用本章关于数系构造和性质的知识，难度超出常规练习。

---

## 挑战题 1：有理数域的严格构造

从整数 $\mathbb{Z}$ 出发，严格构造有理数域 $\mathbb{Q}$，并验证域公理。

**(a)** 定义集合 $F = \mathbb{Z} \times (\mathbb{Z} \setminus \{0\})$ 上的等价关系 $\sim$：$(a, b) \sim (c, d) \iff ad = bc$。证明 $\sim$ 确实是等价关系。

**(b)** 在商集 $F / {\sim}$ 上定义加法和乘法：
$$[(a, b)] + [(c, d)] = [(ad + bc, bd)]$$
$$[(a, b)] \cdot [(c, d)] = [(ac, bd)]$$
证明这两个运算是**良定义的**（与代表元的选取无关）。

**(c)** 验证 $(F/{\sim}, +, \cdot)$ 满足域公理：加法交换律、加法结合律、加法单位元、加法逆元、乘法交换律、乘法结合律、乘法单位元、非零元素的乘法逆元、分配律。

### 提示

- (a) 传递性需要分 $c = 0$ 和 $c \neq 0$ 两种情况讨论。
- (b) 良定义性的证明：假设 $(a, b) \sim (a', b')$ 和 $(c, d) \sim (c', d')$，需要证明运算结果仍在同一等价类中。乘法的良定义性较直接（$ab' = a'b$ 且 $cd' = c'd$ $\Rightarrow$ $acb'd' = a'c'bd$）。加法需要更细致的运算。
- (c) 逐一验证九条公理。加法单位元是 $[(0, 1)]$，乘法单位元是 $[(1, 1)]$，$[(a, b)]$ 的加法逆元是 $[(-a, b)]$，$[(a, b)]$（$a \neq 0$）的乘法逆元是 $[(b, a)]$。

### 解答大纲

**(a)** 等价关系的验证。

**自反性**：$ab = ba$（整数乘法交换律）。✓

**对称性**：若 $ad = bc$，则 $cb = da$。✓

**传递性**：设 $ad = bc$ 且 $cf = de$。

- 若 $c \neq 0$：$(ad)(cf) = (bc)(de)$，即 $acdf = bcde$。消去 $cd \neq 0$：$af = be$。✓
- 若 $c = 0$：由 $ad = bc = 0$ 且 $d \neq 0$ 得 $a = 0$。由 $cf = 0 = de$ 且 $d \neq 0$ 得 $e = 0$。则 $af = 0 = be$。✓

**(b)** 良定义性。

**乘法**：设 $ab' = a'b$，$cd' = c'd$。则 $ac \cdot b'd' = ab' \cdot cd' = a'b \cdot c'd = a'c' \cdot bd$。即 $(ac, bd) \sim (a'c', b'd')$。✓

**加法**：设 $ab' = a'b$，$cd' = c'd$。需证 $(ad + bc) \cdot b'd' = bd \cdot (a'd' + b'c')$。

LHS $= adb'd' + bcb'd'$。利用 $ab' = a'b$：$adb'd' = ab' \cdot dd' = a'b \cdot dd' = a'd' \cdot bd$。利用 $cd' = c'd$：$bcb'd' = b \cdot cd' \cdot b' = b \cdot c'd \cdot b' = b'c' \cdot bd$。

因此 LHS $= a'd' \cdot bd + b'c' \cdot bd = bd(a'd' + b'c') = $ RHS。✓

**(c)** 域公理验证（大纲）。

| 公理 | 验证要点 |
|------|----------|
| 加法交换律 | $ad + bc = cb + da$（整数加法交换律） |
| 加法结合律 | 展开后利用整数的结合律和分配律 |
| 加法单位元 $[(0, 1)]$ | $[(a, b)] + [(0, 1)] = [(a \cdot 1 + b \cdot 0, b \cdot 1)] = [(a, b)]$ |
| 加法逆元 $[(-a, b)]$ | $[(a, b)] + [(-a, b)] = [(ab - ab, b^2)] = [(0, b^2)] \sim [(0, 1)]$ |
| 乘法交换律 | $ac = ca$，$bd = db$ |
| 乘法结合律 | $(ac)e = a(ce)$，$(bd)f = b(df)$ |
| 乘法单位元 $[(1, 1)]$ | $[(a, b)] \cdot [(1, 1)] = [(a, b)]$ |
| 乘法逆元 $[(b, a)]$（$a \neq 0$） | $[(a, b)] \cdot [(b, a)] = [(ab, ab)] \sim [(1, 1)]$ |
| 分配律 | 展开验证 $[(a,b)] \cdot ([(c,d)] + [(e,f)]) = [(a,b)] \cdot [(c,d)] + [(a,b)] \cdot [(e,f)]$ |

$\blacksquare$

---

## 挑战题 2：有理数和无理数的稠密性

证明：在任意两个不同的实数之间，既存在有理数，也存在无理数。

更精确地：

**(a)** 设 $a, b \in \mathbb{R}$，$a < b$。证明存在 $r \in \mathbb{Q}$ 使得 $a < r < b$。

**(b)** 设 $a, b \in \mathbb{R}$，$a < b$。证明存在无理数 $\alpha$ 使得 $a < \alpha < b$。

**(c)** 推广：证明在任意两个不同的实数之间，有**无穷多**个有理数和**无穷多**个无理数。

### 提示

- (a) 利用 Archimedean 性质找到"足够细"的网格 $\frac{m}{n}$。
- (b) 用 (a) 的结果加上一个无理数"偏移"。
- (c) 将区间反复细分。

### 解答大纲

**(a)** 有理数的稠密性。

由 Archimedean 性质，存在正整数 $n$ 使得 $n(b - a) > 1$，即 $\frac{1}{n} < b - a$。

取 $m = \lfloor na \rfloor + 1$。则 $na < m \leq na + 1$。

$a < \frac{m}{n}$：因为 $m > na$。

$\frac{m}{n} < b$：因为 $m \leq na + 1 < na + n(b - a) = nb$。

令 $r = \frac{m}{n}$，则 $a < r < b$ 且 $r \in \mathbb{Q}$。$\blacksquare$

**(b)** 无理数的稠密性。

由 (a)，存在 $r \in \mathbb{Q}$ 使得 $a - \sqrt{2} < r < b - \sqrt{2}$。

令 $\alpha = r + \sqrt{2}$。则 $a < \alpha < b$。

若 $\alpha \in \mathbb{Q}$，则 $\sqrt{2} = \alpha - r \in \mathbb{Q}$，矛盾。因此 $\alpha \notin \mathbb{Q}$。$\blacksquare$

**(c)** 推广到无穷多个。

**有理数**：由 (a)，存在 $r_1 \in \mathbb{Q}$ 使得 $a < r_1 < b$。再由 (a)，存在 $r_2 \in \mathbb{Q}$ 使得 $a < r_2 < r_1$。继续此过程，得到无穷序列 $r_1 > r_2 > r_3 > \cdots$，全部位于 $(a, b)$ 中。这些有理数互不相同（严格递减），因此是无穷多个。

**无理数**：同理，用 (b) 反复在更小的子区间中找无理数。或者：对每个正整数 $k$，在 $(a, b)$ 中取有理数 $r_k$，令 $\alpha_k = r_k + \frac{\sqrt{2}}{k}$。当 $k$ 足够大时，$\alpha_k \in (a, b)$（因为 $\frac{\sqrt{2}}{k} \to 0$）。不同的 $k$ 给出不同的 $\alpha_k$（因为若 $\alpha_j = \alpha_k$，则 $r_j - r_k = \sqrt{2}(\frac{1}{k} - \frac{1}{j})$，左边有理右边无理，矛盾于 $j \neq k$）。$\blacksquare$

---

## 挑战题 3：代数数的可数性

证明全体代数数（algebraic numbers）的集合是可数的。由此推论：超越数（transcendental numbers）的集合是不可数的。

**(a)** 证明：对于固定的正整数 $n$ 和正整数 $H$，满足 $|a_0| + |a_1| + \cdots + |a_n| \leq H$ 的整系数多项式 $a_n x^n + \cdots + a_0$（$a_n \neq 0$，次数恰好为 $n$）只有有限多个。

**(b)** 证明：每个 $n$ 次整系数多项式至多有 $n$ 个根（在 $\mathbb{C}$ 中）。

**(c)** 利用 (a) 和 (b)，证明代数数的集合 $\mathbb{A}$ 是可数的。

**(d)** 推论：超越数集合 $\mathbb{R} \setminus \mathbb{A}$ 是不可数的。

### 提示

- (a) 每个系数 $a_i$ 的取值范围是有限集（$|a_i|$ 有上界），所以系数的组合数有限。
- (b) 这是代数的基本事实（可由因式分解推导）。
- (c) 可数个有限集的并是可数的。更精确地：代数数 = $\bigcup_{n=1}^{\infty} \bigcup_{H=1}^{\infty}$ "次数 $\leq n$、系数绝对值之和 $\leq H$ 的多项式的根"。
- (d) 若 $\mathbb{A}$ 可数且 $\mathbb{R} = \mathbb{A} \cup (\mathbb{R} \setminus \mathbb{A})$，若 $\mathbb{R} \setminus \mathbb{A}$ 也可数，则 $\mathbb{R}$ 可数，矛盾。

### 解答大纲

**(a)** 固定 $n$ 和 $H$，系数 $(a_0, a_1, \ldots, a_n)$ 满足 $|a_0| + |a_1| + \cdots + |a_n| \leq H$，$a_n \neq 0$。每个 $a_i$ 是整数且 $|a_i| \leq H$，所以 $a_i \in \{-H, \ldots, H\}$，有 $2H + 1$ 种选择。

总共至多 $(2H + 1)^{n+1}$ 个多项式。这是有限的。$\blacksquare$

**(b)** $n$ 次多项式至多有 $n$ 个根。这可以通过因式定理归纳证明：若 $r$ 是 $p(x)$ 的根，则 $p(x) = (x - r)q(x)$，其中 $q(x)$ 的次数为 $n - 1$。归纳地，$q(x)$ 至多有 $n - 1$ 个根，所以 $p(x)$ 至多有 $n$ 个根。$\blacksquare$

**(c)** 定义"高度"（height）$h(p) = n + H$，其中 $n$ 是次数，$H = |a_0| + |a_1| + \cdots + |a_n|$。

对每个正整数 $k$，设 $A_k$ = 高度 $\leq k$ 的所有整系数多项式的根的集合。

由 (a)，高度 $\leq k$ 的多项式只有有限多个。由 (b)，每个多项式至多有有限个根。因此 $A_k$ 是有限集。

代数数集 $\mathbb{A} = \bigcup_{k=1}^{\infty} A_k$——可数个有限集的并是可数集（Part 1 Ch02 §4）。$\blacksquare$

**(d)** $\mathbb{R} = \mathbb{A} \cup (\mathbb{R} \setminus \mathbb{A})$。

$\mathbb{A}$ 可数（由 (c)）。若 $\mathbb{R} \setminus \mathbb{A}$ 也可数，则 $\mathbb{R}$ 是两个可数集的并，因此可数。

但 $\mathbb{R}$ 不可数（Cantor 对角线论证，Part 1 Ch02 §4），矛盾。

因此 $\mathbb{R} \setminus \mathbb{A}$ 不可数。即超越数集合是不可数的。

推论：超越数比代数数"多得多"——尽管我们能叫出名字的数（$\pi, e$ 等）屈指可数，但"大多数"实数是超越数。$\blacksquare$
