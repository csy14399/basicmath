# 第 4 章 反三角函数 — 思考者角落（Thinker's Corner）

> 本节超越教材的核心内容，带你一窥反三角函数的深层世界。这里没有考试，只有好奇心。

---

## 1. 多值函数与 Riemann 面——"反函数"的完整图景

### 单值化的代价

在定义 $\arcsin$ 时，我们通过限制 $\sin$ 的定义域到 $[-\pi/2, \pi/2]$ 来得到一个"良定的"反函数。但这意味着我们**丢弃了信息**——$\sin x = 0.5$ 有无穷多个解，我们只选了其中一个。

在复分析（complex analysis）中，数学家采取不同的策略：他们接受反三角函数是**多值函数**（multi-valued function）的事实。$\arcsin z$（$z \in \mathbb{C}$）的每个值都有无穷多个分支（branches），彼此相差 $2\pi$ 的整数倍或涉及符号翻转。

### Riemann 面

**Bernhard Riemann**（1826–1866）提出了一种优雅的几何解决方案：将多值函数的不同分支排列在不同的"层"上，形成一个**Riemann 面**（Riemann surface）。在这个面上，多值函数变成了单值函数。

对于 $\arcsin$，Riemann 面看起来像一个**螺旋楼梯**——每上一层对应原函数的一个周期。这种思想深刻地影响了代数几何和弦理论。

---

## 2. 反三角函数的复数形式

### 从三角函数到指数函数

利用 Euler 公式 $e^{i\theta} = \cos\theta + i\sin\theta$，可以将三角函数用指数表示：

$$\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}, \qquad \cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$$

### 反正弦的复数公式

设 $w = \arcsin z$，即 $\sin w = z$。用指数形式：

$$\frac{e^{iw} - e^{-iw}}{2i} = z$$

令 $u = e^{iw}$：$\frac{u - u^{-1}}{2i} = z$，即 $u^2 - 2izu - 1 = 0$。

用求根公式：$u = iz + \sqrt{1 - z^2}$（选取适当分支）。

因此 $iw = \ln(iz + \sqrt{1-z^2})$，即：

$$\arcsin z = -i\ln\left(iz + \sqrt{1-z^2}\right)$$

这个令人惊叹的公式将反三角函数与对数函数和复数的平方根联系在一起——三个看似无关的概念实际上是同一个硬币的不同面。

类似地：

$$\arccos z = -i\ln\left(z + i\sqrt{1-z^2}\right)$$

$$\arctan z = \frac{1}{2i}\ln\frac{1+iz}{1-iz}$$

### 深层含义

这些公式揭示了一个深刻的统一性：**在复数的世界里，三角函数、指数函数和对数函数是同一族函数的不同面貌**。它们之间的关系通过 Euler 公式 $e^{i\theta} = \cos\theta + i\sin\theta$ 建立起来。

---

## 3. $\arctan$ 与 $\pi$ 的计算历史

### Leibniz 公式（1674）

$$\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots = \sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}$$

这实际上是 $\arctan x$ 的 Taylor 级数在 $x = 1$ 处的值：

$$\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \cdots = \sum_{k=0}^{\infty}\frac{(-1)^k x^{2k+1}}{2k+1} \quad (|x| \leq 1)$$

这个级数极其美丽，但收敛极慢——需要 500,000 项才能得到 $\pi$ 的 5 位精度。

### 加速方法

Machin（1706）的巧妙之处在于用 $\arctan$ 加法公式将 $\frac{\pi}{4}$ 分解为小参数的 $\arctan$ 之和：

$$\frac{\pi}{4} = 4\arctan\frac{1}{5} - \arctan\frac{1}{239}$$

$\arctan\frac{1}{5}$ 的级数以 $\frac{1}{5^{2k+1}}$ 的速度衰减——仅需 15 项即可得到 $\pi$ 的 20 位精度。

后世数学家发现了更多类似的"Machin 型公式"：

**Størmer（1896）**：

$$\frac{\pi}{4} = 6\arctan\frac{1}{8} + 2\arctan\frac{1}{57} + \arctan\frac{1}{239}$$

**黄见利（Hwang Chien-Lih, 1997）**：

$$\frac{\pi}{4} = 183\arctan\frac{1}{239} + 32\arctan\frac{1}{1023} - 68\arctan\frac{1}{5832} + 12\arctan\frac{1}{110443} - 12\arctan\frac{1}{4841182} - 100\arctan\frac{1}{6826318}$$

现代计算 $\pi$ 数万亿位数的方法已经超越了 Machin 公式（如 Chudnovsky 兄弟的超几何级数公式），但 $\arctan$ 公式在 $\pi$ 的计算史上留下了不可磨灭的印记。

---

## 4. Gudermannian 函数——连接三角函数与双曲函数

### 定义

**Gudermannian 函数** $\text{gd}(x)$ 定义为：

$$\text{gd}(x) = 2\arctan(e^x) - \frac{\pi}{2} = \arctan(\sinh x) = \arcsin(\tanh x)$$

### 特殊性质

这个函数建立了**三角函数**和**双曲函数**之间的直接联系——**不需要复数**！

$$\sin(\text{gd}(x)) = \tanh x, \qquad \cos(\text{gd}(x)) = \text{sech}\, x$$

$$\tan(\text{gd}(x)) = \sinh x, \qquad \sec(\text{gd}(x)) = \cosh x$$

### 应用

Gudermannian 函数出现在**墨卡托投影**（Mercator projection）中——这是将球面上的经纬度映射到平面地图上最著名的方法之一。具体地，纬度 $\phi$ 对应的 $y$ 坐标为 $y = \text{gd}^{-1}(\phi)$。

---

## 5. 反三角函数的导数——微积分的预告

虽然我们尚未正式学习微积分，但反三角函数的导数公式之美值得提前一窥：

$$\frac{d}{dx}\arcsin x = \frac{1}{\sqrt{1-x^2}}, \qquad \frac{d}{dx}\arccos x = -\frac{1}{\sqrt{1-x^2}}$$

$$\frac{d}{dx}\arctan x = \frac{1}{1+x^2}$$

这些公式有两个惊人之处：

1. **代数函数的反三角函数的导数竟然是代数函数**——$\frac{1}{\sqrt{1-x^2}}$ 和 $\frac{1}{1+x^2}$ 不含任何三角或反三角。这意味着反三角函数是某些"简单"函数的原函数（antiderivative）。

2. **$\arctan$ 的导数 $\frac{1}{1+x^2}$ 极其简洁**，它是 Cauchy 分布（概率论）和 Breit-Wigner 共振（粒子物理）的核心函数。

在 Part 6（分析基础）中，我们将严格推导这些公式，并看到它们如何产生丰富的积分公式。
