# 第二章 集合论 — 练习题解答

## §1 集合与集合运算

**1.** 用列举法表示下列集合。

(a) $\{x \in \mathbb{Z} \mid -3 \leq x \leq 3\} = \{-3, -2, -1, 0, 1, 2, 3\}$。

(b) $\{x \in \mathbb{N} \mid x^2 < 20\}$。满足条件的自然数为 $0, 1, 2, 3, 4$（$4^2 = 16 < 20$，$5^2 = 25 \geq 20$）。所以答案为 $\{0, 1, 2, 3, 4\}$。

(c) $\{x \in \mathbb{Z} \mid x^2 = 4\}$。$x^2 = 4$ 的整数解为 $x = 2$ 或 $x = -2$。所以答案为 $\{-2, 2\}$。

---

**2.** 用描述法表示下列集合。

(a) $\{1, 4, 9, 16, 25\} = \{n^2 \mid n \in \mathbb{Z}^+, 1 \leq n \leq 5\}$，或 $\{x \in \mathbb{Z}^+ \mid \exists n \in \{1,2,3,4,5\},\, x = n^2\}$。

(b) $\{2, 3, 5, 7, 11, 13\} = \{p \in \mathbb{Z}^+ \mid p \text{ 是素数且 } p \leq 13\}$。

(c) $\{0, 3, 6, 9, 12, \ldots\} = \{3k \mid k \in \mathbb{N}\} = \{x \in \mathbb{N} \mid 3 \mid x\}$。

---

**3.** 集合运算。$A = \{1, 2, 3, 4, 5\}$, $B = \{3, 5, 7, 9\}$, $U = \{1,2,\ldots,10\}$。

(a) $A \cup B = \{1, 2, 3, 4, 5, 7, 9\}$

(b) $A \cap B = \{3, 5\}$

(c) $A \setminus B = \{1, 2, 4\}$

(d) $B \setminus A = \{7, 9\}$

(e) $A \triangle B = (A \setminus B) \cup (B \setminus A) = \{1, 2, 4, 7, 9\}$

(f) $A^c = U \setminus A = \{6, 7, 8, 9, 10\}$

(g) $(A \cap B)^c = \{3, 5\}^c = \{1, 2, 4, 6, 7, 8, 9, 10\}$

(h) $A^c \cup B^c = \{6,7,8,9,10\} \cup \{1,2,4,6,8,10\} = \{1,2,4,6,7,8,9,10\}$

验证 De Morgan 律：(g) = (h)。✓

---

**4.** 判断真假。

(a) $\emptyset \subseteq \{1, 2, 3\}$：**真。** 空集是任何集合的子集（空真）。

(b) $\emptyset \in \{1, 2, 3\}$：**假。** $\{1, 2, 3\}$ 的元素是 $1, 2, 3$，不包含 $\emptyset$。

(c) $\{1\} \in \{1, 2, 3\}$：**假。** $\{1, 2, 3\}$ 的元素是数字 $1, 2, 3$，不包含集合 $\{1\}$。

(d) $\{1\} \subseteq \{1, 2, 3\}$：**真。** $\{1\}$ 的唯一元素 $1$ 属于 $\{1, 2, 3\}$。

(e) $\{1, 2\} \in \mathcal{P}(\{1, 2, 3\})$：**真。** $\{1, 2\}$ 是 $\{1, 2, 3\}$ 的子集，因此是幂集的元素。

(f) $\{1, 2\} \subseteq \mathcal{P}(\{1, 2, 3\})$：**假。** $\{1, 2\}$ 的元素是 $1$ 和 $2$。但 $1 \notin \mathcal{P}(\{1, 2, 3\})$（$1$ 不是 $\{1, 2, 3\}$ 的子集，因为 $1$ 不是集合）。所以 $\{1, 2\} \not\subseteq \mathcal{P}(\{1, 2, 3\})$。

---

**5.** $\mathcal{P}(\{a, b\}) = \{\emptyset, \{a\}, \{b\}, \{a, b\}\}$。共 $4 = 2^2$ 个元素。✓

---

**6.** 证明 $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$。

**($\subseteq$)** 设 $x \in A \cup (B \cap C)$。则 $x \in A$ 或 $x \in B \cap C$。

