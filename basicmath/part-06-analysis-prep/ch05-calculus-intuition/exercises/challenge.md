# 第 5 章 微积分直觉 — 挑战题（Challenge Problems）

以下挑战题探索微积分和 Euler 公式的深层问题。

---

## 挑战题 1：Wallis 乘积公式

**题目**：John Wallis（1655）发现了以下令人惊叹的公式：

$$\frac{\pi}{2} = \frac{2}{1} \cdot \frac{2}{3} \cdot \frac{4}{3} \cdot \frac{4}{5} \cdot \frac{6}{5} \cdot \frac{6}{7} \cdots = \prod_{n=1}^{\infty}\frac{4n^2}{4n^2-1}$$

(a) 定义 $I_n = \int_0^{\pi/2}\sin^n x\,dx$。利用分部积分（或直接验证）说明 $I_n = \dfrac{n-1}{n}I_{n-2}$。

(b) 计算 $I_0, I_1, I_2, I_3, I_4, I_5$。

(c) 利用 $0 \leq \sin x \leq 1$ 说明 $I_{2n+1} \leq I_{2n} \leq I_{2n-1}$，由此推导 $I_{2n}/I_{2n+1} \to 1$。

(d) 计算 $I_{2n}/I_{2n+1}$ 的显式表达，从而得到 Wallis 公式。

### 解答

**(a)** $I_n = \int_0^{\pi/2}\sin^{n-1}x \cdot \sin x\,dx$。令 $u = \sin^{n-1}x$，$dv = \sin x\,dx$，则 $du = (n-1)\sin^{n-2}x\cos x\,dx$，$v = -\cos x$。

$I_n = [-\sin^{n-1}x\cos x]_0^{\pi/2} + (n-1)\int_0^{\pi/2}\sin^{n-2}x\cos^2 x\,dx = 0 + (n-1)\int_0^{\pi/2}\sin^{n-2}x(1-\sin^2 x)\,dx$

$= (n-1)(I_{n-2} - I_n)$。因此 $I_n + (n-1)I_n = (n-1)I_{n-2}$，$nI_n = (n-1)I_{n-2}$，$I_n = \dfrac{n-1}{n}I_{n-2}$。

**(b)** $I_0 = \pi/2$，$I_1 = 1$。$I_2 = \frac{1}{2}\cdot\frac{\pi}{2}$，$I_3 = \frac{2}{3}$，$I_4 = \frac{3}{4}\cdot\frac{1}{2}\cdot\frac{\pi}{2} = \frac{3\pi}{16}$，$I_5 = \frac{4}{5}\cdot\frac{2}{3} = \frac{8}{15}$。

**(c)** $\sin^{2n+1}x \leq \sin^{2n}x \leq \sin^{2n-1}x$。积分得 $I_{2n+1} \leq I_{2n} \leq I_{2n-1}$。

$\dfrac{I_{2n}}{I_{2n+1}} \leq \dfrac{I_{2n-1}}{I_{2n+1}} = \dfrac{2n+1}{2n} \to 1$。下界显然 $\geq 1$。由夹逼，$I_{2n}/I_{2n+1} \to 1$。

**(d)** $\dfrac{I_{2n}}{I_{2n+1}} = \dfrac{\frac{(2n-1)!!}{(2n)!!}\cdot\frac{\pi}{2}}{\frac{(2n)!!}{(2n+1)!!}} = \frac{\pi}{2}\cdot\frac{((2n-1)!!)^2 \cdot (2n+1)}{((2n)!!)^2} \to 1$。

因此 $\dfrac{\pi}{2} = \lim \dfrac{((2n)!!)^2}{((2n-1)!!)^2(2n+1)} = \prod_{n=1}^{\infty}\dfrac{4n^2}{4n^2-1}$。$\blacksquare$

---

## 挑战题 2：Newton 与 Leibniz 的优先权之争

**题目**（历史探究）：

