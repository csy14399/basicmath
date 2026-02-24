# 第 4 章 复数的代数运算 — 练习题解答

## §1 复数的运算

**1.** $(5 + 3i) + (2 - 7i) = 7 - 4i$。

---

**2.** $(3 + 4i)(2 - i) = 6 - 3i + 8i - 4i^2 = 6 + 5i + 4 = 10 + 5i$。

---

**3.** $\displaystyle\frac{1 + i}{1 - i} = \frac{(1+i)^2}{(1-i)(1+i)} = \frac{1 + 2i + i^2}{1 + 1} = \frac{2i}{2} = i$。

---

**4.** $\bar{z} = 2 + 3i$，$|z| = \sqrt{4 + 9} = \sqrt{13}$，$z\bar{z} = |z|^2 = 13$。

验证：$(2 - 3i)(2 + 3i) = 4 + 9 = 13$。✓

---

**5.** $2025 = 4 \times 506 + 1$，所以 $i^{2025} = i^1 = i$。

---

**6.** $z^2 = (1 + 2i)^2 = 1 + 4i + 4i^2 = -3 + 4i$。

$z^3 = z^2 \cdot z = (-3 + 4i)(1 + 2i) = -3 - 6i + 4i + 8i^2 = -11 - 2i$。

$z\bar{z} = (1 + 2i)(1 - 2i) = 1 + 4 = 5$。

---

**7.** 设 $w_1 = \frac{3 - 4i}{2 + i}$，$w_2 = \frac{3 + 4i}{2 - i}$。

$w_1 = \frac{(3-4i)(2-i)}{(2+i)(2-i)} = \frac{6 - 3i - 8i + 4i^2}{5} = \frac{2 - 11i}{5}$。

$w_2 = \frac{(3+4i)(2+i)}{(2-i)(2+i)} = \frac{6 + 3i + 8i + 4i^2}{5} = \frac{2 + 11i}{5}$。

$w_1 + w_2 = \frac{2 - 11i + 2 + 11i}{5} = \frac{4}{5}$。

注：也可以观察到 $w_2 = \bar{w}_1$，所以 $w_1 + w_2 = 2\text{Re}(w_1) = \frac{4}{5}$。

---

**8.** $|4 + 3i| = \sqrt{16 + 9} = 5$。由三角不等式和反向三角不等式：

$$|5 - 3| \leq |z + 4 + 3i| \leq 5 + 3$$

$$2 \leq |z + 4 + 3i| \leq 8$$

---

**9.** 设 $z = a + bi$（$a, b \in \mathbb{R}$）。

$z + \bar{z} = (a + bi) + (a - bi) = 2a \in \mathbb{R}$。

$z\bar{z} = (a + bi)(a - bi) = a^2 + b^2 \in \mathbb{R}$。$\blacksquare$

---

**10.** $|z - 2 + i| = |z - (2 - i)| = 3$。这是以 $2 - i$（即平面上 $(2, -1)$）为圆心、半径为 $3$ 的圆。

---

**11.** $z_1 z_2 = (2+i)(1-3i) = 2 - 6i + i - 3i^2 = 5 - 5i$。

$\overline{z_1 z_2} = 5 + 5i$。

$\bar{z}_1 \bar{z}_2 = (2 - i)(1 + 3i) = 2 + 6i - i - 3i^2 = 5 + 5i$。

$\overline{z_1 z_2} = \bar{z}_1 \bar{z}_2$。✓

---

**12.** 设 $z = a + bi$。$(a + bi)^2 = a^2 - b^2 + 2abi = 3 + 4i$。

比较实部和虚部：$a^2 - b^2 = 3$，$2ab = 4$，即 $b = 2/a$。

代入：$a^2 - 4/a^2 = 3$，$a^4 - 3a^2 - 4 = 0$，$(a^2 - 4)(a^2 + 1) = 0$。

$a^2 = 4$（$a^2 = -1$ 无实数解），$a = \pm 2$。

$a = 2 \implies b = 1$；$a = -2 \implies b = -1$。

$z = 2 + i$ 或 $z = -2 - i$。

验证：$(2 + i)^2 = 4 + 4i + i^2 = 3 + 4i$。✓

---

**13.** 设 $z = \text{cis}\,\theta$（$|z| = 1$），$z \neq -1$。

$$w = \frac{z - 1}{z + 1} = \frac{\text{cis}\,\theta - 1}{\text{cis}\,\theta + 1}$$

计算 $w + \bar{w}$：

$$\bar{w} = \frac{\bar{z} - 1}{\bar{z} + 1} = \frac{z^{-1} - 1}{z^{-1} + 1} = \frac{1 - z}{1 + z} = -w$$

