# §2 谓词逻辑（Predicate Logic）

**前置知识**：[§1 命题逻辑](01-propositions.md)

**全景图**：命题逻辑只能处理"真或假"的整体命题，但数学中我们需要表达"对所有 $x$"和"存在某个 $x$"这样的结构。谓词逻辑（predicate logic），也称一阶逻辑（first-order logic），扩展了命题逻辑的表达能力，让我们能够讨论数学对象的性质和它们之间的关系。

**预估学习时间**：2–3 小时

---

## 动机

命题逻辑有一个根本的局限：它把每个命题视为不可分割的整体。考虑以下两个数学命题：

- "所有偶数都能被 2 整除。"
- "存在一个偶数大于 100。"

在命题逻辑中，我们只能把它们各自记为一个符号，比如 $p$ 和 $q$。但这两个命题的内部结构完全不同——第一个说的是"对所有满足某种性质的对象，另一种性质成立"，第二个说的是"存在一个满足某种性质的对象，使得另一种性质成立"。命题逻辑无法捕捉这种区别。

谓词逻辑通过引入两个关键概念来解决这个问题：

- **谓词（predicate）**：描述对象性质的模板，如"$x$ 是偶数"。
- **量词（quantifier）**：说明谓词对多少对象成立，如"对所有 $x$"或"存在某个 $x$"。

这两个概念将给予我们足够的表达力，来精确陈述数学中几乎所有的定理和定义。

---

## 1. 谓词（Predicate）

> **定义 1**（谓词，predicate）
>
> 谓词是一个含有一个或多个变量的陈述，当变量被赋予具体的值后，就变成一个命题。含一个变量的谓词记作 $P(x)$，含两个变量的记作 $P(x, y)$，以此类推。

**例子：**

- $P(x)$：" $x$ 是偶数"。这不是命题，因为 $x$ 的值未确定。但一旦给 $x$ 赋值，它就变成命题：
  - $P(4)$：" $4$ 是偶数"——真。
  - $P(7)$：" $7$ 是偶数"——假。

- $Q(x, y)$：" $x + y > 10$"。这是一个二元谓词。
  - $Q(3, 5)$：" $3 + 5 > 10$"，即 "$8 > 10$"——假。
  - $Q(6, 7)$：" $6 + 7 > 10$"，即 "$13 > 10$"——真。

- $R(x, y, z)$：" $x^2 + y^2 = z^2$"。这是一个三元谓词。
  - $R(3, 4, 5)$：" $9 + 16 = 25$"——真（勾股数）。
  - $R(1, 2, 3)$：" $1 + 4 = 9$"——假。

谓词本身不是命题——它有"空位"（变量）需要填充。我们可以通过两种方式把谓词变成命题：

1. **赋值**：给变量指定具体的值。如上面的 $P(4)$, $Q(3,5)$。
2. **量化**：用量词说明变量的取值范围和条件。这是下面要讨论的内容。

---

## 2. 论域（Domain of Discourse）

> **定义 2**（论域，domain of discourse / universe of discourse）
>
> 论域（也称全集）是变量可以取值的集合，通常记作 $U$ 或 $D$。量化的陈述总是相对于某个论域而言的。

论域的选择至关重要——同一个谓词在不同论域下可能有完全不同的真值。

**例子：**

考虑谓词 $P(x)$："$x^2 \geq 0$"。

- 论域 $U = \mathbb{R}$（所有实数）：$\forall x\, P(x)$ 为真——每个实数的平方都非负。
- 论域 $U = \mathbb{C}$（所有复数）：这个问题在复数域中没有直接意义，因为复数不像实数那样具有全序关系。

考虑谓词 $Q(x)$："$x + 1 > x$"。

- 论域 $U = \mathbb{R}$：$\forall x\, Q(x)$ 为真。
- 论域 $U = \{$所有基数$\}$：情况变得微妙（涉及无穷基数的算术）。

在使用量词时，必须明确论域，或者从上下文中可以明确推断论域。在本教材中，如果没有特别说明，默认论域通常是实数集 $\mathbb{R}$ 或自然数集 $\mathbb{N}$。

---

## 3. 全称量词（Universal Quantifier）

> **定义 3**（全称量词，universal quantifier）
>
> 设 $P(x)$ 是一个谓词，$U$ 是论域。**全称量化**（universal quantification）$\forall x\, P(x)$（读作"对所有 $x$，$P(x)$"）表示：对论域 $U$ 中的**每一个** $x$，$P(x)$ 都为真。

符号 $\forall$ 是倒写的字母 A，来自英文"for **A**ll"。

> **直觉**
>
> 想象论域中的所有元素排成一列。$\forall x\, P(x)$ 的意思是：你逐一检查每一个元素，每一个都满足 $P$。就像一个严格的质量检查员，检查流水线上的每一件产品——只有全部合格，才判定"所有产品合格"。

**判断 $\forall x\, P(x)$ 的真假：**

