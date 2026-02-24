# 第 1 章 数列 — 练习题解答

## §1 数列的概念

**1.**
(a) $a_n = 2n$
(b) $a_n = n^2$
(c) $a_n = (-1)^{n+1}$（或 $a_n = (-1)^{n-1}$）
(d) $a_n = \dfrac{n}{n+1}$

---

**2.** $a_{10} = 5 + 9(-3) = 5 - 27 = -22$。

$S_{10} = \dfrac{10(a_1 + a_{10})}{2} = \dfrac{10(5 + (-22))}{2} = \dfrac{10 \times (-17)}{2} = -85$。

---

**3.** 由 $a_5 = a_1 + 4d = 20$ 和 $a_{12} = a_1 + 11d = 48$。

两式相减：$7d = 28$，$d = 4$。代回：$a_1 = 20 - 16 = 4$。

---

**4.** $a_6 = 2 \cdot 3^5 = 2 \cdot 243 = 486$。

$S_6 = \dfrac{2(1 - 3^6)}{1 - 3} = \dfrac{2(1 - 729)}{-2} = \dfrac{-1456}{-2} = 728$。

---

**5.** $a_2 = a_1 r = 6$，$a_5 = a_1 r^4 = 162$。

$\dfrac{a_5}{a_2} = r^3 = \dfrac{162}{6} = 27$，$r = 3$。代回：$a_1 = 6/3 = 2$。

---

**6.** $S_n = \dfrac{n[2a_1 + (n-1)d]}{2} = \dfrac{d}{2}n^2 + \left(a_1 - \dfrac{d}{2}\right)n$。

当 $d \neq 0$ 时，这是 $n$ 的二次函数（首项系数 $d/2 \neq 0$，无常数项）。当 $d = 0$ 时，$S_n = na_1$，为一次函数。

---

**7.** $S_7 = \dfrac{7(a_1 + a_7)}{2} = \dfrac{7 \cdot 2a_4}{2} = 7a_4$（利用 $a_1 + a_7 = 2a_4$）。

故 $a_4 = 77/7 = 11$。

---

**8.** $a_1 + a_1 r^2 = 10$，$a_1 r + a_1 r^3 = 20$。

第二式 $= r \cdot$ 第一式：$r(a_1 + a_1 r^2) = 20$，即 $10r = 20$，$r = 2$。

代回：$a_1(1 + 4) = 10$，$a_1 = 2$。

---

**9.** 特征方程：$\lambda^2 - 4\lambda + 4 = 0$，即 $(\lambda - 2)^2 = 0$。重根 $\lambda = 2$。

通解：$a_n = (A + Bn) \cdot 2^n$。

$a_1 = (A + B) \cdot 2 = 1$，$a_2 = (A + 2B) \cdot 4 = 4$。

由第二式：$A + 2B = 1$。由第一式：$A + B = 1/2$。

相减：$B = 1/2$，$A = 0$。

$$a_n = \frac{n}{2} \cdot 2^n = n \cdot 2^{n-1}$$

验证：$a_1 = 1 \cdot 1 = 1$ ✓，$a_2 = 2 \cdot 2 = 4$ ✓，$a_3 = 4 \cdot 4 - 4 \cdot 1 = 12 = 3 \cdot 4$ ✓。

---

**10.**
(a) $a_n = \dfrac{n}{2n+1}$。$a_{n+1} - a_n = \dfrac{n+1}{2n+3} - \dfrac{n}{2n+1} = \dfrac{(n+1)(2n+1) - n(2n+3)}{(2n+3)(2n+1)} = \dfrac{1}{(2n+3)(2n+1)} > 0$。严格递增。$0 < a_n < 1/2$，有界。

(b) $a_n = (-1)^n/n$。不单调（交替正负）。$|a_n| = 1/n \leq 1$，有界。

(c) $\dfrac{a_{n+1}}{a_n} = \dfrac{2}{n+1}$。当 $n \geq 2$ 时 $a_{n+1}/a_n < 1$，从第 2 项起严格递减。$a_n > 0$，有下界。有上界（$a_1 = 2$, $a_2 = 2$，此后递减）。有界。

---

