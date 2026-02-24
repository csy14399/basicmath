# 第 3 章 线性方程组 — 练习题解答 [Bridge]

## §1 Gauss 消元法

**1.** 两式相加：$2x = 6$，$x = 3$，$y = 2$。

---

**2.** $\left(\begin{array}{cc|c} 2 & 1 & 7 \\ 1 & -3 & -2 \end{array}\right) \xrightarrow{R_1 \leftrightarrow R_2} \left(\begin{array}{cc|c} 1 & -3 & -2 \\ 2 & 1 & 7 \end{array}\right) \xrightarrow{R_2 - 2R_1} \left(\begin{array}{cc|c} 1 & -3 & -2 \\ 0 & 7 & 11 \end{array}\right)$

$y = 11/7$，$x = -2 + 3(11/7) = -2 + 33/7 = 19/7$。

---

**3.** $R_1 \leftrightarrow R_2$：$\begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & -2 \\ 3 & 6 & -1 \end{pmatrix}$。

$R_2 \gets R_2 - 2R_1$，$R_3 \gets R_3 - 3R_1$：$\begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & -4 \\ 0 & 0 & -4 \end{pmatrix}$。

$R_3 \gets R_3 - R_2$：$\begin{pmatrix} 1 & 2 & 1 \\ 0 & 0 & -4 \\ 0 & 0 & 0 \end{pmatrix}$。REF 完成。

---

**4.** $\left(\begin{array}{ccc|c} 1 & 1 & 1 & 3 \\ 2 & -1 & 1 & 2 \\ 1 & 2 & -1 & 2 \end{array}\right)$。

$R_2 - 2R_1$，$R_3 - R_1$：$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 3 \\ 0 & -3 & -1 & -4 \\ 0 & 1 & -2 & -1 \end{array}\right)$。

$R_2 \leftrightarrow R_3$：$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 3 \\ 0 & 1 & -2 & -1 \\ 0 & -3 & -1 & -4 \end{array}\right)$。

$R_3 + 3R_2$：$\left(\begin{array}{ccc|c} 1 & 1 & 1 & 3 \\ 0 & 1 & -2 & -1 \\ 0 & 0 & -7 & -7 \end{array}\right)$。

$z = 1$，$y = -1 + 2 = 1$，$x = 3 - 1 - 1 = 1$。解：$x = y = z = 1$。

---

**5.** $\left(\begin{array}{cc|c} 1 & 2 & 1 \\ 3 & 6 & 5 \end{array}\right) \xrightarrow{R_2 - 3R_1} \left(\begin{array}{cc|c} 1 & 2 & 1 \\ 0 & 0 & 2 \end{array}\right)$。

第二行 $0 = 2$，矛盾，**无解**。

---

**6.** 第二行是第一行的 $2$ 倍，第三行是第一行的 $-1$ 倍。

RREF：$\left(\begin{array}{ccc|c} 1 & -1 & 2 & 3 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{array}\right)$。

自由变量 $y = s, z = t$：$x = 3 + s - 2t$。**无穷多解**。

---

**7.** $R_3 - 2R_1$：$\left(\begin{array}{cccc|c} 1 & 2 & 0 & 1 & 3 \\ 0 & 1 & 1 & -1 & 2 \\ 0 & 1 & 1 & -2 & 2 \end{array}\right)$。

$R_3 - R_2$：$\left(\begin{array}{cccc|c} 1 & 2 & 0 & 1 & 3 \\ 0 & 1 & 1 & -1 & 2 \\ 0 & 0 & 0 & -1 & 0 \end{array}\right)$。

$R_3 \gets -R_3$：$\left(\begin{array}{cccc|c} 1 & 2 & 0 & 1 & 3 \\ 0 & 1 & 1 & -1 & 2 \\ 0 & 0 & 0 & 1 & 0 \end{array}\right)$。

$R_2 + R_3$，$R_1 - R_3$：$\left(\begin{array}{cccc|c} 1 & 2 & 0 & 0 & 3 \\ 0 & 1 & 1 & 0 & 2 \\ 0 & 0 & 0 & 1 & 0 \end{array}\right)$。

$R_1 - 2R_2$：$\left(\begin{array}{cccc|c} 1 & 0 & -2 & 0 & -1 \\ 0 & 1 & 1 & 0 & 2 \\ 0 & 0 & 0 & 1 & 0 \end{array}\right)$。RREF。

$x_3 = t$（自由），$x_1 = -1 + 2t$，$x_2 = 2 - t$，$x_4 = 0$。

---

**8.** (a) 不是 RREF。第二行主元为 $2$（应为 $1$）。

(b) 是 RREF。

(c) 是 RREF。

---

**9.** $\left(\begin{array}{cc|c} 1 & 1 & 2 \\ 2 & k & 4 \end{array}\right) \xrightarrow{R_2 - 2R_1} \left(\begin{array}{cc|c} 1 & 1 & 2 \\ 0 & k-2 & 0 \end{array}\right)$。

无穷多解需要第二行为全零行：$k - 2 = 0$，即 $k = 2$。

---

**10.** $R_1 + R_2$：$2x_1 + 2x_2 = 0$，即 $x_1 = -x_2$。$R_1 - R_2$：$2x_3 + 2x_4 = 0$，即 $x_3 = -x_4$。

令 $x_2 = s, x_4 = t$：$(x_1, x_2, x_3, x_4) = s(-1, 1, 0, 0) + t(0, 0, -1, 1)$。

