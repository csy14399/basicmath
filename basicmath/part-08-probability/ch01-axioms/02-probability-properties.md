# §2 概率的性质（Properties of Probability）

**前置知识**：[§1 概率的概念](01-probability-concepts.md)（样本空间、事件、Kolmogorov 公理、古典概型）、[Part 1 第 2 章 集合](../../part-01-foundations/ch02-sets/README.md)（集合运算、De Morgan 律）、[Part 7 第 1 章 §2 容斥原理](../../part-07-combinatorics/ch01-counting/02-inclusion-exclusion.md)

**全景图**：上一节建立了概率的公理化定义。本节从这三条公理出发，系统推导概率的各种性质——补集公式、加法公式、容斥原理的概率版本、单调性和 Boole 不等式。这些性质是概率计算的基本工具，在条件概率（Ch02）和分布理论（Ch03）中会反复使用。

**预估学习时间**：约 3–4 小时

---

## 动机

知道了 Kolmogorov 的三条公理之后，一个自然的问题是：**从这三条公理能推出什么？**

事实上，仅凭三条公理就能推出大量有用的性质。本节的目标是系统地推导这些性质，并通过例题展示它们在计算中的应用。

你将看到，很多直觉上"显然"的结论——比如"$A$ 不发生的概率 $= 1$ 减去 $A$ 发生的概率"——都需要（而且能够）从公理严格证明。这正是公理化方法的价值：一切都有据可查。

---

## 1. 补集公式（Complement Rule）

> **定理 1**（补集公式）
>
> 对任意事件 $A$，
>
> $$P(A^c) = 1 - P(A)$$

**证明**：$\Omega = A \cup A^c$，且 $A \cap A^c = \emptyset$。

由公理 3（有限可加性）：$P(\Omega) = P(A) + P(A^c)$。

由公理 2：$P(\Omega) = 1$。

故 $P(A^c) = 1 - P(A)$。$\blacksquare$

**应用：正难则反**。当 $P(A)$ 难以直接计算时，可以先算 $P(A^c)$，再用 $P(A) = 1 - P(A^c)$。

> **例 1**（至少一个正面）
>
> 掷 $10$ 枚公平硬币，求至少一枚正面的概率。

**解**：直接计算"至少一枚正面"需要考虑恰好 $1, 2, \ldots, 10$ 枚正面的所有情况。

用补集法：$A^c$ = "没有正面"= "全部反面"。

$$P(A^c) = \left(\frac{1}{2}\right)^{10} = \frac{1}{1024}$$

$$P(A) = 1 - \frac{1}{1024} = \frac{1023}{1024} \approx 0.999 \quad \blacksquare$$

---

## 2. 加法公式（Addition Rule）

### 2.1 两个事件的加法公式

> **定理 2**（加法公式 / 概率版容斥，两事件）
>
> 对任意两个事件 $A$ 和 $B$，
>
> $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**证明**：将 $A \cup B$ 分解为三个两两互斥的部分：

$$A \cup B = (A \cap B^c) \cup (A \cap B) \cup (A^c \cap B)$$

由有限可加性：

$$P(A \cup B) = P(A \cap B^c) + P(A \cap B) + P(A^c \cap B)$$

又 $A = (A \cap B^c) \cup (A \cap B)$，两者互斥，故 $P(A) = P(A \cap B^c) + P(A \cap B)$，即 $P(A \cap B^c) = P(A) - P(A \cap B)$。

同理 $P(A^c \cap B) = P(B) - P(A \cap B)$。

代入：

$$P(A \cup B) = [P(A) - P(A \cap B)] + P(A \cap B) + [P(B) - P(A \cap B)]$$

$$= P(A) + P(B) - P(A \cap B) \quad \blacksquare$$

### 2.2 特殊情况

- **互斥事件**：若 $A \cap B = \emptyset$，则 $P(A \cap B) = 0$，加法公式退化为 $P(A \cup B) = P(A) + P(B)$（公理 3 的有限版本）。
- **上界**：由于 $P(A \cap B) \geq 0$，总有 $P(A \cup B) \leq P(A) + P(B)$。

---

## 3. 概率版容斥原理（Inclusion-Exclusion for Probability）

### 3.1 三个事件

> **定理 3**（容斥原理，三事件）
>
> $$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

**证明思路**：先将 $A \cup B \cup C = (A \cup B) \cup C$，对 $A \cup B$ 和 $C$ 用定理 2，然后对 $P((A \cup B) \cap C) = P((A \cap C) \cup (B \cap C))$ 再用一次定理 2，展开整理即得。

