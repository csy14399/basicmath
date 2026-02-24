# 第 2 章 实数的深入 — 练习题解答

## §1 实数的性质

**1.** 证明：若 $a > 0$，则 $-a < 0$。

> **解**：$a > 0$ 意味着 $0 < a$。由加法保序（O4），两边加 $(-a)$：
>
> $$0 + (-a) < a + (-a) \implies -a < 0 \qquad \blacksquare$$

---

**2.** 证明：若 $a < 0$ 且 $b < 0$，则 $ab > 0$。

> **解**：由第 1 题，$-a > 0$ 且 $-b > 0$。由正元素乘法保序（O5，以 $0 \leq -a, -b$），$(-a)(-b) > 0$。
>
> 而 $(-a)(-b) = ab$（由域公理推出：$(-a)(-b) = (-1)(a)(-1)(b) = (-1)(-1)ab = ab$）。
>
> 故 $ab > 0$。$\blacksquare$

---

**3.** 证明：在有序域中，若 $0 < a < b$，则 $a^2 < b^2$。

> **解**：$b^2 - a^2 = (b - a)(b + a)$。
>
> 由 $a < b$，$b - a > 0$。由 $0 < a$ 和 $0 < b$，$b + a > 0$。
>
> 由正元素乘法保序，$(b - a)(b + a) > 0$，即 $b^2 - a^2 > 0$，故 $a^2 < b^2$。$\blacksquare$

---

**4.** 证明整数部分 $\lfloor x \rfloor$ 的存在性和唯一性。

> **解**：**存在性**：设 $x \in \mathbb{R}$。
>
> 由阿基米德性质，存在 $N_1 \in \mathbb{N}$ 使得 $N_1 > x$，即 $x < N_1$。同样存在 $N_2 \in \mathbb{N}$ 使得 $N_2 > -x$，即 $-N_2 < x$。
>
> 考虑集合 $S = \{k \in \mathbb{Z} : k \leq x\}$。$S$ 非空（$-N_2 \in S$）且有上界（$N_1$）。由整数的良序性（取 $\{k \in \mathbb{Z} : k > x\}$ 的最小元素 $m$，则 $n = m - 1$ 满足 $n \leq x < n + 1$），存在 $n \in \mathbb{Z}$ 使得 $n \leq x < n + 1$。
>
> **唯一性**：若 $n, n'$ 都满足条件且 $n \neq n'$，不妨设 $n < n'$，则 $n' \geq n + 1$，故 $x \geq n' \geq n + 1$，与 $x < n + 1$ 矛盾。$\blacksquare$

---

**5.** 证明 $(a, b)$ 中有无穷多个有理数。

> **解**：由有理数稠密性，存在 $q_1 \in \mathbb{Q}$ 使得 $a < q_1 < b$。
>
> 再由稠密性，存在 $q_2 \in \mathbb{Q}$ 使得 $a < q_2 < q_1$。
>
> 归纳地，对每个 $n$，存在 $q_{n+1} \in \mathbb{Q}$ 使得 $a < q_{n+1} < q_n$。
>
> 这样构造的 $q_1 > q_2 > q_3 > \cdots$ 两两不同，都属于 $(a, b)$。故 $(a, b)$ 包含无穷多个有理数。$\blacksquare$

---

**6.** 证明三角不等式的推广。

> **解**：用数学归纳法。
>
> **基础情形**：$n = 1$ 时，$|a_1| \leq |a_1|$，显然成立。$n = 2$ 时即三角不等式。
>
> **归纳步骤**：假设对 $n = k$ 成立。对 $n = k + 1$：
>
> $$|a_1 + \cdots + a_k + a_{k+1}| \leq |a_1 + \cdots + a_k| + |a_{k+1}| \leq (|a_1| + \cdots + |a_k|) + |a_{k+1}|$$
>
> 第一个不等式用了三角不等式，第二个用了归纳假设。$\blacksquare$

---

**7.** 证明 $\{a + nb : n \in \mathbb{Z}\}$ 在 $\mathbb{R}$ 中稠密。

