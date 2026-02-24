# 第 3 章 线性方程组 — 挑战题（Challenge Problems）[Bridge]

---

## 挑战题 1：消元法的矩阵分解解读

> **题目**：设 $A = \begin{pmatrix} 2 & 1 \\ 6 & 4 \end{pmatrix}$。
>
> (a) 用 Gauss 消元将 $A$ 化为上三角矩阵 $U$。
>
> (b) 将消元过程中的倍加操作记录为下三角矩阵 $L$，验证 $A = LU$。

### 解答

(a) $R_2 \gets R_2 - 3R_1$：$U = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$。

(b) 消元中对 $R_2$ 减去了 $3$ 倍的 $R_1$。记录乘数 $l_{21} = 3$：

$$L = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$$

验证：$LU = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}\begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 6 & 4 \end{pmatrix} = A$。✓

这就是 **LU 分解**——Gauss 消元的矩阵形式。

---

## 挑战题 2：含参数的方程组

> **题目**：讨论方程组的解随参数 $k$ 的变化：
>
> $$\begin{cases} x + y + z = 1 \\ x + 2y + kz = 2 \\ x + y + k^2z = k \end{cases}$$

### 解答

增广矩阵：$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 1 & 2 & k & 2 \\ 1 & 1 & k^2 & k \end{array}\right)$。

$R_2 - R_1$，$R_3 - R_1$：

$$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\ 0 & 1 & k-1 & 1 \\ 0 & 0 & k^2-1 & k-1 \end{array}\right)$$

$k^2 - 1 = (k-1)(k+1)$。

**情形 1**：$k \neq \pm 1$。三个主元，唯一解。

第三行：$(k-1)(k+1)z = k-1$，$z = \frac{1}{k+1}$。

$y = 1 - (k-1) \cdot \frac{1}{k+1} = 1 - \frac{k-1}{k+1} = \frac{2}{k+1}$。

$x = 1 - y - z = 1 - \frac{2}{k+1} - \frac{1}{k+1} = 1 - \frac{3}{k+1} = \frac{k-2}{k+1}$。

**情形 2**：$k = 1$。第三行变为 $0 = 0$，第二行为 $y = 1$。$z = t$（自由），$x = -t$。无穷多解。

**情形 3**：$k = -1$。第三行变为 $0 = -2$，矛盾。无解。

---

## 挑战题 3：秩的不等式

> **题目**：设 $A$ 是 $m \times n$ 矩阵，$B$ 是 $n \times p$ 矩阵。证明：
>
> $$\text{rank}(AB) \leq \min(\text{rank}(A), \text{rank}(B))$$

### 解答

**$\text{rank}(AB) \leq \text{rank}(A)$**：$AB$ 的列空间是 $A$ 的列空间的子空间（因为 $AB$ 的每一列是 $A$ 的列的线性组合）。子空间的维数 $\leq$ 母空间的维数。

**$\text{rank}(AB) \leq \text{rank}(B)$**：$N(B) \subseteq N(AB)$（若 $B\mathbf{x} = \mathbf{0}$，则 $AB\mathbf{x} = \mathbf{0}$）。

由秩-零度定理：$\text{nullity}(B) \leq \text{nullity}(AB)$。

$p - \text{rank}(B) \leq p - \text{rank}(AB)$，即 $\text{rank}(AB) \leq \text{rank}(B)$。
