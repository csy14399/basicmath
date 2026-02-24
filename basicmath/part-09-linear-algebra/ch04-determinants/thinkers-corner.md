# 第 4 章 行列式 — 思考者角落（Thinker's Corner）[Bridge]

> 本节超越教材核心内容，展望行列式连接的更广阔数学世界。

---

## 1. 特征值预览：行列式的"光谱"

在大学线性代数中，一个核心问题是：对于方阵 $A$，存在哪些标量 $\lambda$ 和非零向量 $\mathbf{v}$，使得

$$A\mathbf{v} = \lambda \mathbf{v}$$

这样的 $\lambda$ 称为**特征值**（eigenvalue），$\mathbf{v}$ 称为**特征向量**（eigenvector）。

这个方程等价于 $(A - \lambda I)\mathbf{v} = \mathbf{0}$ 有非平凡解，即

$$\det(A - \lambda I) = 0$$

这个方程叫做**特征方程**（characteristic equation），$\det(A - \lambda I)$ 是一个关于 $\lambda$ 的 $n$ 次多项式——称为**特征多项式**。

**行列式在这里扮演了关键角色**——它把"矩阵的本征性质"转化为"多项式的根"。

对于 $2 \times 2$ 矩阵 $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$：

$$\det(A - \lambda I) = (a-\lambda)(d-\lambda) - bc = \lambda^2 - (a+d)\lambda + (ad-bc)$$

$$= \lambda^2 - \text{tr}(A) \lambda + \det(A)$$

特征值的和 = $\text{tr}(A)$（迹），特征值的积 = $\det(A)$（行列式）！

---

## 2. Google PageRank：线性代数改变世界

Google 搜索引擎的核心算法 **PageRank** 可以用线性代数精确描述。

互联网上的 $n$ 个网页构成一个有向图。定义 $n \times n$ 转移矩阵 $M$，其中 $M_{ij}$ 表示从网页 $j$ 跳转到网页 $i$ 的概率。

PageRank 向量 $\mathbf{r}$ 是 $M$ 的**特征值 $1$ 对应的特征向量**：

$$M\mathbf{r} = \mathbf{r}$$

即 $\mathbf{r}$ 是方程 $(M - I)\mathbf{r} = \mathbf{0}$ 的非平凡解。$\det(M - I) = 0$ 保证了这个解的存在。

实际的 PageRank 算法用**幂迭代法**（power iteration）——反复用矩阵乘以向量——来逼近这个特征向量，无需显式计算行列式或求逆矩阵。但行列式的理论保证了解的存在性。

---

## 3. 机器学习中的行列式

### 高斯分布与行列式

多元高斯分布（multivariate Gaussian distribution）的概率密度函数为：

$$f(\mathbf{x}) = \frac{1}{(2\pi)^{n/2} |\det(\Sigma)|^{1/2}} \exp\!\left(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^T \Sigma^{-1} (\mathbf{x}-\boldsymbol{\mu})\right)$$

其中 $\Sigma$ 是**协方差矩阵**，$\det(\Sigma)$ 出现在归一化常数中——它度量数据的"散布体积"。

### Fisher 判别分析

Fisher 线性判别分析（LDA）的优化目标涉及两个矩阵的行列式之比：

$$\max_{\mathbf{w}} \frac{|\mathbf{w}^T S_B \mathbf{w}|}{|\mathbf{w}^T S_W \mathbf{w}|}$$

其中 $S_B$ 是类间散布矩阵，$S_W$ 是类内散布矩阵。这是一个**广义特征值问题**——行列式帮助我们找到最佳的分类方向。

---

## 4. 行列式的深层数学

### 外代数与微分形式

行列式的多线性和交替性质可以推广为**外代数**（exterior algebra）的理论。在这个框架中，行列式是**最高次外积**（top exterior product）。

微分几何中的**微分形式**（differential forms）就是外代数的推广——它们定义了流形上的"体积"概念。多变量微积分中的换元公式 $dx\,dy = |J| \, du\,dv$（其中 $J$ 是 Jacobian 行列式）就是这个理论的一个特例。

### Leibniz 公式

行列式有一个用置换群（permutation group）表述的完全展开式：

$$\det(A) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^n a_{i,\sigma(i)}$$

其中 $S_n$ 是 $n$ 个元素的所有排列，$\text{sgn}(\sigma)$ 是排列的符号（$+1$ 或 $-1$）。这个公式将行列式与**群论**（group theory）联系起来——线性代数与抽象代数在此交汇。

---

## 5. 行列式的历史

行列式的历史比矩阵更早！

- **关孝和**（日本，1683）和 **Leibniz**（德国，1693）独立地引入了行列式来研究方程组。
- **Cramer**（瑞士，1750）给出了用行列式解方程组的法则。
- **Cauchy**（法国，1812–1815）系统发展了行列式理论。
- **Cayley**（英国，1858）引入了"矩阵"的概念——比行列式晚了一百多年！

有趣的是，中国古代《九章算术》（约公元 1 世纪）的"方程"章中已有消元法的雏形，但没有明确提出行列式的概念。