Newton 和 Leibniz 在 17 世纪 70 年代各自独立发明了微积分。Newton 先发现（约 1666 年），但 Leibniz 先发表（1684 年）。此后爆发了数学史上最著名的优先权之争。

(a) Newton 使用"流数法"（fluxions），Leibniz 使用 $\frac{dy}{dx}$ 记号。比较两种记号在链式法则 $\frac{dy}{dx} = \frac{dy}{du}\cdot\frac{du}{dx}$ 上的表现。Leibniz 记号为什么更方便？

(b) [信息] 这场争论的后果是：英国数学家坚持使用 Newton 记号，欧洲大陆使用 Leibniz 记号。结果英国数学在整个 18 世纪落后于欧洲大陆（Euler, Lagrange, Laplace 等）。直到 19 世纪初，Cambridge 的 Analytical Society 才引入 Leibniz 记号。

### 解答

**(a)** Newton 的流数记号：$\dot{y}$（$y$ 对时间的导数）。链式法则写为：$\dot{y} = \dot{y}/\dot{u} \cdot \dot{u}$，需要"除以流数"的概念，不太自然。

Leibniz 记号：$\dfrac{dy}{dx} = \dfrac{dy}{du}\cdot\dfrac{du}{dx}$，形式上像分数的"约分"——尽管 $dy$ 和 $dx$ 本身不是数，但这种记号暗示了正确的运算规则。这种"启发式正确性"使得 Leibniz 记号在实际计算中极其方便。

此外，Leibniz 记号自然地推广到多变量（$\partial y/\partial x$）、高阶导数（$d^2y/dx^2$）和积分（$\int f\,dx$），而 Newton 记号在这些方面不够灵活。

---

## 挑战题 3：无穷的哲学——从 Zeno 到 Cantor

**题目**（哲学探究）：

(a) Zeno 的"Achilles 与乌龟"悖论本质上是在问："完成无穷多个步骤是否可能？"用级数理论给出数学回答。从哲学角度思考：数学的"完成"（极限存在）与物理的"完成"（Achilles 实际追上乌龟）是否是同一回事？

(b) Newton 和 Leibniz 使用"无穷小量"（infinitesimals）——比任何正数都小但不为零的量。这在逻辑上有问题（Archimedes 公理排除了这种量）。Cauchy 和 Weierstrass 用 $\epsilon$-$\delta$ 语言消除了无穷小量。但 1960 年，Abraham Robinson 的**非标准分析**（nonstandard analysis）严格化了无穷小量！这说明什么？

(c) [信息] 关于无穷的哲学思考从未停止。Hilbert 的名言"没有人能将我们从 Cantor 为我们创造的天堂中驱逐"反映了数学界对实无穷的接受。但直觉主义者（Brouwer）和构造主义者仍然质疑实无穷的合法性。在数学基础中，这些问题至今没有定论。

### 解答

**(a)** 数学回答：Achilles 跑过的距离是收敛级数 $\sum 100(1/10)^n = 100/(1-1/10) = 1000/9$ 米。跑完的时间也是收敛级数。数学上，"无穷多个步骤的和"有精确定义——即部分和序列的极限。

哲学思考：数学通过定义解决了问题——"和"被定义为极限。但这是否意味着Achilles"真正"完成了无穷多个步骤，还是我们只是找到了一个数学模型来描述物理现实？实际上，物理空间可能在 Planck 长度（$\sim 10^{-35}$ m）处是离散的——也许 Zeno 的问题在物理上根本不出现。

**(b)** Robinson 的非标准分析表明：数学理论可以有不同的严格化方式。$\epsilon$-$\delta$ 方法和非标准分析方法在逻辑上**等价**——它们证明完全相同的定理。这说明数学的"正确性"不依赖于特定的形式化方式，而在于逻辑的一致性。Newton 和 Leibniz 的直觉是正确的——只是他们没有找到严格的语言来表达。
