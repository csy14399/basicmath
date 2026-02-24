# 第 5 章 向量几何 — 练习题解答

## §1 向量基础

**1.** $\vec{u} + \vec{v} = (1, 3, 3)$，$\vec{u} - \vec{v} = (5, -5, 1)$，$3\vec{u} - 2\vec{v} = (9+4, -3-8, 6-2) = (13, -11, 4)$。

---

**2.** $|\vec{v}| = \sqrt{1+4+4} = 3$。$\hat{v} = \left(\frac{1}{3}, -\frac{2}{3}, \frac{2}{3}\right)$。

---

**3.** $\overrightarrow{AB} = (-2, -2, 6)$。$|\overrightarrow{AB}| = \sqrt{4+4+36} = \sqrt{44} = 2\sqrt{11}$。中点 $= \left(2, 0, 1\right)$。

---

**4.** $\vec{v} = -\frac{3}{2}\vec{u}$（$-3 = -\frac{3}{2} \cdot 2$, $9 = -\frac{3}{2} \cdot (-6)$, $-6 = -\frac{3}{2} \cdot 4$）。平行（反向）。

---

**5.** $\vec{w} = a\vec{u} + b\vec{v}$：$a + 3b = 5$，$2a + b = 7$。解：$a = \frac{16}{-5} $...

更直接：$2a + b = 7$，$a + 3b = 5$。由第一式 $b = 7 - 2a$，代入 $a + 3(7-2a) = 5$，$a + 21 - 6a = 5$，$-5a = -16$，$a = \frac{16}{5}$，$b = 7 - \frac{32}{5} = \frac{3}{5}$。

$\vec{w} = \frac{16}{5}(1, 2) + \frac{3}{5}(3, 1) = \frac{1}{5}(16+9, 32+3) = \frac{1}{5}(25, 35) = (5, 7)$。✓

---

**6.** 重心 $= \frac{1}{3}(1+0+0, 0+2+0, 0+0+3) = \left(\frac{1}{3}, \frac{2}{3}, 1\right)$。

$AB$ 中点 $= \left(\frac{1}{2}, 1, 0\right)$，$BC$ 中点 $= \left(0, 1, \frac{3}{2}\right)$，$AC$ 中点 $= \left(\frac{1}{2}, 0, \frac{3}{2}\right)$。

---

**7.** $P = \frac{3A + 2B}{2+3} = \frac{(3, 15) + (12, 0)}{5} = \frac{(15, 15)}{5} = (3, 3)$。

---

**8.** 设平行四边形 $ABCD$，$\overrightarrow{AB} = \vec{u}$，$\overrightarrow{AD} = \vec{v}$。

对角线 $AC$ 的中点：$A + \frac{1}{2}\overrightarrow{AC} = A + \frac{1}{2}(\vec{u} + \vec{v})$。

对角线 $BD$ 的中点：$B + \frac{1}{2}\overrightarrow{BD} = A + \vec{u} + \frac{1}{2}(\vec{v} - \vec{u}) = A + \frac{1}{2}(\vec{u} + \vec{v})$。

两个中点相同。$\blacksquare$

---

## §2 点积

**1.** $\vec{u} \cdot \vec{v} = 4 - 3 - 10 = -9$。

---

**2.** $\vec{u} \cdot \vec{v} = -2 + 2 = 0$。$\cos\theta = 0$，$\theta = 90°$。两向量正交。

---

**3.** 标量投影 $= \frac{(4,3)\cdot(1,0)}{|(1,0)|} = \frac{4}{1} = 4$。向量投影 $= 4(1,0) = (4, 0)$。

---

**4.** $\text{proj}_{\vec{v}}\vec{u} = \frac{1+2+3}{1+1+1}(1,1,1) = 2(1,1,1) = (2, 2, 2)$。

正交分量 $= (1,2,3) - (2,2,2) = (-1, 0, 1)$。

验证：$(-1, 0, 1) \cdot (1, 1, 1) = -1 + 0 + 1 = 0$。✓

---

**5.** 用叉积：$\vec{u} \times \vec{v} = (2 \cdot 0 - (-3)(-1), (-3)(2) - 1(0), 1(-1) - 2(2)) = (0-3, -6-0, -1-4) = (-3, -6, -5)$。

$|\vec{u} \times \vec{v}| = \sqrt{9+36+25} = \sqrt{70}$。

