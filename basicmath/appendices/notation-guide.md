# 附录 A：记号约定说明（Notation Guide）

数学记号是数学的书写系统。不同的教材、不同的国家、不同的数学传统，对同一个概念可能使用不同的符号。本附录列出本书中使用的全部记号约定，并指出它们与其他常见体系（特别是中国高中教材和 ISO 标准）的差异。

---

## A.1 集合记号（Set Notation）

| 记号 | 含义 | 说明 |
|------|------|------|
| $\in$ | 属于（element of） | $x \in A$ 表示 $x$ 是集合 $A$ 的元素 |
| $\notin$ | 不属于（not an element of） | $x \notin A$ 表示 $x$ 不是集合 $A$ 的元素 |
| $\subseteq$ | 子集（subset or equal） | $A \subseteq B$ 表示 $A$ 的每个元素都在 $B$ 中，允许 $A = B$ |
| $\subsetneq$ | 真子集（proper subset） | $A \subsetneq B$ 表示 $A \subseteq B$ 且 $A \neq B$ |
| $\cup$ | 并集（union） | $A \cup B = \{x : x \in A \text{ 或 } x \in B\}$ |
| $\cap$ | 交集（intersection） | $A \cap B = \{x : x \in A \text{ 且 } x \in B\}$ |
| $\setminus$ | 差集（set difference） | $A \setminus B = \{x : x \in A \text{ 且 } x \notin B\}$ |
| $\emptyset$ | 空集（empty set） | 不含任何元素的集合，也写作 $\{\}$ |
| $\mathcal{P}(A)$ | 幂集（power set） | $A$ 的所有子集构成的集合 |
| $A^c$ 或 $\overline{A}$ | 补集（complement） | 相对于全集 $U$ 的补集：$A^c = U \setminus A$ |
| $A \times B$ | 笛卡尔积（Cartesian product） | 所有有序对 $(a, b)$ 的集合，其中 $a \in A$, $b \in B$ |
| $A \triangle B$ | 对称差（symmetric difference） | $A \triangle B = (A \setminus B) \cup (B \setminus A)$ |
| $\{x : P(x)\}$ | 集合构造（set-builder） | 满足性质 $P(x)$ 的所有 $x$ 构成的集合，也写作 $\{x \mid P(x)\}$ |
| $|A|$ 或 $\#A$ | 基数/元素个数（cardinality） | 集合 $A$ 的元素个数（有限集）或基数（无限集） |

**约定**：本书使用 $\subseteq$ 表示"子集（含相等）"，$\subsetneq$ 表示"真子集"。这与 Bourbaki 传统一致。注意部分教材使用 $\subset$ 表示真子集，另一些教材用 $\subset$ 表示（可能相等的）子集——这种歧义是数学记号中最常见的混淆之一。本书避免单独使用 $\subset$，以杜绝歧义。

---

## A.2 数集记号（Number Set Notation）

| 记号 | 名称 | 定义 |
|------|------|------|
| $\mathbb{N}$ | 自然数集（natural numbers） | $\mathbb{N} = \{0, 1, 2, 3, \ldots\}$ |
| $\mathbb{Z}$ | 整数集（integers） | $\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$ |
| $\mathbb{Z}^+$ | 正整数集（positive integers） | $\mathbb{Z}^+ = \{1, 2, 3, \ldots\}$ |
| $\mathbb{Q}$ | 有理数集（rational numbers） | $\mathbb{Q} = \{p/q : p \in \mathbb{Z}, q \in \mathbb{Z}^+, \gcd(p,q)=1\}$ |
| $\mathbb{R}$ | 实数集（real numbers） | 有理数与无理数的并集，满足完备性公理 |
| $\mathbb{C}$ | 复数集（complex numbers） | $\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}$，其中 $i^2 = -1$ |

**关键约定**：本书中 $\mathbb{N}$ **包含 $0$**。这与 ISO 80000-2 标准以及集合论、逻辑学、计算机科学的惯例一致。如果需要排除 $0$，我们写 $\mathbb{N}^* = \mathbb{Z}^+ = \{1, 2, 3, \ldots\}$。

注意：部分数论教材和法国数学传统中 $\mathbb{N}$ 从 $1$ 开始。读者在阅读其他文献时，务必检查作者的约定。

**区间记号**：

