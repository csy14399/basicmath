# 第 2 章 实数的深入 — 练习题

## §1 实数的性质（Properties of Real Numbers）

1. ★☆☆ 从有序域公理出发，证明：若 $a > 0$，则 $-a < 0$。

2. ★☆☆ 从有序域公理出发，证明：若 $a < 0$ 且 $b < 0$，则 $ab > 0$。

3. ★★☆ 证明：在有序域中，若 $0 < a < b$，则 $a^2 < b^2$。

4. ★★☆ 用阿基米德性质证明：对任意 $x \in \mathbb{R}$，存在唯一的整数 $n$ 使得 $n \leq x < n + 1$。（这个 $n$ 称为 $x$ 的**整数部分**或**下取整**，记作 $\lfloor x \rfloor$。）

5. ★★☆ 证明：对任意实数 $a < b$，开区间 $(a, b)$ 中包含无穷多个有理数。

6. ★★☆ 利用三角不等式证明：对任意 $a_1, a_2, \ldots, a_n \in \mathbb{R}$，
   $$|a_1 + a_2 + \cdots + a_n| \leq |a_1| + |a_2| + \cdots + |a_n|$$

7. ★★★ 设 $a, b \in \mathbb{R}$，$b > 0$。证明：集合 $\{a + nb : n \in \mathbb{Z}\}$ 在 $\mathbb{R}$ 中稠密。（即对任意 $x, y \in \mathbb{R}$，$x < y$，存在 $n \in \mathbb{Z}$ 使得 $x < a + nb < y$。）

8. ★★★ 证明区间套定理中条件"$b_n - a_n \to 0$"不可省略：构造嵌套闭区间 $[a_n, b_n]$ 使得 $\bigcap_{n=1}^{\infty}[a_n, b_n]$ 包含不止一个点。

---

## §2 实数的完备性（Completeness of Real Numbers）

9. ★☆☆ 求以下集合的上确界和下确界（若存在）：
   (a) $\{1/n : n \in \mathbb{N}^+\}$
   (b) $\{(-1)^n (1 + 1/n) : n \in \mathbb{N}^+\}$
   (c) $\{x \in \mathbb{R} : x^3 < 8\}$

10. ★★☆ 设 $A, B \subseteq \mathbb{R}$ 非空有上界。证明：$\sup(A \cup B) = \max(\sup A, \sup B)$。

11. ★★☆ 设 $S \subseteq \mathbb{R}$ 非空有上界，$c > 0$。定义 $cS = \{cs : s \in S\}$。证明：$\sup(cS) = c \cdot \sup S$。

12. ★★★ 设 $A, B \subseteq \mathbb{R}$ 非空，且 $A$ 有上界、$B$ 有下界。定义 $A - B = \{a - b : a \in A, b \in B\}$。证明：$\sup(A - B) = \sup A - \inf B$。