因此 $w + \bar{w} = 0$，即 $\text{Re}(w) = 0$，所以 $w$ 是纯虚数或零。

$w = 0$ 当且仅当 $z = 1$。当 $z \neq 1$ 时，$w$ 是纯虚数。$\blacksquare$

---

**14.** 展开左端：

$$|z_1 + z_2|^2 = (z_1 + z_2)\overline{(z_1 + z_2)} = |z_1|^2 + z_1\bar{z}_2 + \bar{z}_1 z_2 + |z_2|^2$$

$$|z_1 - z_2|^2 = (z_1 - z_2)\overline{(z_1 - z_2)} = |z_1|^2 - z_1\bar{z}_2 - \bar{z}_1 z_2 + |z_2|^2$$

相加：$|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2|z_1|^2 + 2|z_2|^2$。$\blacksquare$

几何解读：平行四边形两条对角线的平方和等于四条边的平方和。

---

## §2 复数的极坐标形式

**1.** $r = \sqrt{1 + 1} = \sqrt{2}$，$\theta = -\pi/4$（第四象限）。

$$1 - i = \sqrt{2}\,\text{cis}\left(-\frac{\pi}{4}\right)$$

---

**2.** $r = 3$，$\theta = \pi$。$-3 = 3\,\text{cis}\,\pi$。

---

**3.** $z = 4(\cos\frac{\pi}{3} + i\sin\frac{\pi}{3}) = 4(\frac{1}{2} + \frac{\sqrt{3}}{2}i) = 2 + 2\sqrt{3}\,i$。

---

**4.** $1 + i = \sqrt{2}\,\text{cis}\frac{\pi}{4}$，$1 - i = \sqrt{2}\,\text{cis}(-\frac{\pi}{4})$。

$(1+i)(1-i) = 2\,\text{cis}(0) = 2$。

验证：$(1+i)(1-i) = 1 + 1 = 2$。✓

---

**5.** $\sqrt{3} + i = 2\,\text{cis}\frac{\pi}{6}$。

$(\sqrt{3} + i)^6 = 2^6\,\text{cis}\pi = 64(\cos\pi + i\sin\pi) = -64$。

---

**6.** $z^4 = 1$，$z_k = \text{cis}\frac{2k\pi}{4} = \text{cis}\frac{k\pi}{2}$。

$z_0 = 1$，$z_1 = i$，$z_2 = -1$，$z_3 = -i$。

复平面上：单位圆上的正方形顶点 $(1,0)$、$(0,1)$、$(-1,0)$、$(0,-1)$。

---

**7.** $-27 = 27\,\text{cis}\,\pi$。

$z_k = 3\,\text{cis}\frac{\pi + 2k\pi}{3}$。

$z_0 = 3\,\text{cis}\frac{\pi}{3} = 3(\frac{1}{2} + \frac{\sqrt{3}}{2}i) = \frac{3}{2} + \frac{3\sqrt{3}}{2}i$。

$z_1 = 3\,\text{cis}\,\pi = -3$。

$z_2 = 3\,\text{cis}\frac{5\pi}{3} = \frac{3}{2} - \frac{3\sqrt{3}}{2}i$。

---

**8.** 首先化为极坐标：$w = -8 + 8\sqrt{3}\,i$。

$|w| = \sqrt{64 + 192} = \sqrt{256} = 16$。

$\text{Arg}(w) = \pi - \arctan\frac{8\sqrt{3}}{8} = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$。

$z_k = 16^{1/4}\,\text{cis}\frac{2\pi/3 + 2k\pi}{4} = 2\,\text{cis}\frac{(2+6k)\pi}{12} = 2\,\text{cis}\frac{(1+3k)\pi}{6}$。

$z_0 = 2\,\text{cis}\frac{\pi}{6} = \sqrt{3} + i$。

$z_1 = 2\,\text{cis}\frac{4\pi}{6} = 2\,\text{cis}\frac{2\pi}{3} = -1 + \sqrt{3}\,i$。

$z_2 = 2\,\text{cis}\frac{7\pi}{6} = -\sqrt{3} - i$。

$z_3 = 2\,\text{cis}\frac{10\pi}{6} = 2\,\text{cis}\frac{5\pi}{3} = 1 - \sqrt{3}\,i$。

---

**9.** 由 De Moivre 定理：$\cos(4\theta) + i\sin(4\theta) = (\cos\theta + i\sin\theta)^4$。

展开（二项式定理）：

$$= \cos^4\theta + 4i\cos^3\theta\sin\theta + 6i^2\cos^2\theta\sin^2\theta + 4i^3\cos\theta\sin^3\theta + i^4\sin^4\theta$$