> **解**：设 $x < y$。需要找 $n \in \mathbb{Z}$ 使得 $x < a + nb < y$，即 $(x - a)/b < n < (y - a)/b$。
>
> 由 $y - x > 0$ 和 $b > 0$，$(y - a)/b - (x - a)/b = (y - x)/b > 0$。
>
> 由阿基米德性质，存在 $N \in \mathbb{N}^+$ 使得 $N > b/(y-x)$，但这里我们需要的是在长度为 $(y-x)/b$ 的开区间中找到一个整数。
>
> 由阿基米德性质（取整数部分），区间 $((x-a)/b, (y-a)/b)$ 的长度为 $(y-x)/b > 0$。由整数部分的性质（第 4 题），取 $n = \lfloor (x-a)/b \rfloor + 1$。若 $(y-x)/b > 1$，则 $n < (y-a)/b$，满足要求。
>
> 一般情况：由阿基米德性质，存在正整数 $k$ 使得 $k(y-x)/b > 1$。将区间 $((x-a)/b, (y-a)/b)$ 分成 $k$ 段，至少有一段长度 $> 1/k \cdot k(y-x)/b/(y-x) \cdot b$... 
>
> 更简洁地：由阿基米德性质，存在正整数 $m$ 使得 $mb > y - x$... 不对，$b$ 是固定的。
>
> 实际上更直接：$(y-x)/b > 0$，由阿基米德性质，存在正整数 $N$ 使得 $N \cdot (y-x)/b > 1$，但这没用。
>
> 正确方法：令 $c = (x - a)/b$，$d = (y - a)/b$，则 $d - c = (y - x)/b > 0$。问题变成：证明开区间 $(c, d)$ 中存在整数。
>
> 由阿基米德性质（第 4 题的下取整），取 $n = \lfloor c \rfloor + 1$。则 $n > c$。需要 $n < d$，即 $\lfloor c \rfloor + 1 < d$。这在 $d - c \geq 1$ 时成立。
>
> 当 $d - c < 1$ 时，可能 $(c, d)$ 中没有整数。但题目没有要求 $(y-x)/b \geq 1$。
>
> 修正：实际上 $(c, d)$ 中存在整数当且仅当 $\lfloor c \rfloor + 1 < d$，即 $\lceil c+1 \rceil \leq \lfloor d \rfloor$... 不一定成立。
>
> 重新审视问题。需要的是 $x < a + nb < y$，即需要整数 $n$ 使得 $(x-a)/b < n < (y-a)/b$。由有理数稠密性的证明方法（§1 定理 2），这等价于在长度 $(y-x)/b > 0$ 的区间中找整数。由阿基米德性质的推论（任何长度 $> 0$ 的区间中存在整数——等等，这不一定对）。
>
> 修正方案：任何长度 $> 1$ 的区间包含整数。所以当 $y - x > b$ 时直接成立。当 $y - x \leq b$ 时，注意 $\{a + nb : n \in \mathbb{Z}\}$ 是间距为 $b$ 的等间距点列，任何长度 $> b$ 的区间必包含至少一个点。但当 $y - x \leq b$ 时，也可能包含——取决于 $a$ 的位置。
>
> 实际上命题在一般情况下不成立！例如 $a = 0, b = 1$，则 $\{n : n \in \mathbb{Z}\}$ 就是所有整数，$(0.3, 0.7)$ 中没有整数。所以 $\{a + nb\}$ **不一定**在 $\mathbb{R}$ 中稠密。
>
> 题目可能要求 $b$ 是无理数，或应理解为 $b$ 与 $1$ 的比是无理数。但题目原文没有这个条件。
>
> 修正理解：题目可能有误，或者理解为"$\{a + nb : n \in \mathbb{Z}\} \cap (x, y) \neq \varnothing$ 对所有 $y - x > b$"。这是显然的。
>
> 作为习题解答，我们给出条件成立的正确版本：当 $y - x > b$ 时结论成立。$\blacksquare$

---

**8.** 构造嵌套闭区间使交集非单点。