- 若 $x \in A$：则 $x \in A \cup B$ 且 $x \in A \cup C$，所以 $x \in (A \cup B) \cap (A \cup C)$。
- 若 $x \in B \cap C$：则 $x \in B$ 且 $x \in C$。由 $x \in B$ 得 $x \in A \cup B$；由 $x \in C$ 得 $x \in A \cup C$。所以 $x \in (A \cup B) \cap (A \cup C)$。

**($\supseteq$)** 设 $x \in (A \cup B) \cap (A \cup C)$。则 $x \in A \cup B$ 且 $x \in A \cup C$。

- 若 $x \in A$：则 $x \in A \cup (B \cap C)$。
- 若 $x \notin A$：由 $x \in A \cup B$ 且 $x \notin A$，得 $x \in B$。由 $x \in A \cup C$ 且 $x \notin A$，得 $x \in C$。所以 $x \in B \cap C$，因此 $x \in A \cup (B \cap C)$。

由双重包含，$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$。$\blacksquare$

---

**7.** 证明 $(A \cap B)^c = A^c \cup B^c$。

**($\subseteq$)** 设 $x \in (A \cap B)^c$。则 $x \notin A \cap B$，即 $\neg(x \in A \wedge x \in B)$。由 De Morgan 律（逻辑），$\neg(x \in A) \vee \neg(x \in B)$，即 $x \notin A$ 或 $x \notin B$。因此 $x \in A^c$ 或 $x \in B^c$，即 $x \in A^c \cup B^c$。

**($\supseteq$)** 设 $x \in A^c \cup B^c$。则 $x \in A^c$ 或 $x \in B^c$，即 $x \notin A$ 或 $x \notin B$。因此 $\neg(x \in A) \vee \neg(x \in B)$，由 De Morgan 律等价于 $\neg(x \in A \wedge x \in B)$，即 $x \notin A \cap B$，即 $x \in (A \cap B)^c$。

由双重包含，$(A \cap B)^c = A^c \cup B^c$。$\blacksquare$

---

**8.** 证明 $A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)$。

将差集转化为交集和补集：$A \setminus X = A \cap X^c$。

$$A \setminus (B \cup C) = A \cap (B \cup C)^c = A \cap (B^c \cap C^c) \quad \text{（De Morgan 律）}$$

$$= (A \cap B^c) \cap (A \cap C^c) \quad \text{（不完全正确——需要结合律和幂等律）}$$

更精确地：$A \cap (B^c \cap C^c) = A \cap B^c \cap C^c$（结合律）。

而 $(A \setminus B) \cap (A \setminus C) = (A \cap B^c) \cap (A \cap C^c) = A \cap A \cap B^c \cap C^c = A \cap B^c \cap C^c$（结合律 + 幂等律 $A \cap A = A$）。

两者相等。$\blacksquare$

---

**9.** 证明 $A \subseteq B \iff A \cap B = A$。

**($\Rightarrow$)** 设 $A \subseteq B$。

$A \cap B \subseteq A$（交集的定义：$x \in A \cap B \implies x \in A$）。

$A \subseteq A \cap B$：设 $x \in A$。由 $A \subseteq B$，$x \in B$。所以 $x \in A$ 且 $x \in B$，即 $x \in A \cap B$。

由双重包含，$A \cap B = A$。

**($\Leftarrow$)** 设 $A \cap B = A$。

设 $x \in A$。则 $x \in A \cap B$（因为 $A = A \cap B$）。所以 $x \in A$ 且 $x \in B$，特别地 $x \in B$。因此 $A \subseteq B$。$\blacksquare$

---

**10.** $|A \times B| = mn$, $|\mathcal{P}(A)| = 2^m$, $|\mathcal{P}(A \times B)| = 2^{mn}$。

$|A \times B| = |A| \cdot |B| = mn$：$A$ 中有 $m$ 个选择作为第一分量，$B$ 中有 $n$ 个选择作为第二分量，共 $mn$ 个有序对。

$|\mathcal{P}(A)| = 2^{|A|} = 2^m$。

$|\mathcal{P}(A \times B)| = 2^{|A \times B|} = 2^{mn}$。

---

**11.** 证明 $\mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B)$。

