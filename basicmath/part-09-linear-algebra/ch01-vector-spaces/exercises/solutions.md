# 第 1 章 向量空间 — 练习题解答 [Bridge]

## §1 向量空间的直觉

**1.** $\mathbf{u} + \mathbf{v} = (1+4, -2+0, 3+(-1)) = (5, -2, 2)$。

$3\mathbf{u} - 2\mathbf{v} = (3, -6, 9) + (-8, 0, 2) = (-5, -6, 11)$。

---

**2.** 加法公理：A1（交换律）、A2（结合律）、A3（零元素）、A4（逆元素）。标量乘法公理：S1（结合律）、S2（单位元）。分配律：D1（标量对向量加法）、D2（向量对标量加法）。

---

**3.** 不是子空间。$(1, 0) \in W$，但 $(-1)(1, 0) = (-1, 0) \notin W$（$-1 < 0$），标量乘法不封闭。

---

**4.** 是子空间。

- $\mathbf{0}$：$0 - 0 + 0 = 0$。✓
- 加法封闭：设 $(x_1 - 2y_1 + 3z_1) = 0$ 且 $(x_2 - 2y_2 + 3z_2) = 0$，则 $(x_1+x_2) - 2(y_1+y_2) + 3(z_1+z_2) = 0$。✓
- 标量乘法封闭：$c(x - 2y + 3z) = cx - 2(cy) + 3(cz) = 0$。✓

---

**5.** $W = \{a_0 + a_1 x + a_2 x^2 \in P_2 : a_0 + a_1 + a_2 = 0\}$。

- 零多项式：$0 + 0 + 0 = 0$。✓
- 加法封闭：若 $p(1) = 0$ 且 $q(1) = 0$，则 $(p+q)(1) = p(1) + q(1) = 0$。✓
- 标量乘法封闭：$(cp)(1) = c \cdot p(1) = 0$。✓

---

**6.** $W_1 \cap W_2 = \{(x,y,z) : x+y = 0 \text{ 且 } y+z = 0\}$。

由 $y = -x$ 和 $z = -y = x$，得 $W_1 \cap W_2 = \{(x, -x, x) : x \in \mathbb{R}\} = \text{span}\{(1,-1,1)\}$。

这是过原点的直线，是子空间（也由命题 5 直接得到）。

---

**7.** 若 $\mathbf{v} + W$ 是子空间，则 $\mathbf{0} \in \mathbf{v} + W$，即存在 $\mathbf{w} \in W$ 使得 $\mathbf{v} + \mathbf{w} = \mathbf{0}$，即 $\mathbf{v} = -\mathbf{w} \in W$（因为 $W$ 是子空间，$-\mathbf{w} \in W$）。但 $\mathbf{v} \notin W$，矛盾。

---

**8.** 假设 $c \neq 0$。要证 $\mathbf{v} = \mathbf{0}$。

$c\mathbf{v} = \mathbf{0}$ 两边乘 $c^{-1}$：

$$\mathbf{v} = 1 \cdot \mathbf{v} = (c^{-1} c) \mathbf{v} = c^{-1}(c\mathbf{v}) = c^{-1} \mathbf{0} = \mathbf{0}$$

其中最后一步用了命题 3（$0 \cdot \mathbf{u} = \mathbf{0}$），以及标量 $0$ 等于 $c^{-1} \cdot 0$。

---

**9.** 是子空间。$A^T = A$ 的矩阵形如 $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$。

- 零矩阵对称。✓
- 对称矩阵之和仍对称：$(A+B)^T = A^T + B^T = A + B$。✓
- 标量倍仍对称：$(cA)^T = cA^T = cA$。✓

---

**10.** $(\Leftarrow)$：若 $W_1 \subseteq W_2$，则 $W_1 \cup W_2 = W_2$，是子空间。

$(\Rightarrow)$：反证法。假设 $W_1 \not\subseteq W_2$ 且 $W_2 \not\subseteq W_1$。则存在 $\mathbf{u} \in W_1 \setminus W_2$ 和 $\mathbf{v} \in W_2 \setminus W_1$。

若 $W_1 \cup W_2$ 是子空间，则 $\mathbf{u} + \mathbf{v} \in W_1 \cup W_2$。

- 若 $\mathbf{u} + \mathbf{v} \in W_1$，则 $\mathbf{v} = (\mathbf{u}+\mathbf{v}) - \mathbf{u} \in W_1$（$W_1$ 对减法封闭），矛盾。
- 若 $\mathbf{u} + \mathbf{v} \in W_2$，则 $\mathbf{u} = (\mathbf{u}+\mathbf{v}) - \mathbf{v} \in W_2$，矛盾。

