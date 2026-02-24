# 第 5 章 参数方程与极坐标 — 挑战题（Challenge Problems）

以下挑战题综合运用参数方程和极坐标的深层知识。

---

## 挑战题 1：Bézier 曲线——计算机图形学的基石

### 背景

**Bézier 曲线**是计算机图形学中最重要的参数曲线之一（Adobe Illustrator、字体设计、CAD 软件都大量使用）。一条**三次 Bézier 曲线**由四个**控制点** $P_0, P_1, P_2, P_3$ 确定，参数方程为：

$$B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t)t^2 P_2 + t^3 P_3, \quad t \in [0, 1]$$

### 任务

(a) 验证 $B(0) = P_0$ 且 $B(1) = P_3$（曲线从 $P_0$ 开始，到 $P_3$ 结束）。

(b) 设 $P_0 = (0,0)$，$P_1 = (1,2)$，$P_2 = (3,2)$，$P_3 = (4,0)$。写出 $x(t)$ 和 $y(t)$ 的显式表达式。

(c) 证明 Bézier 曲线在 $t = 0$ 处的切线方向为 $\overrightarrow{P_0 P_1}$，在 $t = 1$ 处的切线方向为 $\overrightarrow{P_2 P_3}$。（提示：计算 $B'(0)$ 和 $B'(1)$。）

### 解答

**(a)** $B(0) = 1 \cdot P_0 + 0 + 0 + 0 = P_0$。$B(1) = 0 + 0 + 0 + 1 \cdot P_3 = P_3$。✓

**(b)** 逐坐标计算：

$$x(t) = (1-t)^3 \cdot 0 + 3(1-t)^2 t \cdot 1 + 3(1-t)t^2 \cdot 3 + t^3 \cdot 4$$

$$= 3t(1-t)^2 + 9t^2(1-t) + 4t^3$$

展开：$= 3t(1-2t+t^2) + 9t^2 - 9t^3 + 4t^3 = 3t - 6t^2 + 3t^3 + 9t^2 - 9t^3 + 4t^3$

$$= 3t + 3t^2 - 2t^3$$

$$y(t) = 0 + 3(1-t)^2 t \cdot 2 + 3(1-t)t^2 \cdot 2 + 0$$

$$= 6t(1-t)^2 + 6t^2(1-t) = 6t(1-t)[(1-t) + t] = 6t(1-t)$$

所以 $x(t) = 3t + 3t^2 - 2t^3$，$y(t) = 6t - 6t^2$。

**(c)** $B'(t) = -3(1-t)^2 P_0 + [3(1-t)^2 - 6(1-t)t]P_1 + [6(1-t)t - 3t^2]P_2 + 3t^2 P_3$。

$B'(0) = -3P_0 + 3P_1 = 3(P_1 - P_0)$。方向为 $\overrightarrow{P_0 P_1}$。

$B'(1) = -3P_2 + 3P_3 = 3(P_3 - P_2)$。方向为 $\overrightarrow{P_2 P_3}$。$\blacksquare$

---

## 挑战题 2：等角螺旋线与 Jacob Bernoulli 的墓志铭

### 背景

**等角螺旋线**（equiangular spiral），也叫**对数螺旋线**（logarithmic spiral），其极坐标方程为：

$$r = ae^{b\theta} \quad (a > 0, b \neq 0)$$

Jacob Bernoulli（1654–1705）对这条曲线着迷不已，称之为 *Spira mirabilis*（"奇妙的螺旋"），因为它在多种变换下保持形状不变。他遗嘱要求在墓碑上刻一条对数螺旋和铭文 *Eadem mutata resurgo*（"虽然改变，但以同样的形式重生"）。（可惜石匠刻的是阿基米德螺旋线。）

### 任务

(a) 证明对数螺旋的自相似性：对任意常数 $c > 0$，将螺旋绕原点旋转角度 $\alpha = \frac{\ln c}{b}$ 并缩放 $c$ 倍后，得到的仍是同一条螺旋。

(b) 证明从原点出发的任意射线（$\theta =$ 常数）与螺旋线的夹角恒为 $\text{arccot}\, b$。（这就是"等角"的含义。）

(c) 螺旋线从 $\theta = 0$ 沿 $\theta \to -\infty$ 的方向**无限旋转但弧长有限**。假设弧长公式 $L = \int_{\theta_1}^{\theta_2}\sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta$，计算从 $\theta = -\infty$ 到 $\theta = 0$ 的弧长。

### 解答

**(a)** 旋转角度 $\alpha$ 意味着将 $\theta$ 替换为 $\theta - \alpha$；缩放 $c$ 倍意味着将 $r$ 乘以 $c$：

$$r' = c \cdot ae^{b(\theta - \alpha)} = ca \cdot e^{b\theta} \cdot e^{-b\alpha}$$

取 $\alpha = \frac{\ln c}{b}$，则 $e^{-b\alpha} = e^{-\ln c} = \frac{1}{c}$：

$$r' = ca \cdot e^{b\theta} \cdot \frac{1}{c} = ae^{b\theta} = r$$

所以变换后的曲线与原曲线完全相同。$\blacksquare$

**(b)** 用极坐标中切线角的公式。射线方向的单位向量为 $\hat{e}_r$，曲线切线方向由 $\frac{dr}{d\theta}$ 和 $r$ 决定。切线与射线的夹角 $\psi$ 满足：

$$\tan\psi = \frac{r}{dr/d\theta}$$

对于 $r = ae^{b\theta}$：$\frac{dr}{d\theta} = abe^{b\theta} = br$。

$$\tan\psi = \frac{r}{br} = \frac{1}{b}$$

$\psi = \arctan\frac{1}{b} = \text{arccot}\, b$，为常数。$\blacksquare$

**(c)** $\frac{dr}{d\theta} = abr^{b\theta} = br$，$r^2 + (dr/d\theta)^2 = r^2(1+b^2)$。

$$L = \int_{-\infty}^{0}\sqrt{r^2(1+b^2)}\,d\theta = \sqrt{1+b^2}\int_{-\infty}^{0}ae^{b\theta}\,d\theta$$

当 $b > 0$ 时：

$$= \sqrt{1+b^2}\cdot a \cdot \left[\frac{e^{b\theta}}{b}\right]_{-\infty}^{0} = \sqrt{1+b^2}\cdot\frac{a}{b}\cdot(1 - 0) = \frac{a\sqrt{1+b^2}}{b}$$

这是一个**有限值**！螺旋线虽然无限旋转趋向原点，但总弧长是有限的。$\blacksquare$