> **解**：取 $[a_n, b_n] = [-1/n, 1 + 1/n]$，$n = 1, 2, 3, \ldots$
>
> 嵌套性：$a_n = -1/n$ 递增，$b_n = 1 + 1/n$ 递减，故 $[a_{n+1}, b_{n+1}] \subseteq [a_n, b_n]$。
>
> $b_n - a_n = 1 + 2/n \to 1 \neq 0$。
>
> 公共交集：$\bigcap [a_n, b_n] = [0, 1]$（包含无穷多个点）。
>
> 这说明条件"$b_n - a_n \to 0$"是唯一性所必需的。$\blacksquare$

---

## §2 实数的完备性

**9.** 求上确界和下确界。

> **解**：
>
> (a) $S = \{1/n : n \in \mathbb{N}^+\} = \{1, 1/2, 1/3, \ldots\}$。
>
> $\sup S = 1$（在 $n = 1$ 时取到）。$\inf S = 0$（§1 推论 1）。
>
> (b) $S = \{(-1)^n(1 + 1/n)\} = \{-2, 3/2, -4/3, 5/4, \ldots\}$。
>
> 偶数项：$1 + 1/n$（$n$ 为偶数），递减趋于 $1$，最大值 $3/2$（$n=2$）。
>
> 奇数项：$-(1 + 1/n)$（$n$ 为奇数），递增趋于 $-1$，最小值 $-2$（$n=1$）。
>
> $\sup S = 3/2$，$\inf S = -2$。
>
> (c) $S = \{x \in \mathbb{R} : x^3 < 8\} = (-\infty, 2)$。
>
> $\sup S = 2$（$2$ 是上界，且 $2 - \varepsilon \in S$ 对所有 $\varepsilon > 0$）。$\inf S$ 不存在（$S$ 无下界）。$\blacksquare$

---

**10.** 证明 $\sup(A \cup B) = \max(\sup A, \sup B)$。

> **解**：设 $\alpha = \sup A$，$\beta = \sup B$，$\gamma = \max(\alpha, \beta)$。
>
> **$\gamma$ 是 $A \cup B$ 的上界**：对任意 $x \in A \cup B$，若 $x \in A$ 则 $x \leq \alpha \leq \gamma$，若 $x \in B$ 则 $x \leq \beta \leq \gamma$。
>
> **$\gamma$ 是最小上界**：不妨设 $\gamma = \alpha$（即 $\alpha \geq \beta$）。对任意 $\varepsilon > 0$，存在 $a \in A$ 使得 $a > \alpha - \varepsilon = \gamma - \varepsilon$。因 $a \in A \cup B$，故 $\gamma - \varepsilon$ 不是 $A \cup B$ 的上界。$\blacksquare$

---

**11.** 证明 $\sup(cS) = c \cdot \sup S$（$c > 0$）。

> **解**：设 $\alpha = \sup S$。
>
> **$c\alpha$ 是 $cS$ 的上界**：对任意 $cs \in cS$（$s \in S$），$s \leq \alpha$，故 $cs \leq c\alpha$（$c > 0$）。
>
> **$c\alpha$ 是最小上界**：对任意 $\varepsilon > 0$，$\varepsilon/c > 0$，故存在 $s_0 \in S$ 使得 $s_0 > \alpha - \varepsilon/c$。则 $cs_0 > c\alpha - \varepsilon$，且 $cs_0 \in cS$。$\blacksquare$

---

**12.** 证明 $\sup(A - B) = \sup A - \inf B$。

> **解**：设 $\alpha = \sup A$，$\beta = \inf B$。
>
> **$\alpha - \beta$ 是 $A - B$ 的上界**：对任意 $a - b \in A - B$，$a \leq \alpha$ 且 $b \geq \beta$，故 $a - b \leq \alpha - \beta$。
>
> **$\alpha - \beta$ 是最小上界**：对任意 $\varepsilon > 0$，存在 $a_0 \in A$ 使得 $a_0 > \alpha - \varepsilon/2$，存在 $b_0 \in B$ 使得 $b_0 < \beta + \varepsilon/2$。则
>
> $$a_0 - b_0 > (\alpha - \varepsilon/2) - (\beta + \varepsilon/2) = \alpha - \beta - \varepsilon$$
>
> 故 $\alpha - \beta - \varepsilon$ 不是 $A - B$ 的上界。由 $\varepsilon$ 的任意性，$\alpha - \beta$ 是最小上界。$\blacksquare$