**11.** 先证 $a_n < 2$（数学归纳法）：$a_1 = \sqrt{2} < 2$。若 $a_k < 2$，则 $a_{k+1} = \sqrt{2 + a_k} < \sqrt{2 + 2} = 2$。

再证单调递增：$a_{n+1}^2 - a_n^2 = (2 + a_n) - a_n^2 = -(a_n^2 - a_n - 2) = -(a_n - 2)(a_n + 1)$。因为 $a_n < 2$ 且 $a_n > 0$，$(a_n - 2) < 0$，$(a_n + 1) > 0$，故 $a_{n+1}^2 - a_n^2 > 0$。由于 $a_n > 0$，$a_{n+1} > a_n$。单调递增。

---

**12.** Fibonacci 递推 $F_{n+2} = F_{n+1} + F_n$ 的特征方程：$\lambda^2 - \lambda - 1 = 0$，根 $\lambda_{1,2} = \dfrac{1 \pm \sqrt{5}}{2}$。

通解 $F_n = A\lambda_1^n + B\lambda_2^n$。由 $F_1 = 1$：$A\lambda_1 + B\lambda_2 = 1$。由 $F_2 = 1$：$A\lambda_1^2 + B\lambda_2^2 = 1$。

利用 $\lambda_i^2 = \lambda_i + 1$：$A(\lambda_1 + 1) + B(\lambda_2 + 1) = 1$，即 $A\lambda_1 + B\lambda_2 + A + B = 1$，得 $A + B = 0$，$B = -A$。

代回第一式：$A(\lambda_1 - \lambda_2) = 1$，$A \cdot \sqrt{5} = 1$，$A = 1/\sqrt{5}$，$B = -1/\sqrt{5}$。

$$F_n = \frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n\right]$$

验证：$F_1 = \frac{1}{\sqrt{5}} \cdot \frac{(1+\sqrt{5}) - (1-\sqrt{5})}{2} = \frac{1}{\sqrt{5}} \cdot \frac{2\sqrt{5}}{2} = 1$ ✓。$F_2$ 类似可验证。

---

## §2 数列的极限

**1.** 设 $\epsilon > 0$。$\left|\dfrac{1}{n^2}\right| = \dfrac{1}{n^2} \leq \dfrac{1}{n}$。取 $N = \lceil 1/\epsilon \rceil$。对 $n > N$：$\dfrac{1}{n^2} \leq \dfrac{1}{n} < \dfrac{1}{N} \leq \epsilon$。故 $\lim 1/n^2 = 0$。$\blacksquare$

---

**2.**
(a) $\dfrac{2n+3}{5n-1} = \dfrac{2 + 3/n}{5 - 1/n} \to \dfrac{2}{5}$。

(b) $\dfrac{n^2 - 1}{3n^2 + 2} = \dfrac{1 - 1/n^2}{3 + 2/n^2} \to \dfrac{1}{3}$。

(c) $\dfrac{4n^3 + n}{2n^3 - 3n^2 + 1} = \dfrac{4 + 1/n^2}{2 - 3/n + 1/n^3} \to \dfrac{4}{2} = 2$。

---

**3.** $-\dfrac{1}{n} \leq \dfrac{\cos n}{n} \leq \dfrac{1}{n}$（因为 $|\cos n| \leq 1$）。$\lim(-1/n) = 0$，$\lim(1/n) = 0$。由夹逼定理，$\lim \dfrac{\cos n}{n} = 0$。

---

**4.** 设 $\epsilon > 0$。

$$\left|\frac{2n-1}{3n+2} - \frac{2}{3}\right| = \left|\frac{3(2n-1) - 2(3n+2)}{3(3n+2)}\right| = \frac{|-3-4|}{3(3n+2)} = \frac{7}{3(3n+2)} < \frac{7}{9n}$$

取 $N = \lceil 7/(9\epsilon) \rceil$。对 $n > N$：$\dfrac{7}{9n} < \dfrac{7}{9N} \leq \epsilon$。$\blacksquare$

---