- **为真**：需要证明对论域中的**每一个** $x$，$P(x)$ 都成立。当论域是无穷集时，不能逐一检查，需要给出一个对任意 $x$ 都适用的论证。
- **为假**：只需找到**一个反例**（counterexample）——论域中某个 $x_0$ 使得 $P(x_0)$ 为假。

**例子：**

- $\forall x \in \mathbb{R}\, (x^2 \geq 0)$："对所有实数 $x$，$x^2 \geq 0$。"这为真。
- $\forall x \in \mathbb{R}\, (x^2 > 0)$："对所有实数 $x$，$x^2 > 0$。"这为假——反例：$x = 0$ 时 $x^2 = 0$，不大于 0。
- $\forall n \in \mathbb{N}\, (n + 1 > n)$："对所有自然数 $n$，$n + 1 > n$。"这为真。

**全称量词与合取的关系：**

当论域是有限集 $U = \{a_1, a_2, \ldots, a_n\}$ 时，$\forall x\, P(x)$ 等价于：

$$P(a_1) \wedge P(a_2) \wedge \cdots \wedge P(a_n)$$

即对每个元素都逐一检查并取合取。当论域是无穷集时，这种展开不可能完成，但直觉是一样的。

**全称量化与蕴含的标准组合：**

在实际使用中，全称量词通常与蕴含搭配，表达"所有满足条件 A 的对象都满足条件 B"：

$$\forall x\, (A(x) \to B(x))$$

例如，"所有偶数都能被 2 整除"：$\forall x\, (\text{Even}(x) \to 2 \mid x)$。

这里用蕴含而不是合取是关键：我们不要求论域中的每一个 $x$ 都是偶数，只对那些碰巧是偶数的 $x$ 做出断言。关于这个搭配模式，我们将在第 9 节"翻译"中详细讨论。

**关于证明和证伪的不对称性：**

全称命题的证明与证伪存在深刻的不对称性：

- **证伪**极其容易——一个反例足矣。例如，要证伪"所有质数都是奇数"，只需指出 $2$ 是偶数的质数。
- **证明**通常困难得多——需要对论域中的所有元素给出统一的论证。当论域是无穷集（如 $\mathbb{N}$、$\mathbb{R}$）时，你不可能逐一检查每个元素，必须给出一个对任意 $x$ 都成立的推理。

这种不对称性在数学研究中有深远的影响。一个数学猜想（如哥德巴赫猜想）可能经过数百年的验证都没有找到反例，但这并不构成证明。而只要找到一个反例，猜想就被推翻了。

---

## 4. 存在量词（Existential Quantifier）

> **定义 4**（存在量词，existential quantifier）
>
> 设 $P(x)$ 是一个谓词，$U$ 是论域。**存在量化**（existential quantification）$\exists x\, P(x)$（读作"存在 $x$，使得 $P(x)$"）表示：论域 $U$ 中**至少有一个** $x$，使得 $P(x)$ 为真。

符号 $\exists$ 是倒写（或反写）的字母 E，来自英文"there **E**xists"。

> **直觉**
>
> 还是想象论域中的所有元素。$\exists x\, P(x)$ 的意思是：你只需要找到**一个**满足条件的元素就够了。就像在一堆石头里找一块金子——你不需要检查每块石头，找到一块就行。

**判断 $\exists x\, P(x)$ 的真假：**

- **为真**：需要找到（或证明存在）一个 $x_0$（称为**见证者**，witness）使得 $P(x_0)$ 为真。
- **为假**：需要证明论域中**没有任何** $x$ 使得 $P(x)$ 为真，即需要证明 $\forall x\, \neg P(x)$。

**例子：**

- $\exists x \in \mathbb{R}\, (x^2 = 2)$："存在实数 $x$，使得 $x^2 = 2$。"这为真——见证者：$x = \sqrt{2}$。
- $\exists x \in \mathbb{Q}\, (x^2 = 2)$："存在有理数 $x$，使得 $x^2 = 2$。"这为假——$\sqrt{2}$ 是无理数。注意论域从 $\mathbb{R}$ 变成 $\mathbb{Q}$ 后，真值改变了。
- $\exists n \in \mathbb{N}\, (n > 1000000)$："存在自然数大于一百万。"这为真——见证者：$n = 1000001$（或任何更大的数）。

**存在量词与析取的关系：**

当论域是有限集 $U = \{a_1, a_2, \ldots, a_n\}$ 时，$\exists x\, P(x)$ 等价于：

$$P(a_1) \vee P(a_2) \vee \cdots \vee P(a_n)$$

即对每个元素逐一检查并取析取。

**存在性证明的两种策略：**

要证明 $\exists x\, P(x)$，有两种基本策略：

1. **构造性证明**（constructive proof）：直接给出一个具体的见证者 $x_0$，验证 $P(x_0)$ 为真。例如，证明"存在两个无理数 $a, b$ 使得 $a^b$ 是有理数"——取 $a = \sqrt{2}, b = 2$，则 $a^b = 2$。

