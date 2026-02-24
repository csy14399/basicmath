# 第一章 逻辑 — 练习题解答

## §1 命题逻辑（Propositional Logic）

**1.** 判断下列句子中哪些是命题。

命题（proposition）是一个有确定真值（真或假）的陈述句。

(a) $3 + 5 = 8$

**是命题。** 这是一个陈述句，其真值为真（T）。

(b) 请关上门。

**不是命题。** 这是一个祈使句（命令），没有真值。

(c) $x^2 + 1 > 0$

**不是命题（严格来说）。** 含有自由变量 $x$，其真值取决于 $x$ 的取值。它是一个谓词（propositional function），而非命题。若指定了 $x$ 的值或加上量词，则可成为命题。

(d) 你今天吃早饭了吗？

**不是命题。** 这是一个疑问句，没有真值。

(e) 这句话是假的。

**不是命题。** 这是说谎者悖论（Liar's Paradox）。假设它是命题：若为真，则它所断言的"自己为假"成立，矛盾；若为假，则"自己为假"不成立，即自己为真，矛盾。因此它不能被赋予确定的真值，不构成命题。

(f) 所有偶数都能被 $2$ 整除。

**是命题。** 这是一个陈述句，其真值为真（T）。（偶数的定义就是能被 $2$ 整除的整数。）

---

**2.** 构造 $(p \wedge q) \to (\neg p \vee q)$ 的真值表。

| $p$ | $q$ | $p \wedge q$ | $\neg p$ | $\neg p \vee q$ | $(p \wedge q) \to (\neg p \vee q)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | T | T |
| T | F | F | F | F | T |
| F | T | F | T | T | T |
| F | F | F | T | T | T |

最后一列全为 T，因此 $(p \wedge q) \to (\neg p \vee q)$ 是**重言式（tautology）**。

直觉理解：当 $p \wedge q$ 为真时，$q$ 为真，于是 $\neg p \vee q$ 为真；当 $p \wedge q$ 为假时，蕴含式前件为假，整个蕴含式为真。

---

**3.** 用真值表验证 $p \to q \equiv \neg p \vee q$。

| $p$ | $q$ | $p \to q$ | $\neg p$ | $\neg p \vee q$ |
|:---:|:---:|:---:|:---:|:---:|
| T | T | T | F | T |
| T | F | F | F | F |
| F | T | T | T | T |
| F | F | T | T | T |

$p \to q$ 与 $\neg p \vee q$ 在所有行的真值完全相同，故 $p \to q \equiv \neg p \vee q$。$\blacksquare$

---

**4.** 用逻辑等价律化简 $\neg(\neg p \wedge q)$。