单位向量 $= \frac{1}{\sqrt{70}}(-3, -6, -5)$。（也可取负号。）

---

**6.** $\vec{d} = \overrightarrow{AB} = (2, 4, -2)$。$W = \vec{F} \cdot \vec{d} = 4 + 20 + 2 = 26$。

---

**7.** $d = \frac{|3(2)+4(3)-5|}{\sqrt{9+16}} = \frac{|6+12-5|}{5} = \frac{13}{5}$。

向量方法：法向量 $\vec{n} = (3, 4)$。直线上取 $A = (\frac{5}{3}, 0)$。$\overrightarrow{AP} = (2-\frac{5}{3}, 3) = (\frac{1}{3}, 3)$。

$\overrightarrow{AP} \cdot \vec{n} = 1 + 12 = 13$。$d = \frac{|13|}{5} = \frac{13}{5}$。✓

---

**8.** 设三角形 $ABC$，$\vec{a} = \overrightarrow{BC}$, $\vec{b} = \overrightarrow{CA}$, $\vec{c} = \overrightarrow{AB}$。

$\vec{a} + \vec{b} + \vec{c} = \vec{0}$（回路）。

角 $A$ 对应 $\overrightarrow{AB}$ 和 $\overrightarrow{AC}$ 的夹角，即 $\vec{c}$ 和 $-\vec{b}$ 的夹角。

$\cos A = \frac{\vec{c} \cdot (-\vec{b})}{|\vec{c}||\vec{b}|}$，类似可得 $\cos B$, $\cos C$。

完整证明需要用到三角恒等式，这里从 $\vec{a} + \vec{b} + \vec{c} = \vec{0}$ 出发，两边取模的平方：$|\vec{a}|^2 + |\vec{b}|^2 + |\vec{c}|^2 + 2\vec{a}\cdot\vec{b} + 2\vec{b}\cdot\vec{c} + 2\vec{c}\cdot\vec{a} = 0$，由此可以建立角度关系。直接证明 $A + B + C = \pi$ 需要用向量旋转和复数方法（超出本节范围但可以参考 Part 3 Ch04）。

---

**9.** $|2\vec{u} - \vec{v}|^2 = 4|\vec{u}|^2 - 4\vec{u}\cdot\vec{v} + |\vec{v}|^2 = 4(9) - 4(-7) + 25 = 36 + 28 + 25 = 89$。

$|2\vec{u} - \vec{v}| = \sqrt{89}$。

---

**10.** $|\vec{u}+\vec{v}|^2 = |\vec{u}|^2 + 2\vec{u}\cdot\vec{v} + |\vec{v}|^2$。

$|\vec{u}-\vec{v}|^2 = |\vec{u}|^2 - 2\vec{u}\cdot\vec{v} + |\vec{v}|^2$。

相加：$|\vec{u}+\vec{v}|^2 + |\vec{u}-\vec{v}|^2 = 2|\vec{u}|^2 + 2|\vec{v}|^2$。$\blacksquare$

几何意义：平行四边形两条对角线的平方和 = 四条边的平方和。

---

## §3 叉积与混合积

**1.** $\vec{i} \times \vec{j} = \vec{k} = (0, 0, 1)$。

---

**2.** $\vec{u} \times \vec{v} = (3 \cdot 2 - 1 \cdot (-1),\; 1 \cdot 1 - 2 \cdot 2,\; 2 \cdot (-1) - 3 \cdot 1) = (7, -3, -5)$。

---

**3.** $\overrightarrow{AB} = (1, -1, 1)$, $\overrightarrow{AC} = (-1, 1, 1)$。

$\overrightarrow{AB} \times \overrightarrow{AC} = (-1-1, -(1+1), 1-1) = (-2, -2, 0)$。

$S = \frac{1}{2}\sqrt{4+4+0} = \frac{1}{2} \cdot 2\sqrt{2} = \sqrt{2}$。

---

**4.** $\overrightarrow{AB} = (1, 2, 0)$, $\overrightarrow{AC} = (2, 0, 1)$。

$\vec{n} = \overrightarrow{AB} \times \overrightarrow{AC} = (2-0, 0-1, 0-4) = (2, -1, -4)$。

平面方程：$2(x-1) - (y-1) - 4(z-1) = 0$，$2x - y - 4z + 3 = 0$。

---

