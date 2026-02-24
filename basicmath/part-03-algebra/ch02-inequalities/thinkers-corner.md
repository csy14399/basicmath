# 第 2 章 不等式 — 思考者角落（Thinker's Corner）

> 本节超越教材的核心内容，探索不等式在更广阔的数学世界中的角色。这里没有考试，只有好奇心。

---

## 1. 不等式与优化——从代数到变分法

### 从有限到无穷

本章中的 AM-GM 和 Cauchy-Schwarz 不等式处理的是**有限个**变量的优化问题。但许多最深刻的优化问题涉及**无穷维**的对象——函数。

**等周问题**（isoperimetric problem）是最古老的优化问题之一：

> 在所有具有给定周长 $L$ 的封闭曲线中，哪一条围出的面积最大？

答案是**圆**（面积 $A = \frac{L^2}{4\pi}$）。这就是**等周不等式**（isoperimetric inequality）：

$$4\pi A \leq L^2$$

### 等周不等式的一个代数证明思路

对于多边形，等周不等式可以用 AM-GM 不等式的精神来理解：

1. 给定周长的正 $n$ 边形的面积大于任何其他等周长的 $n$ 边形（可以用 AM-GM 论证：边长均匀分布时面积最大）。
2. 正 $n$ 边形的面积 $A_n = \frac{ns^2}{4}\cot\frac{\pi}{n}$（$s = L/n$），当 $n \to \infty$ 时趋向于 $\frac{L^2}{4\pi}$——即圆的面积。

这个从离散到连续的极限过程，正是**变分法**（calculus of variations）的精髓：在函数空间中寻找极值。

### 变分法的诞生

1696 年，Johann Bernoulli 提出了著名的**最速降线问题**（brachistochrone problem）：

> 在重力作用下，一颗珠子沿什么曲线从 $A$ 点滑到 $B$ 点最快？

答案是**摆线**（cycloid）。Newton、Leibniz、L'Hôpital、Jakob Bernoulli 都给出了解答。这个问题催生了变分法——一种在"函数的函数"（泛函）中寻找极值的数学理论。

变分法的核心方程——**Euler-Lagrange 方程**——本质上是一个关于函数的"不等式"条件：极值函数必须满足某个微分方程。

---

## 2. 不等式的层级——从 AM-GM 到 Sobolev

数学中有一个不等式的"层级结构"，从最基本的到最深刻的：

### 第一层：代数不等式

- **AM-GM**：$\frac{a+b}{2} \geq \sqrt{ab}$
- **Cauchy-Schwarz**：$(\sum a_ib_i)^2 \leq (\sum a_i^2)(\sum b_i^2)$
- **幂平均不等式**：QM $\geq$ AM $\geq$ GM $\geq$ HM

这些不等式只涉及有限个实数，用纯代数方法即可证明。

### 第二层：积分不等式

- **Cauchy-Schwarz 积分形式**：$\left(\int fg\right)^2 \leq \int f^2 \cdot \int g^2$
- **Hölder 不等式**：$\int |fg| \leq \left(\int |f|^p\right)^{1/p}\left(\int |g|^q\right)^{1/q}$（$\frac{1}{p} + \frac{1}{q} = 1$）
- **Minkowski 不等式**：$\left(\int |f+g|^p\right)^{1/p} \leq \left(\int |f|^p\right)^{1/p} + \left(\int |g|^p\right)^{1/p}$

这些是代数不等式的"连续版本"，需要积分理论。

### 第三层：泛函不等式

- **Poincaré 不等式**：$\int |f|^2 \leq C\int |\nabla f|^2$（函数的大小被其梯度控制）
- **Sobolev 不等式**：$\|f\|_{L^q} \leq C\|\nabla f\|_{L^p}$
- **等周不等式的分析版本**

这些不等式联系了函数的不同"规模"（norm），是偏微分方程和几何分析的核心工具。

### 贯穿各层的主题

从 AM-GM 到 Sobolev 不等式，有一个共同的主题：**对称性与极值**。AM-GM 的等号条件是"各变量相等"（最对称）；等周不等式的等号条件是"圆"（最对称的封闭曲线）；Sobolev 不等式的最佳常数往往由最对称的函数（如高斯函数）达到。

