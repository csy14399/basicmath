# 第 3 章 数论 — 挑战题

以下题目超出常规练习的难度，适合深入探索。

---

**C1.** ★★★★ 证明 **Wilson 定理**：$p$ 是质数当且仅当 $(p-1)! \equiv -1 \pmod{p}$。

<details>
<summary>提示</summary>

($\Rightarrow$) 在 $\mathbb{Z}/p\mathbb{Z}$ 中，将 $(p-1)!$ 中的元素配对：$a$ 和 $a^{-1}$。哪些元素等于自己的逆？

($\Leftarrow$) 若 $p$ 不是质数，考虑 $(p-1)!$ 中的因子。
</details>

<details>
<summary>解答</summary>

**($\Rightarrow$)** 设 $p$ 是质数。在 $\mathbb{Z}/p\mathbb{Z}^*$ 中，每个元素 $a$ 都有逆元 $a^{-1}$。$a = a^{-1} \iff a^2 \equiv 1 \iff p \mid (a-1)(a+1) \iff a \equiv 1$ 或 $a \equiv -1$。

故在 $\{1, 2, \ldots, p-1\}$ 中，除了 $1$ 和 $p-1$ 之外，其余元素两两配对（$a$ 和 $a^{-1}$ 配对），每对乘积 $\equiv 1$。

$(p-1)! = 1 \times (配对乘积) \times (p-1) \equiv 1 \times 1 \times \cdots \times 1 \times (p-1) \equiv -1 \pmod{p}$。

**($\Leftarrow$)** 若 $p = ab$（$1 < a, b < p$），则 $a \mid (p-1)!$（因 $a < p$，$a$ 出现在 $1, 2, \ldots, p-1$ 中），故 $(p-1)! \equiv 0 \pmod{a}$。若 $(p-1)! \equiv -1 \pmod{p}$，则 $(p-1)! \equiv -1 \pmod{a}$（因 $a \mid p$），与 $(p-1)! \equiv 0 \pmod{a}$ 矛盾（$0 \not\equiv -1 \pmod{a}$，因 $a > 1$）。$\blacksquare$
</details>

---

**C2.** ★★★★ **RSA 加密的数学原理**。

设 $p, q$ 是不同的大质数，$n = pq$，$\phi(n) = (p-1)(q-1)$。选择 $e$ 满足 $\gcd(e, \phi(n)) = 1$，计算 $d$ 使得 $ed \equiv 1 \pmod{\phi(n)}$。

证明：对任意 $0 \leq m < n$，$(m^e)^d \equiv m \pmod{n}$。

（即加密后再用私钥解密，能还原原始消息。）

<details>
<summary>提示</summary>

$m^{ed} = m^{1 + k\phi(n)}$。对 $\gcd(m, n) = 1$ 的情况用 Euler 定理（Fermat 小定理的推广）。对 $\gcd(m, n) > 1$ 的情况（$p \mid m$ 或 $q \mid m$），分别模 $p$ 和模 $q$ 讨论，再用中国剩余定理合并。
</details>

<details>
<summary>解答</summary>

$ed = 1 + k\phi(n)$ 对某 $k \in \mathbb{Z}$。

**情况 1**：$\gcd(m, n) = 1$。

由 Euler 定理（Fermat 小定理的推广，此处取 $n = pq$），$m^{\phi(n)} \equiv 1 \pmod{n}$。

$m^{ed} = m^{1+k\phi(n)} = m \cdot (m^{\phi(n)})^k \equiv m \cdot 1 = m \pmod{n}$。

**情况 2**：$\gcd(m, n) > 1$。因 $0 \leq m < n$ 且 $n = pq$，不妨设 $p \mid m$（且 $q \nmid m$，否则 $n \mid m$，即 $m = 0$，结论显然）。

模 $p$：$m \equiv 0 \pmod{p}$，故 $m^{ed} \equiv 0 \equiv m \pmod{p}$。

模 $q$：$\gcd(m, q) = 1$。由 Fermat 小定理，$m^{q-1} \equiv 1 \pmod{q}$。

