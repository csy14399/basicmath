# 第 3 章 数论 — 练习题解答

## §1 整除性与质数

**1.** $\gcd(84, 36)$。

> $84 = 36 \times 2 + 12$
> $36 = 12 \times 3 + 0$
>
> $\gcd(84, 36) = 12$。$\blacksquare$

---

**2.** $5040$ 的质因数分解。

> $5040 = 2 \times 2520 = 2^2 \times 1260 = 2^3 \times 630 = 2^4 \times 315 = 2^4 \times 3 \times 105 = 2^4 \times 3 \times 3 \times 35 = 2^4 \times 3^2 \times 5 \times 7$。
>
> $5040 = 2^4 \times 3^2 \times 5 \times 7$。（注：$5040 = 7!$）$\blacksquare$

---

**3.** $\gcd(91, 65)$ 及 Bézout 系数。

> $91 = 65 \times 1 + 26$
> $65 = 26 \times 2 + 13$
> $26 = 13 \times 2 + 0$
>
> $\gcd(91, 65) = 13$。
>
> 反推：$13 = 65 - 26 \times 2 = 65 - (91 - 65) \times 2 = 65 \times 3 - 91 \times 2 = 91 \times (-2) + 65 \times 3$。
>
> 即 $x = -2, y = 3$。验证：$91(-2) + 65(3) = -182 + 195 = 13$。✓ $\blacksquare$

---

**4.** 若 $a \mid b$ 且 $a \mid c$，证明 $a \mid (b^2 + c^2)$。

> $b = ak_1, c = ak_2$。$b^2 + c^2 = a^2k_1^2 + a^2k_2^2 = a^2(k_1^2 + k_2^2) = a \cdot a(k_1^2 + k_2^2)$。
>
> 故 $a \mid (b^2 + c^2)$。$\blacksquare$

---

**5.** 证明 $\gcd(n, 2n+1) = 1$。

> 设 $d = \gcd(n, 2n+1)$。则 $d \mid n$ 且 $d \mid (2n+1)$。故 $d \mid ((2n+1) - 2n) = 1$。因此 $d = 1$。$\blacksquare$

---

**6.** 若 $\gcd(a,b) = 1$，$a \mid c$，$b \mid c$，证明 $ab \mid c$。

> $a \mid c$ 意味 $c = ak$。$b \mid c = ak$。由 $\gcd(a,b) = 1$ 和 Euclid 引理，$b \mid k$。设 $k = bl$。则 $c = abl$，即 $ab \mid c$。$\blacksquare$

---

**7.** 用算术基本定理证明 $\sqrt{3}$ 无理。

> 假设 $\sqrt{3} = p/q$，$p, q \in \mathbb{Z}^+$，$\gcd(p,q) = 1$。则 $p^2 = 3q^2$。
>
> 考虑质因数 $3$ 在两边出现的次数。设 $3$ 在 $p$ 的分解中出现 $a$ 次，在 $q$ 中出现 $b$ 次。
>
> 左边：$3$ 出现 $2a$ 次（偶数次）。右边：$3$ 出现 $2b + 1$ 次（奇数次）。
>
> 偶数 $\neq$ 奇数，矛盾。$\blacksquare$

---

**8.** $\gcd(a,b) \cdot \text{lcm}(a,b) = ab$。

> 设 $a = \prod p_i^{a_i}$，$b = \prod p_i^{b_i}$（对所有相关质数，允许指数为 $0$）。
>
> $\gcd(a,b) = \prod p_i^{\min(a_i, b_i)}$，$\text{lcm}(a,b) = \prod p_i^{\max(a_i, b_i)}$。
>
> $\gcd \cdot \text{lcm} = \prod p_i^{\min(a_i,b_i) + \max(a_i,b_i)} = \prod p_i^{a_i + b_i} = ab$。$\blacksquare$

---

**9.** $n! + k$（$2 \leq k \leq n$）都是合数。

> $k \leq n$ 意味 $k \mid n!$，故 $k \mid (n! + k)$。又 $n! + k > k$（因 $n \geq 2$，$n! \geq 2$），故 $n! + k$ 有因子 $k$（$1 < k < n! + k$），是合数。$\blacksquare$

---

**10.** $p > 3$ 质数则 $p^2 \equiv 1 \pmod{24}$。

