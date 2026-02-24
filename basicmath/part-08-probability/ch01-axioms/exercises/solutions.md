# 第 1 章 概率公理 — 练习题解答

## §1 概率的概念

**1.** $A = \{5, 6\}$，$P(A) = 2/6 = 1/3$。

---

**2.** $5$ 的倍数：$5, 10, 15, 20, 25, 30$，共 $6$ 个。$P = 6/30 = 1/5$。

---

**3.** 红球或蓝球共 $4 + 2 = 6$ 个，总球数 $9$。$P = 6/9 = 2/3$。

---

**4.** $\Omega = \{(i,j): 1 \leq i,j \leq 6\}$，$|\Omega| = 36$。

$i + j$ 为偶数 $\Leftrightarrow$ $i, j$ 同奇或同偶。奇数有 $3$ 个，偶数有 $3$ 个。

同奇：$3 \times 3 = 9$ 种；同偶：$3 \times 3 = 9$ 种。$|A| = 18$。

$P = 18/36 = 1/2$。

---

**5.** 红心 $13$ 张，人头牌 $12$ 张（$4$ 种花色各 $3$ 张），红心中的人头牌 $3$ 张。

$P = (13 + 12 - 3)/52 = 22/52 = 11/26$。

---

**6.** $4$ 的倍数：$\lfloor 100/4 \rfloor = 25$ 个，$P(A) = 25/100$。

$6$ 的倍数：$\lfloor 100/6 \rfloor = 16$ 个，$P(B) = 16/100$。

$A \cap B$ = $\text{lcm}(4,6) = 12$ 的倍数：$\lfloor 100/12 \rfloor = 8$ 个，$P(A \cap B) = 8/100$。

$P(A) + P(B) - P(A \cap B) = 25/100 + 16/100 - 8/100 = 33/100$。

$|A \cup B| = 25 + 16 - 8 = 33$，$P(A \cup B) = 33/100$。验证一致。✓

---

**7.** $\Omega = \{HHH, HHT, HTH, THH, HTT, THT, TTH, TTT\}$，$|\Omega| = 8$。

恰好两枚正面：$\{HHT, HTH, THH\}$，$3$ 个。$P = 3/8$。

---

**8.** $|\Omega| = \binom{10}{4} = 210$。

恰好 $1$ 个次品：从 $3$ 个次品中选 $1$，从 $7$ 个正品中选 $3$。

$|A| = \binom{3}{1}\binom{7}{3} = 3 \times 35 = 105$。

$P = 105/210 = 1/2$。

---

**9.** 需要 $\sum_{k=1}^{\infty} P(\{\omega_k\}) = 1$。

$$\sum_{k=1}^{\infty} c \cdot \left(\frac{2}{3}\right)^k = c \cdot \frac{2/3}{1 - 2/3} = c \cdot 2 = 1$$

所以 $c = 1/2$。

验证：$P(\{\omega_k\}) = \frac{1}{2} \cdot (2/3)^k > 0$ ✓，$\sum = 1$ ✓。

---

**10.** 由加法公式：$P(A \cup B) = P(A) + P(B) - P(A \cap B)$。

又 $P(A \cup B) \leq 1$，所以 $P(A \cap B) = P(A) + P(B) - P(A \cup B) \geq 0.6 + 0.7 - 1 = 0.3$。$\blacksquare$

---

## §2 概率的性质

**11.** $P(A^c) = 1 - 0.35 = 0.65$。

---

**12.** $P(A \cup B) = 0.4 + 0.5 - 0.2 = 0.7$。

---

**13.** $P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.5 + 0.6 - 0.8 = 0.3$。

$P(A^c \cap B) = P(B) - P(A \cap B) = 0.6 - 0.3 = 0.3$。

---

**14.** $A \subseteq B$ $\Rightarrow$ $P(B \setminus A) = P(B) - P(A) = 0.7 - 0.3 = 0.4$。

---

**15.** (a) $P(\text{篮球} \cup \text{足球}) = 25/40 + 20/40 - 10/40 = 35/40 = 7/8$。

(b) $P(\text{都不喜欢}) = 1 - 7/8 = 1/8$。

---

**16.** 互斥：$P(A \cup B) = 0.3 + 0.4 = 0.7$。

$P(A^c \cap B^c) = P((A \cup B)^c) = 1 - 0.7 = 0.3$。

---

**17.** $P(A \cup B) = P(A) + P(B) - P(A \cap B) \leq 1$。

移项得 $P(A \cap B) \geq P(A) + P(B) - 1$。$\blacksquare$

---

**18.** 由 Boole 不等式的对偶形式（Bonferroni 不等式的推广）：

$$P(A_1 \cap \cdots \cap A_n) = 1 - P(A_1^c \cup \cdots \cup A_n^c) \geq 1 - \sum_{i=1}^{n} P(A_i^c)$$

$P(A_i^c) = 1 - P(A_i) < 1/n$，所以 $\sum P(A_i^c) < n \cdot (1/n) = 1$。

因此 $P(A_1 \cap \cdots \cap A_n) > 1 - 1 = 0$。$\blacksquare$

---

**19.** 设 $A$ = "被 $2$ 整除"，$B$ = "被 $3$ 整除"，$C$ = "被 $5$ 整除"。从 $\{1, \ldots, 1000\}$ 中随机取一个数。

$P(A) = 500/1000$，$P(B) = 333/1000$，$P(C) = 200/1000$。

$P(A \cap B) = \lfloor 1000/6 \rfloor / 1000 = 166/1000$。

$P(A \cap C) = \lfloor 1000/10 \rfloor / 1000 = 100/1000$。

$P(B \cap C) = \lfloor 1000/15 \rfloor / 1000 = 66/1000$。

$P(A \cap B \cap C) = \lfloor 1000/30 \rfloor / 1000 = 33/1000$。

$P(A \cup B \cup C) = 500 + 333 + 200 - 166 - 100 - 66 + 33 = 734$。个数 $= 734$。

不能被 $2$、$3$ 或 $5$ 整除的个数 $= 1000 - 734 = 266$。

（验证：$1000 \times (1-1/2)(1-1/3)(1-1/5) = 1000 \times 4/15 \approx 266.67$，取 $\lfloor \cdot \rfloor$ 后因边界效应略有差异，精确值为 $266$。）

---

**20.** $A_1 \subseteq A_2 \subseteq \cdots$，$P(A_n) = 1 - 1/n \to 1$。

由概率的下连续性（定理 7）：

$$P\!\left(\bigcup_{n=1}^{\infty} A_n\right) = \lim_{n \to \infty} P(A_n) = \lim_{n \to \infty} \left(1 - \frac{1}{n}\right) = 1$$
