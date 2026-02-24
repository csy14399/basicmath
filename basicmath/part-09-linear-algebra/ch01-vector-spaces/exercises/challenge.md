# 第 1 章 向量空间 — 挑战题（Challenge Problems）[Bridge]

以下挑战题深入探讨向量空间的结构，难度超出常规练习。

---

## 挑战题 1：构造非标准向量空间

> **题目**：在 $\mathbb{R}_{>0} = \{x \in \mathbb{R} : x > 0\}$（所有正实数的集合）上，定义"加法"和"标量乘法"为：
>
> $$x \oplus y = xy \quad (\text{通常的乘法}), \qquad c \odot x = x^c \quad (\text{通常的幂运算})$$
>
> 证明 $(\mathbb{R}_{>0}, \oplus, \odot)$ 是一个向量空间。它的零向量和逆元素是什么？维数是多少？

### 提示

逐一验证八条公理。"零向量"不是数字 $0$，而是加法运算 $\oplus$ 下的单位元。

### 解答

**零向量**：需要 $x \oplus e = x$，即 $x \cdot e = x$，所以 $e = 1$。"零向量"是正实数 $1$。

**逆元素**：需要 $x \oplus x' = 1$，即 $x \cdot x' = 1$，所以 $x' = 1/x$。

验证八条公理：

1. $x \oplus y = xy = yx = y \oplus x$。✓
2. $(x \oplus y) \oplus z = (xy)z = x(yz) = x \oplus (y \oplus z)$。✓
3. $x \oplus 1 = x \cdot 1 = x$。✓
4. $x \oplus (1/x) = x \cdot (1/x) = 1$。✓
5. $c \odot (d \odot x) = c \odot x^d = (x^d)^c = x^{cd} = (cd) \odot x$。✓
6. $1 \odot x = x^1 = x$。✓
7. $c \odot (x \oplus y) = (xy)^c = x^c y^c = (c \odot x) \oplus (c \odot y)$。✓
8. $(c+d) \odot x = x^{c+d} = x^c \cdot x^d = (c \odot x) \oplus (d \odot x)$。✓

维数：$\dim = 1$。一组基为 $\{e\}$（任何 $e > 0, e \neq 1$），因为任何 $x > 0$ 可以唯一写为 $x = e^c$（取 $c = \log_e x$），即 $x = c \odot e$。

---

## 挑战题 2：向量空间中的唯一表示

> **题目**：设 $V$ 是向量空间，$\mathbf{v}_1, \ldots, \mathbf{v}_n \in V$。证明：$\{\mathbf{v}_1, \ldots, \mathbf{v}_n\}$ 是 $V$ 的基当且仅当 $V$ 中每个向量都可以**唯一地**表示为 $\mathbf{v}_1, \ldots, \mathbf{v}_n$ 的线性组合。

### 解答

$(\Rightarrow)$：已在正文定理 2 中证明。

$(\Leftarrow)$：假设每个向量都能唯一表示。

- **生成**：每个向量至少能表示一次，所以 $\text{span}(\mathbf{v}_1, \ldots, \mathbf{v}_n) = V$。
- **线性无关**：$\mathbf{0} = 0\mathbf{v}_1 + \cdots + 0\mathbf{v}_n$（全零系数）。由唯一性，这是 $\mathbf{0}$ 的唯一表示，所以 $c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n = \mathbf{0}$ 蕴含所有 $c_i = 0$。

---

## 挑战题 3：子空间的和

> **题目**：设 $W_1, W_2$ 是 $V$ 的子空间。定义 $W_1 + W_2 = \{\mathbf{w}_1 + \mathbf{w}_2 : \mathbf{w}_1 \in W_1, \mathbf{w}_2 \in W_2\}$。
>
> (a) 证明 $W_1 + W_2$ 是 $V$ 的子空间。
>
> (b) 证明维数公式：$\dim(W_1 + W_2) = \dim W_1 + \dim W_2 - \dim(W_1 \cap W_2)$。

### 解答

**(a)** $\mathbf{0} = \mathbf{0} + \mathbf{0} \in W_1 + W_2$。

设 $\mathbf{u} = \mathbf{w}_1 + \mathbf{w}_2$，$\mathbf{v} = \mathbf{w}_1' + \mathbf{w}_2' \in W_1 + W_2$。则 $\mathbf{u} + \mathbf{v} = (\mathbf{w}_1 + \mathbf{w}_1') + (\mathbf{w}_2 + \mathbf{w}_2')$，其中 $\mathbf{w}_1 + \mathbf{w}_1' \in W_1$，$\mathbf{w}_2 + \mathbf{w}_2' \in W_2$。✓

$c\mathbf{u} = c\mathbf{w}_1 + c\mathbf{w}_2 \in W_1 + W_2$。✓

**(b)** 设 $\dim(W_1 \cap W_2) = r$，$\dim W_1 = m$，$\dim W_2 = n$。

取 $W_1 \cap W_2$ 的一组基 $\{\mathbf{a}_1, \ldots, \mathbf{a}_r\}$。将其扩展为 $W_1$ 的基 $\{\mathbf{a}_1, \ldots, \mathbf{a}_r, \mathbf{b}_1, \ldots, \mathbf{b}_{m-r}\}$ 和 $W_2$ 的基 $\{\mathbf{a}_1, \ldots, \mathbf{a}_r, \mathbf{c}_1, \ldots, \mathbf{c}_{n-r}\}$。

可以证明 $\{\mathbf{a}_1, \ldots, \mathbf{a}_r, \mathbf{b}_1, \ldots, \mathbf{b}_{m-r}, \mathbf{c}_1, \ldots, \mathbf{c}_{n-r}\}$ 是 $W_1 + W_2$ 的基（需要验证线性无关性和生成性）。

因此 $\dim(W_1 + W_2) = r + (m-r) + (n-r) = m + n - r$。
