# 第 4 章 行列式 — 挑战题（Challenge Problems）[Bridge]

---

## 挑战题 1：行列式的递推

> **题目**：设 $D_n = \begin{vmatrix} 2 & 1 & 0 & \cdots & 0 \\ 1 & 2 & 1 & \cdots & 0 \\ 0 & 1 & 2 & \cdots & 0 \\ \vdots & & \ddots & \ddots & 1 \\ 0 & 0 & \cdots & 1 & 2 \end{vmatrix}_{n \times n}$
>
> (a) 计算 $D_1, D_2, D_3$。
>
> (b) 证明递推公式 $D_n = 2D_{n-1} - D_{n-2}$。
>
> (c) 求 $D_n$ 的通项公式。

### 解答

(a) $D_1 = 2$，$D_2 = 4 - 1 = 3$，$D_3 = 2 \cdot 3 - 2 = 4$。

(b) 按第一行展开：

$$D_n = 2 \cdot D_{n-1} - 1 \cdot \begin{vmatrix} 1 & 1 & 0 & \cdots \\ 0 & 2 & 1 & \cdots \\ \vdots & & \ddots & \\ 0 & \cdots & 1 & 2 \end{vmatrix}$$

右边的行列式按第一列展开得 $1 \cdot D_{n-2}$。

所以 $D_n = 2D_{n-1} - D_{n-2}$。

(c) 特征方程 $r^2 = 2r - 1$，$(r-1)^2 = 0$，$r = 1$（重根）。

通解 $D_n = (A + Bn) \cdot 1^n = A + Bn$。

$D_1 = A + B = 2$，$D_2 = A + 2B = 3$。解得 $B = 1$，$A = 1$。

$$D_n = n + 1$$

---

## 挑战题 2：行列式与面积的推广

> **题目**：三角形的三个顶点为 $(x_1, y_1)$, $(x_2, y_2)$, $(x_3, y_3)$。证明三角形的面积为：
>
> $$S = \frac{1}{2}\left|\begin{vmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{vmatrix}\right|$$

### 解答

以 $(x_1, y_1)$ 为原点，两条边的向量为 $\mathbf{u} = (x_2 - x_1, y_2 - y_1)$，$\mathbf{v} = (x_3 - x_1, y_3 - y_1)$。

三角形面积 = $\frac{1}{2} |\mathbf{u} \times \mathbf{v}|$（平行四边形面积的一半）：

$$2S = |(x_2 - x_1)(y_3 - y_1) - (x_3 - x_1)(y_2 - y_1)|$$

另一方面，对行列式做列变换 $C_1 \gets C_1 - x_1 C_3$，$C_2 \gets C_2 - y_1 C_3$：

$$\begin{vmatrix} 0 & 0 & 1 \\ x_2-x_1 & y_2-y_1 & 1 \\ x_3-x_1 & y_3-y_1 & 1 \end{vmatrix}$$

按第一行展开：$1 \cdot \begin{vmatrix} x_2-x_1 & y_2-y_1 \\ x_3-x_1 & y_3-y_1 \end{vmatrix} = (x_2-x_1)(y_3-y_1) - (y_2-y_1)(x_3-x_1)$。

取绝对值除以 $2$ 得面积公式。

---

## 挑战题 3：行列式的微分

> **题目**：设 $f(t) = \begin{vmatrix} 1 & t \\ t & 1 \end{vmatrix}$。
>
> (a) 求 $f(t)$ 的表达式。
>
> (b) 求 $f'(t)$。
>
> (c) 对于什么 $t$ 值，对应的矩阵不可逆？此时 $f(t)$ 有什么特征？

### 解答

(a) $f(t) = 1 - t^2$。

(b) $f'(t) = -2t$。

(c) $f(t) = 0$ 时不可逆，即 $t = \pm 1$。此时 $f(t)$ 过零点——行列式从正变负（或反之），几何上矩阵从保持方向变为翻转方向。

在 $t = 0$ 时 $f(0) = 1$（矩阵就是 $I$），$f'(0) = 0$——行列式对 $t$ 的变化最不敏感。