$$\neg(\neg p \wedge q) \equiv \neg(\neg p) \vee \neg q \quad \text{（德摩根律，De Morgan's Law）}$$

$$\equiv p \vee \neg q \quad \text{（双重否定律，Double Negation Law）}$$

最终结果：$\neg(\neg p \wedge q) \equiv p \vee \neg q$。

---

**5.** 判断 $(p \to q) \wedge (q \to p) \equiv p \leftrightarrow q$。

**方法一：真值表**

| $p$ | $q$ | $p \to q$ | $q \to p$ | $(p \to q) \wedge (q \to p)$ | $p \leftrightarrow q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | T | T |
| T | F | F | T | F | F |
| F | T | T | F | F | F |
| F | F | T | T | T | T |

两列完全相同，因此 $(p \to q) \wedge (q \to p) \equiv p \leftrightarrow q$。$\blacksquare$

**方法二：等价律**

由双条件的定义，$p \leftrightarrow q$ 就定义为 $(p \to q) \wedge (q \to p)$，因此二者等价是定义本身的直接推论。

---

**6.** 证明 $\{\neg, \wedge\}$ 是功能完备集。

**证明**：已知 $\{\neg, \wedge, \vee\}$ 可以表达所有真值函数（因为任何布尔函数都有析取范式，析取范式仅使用 $\neg, \wedge, \vee$）。因此只需证明 $\vee$ 可以由 $\neg$ 和 $\wedge$ 表示。

由德摩根律：
$$p \vee q \equiv \neg(\neg p \wedge \neg q).$$

右边只含 $\neg$ 和 $\wedge$，因此 $\vee$ 可被 $\{\neg, \wedge\}$ 表示。

同理，蕴含可表示为：
$$p \to q \equiv \neg p \vee q \equiv \neg(\neg(\neg p) \wedge \neg q) \equiv \neg(p \wedge \neg q).$$

由于 $\{\neg, \wedge, \vee\}$ 的功能完备性已知（任何真值函数的析取范式仅用这三个联结词），而 $\vee$ 可由 $\{\neg, \wedge\}$ 构造，故 $\{\neg, \wedge\}$ 也是功能完备集。$\blacksquare$

---

**7.** 用 $\neg, \wedge, \vee$ 表示 $p \oplus q$。

异或的含义：$p \oplus q$ 为真当且仅当 $p$ 和 $q$ 恰好有一个为真。

$$(p \oplus q) \equiv (p \vee q) \wedge \neg(p \wedge q)$$

也可以写作：

$$(p \oplus q) \equiv (p \wedge \neg q) \vee (\neg p \wedge q)$$

**真值表验证**（以第二种形式为例）：

| $p$ | $q$ | $p \wedge \neg q$ | $\neg p \wedge q$ | $(p \wedge \neg q) \vee (\neg p \wedge q)$ | $p \oplus q$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | F | F | F | F |
| T | F | T | F | T | T |
| F | T | F | T | T | T |
| F | F | F | F | F | F |

最后两列完全一致，验证成功。$\blacksquare$

---

**8.** 用等价律证明 $(p \to q) \wedge (p \to r) \equiv p \to (q \wedge r)$。

$$\text{左边} = (p \to q) \wedge (p \to r)$$

$$= (\neg p \vee q) \wedge (\neg p \vee r) \quad \text{（蕴含等价式）}$$

$$= \neg p \vee (q \wedge r) \quad \text{（分配律，Distributive Law：} A \vee (B \wedge C) \equiv (A \vee B) \wedge (A \vee C)\text{的逆向使用）}$$

$$= p \to (q \wedge r) \quad \text{（蕴含等价式）}$$

$$= \text{右边}$$

关键步骤解释：分配律 $A \vee (B \wedge C) \equiv (A \vee B) \wedge (A \vee C)$ 令 $A = \neg p$，$B = q$，$C = r$，得 $(\neg p \vee q) \wedge (\neg p \vee r) \equiv \neg p \vee (q \wedge r)$。$\blacksquare$

---

**9.** 已知 $p \to q$ 为假，确定 $p$ 和 $q$ 的真值。

回顾蕴含的真值表：

| $p$ | $q$ | $p \to q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | **F** |
| F | T | T |
| F | F | T |

$p \to q$ 为假的唯一情况是 $p$ 为**真**且 $q$ 为**假**。

直觉理解：蕴含 $p \to q$ 的含义是"若 $p$ 成立则 $q$ 也成立"。唯一使此承诺落空的情况是：前提 $p$ 确实成立了，但结论 $q$ 却不成立。

---

**10.** 证明假言三段论（hypothetical syllogism）：若 $p \to q$ 与 $q \to r$ 均为真，则 $p \to r$ 为真。

**证明**：假设 $p \to q$ 为真且 $q \to r$ 为真。需证 $p \to r$ 为真。

对 $p$ 的真值分两种情况讨论：

**情况 1**：$p$ 为假。

此时无论 $r$ 取何值，$p \to r$ 为真（前件为假的蕴含恒真）。

**情况 2**：$p$ 为真。

由 $p$ 为真和 $p \to q$ 为真（肯定前件律，modus ponens），得 $q$ 为真。

由 $q$ 为真和 $q \to r$ 为真（再次使用肯定前件律），得 $r$ 为真。

因此 $p$ 为真且 $r$ 为真，$p \to r$ 为真。

两种情况下 $p \to r$ 均为真。$\blacksquare$

**方法二：等价律**

$$(p \to q) \wedge (q \to r) \to (p \to r)$$

用真值表可以验证这是一个重言式。由于有 $3$ 个变量，真值表有 $8$ 行：

| $p$ | $q$ | $r$ | $p \to q$ | $q \to r$ | $(p \to q) \wedge (q \to r)$ | $p \to r$ | 整体 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | T | T | T | T |
| T | T | F | T | F | F | F | T |
| T | F | T | F | T | F | T | T |
| T | F | F | F | T | F | F | T |
| F | T | T | T | T | T | T | T |
| F | T | F | T | F | F | T | T |
| F | F | T | T | T | T | T | T |
| F | F | F | T | T | T | T | T |

最后一列全为 T，是重言式。因此假言三段论成立。$\blacksquare$

---

**11.** 骑士与无赖问题。

**(a) 形式化**

设命题变量：
- $a$：A 是骑士（$a$ 为真 $\Leftrightarrow$ A 是骑士）
- $b$：B 是骑士（$b$ 为真 $\Leftrightarrow$ B 是骑士）

骑士说的话为真，无赖说的话为假。

A 说"B 是骑士"。
- 若 A 是骑士（$a$ 为真），则 A 说的为真，即 $b$ 为真。
- 若 A 是无赖（$a$ 为假），则 A 说的为假，即 $b$ 为假。
- 因此：$a \leftrightarrow b$。

B 说"A 和我是不同类型的"。
- "A 和我是不同类型的"即 $\neg(a \leftrightarrow b)$，即 $a \oplus b$。
- 若 B 是骑士（$b$ 为真），则此话为真：$a \oplus b$ 为真。
- 若 B 是无赖（$b$ 为假），则此话为假：$a \oplus b$ 为假，即 $a \leftrightarrow b$ 为真。
- 因此：$b \leftrightarrow (a \oplus b)$。

**(b)-(c) 求解**

由 A 的话得：$a \leftrightarrow b$ ——即 A 和 B 同类型。

由 B 的话得：$b \leftrightarrow (a \oplus b)$。

将 $a \leftrightarrow b$（A 和 B 同类型）代入 B 的约束：

若 $a \leftrightarrow b$ 为真（即 A、B 同类），则 $a \oplus b$ 为假。于是 B 的约束变为 $b \leftrightarrow F$，即 $b$ 为假（B 是无赖）。

由 $a \leftrightarrow b$ 和 $b$ 为假，得 $a$ 为假（A 是无赖）。

**验证**：
- A 是无赖，说"B 是骑士"——这是假话。B 确实不是骑士（B 是无赖），所以 A 的话为假。✓
- B 是无赖，说"A 和我是不同类型的"——这是假话。A 和 B 确实是同类型的（都是无赖），所以 B 的话为假。✓

**结论：A 和 B 都是无赖（knave）。**

---

**12.** $n$ 个命题变量的真值表行数。

每个命题变量有 $2$ 个可能取值（T 或 F）。$n$ 个独立的命题变量的所有可能取值组合数为：

$$2^n$$

这是因为每增加一个变量，可能性翻倍（乘法原理/counting principle）。

- $n = 1$：$2$ 行
- $n = 2$：$4$ 行
- $n = 3$：$8$ 行
- $n = 10$：$1024$ 行
- $n = 20$：$1{,}048{,}576$（约一百万）行
- $n = 100$：$2^{100} \approx 1.27 \times 10^{30}$ 行

**为什么真值表方法不切实际？** 真值表行数随变量数呈指数增长（exponential growth）。当变量数超过 $20$ 至 $30$ 个时，行数已达天文数字，无论用纸笔还是计算机都无法在合理时间内穷尽所有行。这正是为什么我们需要等价律、推理规则等**符号化方法**——它们允许我们在不枚举所有情况的前提下进行证明。

这也与计算机科学中的**可满足性问题（SAT problem）**直接相关：判断一个命题公式是否可满足已被证明是 NP 完全问题（NP-complete），目前没有已知的多项式时间算法。

---

## §2 谓词逻辑（Predicate Logic）

**1.** 翻译"每个大于 $1$ 的整数要么是素数，要么是合数"。

**论域**：$\mathbb{Z}$（全体整数），或更精确地取 $D = \{n \in \mathbb{Z} : n > 1\}$。

**谓词**：
- $\text{Prime}(x)$：$x$ 是素数
- $\text{Composite}(x)$：$x$ 是合数

**翻译**（论域为 $\mathbb{Z}$）：

$$\forall x\, \bigl(x \in \mathbb{Z} \wedge x > 1 \bigr) \to \bigl(\text{Prime}(x) \vee \text{Composite}(x)\bigr)$$

或者更常见的写法：

$$\forall x\, \bigl(x > 1 \to (\text{Prime}(x) \vee \text{Composite}(x))\bigr)$$

注意异或也可接受（因为素数与合数互斥），但使用 $\vee$ 即可，因为二者不会同时为真。

---

**2.** 写出 $\forall x\, \exists y\, (x + y = 0)$ 的否定式（论域 $\mathbb{Z}$）。

逐步否定：

$$\neg \bigl[\forall x\, \exists y\, (x + y = 0)\bigr]$$

$$\equiv \exists x\, \neg \bigl[\exists y\, (x + y = 0)\bigr] \quad \text{（}\forall\text{ 的否定变 }\exists\text{）}$$

$$\equiv \exists x\, \forall y\, \neg(x + y = 0) \quad \text{（}\exists\text{ 的否定变 }\forall\text{）}$$

$$\equiv \exists x\, \forall y\, (x + y \neq 0)$$

**自然语言**：存在一个整数 $x$，使得对所有整数 $y$，都有 $x + y \neq 0$。

**真值判断**：

- 原命题 $\forall x\, \exists y\, (x + y = 0)$：对每个整数 $x$，取 $y = -x$ 即可得 $x + y = 0$。所以原命题为**真**。
- 否定式：为**假**（因为原命题为真）。

---

**3.** 在 $\forall x\, (P(x, y) \to \exists z\, Q(z))$ 中区分自由变量和约束变量。

- $x$：被 $\forall x$ 约束，是**约束变量（bound variable）**。
- $y$：没有被任何量词约束，是**自由变量（free variable）**。
- $z$：被 $\exists z$ 约束，是**约束变量（bound variable）**。

因此该公式有一个自由变量 $y$。这意味着该公式的真值取决于 $y$ 的取值——在赋予 $y$ 具体值之前，它不是一个命题而是一个**命题函数**。

---

**4.** $\forall x\, (x^2 \geq 0)$ 在 $\mathbb{R}$ 和 $\mathbb{C}$ 上的讨论。

**在 $\mathbb{R}$ 上**：对任意实数 $x$，$x^2 \geq 0$ 恒成立（实数的平方非负）。所以该命题为**真**。

**在 $\mathbb{C}$ 上**：该命题**没有意义**（至少在通常意义下）。复数域 $\mathbb{C}$ 上不存在与实数域兼容的全序关系。换言之，$\geq$ 对复数没有标准定义。例如 $i^2 = -1$，但我们不能说 $-1 \geq 0$ 也不能说 $-1 < 0$ 在复数的意义下成立——因为 $\geq$ 本身未定义。

严格地说，要使 $\forall x\, (x^2 \geq 0)$ 有意义，论域上需要配备一个序关系。$\mathbb{R}$ 有自然序，$\mathbb{C}$ 没有（至少不是有序域）。

---

**5.** 阿基米德性质（Archimedean property）的形式化与否定。

**形式化**：

令论域为实数。设 $\mathbb{Z}^+$ 表示正整数集。

$$\forall \epsilon\, \Bigl(\epsilon > 0 \to \exists N\, \bigl(N \in \mathbb{Z}^+ \wedge \frac{1}{N} < \epsilon\bigr)\Bigr)$$

**否定式**：

$$\neg\Bigl[\forall \epsilon\, \Bigl(\epsilon > 0 \to \exists N\, \bigl(N \in \mathbb{Z}^+ \wedge \frac{1}{N} < \epsilon\bigr)\Bigr)\Bigr]$$

$$\equiv \exists \epsilon\, \Bigl(\epsilon > 0 \wedge \neg\bigl[\exists N\, (N \in \mathbb{Z}^+ \wedge \frac{1}{N} < \epsilon)\bigr]\Bigr)$$

（注意 $\neg(A \to B) \equiv A \wedge \neg B$）

$$\equiv \exists \epsilon\, \Bigl(\epsilon > 0 \wedge \forall N\, \bigl(N \in \mathbb{Z}^+ \to \frac{1}{N} \geq \epsilon\bigr)\Bigr)$$

（注意 $\neg(A \wedge B) \equiv \neg A \vee \neg B$，以及 $\neg(N \in \mathbb{Z}^+) \vee \frac{1}{N} \geq \epsilon$ 即 $N \in \mathbb{Z}^+ \to \frac{1}{N} \geq \epsilon$）

**自然语言翻译**：存在一个正实数 $\epsilon$，使得对所有正整数 $N$，都有 $1/N \geq \epsilon$。

换言之，$1/N$ 不能任意小——存在一个正下界。（在实数中阿基米德性质成立，所以否定式为假。）

---

**6.** $\forall x\, \exists y\, (x < y)$ 与 $\exists y\, \forall x\, (x < y)$ 的区别。

**语义区别**：

- $\forall x\, \exists y\, (x < y)$：对**每个** $x$，**存在**（可能依赖于 $x$ 的）$y$ 使得 $x < y$。直觉：无论给定什么数，总能找到更大的数。
- $\exists y\, \forall x\, (x < y)$：**存在**一个固定的 $y$，使得**所有** $x$ 都小于它。直觉：存在一个"最大数"比所有数都大。

**在 $\mathbb{R}$ 上**：

- $\forall x\, \exists y\, (x < y)$：**真**。对任意 $x \in \mathbb{R}$，取 $y = x + 1$ 即可。
- $\exists y\, \forall x\, (x < y)$：**假**。$\mathbb{R}$ 中不存在最大的实数。若存在这样的 $y$，则 $y + 1 > y$，但同时要求 $y + 1 < y$，矛盾。

**在 $\{1, 2, 3\}$ 上**：

- $\forall x\, \exists y\, (x < y)$：**假**。取 $x = 3$，不存在域中的 $y$ 使得 $3 < y$（$y$ 只能取 $1, 2, 3$）。
- $\exists y\, \forall x\, (x < y)$：**假**。同理，$y = 3$ 是最大的候选者，但 $3 < 3$ 不成立。

注意：$\forall x\, \exists y$ 不能随意交换为 $\exists y\, \forall x$。前者允许 $y$ 依赖于 $x$，后者要求 $y$ 独立于 $x$。一般地，$\exists y\, \forall x\, P(x,y) \Rightarrow \forall x\, \exists y\, P(x,y)$，但反向不成立。

---

**7.** 翻译并判断"存在一个实数是其自身的平方"。

**谓词逻辑表达**：

$$\exists x \in \mathbb{R}\, (x^2 = x)$$

或写为：$\exists x\, (x \in \mathbb{R} \wedge x^2 = x)$。

**求解**：

$$x^2 = x \iff x^2 - x = 0 \iff x(x - 1) = 0 \iff x = 0 \text{ 或 } x = 1.$$

满足条件的实数有 $x = 0$ 和 $x = 1$。

**真值**：该命题为**真**，因为确实存在这样的实数（两个：$0$ 和 $1$）。

---

**8.** 函数 $f$ 在 $x_0$ 处连续的 $\epsilon$-$\delta$ 形式化。

**形式化**（$f$ 在 $x_0$ 处连续）：

$$\forall \epsilon\, \Bigl(\epsilon > 0 \to \exists \delta\, \bigl(\delta > 0 \wedge \forall x\, (|x - x_0| < \delta \to |f(x) - f(x_0)| < \epsilon)\bigr)\Bigr)$$

**否定式**（$f$ 在 $x_0$ 处不连续）：

$$\exists \epsilon\, \Bigl(\epsilon > 0 \wedge \forall \delta\, \bigl(\delta > 0 \to \exists x\, (|x - x_0| < \delta \wedge |f(x) - f(x_0)| \geq \epsilon)\bigr)\Bigr)$$

推导过程：

$$\neg\bigl[\forall \epsilon > 0\, \exists \delta > 0\, \forall x\, (|x - x_0| < \delta \to |f(x) - f(x_0)| < \epsilon)\bigr]$$

$$\equiv \exists \epsilon > 0\, \neg\bigl[\exists \delta > 0\, \forall x\, (\cdots)\bigr]$$

$$\equiv \exists \epsilon > 0\, \forall \delta > 0\, \neg\bigl[\forall x\, (|x - x_0| < \delta \to |f(x) - f(x_0)| < \epsilon)\bigr]$$

$$\equiv \exists \epsilon > 0\, \forall \delta > 0\, \exists x\, \neg(|x - x_0| < \delta \to |f(x) - f(x_0)| < \epsilon)$$

$$\equiv \exists \epsilon > 0\, \forall \delta > 0\, \exists x\, (|x - x_0| < \delta \wedge |f(x) - f(x_0)| \geq \epsilon)$$

**自然语言翻译**：存在一个正数 $\epsilon$，使得无论 $\delta$ 取多小的正数，都能找到一个 $x$，它与 $x_0$ 的距离小于 $\delta$，但 $f(x)$ 与 $f(x_0)$ 的距离不小于 $\epsilon$。

直觉：$f$ 在 $x_0$ 处有一个"跳跃"或"振荡"——存在一个无法消除的误差。

---

**9.** 证明 $\forall x\, \forall y\, P(x, y) \equiv \forall y\, \forall x\, P(x, y)$。

**证明**：需要证明两个方向。

**方向一**：$\forall x\, \forall y\, P(x, y) \Rightarrow \forall y\, \forall x\, P(x, y)$。

假设 $\forall x\, \forall y\, P(x, y)$ 为真。要证 $\forall y\, \forall x\, P(x, y)$ 为真。

设 $b$ 和 $a$ 为论域中任意元素。需证 $P(a, b)$。

由 $\forall x\, \forall y\, P(x, y)$，对 $x$ 取 $a$，得 $\forall y\, P(a, y)$。

再对 $y$ 取 $b$，得 $P(a, b)$。

由于 $a, b$ 是任意的，故 $\forall y\, \forall x\, P(x, y)$ 为真。

**方向二**：$\forall y\, \forall x\, P(x, y) \Rightarrow \forall x\, \forall y\, P(x, y)$。

假设 $\forall y\, \forall x\, P(x, y)$ 为真。要证 $\forall x\, \forall y\, P(x, y)$ 为真。

设 $a$ 和 $b$ 为论域中任意元素。需证 $P(a, b)$。

由 $\forall y\, \forall x\, P(x, y)$，对 $y$ 取 $b$，得 $\forall x\, P(x, b)$。

再对 $x$ 取 $a$，得 $P(a, b)$。

由于 $a, b$ 是任意的，故 $\forall x\, \forall y\, P(x, y)$ 为真。

两个方向均成立，故 $\forall x\, \forall y\, P(x, y) \equiv \forall y\, \forall x\, P(x, y)$。$\blacksquare$

**注**：类似地，$\exists x\, \exists y\, P(x, y) \equiv \exists y\, \exists x\, P(x, y)$（同类量词可交换）。但 $\forall$ 与 $\exists$ 不能交换——正如第 6 题所示。

---

**10.** 构造谓词与论域。

**第一部分**：$\forall x\, P(x)$ 为假但 $\exists x\, P(x)$ 为真。

取论域 $D = \{1, 2, 3\}$，$P(x)$："$x$ 是偶数"。

- $P(1)$：假（$1$ 不是偶数）
- $P(2)$：真（$2$ 是偶数）
- $P(3)$：假

$\forall x\, P(x)$：假（$P(1)$ 为假）。$\exists x\, P(x)$：真（$P(2)$ 为真）。✓

**第二部分**：$\forall x\, Q(x)$ 和 $\exists x\, Q(x)$ 都为真。

取论域 $D = \{2, 4, 6\}$，$Q(x)$："$x$ 是偶数"。

- $Q(2)$：真，$Q(4)$：真，$Q(6)$：真

$\forall x\, Q(x)$：真。$\exists x\, Q(x)$：真。✓

（或者更简单地，取任何论域和恒真谓词 $Q(x) = \text{T}$。）

**$\forall$ 与 $\exists$ 的关系**：

从这些例子可以看出：

1. $\forall x\, P(x) \Rightarrow \exists x\, P(x)$（在非空论域上）：若所有元素都满足 $P$，则至少存在一个满足 $P$ 的元素。反向不成立。

2. $\forall$ 比 $\exists$ 更"强"：$\forall x\, P(x)$ 为真要求**每个**元素都满足 $P$；$\exists x\, P(x)$ 为真只需**一个**元素满足 $P$。

3. 二者通过否定联系：$\neg \forall x\, P(x) \equiv \exists x\, \neg P(x)$，$\neg \exists x\, P(x) \equiv \forall x\, \neg P(x)$。

4. 在非空论域中，$\forall x\, P(x)$ 蕴含 $\exists x\, P(x)$，但反之不然。这是因为"所有"蕴含"存在"，但"存在"不蕴含"所有"。
