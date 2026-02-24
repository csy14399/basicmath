# 第 1 章 数列 — 练习题

## §1 数列的概念

1. ★☆☆ 写出以下数列的通项公式：
   (a) $2, 4, 6, 8, 10, \ldots$
   (b) $1, 4, 9, 16, 25, \ldots$
   (c) $1, -1, 1, -1, 1, \ldots$
   (d) $\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \frac{4}{5}, \ldots$

2. ★☆☆ 等差数列中 $a_1 = 5$，$d = -3$。求 $a_{10}$ 和 $S_{10}$。

3. ★☆☆ 等差数列中 $a_5 = 20$，$a_{12} = 48$。求 $a_1$ 和 $d$。

4. ★☆☆ 等比数列中 $a_1 = 2$，$r = 3$。求 $a_6$ 和 $S_6$。

5. ★☆☆ 等比数列中 $a_2 = 6$，$a_5 = 162$。求 $a_1$ 和 $r$。

6. ★★☆ 证明：等差数列的前 $n$ 项和 $S_n$ 是 $n$ 的二次函数（当 $d \neq 0$ 时）或一次函数（当 $d = 0$ 时）。

7. ★★☆ 在等差数列 $\{a_n\}$ 中，$S_7 = 77$。求 $a_4$。

8. ★★☆ 等比数列 $\{a_n\}$ 满足 $a_1 + a_3 = 10$，$a_2 + a_4 = 20$。求公比 $r$ 和首项 $a_1$。

9. ★★☆ 用特征方程法求解：$a_{n+2} = 4a_{n+1} - 4a_n$，$a_1 = 1$，$a_2 = 4$。（注意特征方程有重根。）

10. ★★☆ 判断以下数列的单调性和有界性：
    (a) $a_n = \dfrac{n}{2n+1}$
    (b) $a_n = (-1)^n \cdot \dfrac{1}{n}$
    (c) $a_n = \dfrac{2^n}{n!}$（$n \geq 1$）

11. ★★★ 设 $a_1 = \sqrt{2}$，$a_{n+1} = \sqrt{2 + a_n}$。证明 $\{a_n\}$ 单调递增且有上界 $2$。

12. ★★★ 用特征方程法求 Fibonacci 数列的通项公式（Binet 公式），并验证 $F_1 = 1$，$F_2 = 1$。

---

## §2 数列的极限

1. ★☆☆ 用 $\epsilon$-$N$ 定义证明 $\displaystyle\lim_{n \to \infty} \frac{1}{n^2} = 0$。

2. ★☆☆ 用极限的四则运算法则求以下极限：
   (a) $\displaystyle\lim_{n \to \infty} \frac{2n+3}{5n-1}$
   (b) $\displaystyle\lim_{n \to \infty} \frac{n^2 - 1}{3n^2 + 2}$
   (c) $\displaystyle\lim_{n \to \infty} \frac{4n^3 + n}{2n^3 - 3n^2 + 1}$

3. ★☆☆ 用夹逼定理证明 $\displaystyle\lim_{n \to \infty} \frac{\cos n}{n} = 0$。

4. ★★☆ 用 $\epsilon$-$N$ 定义证明 $\displaystyle\lim_{n \to \infty} \frac{2n-1}{3n+2} = \frac{2}{3}$。

5. ★★☆ 证明：如果 $\lim a_n = L$ 且 $a_n > 0$ 对所有 $n$，则 $L \geq 0$。

6. ★★☆ 设 $\lim a_n = L > 0$。证明存在 $N$ 使得 $n > N$ 时 $a_n > L/2$。

7. ★★☆ 求极限 $\displaystyle\lim_{n \to \infty} \left(\sqrt{n+1} - \sqrt{n}\right)$。（提示：有理化。）

8. ★★☆ 用夹逼定理求 $\displaystyle\lim_{n \to \infty} \frac{1}{n}\left(\frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}} + \cdots + \frac{1}{\sqrt{n}}\right)$。

9. ★★★ 用 $\epsilon$-$N$ 定义证明极限的乘法法则：若 $\lim a_n = L$，则 $\lim (c \cdot a_n) = cL$（$c$ 为常数）。

10. ★★★ 证明：$\displaystyle\lim_{n \to \infty} \frac{a^n}{n!} = 0$（对任意常数 $a > 0$）。

11. ★★★ 设 $a_1 = 1$，$a_{n+1} = \dfrac{a_n + 2}{a_n + 1}$。证明 $\{a_n\}$ 收敛并求其极限。（提示：先证有界和单调，再设极限为 $L$ 求解。）

12. ★★★ 证明 Stolz-Cesàro 定理的一个特殊情况：若 $\{b_n\}$ 严格递增趋于 $+\infty$，且 $\displaystyle\lim_{n \to \infty} \frac{a_n - a_{n-1}}{b_n - b_{n-1}} = L$，则 $\displaystyle\lim_{n \to \infty} \frac{a_n}{b_n} = L$。