| 记号 | 含义 |
|------|------|
| $[a, b]$ | 闭区间（closed interval）：$\{x \in \mathbb{R} : a \leq x \leq b\}$ |
| $(a, b)$ | 开区间（open interval）：$\{x \in \mathbb{R} : a < x < b\}$ |
| $[a, b)$ | 半开半闭区间：$\{x \in \mathbb{R} : a \leq x < b\}$ |
| $(a, b]$ | 半开半闭区间：$\{x \in \mathbb{R} : a < x \leq b\}$ |
| $(-\infty, b]$ | 无穷区间：$\{x \in \mathbb{R} : x \leq b\}$ |
| $[a, +\infty)$ | 无穷区间：$\{x \in \mathbb{R} : x \geq a\}$ |

**注意**：$\infty$ 不是实数，因此含 $\infty$ 的端点永远使用圆括号（开区间）。

---

## A.3 逻辑记号（Logic Notation）

| 记号 | 名称 | 含义 |
|------|------|------|
| $\neg P$ | 否定（negation） | "非 $P$"：当 $P$ 为假时 $\neg P$ 为真 |
| $P \wedge Q$ | 合取（conjunction） | "$P$ 且 $Q$"：两者都为真时才为真 |
| $P \vee Q$ | 析取（disjunction） | "$P$ 或 $Q$"：至少一个为真即为真（包含或） |
| $P \to Q$ | 蕴含（implication） | "若 $P$ 则 $Q$"：仅当 $P$ 真且 $Q$ 假时为假 |
| $P \leftrightarrow Q$ | 双条件（biconditional） | "$P$ 当且仅当 $Q$"：$P$ 与 $Q$ 真值相同时为真 |
| $\forall x$ | 全称量词（universal quantifier） | "对所有 $x$" |
| $\exists x$ | 存在量词（existential quantifier） | "存在某个 $x$" |
| $\exists! x$ | 唯一存在量词（unique existential） | "存在唯一的 $x$" |

**约定**：本书中 $P \to Q$ 的否定写作 $P \wedge \neg Q$（即 $\neg(P \to Q) \equiv P \wedge \neg Q$）。蕴含的逆否命题（contrapositive）为 $\neg Q \to \neg P$，与原命题逻辑等价。蕴含的逆命题（converse）为 $Q \to P$，与原命题不一定等价——混淆逆命题与逆否命题是初学者最常见的错误之一。

---

## A.4 函数记号（Function Notation）

