# §1 向量空间的直觉（Vector Space Intuition）[Bridge]

**前置知识**：[Part 1 第 1 章 逻辑](../../part-01-foundations/ch01-logic/README.md)（命题逻辑、量词）、[Part 1 第 2 章 集合](../../part-01-foundations/ch02-sets/README.md)（集合运算、子集）、[Part 5 第 5 章 向量](../../part-05-geometry/ch05-vectors/README.md)（几何向量的加法、数乘）

**全景图**：在 Part 5 中，我们把向量理解为"有方向和大小的箭头"。但数学家发现：不仅箭头可以"相加"和"缩放"，多项式也可以，函数也可以，甚至矩阵也可以——它们服从完全相同的代数规则。把这些规则提炼出来，就得到**向量空间**的公理。本节从具体的 $\mathbb{R}^n$ 出发，逐步抽象到公理化定义，然后探索子空间的概念。这是线性代数大厦的地基——后续的矩阵（Ch02）、线性方程组（Ch03）、行列式（Ch04）都建立在向量空间之上。

**预估学习时间**：约 4–5 小时

---

## 动机

你已经在 Part 5 中学会了对**几何向量**进行加法和数乘运算。例如在 $\mathbb{R}^2$ 中：

$$\mathbf{u} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}, \quad \mathbf{v} = \begin{pmatrix} 3 \\ -1 \end{pmatrix}$$

$$\mathbf{u} + \mathbf{v} = \begin{pmatrix} 4 \\ 1 \end{pmatrix}, \quad 3\mathbf{u} = \begin{pmatrix} 3 \\ 6 \end{pmatrix}$$

这些运算具有很好的性质：加法满足交换律、结合律，有零向量，有反向量……但这些性质并不是 $\mathbb{R}^2$ 所独有的。

考虑**多项式**。设 $p(x) = 1 + 2x$ 和 $q(x) = 3 - x$，那么：

$$p(x) + q(x) = 4 + x, \quad 3 \cdot p(x) = 3 + 6x$$

这些运算同样满足交换律、结合律，有零多项式 $0$，有反多项式 $-p(x) = -1 - 2x$……

惊人的是，**这两个完全不同的数学对象服从相同的代数规则**！线性代数的伟大洞察是：把这些共同规则提炼为**公理**，统一研究所有满足这些规则的对象。

---

## 1. 从几何向量到 $\mathbb{R}^n$（From Geometric Vectors to $\mathbb{R}^n$）

### 1.1 $\mathbb{R}^n$ 的定义

> **定义 1**（$\mathbb{R}^n$）
>
> $n$ 维实数空间 $\mathbb{R}^n$ 是所有 $n$ 元有序实数组的集合：
>
> $$\mathbb{R}^n = \left\{ \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} : x_1, x_2, \ldots, x_n \in \mathbb{R} \right\}$$
>
> 其中的元素称为**向量**（vector），$x_i$ 称为第 $i$ 个**分量**（component）。

$\mathbb{R}^1$ 就是实数轴，$\mathbb{R}^2$ 就是平面，$\mathbb{R}^3$ 就是三维空间。当 $n \geq 4$ 时，虽然无法画图，但代数上一切照旧。

### 1.2 $\mathbb{R}^n$ 上的运算

在 $\mathbb{R}^n$ 中，我们定义两种运算：

**向量加法**（vector addition）：逐分量相加

$$\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} + \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix} = \begin{pmatrix} x_1 + y_1 \\ \vdots \\ x_n + y_n \end{pmatrix}$$

**标量乘法**（scalar multiplication）：每个分量乘以标量

$$c \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} = \begin{pmatrix} cx_1 \\ \vdots \\ cx_n \end{pmatrix}, \quad c \in \mathbb{R}$$

这里的 $c$ 称为**标量**（scalar）——在我们的讨论中，标量就是实数。

### 1.3 $\mathbb{R}^n$ 的代数性质