2. **非构造性证明**（non-constructive proof）：证明满足条件的 $x$ 一定存在，但不一定指出具体是哪个。这类证明通常使用反证法——假设不存在这样的 $x$，然后推出矛盾。非构造性证明在数学中完全合法，但它不告诉你见证者具体是什么。

这两种策略各有优劣，我们将在 [第 3 章 证明方法](../ch03-proof-methods/README.md) 中深入讨论。

---

## 5. 唯一存在量词（Uniqueness Quantifier）

> **定义 5**（唯一存在量词，uniqueness quantifier）
>
> $\exists! x\, P(x)$（读作"存在唯一的 $x$，使得 $P(x)$"）表示：论域中**恰好有一个** $x$ 使得 $P(x)$ 为真。

唯一存在量词可以用 $\forall$ 和 $\exists$ 来定义：

$$\exists! x\, P(x) \equiv \exists x\, \big(P(x) \wedge \forall y\, (P(y) \to y = x)\big)$$

这个定义的含义是：存在某个 $x$ 满足 $P(x)$，**并且**任何满足 $P$ 的 $y$ 都必须等于这个 $x$。

等价地：

$$\exists! x\, P(x) \equiv \exists x\, P(x) \wedge \forall x\, \forall y\, ((P(x) \wedge P(y)) \to x = y)$$

这把"恰好一个"拆成两部分：**至少一个**（存在性）加上**至多一个**（唯一性）。

**例子：**

- $\exists! x \in \mathbb{R}\, (x + 3 = 5)$："存在唯一的实数 $x$ 使得 $x + 3 = 5$。"这为真——唯一的解是 $x = 2$。
- $\exists! x \in \mathbb{R}\, (x^2 = 4)$："存在唯一的实数 $x$ 使得 $x^2 = 4$。"这为假——有两个解 $x = 2$ 和 $x = -2$。存在性满足，但唯一性不满足。

---

## 6. 约束变量与自由变量（Bound and Free Variables）

> **定义 6**（约束变量与自由变量，bound and free variables）
>
> 在公式中，被量词作用的变量称为**约束变量**（bound variable），未被量词作用的变量称为**自由变量**（free variable）。

**例子：**

- 在 $\forall x\, (x + y > 0)$ 中，$x$ 是约束变量（被 $\forall$ 绑定），$y$ 是自由变量。
- 在 $\exists x\, (x > y) \wedge (z = 0)$ 中，$x$ 是约束变量，$y$ 和 $z$ 是自由变量。
- 在 $\forall x\, \exists y\, (x + y = 0)$ 中，$x$ 和 $y$ 都是约束变量，没有自由变量。

**关键规则**：含自由变量的公式**不是命题**——它的真假取决于自由变量取什么值。只有所有变量都被量词约束（或被赋予具体值）后，公式才成为命题。

约束变量的名字是可以替换的（就像求和号 $\sum$ 下面的指标变量）：$\forall x\, P(x)$ 和 $\forall y\, P(y)$ 表达的是同一个命题。但替换时要小心，不能与已有的变量名冲突。

---

## 7. 量词的否定（Negation of Quantifiers）

量词的否定规则是谓词逻辑中最重要的规则之一，它在数学证明中被反复使用。

> **定理 1**（量词否定律，negation of quantifiers / De Morgan's laws for quantifiers）
>
> $$\neg \forall x\, P(x) \equiv \exists x\, \neg P(x)$$
>
> $$\neg \exists x\, P(x) \equiv \forall x\, \neg P(x)$$

> **证明**
>
> 第一条：$\neg \forall x\, P(x)$ 的意思是"并非对所有 $x$ 都有 $P(x)$"，即"存在某个 $x$ 使得 $P(x)$ 不成立"，即 $\exists x\, \neg P(x)$。
>
> 第二条：$\neg \exists x\, P(x)$ 的意思是"不存在 $x$ 使得 $P(x)$"，即"对所有 $x$，$P(x)$ 都不成立"，即 $\forall x\, \neg P(x)$。$\blacksquare$

> **直觉**
>
> - "并非所有人都喜欢巧克力" $\equiv$ "存在一个人不喜欢巧克力"
> - "不存在完美的人" $\equiv$ "每个人都不完美"（即"所有人都有缺点"）
>
> 否定穿过量词时，$\forall$ 和 $\exists$ 互换，同时内部的谓词取否定。这与命题逻辑中 De Morgan 律的精神完全一致（$\neg$ 穿过 $\wedge$/$\vee$ 时互换），因为 $\forall$ 是"广义合取"，$\exists$ 是"广义析取"。

**多重量词的否定：**

对于多个量词的情况，否定逐层穿过每个量词，每次都翻转量词类型：

$$\neg \forall x\, \exists y\, P(x, y) \equiv \exists x\, \neg \exists y\, P(x, y) \equiv \exists x\, \forall y\, \neg P(x, y)$$