所以 $W_1 \cup W_2$ 不是子空间。

---

## §2 线性无关与基

**11.** $(2, 6) = 2(1, 3)$，所以线性相关（共线），不是线性无关的。

---

**12.** 解 $c_1(1,1,0) + c_2(0,1,1) = (5,7,1)$：

$c_1 = 5$，$c_1 + c_2 = 7 \Rightarrow c_2 = 2$，$c_2 = 1$。

$c_2$ 不一致（$2 \neq 1$），所以 $(5,7,1)$ 不是 $(1,1,0)$ 和 $(0,1,1)$ 的线性组合。

---

**13.** 解 $c_1(1,0,1) + c_2(0,1,1) + c_3(1,1,0) = (0,0,0)$：

$c_1 + c_3 = 0$，$c_2 + c_3 = 0$，$c_1 + c_2 = 0$。

由前两个：$c_1 = -c_3$，$c_2 = -c_3$。代入第三个：$-c_3 + (-c_3) = 0$，即 $c_3 = 0$。则 $c_1 = c_2 = 0$。

只有平凡解，所以**线性无关**。

---

**14.** 由 $2x - y + z = 0$ 得 $y = 2x + z$。令 $x = s, z = t$：

$(x, y, z) = (s, 2s+t, t) = s(1, 2, 0) + t(0, 1, 1)$

$(1, 2, 0)$ 和 $(0, 1, 1)$ 线性无关（不共线），所以 $\{(1, 2, 0), (0, 1, 1)\}$ 是一组基，$\dim W = 2$。

---

**15.** $P_1 = \{a + bx : a, b \in \mathbb{R}\}$，$\dim P_1 = 2$。

线性无关性：$c_1(1-x) + c_2(1+x) = 0$ 给出 $(c_1+c_2) + (-c_1+c_2)x = 0$。

$c_1 + c_2 = 0$ 且 $-c_1 + c_2 = 0$，解得 $c_1 = c_2 = 0$。线性无关。

两个线性无关的向量在 $2$ 维空间中自动构成基。

---

**16.** $(2, 4, 6) = 2(1, 2, 3)$，所以 $\text{span}\{(1,2,3), (2,4,6)\} = \text{span}\{(1,2,3)\}$，维数为 $1$。

---

**17.** 设 $a(\mathbf{v}_1+\mathbf{v}_2) + b(\mathbf{v}_2+\mathbf{v}_3) + c(\mathbf{v}_1+\mathbf{v}_3) = \mathbf{0}$。

整理：$(a+c)\mathbf{v}_1 + (a+b)\mathbf{v}_2 + (b+c)\mathbf{v}_3 = \mathbf{0}$。

由 $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ 线性无关：

$a+c = 0, \quad a+b = 0, \quad b+c = 0$

由前两个：$c = -a, b = -a$。代入第三个：$-a + (-a) = 0$，即 $a = 0$。则 $b = c = 0$。

因此线性无关。

---

**18.** 方程组：$x+y+z+w = 0$ 且 $x-y+z-w = 0$。

两式相加：$2x + 2z = 0$，即 $z = -x$。

两式相减：$2y + 2w = 0$，即 $w = -y$。

令 $x = s, y = t$：$(s, t, -s, -t) = s(1,0,-1,0) + t(0,1,0,-1)$。

$\{(1,0,-1,0), (0,1,0,-1)\}$ 线性无关，$\dim W = 2$。

---

**19.** 不能。$\dim \mathbb{R}^3 = 3$，而基必须有 $3$ 个元素。两个向量即使线性无关，也只能张成一个 $2$ 维子空间（过原点的平面），不能生成整个 $\mathbb{R}^3$。

---

**20.** 反证法。假设 $\mathbf{v}_1, \ldots, \mathbf{v}_n$ 线性相关。则存在不全为零的 $c_i$ 使得 $\sum c_i \mathbf{v}_i = \mathbf{0}$。不妨设 $c_1 \neq 0$，则 $\mathbf{v}_1 = -\frac{c_2}{c_1}\mathbf{v}_2 - \cdots - \frac{c_n}{c_1}\mathbf{v}_n$。

于是 $\text{span}(\mathbf{v}_1, \ldots, \mathbf{v}_n) = \text{span}(\mathbf{v}_2, \ldots, \mathbf{v}_n)$。但 $\text{span}(\mathbf{v}_2, \ldots, \mathbf{v}_n)$ 最多是 $n-1$ 维的。

然而 $\text{span}(\mathbf{v}_1, \ldots, \mathbf{v}_n) = V$，$\dim V = n$。矛盾——一个 $n$ 维空间不能由 $n-1$ 个向量生成。