---

## §2 解的结构

**11.** $1 + (-1) + 2 = 2$ ✓，$2(1) - (-1) + 2 = 5$ ✓。

齐次方程 $x+y+z = 0$，$2x-y+z = 0$。$R_2 - 2R_1$：$-3y - z = 0$，$z = -3y$。令 $y = t$：$(x,y,z) = t(-\frac{2}{3}, 1, -3)$，或取 $t=3$：$(2, -3, 9)$... 

重新算：$y = t$，$z = -3t$，$x = -t-z = -t+3t = 2t$。非平凡解：$(2, 1, -3)$。

---

**12.** $R_2 - 2R_1$：$\begin{pmatrix} 1 & 3 \\ 0 & 0 \end{pmatrix}$。$\text{rank}(A) = 1$。

$x_1 + 3x_2 = 0$，$x_1 = -3x_2$。$N(A) = \text{span}\{(-3, 1)\}$。

---

**13.** $R_2 - 2R_1$，$R_3 - R_1$：$\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{pmatrix}$。$R_3 - R_2$：$\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}$。

$\text{rank}(A) = 2$。$A\mathbf{x} = \mathbf{b}$ 有解当且仅当 $\text{rank}(A) = \text{rank}(A|\mathbf{b})$，即 $\mathbf{b}$ 满足 $b_3 = b_2$（第三个方程与第二个相同的约束条件）。更精确地：$b_3 - b_2 = 0$（从消元过程导出）。

实际上：原第三行减第二行为 $(-1, 0, -1 \mid b_3 - b_2)$，加第一行为 $(0, 0, 0 \mid b_3 - b_2 + b_1 - b_2)$... 让我重新做。

$R_3 - R_1$：$(0, 1, 1 \mid b_3 - b_1)$。$R_2 - 2R_1$：$(0, 1, 1 \mid b_2 - 2b_1)$。$R_3 - R_2$ 新：$(0, 0, 0 \mid b_3 - b_1 - b_2 + 2b_1) = (0, 0, 0 \mid b_1 - b_2 + b_3)$。

有解条件：$b_1 - b_2 + b_3 = 0$。

---

**14.** $\text{nullity}(A) = 7 - 4 = 3$。齐次解空间维数为 $3$。

---

**15.** 增广：$\left(\begin{array}{ccc|c} 1 & 1 & -1 & 1 \\ 2 & 1 & 1 & 3 \end{array}\right) \xrightarrow{R_2 - 2R_1} \left(\begin{array}{ccc|c} 1 & 1 & -1 & 1 \\ 0 & -1 & 3 & 1 \end{array}\right)$。

$R_2 \gets -R_2$，$R_1 + R_2'$... RREF：$\left(\begin{array}{ccc|c} 1 & 0 & 2 & 2 \\ 0 & 1 & -3 & -1 \end{array}\right)$。

$z = t$（自由），$x = 2 - 2t$，$y = -1 + 3t$。

$$\mathbf{x} = \begin{pmatrix} 2 \\ -1 \\ 0 \end{pmatrix} + t\begin{pmatrix} -2 \\ 3 \\ 1 \end{pmatrix}$$

---

**16.** $\text{rank}(A) = 3 = n$，满秩。对任意 $\mathbf{b}$ 都有解，且解唯一（$\text{nullity} = 0$，无自由变量）。$A$ 可逆。

---

**17.** 注意第二行是第一行的 $2$ 倍。$R_2 - 2R_1$：全零行。

$$\begin{pmatrix} 1 & -1 & 2 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 1 & -1 & 3 \end{pmatrix} \xrightarrow{R_2 \leftrightarrow R_3} \begin{pmatrix} 1 & -1 & 2 & 1 \\ 0 & 1 & -1 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

$R_1 + R_2$：$\begin{pmatrix} 1 & 0 & 1 & 4 \\ 0 & 1 & -1 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}$。

$\text{rank}(A) = 2$，$\text{nullity} = 2$。自由变量 $x_3 = s, x_4 = t$：

$x_1 = -s - 4t$，$x_2 = s - 3t$。

$N(A) = \text{span}\left\{\begin{pmatrix}-1\\1\\1\\0\end{pmatrix}, \begin{pmatrix}-4\\-3\\0\\1\end{pmatrix}\right\}$。

---

**18.** $\text{rank}(A) \leq m < n$。$\text{nullity}(A) = n - \text{rank}(A) \geq n - m > 0$。

零空间维数 $> 0$，所以必有非平凡解。

---

**19.** 解方程组：$\begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 1 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$。

$y = 0$，$x = -z$。令 $z = t$：$(x,y,z) = t(-1,0,1)$。

解集是过原点沿方向 $(-1,0,1)$ 的**直线**。

---

**20.** $A$ 可逆 $\iff$ $\text{rank}(A) = n$（满秩）。

$(\Rightarrow)$：$A$ 可逆 $\Rightarrow$ $A\mathbf{x} = \mathbf{0}$ 只有 $\mathbf{x} = \mathbf{0}$（两边左乘 $A^{-1}$），$\text{nullity} = 0$，$\text{rank} = n$。

$(\Leftarrow)$：$\text{rank} = n$ $\Rightarrow$ REF 有 $n$ 个主元 $\Rightarrow$ 可继续化为 $I$，意味着存在行变换矩阵 $E$ 使 $EA = I$，$A$ 可逆。