每遇到一个量词，就翻转一次（$\forall \leftrightarrow \exists$），最终对最内层的谓词取否定。

---

## 8. 多重量词（Nested Quantifiers）

数学中的许多重要命题涉及多个量词。理解多重量词的关键是：**量词的顺序很重要**。

### 8.1 量词顺序的影响

考虑论域 $U$ 为所有人的集合，谓词 $L(x, y)$："$x$ 爱 $y$"。

- $\forall x\, \exists y\, L(x, y)$："对每个人 $x$，都存在某个人 $y$，使得 $x$ 爱 $y$。"
  即：每个人都爱至少一个人。（不同的 $x$ 可以爱不同的 $y$。）

- $\exists y\, \forall x\, L(x, y)$："存在某个人 $y$，使得对每个人 $x$，$x$ 都爱 $y$。"
  即：存在一个人被所有人爱。（同一个 $y$ 被所有 $x$ 爱。）

这两个命题含义截然不同。第一个只要求每个人都有所爱（每个人爱的对象可以不同），第二个要求存在一个"万人迷"被所有人爱。第二个显然比第一个更强。

> ⚠️ **警告**
>
> 量词顺序不可交换！$\forall x\, \exists y\, P(x,y)$ 和 $\exists y\, \forall x\, P(x,y)$ 的含义完全不同。
>
> 一般规律：$\exists y\, \forall x\, P(x,y) \Rightarrow \forall x\, \exists y\, P(x,y)$（反方向不成立）。
>
> 即：如果存在一个 $y$ 对所有 $x$ 都满足 $P$，那么对每个 $x$ 自然可以找到某个 $y$（就用那个通用的 $y$）。但反过来，每个 $x$ 各自找到的 $y$ 可能不同，未必存在一个通用的。

再看一个数学化的例子：

- $\forall x \in \mathbb{R}\, \exists y \in \mathbb{R}\, (x + y = 0)$："对每个实数 $x$，都存在实数 $y$ 使得 $x + y = 0$。"这为真——取 $y = -x$ 即可。不同的 $x$ 对应不同的 $y$。

- $\exists y \in \mathbb{R}\, \forall x \in \mathbb{R}\, (x + y = 0)$："存在一个实数 $y$，使得对所有实数 $x$ 都有 $x + y = 0$。"这为假——不可能有一个 $y$ 同时让 $1 + y = 0$、$2 + y = 0$、$3 + y = 0$ 全部成立。

### 8.2 同类量词的交换

虽然不同类型的量词（$\forall$ 和 $\exists$）不能交换，但**同类量词可以交换**：

$$\forall x\, \forall y\, P(x, y) \equiv \forall y\, \forall x\, P(x, y)$$

$$\exists x\, \exists y\, P(x, y) \equiv \exists y\, \exists x\, P(x, y)$$

这是因为"所有 $x$ 和所有 $y$"与"所有 $y$ 和所有 $x$"没有区别。同理，"存在 $x$ 和存在 $y$"与"存在 $y$ 和存在 $x$"也没有区别。

### 8.3 更多量词顺序的数学例子

**例子 1**：论域为 $\mathbb{R}$，谓词 $P(x,y)$："$xy = 1$"。

- $\forall x\, \exists y\, (xy = 1)$："对每个实数 $x$，都存在实数 $y$ 使得 $xy = 1$。"
  这为**假**——当 $x = 0$ 时，不存在 $y$ 使得 $0 \cdot y = 1$。

- $\exists x\, \forall y\, (xy = 1)$："存在一个实数 $x$，使得对所有实数 $y$ 都有 $xy = 1$。"
  这也为**假**——不可能有一个 $x$ 同时让 $x \cdot 1 = 1$、$x \cdot 2 = 1$、$x \cdot 3 = 1$。

**例子 2**：论域为 $\mathbb{R}$，谓词 $P(x,y)$："$x \leq y$"。

- $\forall x\, \exists y\, (x \leq y)$："对每个实数 $x$，存在实数 $y$ 使得 $x \leq y$。"
  这为**真**——取 $y = x$ 即可（或 $y = x + 1$）。

- $\exists y\, \forall x\, (x \leq y)$："存在一个实数 $y$，使得所有实数 $x$ 都不超过 $y$。"
  这为**假**——实数集没有上界（没有最大的实数）。

这些例子清楚地展示了：$\forall x\, \exists y$ 中 $y$ 可以依赖于 $x$（每个 $x$ 找自己的 $y$），而 $\exists y\, \forall x$ 中 $y$ 必须独立于 $x$（一个 $y$ 应付所有 $x$）。

### 8.4 读解多重量词的方法

面对复杂的多重量词表达式，可以从外向内逐层读解：

$$\forall x\, \exists y\, \forall z\, P(x, y, z)$$