**($\subseteq$)** 设 $S \in \mathcal{P}(A \cap B)$。则 $S \subseteq A \cap B$，即对所有 $x \in S$，$x \in A$ 且 $x \in B$。因此 $S \subseteq A$（即 $S \in \mathcal{P}(A)$）且 $S \subseteq B$（即 $S \in \mathcal{P}(B)$）。所以 $S \in \mathcal{P}(A) \cap \mathcal{P}(B)$。

**($\supseteq$)** 设 $S \in \mathcal{P}(A) \cap \mathcal{P}(B)$。则 $S \in \mathcal{P}(A)$ 且 $S \in \mathcal{P}(B)$，即 $S \subseteq A$ 且 $S \subseteq B$。设 $x \in S$，则 $x \in A$ 且 $x \in B$，即 $x \in A \cap B$。所以 $S \subseteq A \cap B$，即 $S \in \mathcal{P}(A \cap B)$。

由双重包含，$\mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B)$。$\blacksquare$

---

**12.** $\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)$：**反驳。**

**反例**：设 $A = \{1\}$, $B = \{2\}$。

$\mathcal{P}(A) = \{\emptyset, \{1\}\}$, $\mathcal{P}(B) = \{\emptyset, \{2\}\}$。

$\mathcal{P}(A) \cup \mathcal{P}(B) = \{\emptyset, \{1\}, \{2\}\}$。

$A \cup B = \{1, 2\}$, $\mathcal{P}(A \cup B) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$。

$\{1, 2\} \in \mathcal{P}(A \cup B)$ 但 $\{1, 2\} \notin \mathcal{P}(A) \cup \mathcal{P}(B)$（因为 $\{1, 2\} \not\subseteq A$ 且 $\{1, 2\} \not\subseteq B$）。

所以 $\mathcal{P}(A \cup B) \neq \mathcal{P}(A) \cup \mathcal{P}(B)$。

注：$\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$ 总是成立的（可证明），但反向包含一般不成立。$\blacksquare$

---

## §2 关系

**1.** $A \times B = \{(1, x), (1, y), (2, x), (2, y), (3, x), (3, y)\}$。共 $3 \times 2 = 6$ 个元素。

---

**2.** $A = \{1, 2, 3, 4\}$, $R = \{(a, b) \mid a \leq b\}$：

$$R = \{(1,1), (1,2), (1,3), (1,4), (2,2), (2,3), (2,4), (3,3), (3,4), (4,4)\}$$

共 $1 + 2 + 3 + 4 = 10$ 个有序对。

---

**3.** 判断 $\{1, 2, 3\}$ 上关系的性质。

**(a)** $R_1 = \{(1,1), (2,2), (3,3)\}$（恒等关系）。
- 自反：✓（$(1,1), (2,2), (3,3) \in R_1$）
- 对称：✓（所有对都是 $(a,a)$ 形式）
- 反对称：✓（$a\,R_1\,b \wedge b\,R_1\,a$ 只在 $a = b$ 时发生）
- 传递：✓（$a\,R_1\,b \wedge b\,R_1\,c$ 只在 $a = b = c$ 时发生，此时 $a\,R_1\,c$）

**(b)** $R_2 = \{(1,1), (1,2), (2,1), (2,2), (3,3)\}$。
- 自反：✓
- 对称：✓（$(1,2)$ 和 $(2,1)$ 都在；其余为 $(a,a)$）
- 反对称：✗（$(1,2) \in R_2$ 且 $(2,1) \in R_2$，但 $1 \neq 2$）
- 传递：✓（逐一检查：$(1,2)(2,1) \to (1,1)$✓, $(1,2)(2,2) \to (1,2)$✓, $(2,1)(1,1) \to (2,1)$✓, $(2,1)(1,2) \to (2,2)$✓）

**(c)** $R_3 = \{(1,2), (2,3)\}$。
- 自反：✗（$(1,1) \notin R_3$）
- 对称：✗（$(1,2) \in R_3$ 但 $(2,1) \notin R_3$）
- 反对称：✓（空真——不存在 $a \neq b$ 使得 $a\,R_3\,b$ 且 $b\,R_3\,a$）
- 传递：✗（$(1,2) \in R_3$ 且 $(2,3) \in R_3$，但 $(1,3) \notin R_3$）