$$= (\cos^4\theta - 6\cos^2\theta\sin^2\theta + \sin^4\theta) + i(4\cos^3\theta\sin\theta - 4\cos\theta\sin^3\theta)$$

实部：$\cos(4\theta) = \cos^4\theta - 6\cos^2\theta\sin^2\theta + \sin^4\theta$。

用 $\sin^2\theta = 1 - \cos^2\theta$：

$$\cos(4\theta) = \cos^4\theta - 6\cos^2\theta(1-\cos^2\theta) + (1-\cos^2\theta)^2 = 8\cos^4\theta - 8\cos^2\theta + 1$$

---

**10.** $(\text{cis}\,\alpha)(\text{cis}\,\beta) = (\cos\alpha + i\sin\alpha)(\cos\beta + i\sin\beta)$

$= (\cos\alpha\cos\beta - \sin\alpha\sin\beta) + i(\cos\alpha\sin\beta + \sin\alpha\cos\beta)$

另一方面，$\text{cis}(\alpha + \beta) = \cos(\alpha+\beta) + i\sin(\alpha+\beta)$。

由复数相等（实部和虚部分别相等）：

$$\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$$

$$\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$$

这就是三角函数的和角公式。$\blacksquare$

---

**11.** $\omega = \text{cis}\frac{2\pi}{5}$ 是 $z^5 = 1$ 的根，$\omega \neq 1$。

$z^5 - 1 = (z - 1)(z^4 + z^3 + z^2 + z + 1) = 0$。

因为 $\omega \neq 1$，所以 $\omega^4 + \omega^3 + \omega^2 + \omega + 1 = 0$。

求 $\cos\frac{4\pi}{5}$：设 $u = \omega + \omega^{-1} = 2\cos\frac{2\pi}{5}$，$v = \omega^2 + \omega^{-2} = 2\cos\frac{4\pi}{5}$。

$v = u^2 - 2$。

由 $\omega^4 + \omega^3 + \omega^2 + \omega + 1 = 0$ 除以 $\omega^2$：$v + u + 1 = 0$。

代入 $v = u^2 - 2$：$u^2 + u - 1 = 0$，$u = \frac{-1+\sqrt{5}}{2}$（取正值）。

$v = -1 - u = -1 - \frac{-1+\sqrt{5}}{2} = \frac{-1 - \sqrt{5}}{2}$。

$$\cos\frac{4\pi}{5} = \frac{v}{2} = \frac{-1 - \sqrt{5}}{4}$$

---

**12.** 由 $z^n - 1 = (z - 1)(z - \omega)(z - \omega^2)\cdots(z - \omega^{n-1})$，其中 $\omega = \text{cis}\frac{2\pi}{n}$。

除以 $(z - 1)$：$z^{n-1} + z^{n-2} + \cdots + z + 1 = (z - \omega)(z - \omega^2)\cdots(z - \omega^{n-1})$。

令 $z = 1$：$n = (1 - \omega)(1 - \omega^2)\cdots(1 - \omega^{n-1})$。$\blacksquare$

---

**13.** 设 $w = z^3$，则方程变为 $w^2 + w + 1 = 0$。

$w = \frac{-1 \pm \sqrt{3}\,i}{2} = \text{cis}\frac{2\pi}{3}$ 或 $\text{cis}\frac{4\pi}{3}$。

这正是 $3$ 次本原单位根 $\omega$ 和 $\omega^2$（$\omega = \text{cis}\frac{2\pi}{3}$）。

对 $w_1 = \text{cis}\frac{2\pi}{3}$：$z^3 = \text{cis}\frac{2\pi}{3}$，$z_k = \text{cis}\frac{2\pi/3 + 2k\pi}{3} = \text{cis}\frac{(2+6k)\pi}{9}$。

$k = 0, 1, 2$：$z = \text{cis}\frac{2\pi}{9}$，$\text{cis}\frac{8\pi}{9}$，$\text{cis}\frac{14\pi}{9}$。

对 $w_2 = \text{cis}\frac{4\pi}{3}$：$z_k = \text{cis}\frac{(4+6k)\pi}{9}$。

$k = 0, 1, 2$：$z = \text{cis}\frac{4\pi}{9}$，$\text{cis}\frac{10\pi}{9}$，$\text{cis}\frac{16\pi}{9}$。

共 $6$ 个根：$\text{cis}\frac{2k\pi}{9}$，$k = 1, 2, 4, 5, 7, 8$。

注意这些正是 $9$ 次单位根中不是 $3$ 次单位根的那六个。