读作："对每一个 $x$（固定 $x$），都存在某个 $y$（$y$ 可以依赖于 $x$），使得对所有 $z$，$P(x, y, z)$ 成立。"

关键：每个量词引入一个变量，后面的量词所引入的变量**可以依赖于前面已经固定的变量**。$\exists y$ 中的 $y$ 可以是 $x$ 的函数；$\forall z$ 要求对所有 $z$ 都成立，$z$ 不依赖于 $x$ 或 $y$ 的选择。

---

## 9. 从日常语言到形式逻辑的翻译

将自然语言翻译为谓词逻辑是一项重要的技能。以下是系统化的翻译步骤。

### 9.1 翻译步骤

1. **确定论域**：变量的取值范围是什么？
2. **确定谓词**：句子涉及哪些性质和关系？用符号表示它们。
3. **确定量词**：句子中有"所有"、"每一个"、"任意"（→ $\forall$）还是"存在"、"某个"、"至少一个"（→ $\exists$）？
4. **确定逻辑结构**：量词之间和谓词之间用什么联结词连接？
5. **注意隐含量词**：日常语言中的量词常常是隐含的。"人是会犯错的"意思是"所有人都会犯错"。

### 9.2 翻译中的关键模式

**"所有 A 都是 B"** 的标准翻译：

$$\forall x\, (A(x) \to B(x))$$

注意用的是**蕴含** $\to$，不是合取 $\wedge$。因为我们只关心那些满足 $A$ 的对象——对于不满足 $A$ 的对象，我们不做任何断言。

错误翻译 $\forall x\, (A(x) \wedge B(x))$ 的意思是"所有 $x$ 既是 $A$ 又是 $B$"——这太强了。例如，"所有狗都是哺乳动物"应译为 $\forall x\, (\text{Dog}(x) \to \text{Mammal}(x))$，而不是 $\forall x\, (\text{Dog}(x) \wedge \text{Mammal}(x))$（后者说的是"一切事物都是狗并且是哺乳动物"）。

**"存在一个 A 是 B"** 的标准翻译：

$$\exists x\, (A(x) \wedge B(x))$$

注意用的是**合取** $\wedge$，不是蕴含 $\to$。因为我们要找一个**同时**满足 $A$ 和 $B$ 的对象。

错误翻译 $\exists x\, (A(x) \to B(x))$ 几乎总是真的——只要存在一个不满足 $A$ 的对象即可（空真）。例如，"存在一只会飞的猪"不应译为 $\exists x\, (\text{Pig}(x) \to \text{Fly}(x))$（这个命题为真，因为任何非猪的对象都使蕴含为真），而应译为 $\exists x\, (\text{Pig}(x) \wedge \text{Fly}(x))$。

> ⚠️ **警告**
>
> 翻译模式的经验法则：
> - **$\forall$ 搭配 $\to$**："所有 A 都是 B" → $\forall x\, (A(x) \to B(x))$
> - **$\exists$ 搭配 $\wedge$**："存在 A 是 B" → $\exists x\, (A(x) \wedge B(x))$
>
> 搭配反了几乎一定是错误的。

### 9.3 翻译练习

**例 1**："每个学生都通过了考试。"

论域 $U$：所有人。谓词：$S(x)$——"$x$ 是学生"，$P(x)$——"$x$ 通过了考试"。

$$\forall x\, (S(x) \to P(x))$$

**例 2**："有些学生没有通过考试。"

$$\exists x\, (S(x) \wedge \neg P(x))$$

注意：这恰好是例 1 的否定。$\neg \forall x\, (S(x) \to P(x)) \equiv \exists x\, \neg(S(x) \to P(x)) \equiv \exists x\, (S(x) \wedge \neg P(x))$。最后一步用了 [§1](01-propositions.md) 中的等价律 $\neg(p \to q) \equiv p \wedge \neg q$。

**例 3**："如果一个数是质数且大于 2，则它是奇数。"

论域 $U = \mathbb{N}$。谓词：$\text{Prime}(x)$，$\text{Odd}(x)$。

$$\forall x\, ((\text{Prime}(x) \wedge x > 2) \to \text{Odd}(x))$$

**例 4**："没有最大的自然数。"

论域 $U = \mathbb{N}$。

$$\neg \exists x\, \forall y\, (x \geq y)$$

等价地（应用量词否定律）：

$$\forall x\, \exists y\, (y > x)$$

"对每个自然数 $x$，都存在更大的自然数 $y$。"

**例 5**："每个正整数要么是质数，要么可以写成质数的乘积。"

论域 $U = \{n \in \mathbb{Z} : n > 1\}$。

$$\forall n\, (\text{Prime}(n) \vee \exists p_1 \exists p_2 \ldots \exists p_k\, (\text{Prime}(p_1) \wedge \cdots \wedge \text{Prime}(p_k) \wedge n = p_1 \cdot p_2 \cdots p_k))$$

