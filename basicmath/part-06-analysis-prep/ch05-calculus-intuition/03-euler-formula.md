# §3 Euler 公式（Euler's Formula）[Bridge]

**前置知识**：[Part 6 第 4 章 §3 幂级数初步](../ch04-series/03-power-series.md)（Taylor 展开：$e^x$, $\sin x$, $\cos x$）、[Part 3 第 4 章 复数](../../part-03-algebra/ch04-complex/README.md)（虚数单位 $i$、复数运算）

**全景图**：本节是整本教材的华彩终章。我们将用 Taylor 级数推导出数学中最优美的公式——**Euler 公式**：$e^{i\theta} = \cos\theta + i\sin\theta$。这个公式统一了指数函数、三角函数和复数，揭示了它们之间的深层联系。作为特例，**Euler 恒等式** $e^{i\pi} + 1 = 0$ 被誉为"数学中最美的等式"——它仅用五个最基本的数学常数（$e$, $i$, $\pi$, $0$, $1$）和三种基本运算（加、乘、幂），写出了一个惊人的关系。

**预估学习时间**：约 2–3 小时

> 🌉 本节为 Bridge 内容。Euler 公式的严格证明需要复分析（complex analysis）中关于复指数函数和复幂级数的理论。我们这里采用形式推导——将实数 Taylor 级数中的 $x$ 替换为复数——直觉上是自然的，但严格证明需要验证复幂级数的收敛性。

---

## 动机

在 Part 3 Ch04 中，我们学习了复数 $z = a + bi$ 的代数运算。在 Part 4 中，我们分别研究了指数函数 $e^x$ 和三角函数 $\sin x$, $\cos x$。

这三个看似独立的主题——复数、指数、三角——有什么联系吗？

答案出人意料地优美：

$$e^{i\theta} = \cos\theta + i\sin\theta$$

这个公式表明：**将虚数代入指数函数，就得到三角函数**。更深层地，$e^{i\theta}$ 是单位圆上角度为 $\theta$ 的点。这意味着**复指数 = 旋转**。

---

## 1. Euler 公式（Euler's Formula）

### 1.1 公式陈述

> **定理 1**（Euler 公式）
>
> 对所有实数 $\theta$：
>
> $$e^{i\theta} = \cos\theta + i\sin\theta$$

其中 $i = \sqrt{-1}$ 是虚数单位。

### 1.2 公式的含义

$e^{i\theta}$ 是复平面上的一个点，坐标为 $(\cos\theta, \sin\theta)$——即**单位圆**上角度为 $\theta$ 的点。

| $\theta$ | $e^{i\theta}$ | 位置 |
|----------|---------------|------|
| $0$ | $1$ | 实轴正方向 |
| $\pi/2$ | $i$ | 虚轴正方向 |
| $\pi$ | $-1$ | 实轴负方向 |
| $3\pi/2$ | $-i$ | 虚轴负方向 |
| $2\pi$ | $1$ | 回到起点 |

![Euler 公式与单位圆](../../images/p06-ch05-euler-formula.png)

---

## 2. 从 Taylor 级数推导（Derivation from Taylor Series）

### 2.1 回顾三个 Taylor 展开

$$e^x = \sum_{n=0}^{\infty}\frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$

$$\cos\theta = \sum_{n=0}^{\infty}\frac{(-1)^n\theta^{2n}}{(2n)!} = 1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} + \cdots$$

$$\sin\theta = \sum_{n=0}^{\infty}\frac{(-1)^n\theta^{2n+1}}{(2n+1)!} = \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} + \cdots$$

### 2.2 将 $i\theta$ 代入 $e^x$

大胆地将 $x = i\theta$ 代入 $e^x$ 的 Taylor 展开：

$$e^{i\theta} = \sum_{n=0}^{\infty}\frac{(i\theta)^n}{n!} = 1 + i\theta + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!} + \frac{(i\theta)^4}{4!} + \cdots$$

利用 $i$ 的幂次循环：$i^0 = 1$, $i^1 = i$, $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, $\ldots$

$$e^{i\theta} = 1 + i\theta - \frac{\theta^2}{2!} - \frac{i\theta^3}{3!} + \frac{\theta^4}{4!} + \frac{i\theta^5}{5!} - \frac{\theta^6}{6!} - \cdots$$

### 2.3 分离实部和虚部

将实数项和虚数项分开：

$$e^{i\theta} = \underbrace{\left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} + \cdots\right)}_{\cos\theta} + i\underbrace{\left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} + \cdots\right)}_{\sin\theta}$$

因此：

$$\boxed{e^{i\theta} = \cos\theta + i\sin\theta} \qquad \blacksquare$$

### 2.4 推导的严格性

这个推导在形式上完美，但有一个微妙之处：我们假设了 Taylor 级数在复数域上的性质（逐项替换、分离实虚部、逐项收敛）与实数域相同。严格验证这一点需要复分析——但结论是正确的：$e^x$ 的 Taylor 级数对所有复数 $x$ 绝对收敛，且定义了一个解析函数。