$\mathbb{R}^n$ 上的加法和标量乘法满足以下八条性质。设 $\mathbf{u}, \mathbf{v}, \mathbf{w} \in \mathbb{R}^n$，$c, d \in \mathbb{R}$：

| 编号 | 性质 | 公式 |
|------|------|------|
| A1 | 加法交换律 | $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ |
| A2 | 加法结合律 | $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$ |
| A3 | 零元素 | 存在 $\mathbf{0}$ 使得 $\mathbf{u} + \mathbf{0} = \mathbf{u}$ |
| A4 | 加法逆元 | 存在 $-\mathbf{u}$ 使得 $\mathbf{u} + (-\mathbf{u}) = \mathbf{0}$ |
| S1 | 标量乘法结合律 | $c(d\mathbf{u}) = (cd)\mathbf{u}$ |
| S2 | 标量乘法单位元 | $1 \cdot \mathbf{u} = \mathbf{u}$ |
| D1 | 标量对向量加法的分配律 | $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$ |
| D2 | 向量对标量加法的分配律 | $(c + d)\mathbf{u} = c\mathbf{u} + d\mathbf{u}$ |

在 $\mathbb{R}^n$ 中，这八条性质都可以通过**逐分量计算**直接验证。例如 A1（交换律）：

$$\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix} + \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix} = \begin{pmatrix} x_1 + y_1 \\ \vdots \\ x_n + y_n \end{pmatrix} = \begin{pmatrix} y_1 + x_1 \\ \vdots \\ y_n + x_n \end{pmatrix} = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix} + \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$$

其中第二个等号用了实数加法的交换律。

---

## 2. 向量空间的公理（Vector Space Axioms）

$\mathbb{R}^n$ 的八条性质不是偶然的——多项式、函数、矩阵等对象也满足同样的规则。数学家将这些规则提炼为**公理**，定义了一个更一般的概念。