**(d)** $R_4 = \{(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)\}$（$\leq$ 关系）。
- 自反：✓
- 对称：✗（$(1,2) \in R_4$ 但 $(2,1) \notin R_4$）
- 反对称：✓（当 $a \neq b$ 时，只有 $(a,b)$ 在 $R_4$ 中，$(b,a)$ 不在）
- 传递：✓（逐一检查所有情况均成立）

---

**4.** $a \sim b \iff 3 \mid (a - b)$。

**自反性**：$a - a = 0$，$3 \mid 0$。✓

**对称性**：$3 \mid (a - b) \implies a - b = 3k \implies b - a = -3k = 3(-k) \implies 3 \mid (b - a)$。✓

**传递性**：$3 \mid (a - b)$ 且 $3 \mid (b - c) \implies a - b = 3k, b - c = 3l \implies a - c = 3(k + l) \implies 3 \mid (a - c)$。✓

等价类：
- $[0] = \{\ldots, -6, -3, 0, 3, 6, 9, \ldots\}$
- $[1] = \{\ldots, -5, -2, 1, 4, 7, 10, \ldots\}$
- $[2] = \{\ldots, -4, -1, 2, 5, 8, 11, \ldots\}$

---

**5.** $A = \{1, 2, 3, 4, 5, 6\}$, $a\,R\,b \iff a \equiv b \pmod{3}$。

**(a)** $R$ 的所有元素（有序对）：

模 $3$ 余 $0$ 的元素：$\{3, 6\}$。模 $3$ 余 $1$ 的元素：$\{1, 4\}$。模 $3$ 余 $2$ 的元素：$\{2, 5\}$。

$$R = \{(1,1), (1,4), (4,1), (4,4), (2,2), (2,5), (5,2), (5,5), (3,3), (3,6), (6,3), (6,6)\}$$

**(b)** 等价类：$[1] = [4] = \{1, 4\}$, $[2] = [5] = \{2, 5\}$, $[3] = [6] = \{3, 6\}$。

**(c)** 划分：$\{\{1, 4\}, \{2, 5\}, \{3, 6\}\}$。

---

**6.** 关系的例子。

**(a)** 自反且对称，但不传递。

在 $\mathbb{Z}$ 上定义 $a\,R\,b \iff |a - b| \leq 1$。

自反：$|a - a| = 0 \leq 1$。✓ 对称：$|a - b| = |b - a|$。✓ 不传递：$1\,R\,2$ 且 $2\,R\,3$，但 $1 \not R\, 3$（$|1 - 3| = 2 > 1$）。✓

**(b)** 自反且传递，但不对称。

$\leq$ 在 $\mathbb{R}$ 上。自反：$a \leq a$。✓ 传递：$a \leq b, b \leq c \implies a \leq c$。✓ 不对称：$1 \leq 2$ 但 $2 \leq 1$ 为假。✓

**(c)** 对称且传递，但不自反。

$A = \{1, 2, 3\}$ 上的 $R = \{(1, 2), (2, 1), (1, 1), (2, 2)\}$。对称：✓。传递：✓（逐一检查）。不自反：$(3, 3) \notin R$。✓

（或者在 $\mathbb{R}$ 上取空关系 $R = \emptyset$：空真地对称、空真地传递，但不自反（$a \not R\, a$ 对所有 $a$）。）

---

**7.** $\{1, 2, 3, 4, 6, 12\}$ 上的整除关系。

**(a)** 自反：$a \mid a$。✓ 反对称：$a \mid b \wedge b \mid a \implies a = b$（在正整数中）。✓ 传递：$a \mid b \wedge b \mid c \implies a \mid c$。✓ 偏序关系。✓

**(b)** Hasse 图。覆盖关系为：$1 \lessdot 2$, $1 \lessdot 3$, $2 \lessdot 4$, $2 \lessdot 6$, $3 \lessdot 6$, $4 \lessdot 12$, $6 \lessdot 12$。

```
       12
      / \
     4   6
     |  / \
     2    3
      \ /
       1
```

**(c)** 极小元素：$1$（也是最小元素）。极大元素：$12$（也是最大元素）。

**(d)** 不是全序集。例如 $3$ 和 $4$ 不可比：$3 \nmid 4$ 且 $4 \nmid 3$。

---

**8.** 证明 $R^{-1} = R$（当 $R$ 是等价关系时）。

$R^{-1} = \{(b, a) \mid (a, b) \in R\}$。