这就是**算术基本定理**（Fundamental Theorem of Arithmetic）的存在性部分的形式化。（完整的算术基本定理还包括分解的唯一性。）

严格的形式化需要处理"有限个质数的乘积"这一概念，在纯一阶逻辑中这需要一些技巧。在实际数学写作中，我们通常用自然语言辅助形式化。

**例 6**："任何两个不同的实数之间都有一个有理数。"

论域 $U = \mathbb{R}$。

$$\forall x \in \mathbb{R}\, \forall y \in \mathbb{R}\, (x < y \to \exists q \in \mathbb{Q}\, (x < q < y))$$

这是有理数在实数中的**稠密性**（density of rationals in reals）。

### 9.4 翻译中的常见陷阱

**陷阱 1：隐含量词。** "整数的平方是非负的"——这里隐含了一个全称量词："**所有**整数的平方是非负的"，即 $\forall n \in \mathbb{Z}\, (n^2 \geq 0)$。

**陷阱 2："只有"和"仅当"。** "只有努力学习才能通过考试"——这**不**等于"如果努力学习就能通过考试"。"只有 $A$ 才 $B$"的意思是"$B \to A$"（$A$ 是 $B$ 的必要条件），而不是"$A \to B$"。

**陷阱 3：嵌套条件。** "如果一个数是质数且大于 2，那么它是奇数"中，前件本身是一个合取命题。翻译时需要准确识别前件和后件的边界。

---

## 10. 例题

> **例题 1**
>
> 将"每个偶数都是两个质数之和"（哥德巴赫猜想）翻译为谓词逻辑。
>
> **解**：
>
> 论域 $U = \mathbb{Z}$（整数）。
>
> 定义谓词：
> - $E(x)$："$x$ 是偶数"，即 $\exists k \in \mathbb{Z}\, (x = 2k)$
> - $\text{Prime}(x)$："$x$ 是质数"
>
> 哥德巴赫猜想更精确的表述是"每个大于 2 的偶数都是两个质数之和"：
>
> $$\forall n\, ((E(n) \wedge n > 2) \to \exists p\, \exists q\, (\text{Prime}(p) \wedge \text{Prime}(q) \wedge n = p + q))$$
>
> 读作：对每个整数 $n$，如果 $n$ 是偶数且大于 2，则存在质数 $p$ 和质数 $q$ 使得 $n = p + q$。
>
> 这个猜想至今（2026 年）未被证明。

> **例题 2**
>
> 否定极限定义：$\forall \epsilon > 0\, \exists N \in \mathbb{N}\, \forall n > N\, |a_n - L| < \epsilon$。
>
> **解**：
>
> 这个公式是数列极限（limit of a sequence）的 $\epsilon$-$N$ 定义：数列 $\{a_n\}$ 的极限是 $L$，意思是"对任意正数 $\epsilon$（无论多小），都存在自然数 $N$，使得当 $n > N$ 时，$a_n$ 与 $L$ 的距离小于 $\epsilon$"。
>
> 逐层否定：
>
> $$\neg \forall \epsilon > 0\, \exists N \in \mathbb{N}\, \forall n > N\, (|a_n - L| < \epsilon)$$
>
> 第一层：$\neg \forall$ 变成 $\exists$：
>
> $$\exists \epsilon > 0\, \neg \exists N \in \mathbb{N}\, \forall n > N\, (|a_n - L| < \epsilon)$$
>
> 第二层：$\neg \exists$ 变成 $\forall$：
>
> $$\exists \epsilon > 0\, \forall N \in \mathbb{N}\, \neg \forall n > N\, (|a_n - L| < \epsilon)$$
>
> 第三层：$\neg \forall$ 变成 $\exists$，内部谓词取否定：
>
> $$\exists \epsilon > 0\, \forall N \in \mathbb{N}\, \exists n > N\, (|a_n - L| \geq \epsilon)$$
>
> 最终结果的含义："存在某个正数 $\epsilon_0$，使得无论 $N$ 多大，都能找到某个 $n > N$，使得 $a_n$ 与 $L$ 的距离不小于 $\epsilon_0$。"
>
> 换句话说，数列中总有些项"跑不进去"以 $L$ 为中心、$\epsilon_0$ 为半径的区间——数列不收敛到 $L$。
>
> 这个例题展示了量词否定在分析学（analysis）中的核心作用。我们将在 [Part 6 分析预备](../../part-06-analysis-prep/README.md) 中正式学习极限的定义。

> **例题 3**
>
> 证明 $\forall x\, \exists y\, (x < y)$ 在论域 $\mathbb{N}$（自然数集）上为真。
>
> **解**：
>
> 要证明"对每个自然数 $x$，都存在自然数 $y$ 使得 $x < y$"。
>
> > **证明**
> >
> > 设 $x$ 是任意自然数。令 $y = x + 1$。则 $y \in \mathbb{N}$（自然数对加法封闭），且 $x < x + 1 = y$。因此对任意 $x \in \mathbb{N}$，我们找到了 $y = x + 1 \in \mathbb{N}$ 使得 $x < y$。$\blacksquare$
>
> 注意证明的结构：
> 1. "设 $x$ 是任意自然数"——处理 $\forall x$ 的标准方式：取任意的 $x$。
> 2. "令 $y = x + 1$"——处理 $\exists y$ 的标准方式：给出一个具体的见证者。
> 3. 验证见证者满足条件。

