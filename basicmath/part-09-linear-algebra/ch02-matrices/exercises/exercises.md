# 第 2 章 矩阵 — 练习题 [Bridge]

## §1 矩阵运算

1. ★☆☆ 设 $A = \begin{pmatrix} 1 & -2 \\ 3 & 0 \end{pmatrix}$，$B = \begin{pmatrix} 4 & 1 \\ -1 & 2 \end{pmatrix}$。计算 $A + B$，$A - B$，$3A$。

2. ★☆☆ 设 $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$，$B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$。计算 $AB$ 和 $BA$，验证 $AB \neq BA$。

3. ★★☆ 设 $A = \begin{pmatrix} 1 & 0 & 2 \\ 3 & 1 & -1 \end{pmatrix}$，$B = \begin{pmatrix} 2 & 1 \\ 0 & -1 \\ 1 & 3 \end{pmatrix}$。计算 $AB$。$BA$ 能计算吗？如果能，计算之。

4. ★★☆ 设 $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$。计算 $A^2 = AA$ 和 $A^3 = A^2 A$。观察规律并猜测 $A^n$ 的公式。

5. ★★☆ 设 $A\mathbf{x} = \mathbf{b}$，其中 $A = \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix}$，$\mathbf{b} = \begin{pmatrix} 5 \\ 10 \end{pmatrix}$。把 $A\mathbf{x}$ 写成 $A$ 的列向量的线性组合形式。

6. ★★☆ 构造两个 $2 \times 2$ 非零矩阵 $A, B$，使得 $AB = O$（零矩阵）。

7. ★★★ 设 $A$ 是 $m \times n$ 矩阵。证明 $AI_n = A$ 和 $I_m A = A$。

8. ★★☆ 写出 $\mathbb{R}^2$ 中绕原点逆时针旋转 $90°$ 对应的矩阵，并用它计算 $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$ 和 $\begin{pmatrix} 3 \\ 4 \end{pmatrix}$ 的像。

9. ★★★ 设 $A, B$ 是 $n \times n$ 矩阵，且 $AB = O$。是否必然 $BA = O$？给出证明或反例。

10. ★★★ 证明：如果 $A$ 是 $m \times n$ 矩阵，则 $A\mathbf{x} = \mathbf{0}$ 的解集是 $\mathbb{R}^n$ 的子空间。

---

## §2 特殊矩阵

11. ★☆☆ 计算 $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}^T$ 和 $\begin{pmatrix} 1 & 0 & -1 \\ 2 & 3 & 5 \end{pmatrix}^T$。

12. ★☆☆ 求矩阵 $A = \begin{pmatrix} 2 & 5 \\ 1 & 3 \end{pmatrix}$ 的逆矩阵。

13. ★★☆ 判断 $A = \begin{pmatrix} 6 & 4 \\ 3 & 2 \end{pmatrix}$ 是否可逆。

14. ★★☆ 设 $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$。验证 $(A^T)^T = A$ 和 $A^TA$ 是对称矩阵。

15. ★★☆ 用逆矩阵解方程组 $\begin{cases} 2x + 5y = 1 \\ x + 3y = 2 \end{cases}$。

16. ★★☆ 设 $D = \text{diag}(2, -3, 5)$。计算 $D^2$ 和 $D^{-1}$。

17. ★★★ 证明：若 $A$ 和 $B$ 都可逆（且大小相同），则 $AB$ 可逆，且 $(AB)^{-1} = B^{-1}A^{-1}$。

18. ★★★ 设 $A$ 是 $n \times n$ 对称矩阵。证明 $A^2$ 也是对称矩阵。

19. ★★☆ 设 $A$ 可逆且 $A\mathbf{x} = A\mathbf{y}$。证明 $\mathbf{x} = \mathbf{y}$（可逆矩阵的消去律）。

20. ★★★ 设 $A$ 是 $n \times n$ 矩阵，满足 $A^2 = A$（称为**幂等矩阵**，idempotent matrix）。证明 $I - A$ 也是幂等矩阵，且 $(I-A)A = O$。