> **例 2**（三事件容斥）
>
> 在一个班级中，$60\%$ 的学生喜欢数学（$M$），$50\%$ 喜欢物理（$P$），$40\%$ 喜欢化学（$C$）。同时喜欢数学和物理的有 $30\%$，同时喜欢数学和化学的有 $20\%$，同时喜欢物理和化学的有 $15\%$。三门都喜欢的有 $10\%$。求至少喜欢一门的学生比例。

**解**：

$$P(M \cup P \cup C) = 0.6 + 0.5 + 0.4 - 0.3 - 0.2 - 0.15 + 0.1 = 0.95$$

$95\%$ 的学生至少喜欢一门学科。$\blacksquare$

### 3.2 一般容斥原理

> **定理 4**（容斥原理，一般形式）
>
> 对任意 $n$ 个事件 $A_1, A_2, \ldots, A_n$，
>
> $$P\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i} P(A_i) - \sum_{i<j} P(A_i \cap A_j) + \sum_{i<j<k} P(A_i \cap A_j \cap A_k) - \cdots + (-1)^{n+1} P(A_1 \cap \cdots \cap A_n)$$

这与 Part 7 中集合的容斥原理完全平行——只是把 $|A|$ 换成了 $P(A)$。

---

## 4. 单调性（Monotonicity）

> **定理 5**（单调性）
>
> 若 $A \subseteq B$，则 $P(A) \leq P(B)$。

**证明**：$B = A \cup (B \setminus A)$，且 $A \cap (B \setminus A) = \emptyset$。

由有限可加性：$P(B) = P(A) + P(B \setminus A)$。

由公理 1：$P(B \setminus A) \geq 0$。

故 $P(A) \leq P(B)$。$\blacksquare$

**直觉**："包含更多样本点的事件，概率不会更小。"

### 差集公式

上面的证明同时给出了**差集公式**：

$$P(B \setminus A) = P(B) - P(A) \quad \text{（当 $A \subseteq B$ 时）}$$

更一般地，$P(B \setminus A) = P(B) - P(A \cap B)$（不需要 $A \subseteq B$）。

---

## 5. Boole 不等式（Union Bound）

> **定理 6**（Boole 不等式 / 次可加性）
>
> 对任意事件 $A_1, A_2, \ldots, A_n$（不要求互斥），
>
> $$P\!\left(\bigcup_{i=1}^{n} A_i\right) \leq \sum_{i=1}^{n} P(A_i)$$

**证明**（归纳法）：

**基底**：$n = 1$ 时，$P(A_1) \leq P(A_1)$，成立。

**归纳步骤**：假设对 $n-1$ 个事件成立。

$$P\!\left(\bigcup_{i=1}^{n} A_i\right) = P\!\left(\bigcup_{i=1}^{n-1} A_i\right) + P(A_n) - P\!\left(\left(\bigcup_{i=1}^{n-1} A_i\right) \cap A_n\right)$$

由 $P\!\left(\left(\bigcup_{i=1}^{n-1} A_i\right) \cap A_n\right) \geq 0$，

$$\leq P\!\left(\bigcup_{i=1}^{n-1} A_i\right) + P(A_n) \leq \sum_{i=1}^{n-1} P(A_i) + P(A_n) = \sum_{i=1}^{n} P(A_i) \quad \blacksquare$$

**可列形式**：Boole 不等式也对可列多个事件成立：

$$P\!\left(\bigcup_{i=1}^{\infty} A_i\right) \leq \sum_{i=1}^{\infty} P(A_i)$$

### Boole 不等式的意义

Boole 不等式虽然是一个**不等式**而非等式，但在实际中非常有用——当精确计算 $P(\bigcup A_i)$ 很困难时，Boole 不等式提供了一个快速的**上界估计**。

> **例 3**（Boole 不等式应用）
>
> 一个系统有 $100$ 个独立组件，每个组件故障的概率为 $0.001$。估计至少一个组件故障的概率的上界。

**解**：设 $A_i$ = "第 $i$ 个组件故障"，$P(A_i) = 0.001$。

$$P\!\left(\bigcup_{i=1}^{100} A_i\right) \leq \sum_{i=1}^{100} P(A_i) = 100 \times 0.001 = 0.1$$

至少一个组件故障的概率不超过 $10\%$。$\blacksquare$