> **例题 4**
>
> 否定命题"对每个 $\epsilon > 0$，存在 $\delta > 0$，使得当 $|x - a| < \delta$ 时 $|f(x) - f(a)| < \epsilon$"。
>
> **解**：
>
> 这是函数在一点 $a$ 处连续性的 $\epsilon$-$\delta$ 定义。形式化为：
>
> $$\forall \epsilon > 0\, \exists \delta > 0\, \forall x\, (|x - a| < \delta \to |f(x) - f(a)| < \epsilon)$$
>
> 逐层否定：
>
> $$\neg \forall \epsilon > 0\, \exists \delta > 0\, \forall x\, (|x - a| < \delta \to |f(x) - f(a)| < \epsilon)$$
>
> 第一层（$\neg\forall \to \exists$）：
>
> $$\exists \epsilon > 0\, \neg \exists \delta > 0\, \forall x\, (|x - a| < \delta \to |f(x) - f(a)| < \epsilon)$$
>
> 第二层（$\neg\exists \to \forall$）：
>
> $$\exists \epsilon > 0\, \forall \delta > 0\, \neg \forall x\, (|x - a| < \delta \to |f(x) - f(a)| < \epsilon)$$
>
> 第三层（$\neg\forall \to \exists$，并对内部蕴含取否定）：
>
> $$\exists \epsilon > 0\, \forall \delta > 0\, \exists x\, \neg(|x - a| < \delta \to |f(x) - f(a)| < \epsilon)$$
>
> 由 [§1](01-propositions.md) 中的等价律 $\neg(p \to q) \equiv p \wedge \neg q$：
>
> $$\exists \epsilon > 0\, \forall \delta > 0\, \exists x\, (|x - a| < \delta \wedge |f(x) - f(a)| \geq \epsilon)$$
>
> 最终含义："存在某个正数 $\epsilon_0$，无论 $\delta$ 多小，都能找到一个 $x$，虽然 $x$ 离 $a$ 很近（$|x - a| < \delta$），但 $f(x)$ 离 $f(a)$ 仍然不够近（$|f(x) - f(a)| \geq \epsilon_0$）。"这就是"$f$ 在 $a$ 处不连续"的精确定义。
>
> 这个例题再次展示了谓词逻辑在分析学中的核心地位。

> **例题 5**
>
> 判断以下命题在论域 $\mathbb{Z}$（整数）上的真假：$\forall x\, \forall y\, (x < y \to \exists z\, (x < z < y))$。
>
> **解**：
>
> 这个命题说的是"任意两个整数之间都有第三个整数"。这为**假**：取 $x = 0, y = 1$，则不存在整数 $z$ 满足 $0 < z < 1$。
>
> 但如果把论域换成 $\mathbb{Q}$（有理数）或 $\mathbb{R}$（实数），则这个命题为真——取 $z = \frac{x+y}{2}$ 即可。这再次说明了论域的重要性。

---

> **联系** → [证明方法（Ch03）](../ch03-proof-methods/README.md)
>
> 谓词逻辑的量词否定将在证明方法中频繁使用：
> - **反证法**：要证明 $\forall x\, P(x)$，假设其否定 $\exists x\, \neg P(x)$，然后推出矛盾。
> - **反例证明**：要证明 $\forall x\, P(x)$ 为假，只需找到一个 $x_0$ 使得 $\neg P(x_0)$。

> **联系** → [分析预备（Part 6）](../../part-06-analysis-prep/README.md)
>
> 极限的 $\epsilon$-$\delta$ 定义和 $\epsilon$-$N$ 定义是谓词逻辑的直接应用。理解多重量词和量词否定是学习分析学的先决条件。

---

> **历史**
>
> 谓词逻辑的诞生归功于 **Gottlob Frege**（弗雷格，1848–1925）。他在 1879 年发表的《概念文字》（*Begriffsschrift*，意为"概念的书写"）中首次引入了量词和谓词的形式化体系，将亚里士多德以来两千多年的逻辑学推进到了一个全新的高度。
>
> Frege 的动机是要为数学提供一个绝对严格的逻辑基础。他的工作后来启发了 **Bertrand Russell**（罗素）和 **Alfred North Whitehead**（怀特海），他们在 1910–1913 年出版的巨著《数学原理》（*Principia Mathematica*）中试图从逻辑出发推导出全部数学。虽然这个"逻辑主义"纲领最终未能完全实现（哥德尔不完备定理给出了根本性的限制），但它奠定了现代数理逻辑的基础。
>
> 今天，谓词逻辑（更确切地说，一阶逻辑）是数学、计算机科学和哲学的通用语言。数据库查询语言 SQL 的 WHERE 子句本质上就是谓词逻辑的应用；程序验证中的前置条件和后置条件也是谓词逻辑的体现。