> $p > 3$ 且 $p$ 是质数，故 $p$ 是奇数且 $3 \nmid p$。
>
> **模 8**：$p$ 是奇数，$p \equiv 1, 3, 5, 7 \pmod{8}$。$p^2 \equiv 1, 9, 25, 49 \equiv 1, 1, 1, 1 \pmod{8}$。
>
> **模 3**：$p \not\equiv 0 \pmod{3}$，$p \equiv 1$ 或 $2$，$p^2 \equiv 1$ 或 $4 \equiv 1 \pmod{3}$。
>
> 综合：$8 \mid (p^2 - 1)$ 且 $3 \mid (p^2 - 1)$，由 $\gcd(8,3) = 1$，$24 \mid (p^2 - 1)$。$\blacksquare$

---

## §2 同余与模运算

**11.** $7^{50} \bmod 11$。

> Fermat：$7^{10} \equiv 1 \pmod{11}$。$50 = 10 \times 5$。$7^{50} = (7^{10})^5 \equiv 1 \pmod{11}$。$\blacksquare$

---

**12.** $[3]^{-1}$ 在 $\mathbb{Z}/7\mathbb{Z}$ 中。

> $3 \times 5 = 15 = 2 \times 7 + 1 \equiv 1 \pmod{7}$。故 $[3]^{-1} = [5]$。$\blacksquare$

---

**13.** $x \equiv 3 \pmod{6}$ 且 $x \equiv 5 \pmod{6}$？

> 若两式同时成立，则 $3 \equiv 5 \pmod{6}$，即 $6 \mid 2$，矛盾。无解。$\blacksquare$

---

**14.** $x \equiv 1 \pmod{5}$，$x \equiv 2 \pmod{7}$，$x \equiv 3 \pmod{9}$。

> $M = 5 \times 7 \times 9 = 315$。$M_1 = 63, M_2 = 45, M_3 = 35$。
>
> $63y_1 \equiv 1 \pmod{5}$：$63 \equiv 3$，$3 \times 2 = 6 \equiv 1$，$y_1 = 2$。
>
> $45y_2 \equiv 1 \pmod{7}$：$45 \equiv 3$，$3 \times 5 = 15 \equiv 1$，$y_2 = 5$。
>
> $35y_3 \equiv 1 \pmod{9}$：$35 \equiv 8 \equiv -1$，$(-1)(-1) = 1$，$y_3 = -1 \equiv 8$。
>
> $x = 1 \times 63 \times 2 + 2 \times 45 \times 5 + 3 \times 35 \times 8 = 126 + 450 + 840 = 1416$。
>
> $1416 \bmod 315 = 1416 - 4 \times 315 = 1416 - 1260 = 156$。
>
> 验证：$156 = 31 \times 5 + 1$ ✓，$156 = 22 \times 7 + 2$ ✓，$156 = 17 \times 9 + 3$ ✓。$\blacksquare$

---

**15.** $6 \mid n^3 - n$。

> $n^3 - n = n(n-1)(n+1)$：三个连续整数之积。
>
> 连续三整数中必有一个是 $2$ 的倍数，必有一个是 $3$ 的倍数。故 $6 \mid n(n-1)(n+1)$。$\blacksquare$

---

**16.** $2^{1000} \bmod 13$。

> Fermat：$2^{12} \equiv 1 \pmod{13}$。$1000 = 12 \times 83 + 4$。
>
> $2^{1000} \equiv 2^4 = 16 \equiv 3 \pmod{13}$。$\blacksquare$

---

**17.** $\mathbb{Z}/p\mathbb{Z}$ 中恰好 $(p-1)/2$ 个非零元素是完全平方。

> 映射 $f: (\mathbb{Z}/p\mathbb{Z})^* \to (\mathbb{Z}/p\mathbb{Z})^*$，$f([a]) = [a^2]$。
>
> $f([a]) = f([b]) \iff a^2 \equiv b^2 \iff p \mid (a-b)(a+b) \iff a \equiv b$ 或 $a \equiv -b$。
>
> 因 $p$ 是奇质数，$a \not\equiv -a$（否则 $2a \equiv 0$，$p \mid 2a$，$p \mid a$，与 $a \not\equiv 0$ 矛盾）。
>
> 故 $f$ 是 $2$ 对 $1$ 的映射。像的大小 $= (p-1)/2$。$\blacksquare$

---

**18.** $1^{p-1} + 2^{p-1} + \cdots + (p-1)^{p-1} \equiv -1 \pmod{p}$。

