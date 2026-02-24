# 第 4 章 级数 — 挑战题（Challenge Problems）

以下挑战题探索级数理论的深层问题，难度超出常规练习。

---

## 挑战题 1：Euler 的巴塞尔问题

**题目**：我们知道 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}$（Euler, 1734）。本题探索 Euler 最初的非严格但惊人的推导。

(a) 考虑函数 $f(x) = \dfrac{\sin x}{x}$。写出它的 Taylor 展开：

$$\frac{\sin x}{x} = 1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \cdots$$

(b) 如果我们大胆地将 $\sin x / x$ 视为一个"无穷次多项式"，其零点为 $x = \pm\pi, \pm 2\pi, \pm 3\pi, \ldots$，则可以写成：

$$\frac{\sin x}{x} = \left(1 - \frac{x^2}{\pi^2}\right)\left(1 - \frac{x^2}{4\pi^2}\right)\left(1 - \frac{x^2}{9\pi^2}\right)\cdots$$

展开此乘积，比较 $x^2$ 的系数，你得到什么？

(c) 解释为什么这个推导在 Euler 的时代还不算严格（Weierstrass 乘积定理直到 19 世纪下半叶才被证明）。

### 解答

**(a)** $\sin x = x - x^3/6 + x^5/120 - \cdots$，除以 $x$：

$$\frac{\sin x}{x} = 1 - \frac{x^2}{6} + \frac{x^4}{120} - \cdots$$

**(b)** 右边乘积展开后，$x^2$ 的系数为：

$$-\left(\frac{1}{\pi^2} + \frac{1}{4\pi^2} + \frac{1}{9\pi^2} + \cdots\right) = -\frac{1}{\pi^2}\sum_{n=1}^{\infty}\frac{1}{n^2}$$

左边（Taylor 展开）$x^2$ 的系数为 $-1/6$。令两者相等：

$$-\frac{1}{\pi^2}\sum\frac{1}{n^2} = -\frac{1}{6}$$

$$\sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}$$

**(c)** Euler 假设了一个多项式关于零点的因式分解公式（如果 $p(x)$ 是首一多项式，零点为 $r_1, r_2, \ldots, r_n$，则 $p(x) = (x-r_1)(x-r_2)\cdots(x-r_n)$）可以推广到无穷乘积。这对有限次多项式是代数基本定理的推论，但对无穷乘积需要额外的收敛性论证。Weierstrass 在 1876 年给出了这一推广的严格版本（Weierstrass 因子分解定理）。

---

## 挑战题 2：条件收敛级数的重排

**题目**：考虑交错调和级数 $\displaystyle S = \sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots = \ln 2$。

(a) 构造一个重排，使得级数收敛于 $\dfrac{3}{2}\ln 2$。（提示：先取正项直到部分和超过 $3\ln 2/2$，再取一个负项使部分和低于 $3\ln 2/2$，如此循环。）

(b) 更具体地：考虑重排 $1 + \frac{1}{3} - \frac{1}{2} + \frac{1}{5} + \frac{1}{7} - \frac{1}{4} + \cdots$（每两个正项后接一个负项）。证明此重排收敛于 $\dfrac{3}{2}\ln 2$。

### 解答

**(a)** Riemann 重排定理的构造思路：设目标值为 $L = 3\ln 2/2$。

正项 $1, 1/3, 1/5, 1/7, \ldots$ 之和 $= +\infty$（因为它们大于等于 $1/(2n)$，后者发散）。
负项 $1/2, 1/4, 1/6, \ldots$ 之和 $= -\infty$。

先累加正项直到部分和首次超过 $L$；然后加入负项直到部分和低于 $L$；再加正项直到超过 $L$；如此反复。因正项和负项都趋于零，每次"超过"或"低于"$L$ 的幅度趋于零，部分和收敛于 $L$。

**(b)** 设原级数部分和 $H_n = \sum_{k=1}^{n}1/k$。重排的部分和（取到第 $3m$ 项）为：

$$T_{3m} = \sum_{k=1}^{2m}\frac{1}{2k-1} - \sum_{k=1}^{m}\frac{1}{2k}$$

$\sum_{k=1}^{2m}\frac{1}{2k-1} = H_{4m} - \frac{1}{2}H_{2m}$（因为 $\sum_{k=1}^{2m}\frac{1}{2k-1} = \sum_{k=1}^{4m}\frac{1}{k} - \sum_{k=1}^{2m}\frac{1}{2k}$）。

$\sum_{k=1}^{m}\frac{1}{2k} = \frac{1}{2}H_m$。

$T_{3m} = H_{4m} - \frac{1}{2}H_{2m} - \frac{1}{2}H_m$。

利用 $H_n \approx \ln n + \gamma$：

$T_{3m} \approx \ln 4m - \frac{1}{2}\ln 2m - \frac{1}{2}\ln m = \ln 4m - \frac{1}{2}\ln(2m^2)$

$= \ln 4m - \frac{1}{2}(\ln 2 + 2\ln m) = 2\ln 2 + \ln m - \frac{1}{2}\ln 2 - \ln m = \frac{3}{2}\ln 2$。

---

## 挑战题 3：Cesàro 可和性

**题目**：级数 $\sum (-1)^n = 1 - 1 + 1 - 1 + \cdots$（Grandi 级数）按通常定义发散。但 Cesàro 在 1890 年引入了一种更宽泛的"求和"概念。

定义部分和 $S_n = \sum_{k=0}^{n}(-1)^k$，**Cesàro 均值** 为：

$$\sigma_n = \frac{S_0 + S_1 + \cdots + S_n}{n + 1}$$

(a) 计算前几个 $S_n$ 和 $\sigma_n$。$\sigma_n$ 趋向什么值？

(b) 证明 $\lim_{n \to \infty}\sigma_n = 1/2$。于是我们说 $\sum (-1)^n$ "Cesàro 可和"，Cesàro 和为 $1/2$。

(c) [信息] 若级数按通常意义收敛于 $S$，则它的 Cesàro 均值也收敛于 $S$。但 Cesàro 可和性严格更宽泛——有些发散级数（如 Grandi 级数）也是 Cesàro 可和的。

### 解答

**(a)**
$S_0 = 1$, $S_1 = 0$, $S_2 = 1$, $S_3 = 0$, $S_4 = 1$, $\ldots$

$\sigma_0 = 1$, $\sigma_1 = 1/2$, $\sigma_2 = 2/3$, $\sigma_3 = 2/4 = 1/2$, $\sigma_4 = 3/5$, $\sigma_5 = 3/6 = 1/2$, $\ldots$

$\sigma_n$ 在 $1/2$ 附近振荡且幅度趋于零。

**(b)** $S_{2k} = 1$，$S_{2k+1} = 0$。

$$\sigma_{2m} = \frac{(m+1) \cdot 1 + m \cdot 0}{2m+1} = \frac{m+1}{2m+1} \to \frac{1}{2}$$

$$\sigma_{2m+1} = \frac{(m+1) \cdot 1 + (m+1) \cdot 0}{2m+2} = \frac{m+1}{2m+2} = \frac{1}{2}$$

所以 $\sigma_n \to 1/2$。$\blacksquare$
