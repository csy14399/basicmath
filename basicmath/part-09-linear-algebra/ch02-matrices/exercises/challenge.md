# 第 2 章 矩阵 — 挑战题（Challenge Problems）[Bridge]

以下挑战题探索矩阵运算的更深层面。

---

## 挑战题 1：矩阵幂的一般公式

> **题目**：设 $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$。
>
> (a) 计算 $A^2, A^3, A^4$。
>
> (b) 猜测并用数学归纳法证明 $A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$。

### 解答

(a) $A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$，$A^3 = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$，$A^4 = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$。

(b) 归纳证明。基始 $n=1$：$A^1 = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$。✓

归纳步：假设 $A^k = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$。则：

$$A^{k+1} = A^k \cdot A = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & k+1 \\ 0 & 1 \end{pmatrix}$$

---

## 挑战题 2：Cayley–Hamilton 定理的 $2 \times 2$ 验证

> **题目**：设 $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$。定义 $A$ 的**特征多项式**为 $p(\lambda) = \lambda^2 - (a+d)\lambda + (ad-bc)$。
>
> 证明 $p(A) = A^2 - (a+d)A + (ad-bc)I = O$（零矩阵）。

### 解答

$A^2 = \begin{pmatrix} a^2+bc & ab+bd \\ ac+cd & bc+d^2 \end{pmatrix}$。

$(a+d)A = \begin{pmatrix} a^2+ad & ab+bd \\ ac+cd & ad+d^2 \end{pmatrix}$。

$(ad-bc)I = \begin{pmatrix} ad-bc & 0 \\ 0 & ad-bc \end{pmatrix}$。

$$A^2 - (a+d)A + (ad-bc)I = \begin{pmatrix} a^2+bc-a^2-ad+ad-bc & 0 \\ 0 & bc+d^2-ad-d^2+ad-bc \end{pmatrix} = O$$

这是 Cayley–Hamilton 定理在 $2 \times 2$ 情形的直接验证。该定理对任意 $n \times n$ 矩阵都成立。

---

## 挑战题 3：矩阵的迹

> **题目**：矩阵 $A$ 的**迹**（trace）定义为 $\text{tr}(A) = \sum_{i=1}^n a_{ii}$（主对角线元素之和）。
>
> (a) 证明 $\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)$。
>
> (b) 证明 $\text{tr}(AB) = \text{tr}(BA)$（即使 $AB \neq BA$）。
>
> (c) 是否有 $\text{tr}(ABC) = \text{tr}(BAC)$？

### 解答

(a) $\text{tr}(A+B) = \sum_i (a_{ii}+b_{ii}) = \sum_i a_{ii} + \sum_i b_{ii} = \text{tr}(A) + \text{tr}(B)$。

(b) $\text{tr}(AB) = \sum_i (AB)_{ii} = \sum_i \sum_j a_{ij}b_{ji}$。

$\text{tr}(BA) = \sum_i (BA)_{ii} = \sum_i \sum_j b_{ij}a_{ji} = \sum_j \sum_i a_{ji}b_{ij}$。

交换求和顺序和哑标记号，两者相等。

(c) 不一定。但 $\text{tr}(ABC) = \text{tr}(BCA) = \text{tr}(CAB)$（循环置换不变），而不一定等于 $\text{tr}(BAC)$。
