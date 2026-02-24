# §2 行列式的应用（Applications of Determinants）[Bridge]

**前置知识**：[§1 行列式](01-determinants.md)（行列式定义、性质、计算方法）、[Ch02 §2](../ch02-matrices/02-special-matrices.md)（逆矩阵）、[Ch03 §1](../ch03-linear-systems/01-gaussian-elimination.md)（线性方程组）

**全景图**：行列式不仅是一个数——它是连接线性代数各个主题的**枢纽**。本节探讨行列式的三大应用：(1) 判定矩阵的可逆性——$\det(A) \neq 0$ 与 $A$ 可逆等价；(2) Cramer 法则——用行列式的比值直接写出方程组的解；(3) 伴随矩阵公式——用代数余子式构造逆矩阵。这些工具将行列式、逆矩阵和线性方程组统一在一个优美的理论框架中。

**预估学习时间**：约 3–4 小时

---

## 动机

到目前为止，我们有两种工具来判定方程 $A\mathbf{x} = \mathbf{b}$ 是否有唯一解：

1. **Gauss 消元**：将增广矩阵化为 REF，看主元个数。
2. **秩**：$\text{rank}(A) = n$ 时有唯一解。

现在我们有第三种工具——**行列式**：$\det(A) \neq 0$ 时有唯一解。更妙的是，行列式还能通过 Cramer 法则**直接写出解的公式**。

---

## 1. 可逆性判定（Invertibility Criterion）

> **定理 1**（行列式与可逆性）
>
> $n \times n$ 矩阵 $A$ **可逆**当且仅当 $\det(A) \neq 0$。
>
> 等价表述：以下条件相互等价：
> - (a) $A$ 可逆
> - (b) $\det(A) \neq 0$
> - (c) $\text{rank}(A) = n$
> - (d) $A\mathbf{x} = \mathbf{0}$ 只有平凡解
> - (e) $A$ 的列向量线性无关
> - (f) $A\mathbf{x} = \mathbf{b}$ 对任意 $\mathbf{b}$ 都有唯一解
> - (g) $A$ 可以用行变换化为 $I_n$

**证明思路**（$\det(A) \neq 0 \Leftrightarrow$ $A$ 可逆）：

$(\Rightarrow)$：$A$ 可逆时，$I = AA^{-1}$，所以 $1 = \det(I) = \det(A)\det(A^{-1})$，故 $\det(A) \neq 0$。

$(\Leftarrow)$：$\det(A) \neq 0$ 意味着 Gauss 消元后无全零行（否则行列式为 $0$），所以 $\text{rank}(A) = n$，$A$ 可逆。$\blacksquare$

**这是线性代数的核心定理之一**——它将代数（行列式）、几何（线性无关）和计算（方程组的解）统一起来。

---

## 2. Cramer 法则（Cramer's Rule）

> **定理 2**（Cramer 法则）
>
> 设 $A$ 是 $n \times n$ 可逆矩阵，$\mathbf{b} \in \mathbb{R}^n$。则方程组 $A\mathbf{x} = \mathbf{b}$ 的唯一解为：
>
> $$x_i = \frac{\det(A_i)}{\det(A)}, \qquad i = 1, 2, \ldots, n$$
>
> 其中 $A_i$ 是将 $A$ 的第 $i$ 列替换为 $\mathbf{b}$ 得到的矩阵。

### 2.1 $2 \times 2$ Cramer 法则

$$\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases}$$

$$x = \frac{\begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix}}{\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}} = \frac{c_1 b_2 - b_1 c_2}{a_1 b_2 - b_1 a_2}, \qquad y = \frac{\begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix}}{\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}} = \frac{a_1 c_2 - c_1 a_2}{a_1 b_2 - b_1 a_2}$$

### 2.2 $2 \times 2$ Cramer 法则的证明

设 $A = \begin{pmatrix} a_1 & b_1 \\ a_2 & b_2 \end{pmatrix}$，$\Delta = \det(A) = a_1 b_2 - b_1 a_2 \neq 0$。

方程组 $\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases}$。

第一个方程乘 $b_2$，第二个方程乘 $b_1$：

$$a_1 b_2 x + b_1 b_2 y = c_1 b_2$$
$$a_2 b_1 x + b_1 b_2 y = c_2 b_1$$

两式相减：$(a_1 b_2 - a_2 b_1)x = c_1 b_2 - c_2 b_1$，即 $\Delta \cdot x = \det(A_1)$。

因此 $x = \det(A_1)/\Delta$。$y$ 的证明类似。$\blacksquare$

### 2.3 实际价值

Cramer 法则在**理论上**非常优雅——它给出了解的**封闭公式**（closed-form formula）。但在**计算上**效率低——对 $n \times n$ 方程组需要计算 $n + 1$ 个行列式，总复杂度为 $O(n \cdot n!)$，远不如 Gauss 消元的 $O(n^3)$。