> **定义 2**（向量空间）
>
> 设 $V$ 是一个非空集合，$\mathbb{R}$ 是实数域。在 $V$ 上定义两种运算：
> - **向量加法**：$+: V \times V \to V$
> - **标量乘法**：$\cdot: \mathbb{R} \times V \to V$
>
> 如果这两种运算满足以下八条公理（axioms），则称 $(V, +, \cdot)$ 为一个（实数域上的）**向量空间**（vector space），$V$ 的元素称为**向量**：
>
> **加法公理**（对任意 $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$）：
> 1. **交换律**：$\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$
> 2. **结合律**：$(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$
> 3. **零元素**：存在 $\mathbf{0} \in V$，使得 $\mathbf{u} + \mathbf{0} = \mathbf{u}$
> 4. **逆元素**：对每个 $\mathbf{u} \in V$，存在 $-\mathbf{u} \in V$，使得 $\mathbf{u} + (-\mathbf{u}) = \mathbf{0}$
>
> **标量乘法公理**（对任意 $\mathbf{u}, \mathbf{v} \in V$ 和 $c, d \in \mathbb{R}$）：
> 5. **标量乘法结合律**：$c(d\mathbf{u}) = (cd)\mathbf{u}$
> 6. **标量单位元**：$1 \cdot \mathbf{u} = \mathbf{u}$
> 7. **标量对向量加法的分配律**：$c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$
> 8. **向量对标量加法的分配律**：$(c + d)\mathbf{u} = c\mathbf{u} + d\mathbf{u}$

**术语**：向量空间中的"向量"不一定是箭头——它是满足这八条规则的**任何对象**。这就是抽象的力量。

### 2.1 公理的直觉

这八条公理说的是：

- A1–A4：加法"行为良好"——可以交换顺序、重新结合括号、加零不变、可以"撤销"加法。
- S1–S2：标量乘法"行为良好"——连续缩放等于一次缩放、乘以 $1$ 不变。
- D1–D2：加法和标量乘法"协调一致"——分配律将两种运算联系起来。

这些规则如此自然，以至于你可能觉得"不言而喻"。但正是通过**明确列出**这些规则，我们才能研究哪些对象满足它们、哪些不满足——这就是公理化方法的威力。

---

## 3. 向量空间的例子（Examples of Vector Spaces）

### 3.1 $\mathbb{R}^n$——最基本的例子

$\mathbb{R}^n$（连同逐分量的加法和标量乘法）是向量空间——我们在第 1 节已经验证了这一点。

- $\mathbb{R}^1$：实数轴。向量就是实数。
- $\mathbb{R}^2$：平面上的列向量。
- $\mathbb{R}^3$：三维空间中的列向量。

### 3.2 多项式空间 $P_n$

> **定义 3**（多项式空间）
>
> 设 $n \geq 0$ 为非负整数。$P_n$ 是所有次数**不超过** $n$ 的实系数多项式的集合：
>
> $$P_n = \{ a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n : a_0, a_1, \ldots, a_n \in \mathbb{R} \}$$
>
> 加法和标量乘法按通常的多项式运算定义。

**验证**（选取几条公理来检验）：

- **加法封闭**：两个次数 $\leq n$ 的多项式之和，次数仍 $\leq n$。✓
- **标量乘法封闭**：$c \cdot p(x)$ 的次数仍 $\leq n$。✓
- **零元素**：零多项式 $0$（所有系数为 $0$）。✓
- **逆元素**：$p(x) = a_0 + a_1 x + \cdots + a_n x^n$ 的逆为 $-p(x) = -a_0 - a_1 x - \cdots - a_n x^n$。✓
- 其余公理由实数运算的性质直接继承。

**注意**：$P_n$ 不同于"$n$ 次多项式的集合"。例如 $P_2$ 包含 $1 + x$（1 次）和 $0$（零多项式），因为它们的次数 $\leq 2$。这一点很重要——如果只取恰好 $n$ 次的多项式，加法不封闭（$x^2 + (-x^2) = 0$），就不构成向量空间。

### 3.3 函数空间

> **定义 4**（函数空间）
>
> 设 $S$ 是一个非空集合。从 $S$ 到 $\mathbb{R}$ 的所有函数的集合记为 $\mathcal{F}(S, \mathbb{R})$，加法和标量乘法定义为：
>
> $$(f + g)(x) = f(x) + g(x), \quad (cf)(x) = c \cdot f(x), \quad \forall x \in S$$

$\mathcal{F}(S, \mathbb{R})$ 是一个向量空间。特别地：

- 零元素是**零函数** $\mathbf{0}(x) = 0$（对所有 $x$）。
- $f$ 的逆元素是 $(-f)(x) = -f(x)$。

**重要的子例**：

| 函数空间 | 定义 |
|----------|------|
| $C[a,b]$ | $[a,b]$ 上所有连续函数 |
| $C^1[a,b]$ | $[a,b]$ 上所有具有连续导数的函数 |
| $C^\infty(\mathbb{R})$ | 所有无穷次可微函数 |

这些都是向量空间——因为连续函数之和仍连续，连续函数的标量倍仍连续。

### 3.4 零空间

只含零向量的集合 $\{\mathbf{0}\}$ 是一个向量空间，称为**零空间**（zero space）或**平凡向量空间**（trivial vector space）。

### 3.5 非例子：什么不是向量空间？

**反例 1**：$\mathbb{R}^2$ 中的第一象限 $\{(x,y) : x \geq 0, y \geq 0\}$。

这不是向量空间，因为**加法逆元不存在**：$(1, 2)$ 在第一象限中，但 $-(1,2) = (-1,-2)$ 不在。

**反例 2**：所有恰好 $2$ 次的多项式集合 $\{a_0 + a_1 x + a_2 x^2 : a_2 \neq 0\}$。

这不是向量空间，因为**加法不封闭**：$x^2 + (-x^2 + 1) = 1$，结果不是 $2$ 次多项式。实际上，零多项式也不在这个集合中。

**反例 3**：定义"加法"为 $\mathbf{u} \oplus \mathbf{v} = \mathbf{u} - \mathbf{v}$ 的 $\mathbb{R}^2$。

这不满足交换律：$\mathbf{u} \oplus \mathbf{v} = \mathbf{u} - \mathbf{v} \neq \mathbf{v} - \mathbf{u} = \mathbf{v} \oplus \mathbf{u}$（一般地）。

---

## 4. 从公理推导的基本性质（Properties Derived from Axioms）

以下性质看似显然，但需要从八条公理**严格推导**。这是公理化方法的精髓：一切结论都从公理出发。

> **命题 1**（零向量唯一）
>
> 向量空间中的零向量是唯一的。

**证明**：假设 $\mathbf{0}'$ 也是零向量，即对所有 $\mathbf{u}$，$\mathbf{u} + \mathbf{0}' = \mathbf{u}$。则：

$$\mathbf{0} = \mathbf{0} + \mathbf{0}' = \mathbf{0}' + \mathbf{0} = \mathbf{0}'$$

第一个等号用了 $\mathbf{0}'$ 是零向量，第三个等号用了 $\mathbf{0}$ 是零向量。$\blacksquare$

> **命题 2**（加法逆元唯一）
>
> 每个向量的加法逆元是唯一的。

**证明**：设 $\mathbf{u} + \mathbf{w}_1 = \mathbf{0}$ 且 $\mathbf{u} + \mathbf{w}_2 = \mathbf{0}$。则：

$$\mathbf{w}_1 = \mathbf{w}_1 + \mathbf{0} = \mathbf{w}_1 + (\mathbf{u} + \mathbf{w}_2) = (\mathbf{w}_1 + \mathbf{u}) + \mathbf{w}_2 = \mathbf{0} + \mathbf{w}_2 = \mathbf{w}_2$$

其中第三个等号用了结合律（A2）。$\blacksquare$

> **命题 3**（标量 $0$ 的作用）
>
> 对任意向量 $\mathbf{u}$，$0 \cdot \mathbf{u} = \mathbf{0}$。

**证明**：

$$0 \cdot \mathbf{u} = (0 + 0) \cdot \mathbf{u} = 0 \cdot \mathbf{u} + 0 \cdot \mathbf{u}$$

两边加上 $0 \cdot \mathbf{u}$ 的逆元：$\mathbf{0} = 0 \cdot \mathbf{u}$。$\blacksquare$

> **命题 4**（$(-1)$ 乘以向量给出逆元）
>
> 对任意向量 $\mathbf{u}$，$(-1) \cdot \mathbf{u} = -\mathbf{u}$。

**证明**：

$$\mathbf{u} + (-1)\mathbf{u} = 1 \cdot \mathbf{u} + (-1) \cdot \mathbf{u} = (1 + (-1)) \cdot \mathbf{u} = 0 \cdot \mathbf{u} = \mathbf{0}$$

由逆元的唯一性，$(-1)\mathbf{u} = -\mathbf{u}$。$\blacksquare$

---

## 5. 子空间（Subspaces）

### 5.1 定义

> **定义 5**（子空间）
>
> 设 $V$ 是一个向量空间，$W \subseteq V$ 是 $V$ 的一个非空子集。如果 $W$ 在 $V$ 的加法和标量乘法下**自身也构成向量空间**，则称 $W$ 是 $V$ 的**子空间**（subspace）。

直觉上，子空间就是向量空间中"自成一体"的子集——从中取向量做加法和数乘，结果永远不会跑出这个子集。

### 5.2 子空间判定法

要验证子空间，不需要逐一检验八条公理——因为大部分公理由 $V$ 继承。只需检验三条：

> **定理 1**（子空间判定法，Subspace Test）
>
> 设 $V$ 是向量空间，$W \subseteq V$ 非空。$W$ 是 $V$ 的子空间当且仅当：
> 1. **零向量**：$\mathbf{0} \in W$
> 2. **加法封闭**：若 $\mathbf{u}, \mathbf{v} \in W$，则 $\mathbf{u} + \mathbf{v} \in W$
> 3. **标量乘法封闭**：若 $\mathbf{u} \in W$，$c \in \mathbb{R}$，则 $c\mathbf{u} \in W$

**证明思路**：

- 条件 2 和 3 确保运算不"跑出" $W$。
- 条件 1 确保零元素存在（也可由条件 3 导出：取 $c = 0$，则 $0 \cdot \mathbf{u} = \mathbf{0} \in W$）。
- 加法逆元由条件 3 保证：取 $c = -1$，则 $(-1)\mathbf{u} = -\mathbf{u} \in W$。
- 交换律、结合律、分配律等从 $V$ 继承。$\blacksquare$

**实用技巧**：条件 2 和 3 可以合并为一条——**对线性组合封闭**：若 $\mathbf{u}, \mathbf{v} \in W$，$c, d \in \mathbb{R}$，则 $c\mathbf{u} + d\mathbf{v} \in W$。

### 5.3 子空间的例子

**例 1**：$\mathbb{R}^3$ 中过原点的平面。

设 $W = \{(x, y, z) \in \mathbb{R}^3 : ax + by + cz = 0\}$，其中 $a, b, c$ 不全为零。

验证：
- $\mathbf{0} = (0, 0, 0) \in W$，因为 $a \cdot 0 + b \cdot 0 + c \cdot 0 = 0$。✓
- 设 $\mathbf{u} = (u_1, u_2, u_3), \mathbf{v} = (v_1, v_2, v_3) \in W$，则 $a u_1 + b u_2 + c u_3 = 0$ 且 $a v_1 + b v_2 + c v_3 = 0$。于是 $a(u_1 + v_1) + b(u_2 + v_2) + c(u_3 + v_3) = 0$，所以 $\mathbf{u} + \mathbf{v} \in W$。✓
- 设 $\mathbf{u} \in W$，$k \in \mathbb{R}$。则 $a(ku_1) + b(ku_2) + c(ku_3) = k(au_1 + bu_2 + cu_3) = 0$，所以 $k\mathbf{u} \in W$。✓

所以过原点的平面是 $\mathbb{R}^3$ 的子空间。

**例 2**：$\mathbb{R}^3$ 中过原点的直线。

$W = \{t \mathbf{d} : t \in \mathbb{R}\}$，其中 $\mathbf{d}$ 是一个固定的非零向量。容易验证这是子空间。

**例 3**：不过原点的平面**不是**子空间。

$W = \{(x, y, z) : x + y + z = 1\}$ 不是子空间，因为 $\mathbf{0} = (0,0,0) \notin W$（$0 + 0 + 0 = 0 \neq 1$）。

**例 4**：$P_n$ 是 $P_m$ 的子空间（当 $n \leq m$ 时）。

次数 $\leq n$ 的多项式是次数 $\leq m$ 的多项式的子集，且对加法和标量乘法封闭。

**例 5**：连续函数空间 $C[a,b]$ 是所有函数空间 $\mathcal{F}([a,b], \mathbb{R})$ 的子空间。

连续函数之和仍连续，连续函数的标量倍仍连续，零函数连续。

### 5.4 子空间的交集

> **命题 5**（子空间的交集仍为子空间）
>
> 设 $W_1$ 和 $W_2$ 是向量空间 $V$ 的子空间，则 $W_1 \cap W_2$ 也是 $V$ 的子空间。

**证明**：
- $\mathbf{0} \in W_1$ 且 $\mathbf{0} \in W_2$，所以 $\mathbf{0} \in W_1 \cap W_2$。
- 设 $\mathbf{u}, \mathbf{v} \in W_1 \cap W_2$。则 $\mathbf{u}, \mathbf{v} \in W_1$，所以 $\mathbf{u} + \mathbf{v} \in W_1$（$W_1$ 对加法封闭）；类似地 $\mathbf{u} + \mathbf{v} \in W_2$。所以 $\mathbf{u} + \mathbf{v} \in W_1 \cap W_2$。
- 标量乘法封闭性的证明类似。$\blacksquare$

**注意**：子空间的并集一般**不是**子空间！例如 $\mathbb{R}^2$ 中的 $x$ 轴和 $y$ 轴的并集：$(1,0)$ 和 $(0,1)$ 都在并集中，但 $(1,0) + (0,1) = (1,1)$ 不在任何一条坐标轴上。

---

## 例题

### 例题 1：验证 $\mathbb{R}^2$ 的子空间

> **题目**：设 $W = \{(x, y) \in \mathbb{R}^2 : 2x - 3y = 0\}$。证明 $W$ 是 $\mathbb{R}^2$ 的子空间，并给出 $W$ 的几何描述。

**解答**：

用子空间判定法：

**零向量**：$(0, 0) \in W$，因为 $2 \cdot 0 - 3 \cdot 0 = 0$。✓

**加法封闭**：设 $(x_1, y_1), (x_2, y_2) \in W$，即 $2x_1 - 3y_1 = 0$ 且 $2x_2 - 3y_2 = 0$。则：

$$2(x_1 + x_2) - 3(y_1 + y_2) = (2x_1 - 3y_1) + (2x_2 - 3y_2) = 0 + 0 = 0$$

所以 $(x_1 + x_2, y_1 + y_2) \in W$。✓

**标量乘法封闭**：设 $(x, y) \in W$，$c \in \mathbb{R}$。则：

$$2(cx) - 3(cy) = c(2x - 3y) = c \cdot 0 = 0$$

所以 $(cx, cy) \in W$。✓

因此 $W$ 是 $\mathbb{R}^2$ 的子空间。

**几何描述**：$2x - 3y = 0$ 即 $y = \frac{2}{3}x$，这是过原点的一条直线。$W$ 是斜率为 $\frac{2}{3}$ 的过原点直线。$\blacksquare$

### 例题 2：判断是否为子空间

> **题目**：以下哪些是 $\mathbb{R}^3$ 的子空间？
>
> (a) $W_1 = \{(x, y, z) : x + y + z = 0\}$
>
> (b) $W_2 = \{(x, y, z) : x^2 + y^2 + z^2 \leq 1\}$
>
> (c) $W_3 = \{(x, y, z) : x = 2z\}$

**解答**：

**(a)** $W_1$ **是**子空间。

- $\mathbf{0} \in W_1$：$0 + 0 + 0 = 0$。✓
- 加法封闭：$(x_1 + y_1 + z_1) + (x_2 + y_2 + z_2) = (x_1+x_2) + (y_1+y_2) + (z_1+z_2) = 0$。✓
- 标量乘法封闭：$cx + cy + cz = c(x+y+z) = 0$。✓

**(b)** $W_2$ **不是**子空间。

虽然 $\mathbf{0} \in W_2$，但标量乘法不封闭：$(1, 0, 0) \in W_2$（因为 $1 \leq 1$），但 $2(1,0,0) = (2,0,0) \notin W_2$（因为 $4 > 1$）。

**(c)** $W_3$ **是**子空间。

- $\mathbf{0} \in W_3$：$0 = 2 \cdot 0$。✓
- 加法封闭：若 $x_1 = 2z_1$ 且 $x_2 = 2z_2$，则 $x_1 + x_2 = 2(z_1 + z_2)$。✓
- 标量乘法封闭：若 $x = 2z$，则 $cx = 2(cz)$。✓ $\blacksquare$

### 例题 3：多项式空间的子空间

> **题目**：设 $W = \{p(x) \in P_3 : p(0) = 0\}$。证明 $W$ 是 $P_3$ 的子空间。

**解答**：

$P_3$ 中的元素形如 $p(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3$。条件 $p(0) = 0$ 意味着 $a_0 = 0$。

所以 $W = \{a_1 x + a_2 x^2 + a_3 x^3 : a_1, a_2, a_3 \in \mathbb{R}\}$。

用子空间判定法：

- **零元素**：零多项式 $0$ 满足 $0 = 0$，所以 $0 \in W$。✓
- **加法封闭**：设 $p, q \in W$，则 $p(0) = 0$ 且 $q(0) = 0$。于是 $(p+q)(0) = p(0) + q(0) = 0$，所以 $p + q \in W$。✓
- **标量乘法封闭**：$(cp)(0) = c \cdot p(0) = c \cdot 0 = 0$，所以 $cp \in W$。✓

因此 $W$ 是 $P_3$ 的子空间。$\blacksquare$

---

## 要点回顾

| 概念 | 要点 |
|------|------|
| $\mathbb{R}^n$ | $n$ 元有序实数组的集合，逐分量加法和标量乘法 |
| 向量空间 | 满足八条公理（A1–A4, S1–S2, D1–D2）的集合 |
| 向量 | 向量空间的元素——不一定是箭头！ |
| 多项式空间 $P_n$ | 次数 $\leq n$ 的实系数多项式 |
| 函数空间 | 从集合 $S$ 到 $\mathbb{R}$ 的所有函数 |
| 子空间 | 向量空间中对加法和标量乘法封闭的非空子集 |
| 子空间判定法 | 验证三条：含 $\mathbf{0}$、加法封闭、标量乘法封闭 |
| 零空间 | $\{\mathbf{0}\}$——最小的子空间 |

---

## 进度检查点

完成本节后，你应该能够：

- [ ] 写出 $\mathbb{R}^n$ 的定义及其上的加法和标量乘法
- [ ] 陈述向量空间的八条公理
- [ ] 给出至少三个不同的向量空间例子
- [ ] 给出至少两个"不是向量空间"的反例并说明原因
- [ ] 用子空间判定法验证一个子集是否为子空间
- [ ] 解释为什么过原点的平面是子空间，而不过原点的平面不是

---

## 自测题

**1.** $\mathbb{R}^2$ 中，集合 $W = \{(x, y) : y = x^2\}$ 是否为子空间？

<details>
<summary>答案</summary>

不是。加法不封闭：$(1, 1) \in W$（$1 = 1^2$），$(2, 4) \in W$（$4 = 2^2$），但 $(1,1) + (2,4) = (3, 5)$，而 $5 \neq 3^2 = 9$，所以 $(3,5) \notin W$。

也可以注意到 $\mathbf{0} = (0,0) \in W$，但标量乘法不封闭：$2(1,1) = (2,2)$，而 $2 \neq 2^2 = 4$。
</details>

**2.** 向量空间中，$0 \cdot \mathbf{v}$ 是否一定等于零向量 $\mathbf{0}$？

<details>
<summary>答案</summary>

是的。这可以从公理推导：$0 \cdot \mathbf{v} = (0+0) \cdot \mathbf{v} = 0 \cdot \mathbf{v} + 0 \cdot \mathbf{v}$。两边加上 $0 \cdot \mathbf{v}$ 的逆元，得 $\mathbf{0} = 0 \cdot \mathbf{v}$。
</details>

**3.** 设 $W = \{(x, y, z) \in \mathbb{R}^3 : x - 2y + z = 0, \; x + z = 0\}$。$W$ 是 $\mathbb{R}^3$ 的子空间吗？

<details>
<summary>答案</summary>

是。$W$ 是两个齐次线性方程的解集，等价于两个子空间的交集。由命题 5，子空间的交集仍为子空间。

也可以直接验证：$\mathbf{0} \in W$；加法和标量乘法封闭性由线性方程的性质保证（齐次线性方程解的和仍为解，标量倍仍为解）。
</details>

**4.** 所有满足 $f(0) = 1$ 的连续函数是否构成 $C(\mathbb{R})$ 的子空间？

<details>
<summary>答案</summary>

不是。零函数 $\mathbf{0}$ 满足 $\mathbf{0}(0) = 0 \neq 1$，所以零函数不在这个集合中。因此它不是子空间。

也可以从加法封闭性看：若 $f(0) = 1$ 且 $g(0) = 1$，则 $(f+g)(0) = 2 \neq 1$。
</details>

---

## 习题引用

本节练习见 [exercises/exercises.md](exercises/exercises.md) 第 §1 部分（第 1–10 题）。