（精确值为 $1 - (1 - 0.001)^{100} \approx 0.0952$，Boole 上界 $0.1$ 相当接近。当各事件概率都很小时，Boole 不等式是很好的近似。）

---

## 6. 概率的连续性（Continuity of Probability）

### 6.1 递增事件列

> **定理 7**（概率的下连续性）
>
> 若 $A_1 \subseteq A_2 \subseteq A_3 \subseteq \cdots$（递增事件列），则
>
> $$P\!\left(\bigcup_{n=1}^{\infty} A_n\right) = \lim_{n \to \infty} P(A_n)$$

**证明思路**：设 $B_1 = A_1$，$B_n = A_n \setminus A_{n-1}$（$n \geq 2$）。则 $B_1, B_2, \ldots$ 两两互斥，$\bigcup B_n = \bigcup A_n$。由可列可加性：

$$P\!\left(\bigcup A_n\right) = \sum_{n=1}^{\infty} P(B_n) = \lim_{N \to \infty} \sum_{n=1}^{N} P(B_n) = \lim_{N \to \infty} P(A_N) \quad \blacksquare$$

### 6.2 递减事件列

> **定理 8**（概率的上连续性）
>
> 若 $A_1 \supseteq A_2 \supseteq A_3 \supseteq \cdots$（递减事件列），则
>
> $$P\!\left(\bigcap_{n=1}^{\infty} A_n\right) = \lim_{n \to \infty} P(A_n)$$

**证明**：对补集 $A_n^c$ 应用定理 7（$A_1^c \subseteq A_2^c \subseteq \cdots$），再用 De Morgan 律和补集公式。

**注意**：连续性定理是可列可加性的推论——这正是公理 3 要求"可列"而非仅"有限"可加性的重要原因之一。

---

## 7. 性质总结表

| 性质 | 公式 | 条件 |
|------|------|------|
| 补集 | $P(A^c) = 1 - P(A)$ | 任意 $A$ |
| 加法（两事件） | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | 任意 $A, B$ |
| 互斥加法 | $P(A \cup B) = P(A) + P(B)$ | $A \cap B = \emptyset$ |
| 单调性 | $P(A) \leq P(B)$ | $A \subseteq B$ |
| 差集 | $P(B \setminus A) = P(B) - P(A \cap B)$ | 任意 $A, B$ |
| Boole 不等式 | $P(\bigcup A_i) \leq \sum P(A_i)$ | 任意事件列 |
| 容斥（一般） | 交替加减各阶交集的概率 | 任意有限事件族 |

---

## 例题

> **例题 1**
>
> 设 $P(A) = 0.6$，$P(B) = 0.5$，$P(A \cap B) = 0.3$。求 (a) $P(A \cup B)$；(b) $P(A^c \cap B^c)$；(c) $P(A \cap B^c)$。

**解**：

(a) $P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.6 + 0.5 - 0.3 = 0.8$。

(b) 由 De Morgan 律，$A^c \cap B^c = (A \cup B)^c$。

$$P(A^c \cap B^c) = 1 - P(A \cup B) = 1 - 0.8 = 0.2$$

(c) $P(A \cap B^c) = P(A) - P(A \cap B) = 0.6 - 0.3 = 0.3$。$\blacksquare$

> **例题 2**
>
> 掷两个公平骰子。设 $A$ = "第一个骰子是偶数"，$B$ = "两个骰子点数之和 $\leq 5$"。求 $P(A \cup B)$。

**解**：$\Omega = \{(i,j): 1 \leq i,j \leq 6\}$，$|\Omega| = 36$。

$A = \{(i,j): i \in \{2,4,6\}\}$，$|A| = 3 \times 6 = 18$，$P(A) = 18/36 = 1/2$。

$B = \{(i,j): i+j \leq 5\}$。枚举：$(1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1)$，$|B| = 10$，$P(B) = 10/36 = 5/18$。

$A \cap B = \{(i,j): i \in \{2,4,6\} \text{ 且 } i+j \leq 5\}$。

- $i=2$：$j \leq 3$，即 $j \in \{1,2,3\}$，$3$ 个
- $i=4$：$j \leq 1$，即 $j = 1$，$1$ 个
- $i=6$：$j \leq -1$，不存在

$|A \cap B| = 4$，$P(A \cap B) = 4/36 = 1/9$。

