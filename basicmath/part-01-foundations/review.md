# Part 1 综合回顾 (Comprehensive Review)

> **基础三角：逻辑 (Logic) · 集合 (Sets) · 证明 (Proofs)**

本回顾将 Part 1 的三章内容——命题与谓词逻辑、集合论、证明方法——整合为一个统一的图景，帮助读者看清它们之间的深层联系。

---

## 1. 逻辑→集合→证明的统一图景

数学的基础可以用一句话概括：

$$\text{逻辑是语言，集合是对象，证明是方法。}$$

三者协同工作，构成了整个数学大厦的地基。

### 1.1 逻辑提供精确的推理规则

逻辑是数学的"语法"。没有逻辑，数学语句就无法被精确表达，推理也无法被严格验证。

**命题逻辑 (Propositional Logic)** 提供了五个基本联结词 (connectives)：

| 联结词 | 符号 | 含义 |
|--------|------|------|
| 否定 (Negation) | $\neg P$ | "非 $P$" |
| 合取 (Conjunction) | $P \land Q$ | "$P$ 且 $Q$" |
| 析取 (Disjunction) | $P \lor Q$ | "$P$ 或 $Q$" |
| 蕴含 (Implication) | $P \to Q$ | "若 $P$ 则 $Q$" |
| 双条件 (Biconditional) | $P \leftrightarrow Q$ | "$P$ 当且仅当 $Q$" |

这些联结词让我们可以从简单命题构建复合命题，并用真值表 (truth table) 精确判定其真假。

**谓词逻辑 (Predicate Logic)** 在此基础上增加了量词 (quantifiers)：

- 全称量词 (Universal Quantifier)：$\forall x,\, P(x)$ —— "对所有 $x$，$P(x)$ 成立"
- 存在量词 (Existential Quantifier)：$\exists x,\, P(x)$ —— "存在某个 $x$，使得 $P(x)$ 成立"

量词使我们能够对无穷多对象做出断言，这正是数学区别于日常推理之处。

### 1.2 集合论用逻辑的语言定义数学对象

集合论 (Set Theory) 是数学对象的"容器"。几乎一切数学概念——数、函数、空间——都可以用集合来定义。

集合的构造依赖于逻辑：集合构造符号 (set-builder notation) $\{x \mid P(x)\}$ 的含义就是"满足谓词 $P(x)$ 的所有 $x$ 的集合"。逻辑谓词决定了哪些元素属于集合、哪些不属于。

在集合论的框架内，我们定义了：

- **关系 (Relations)**：$R \subseteq A \times B$，即笛卡尔积 (Cartesian product) 的子集
- **等价关系 (Equivalence Relations)**：满足自反性 (reflexive)、对称性 (symmetric)、传递性 (transitive) 的关系
- **函数 (Functions)**：满足"每个输入恰好一个输出"条件的特殊关系
- **基数 (Cardinality)**：通过双射 (bijection) 比较集合的大小

### 1.3 证明方法提供从假设到结论的具体路径

证明是数学的"动词"——是我们确立命题为真的过程。每种证明方法都有其逻辑基础：

| 证明方法 | 逻辑基础 | 适用场景 |
|----------|----------|----------|
| 直接证明 (Direct Proof) | $P \to Q$：假设 $P$，推出 $Q$ | 结论的形式比较直接 |
| 反证法 (Proof by Contradiction) | $\neg Q \to \bot$，因此 $Q$ | 正面难以着手，或结论涉及"不存在" |
| 逆否证明 (Contrapositive) | $\neg Q \to \neg P$ 等价于 $P \to Q$ | 结论的否定比结论本身更容易处理 |
| 数学归纳法 (Mathematical Induction) | 良序原理 (Well-Ordering Principle) | 命题涉及自然数或递归结构 |
| 分情况讨论 (Proof by Cases) | $(P_1 \lor P_2) \to Q$ 等价于 $(P_1 \to Q) \land (P_2 \to Q)$ | 条件自然分为若干互斥情况 |
| 构造性证明 (Constructive Proof) | 显式给出 $\exists x,\, P(x)$ 中的 $x$ | 证明"存在"型命题 |

---

## 2. 关键联系总结

### 2.1 集合运算 ↔ 逻辑联结词

这是 Part 1 中最重要的对应之一。设全集 $U$ 上的子集 $A = \{x \in U \mid P(x)\}$，$B = \{x \in U \mid Q(x)\}$，则：

$$A \cup B = \{x \in U \mid P(x) \lor Q(x)\} \qquad (\text{并} \leftrightarrow \text{析取})$$

$$A \cap B = \{x \in U \mid P(x) \land Q(x)\} \qquad (\text{交} \leftrightarrow \text{合取})$$

$$A^c = \{x \in U \mid \neg P(x)\} \qquad (\text{补} \leftrightarrow \text{否定})$$

这一对应不仅是形式上的相似，更意味着：集合论的定理可以从逻辑的定理自动"翻译"而来。例如，De Morgan 律的逻辑版本

$$\neg(P \land Q) \equiv \neg P \lor \neg Q$$

直接翻译为集合版本

$$(A \cap B)^c = A^c \cup B^c.$$

### 2.2 证明中如何使用逻辑

每个证明都有"假设→推理→结论"的结构，这正是蕴含 $P \to Q$ 的体现：

1. **假设 (Hypothesis)**：明确前提 $P$，这是推理的起点
2. **推理 (Reasoning)**：运用已知定理、定义和逻辑规则，构成推理链
3. **结论 (Conclusion)**：到达 $Q$，证明完成