---

## 要点回顾

1. **谓词**是含变量的陈述，赋值或量化后变成命题。
2. **论域**决定变量的取值范围，同一谓词在不同论域下可能有不同的真值。
3. **全称量词** $\forall x\, P(x)$：对论域中的每一个 $x$，$P(x)$ 都为真。证伪只需一个反例。
4. **存在量词** $\exists x\, P(x)$：论域中至少有一个 $x$ 使得 $P(x)$ 为真。证明需要一个见证者。
5. **量词否定律**：$\neg \forall \equiv \exists \neg$，$\neg \exists \equiv \forall \neg$。否定穿过量词时翻转量词类型。
6. **量词顺序不可交换**：$\forall x\, \exists y$ 和 $\exists y\, \forall x$ 含义不同。
7. **翻译模式**：$\forall$ 搭配 $\to$，$\exists$ 搭配 $\wedge$。

---

## 进度检查点

- ☐ 我能区分谓词和命题
- ☐ 我能正确使用全称量词和存在量词
- ☐ 我能否定含量词的命题（逐层翻转量词类型）
- ☐ 我理解量词顺序的重要性，能区分 $\forall x\, \exists y$ 和 $\exists y\, \forall x$
- ☐ 我能将自然语言的数学陈述翻译为谓词逻辑公式

---

### 自测题

1. 将"存在一个自然数同时是偶数和质数"翻译为谓词逻辑，并判断其真假。

2. 否定以下命题：$\forall x \in \mathbb{R}\, \exists y \in \mathbb{R}\, (x + y = 0)$。

3. 判断真假：$\exists y \in \mathbb{R}\, \forall x \in \mathbb{R}\, (x + y = 0)$。解释为什么它与自测题 2 中原命题的真假不同。

4. 将"没有最小的正实数"翻译为谓词逻辑。

5. 以下翻译是否正确？"有些鸟不会飞"翻译为 $\exists x\, (\text{Bird}(x) \to \neg\text{Fly}(x))$。如果不正确，给出正确翻译并解释错误原因。

<details>
<summary>查看答案</summary>

1. $\exists n \in \mathbb{N}\, (E(n) \wedge \text{Prime}(n))$，其中 $E(n)$ 表示"$n$ 是偶数"。真值为**真**——见证者：$n = 2$，它是唯一的偶质数。

2. 逐层否定：
   $$\neg \forall x \in \mathbb{R}\, \exists y \in \mathbb{R}\, (x + y = 0)$$
   $$\equiv \exists x \in \mathbb{R}\, \neg \exists y \in \mathbb{R}\, (x + y = 0)$$
   $$\equiv \exists x \in \mathbb{R}\, \forall y \in \mathbb{R}\, (x + y \neq 0)$$
   含义："存在一个实数 $x$，使得无论 $y$ 取什么实数值，$x + y$ 都不等于 0。"这为假（因为对任何 $x$，取 $y = -x$ 即可使 $x + y = 0$），所以原命题为真。

3. **假。** $\exists y \in \mathbb{R}\, \forall x \in \mathbb{R}\, (x + y = 0)$ 要求存在一个**固定的** $y$ 使得对**所有** $x$ 都有 $x + y = 0$。但不同的 $x$ 需要不同的 $y$（$y = -x$），不可能用一个 $y$ 同时满足所有 $x$。自测题 2 中的原命题 $\forall x\, \exists y\, (x + y = 0)$ 为真，因为每个 $x$ 可以各自选择自己的 $y = -x$。这正是"量词顺序不可交换"的例证。

4. $\neg \exists x \in \mathbb{R}^+\, \forall y \in \mathbb{R}^+\, (x \leq y)$，等价地：$\forall x \in \mathbb{R}^+\, \exists y \in \mathbb{R}^+\, (y < x)$。后者读作："对每个正实数 $x$，都存在更小的正实数 $y$。"这为真——取 $y = x/2$ 即可。

5. **不正确。** $\exists x\, (\text{Bird}(x) \to \neg\text{Fly}(x))$ 是错误的翻译。这个公式几乎总是真的：只要存在一个不是鸟的东西 $x_0$，则 $\text{Bird}(x_0)$ 为假，蕴含空真地为真。正确翻译应该是 $\exists x\, (\text{Bird}(x) \wedge \neg\text{Fly}(x))$——"存在某个 $x$，$x$ 是鸟**并且** $x$ 不会飞"。这遵循"$\exists$ 搭配 $\wedge$"的翻译模式。

</details>

---

**习题引用**：→ 本节习题见 [exercises/exercises.md](exercises/exercises.md#§2-谓词逻辑)