---

## 3. Euler 恒等式（Euler's Identity）

取 $\theta = \pi$：

$$e^{i\pi} = \cos\pi + i\sin\pi = -1 + 0 = -1$$

因此：

$$\boxed{e^{i\pi} + 1 = 0}$$

这就是 **Euler 恒等式**——被广泛认为是数学中最优美的等式。

### 3.1 为什么美？

它以最简洁的方式联系了数学中五个最基本的常数：

| 常数 | 来源 | 含义 |
|------|------|------|
| $e \approx 2.718$ | 分析学 | 自然指数的底，增长率 |
| $i = \sqrt{-1}$ | 代数 | 虚数单位，扩展数系 |
| $\pi \approx 3.14159$ | 几何 | 圆的周长与直径之比 |
| $1$ | 算术 | 乘法单位元 |
| $0$ | 算术 | 加法单位元 |

加上三种基本运算：$+$（加法）、$\times$（乘法，写成并列）、$\wedge$（指数运算）。

这五个常数来自数学的不同分支，Euler 恒等式用一个简单的等式将它们全部联系起来——这体现了数学深层的统一性。

### 3.2 其他特殊值

$e^{i\pi/2} = \cos(\pi/2) + i\sin(\pi/2) = i$

所以 $i^i = (e^{i\pi/2})^i = e^{i^2\pi/2} = e^{-\pi/2} \approx 0.2079$——一个实数！虚数的虚数次方居然是实数。

---

## 4. 联系——统一三角与指数（Unification）

### 4.1 复数的指数形式

任何复数 $z = a + bi$ 可以写成极坐标形式 $z = r(\cos\theta + i\sin\theta) = re^{i\theta}$，其中：
- $r = |z| = \sqrt{a^2 + b^2}$（模）
- $\theta = \arg(z)$（幅角）

这就是复数的**指数形式**——它比三角形式更简洁，计算更方便。

### 4.2 复数乘法 = 旋转 + 缩放

$$z_1 z_2 = r_1 e^{i\theta_1} \cdot r_2 e^{i\theta_2} = r_1 r_2 \cdot e^{i(\theta_1+\theta_2)}$$

- **模相乘**：$|z_1 z_2| = r_1 r_2$
- **幅角相加**：$\arg(z_1 z_2) = \theta_1 + \theta_2$

复数乘法的几何意义：**旋转 + 缩放**。乘以 $e^{i\theta}$ 就是旋转角度 $\theta$。

### 4.3 De Moivre 定理

$(e^{i\theta})^n = e^{in\theta}$，即：

$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)$$

这是 Part 3 Ch04 中的 De Moivre 定理——现在它变成了指数运算的平凡推论！

### 4.4 三角恒等式的快速推导

从 Euler 公式出发：

$$e^{i\theta} = \cos\theta + i\sin\theta \qquad e^{-i\theta} = \cos\theta - i\sin\theta$$

相加：$\cos\theta = \dfrac{e^{i\theta} + e^{-i\theta}}{2}$

相减：$\sin\theta = \dfrac{e^{i\theta} - e^{-i\theta}}{2i}$

**和角公式**：

$$e^{i(\alpha+\beta)} = e^{i\alpha} \cdot e^{i\beta}$$

$$\cos(\alpha+\beta) + i\sin(\alpha+\beta) = (\cos\alpha + i\sin\alpha)(\cos\beta + i\sin\beta)$$

展开右边，分离实虚部：

$$\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$$
$$\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$$

这正是和角公式——但推导只需一行乘法！在 Part 4 中，我们用几何方法证明了和角公式；Euler 公式提供了一个更优雅、更统一的视角。

---

## 5. 应用（Applications）

### 5.1 信号处理（预览）

在电子工程和信号处理中，信号通常用 $e^{i\omega t}$ 表示，而不是 $\cos(\omega t)$ 或 $\sin(\omega t)$。原因：指数运算比三角运算更简单——乘法变成指数相加，微分只是乘以 $i\omega$：

$$(e^{i\omega t})' = i\omega \cdot e^{i\omega t}$$

这使得线性微分方程的求解变得机械化。

### 5.2 Fourier 级数（预览）

任何"合理"的周期函数都可以分解为三角函数的无穷和（Fourier 级数）：

$$f(t) = \sum_{n=-\infty}^{\infty}c_n e^{in\omega t}$$

这是信号分析、音乐理论、量子力学的数学基础。Euler 公式是其核心工具。

### 5.3 量子力学（预览）

量子力学中的波函数 $\psi(x, t)$ 是复值函数。Schrödinger 方程：

$$i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2} + V(x)\psi$$

其中 $i$ 出现在基本方程中——复数不是数学家的玩具，而是物理世界的基本语言。

---

## 例题

**例题 1**：用 Euler 公式计算 $(1+i)^{10}$。

**解**：$1 + i = \sqrt{2}\,e^{i\pi/4}$。

