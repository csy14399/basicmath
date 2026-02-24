# §2 特殊矩阵（Special Matrices）[Bridge]

**前置知识**：[§1 矩阵运算](01-matrix-operations.md)（矩阵定义、加法、乘法）

**全景图**：并非所有矩阵都"生而平等"——某些特殊结构的矩阵拥有额外的好性质，使得计算更简单、理论更深刻。本节介绍最常见的特殊矩阵（单位矩阵、对角矩阵、三角矩阵、对称矩阵），讨论矩阵转置的定义和性质，然后引入**逆矩阵**——矩阵的"除法"。逆矩阵的存在性与行列式密切相关（Ch04），它也是求解线性方程组（Ch03）的关键工具。

**预估学习时间**：约 3–4 小时

---

## 动机

在实数运算中，$1$ 是乘法的单位元（$1 \cdot a = a$），每个非零数 $a$ 都有乘法逆元 $a^{-1} = 1/a$（使得 $a \cdot a^{-1} = 1$）。矩阵世界中是否有类似的概念？

答案是**有**——单位矩阵 $I$ 就是矩阵乘法的"$1$"，逆矩阵 $A^{-1}$ 就是矩阵的"倒数"。但与实数不同，**不是每个非零矩阵都有逆**——这个区别是线性代数中最深刻的现象之一。

---

## 1. 单位矩阵（Identity Matrix）

> **定义 1**（单位矩阵）
>
> $n \times n$ **单位矩阵**（identity matrix）$I_n$（简写 $I$）是主对角线上全为 $1$、其余全为 $0$ 的方阵：
>
> $$I_n = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix}$$

**性质**：对任何大小适当的矩阵 $A$：

$$I_m A = A, \qquad A I_n = A \qquad (A \text{ 为 } m \times n)$$

$I$ 是矩阵乘法的**单位元**——乘以 $I$ 不改变矩阵。

在线性变换的语言中，$I$ 对应**恒等变换**（identity transformation）：$T_I(\mathbf{x}) = I\mathbf{x} = \mathbf{x}$。

---

## 2. 零矩阵（Zero Matrix）

$m \times n$ **零矩阵** $O$（或 $0_{m \times n}$）是所有元素为 $0$ 的矩阵。

性质：$A + O = A$，$AO = O$，$OA = O$。

---

## 3. 对角矩阵（Diagonal Matrix）

> **定义 2**（对角矩阵）
>
> $n \times n$ **对角矩阵**（diagonal matrix）是除主对角线外所有元素为 $0$ 的方阵：
>
> $$D = \text{diag}(d_1, d_2, \ldots, d_n) = \begin{pmatrix} d_1 & 0 & \cdots & 0 \\ 0 & d_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & d_n \end{pmatrix}$$

**对角矩阵的运算极其简单**：

$$\text{diag}(d_1, \ldots, d_n) \cdot \text{diag}(e_1, \ldots, e_n) = \text{diag}(d_1 e_1, \ldots, d_n e_n)$$

$$\text{diag}(d_1, \ldots, d_n)^k = \text{diag}(d_1^k, \ldots, d_n^k)$$

如果 $d_i \neq 0$ 对所有 $i$，则：

$$\text{diag}(d_1, \ldots, d_n)^{-1} = \text{diag}(1/d_1, \ldots, 1/d_n)$$

**几何意义**：对角矩阵沿坐标轴方向独立缩放。

---

## 4. 三角矩阵（Triangular Matrix）

> **定义 3**（三角矩阵）
>
> **上三角矩阵**（upper triangular matrix）：主对角线以下的元素全为 $0$（$a_{ij} = 0$ 当 $i > j$）。
>
> **下三角矩阵**（lower triangular matrix）：主对角线以上的元素全为 $0$（$a_{ij} = 0$ 当 $i < j$）。

$$\text{上三角: } \begin{pmatrix} * & * & * \\ 0 & * & * \\ 0 & 0 & * \end{pmatrix}, \qquad \text{下三角: } \begin{pmatrix} * & 0 & 0 \\ * & * & 0 \\ * & * & * \end{pmatrix}$$

**性质**：
- 上三角矩阵的乘积仍为上三角矩阵。
- 三角矩阵的行列式等于主对角线元素之积（Ch04）。

---

## 5. 转置（Transpose）

> **定义 4**（转置）
>
> 矩阵 $A = (a_{ij})_{m \times n}$ 的**转置**（transpose）$A^T$ 是将 $A$ 的行变成列（列变成行）得到的 $n \times m$ 矩阵：
>
> $$(A^T)_{ij} = a_{ji}$$

**例子**：

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} \implies A^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$$

