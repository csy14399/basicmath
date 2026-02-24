# 第 4 章 行列式 — 练习题 [Bridge]

## §1 行列式

1. ★☆☆ 计算 $\begin{vmatrix} 4 & 3 \\ 2 & 5 \end{vmatrix}$。

2. ★☆☆ 计算 $\begin{vmatrix} -1 & 6 \\ 3 & -2 \end{vmatrix}$。

3. ★★☆ 用 Sarrus 法则计算 $\begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{vmatrix}$。

4. ★★☆ 用余子式展开（按含零最多的行或列）计算 $\begin{vmatrix} 1 & 0 & 3 \\ 2 & 1 & 0 \\ 0 & 0 & 4 \end{vmatrix}$。

5. ★★☆ 设 $\det(A) = 4$。求 $\det(2A)$（$A$ 是 $3 \times 3$ 矩阵）。

6. ★★☆ 设 $A$ 是 $3 \times 3$ 矩阵。如果交换 $A$ 的第一行和第三行得到 $B$，$\det(A)$ 和 $\det(B)$ 的关系是什么？

7. ★★☆ 用行变换计算 $\begin{vmatrix} 2 & 4 & 6 \\ 1 & 3 & 5 \\ 0 & 1 & 2 \end{vmatrix}$。

8. ★★★ 证明：如果 $A$ 是 $n \times n$ 矩阵且 $A^2 = A$，则 $\det(A) = 0$ 或 $\det(A) = 1$。

9. ★★☆ 验证 $\det(AB) = \det(A)\det(B)$，其中 $A = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$，$B = \begin{pmatrix} 5 & 1 \\ 0 & 2 \end{pmatrix}$。

10. ★★★ 计算 $\begin{vmatrix} 1 & 1 & 1 \\ a & b & c \\ a^2 & b^2 & c^2 \end{vmatrix}$（Vandermonde 行列式）。

---

## §2 行列式的应用

11. ★☆☆ 判断矩阵 $\begin{pmatrix} 2 & 3 \\ 4 & 6 \end{pmatrix}$ 是否可逆。

12. ★★☆ 用 Cramer 法则解 $\begin{cases} 2x + y = 5 \\ 3x - 2y = 4 \end{cases}$。

13. ★★☆ 求 $k$ 的值使得 $\begin{pmatrix} 1 & 2 \\ 3 & k \end{pmatrix}$ 不可逆。

14. ★★☆ 用 Cramer 法则解 $\begin{cases} x + y + z = 6 \\ x - y = 0 \\ y + z = 4 \end{cases}$。

15. ★★☆ 用伴随矩阵公式求 $\begin{pmatrix} 1 & 1 \\ 2 & 3 \end{pmatrix}^{-1}$。

16. ★★★ 设 $A$ 是 $3 \times 3$ 正交矩阵（$A^TA = I$）。证明 $\det(A) = \pm 1$。

17. ★★☆ 旋转矩阵 $R_{90°} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ 的行列式是什么？它把单位正方形变成什么？

18. ★★★ 设 $\det(A) = 3$，$A$ 是 $4 \times 4$ 矩阵。求 $\det(\text{adj}(A))$。

19. ★★☆ 矩阵 $A = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$ 把单位正方形变成什么形状？面积是多少？

20. ★★★ 证明 $3 \times 3$ Vandermonde 行列式 $\begin{vmatrix} 1 & 1 & 1 \\ a & b & c \\ a^2 & b^2 & c^2 \end{vmatrix} = (b-a)(c-a)(c-b)$。