$$P(A \cup B) = \frac{1}{2} + \frac{5}{18} - \frac{1}{9} = \frac{9}{18} + \frac{5}{18} - \frac{2}{18} = \frac{12}{18} = \frac{2}{3} \quad \blacksquare$$

> **例题 3**
>
> 证明：对任意三个事件 $A, B, C$，
> $$P(A \cup B \cup C) \leq P(A) + P(B) + P(C)$$
> 并说明等号成立的充要条件。

**证明**：由容斥原理（定理 3）：

$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

由于 $P(A \cap B \cap C) \leq P(A \cap B)$（单调性，因为 $A \cap B \cap C \subseteq A \cap B$），类似地 $P(A \cap B \cap C) \leq P(A \cap C)$ 和 $P(A \cap B \cap C) \leq P(B \cap C)$，所以

$$-P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C) \leq 0$$

因此 $P(A \cup B \cup C) \leq P(A) + P(B) + P(C)$。

等号成立的充要条件是 $P(A \cap B) = P(A \cap C) = P(B \cap C) = P(A \cap B \cap C) = 0$，即 $A, B, C$ 两两互斥。$\blacksquare$

---

## 要点回顾

| 性质 | 核心思想 |
|------|----------|
| 补集 $P(A^c) = 1-P(A)$ | "正难则反"——算不发生比算发生容易 |
| 加法 $P(A \cup B) = P(A)+P(B)-P(A \cap B)$ | 避免重复计算交集部分 |
| 容斥 | 交替加减——与 Part 7 的集合容斥完全平行 |
| 单调性 $A \subseteq B \Rightarrow P(A) \leq P(B)$ | 更大的集合概率不会更小 |
| Boole 不等式 $P(\bigcup A_i) \leq \sum P(A_i)$ | 快速估计并集概率的上界 |

---

## 进度检查点

完成本节后，你应该能够：

- [ ] 使用补集公式简化概率计算
- [ ] 对两个和三个事件运用加法公式（容斥原理）
- [ ] 从公理出发证明概率的基本性质
- [ ] 使用 Boole 不等式估计概率上界
- [ ] 判断何时等号成立（互斥条件）

---

## 自测题

**题 1**：$P(A) = 0.7$，$P(B) = 0.4$。$P(A \cup B)$ 的最大值和最小值分别是多少？

<details>
<summary>答案</summary>

$P(A \cup B) = P(A) + P(B) - P(A \cap B)$。

$P(A \cap B)$ 的范围：$\max(0, P(A)+P(B)-1) \leq P(A \cap B) \leq \min(P(A), P(B))$，即 $0.1 \leq P(A \cap B) \leq 0.4$。

所以 $P(A \cup B)$ 的范围：

- 最大值：$P(A \cap B)$ 最小时，$P(A \cup B) = 0.7 + 0.4 - 0.1 = 1.0$。
- 最小值：$P(A \cap B)$ 最大时，$P(A \cup B) = 0.7 + 0.4 - 0.4 = 0.7$。

$P(A \cup B) \in [0.7, 1.0]$。
</details>

**题 2**：$P(A) = 0.3$，$P(B) = 0.4$，$P(A \cup B) = 0.6$。求 $P(A \cap B)$。

<details>
<summary>答案</summary>

$P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.3 + 0.4 - 0.6 = 0.1$。
</details>

**题 3**：三次独立掷硬币，求至少两次正面的概率。

<details>
<summary>答案</summary>

$\Omega$ 有 $8$ 个等可能样本点。

至少两次正面 = 恰好两次 + 恰好三次 = $\{HHT, HTH, THH, HHH\}$，$4$ 个。

$P = 4/8 = 1/2$。

或用补集：$P(\text{至少两次正面}) = 1 - P(\text{0 次或 1 次正面})$。

$0$ 次：$TTT$，$1$ 个；$1$ 次：$HTT, THT, TTH$，$3$ 个。共 $4$ 个。$P = 1 - 4/8 = 1/2$。
</details>

**题 4**：设 $A_1, A_2, \ldots, A_{10}$ 是事件，每个 $P(A_i) = 0.05$。$P(\bigcup_{i=1}^{10} A_i)$ 至多是多少？

<details>
<summary>答案</summary>

由 Boole 不等式：$P(\bigcup A_i) \leq \sum P(A_i) = 10 \times 0.05 = 0.5$。

最大值 $0.5$，当 $A_1, \ldots, A_{10}$ 两两互斥时取等。
</details>

---

## 习题引用

本节的练习见 [exercises/exercises.md](exercises/exercises.md)。