### 转置的性质

对大小适当的矩阵 $A, B$ 和标量 $c$：

| 编号 | 性质 | 公式 |
|------|------|------|
| T1 | 双重转置 | $(A^T)^T = A$ |
| T2 | 加法 | $(A + B)^T = A^T + B^T$ |
| T3 | 标量乘法 | $(cA)^T = cA^T$ |
| T4 | 乘积的转置 | $(AB)^T = B^T A^T$ |

**注意 T4 中的顺序颠倒**——$(AB)^T = B^T A^T$，不是 $A^T B^T$！

**T4 的证明**：$((AB)^T)_{ij} = (AB)_{ji} = \sum_k a_{jk}b_{ki} = \sum_k (B^T)_{ik}(A^T)_{kj} = (B^TA^T)_{ij}$。$\blacksquare$

---

## 6. 对称矩阵（Symmetric Matrix）

> **定义 5**（对称矩阵）
>
> 方阵 $A$ 称为**对称矩阵**（symmetric matrix），如果 $A^T = A$，即 $a_{ij} = a_{ji}$ 对所有 $i, j$。

**例子**：$\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 3 & 5 & 6 \end{pmatrix}$ 是对称矩阵——关于主对角线"镜像对称"。

**性质**：
- 对任意矩阵 $A$，$A^T A$ 和 $A A^T$ 都是对称矩阵。

**证明**：$(A^T A)^T = A^T (A^T)^T = A^T A$。$\blacksquare$

---

## 7. 逆矩阵（Inverse Matrix）

### 7.1 定义

> **定义 6**（逆矩阵）
>
> 设 $A$ 是 $n \times n$ 方阵。如果存在 $n \times n$ 方阵 $B$ 使得：
>
> $$AB = BA = I_n$$
>
> 则称 $A$ **可逆**（invertible），$B$ 称为 $A$ 的**逆矩阵**（inverse matrix），记作 $A^{-1}$。

**不可逆的矩阵称为奇异矩阵**（singular matrix）。

### 7.2 逆的唯一性

> **命题 1**（逆的唯一性）
>
> 如果 $A$ 可逆，则 $A^{-1}$ 是唯一的。

**证明**：设 $B$ 和 $C$ 都是 $A$ 的逆。则 $B = BI = B(AC) = (BA)C = IC = C$。$\blacksquare$

### 7.3 逆矩阵的性质

| 性质 | 公式 |
|------|------|
| 逆的逆 | $(A^{-1})^{-1} = A$ |
| 乘积的逆 | $(AB)^{-1} = B^{-1}A^{-1}$（顺序颠倒！） |
| 转置的逆 | $(A^T)^{-1} = (A^{-1})^T$ |
| 标量倍的逆 | $(cA)^{-1} = \frac{1}{c}A^{-1}$（$c \neq 0$） |