**5.** $\vec{v} \times \vec{w} = (5 \cdot 9 - 6 \cdot 8,\; 6 \cdot 7 - 4 \cdot 9,\; 4 \cdot 8 - 5 \cdot 7) = (-3, 6, -3)$。

$\vec{u} \cdot (\vec{v} \times \vec{w}) = 1(-3) + 2(6) + 3(-3) = -3 + 12 - 9 = 0$。

共面。

---

**6.** $\vec{u} \times \vec{v} = (2 \cdot (-1) - 0 \cdot 0,\; 0 \cdot 3 - 1 \cdot (-1),\; 1 \cdot 0 - 2 \cdot 3) = (-2, 1, -6)$。

$|\vec{u} \times \vec{v}|^2 = 4 + 1 + 36 = 41$。

$|\vec{u}|^2 = 5$, $|\vec{v}|^2 = 10$, $\vec{u}\cdot\vec{v} = 3$。

$|\vec{u}|^2|\vec{v}|^2 - (\vec{u}\cdot\vec{v})^2 = 50 - 9 = 41$。✓

---

**7.** 平行六面体体积 $= |\overrightarrow{AB} \cdot (\overrightarrow{AC} \times \overrightarrow{AD})|$（底面 $\overrightarrow{AC} \times \overrightarrow{AD}$ 的面积 × 高 $\overrightarrow{AB}$ 在法线方向的投影）。

四面体是平行六面体的 $\frac{1}{6}$（平行六面体可以分割为 6 个等体积四面体）。$\blacksquare$

---

**8.** 由 Lagrange 恒等式：$|\vec{u}\times\vec{v}|^2 + (\vec{u}\cdot\vec{v})^2 = |\vec{u}|^2|\vec{v}|^2$。

$|\vec{u}\times\vec{v}|^2 = 4+1+9 = 14$。$(\vec{u}\cdot\vec{v})^2 = 16$。

$14 + 16 = 4 \cdot |\vec{v}|^2$，$|\vec{v}|^2 = \frac{30}{4} = \frac{15}{2}$，$|\vec{v}| = \sqrt{\frac{15}{2}} = \frac{\sqrt{30}}{2}$。

---

**9.** $\vec{d}_1 \times \vec{d}_2 = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{vmatrix} = (1, -1, 1)$。

$\overrightarrow{AB} = (-1, 1, 0)$。

$d = \frac{|\overrightarrow{AB} \cdot (\vec{d}_1 \times \vec{d}_2)|}{|\vec{d}_1 \times \vec{d}_2|} = \frac{|(-1)(1) + 1(-1) + 0(1)|}{\sqrt{3}} = \frac{2}{\sqrt{3}} = \frac{2\sqrt{3}}{3}$。

---

**10.** 设 $\vec{u} = (u_1, u_2, u_3)$, $\vec{v} = (v_1, v_2, v_3)$, $\vec{w} = (w_1, w_2, w_3)$。

$\vec{v} \times \vec{w} = (v_2 w_3 - v_3 w_2, v_3 w_1 - v_1 w_3, v_1 w_2 - v_2 w_1)$。

$\vec{u} \times (\vec{v} \times \vec{w})$ 逐分量计算并整理，可以验证每个分量都等于 $(\vec{u}\cdot\vec{w})\vec{v} - (\vec{u}\cdot\vec{v})\vec{w}$ 的对应分量。

例如第一个分量：$\vec{u} \times (\vec{v} \times \vec{w})$ 的第一个分量 $= u_2(v_1 w_2 - v_2 w_1) - u_3(v_3 w_1 - v_1 w_3)$

$= u_2 v_1 w_2 - u_2 v_2 w_1 - u_3 v_3 w_1 + u_3 v_1 w_3$

$= v_1(u_2 w_2 + u_3 w_3) - w_1(u_2 v_2 + u_3 v_3)$

$= v_1(\vec{u}\cdot\vec{w} - u_1 w_1) - w_1(\vec{u}\cdot\vec{v} - u_1 v_1)$

$= v_1(\vec{u}\cdot\vec{w}) - w_1(\vec{u}\cdot\vec{v}) - u_1 v_1 w_1 + u_1 v_1 w_1$

$= (\vec{u}\cdot\vec{w})v_1 - (\vec{u}\cdot\vec{v})w_1$。

类似验证其他分量。$\blacksquare$