**5.** 反证法。假设 $L < 0$。取 $\epsilon = -L/2 > 0$。存在 $N$ 使得 $n > N$ 时 $|a_n - L| < -L/2$，即 $L + L/2 < a_n < L - L/2$，即 $3L/2 < a_n < L/2 < 0$。这与 $a_n > 0$ 矛盾。故 $L \geq 0$。$\blacksquare$

---

**6.** 取 $\epsilon = L/2 > 0$。存在 $N$ 使得 $n > N$ 时 $|a_n - L| < L/2$。这意味着 $a_n > L - L/2 = L/2$。$\blacksquare$

---

**7.** 有理化：

$$\sqrt{n+1} - \sqrt{n} = \frac{(n+1) - n}{\sqrt{n+1} + \sqrt{n}} = \frac{1}{\sqrt{n+1} + \sqrt{n}}$$

分母 $\sqrt{n+1} + \sqrt{n} \geq 2\sqrt{n} \to \infty$，故 $\dfrac{1}{\sqrt{n+1} + \sqrt{n}} \to 0$。

更严格地：$0 < \dfrac{1}{\sqrt{n+1} + \sqrt{n}} < \dfrac{1}{2\sqrt{n}}$，而 $\lim \dfrac{1}{2\sqrt{n}} = 0$，由夹逼定理得极限为 $0$。

---

**8.** 注意 $\dfrac{1}{\sqrt{n}} \leq \dfrac{1}{\sqrt{k}} \leq \dfrac{1}{\sqrt{1}} = 1$（当 $1 \leq k \leq n$），因此：

$$\frac{1}{n} \cdot n \cdot \frac{1}{\sqrt{n}} \leq \frac{1}{n}\sum_{k=1}^{n}\frac{1}{\sqrt{k}} \leq \frac{1}{n} \cdot n \cdot 1$$

即 $\dfrac{1}{\sqrt{n}} \leq S \leq 1$。由 $\lim 1/\sqrt{n} = 0$，此估计不够精细。

更好的方法：$\dfrac{1}{\sqrt{k}} \leq 2(\sqrt{k} - \sqrt{k-1})$（因为 $\sqrt{k} - \sqrt{k-1} = \dfrac{1}{\sqrt{k}+\sqrt{k-1}} \geq \dfrac{1}{2\sqrt{k}}$）。

故 $\displaystyle\sum_{k=1}^{n} \frac{1}{\sqrt{k}} \leq 2\sqrt{n}$（裂项求和），$S_n \leq \dfrac{2\sqrt{n}}{n} = \dfrac{2}{\sqrt{n}} \to 0$。

又 $S_n \geq \dfrac{1}{n} \cdot \dfrac{n}{\sqrt{n}} = \dfrac{1}{\sqrt{n}} \to 0$。

等等——这说明 $S_n \to 0$？重新检查：$S_n = \dfrac{1}{n}\sum_{k=1}^{n}\dfrac{1}{\sqrt{k}}$。实际上 $\sum_{k=1}^{n}\dfrac{1}{\sqrt{k}} \geq 2\sqrt{n} - 2$（由 $\dfrac{1}{\sqrt{k}} \geq 2(\sqrt{k+1}-\sqrt{k})$ 不成立）。

用积分估计：$\displaystyle\sum_{k=1}^{n}\frac{1}{\sqrt{k}} \geq \int_1^{n+1}\frac{dx}{\sqrt{x}} = 2\sqrt{n+1} - 2$，$\displaystyle\sum_{k=1}^{n}\frac{1}{\sqrt{k}} \leq 1 + \int_1^{n}\frac{dx}{\sqrt{x}} = 1 + 2\sqrt{n} - 2 = 2\sqrt{n} - 1$。

因此 $\dfrac{2\sqrt{n+1}-2}{n} \leq S_n \leq \dfrac{2\sqrt{n}-1}{n}$。

$\dfrac{2\sqrt{n+1}-2}{n} = \dfrac{2}{\sqrt{n}} \cdot \dfrac{\sqrt{n+1}}{\sqrt{n}} \cdot \dfrac{1}{1} - \dfrac{2}{n} \sim \dfrac{2}{\sqrt{n}} \to 0$。

同样 $\dfrac{2\sqrt{n}-1}{n} = \dfrac{2}{\sqrt{n}} - \dfrac{1}{n} \to 0$。