**乘积逆的证明**：$(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I$。$\blacksquare$

**注意**：$(AB)^{-1} = B^{-1}A^{-1}$，顺序反转——这与 $(AB)^T = B^TA^T$ 类似。直觉：穿衣服和脱衣服的顺序相反。

### 7.4 $2 \times 2$ 矩阵的逆

> **定理 1**（$2 \times 2$ 逆矩阵公式）
>
> 设 $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$。则 $A$ 可逆当且仅当 $ad - bc \neq 0$，此时：
>
> $$A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

量 $\Delta = ad - bc$ 称为 $A$ 的**行列式**（determinant，Ch04 将详细讨论）。

**验证**：

$$A \cdot \frac{1}{\Delta}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \frac{1}{\Delta}\begin{pmatrix} ad-bc & -ab+ba \\ cd-dc & -cb+da \end{pmatrix} = \frac{1}{\Delta}\begin{pmatrix} \Delta & 0 \\ 0 & \Delta \end{pmatrix} = I$$

**记忆法**："主对角线交换，副对角线变号，除以行列式"。

### 7.5 逆与线性方程组

如果 $A$ 可逆，则方程 $A\mathbf{x} = \mathbf{b}$ 有唯一解：

$$\mathbf{x} = A^{-1}\mathbf{b}$$

但在实际计算中，用 Gauss 消元（Ch03）比显式求 $A^{-1}$ 更高效。

---

## 例题

### 例题 1：求 $2 \times 2$ 逆矩阵

> **题目**：求矩阵 $A = \begin{pmatrix} 3 & 4 \\ 5 & 7 \end{pmatrix}$ 的逆矩阵。

**解答**：

$\Delta = ad - bc = 3 \cdot 7 - 4 \cdot 5 = 21 - 20 = 1$。

$$A^{-1} = \frac{1}{1}\begin{pmatrix} 7 & -4 \\ -5 & 3 \end{pmatrix} = \begin{pmatrix} 7 & -4 \\ -5 & 3 \end{pmatrix}$$

**验证**：$AA^{-1} = \begin{pmatrix} 3 \cdot 7 + 4 \cdot (-5) & 3 \cdot (-4) + 4 \cdot 3 \\ 5 \cdot 7 + 7 \cdot (-5) & 5 \cdot (-4) + 7 \cdot 3 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$。✓ $\blacksquare$

### 例题 2：不可逆矩阵

> **题目**：证明 $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ 不可逆。

**解答**：

$\Delta = 1 \cdot 4 - 2 \cdot 2 = 4 - 4 = 0$。

行列式为零，所以 $A$ 不可逆。

**几何解释**：$A$ 的两列 $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ 和 $\begin{pmatrix} 2 \\ 4 \end{pmatrix}$ 线性相关（第二列是第一列的 $2$ 倍）。$A$ 将整个 $\mathbb{R}^2$ 映射到一条直线上——信息丢失了，无法"反转"变换。$\blacksquare$

### 例题 3：利用逆矩阵解方程

> **题目**：用逆矩阵解方程组 $\begin{cases} 3x + 4y = 10 \\ 5x + 7y = 17 \end{cases}$。

**解答**：

矩阵形式：$\begin{pmatrix} 3 & 4 \\ 5 & 7 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 10 \\ 17 \end{pmatrix}$。

由例题 1，$A^{-1} = \begin{pmatrix} 7 & -4 \\ -5 & 3 \end{pmatrix}$。

$$\begin{pmatrix} x \\ y \end{pmatrix} = A^{-1}\begin{pmatrix} 10 \\ 17 \end{pmatrix} = \begin{pmatrix} 7 \cdot 10 + (-4) \cdot 17 \\ (-5) \cdot 10 + 3 \cdot 17 \end{pmatrix} = \begin{pmatrix} 70 - 68 \\ -50 + 51 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$

验证：$3(2) + 4(1) = 10$。✓ $\quad 5(2) + 7(1) = 17$。✓ $\blacksquare$

---

## 要点回顾

| 概念 | 要点 |
|------|------|
| 单位矩阵 $I$ | 对角线为 $1$，其余为 $0$；$AI = IA = A$ |
| 对角矩阵 | 运算简单：逐元素操作 |
| 转置 $A^T$ | 行列互换；$(AB)^T = B^TA^T$（顺序反转） |
| 对称矩阵 | $A^T = A$；$A^TA$ 总是对称的 |
| 逆矩阵 $A^{-1}$ | $AA^{-1} = A^{-1}A = I$；唯一的 |
| $2 \times 2$ 公式 | $A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ |
| 乘积的逆 | $(AB)^{-1} = B^{-1}A^{-1}$（顺序反转） |

---

## 进度检查点

完成本节后，你应该能够：

- [ ] 识别单位矩阵、对角矩阵、三角矩阵、对称矩阵
- [ ] 计算任意矩阵的转置
- [ ] 利用 $(AB)^T = B^TA^T$ 进行推导
- [ ] 判断一个 $2 \times 2$ 矩阵是否可逆
- [ ] 用公式计算 $2 \times 2$ 矩阵的逆
- [ ] 利用逆矩阵解 $2 \times 2$ 线性方程组

---

## 自测题

**1.** 计算 $\begin{pmatrix} 1 & 3 \\ 2 & 5 \end{pmatrix}^{-1}$。

<details>
<summary>答案</summary>

$\Delta = 1 \cdot 5 - 3 \cdot 2 = -1$。

$$A^{-1} = \frac{1}{-1}\begin{pmatrix} 5 & -3 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} -5 & 3 \\ 2 & -1 \end{pmatrix}$$
</details>

**2.** 若 $A^T = -A$，$A$ 叫什么？它的对角线元素一定是什么？

<details>
<summary>答案</summary>

$A$ 叫**反对称矩阵**（skew-symmetric / antisymmetric matrix）。对角线元素满足 $a_{ii} = -a_{ii}$，所以 $a_{ii} = 0$。
</details>

**3.** 已知 $A^{-1} = \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix}$，求 $A$。

<details>
<summary>答案</summary>

$A = (A^{-1})^{-1}$。$\Delta = 2 \cdot 2 - 1 \cdot 3 = 1$。

$$A = \frac{1}{1}\begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -3 & 2 \end{pmatrix}$$
</details>

---

## 习题引用

本节练习见 [exercises/exercises.md](exercises/exercises.md) 第 §2 部分（第 11–20 题）。