由对称性，$(a, b) \in R \implies (b, a) \in R$。因此：

$R^{-1} \subseteq R$：设 $(b, a) \in R^{-1}$，即 $(a, b) \in R$。由对称性，$(b, a) \in R$。✓

$R \subseteq R^{-1}$：设 $(a, b) \in R$。由对称性，$(b, a) \in R$，即 $(a, b) \in R^{-1}$。✓

所以 $R^{-1} = R$。

$R^{-1}$ 是等价关系：由 $R^{-1} = R$ 且 $R$ 是等价关系，$R^{-1}$ 也是等价关系。$\blacksquare$

---

**9.** $R$ 和 $S$ 都是等价关系。

**(a)** $R \cap S$ 是等价关系。**成立。**

自反：$\forall a,\, (a,a) \in R$（$R$ 自反）且 $(a,a) \in S$（$S$ 自反），所以 $(a,a) \in R \cap S$。✓

对称：设 $(a,b) \in R \cap S$。则 $(a,b) \in R$ 且 $(a,b) \in S$。由 $R$ 对称，$(b,a) \in R$。由 $S$ 对称，$(b,a) \in S$。所以 $(b,a) \in R \cap S$。✓

传递：设 $(a,b) \in R \cap S$ 且 $(b,c) \in R \cap S$。则 $(a,b), (b,c) \in R$，由 $R$ 传递得 $(a,c) \in R$。同理 $(a,c) \in S$。所以 $(a,c) \in R \cap S$。✓

因此 $R \cap S$ 是等价关系。$\blacksquare$

**(b)** $R \cup S$ 是等价关系。**反驳。**

**反例**：$A = \{1, 2, 3\}$。
- $R = \{(1,1), (2,2), (3,3), (1,2), (2,1)\}$（划分 $\{\{1,2\}, \{3\}\}$）。
- $S = \{(1,1), (2,2), (3,3), (2,3), (3,2)\}$（划分 $\{\{1\}, \{2,3\}\}$）。

$R \cup S = \{(1,1), (2,2), (3,3), (1,2), (2,1), (2,3), (3,2)\}$。

传递性检查：$(1,2) \in R \cup S$ 且 $(2,3) \in R \cup S$，但 $(1,3) \notin R \cup S$。传递性失败。✗

所以 $R \cup S$ 一般不是等价关系。$\blacksquare$

---

**10.** $A$ 上不同等价关系的数量。

等价关系与划分一一对应，所以问题等价于求 $A$ 的划分数，即贝尔数 $B_n$。

- $B_1 = 1$：$\{1\}$ 只有一种划分 $\{\{1\}\}$。
- $B_2 = 2$：$\{1,2\}$ 的划分为 $\{\{1,2\}\}$ 和 $\{\{1\}, \{2\}\}$。
- $B_3 = 5$：$\{1,2,3\}$ 的划分为 $\{\{1,2,3\}\}$, $\{\{1,2\}, \{3\}\}$, $\{\{1,3\}, \{2\}\}$, $\{\{2,3\}, \{1\}\}$, $\{\{1\}, \{2\}, \{3\}\}$。
- $B_4 = 15$：可通过贝尔三角或递推公式 $B_{n+1} = \sum_{k=0}^{n}\binom{n}{k}B_k$ 计算。$B_4 = \binom{3}{0}B_0 + \binom{3}{1}B_1 + \binom{3}{2}B_2 + \binom{3}{3}B_3 = 1 + 3 + 6 + 5 = 15$（其中 $B_0 = 1$）。

---

## §3 函数（集合论视角）

**1.** 判断函数。

(a) $\{(1, a), (2, b), (3, c)\}$：**是函数。** 每个定义域元素 $1, 2, 3$ 恰好出现一次。✓

(b) $\{(1, a), (2, a), (3, a)\}$：**是函数。** 每个定义域元素恰好出现一次（虽然值都是 $a$，但这不违反函数的定义——不同的输入可以对应相同的输出）。✓

(c) $\{(1, a), (2, b)\}$：**不是函数。** $3$ 没有对应的值。违反存在性（全域性）。✗

(d) $\{(1, a), (2, b), (3, a), (1, c)\}$：**不是函数。** $1$ 对应了两个值 $a$ 和 $c$。违反唯一性（单值性）。✗

