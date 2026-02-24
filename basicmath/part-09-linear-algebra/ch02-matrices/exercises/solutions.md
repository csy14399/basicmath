# 第 2 章 矩阵 — 练习题解答 [Bridge]

## §1 矩阵运算

**1.** $A + B = \begin{pmatrix} 5 & -1 \\ 2 & 2 \end{pmatrix}$，$A - B = \begin{pmatrix} -3 & -3 \\ 4 & -2 \end{pmatrix}$，$3A = \begin{pmatrix} 3 & -6 \\ 9 & 0 \end{pmatrix}$。

---

**2.** $AB = \begin{pmatrix} 1\cdot5+2\cdot7 & 1\cdot6+2\cdot8 \\ 3\cdot5+4\cdot7 & 3\cdot6+4\cdot8 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$。

$BA = \begin{pmatrix} 5\cdot1+6\cdot3 & 5\cdot2+6\cdot4 \\ 7\cdot1+8\cdot3 & 7\cdot2+8\cdot4 \end{pmatrix} = \begin{pmatrix} 23 & 34 \\ 31 & 46 \end{pmatrix}$。

$AB \neq BA$。

---

**3.** $A$ 是 $2\times3$，$B$ 是 $3\times2$。

$AB = \begin{pmatrix} 1\cdot2+0\cdot0+2\cdot1 & 1\cdot1+0\cdot(-1)+2\cdot3 \\ 3\cdot2+1\cdot0+(-1)\cdot1 & 3\cdot1+1\cdot(-1)+(-1)\cdot3 \end{pmatrix} = \begin{pmatrix} 4 & 7 \\ 5 & -1 \end{pmatrix}$。

$BA$：$B$ 是 $3\times2$，$A$ 是 $2\times3$，所以 $BA$ 是 $3\times3$ 矩阵。

$BA = \begin{pmatrix} 2+3 & 0+1 & 4-1 \\ 0-3 & 0-1 & 0+1 \\ 1+9 & 0+3 & 2-3 \end{pmatrix} = \begin{pmatrix} 5 & 1 & 3 \\ -3 & -1 & 1 \\ 10 & 3 & -1 \end{pmatrix}$。

---

**4.** $A^2 = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$，$A^3 = \begin{pmatrix} 1 & 6 \\ 0 & 1 \end{pmatrix}$。

规律：$A^n = \begin{pmatrix} 1 & 2n \\ 0 & 1 \end{pmatrix}$。

---

**5.** $A$ 的列为 $\mathbf{a}_1 = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$，$\mathbf{a}_2 = \begin{pmatrix} -1 \\ 3 \end{pmatrix}$。

$A\mathbf{x} = x \mathbf{a}_1 + y \mathbf{a}_2 = x\begin{pmatrix} 2 \\ 1 \end{pmatrix} + y\begin{pmatrix} -1 \\ 3 \end{pmatrix} = \begin{pmatrix} 5 \\ 10 \end{pmatrix}$。

---

**6.** $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$，$B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$。

$AB = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = O$，但 $A \neq O$，$B \neq O$。

---

**7.** $(AI_n)_{ij} = \sum_{k=1}^n a_{ik}(I_n)_{kj} = \sum_{k=1}^n a_{ik}\delta_{kj} = a_{ij}$。

其中 $\delta_{kj}$ 是 Kronecker delta（$k=j$ 时为 $1$，否则为 $0$）。所以 $AI_n = A$。$I_mA = A$ 类似。

---

**8.** $\theta = 90° = \pi/2$。$\begin{pmatrix} \cos 90° & -\sin 90° \\ \sin 90° & \cos 90° \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$。

$\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$，$\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 3 \\ 4 \end{pmatrix} = \begin{pmatrix} -4 \\ 3 \end{pmatrix}$。

---

**9.** 不必然。反例：$A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$，$B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$。

$AB = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$（非零！），但 $BA = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = O$。

等等，这里 $AB \neq O$。换一个：$A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$，$B = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$。

$AB = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = O$，$BA = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \neq O$。

所以 $AB = O$ 不蕴含 $BA = O$。

---

**10.** 设 $N = \{\mathbf{x} \in \mathbb{R}^n : A\mathbf{x} = \mathbf{0}\}$（零空间/核）。

- $A\mathbf{0} = \mathbf{0}$，所以 $\mathbf{0} \in N$。
- 若 $\mathbf{x}, \mathbf{y} \in N$，则 $A(\mathbf{x}+\mathbf{y}) = A\mathbf{x} + A\mathbf{y} = \mathbf{0} + \mathbf{0} = \mathbf{0}$。
- 若 $\mathbf{x} \in N$，$c \in \mathbb{R}$，则 $A(c\mathbf{x}) = c(A\mathbf{x}) = c\mathbf{0} = \mathbf{0}$。

---

## §2 特殊矩阵

**11.** $\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}$，$\begin{pmatrix} 1 & 2 \\ 0 & 3 \\ -1 & 5 \end{pmatrix}$。

---

**12.** $\Delta = 2\cdot3 - 5\cdot1 = 1$。$A^{-1} = \begin{pmatrix} 3 & -5 \\ -1 & 2 \end{pmatrix}$。

---

**13.** $\Delta = 6\cdot2 - 4\cdot3 = 0$。不可逆。

---

**14.** $(A^T)^T = \left(\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}\right)^T = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = A$。✓

$A^TA = \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 10 & 14 \\ 14 & 20 \end{pmatrix}$。这是对称矩阵。✓

---

**15.** $A = \begin{pmatrix} 2 & 5 \\ 1 & 3 \end{pmatrix}$，$\Delta = 1$。$A^{-1} = \begin{pmatrix} 3 & -5 \\ -1 & 2 \end{pmatrix}$。

$\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 3 & -5 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} -7 \\ 3 \end{pmatrix}$。

验证：$2(-7)+5(3) = 1$。✓ $(-7)+3(3) = 2$。✓

---

**16.** $D^2 = \text{diag}(4, 9, 25)$。$D^{-1} = \text{diag}(1/2, -1/3, 1/5)$。

---

**17.** $(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I$。

$(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1}IB = B^{-1}B = I$。

所以 $B^{-1}A^{-1}$ 是 $AB$ 的逆。

---

**18.** $(A^2)^T = (AA)^T = A^TA^T = AA = A^2$（用了 $A^T = A$）。所以 $A^2$ 对称。

---

**19.** $A\mathbf{x} = A\mathbf{y}$ 两边左乘 $A^{-1}$：$A^{-1}(A\mathbf{x}) = A^{-1}(A\mathbf{y})$，即 $I\mathbf{x} = I\mathbf{y}$，即 $\mathbf{x} = \mathbf{y}$。

---

**20.** $(I-A)^2 = I - 2A + A^2 = I - 2A + A = I - A$。所以 $I-A$ 幂等。

$(I-A)A = A - A^2 = A - A = O$。