这个模式——**最对称的配置给出极值**——是数学中反复出现的深层原理。

---

## 3. 信息论中的不等式

### 从物理到信息

Claude Shannon 在 1948 年创立信息论时，定义了**熵**（entropy）：

$$H(X) = -\sum_{i=1}^n p_i \log p_i$$

其中 $p_1, \ldots, p_n$ 是一个概率分布。熵衡量的是一个随机变量的"不确定性"。

### 最大熵原理

Jensen 不等式直接给出一个基本结果：

> **定理**：在所有取 $n$ 个值的离散概率分布中，**均匀分布** $p_i = \frac{1}{n}$ 具有最大熵。

**证明**：$\log$ 是凹函数。由 Jensen 不等式：

$$H(X) = -\sum p_i \log p_i = \sum p_i \log\frac{1}{p_i} \leq \log\left(\sum p_i \cdot \frac{1}{p_i}\right) = \log n$$

等号当所有 $\frac{1}{p_i}$ 相等，即 $p_i = \frac{1}{n}$。$\blacksquare$

最大熵 $H_{\max} = \log n$。这在直觉上完全合理：当所有结果等可能时，不确定性最大。

### Gibbs 不等式与 KL 散度

信息论中另一个核心不等式是 **Gibbs 不等式**：

$$-\sum p_i \log p_i \leq -\sum p_i \log q_i$$

其中 $(p_i)$ 和 $(q_i)$ 是两个概率分布。等价地：

$$D_{KL}(P \| Q) = \sum p_i \log\frac{p_i}{q_i} \geq 0$$

这里 $D_{KL}$ 是 **Kullback-Leibler 散度**（KL divergence），衡量两个概率分布的"距离"。Gibbs 不等式说这个"距离"总是非负的——它是 Jensen 不等式（$-\log$ 是凸函数）的直接推论。

KL 散度在机器学习中无处不在：它是损失函数（如交叉熵损失）的理论基础。

---

## 4. 物理学中的不等式

### 不确定性原理

量子力学中最著名的不等式是 **Heisenberg 不确定性原理**（Heisenberg uncertainty principle）：

$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

其中 $\Delta x$ 和 $\Delta p$ 分别是位置和动量的标准差，$\hbar$ 是约化普朗克常数。

这个不等式的数学证明正是 **Cauchy-Schwarz 不等式**在 $L^2$ 空间中的应用！更准确地说，它来自于一个一般性的结果：对两个不对易的算子 $\hat{A}$ 和 $\hat{B}$，

$$\sigma_A \sigma_B \geq \frac{1}{2}|\langle[\hat{A}, \hat{B}]\rangle|$$

其中 $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ 是对易子。

从 AM-GM 到 Heisenberg 不确定性原理——同一个数学结构（Cauchy-Schwarz/AM-GM 型不等式）在完全不同的语境中反复出现。这就是数学的统一性之美。

---

## 5. 竞赛数学中的不等式技巧

国际数学奥林匹克（IMO）和各类数学竞赛中，不等式问题是"经典中的经典"。以下是一些高级技巧的预览：

### SOS 方法（Sum of Squares）

将表达式写为平方和来证明非负性。

**例**：证明 $a^4 + b^4 + c^4 \geq a^2bc + ab^2c + abc^2 = abc(a + b + c)$。

观察 $a^4 + b^4 + c^4 - abc(a+b+c) = \frac{1}{2}[(a^2-b^2)^2 + (b^2-c^2)^2 + (c^2-a^2)^2]$ …… 这不完全对，需要更细致的分析。实际上可以用 AM-GM：$a^4 + b^4 \geq 2a^2b^2 \geq 2a^2bc$（当 $b \geq c$ 时需要额外论证）。

SOS 方法的系统化版本是判断一个齐次多项式能否写为平方和——这是**实代数几何**（real algebraic geometry）中的 Hilbert 第 17 问题的主题。

### 调整法（Smoothing/Equalizing）

通过将变量"调整"为更接近的值来证明不等式。核心思想：如果将两个不等的变量替换为它们的平均值不会使表达式变大（或变小），那么极值在"所有变量相等"时取到。

这个方法与 AM-GM 不等式的等号条件有深层联系。