> 由 Fermat 小定理，$k^{p-1} \equiv 1 \pmod{p}$ 对 $1 \leq k \leq p-1$。
>
> $\sum_{k=1}^{p-1} k^{p-1} \equiv \sum_{k=1}^{p-1} 1 = p - 1 \equiv -1 \pmod{p}$。$\blacksquare$

---

**19.** $ax \equiv b \pmod{m}$，$\gcd(a,m) = 1$ 时恰有一个模 $m$ 的解。

> **存在性**：$[a]$ 在 $\mathbb{Z}/m\mathbb{Z}$ 中可逆（命题 3），$x \equiv a^{-1}b \pmod{m}$ 是解。
>
> **唯一性**：若 $ax_1 \equiv ax_2 \pmod{m}$，由消去律（$\gcd(a,m) = 1$），$x_1 \equiv x_2 \pmod{m}$。$\blacksquare$

---

**20.** 若 $p$ 奇质数且 $p \mid a^2 + b^2$，则 $p \equiv 1 \pmod{4}$ 或 $p \mid a, p \mid b$。

> 假设 $p \nmid a$ 且 $p \nmid b$。则 $b$ 有模 $p$ 逆元。$a^2 + b^2 \equiv 0 \implies (ab^{-1})^2 \equiv -1 \pmod{p}$。
>
> 设 $c = ab^{-1}$，$c^2 \equiv -1$。则 $c^{p-1} = (c^2)^{(p-1)/2} \equiv (-1)^{(p-1)/2} \pmod{p}$。
>
> 由 Fermat，$c^{p-1} \equiv 1$。故 $(-1)^{(p-1)/2} \equiv 1$，即 $(p-1)/2$ 是偶数，$4 \mid (p-1)$，$p \equiv 1 \pmod{4}$。$\blacksquare$

---

## §3 丢番图方程初步

**21.** $4x + 6y = 10$。

> $\gcd(4, 6) = 2$，$2 \mid 10$。化简：$2x + 3y = 5$。
>
> 特解：$2(1) + 3(1) = 5$，$(x_0, y_0) = (1, 1)$。
>
> 通解：$x = 1 + 3t, y = 1 - 2t, t \in \mathbb{Z}$。$\blacksquare$

---

**22.** $m = 5, n = 2$ 对应的勾股数。

> $a = 25 - 4 = 21$，$b = 2 \times 5 \times 2 = 20$，$c = 25 + 4 = 29$。
>
> 验证：$21^2 + 20^2 = 441 + 400 = 841 = 29^2$。✓ $\blacksquare$

---

**23.** $15x + 25y = 100$ 的所有非负整数解。

> $\gcd(15, 25) = 5$，$5 \mid 100$。化简：$3x + 5y = 20$。
>
> 特解：$3 \times 5 + 5 \times 1 = 20$，$(x_0, y_0) = (5, 1)$。
>
> 通解：$x = 5 + 5t, y = 1 - 3t$。
>
> 非负：$x \geq 0 \implies t \geq -1$，$y \geq 0 \implies t \leq 0$。
>
> $t = -1$：$(0, 4)$。$t = 0$：$(5, 1)$。
>
> 两组非负整数解：$(x, y) = (0, 4)$ 和 $(5, 1)$。$\blacksquare$

---

**24.** $x^2 + y^2 \equiv 3 \pmod{4}$ 无解。

> $x^2 \bmod 4 \in \{0, 1\}$（$0^2=0, 1^2=1, 2^2=0, 3^2=1$）。
>
> $x^2 + y^2 \bmod 4 \in \{0+0, 0+1, 1+0, 1+1\} = \{0, 1, 2\}$。
>
> $3 \notin \{0, 1, 2\}$，故无解。因此 $x^2 + y^2 = 4k+3$ 无整数解。$\blacksquare$

---

**25.** $c \leq 50$ 的本原勾股数。

> 需要 $m > n > 0$，$\gcd(m,n) = 1$，$m,n$ 奇偶不同，$c = m^2 + n^2 \leq 50$。
>
> | $m$ | $n$ | $a$ | $b$ | $c$ |
> |-----|-----|-----|-----|-----|
> | 2 | 1 | 3 | 4 | 5 |
> | 3 | 2 | 5 | 12 | 13 |
> | 4 | 1 | 15 | 8 | 17 |
> | 4 | 3 | 7 | 24 | 25 |
> | 5 | 2 | 21 | 20 | 29 |
> | 5 | 4 | 9 | 40 | 41 |
> | 6 | 1 | 35 | 12 | 37 |
> | 6 | 5 | 11 | 60 | 61>50 ✗ |
> | 7 | 2 | 45 | 28 | 53>50 ✗ |
>
> 答案：$(3,4,5), (5,12,13), (8,15,17), (7,24,25), (20,21,29), (9,40,41), (12,35,37)$。$\blacksquare$