所以 Cramer 法则主要用于：
- **理论分析**（证明解的存在性和唯一性）
- **小规模方程组**（$2 \times 2$ 或 $3 \times 3$）
- **符号计算**（含参数的方程组）

---

## 3. 伴随矩阵与逆矩阵公式（Adjugate Matrix & Inverse Formula）

> **定义 1**（伴随矩阵）
>
> $n \times n$ 矩阵 $A$ 的**伴随矩阵**（adjugate matrix，也称 classical adjoint），记作 $\text{adj}(A)$，是**代数余子式矩阵的转置**：
>
> $$\text{adj}(A) = (C_{ij})^T, \qquad (\text{adj}(A))_{ij} = C_{ji}$$

> **定理 3**（逆矩阵的伴随公式）
>
> 设 $\det(A) \neq 0$。则：
>
> $$A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$$

### 3.1 $2 \times 2$ 情形

$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$。代数余子式：$C_{11} = d$，$C_{12} = -c$，$C_{21} = -b$，$C_{22} = a$。

$$\text{adj}(A) = \begin{pmatrix} C_{11} & C_{21} \\ C_{12} & C_{22} \end{pmatrix} = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

$$A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

这与 Ch02 的公式完全一致！

### 3.2 验证 $A \cdot \text{adj}(A) = \det(A) \cdot I$

$A \cdot \text{adj}(A)$ 的第 $(i, j)$ 元素：

$$\sum_{k=1}^n a_{ik} (\text{adj}(A))_{kj} = \sum_{k=1}^n a_{ik} C_{jk}$$

- 当 $i = j$ 时，这是行列式沿第 $i$ 行的展开 = $\det(A)$。
- 当 $i \neq j$ 时，这是"错位展开"——用第 $i$ 行的元素和第 $j$ 行的代数余子式展开，相当于一个有两行相同的矩阵的行列式 = $0$。

所以 $A \cdot \text{adj}(A) = \det(A) \cdot I$。$\blacksquare$

---

## 4. 高维体积解释（Volume in Higher Dimensions）

在 $\mathbb{R}^n$ 中，$n \times n$ 矩阵 $A$ 的行列式度量 $A$ 的列向量张成的 $n$ 维平行体（paralleltope）的**有符号体积**：

$$\text{Vol}_n = |\det(A)|$$

| 维数 | 几何对象 | 行列式含义 |
|------|----------|-----------|
| $n = 2$ | 平行四边形 | 面积 |
| $n = 3$ | 平行六面体 | 体积 |
| $n = 4$ | 四维平行体 | 超体积 |

**线性变换对体积的影响**：如果 $T(\mathbf{x}) = A\mathbf{x}$，则 $T$ 将体积缩放 $|\det(A)|$ 倍。特别地：

- $|\det(A)| > 1$：体积放大
- $|\det(A)| < 1$：体积缩小
- $|\det(A)| = 1$：体积不变（如旋转矩阵）
- $\det(A) < 0$：方向翻转（如反射）

---

## 例题

### 例题 1：用 Cramer 法则解方程组

> **题目**：用 Cramer 法则解 $\begin{cases} 3x + 2y = 7 \\ x + 4y = 9 \end{cases}$。

**解答**：

$$\Delta = \det\begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix} = 12 - 2 = 10$$

$$x = \frac{\begin{vmatrix} 7 & 2 \\ 9 & 4 \end{vmatrix}}{10} = \frac{28 - 18}{10} = \frac{10}{10} = 1$$

$$y = \frac{\begin{vmatrix} 3 & 7 \\ 1 & 9 \end{vmatrix}}{10} = \frac{27 - 7}{10} = \frac{20}{10} = 2$$

验证：$3(1) + 2(2) = 7$ ✓，$1 + 4(2) = 9$ ✓。$\blacksquare$

### 例题 2：用伴随矩阵求逆

> **题目**：用伴随矩阵公式求 $A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$ 的逆矩阵。

**解答**：

**步骤 1**：计算 $\det(A)$。按第一行展开：

$$\det(A) = 1 \begin{vmatrix} 1 & 1 \\ 0 & 1 \end{vmatrix} - 2\begin{vmatrix} 0 & 1 \\ 1 & 1 \end{vmatrix} + 0 = 1(1) - 2(-1) = 3$$

**步骤 2**：计算所有代数余子式 $C_{ij}$：

$$C_{11} = \begin{vmatrix} 1 & 1 \\ 0 & 1 \end{vmatrix} = 1, \quad C_{12} = -\begin{vmatrix} 0 & 1 \\ 1 & 1 \end{vmatrix} = 1, \quad C_{13} = \begin{vmatrix} 0 & 1 \\ 1 & 0 \end{vmatrix} = -1$$