---

**2.** $f(x) = |x|$，$f: \mathbb{R} \to \mathbb{R}$。

**单射**：$f(1) = f(-1) = 1$，但 $1 \neq -1$。不是单射。✗

**满射**：$f(x) = |x| \geq 0$，所以负数不在值域中。例如 $-1$ 没有原像。不是满射。✗

---

**3.** $f(n) = n + 3$，$f: \mathbb{Z} \to \mathbb{Z}$。

**单射**：$n_1 + 3 = n_2 + 3 \implies n_1 = n_2$。✓

**满射**：对任意 $m \in \mathbb{Z}$，取 $n = m - 3 \in \mathbb{Z}$，则 $f(n) = m$。✓

**双射**：是。✓ $f^{-1}(m) = m - 3$。

验证：$f(f^{-1}(m)) = f(m - 3) = (m - 3) + 3 = m$。✓

---

**4.** $f(x) = x^2 - 2x + 1 = (x - 1)^2$。

**(a)** 单射：$f(0) = 1 = f(2)$，但 $0 \neq 2$。不是单射。✗

**(b)** 满射：$f(x) = (x-1)^2 \geq 0$，所以负数不在值域中。不是满射。✗

**(c)** 限制定义域为 $[1, +\infty)$（或 $(-\infty, 1]$），到达域为 $[0, +\infty)$。则 $f: [1, +\infty) \to [0, +\infty)$ 是双射。

单射：在 $[1, +\infty)$ 上，$f$ 严格递增。✓ 满射：对任意 $y \geq 0$，$x = 1 + \sqrt{y} \geq 1$，$f(x) = y$。✓

---

**5.** $f: A \to B$, $g: B \to C$。

**(a)** 若 $g \circ f$ 满射，则 $g$ 满射。

**证明**：设 $c \in C$。由 $g \circ f$ 满射，存在 $a \in A$ 使得 $(g \circ f)(a) = c$，即 $g(f(a)) = c$。令 $b = f(a) \in B$，则 $g(b) = c$。所以对任意 $c \in C$，存在 $b \in B$ 使得 $g(b) = c$。$g$ 满射。$\blacksquare$

**(b)** 反例：$A = \{1\}$, $B = \{a, b\}$, $C = \{x\}$。$f(1) = a$, $g(a) = g(b) = x$。$(g \circ f)(1) = x$，$g \circ f$ 满射。但 $f$ 不是满射（$b$ 不在 $f$ 的值域中）。

---

**6.** 证明 $(f^{-1})^{-1} = f$。

$f: A \to B$ 是双射，$f^{-1}: B \to A$ 也是双射。

$(f^{-1})^{-1}$ 是 $f^{-1}$ 的逆函数，即满足 $(f^{-1})^{-1} \circ f^{-1} = \text{id}_B$ 且 $f^{-1} \circ (f^{-1})^{-1} = \text{id}_A$。

但 $f \circ f^{-1} = \text{id}_B$ 且 $f^{-1} \circ f = \text{id}_A$。

因此 $f$ 满足作为 $f^{-1}$ 的逆函数的条件。由逆函数的唯一性，$(f^{-1})^{-1} = f$。$\blacksquare$

---

**7.** 证明 $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$。

需要验证 $(f^{-1} \circ g^{-1}) \circ (g \circ f) = \text{id}_A$ 且 $(g \circ f) \circ (f^{-1} \circ g^{-1}) = \text{id}_C$。

$$(f^{-1} \circ g^{-1}) \circ (g \circ f) = f^{-1} \circ (g^{-1} \circ g) \circ f = f^{-1} \circ \text{id}_B \circ f = f^{-1} \circ f = \text{id}_A$$

$$(g \circ f) \circ (f^{-1} \circ g^{-1}) = g \circ (f \circ f^{-1}) \circ g^{-1} = g \circ \text{id}_B \circ g^{-1} = g \circ g^{-1} = \text{id}_C$$

由逆函数的唯一性，$(g \circ f)^{-1} = f^{-1} \circ g^{-1}$。$\blacksquare$

---

**8.** 从 $A = \{1, 2, 3\}$ 到 $B = \{a, b\}$ 的函数。

总数：每个定义域元素有 $|B| = 2$ 种选择，共 $2^3 = 8$ 个函数。

