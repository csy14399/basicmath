# 第 4 章 复数的代数运算 — 挑战题（Challenge Problems）

以下挑战题综合运用复数的代数运算与极坐标理论，难度超出常规练习。

---

## 挑战题 1：复数与几何——用复数证明 Ptolemy 定理

设圆内接四边形 $ABCD$（按顺序在圆上），对应复数分别为 $a, b, c, d$（在单位圆上，即 $|a| = |b| = |c| = |d| = 1$）。

**Ptolemy 定理**（托勒密定理）：

$$|AC| \cdot |BD| = |AB| \cdot |CD| + |AD| \cdot |BC|$$

即 $|a - c| \cdot |b - d| = |a - b| \cdot |c - d| + |a - d| \cdot |b - c|$。

**(a)** 利用恒等式 $(a - c)(b - d) = (a - b)(c - d) + (a - d)(b - c)$ 验证此恒等式成立（代数展开）。

**(b)** 解释为什么 Ptolemy 等式需要 $ABCD$ 是**圆内接**四边形。对一般四边形，等式变成什么？

### 解答

**(a)** 展开 $(a-c)(b-d) = ab - ad - bc + cd$。

展开 $(a-b)(c-d) + (a-d)(b-c) = ac - ad - bc + bd + ab - ac - db + dc = ab - ad - bc + cd$。

两边相等。$\blacksquare$

**(b)** 恒等式 $(a-c)(b-d) = (a-b)(c-d) + (a-d)(b-c)$ 对所有复数成立。但 Ptolemy 等式涉及的是**模**的等式：

$$|A| = |B + C| \implies |A| \leq |B| + |C|$$

等号成立当且仅当 $B$ 和 $C$ 的辐角相同，即 $(a-b)(c-d)$ 和 $(a-d)(b-c)$ 指向同一方向。这等价于 $\frac{(a-b)(c-d)}{(a-d)(b-c)}$ 为正实数，即**交比** $(a, b; c, d)$ 为正实数——而这恰好是 $ABCD$ 四点共圆（共圆四边形）的充要条件。

对一般四边形，Ptolemy 不等式成立：$|a-c||b-d| \leq |a-b||c-d| + |a-d||b-c|$。

---

## 挑战题 2：复数与切比雪夫多项式

定义**切比雪夫多项式**（Chebyshev polynomial of the first kind）：

$$T_n(\cos\theta) = \cos(n\theta)$$

**(a)** 用 De Moivre 定理证明 $T_n$ 确实是一个次数为 $n$ 的多项式。

**(b)** 计算 $T_0(x)$，$T_1(x)$，$T_2(x)$，$T_3(x)$，$T_4(x)$。

**(c)** 证明递推关系：$T_{n+1}(x) = 2xT_n(x) - T_{n-1}(x)$。

**(d)** 证明 $T_n(x)$ 在 $[-1, 1]$ 上有 $n$ 个零点：$x_k = \cos\frac{(2k-1)\pi}{2n}$，$k = 1, \ldots, n$。

### 解答

**(a)** 由 De Moivre 定理：$\cos(n\theta) + i\sin(n\theta) = (\cos\theta + i\sin\theta)^n$。

展开右边（二项式定理），取实部，得到 $\cos(n\theta)$ 是 $\cos\theta$ 和 $\sin\theta$ 的多项式。

其中每一项含有 $\cos^a\theta \sin^b\theta$（$a + b = n$），由实部条件 $b$ 为偶数，用 $\sin^2\theta = 1 - \cos^2\theta$ 替换，全部化为 $\cos\theta$ 的多项式。最高次项来自 $\cos^n\theta$（系数为 $1$ 当 $n$ 为某些值时为 $2^{n-1}$），故 $T_n$ 是次数为 $n$ 的多项式。具体地，首项系数为 $2^{n-1}$（$n \geq 1$）。

**(b)** $T_0(x) = 1$，$T_1(x) = x$。

$\cos(2\theta) = 2\cos^2\theta - 1$，故 $T_2(x) = 2x^2 - 1$。

$\cos(3\theta) = 4\cos^3\theta - 3\cos\theta$，故 $T_3(x) = 4x^3 - 3x$。

$\cos(4\theta) = 8\cos^4\theta - 8\cos^2\theta + 1$，故 $T_4(x) = 8x^4 - 8x^2 + 1$。

**(c)** 利用和差化积公式：

$$\cos((n+1)\theta) + \cos((n-1)\theta) = 2\cos\theta\cos(n\theta)$$

即 $T_{n+1}(\cos\theta) + T_{n-1}(\cos\theta) = 2\cos\theta \cdot T_n(\cos\theta)$。

设 $x = \cos\theta$：$T_{n+1}(x) = 2xT_n(x) - T_{n-1}(x)$。$\blacksquare$

**(d)** $T_n(x_k) = \cos(n\theta_k)$，其中 $\theta_k = \frac{(2k-1)\pi}{2n}$。

$n\theta_k = \frac{(2k-1)\pi}{2}$，$\cos\frac{(2k-1)\pi}{2} = 0$（奇数倍 $\pi/2$）。✓

$k = 1, \ldots, n$ 给出 $n$ 个不同的 $x_k$（因为 $\cos$ 在 $[0, \pi]$ 上严格递减，$\theta_k$ 两两不同且在 $(0, \pi)$ 中）。$n$ 次多项式至多 $n$ 个零点，故这就是全部零点。$\blacksquare$

---

## 挑战题 3：用复数推导恒等式

利用单位根和 De Moivre 定理，证明以下恒等式：

$$\prod_{k=1}^{n-1} \sin\frac{k\pi}{n} = \frac{n}{2^{n-1}}$$

### 解答

由 $z^n - 1 = (z-1)(z-\omega)\cdots(z-\omega^{n-1})$，其中 $\omega = \text{cis}\frac{2\pi}{n}$。

$z^n - 1 = (z - 1)(z^{n-1} + z^{n-2} + \cdots + 1)$，令 $z = 1$：$n = \prod_{k=1}^{n-1}(1 - \omega^k)$。

取模：$n = \prod_{k=1}^{n-1}|1 - \omega^k|$。

计算 $|1 - \omega^k|$：$\omega^k = \text{cis}\frac{2k\pi}{n}$。

$$1 - \omega^k = 1 - \cos\frac{2k\pi}{n} - i\sin\frac{2k\pi}{n}$$

$$|1 - \omega^k|^2 = \left(1 - \cos\frac{2k\pi}{n}\right)^2 + \sin^2\frac{2k\pi}{n} = 2 - 2\cos\frac{2k\pi}{n} = 4\sin^2\frac{k\pi}{n}$$

$$|1 - \omega^k| = 2\left|\sin\frac{k\pi}{n}\right| = 2\sin\frac{k\pi}{n}$$

（因为 $0 < k < n$ 时 $0 < \frac{k\pi}{n} < \pi$，正弦值为正。）

代入：$n = \prod_{k=1}^{n-1} 2\sin\frac{k\pi}{n} = 2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}$。

$$\prod_{k=1}^{n-1}\sin\frac{k\pi}{n} = \frac{n}{2^{n-1}} \quad \blacksquare$$