$(1+i)^{10} = (\sqrt{2})^{10} \cdot e^{i \cdot 10\pi/4} = 2^5 \cdot e^{i \cdot 5\pi/2} = 32 \cdot e^{i\pi/2} = 32i$。

---

**例题 2**：用 Euler 公式推导 $\cos^2\theta = \dfrac{1+\cos 2\theta}{2}$。

**解**：$\cos\theta = \dfrac{e^{i\theta} + e^{-i\theta}}{2}$。

$$\cos^2\theta = \frac{(e^{i\theta}+e^{-i\theta})^2}{4} = \frac{e^{2i\theta} + 2 + e^{-2i\theta}}{4} = \frac{2 + 2\cos 2\theta}{4} = \frac{1+\cos 2\theta}{2}$$

---

**例题 3**：证明 $\displaystyle\sum_{k=0}^{n-1}\cos\frac{2\pi k}{n} = 0$（$n \geq 2$）。

**解**：$\sum \cos(2\pi k/n) = \text{Re}\left(\sum_{k=0}^{n-1}e^{2\pi ik/n}\right) = \text{Re}\left(\sum_{k=0}^{n-1}\omega^k\right)$，其中 $\omega = e^{2\pi i/n}$ 是 $n$ 次单位根。

$\sum \omega^k = \dfrac{1 - \omega^n}{1 - \omega} = \dfrac{1-1}{1-\omega} = 0$（因 $\omega^n = 1$）。

所以 $\sum \cos(2\pi k/n) = \text{Re}(0) = 0$。$\blacksquare$

---

**例题 4**：解释 $e^{2\pi i} = 1$ 的几何意义。

**解**：$e^{2\pi i} = \cos 2\pi + i\sin 2\pi = 1$。几何意义：在单位圆上旋转 $2\pi$（整圈）回到起点 $1$。这反映了三角函数的周期性：$e^{i\theta}$ 以 $2\pi$ 为周期。

---

## 要点回顾

| 概念 | 要点 |
|------|------|
| **Euler 公式** | $e^{i\theta} = \cos\theta + i\sin\theta$ |
| **推导方法** | 将 $i\theta$ 代入 $e^x$ 的 Taylor 展开，分离实虚部 |
| **Euler 恒等式** | $e^{i\pi} + 1 = 0$——联系 $e, i, \pi, 0, 1$ |
| **指数形式** | $z = re^{i\theta}$，乘法 = 模相乘 + 幅角相加 |
| **三角公式统一** | 和角公式、倍角公式都是 $e^{i\theta}$ 乘法的推论 |
| **应用** | 信号处理、Fourier 分析、量子力学 |

---

## 进度检查点

在结束本章之前，确认你能够：

- [ ] 陈述 Euler 公式并解释其含义
- [ ] 从 Taylor 级数推导 Euler 公式
- [ ] 写出 Euler 恒等式并解释其为何被称为"最美的等式"
- [ ] 用指数形式表示复数并计算复数乘法
- [ ] 用 Euler 公式推导三角恒等式
- [ ] 解释 $e^{i\theta}$ 的旋转几何意义

---

## 自测题

**自测 1**：计算 $e^{i\pi/3}$。

<details>
<summary>答案</summary>

$e^{i\pi/3} = \cos(\pi/3) + i\sin(\pi/3) = \dfrac{1}{2} + i\dfrac{\sqrt{3}}{2}$
</details>

**自测 2**：用 Euler 公式证明 $|e^{i\theta}| = 1$。

<details>
<summary>答案</summary>

$|e^{i\theta}| = |\cos\theta + i\sin\theta| = \sqrt{\cos^2\theta + \sin^2\theta} = \sqrt{1} = 1$。

$e^{i\theta}$ 始终在单位圆上。
</details>

**自测 3**：计算 $i^i$。

<details>
<summary>答案</summary>

$i = e^{i\pi/2}$。$i^i = (e^{i\pi/2})^i = e^{i \cdot i \cdot \pi/2} = e^{-\pi/2} \approx 0.2079$。

虚数的虚数次方是实数！
</details>

**自测 4**：用 Euler 公式推导 $\sin 2\theta = 2\sin\theta\cos\theta$。

<details>
<summary>答案</summary>

$e^{2i\theta} = (e^{i\theta})^2 = (\cos\theta + i\sin\theta)^2 = \cos^2\theta - \sin^2\theta + 2i\sin\theta\cos\theta$。

另一方面，$e^{2i\theta} = \cos 2\theta + i\sin 2\theta$。

比较虚部：$\sin 2\theta = 2\sin\theta\cos\theta$。$\blacksquare$
</details>

**自测 5**：如果 $z = 3e^{i\pi/4}$，求 $z^4$。

<details>
<summary>答案</summary>

$z^4 = 3^4 \cdot e^{i \cdot 4\pi/4} = 81 \cdot e^{i\pi} = 81 \cdot (-1) = -81$。
</details>

---

## 习题引用

本节的练习题见 [练习题](exercises/exercises.md) 的 §3 部分。