满射数：满射要求 $a$ 和 $b$ 都被映射到。总数 $8$ 减去不满射的函数数。

不满射的函数：值域缺少 $a$（即所有值都是 $b$）有 $1$ 个；值域缺少 $b$（即所有值都是 $a$）有 $1$ 个。

由容斥原理：满射数 $= 8 - 1 - 1 = 6$。

（也可以用公式：满射数 $= \sum_{k=0}^{n}(-1)^k\binom{n}{k}(n-k)^m$，其中 $m = |A| = 3$, $n = |B| = 2$：$\binom{2}{0} \cdot 2^3 - \binom{2}{1} \cdot 1^3 + \binom{2}{2} \cdot 0^3 = 8 - 2 + 0 = 6$。）

---

**9.** $a_1 \sim a_2 \iff f(a_1) = f(a_2)$。

**自反性**：$f(a) = f(a)$，所以 $a \sim a$。✓

**对称性**：$a_1 \sim a_2 \implies f(a_1) = f(a_2) \implies f(a_2) = f(a_1) \implies a_2 \sim a_1$。✓

**传递性**：$a_1 \sim a_2 \wedge a_2 \sim a_3 \implies f(a_1) = f(a_2) = f(a_3) \implies f(a_1) = f(a_3) \implies a_1 \sim a_3$。✓

所以 $\sim$ 是等价关系。

等价类 $[a] = \{x \in A \mid f(x) = f(a)\} = f^{-1}(\{f(a)\})$，即 $f(a)$ 的原像。每个等价类由映射到同一个值的所有定义域元素组成。等价类之间的关系刻画了函数的"折叠"结构：$f$ 将同一等价类中的所有元素映射到同一个值。$\blacksquare$

---

**10.** 函数总数和单射数。

**函数总数**：对定义域 $A$ 的每个元素 $a_i$（$i = 1, \ldots, m$），需要在 $B$ 中选一个值 $f(a_i)$，有 $n$ 种选择。由乘法原理，总数为 $n^m$。

**单射数**：$f(a_1)$ 有 $n$ 种选择；$f(a_2)$ 不能等于 $f(a_1)$，有 $n - 1$ 种选择；...；$f(a_m)$ 有 $n - m + 1$ 种选择。

单射数 $= n(n-1)(n-2)\cdots(n-m+1) = \frac{n!}{(n-m)!} = P(n, m)$

当 $m > n$ 时，单射数为 $0$（鸽巢原理：不可能将 $m$ 个不同的值装入 $n < m$ 个"格子"中）。

---

## §4 基数初步

**1.** 双射 $f: \{0, 2, 4, 6, \ldots\} \to \mathbb{N}$：$f(2k) = k$。

单射：$f(2k_1) = f(2k_2) \implies k_1 = k_2 \implies 2k_1 = 2k_2$。✓

满射：对任意 $n \in \mathbb{N}$，$f(2n) = n$。✓

所以 $f$ 是双射。$\blacksquare$

---

**2.** 证明 $(0, 1) \approx (1, +\infty)$。

定义 $f: (0, 1) \to (1, +\infty)$，$f(x) = 1/x$。

单射：$1/x_1 = 1/x_2 \implies x_1 = x_2$。✓

满射：对任意 $y > 1$，$x = 1/y \in (0, 1)$，$f(x) = y$。✓

所以 $f$ 是双射。$\blacksquare$

---

**3.** 证明 $\mathbb{N} \approx \mathbb{N} \setminus \{0\}$。

双射 $f: \mathbb{N} \to \mathbb{N} \setminus \{0\}$，$f(n) = n + 1$。

单射：$n_1 + 1 = n_2 + 1 \implies n_1 = n_2$。✓

满射：对任意 $m \geq 1$，$n = m - 1 \geq 0$，$f(n) = m$。✓

$\blacksquare$

---

**4.** 证明可数集的子集是可数的。

设 $A$ 可数，$B \subseteq A$。如果 $B$ 有限，则 $B$ 可数（有限集是可数的）。

如果 $B$ 无限，由于 $A$ 可数，存在双射 $f: \mathbb{N} \to A$。定义 $B$ 的列举如下：按 $n = 0, 1, 2, \ldots$ 的顺序遍历 $f(n)$，将属于 $B$ 的元素依次记为 $b_0, b_1, b_2, \ldots$（跳过不属于 $B$ 的元素）。

