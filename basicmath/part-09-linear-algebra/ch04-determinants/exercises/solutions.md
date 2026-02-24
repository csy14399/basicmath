# 第 4 章 行列式 — 练习题解答 [Bridge]

## §1 行列式

**1.** $4 \times 5 - 3 \times 2 = 20 - 6 = 14$。

---

**2.** $(-1)(-2) - 6 \times 3 = 2 - 18 = -16$。

---

**3.** Sarrus：$1 \cdot 5 \cdot 9 + 2 \cdot 6 \cdot 7 + 3 \cdot 4 \cdot 8 - 3 \cdot 5 \cdot 7 - 2 \cdot 4 \cdot 9 - 1 \cdot 6 \cdot 8$

$= 45 + 84 + 96 - 105 - 72 - 48 = 225 - 225 = 0$。

$\det = 0$，矩阵不可逆（三行构成等差数列，第三行 = $2 \times$ 第二行 $-$ 第一行）。

---

**4.** 按第三行展开（两个零）：

$\det = 0 \cdot C_{31} + 0 \cdot C_{32} + 4 \cdot C_{33} = 4 \begin{vmatrix} 1 & 0 \\ 2 & 1 \end{vmatrix} = 4(1) = 4$。

---

**5.** $\det(2A) = 2^3 \det(A) = 8 \times 4 = 32$。

---

**6.** 交换第一行和第三行需要一次交换（或通过两次相邻交换：先交换第 $1, 2$ 行，再交换第 $2, 3$ 行，再交换第 $1, 2$ 行……但第 $1$ 行和第 $3$ 行的直接交换是一次操作），行列式变号：$\det(B) = -\det(A)$。

注意：严格来说，交换不相邻的两行仍算一次初等行变换，行列式变号一次。

---

**7.** $R_1 \gets R_1 / 2$（行列式乘 $2$，即 $\det = 2 \det'$）：

$$\begin{pmatrix} 1 & 2 & 3 \\ 1 & 3 & 5 \\ 0 & 1 & 2 \end{pmatrix}$$

$R_2 - R_1$：$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{pmatrix}$。

$R_3 - R_2$：$\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{pmatrix}$。

上三角行列式 $= 1 \times 1 \times 0 = 0$。所以 $\det = 2 \times 0 = 0$。

---

**8.** $A^2 = A$ 两边取行列式：$\det(A)^2 = \det(A)$。

$\det(A)^2 - \det(A) = 0$，$\det(A)(\det(A) - 1) = 0$。

所以 $\det(A) = 0$ 或 $\det(A) = 1$。

---

**9.** $\det(A) = 4 - 6 = -2$，$\det(B) = 10 - 0 = 10$。

$AB = \begin{pmatrix} 5 & 7 \\ 10 & 10 \end{pmatrix}$，$\det(AB) = 50 - 70 = -20$。

$\det(A)\det(B) = (-2)(10) = -20 = \det(AB)$。✓

---

**10.** 按第一行展开：

$$\det = 1 \begin{vmatrix} b & c \\ b^2 & c^2 \end{vmatrix} - 1 \begin{vmatrix} a & c \\ a^2 & c^2 \end{vmatrix} + 1 \begin{vmatrix} a & b \\ a^2 & b^2 \end{vmatrix}$$

$$= (bc^2 - cb^2) - (ac^2 - ca^2) + (ab^2 - ba^2)$$

$$= bc(c-b) - ac(c-a) + ab(b-a)$$

$$= (c-b)(c-a)(b-a)$$

整理（按标准顺序）：$\det = (b-a)(c-a)(c-b)$。

这是著名的 **Vandermonde 行列式**。

---

## §2 行列式的应用

**11.** $\det = 2 \times 6 - 3 \times 4 = 12 - 12 = 0$。不可逆。

---

**12.** $\Delta = 2(-2) - 1 \cdot 3 = -7$。

$x = \frac{5(-2)-1\cdot4}{-7} = \frac{-14}{-7} = 2$。

$y = \frac{2 \cdot 4 - 5 \cdot 3}{-7} = \frac{-7}{-7} = 1$。

---

**13.** $\det = k - 6 = 0$，$k = 6$。

---

**14.** $A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$。