由夹逼定理，$\lim S_n = 0$。

---

**9.** 设 $\epsilon > 0$。

情况 1：$c = 0$。$|ca_n - cL| = 0 < \epsilon$ 对所有 $n$ 成立。取 $N = 1$。

情况 2：$c \neq 0$。由 $a_n \to L$，存在 $N$ 使得 $n > N$ 时 $|a_n - L| < \dfrac{\epsilon}{|c|}$。

则 $|ca_n - cL| = |c| \cdot |a_n - L| < |c| \cdot \dfrac{\epsilon}{|c|} = \epsilon$。$\blacksquare$

---

**10.** 取 $N_0 \geq a$（使得 $k > N_0$ 时 $a/k < 1$）。对 $n > 2N_0$：

$$0 < \frac{a^n}{n!} = \frac{a^{N_0}}{N_0!} \cdot \prod_{k=N_0+1}^{n}\frac{a}{k} \leq \frac{a^{N_0}}{N_0!} \cdot \left(\frac{a}{N_0+1}\right)^{n-N_0}$$

令 $C = \dfrac{a^{N_0}}{N_0!}$（常数），$r = \dfrac{a}{N_0+1} < 1$。则 $0 < \dfrac{a^n}{n!} \leq C \cdot r^{n-N_0} \to 0$。由夹逼定理，$\dfrac{a^n}{n!} \to 0$。$\blacksquare$

---

**11.** 先证 $a_n > 0$（归纳法显然）。

**有界性**：证明 $1 \leq a_n \leq 2$。$a_1 = 1$。若 $a_k \leq 2$，$a_{k+1} = \dfrac{a_k + 2}{a_k + 1} \leq \dfrac{4}{2} = 2$。若 $a_k \geq 1$，$a_{k+1} = \dfrac{a_k + 2}{a_k + 1} = 1 + \dfrac{1}{a_k + 1} \geq 1$。

**单调性**：$a_{n+1} - a_n = \dfrac{a_n + 2}{a_n + 1} - a_n = \dfrac{a_n + 2 - a_n^2 - a_n}{a_n + 1} = \dfrac{2 - a_n^2}{a_n + 1} = \dfrac{(\sqrt{2} - a_n)(\sqrt{2} + a_n)}{a_n + 1}$。

当 $a_n < \sqrt{2}$ 时 $a_{n+1} > a_n$，当 $a_n > \sqrt{2}$ 时 $a_{n+1} < a_n$。$a_1 = 1 < \sqrt{2}$，$a_2 = 3/2 > \sqrt{2}$，$a_3 = 7/5 < \sqrt{2}$，……数列交替在 $\sqrt{2}$ 两侧。

改用：考虑奇偶子列。或者更简洁地，证明 $|a_{n+1} - \sqrt{2}| < |a_n - \sqrt{2}|$：

$$|a_{n+1} - \sqrt{2}| = \left|\frac{a_n + 2}{a_n + 1} - \sqrt{2}\right| = \frac{|a_n - \sqrt{2} \cdot a_n + 2 - \sqrt{2}|}{a_n + 1} = \frac{|a_n(1-\sqrt{2}) + (2-\sqrt{2})|}{a_n+1}$$

$$= \frac{|(1-\sqrt{2})(a_n - \sqrt{2})|}{a_n + 1} = \frac{(\sqrt{2}-1)|a_n - \sqrt{2}|}{a_n + 1} \leq \frac{(\sqrt{2}-1)}{1+1}|a_n-\sqrt{2}| < \frac{1}{2}|a_n-\sqrt{2}|$$

因此 $|a_n - \sqrt{2}| < (1/2)^{n-1}|a_1 - \sqrt{2}| \to 0$，即 $a_n \to \sqrt{2}$。

或用单调有界法：设极限 $L$ 存在，由 $a_{n+1} = \dfrac{a_n + 2}{a_n + 1}$ 取极限：$L = \dfrac{L+2}{L+1}$，$L^2 + L = L + 2$，$L^2 = 2$，$L = \sqrt{2}$（取正值）。

---

**12.** 见 §1 第 12 题。完整推导见正文 §1 关于 Binet 公式的部分。
