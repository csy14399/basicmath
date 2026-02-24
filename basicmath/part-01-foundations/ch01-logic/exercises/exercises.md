# 第一章 逻辑 — 练习题

## §1 命题逻辑（Propositional Logic）

1. ★☆☆ 判断下列句子中哪些是命题（proposition），并说明理由。

   (a) $3 + 5 = 8$

   (b) 请关上门。

   (c) $x^2 + 1 > 0$

   (d) 你今天吃早饭了吗？

   (e) 这句话是假的。

   (f) 所有偶数都能被 $2$ 整除。

2. ★☆☆ 构造命题 $(p \wedge q) \to (\neg p \vee q)$ 的真值表（truth table），并判断它是重言式（tautology）、矛盾式（contradiction）还是可满足式（contingency）。

3. ★☆☆ 用真值表验证逻辑等价式（logical equivalence）：
   $$p \to q \equiv \neg p \vee q.$$

4. ★☆☆ 仅用逻辑等价律（logical equivalence laws）（不使用真值表），化简
   $$\neg(\neg p \wedge q).$$
   写出每一步所用的定律名称。

5. ★☆☆ 判断 $(p \to q) \wedge (q \to p)$ 是否逻辑等价于 $p \leftrightarrow q$。用真值表或等价律证明你的结论。

6. ★★☆ 证明 $\{\neg, \wedge\}$ 是功能完备集（functionally complete set），即任何真值函数都可以仅用 $\neg$ 和 $\wedge$ 表示。

   **提示**：只需说明 $\vee$ 和 $\to$ 可以由 $\neg$ 和 $\wedge$ 表示。

7. ★★☆ 仅使用 $\neg$、$\wedge$、$\vee$ 三个联结词，写出异或（exclusive or）$p \oplus q$ 的等价表达式，并用真值表验证。

8. ★★☆ 用逻辑等价律（不使用真值表）证明：
   $$(p \to q) \wedge (p \to r) \equiv p \to (q \wedge r).$$

9. ★★☆ 已知"$p \to q$ 为假"，确定 $p$ 和 $q$ 各自的真值，并解释原因。

10. ★★★ 证明或反驳：对任意命题 $p, q, r$，若 $p \to q$ 与 $q \to r$ 均为真，则 $p \to r$ 为真（假言三段论，hypothetical syllogism）。

11. ★★★ 一位逻辑学家来到一座小岛，岛上每个人要么是骑士（knight，永远说真话），要么是无赖（knave，永远说假话）。A 说："B 是骑士。"B 说："A 和我是不同类型的。"

    (a) 用命题变量形式化此问题。

    (b) 确定 A 和 B 各自的类型。

    (c) 给出严格的逻辑推理过程。

12. ★★★ 对于 $n$ 个命题变量，一张真值表需要多少行？请给出公式并说明原因。进而回答：为什么真值表方法在变量数较多时是不切实际的？

---

## §2 谓词逻辑（Predicate Logic）

1. ★☆☆ 将下列自然语言翻译为谓词逻辑表达式：

   "每个大于 $1$ 的整数要么是素数（prime），要么是合数（composite）。"

   明确指出你使用的论域（domain）、谓词（predicate）和量词（quantifier）。

2. ★☆☆ 在整数域 $\mathbb{Z}$ 上，写出
   $$\forall x\, \exists y\, (x + y = 0)$$
   的否定式，并判断原命题与否定式的真值。

3. ★☆☆ 在公式 $\forall x\, (P(x, y) \to \exists z\, Q(z))$ 中，指出哪些变量是自由变量（free variable），哪些是约束变量（bound variable）。

4. ★☆☆ 命题 $\forall x\, (x^2 \geq 0)$ 在 $\mathbb{R}$（实数域）上是否为真？在 $\mathbb{C}$（复数域）上是否有意义？请解释。

5. ★★☆ 将阿基米德性质（Archimedean property）用谓词逻辑形式化：

   "对每个正实数 $\epsilon$，都存在正整数 $N$ 使得 $1/N < \epsilon$。"

   然后写出其否定式，并将否定式翻译回自然语言。

6. ★★☆ 解释
   $$\forall x\, \exists y\, (x < y) \quad \text{与} \quad \exists y\, \forall x\, (x < y)$$
   的区别。分别在论域 $\mathbb{R}$（全体实数）和论域 $\{1, 2, 3\}$ 上讨论这两个命题的真值。

7. ★★☆ 翻译并判断真值："存在一个实数是其自身的平方。"

   用谓词逻辑表达，并找出所有满足条件的实数。

8. ★★★ 用 $\epsilon$-$\delta$ 语言将"函数 $f$ 在 $x_0$ 处连续（continuous）"形式化为谓词逻辑命题。然后写出该命题的否定式（即 $f$ 在 $x_0$ 处不连续的精确表述），并将否定式翻译回自然语言。

9. ★★★ 证明同类量词可交换：
   $$\forall x\, \forall y\, P(x, y) \equiv \forall y\, \forall x\, P(x, y).$$
   提示：分别证明两个方向的蕴含。

10. ★★★ 构造一个谓词 $P(x)$ 和论域 $D$，使得 $\forall x\, P(x)$ 为假但 $\exists x\, P(x)$ 为真；再构造一个谓词 $Q(x)$ 和论域，使得 $\forall x\, Q(x)$ 和 $\exists x\, Q(x)$ 都为真。从中你能得出 $\forall$ 与 $\exists$ 之间怎样的关系？