形式上，一个证明就是构造了一个从 $P$ 到 $Q$ 的有效推理序列 (valid argument)。

### 2.3 反证法的逻辑基础

反证法 (Proof by Contradiction) 的核心是：

$$(\neg Q \to \bot) \implies Q$$

即：假设 $Q$ 为假，若能推出矛盾 $\bot$（即同时推出某个命题 $R$ 和 $\neg R$），则 $Q$ 必为真。

这一方法的有效性源于**排中律 (Law of Excluded Middle)**：对任何命题 $Q$，$Q \lor \neg Q$ 必成立。既然 $\neg Q$ 导致矛盾，就只剩 $Q$ 为真。

经典应用：$\sqrt{2}$ 的无理性证明——假设 $\sqrt{2} = p/q$（最简分数），推出 $p$ 和 $q$ 都是偶数，与"最简"矛盾。

### 2.4 归纳法为什么对自然数有效

数学归纳法 (Mathematical Induction) 的有效性源于自然数的**良序原理 (Well-Ordering Principle)**：

> 自然数 $\mathbb{N}$ 的每个非空子集都有最小元素。

归纳法等价于良序原理（可以互推）。其核心逻辑是：

$$\bigl[P(0) \land \forall k\,(P(k) \to P(k+1))\bigr] \implies \forall n\, P(n)$$

如果 $P(n)$ 不是对所有 $n$ 成立，则 $\{n \in \mathbb{N} \mid \neg P(n)\}$ 非空，由良序原理取其最小元素 $m$。由于 $P(0)$ 成立，$m \geq 1$，故 $P(m-1)$ 成立，但由归纳步骤 $P(m-1) \to P(m)$，得 $P(m)$ 也成立，矛盾。

---

## 3. 核心工具清单

以下工具将在后续所有部分中反复使用：

### 3.1 De Morgan 律（逻辑版和集合版）

**逻辑版 (Logical Form)：**

$$\neg(P \land Q) \equiv \neg P \lor \neg Q$$
$$\neg(P \lor Q) \equiv \neg P \land \neg Q$$

**集合版 (Set-Theoretic Form)：**

$$(A \cap B)^c = A^c \cup B^c$$
$$(A \cup B)^c = A^c \cap B^c$$

这两个版本本质上是同一个定理在不同语境中的体现。

### 3.2 量词否定规则

$$\neg \forall x\, P(x) \equiv \exists x\, \neg P(x)$$
$$\neg \exists x\, P(x) \equiv \forall x\, \neg P(x)$$

在证明中，否定一个全称命题等价于找到一个反例；否定一个存在命题等价于证明对所有对象都不满足。

### 3.3 等价关系与划分

等价关系 $\sim$ 将集合 $A$ 划分 (partition) 为互不相交的等价类 (equivalence classes)：

$$A = \bigsqcup_{[a] \in A/{\sim}} [a]$$

其中 $[a] = \{x \in A \mid x \sim a\}$。反过来，任何划分都定义一个等价关系。这一"等价关系↔划分"的双向对应是后续构造商集 (quotient set) 的基础。

### 3.4 函数的单射/满射/双射

设 $f: A \to B$：

- **单射 (Injection)**：$\forall a_1, a_2 \in A,\, f(a_1) = f(a_2) \implies a_1 = a_2$
- **满射 (Surjection)**：$\forall b \in B,\, \exists a \in A,\, f(a) = b$
- **双射 (Bijection)**：既单射又满射，即 $f$ 建立了 $A$ 与 $B$ 之间的一一对应

双射是比较集合大小（基数）的核心工具：$|A| = |B|$ 当且仅当存在 $A$ 到 $B$ 的双射。

### 3.5 证明方法的使用判断

| 要证明的命题形式 | 推荐方法 |
|------------------|----------|
| $P \to Q$（$Q$ 的形式直接） | 直接证明 |
| $P \to Q$（$\neg Q$ 更容易利用） | 逆否证明 |
| "$x$ 不存在"或"$x$ 是无理数" | 反证法 |
| $\exists x,\, P(x)$ | 构造性证明 |
| $\forall n \in \mathbb{N},\, P(n)$ | 数学归纳法 |
| 条件自然分为几种情况 | 分情况讨论 |

---

## 暂认/兑现状态 (IOUs)

Part 1 中无 **[暂认]** 项。

作为整本教材的起始部分，Part 1 建立的是最基本的逻辑和集合论框架。这里使用的所有概念（联结词、量词、集合运算、证明规则）都在本部分内完整定义和验证，不需要先用后证。

---

## 展望 (Looking Ahead)

Part 2（数系构建）将使用这里建立的全部工具：

- **逻辑** 用于精确陈述数的性质和运算公理
- **集合论** 用于构造数系：
  - 自然数 $\mathbb{N}$（Peano 公理）
  - 整数 $\mathbb{Z}$（通过等价关系从 $\mathbb{N} \times \mathbb{N}$ 构造）
  - 有理数 $\mathbb{Q}$（通过等价关系从 $\mathbb{Z} \times \mathbb{Z}^*$ 构造）
  - 实数 $\mathbb{R}$（Dedekind 分割或 Cauchy 列）
  - 复数 $\mathbb{C}$（$\mathbb{R}^2$ 上定义新运算）
- **证明方法** 用于证明数系的性质：
  - 归纳法证明自然数的基本定理
  - 反证法证明 $\sqrt{2} \notin \mathbb{Q}$
  - 构造性证明建立各数系之间的嵌入映射

Part 1 的三大支柱——逻辑、集合、证明——将贯穿整本教材的始终。