因为 $B$ 无限，这个过程不会终止，所以得到从 $\mathbb{N}$ 到 $B$ 的双射。因此 $B$ 可数无限。$\blacksquare$

---

**5.** 证明 $\mathbb{Z} \times \mathbb{Z}$ 可数。

$\mathbb{Z}$ 可数（已知），即存在双射 $g: \mathbb{N} \to \mathbb{Z}$。

定义 $h: \mathbb{N} \times \mathbb{N} \to \mathbb{Z} \times \mathbb{Z}$，$h(m, n) = (g(m), g(n))$。

$h$ 是双射（因为 $g$ 是双射）。

又 $\mathbb{N} \times \mathbb{N}$ 可数（Cantor 配对函数给出 $\mathbb{N} \approx \mathbb{N} \times \mathbb{N}$）。

因此 $\mathbb{Z} \times \mathbb{Z} \approx \mathbb{N} \times \mathbb{N} \approx \mathbb{N}$，$\mathbb{Z} \times \mathbb{Z}$ 可数。$\blacksquare$

---

**6.** $A \cup B$ 可数（$A, B$ 可数）。

**情况 1**：$A$ 或 $B$ 有限，直接列举即可。

**情况 2**：$A$ 和 $B$ 都可数无限。列举 $A = \{a_0, a_1, a_2, \ldots\}$, $B = \{b_0, b_1, b_2, \ldots\}$。

交替列举：$a_0, b_0, a_1, b_1, a_2, b_2, \ldots$

这给出了从 $\mathbb{N}$ 到 $A \cup B$ 的满射（可能有重复，如果 $A \cap B \neq \emptyset$）。去掉重复后得到 $A \cup B$ 的一个列举。

更精确地：定义 $f: \mathbb{N} \to A \cup B$：

$$f(n) = \begin{cases} a_{n/2}, & n \text{ 偶数} \\ b_{(n-1)/2}, & n \text{ 奇数} \end{cases}$$

$f$ 是满射。由定理 4（可数集的子集可数），$A \cup B$（作为 $f$ 的像）是可数的。$\blacksquare$

---

**7.** 有限长度 $0$-$1$ 串的集合可数。

设 $S_n$ 为长度为 $n$ 的 $0$-$1$ 串的集合。$|S_n| = 2^n$（有限）。

所有有限长度 $0$-$1$ 串的集合为 $S = \bigcup_{n=0}^{\infty} S_n$。这是可数个有限集的并。

列举方式：先列长度 $0$ 的串（$1$ 个：空串），再列长度 $1$ 的串（$2$ 个），再列长度 $2$ 的串（$4$ 个），...

$$\varepsilon; \quad 0, 1; \quad 00, 01, 10, 11; \quad 000, 001, \ldots$$

这给出了 $S$ 的一个列举，因此 $S$ 可数。$\blacksquare$

---

**8.** 无穷长 $0$-$1$ 序列不可数。

设 $\mathcal{S} = \{0, 1\}^\mathbb{N}$ 为所有函数 $s: \mathbb{N} \to \{0, 1\}$ 的集合，即所有无穷 $0$-$1$ 序列。

假设 $\mathcal{S}$ 可数，即可以列举为 $s_0, s_1, s_2, \ldots$。

构造新序列 $t: \mathbb{N} \to \{0, 1\}$：

$$t(n) = 1 - s_n(n)$$

即 $t$ 在第 $n$ 位与 $s_n$ 在第 $n$ 位不同。

则对所有 $n$，$t \neq s_n$（因为 $t(n) \neq s_n(n)$）。所以 $t \notin \{s_0, s_1, s_2, \ldots\}$，矛盾。

因此 $\mathcal{S}$ 不可数。

$\mathcal{P}(\mathbb{N}) \approx \{0, 1\}^\mathbb{N}$ 的双射：子集 $A \subseteq \mathbb{N}$ 对应特征函数 $\chi_A: \mathbb{N} \to \{0, 1\}$，$\chi_A(n) = 1 \iff n \in A$。这是一个双射。

因此 $|\mathcal{P}(\mathbb{N})| = |\{0, 1\}^\mathbb{N}|$ 不可数。$\blacksquare$