$\det(A) = 1(-1-0) - 1(1-0) + 1(1-0) = -1 - 1 + 1 = -1$。

$A_1 = \begin{pmatrix} 6 & 1 & 1 \\ 0 & -1 & 0 \\ 4 & 1 & 1 \end{pmatrix}$。按第二行展开：$\det(A_1) = -(-1)(6-4) = 2$... 

让我仔细计算。$\det(A_1)$ 按 $R_2$ 展开：$0 \cdot C_{21} + (-1) \cdot C_{22} + 0 \cdot C_{23}$。

$C_{22} = (-1)^{2+2}\begin{vmatrix} 6 & 1 \\ 4 & 1 \end{vmatrix} = 6-4 = 2$。

$\det(A_1) = -1 \cdot 2 = -2$。$x = \frac{-2}{-1} = 2$。

$A_2 = \begin{pmatrix} 1 & 6 & 1 \\ 1 & 0 & 0 \\ 0 & 4 & 1 \end{pmatrix}$。按 $R_2$ 展开：$\det(A_2) = 1 \cdot (-1)^{2+1}\begin{vmatrix} 6 & 1 \\ 4 & 1 \end{vmatrix} = -1 \cdot 2 = -2$。$y = \frac{-2}{-1} = 2$。

$A_3 = \begin{pmatrix} 1 & 1 & 6 \\ 1 & -1 & 0 \\ 0 & 1 & 4 \end{pmatrix}$。按 $R_3$：$0 \cdot (\cdots) + 1 \cdot C_{32} + 4 \cdot C_{33}$。

$C_{32} = (-1)^{3+2}\begin{vmatrix} 1 & 6 \\ 1 & 0 \end{vmatrix} = -(0-6) = 6$。

$C_{33} = (-1)^{3+3}\begin{vmatrix} 1 & 1 \\ 1 & -1 \end{vmatrix} = -1-1 = -2$。

$\det(A_3) = 6 + 4(-2) = 6 - 8 = -2$。$z = \frac{-2}{-1} = 2$。

解：$x = y = z = 2$。验证：$2 + 2 + 2 = 6$ ✓，$2 - 2 = 0$ ✓，$2 + 2 = 4$ ✓。

---

**15.** $\det = 3 - 2 = 1$。$A^{-1} = \begin{pmatrix} 3 & -1 \\ -2 & 1 \end{pmatrix}$。

---

**16.** $A^TA = I$，取行列式：$\det(A^T)\det(A) = 1$。由 $\det(A^T) = \det(A)$：$\det(A)^2 = 1$，$\det(A) = \pm 1$。

---

**17.** $\det(R_{90°}) = 0 \cdot 0 - (-1) \cdot 1 = 1$。

单位正方形被旋转 $90°$，仍然是单位正方形（面积不变 = $|\det| = 1$）。

---

**18.** 由 $A \cdot \text{adj}(A) = \det(A) \cdot I$，取行列式：

$\det(A) \cdot \det(\text{adj}(A)) = \det(A)^n$（$n = 4$）。

$3 \cdot \det(\text{adj}(A)) = 3^4 = 81$。$\det(\text{adj}(A)) = 27 = 3^3 = \det(A)^{n-1}$。

---

**19.** $A = \text{diag}(2, 3)$。单位正方形的顶点 $(0,0), (1,0), (1,1), (0,1)$ 映射为 $(0,0), (2,0), (2,3), (0,3)$。

变成 $2 \times 3$ 的矩形，面积 $= 6 = |\det(A)| = |2 \times 3|$。

---

**20.** 用列变换 $C_2 \gets C_2 - C_1$，$C_3 \gets C_3 - C_1$：

$$\begin{vmatrix} 1 & 0 & 0 \\ a & b-a & c-a \\ a^2 & b^2-a^2 & c^2-a^2 \end{vmatrix} = \begin{vmatrix} b-a & c-a \\ b^2-a^2 & c^2-a^2 \end{vmatrix}$$

$$= \begin{vmatrix} b-a & c-a \\ (b-a)(b+a) & (c-a)(c+a) \end{vmatrix}$$

$$= (b-a)(c-a)\begin{vmatrix} 1 & 1 \\ b+a & c+a \end{vmatrix} = (b-a)(c-a)(c+a-b-a) = (b-a)(c-a)(c-b)$$