$m^{ed} = m^{1+k(p-1)(q-1)} = m \cdot (m^{q-1})^{k(p-1)} \equiv m \cdot 1 = m \pmod{q}$。

由中国剩余定理（$\gcd(p,q) = 1$），$m^{ed} \equiv m \pmod{pq} = \pmod{n}$。$\blacksquare$
</details>

---

**C3.** ★★★★ 证明：存在无穷多个形如 $4k + 3$ 的质数。

<details>
<summary>提示</summary>

模仿 Euclid 的证明，但构造 $N = 4p_1 p_2 \cdots p_n - 1$（或 $N = 4p_1 p_2 \cdots p_n + 3$）。利用"$4k+3$ 型质数的乘积不全能是 $4k+1$ 型"这一事实。
</details>

<details>
<summary>解答</summary>

假设 $4k+3$ 型质数只有有限多个：$p_1, p_2, \ldots, p_n$（不含 $2$；注意 $3$ 属于此类）。

令 $N = 4p_1 p_2 \cdots p_n - 1$。则 $N \equiv -1 \equiv 3 \pmod{4}$，即 $N$ 是 $4k+3$ 型。

$N$ 的每个质因子都不是 $p_i$（因 $N = 4p_1 \cdots p_n - 1$，$N \equiv -1 \pmod{p_i}$，故 $p_i \nmid N$）。

关键观察：两个 $4k+1$ 型整数的乘积仍是 $4k+1$ 型（$(4a+1)(4b+1) = 16ab + 4a + 4b + 1 = 4(4ab+a+b) + 1$）。

故若 $N$ 的所有质因子都是 $4k+1$ 型（或 $= 2$），则 $N$ 本身是 $2^s$ 乘以 $4k+1$ 型数的乘积。$2^s$ 的模 4 值为 $0, 2, 0, 2, \ldots$（$s \geq 2$ 时为 $0$），$4k+1$ 的乘积模 $4$ 为 $1$。故 $N$ 模 $4$ 为 $0$ 或 $2$ 或 $1$，不可能是 $3$。

矛盾。故 $N$ 至少有一个 $4k+3$ 型质因子，不在列表中。$\blacksquare$
</details>

---

**C4.** ★★★★★ 设 $p$ 是奇质数。证明 $x^2 \equiv 2 \pmod{p}$ 有解当且仅当 $p \equiv \pm 1 \pmod{8}$。

<details>
<summary>提示</summary>

这是二次互反律的特殊情况。可以用 Euler 判据：$2^{(p-1)/2} \equiv \left(\frac{2}{p}\right) \pmod{p}$，然后计算 $2^{(p-1)/2} \bmod p$ 对 $p \bmod 8$ 的依赖。
</details>

<details>
<summary>解答</summary>

由 Euler 判据，$x^2 \equiv 2 \pmod{p}$ 有解当且仅当 $2^{(p-1)/2} \equiv 1 \pmod{p}$。

需要证明：$2^{(p-1)/2} \equiv 1 \pmod{p} \iff p \equiv \pm 1 \pmod{8}$。

一种方法：用 Gauss 引理。设 $S = \{1 \cdot 2, 2 \cdot 2, \ldots, \frac{p-1}{2} \cdot 2\} = \{2, 4, 6, \ldots, p-1\}$。

对每个 $2k$（$1 \leq k \leq (p-1)/2$），取其"最小正剩余"或"负半"代表：若 $2k \leq (p-1)/2$，正号；若 $2k > (p-1)/2$，用 $p - 2k$ 代替（负号）。

设负号出现 $\mu$ 次。由 Gauss 引理，$\left(\frac{2}{p}\right) = (-1)^\mu$。

$\mu$ 等于 $\{2, 4, \ldots, p-1\}$ 中大于 $(p-1)/2$ 的元素个数，即满足 $(p-1)/2 < 2k \leq p-1$ 的 $k$ 的个数，即 $(p-1)/4 < k \leq (p-1)/2$。

通过对 $p \bmod 8$ 的逐案分析，可验证 $\mu$ 为偶当且仅当 $p \equiv \pm 1 \pmod{8}$。$\blacksquare$
</details>