$$C_{21} = -\begin{vmatrix} 2 & 0 \\ 0 & 1 \end{vmatrix} = -2, \quad C_{22} = \begin{vmatrix} 1 & 0 \\ 1 & 1 \end{vmatrix} = 1, \quad C_{23} = -\begin{vmatrix} 1 & 2 \\ 1 & 0 \end{vmatrix} = 2$$

$$C_{31} = \begin{vmatrix} 2 & 0 \\ 1 & 1 \end{vmatrix} = 2, \quad C_{32} = -\begin{vmatrix} 1 & 0 \\ 0 & 1 \end{vmatrix} = -1, \quad C_{33} = \begin{vmatrix} 1 & 2 \\ 0 & 1 \end{vmatrix} = 1$$

**步骤 3**：伴随矩阵（代数余子式矩阵的转置）：

$$\text{adj}(A) = \begin{pmatrix} 1 & -2 & 2 \\ 1 & 1 & -1 \\ -1 & 2 & 1 \end{pmatrix}$$

**步骤 4**：

$$A^{-1} = \frac{1}{3}\begin{pmatrix} 1 & -2 & 2 \\ 1 & 1 & -1 \\ -1 & 2 & 1 \end{pmatrix}$$

验证（第一行）：$\frac{1}{3}(1 \cdot 1 + (-2) \cdot 0 + 2 \cdot 1, 1 \cdot 2 + (-2) \cdot 1 + 2 \cdot 0, 1 \cdot 0 + (-2) \cdot 1 + 2 \cdot 1) = \frac{1}{3}(3, 0, 0) = (1, 0, 0)$。✓ $\blacksquare$

### 例题 3：行列式与可逆性

> **题目**：对于什么值的 $k$，矩阵 $A = \begin{pmatrix} 1 & k \\ k & 1 \end{pmatrix}$ 不可逆？

**解答**：

$\det(A) = 1 - k^2 = (1-k)(1+k)$。

$A$ 不可逆 $\Leftrightarrow$ $\det(A) = 0$ $\Leftrightarrow$ $k = 1$ 或 $k = -1$。

当 $k = 1$ 时，$A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$（两行相同，秩为 $1$）。

当 $k = -1$ 时，$A = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$（两行成 $-1$ 倍关系，秩为 $1$）。$\blacksquare$

---

## 要点回顾

| 概念 | 要点 |
|------|------|
| 可逆性判定 | $A$ 可逆 $\Leftrightarrow$ $\det(A) \neq 0$ |
| 等价条件 | 可逆 $\Leftrightarrow$ 满秩 $\Leftrightarrow$ 列无关 $\Leftrightarrow$ 唯一解 |
| Cramer 法则 | $x_i = \det(A_i)/\det(A)$ |
| 伴随矩阵 | $\text{adj}(A) = (C_{ij})^T$ |
| 逆矩阵公式 | $A^{-1} = \text{adj}(A)/\det(A)$ |
| 体积解释 | $|\det(A)|$ = $n$ 维平行体的体积 |

---

## 进度检查点

完成本节后，你应该能够：

- [ ] 用行列式判断矩阵是否可逆
- [ ] 陈述"可逆矩阵的等价条件"定理
- [ ] 用 Cramer 法则解 $2 \times 2$ 和 $3 \times 3$ 方程组
- [ ] 计算 $3 \times 3$ 矩阵的伴随矩阵
- [ ] 用伴随矩阵公式求逆
- [ ] 解释行列式在高维体积中的作用

---

## 自测题

**1.** 设 $\det(A) = 0$。方程 $A\mathbf{x} = \mathbf{b}$ 有唯一解吗？

<details>
<summary>答案</summary>

没有唯一解。$\det(A) = 0$ 意味着 $A$ 不可逆，所以方程要么无解，要么有无穷多解。
</details>

**2.** 用 Cramer 法则解 $\begin{cases} x + y = 3 \\ 2x - y = 3 \end{cases}$。

<details>
<summary>答案</summary>

$\Delta = -1 - 2 = -3$。

$x = \frac{\begin{vmatrix} 3 & 1 \\ 3 & -1 \end{vmatrix}}{-3} = \frac{-3-3}{-3} = \frac{-6}{-3} = 2$。

$y = \frac{\begin{vmatrix} 1 & 3 \\ 2 & 3 \end{vmatrix}}{-3} = \frac{3-6}{-3} = \frac{-3}{-3} = 1$。
</details>

**3.** $2 \times 2$ 旋转矩阵 $R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ 的行列式是什么？它的几何含义？

<details>
<summary>答案</summary>

$\det(R_\theta) = \cos^2\theta + \sin^2\theta = 1$。

几何含义：旋转不改变面积（$|\det| = 1$），也不翻转方向（$\det > 0$）。
</details>

---

## 习题引用

本节练习见 [exercises/exercises.md](exercises/exercises.md) 第 §2 部分（第 11–20 题）。