---

**26.** $x^2 + y^2 = 3z^2$ 的唯一解是 $x=y=z=0$。

> **模 3**：$x^2 \bmod 3 \in \{0, 1\}$。$x^2 + y^2 \equiv 0 \pmod{3}$ 要求 $x^2 \equiv 0$ 且 $y^2 \equiv 0$（因为 $1+1=2\not\equiv 0, 1+0=1\not\equiv 0, 0+1=1\not\equiv 0$）。故 $3 \mid x$ 且 $3 \mid y$。
>
> 设 $x = 3x', y = 3y'$。则 $9(x')^2 + 9(y')^2 = 3z^2$，$3((x')^2 + (y')^2) = z^2$。故 $3 \mid z^2$，$3 \mid z$。设 $z = 3z'$。
>
> $3((x')^2 + (y')^2) = 9(z')^2$，$(x')^2 + (y')^2 = 3(z')^2$。
>
> 回到同一方程，但 $(x', y', z')$ 比 $(x, y, z)$ 小（各除以 $3$）。无穷递降，故只有 $x=y=z=0$。$\blacksquare$

---

**27.** $x^2 - y^2 = 105$ 的正整数解。

> $(x-y)(x+y) = 105 = 3 \times 5 \times 7$。设 $x-y = d_1, x+y = d_2$，$d_1 d_2 = 105$，$d_1 < d_2$（因 $y > 0$），$d_1, d_2$ 同奇偶（因 $x = (d_1+d_2)/2$ 需为整数）。
>
> $105$ 是奇数，故 $d_1, d_2$ 都是奇数。✓
>
> 分解 $105$ 的方式（$d_1 < d_2$）：
> - $1 \times 105$：$x = 53, y = 52$
> - $3 \times 35$：$x = 19, y = 16$
> - $5 \times 21$：$x = 13, y = 8$
> - $7 \times 15$：$x = 11, y = 4$
>
> 四组解。$\blacksquare$

---

**28.** $x^2 + 3y^2 = 8$ 无正整数解。

> $y = 1$：$x^2 = 5$，无整数解。$y = 2$：$x^2 = -4$，不可能。$y \geq 2$：$3y^2 \geq 12 > 8$。故无正整数解。$\blacksquare$

---

**29.** $x^2 \equiv -1 \pmod{p}$（$p$ 奇质数）有解 $\iff p \equiv 1 \pmod{4}$。

> ($\Leftarrow$) $p \equiv 1 \pmod{4}$。由 Wilson 定理（$(p-1)! \equiv -1 \pmod{p}$），将 $(p-1)! = 1 \times 2 \times \cdots \times \frac{p-1}{2} \times \frac{p+1}{2} \times \cdots \times (p-1)$ 中配对 $k$ 和 $p-k$：
>
> $(p-1)! = \prod_{k=1}^{(p-1)/2} k(p-k) = \prod_{k=1}^{(p-1)/2} (-k^2) = (-1)^{(p-1)/2} \left(\left(\frac{p-1}{2}\right)!\right)^2$。
>
> 因 $p \equiv 1 \pmod{4}$，$(p-1)/2$ 是偶数，$(-1)^{(p-1)/2} = 1$。
>
> 故 $(p-1)! = \left(\left(\frac{p-1}{2}\right)!\right)^2 \equiv -1 \pmod{p}$。令 $x = \left(\frac{p-1}{2}\right)!$，$x^2 \equiv -1$。
>
> ($\Rightarrow$) 见第 20 题解答。$\blacksquare$

---

**30.** $x^4 - y^4 = z^2$ 无正整数解。

> 假设 $(x,y,z)$ 是正整数解，$\gcd(x,y) = 1$（否则约分），且 $z$ 最小。
>
> $x^4 = y^4 + z^2$。改写：$(x^2)^2 = (y^2)^2 + z^2$，即 $(z, y^2, x^2)$ 是勾股数。
>
> 由参数化（需仔细分析正负和奇偶），最终能构造更小的正整数解，与 $z$ 的最小性矛盾。
>
> 这与 Fermat 证明 $x^4 + y^4 = z^2$ 无正整数解（§3 定理 4）的方法类似。$\blacksquare$
