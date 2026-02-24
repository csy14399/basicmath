# 第 3 章 线性方程组 — 练习题 [Bridge]

## §1 Gauss 消元法

1. ★☆☆ 解方程组：$\begin{cases} x + y = 5 \\ x - y = 1 \end{cases}$。

2. ★☆☆ 用增广矩阵和行变换解方程组：$\begin{cases} 2x + y = 7 \\ x - 3y = -2 \end{cases}$。

3. ★★☆ 将矩阵化为 REF：$\begin{pmatrix} 2 & 4 & -2 \\ 1 & 2 & 1 \\ 3 & 6 & -1 \end{pmatrix}$。

4. ★★☆ 解方程组：$\begin{cases} x + y + z = 3 \\ 2x - y + z = 2 \\ x + 2y - z = 2 \end{cases}$。

5. ★★☆ 判断方程组是否有解：$\begin{cases} x + 2y = 1 \\ 3x + 6y = 5 \end{cases}$。

6. ★★☆ 解方程组：$\begin{cases} x - y + 2z = 3 \\ 2x - 2y + 4z = 6 \\ -x + y - 2z = -3 \end{cases}$。

7. ★★★ 将增广矩阵 $\left(\begin{array}{cccc|c} 1 & 2 & 0 & 1 & 3 \\ 0 & 1 & 1 & -1 & 2 \\ 2 & 5 & 1 & 0 & 8 \end{array}\right)$ 化为 RREF，并写出通解。

8. ★★☆ 以下矩阵是否为 RREF？如不是，指出违反了哪条规则。

   (a) $\begin{pmatrix} 1 & 0 & 3 \\ 0 & 2 & 1 \end{pmatrix}$ $\quad$ (b) $\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$ $\quad$ (c) $\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}$

9. ★★★ 求 $k$ 的值使得方程组 $\begin{cases} x + y = 2 \\ 2x + ky = 4 \end{cases}$ 有无穷多解。

10. ★★★ 解方程组：$\begin{cases} x_1 + x_2 + x_3 + x_4 = 0 \\ x_1 + x_2 - x_3 - x_4 = 0 \end{cases}$。

---

## §2 解的结构

11. ★☆☆ 验证 $\mathbf{x} = (1, -1, 2)$ 是方程组 $x + y + z = 2$，$2x - y + z = 5$ 的解。写出齐次方程的一个非平凡解。

12. ★★☆ 求矩阵 $A = \begin{pmatrix} 1 & 3 \\ 2 & 6 \end{pmatrix}$ 的秩和零空间的基。

13. ★★☆ 求 $A = \begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 3 \\ 1 & 1 & 2 \end{pmatrix}$ 的秩。$A\mathbf{x} = \mathbf{b}$ 何时有解？

14. ★★☆ 设 $A$ 是 $5 \times 7$ 矩阵，$\text{rank}(A) = 4$。求 $\text{nullity}(A)$ 和齐次解空间的维数。

15. ★★★ 求方程组 $\begin{cases} x + y - z = 1 \\ 2x + y + z = 3 \end{cases}$ 的通解，写成"特解 + 齐次解"的形式。

16. ★★☆ 设 $A$ 是 $3 \times 3$ 矩阵，$\text{rank}(A) = 3$。$A\mathbf{x} = \mathbf{b}$ 对任意 $\mathbf{b}$ 是否都有解？解是否唯一？

17. ★★★ 求矩阵 $A = \begin{pmatrix} 1 & -1 & 2 & 1 \\ 2 & -2 & 4 & 2 \\ 0 & 1 & -1 & 3 \end{pmatrix}$ 的秩和零空间。

18. ★★★ 证明：如果 $A$ 是 $m \times n$ 矩阵且 $m < n$，则齐次方程 $A\mathbf{x} = \mathbf{0}$ 一定有非平凡解。

19. ★★☆ 在 $\mathbb{R}^3$ 中，方程组 $\begin{cases} x + y + z = 0 \\ x - y + z = 0 \end{cases}$ 的解集是什么几何对象？

20. ★★★ 设 $\text{rank}(A) = r$，$A$ 是 $n \times n$ 方阵。$A$ 可逆的充要条件是什么？