| 记号 | 含义 |
|------|------|
| $f: A \to B$ | $f$ 是从集合 $A$ 到集合 $B$ 的函数，$A$ 是定义域（domain），$B$ 是到达域（codomain） |
| $f(x)$ | $f$ 在 $x$ 处的值（function value） |
| $f \circ g$ | 复合函数（composition）：$(f \circ g)(x) = f(g(x))$ |
| $f^{-1}$ | 反函数（inverse function）：若 $f$ 是双射（bijection），$f^{-1}(y) = x$ 当且仅当 $f(x) = y$ |
| $f^{-1}(B')$ | 原像（preimage）：$f^{-1}(B') = \{x \in A : f(x) \in B'\}$，即使 $f$ 不是双射也有定义 |
| $\text{dom}(f)$ | 定义域（domain） |
| $\text{ran}(f)$ | 值域（range）：$\text{ran}(f) = \{f(x) : x \in A\}$ |
| $\text{Im}(f)$ | 像（image），同值域 |
| $f\big|_S$ | 限制（restriction）：$f$ 在子集 $S \subseteq A$ 上的限制 |

**注意**：$f^{-1}$ 有两种用法——反函数和原像集合。当 $f$ 不是双射时，$f^{-1}$ 仅在原像的意义下使用。本书在上下文中会明确说明使用的是哪种含义。

**注意**：本书区分"到达域"（codomain）和"值域"（range）。$f: \mathbb{R} \to \mathbb{R}$，$f(x) = x^2$ 的到达域是 $\mathbb{R}$，但值域是 $[0, +\infty)$。

---

## A.5 向量记号（Vector Notation）

| 记号 | 使用场景 |
|------|----------|
| $\vec{v}$ | 箭头记号：用于几何上下文（平面/空间几何、物理向量） |
| $\mathbf{v}$ | 粗体记号：用于代数/矩阵上下文（线性代数、向量空间） |
| $\vec{AB}$ | 从点 $A$ 到点 $B$ 的有向线段 |
| $\|\mathbf{v}\|$ 或 $|\vec{v}|$ | 向量的模/范数（magnitude/norm） |
| $\mathbf{v} \cdot \mathbf{w}$ | 点积/内积（dot product / inner product） |
| $\mathbf{v} \times \mathbf{w}$ | 叉积/外积（cross product），仅限三维 |
| $\hat{\mathbf{v}}$ | 单位向量（unit vector）：$\hat{\mathbf{v}} = \mathbf{v}/\|\mathbf{v}\|$ |
| $\mathbf{e}_i$ | 标准基向量（standard basis vector），第 $i$ 个分量为 $1$，其余为 $0$ |
| $\mathbf{0}$ | 零向量（zero vector） |

**约定**：本书在几何章节（Part 5 Ch01–Ch04）中使用箭头记号 $\vec{v}$，在代数/线性代数章节（Part 5 Ch05、Part 9）中使用粗体记号 $\mathbf{v}$。两种记号指代同一概念，区别仅是排版惯例。手写时，向量通常在字母上加箭头；在印刷品中，粗体更为常见。

---

## A.6 矩阵记号（Matrix Notation）

| 记号 | 含义 |
|------|------|
| $A, B, C$ | 矩阵用大写字母表示 |
| $a_{ij}$ | 矩阵 $A$ 的第 $i$ 行第 $j$ 列的元素（entry） |
| $A^T$ | 转置矩阵（transpose）：$(A^T)_{ij} = a_{ji}$ |
| $A^{-1}$ | 逆矩阵（inverse matrix）：$AA^{-1} = A^{-1}A = I$ |
| $I$ 或 $I_n$ | $n \times n$ 单位矩阵（identity matrix） |
| $O$ | 零矩阵（zero matrix） |
| $\det(A)$ 或 $|A|$ | 行列式（determinant） |
| $\text{tr}(A)$ | 迹（trace）：对角元素之和 |
| $\text{rank}(A)$ | 秩（rank）：最大线性无关行/列的数目 |
| $[A \mid \mathbf{b}]$ | 增广矩阵（augmented matrix） |

**注意**：$|A|$ 既可以表示行列式，也可能在某些上下文中表示矩阵的范数。本书中 $|A|$ 专指行列式，范数使用 $\|A\|$。

---

## A.7 微积分预备记号（Pre-Calculus / Analysis Notation）

| 记号 | 含义 |
|------|------|
| $\lim_{x \to a} f(x)$ | 极限（limit）：$x$ 趋于 $a$ 时 $f(x)$ 的极限 |
| $\lim_{n \to \infty} a_n$ | 数列极限：$n$ 趋于无穷时 $a_n$ 的极限 |
| $\sum_{k=1}^{n} a_k$ | 有限求和（finite sum） |
| $\sum_{k=1}^{\infty} a_k$ | 无穷级数（infinite series） |
| $\prod_{k=1}^{n} a_k$ | 有限乘积（finite product） |
| $f'(x)$ | 导数（derivative）的 Lagrange 记号 |
| $\frac{df}{dx}$ | 导数的 Leibniz 记号 |
| $\int_a^b f(x)\,dx$ | 定积分（definite integral） |
| $\epsilon$ | 任意小的正数（通常在 $\epsilon$-$\delta$ 或 $\epsilon$-$N$ 定义中） |
| $\delta$ | 与 $\epsilon$ 对应的正数（在 $\epsilon$-$\delta$ 定义中） |
| $o(g(x))$, $O(g(x))$ | 渐近记号（asymptotic notation）：小 $o$ 和大 $O$ |

**约定**：本书在第六部分（分析预备）中同时使用 Lagrange 记号 $f'(x)$ 和 Leibniz 记号 $\frac{df}{dx}$。前者简洁，后者在链式法则和积分换元中更具启发性。两种记号表达相同的数学概念。

---

## A.8 常用缩写与符号（Common Abbreviations and Symbols）

| 缩写/符号 | 全称 | 中文 |
|-----------|------|------|
| iff | if and only if | 当且仅当 |
| WLOG | without loss of generality | 不失一般性 |
| s.t. | such that | 使得 |
| QED / $\square$ | quod erat demonstrandum | 证毕 |
| $\Rightarrow$ | implies（在证明推理中） | 推出/蕴含 |
| $\Leftrightarrow$ | if and only if（在证明推理中） | 当且仅当 |
| $:=$ 或 $\triangleq$ | defined as | 定义为 |
| $\therefore$ | therefore | 因此/所以 |
| $\because$ | because | 因为 |
| LHS / RHS | left-hand side / right-hand side | 左端/右端 |

**约定**：本书在正式定义中使用 $:=$ 表示"定义为"（左侧被定义为右侧的含义）。例如 $n! := 1 \times 2 \times \cdots \times n$ 表示阶乘的定义。

---

## A.9 本书 vs. 中国高中教材的记号差异

中国高中数学教材（人教版等）在记号上有若干与国际惯例不同之处。下表列出主要差异，帮助有中国高中背景的读者过渡：

| 概念 | 本书记号 | 中国高中教材记号 | 说明 |
|------|----------|------------------|------|
| 自然数集 | $\mathbb{N}$ | $N$ | 高中用普通字母，大学和国际文献用黑板粗体（blackboard bold） |
| 正整数集 | $\mathbb{Z}^+$ 或 $\mathbb{N}^*$ | $N^*$ 或 $N_+$ | 高中教材常用 $N^*$，本书优先使用 $\mathbb{Z}^+$ |
| 整数集 | $\mathbb{Z}$ | $Z$ | 同上，字体差异 |
| 有理数集 | $\mathbb{Q}$ | $Q$ | 同上 |
| 实数集 | $\mathbb{R}$ | $R$ | 同上 |
| 子集 | $\subseteq$ | $\subseteq$ 或 $\subset$ | 高中教材中 $\subset$ 通常表示"子集（含相等）"，本书中 $\subset$ 不使用，用 $\subseteq$ 和 $\subsetneq$ 区分 |
| 真子集 | $\subsetneq$ | $\subsetneq$ 或 $\subset$ | 高中教材的 $\subset$ 有时表示真子集——这是歧义的来源 |
| 补集 | $A^c$ 或 $\overline{A}$ | $\complement_U A$ | 高中使用下标明确标注全集 $U$ |
| 空集 | $\emptyset$ | $\emptyset$ 或 $\varnothing$ | 基本一致，注意 $\emptyset \neq \phi$（希腊字母 phi） |
| 向量 | $\vec{a}$ 或 $\mathbf{a}$ | $\vec{a}$ | 高中统一使用箭头记号 |
| 绝对值/模 | $|x|$, $\|\mathbf{v}\|$ | $|x|$, $|\vec{a}|$ | 高中不区分绝对值和向量模的记号 |
| 导数 | $f'(x)$ | $f'(x)$ 或 $y'$ | 基本一致 |
| 对数 | $\ln x$, $\log_a x$ | $\lg x$ (常用对数), $\ln x$ | 高中用 $\lg$ 表示以 $10$ 为底的对数；本书使用 $\log_{10}$ 或 $\log$ |

**重要提示**：高中教材中 $\lg x$ 表示 $\log_{10} x$，这在国际文献中并不通用。本书中 $\log$ 如无底数标注，在分析/微积分上下文中通常指自然对数 $\ln$，在数论/离散数学上下文中通常指以 $2$ 为底的对数——具体含义视上下文而定，首次使用时会明确说明。

---

## A.10 本书 vs. ISO 80000-2 标准

ISO 80000-2（数学符号标准）是符号使用的国际参考。本书基本遵循此标准，以下列出少数差异：

| 概念 | ISO 80000-2 | 本书 | 说明 |
|------|-------------|------|------|
| 自然数集 | $\mathbb{N}$ 包含 $0$ | $\mathbb{N}$ 包含 $0$ | 一致 |
| 实部/虚部 | $\text{Re}\,z$, $\text{Im}\,z$ | $\text{Re}(z)$, $\text{Im}(z)$ | 本书加括号以增加可读性 |
| 除法 | $a/b$ 或 $\frac{a}{b}$ | 同上 | 一致 |
| 区间 | $[a, b]$, $]a, b[$ | $[a, b]$, $(a, b)$ | ISO 允许两种记法；本书使用圆括号表示开区间，不使用反方括号 $]a, b[$ |
| 行列式 | $\det A$ | $\det(A)$ 或 $|A|$ | 本书加括号以增加可读性，竖线记号在小矩阵中更简洁 |
| 转置 | $A^{\mathsf{T}}$ | $A^T$ | 本书使用斜体 $T$，不使用 sans-serif 体 |
| 虚数单位 | $\mathrm{i}$ (正体) | $i$ (斜体) | ISO 推荐正体以区分变量，但斜体在数学文献中更普遍 |
| 自然底数 | $\mathrm{e}$ (正体) | $e$ (斜体) | 同上 |
| 圆周率 | $\pi$ | $\pi$ | 一致 |

**原则**：本书在 ISO 标准和数学传统之间取得平衡。当两者冲突时，优先选择数学文献中更广泛使用的记号，以便读者后续阅读大学教材时无需重新适应。

---

## A.11 阅读建议

1. **不要试图"背"记号**：记号是工具，不是目的。反复使用后自然熟悉。
2. **遇到陌生记号时回查**：本附录和[符号索引](symbol-table.md)是你的参考手册。
3. **注意上下文**：同一符号在不同上下文中可能有不同含义（例如 $|x|$ 表示绝对值或集合基数）。
4. **读其他书时先查记号约定**：严肃的数学教材在前言或附录中都会列出记号约定。
5. **从歧义中学习**：记号的歧义（如 $\subset$ 的两种用法）恰恰说明了精确定义的重要性——这本身就是一堂数学课。
