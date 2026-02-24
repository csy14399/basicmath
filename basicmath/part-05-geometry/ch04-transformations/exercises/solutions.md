# 第 4 章 变换几何 — 练习题解答

## §1 平移与旋转

**1.** $\vec{v} = (-2, 4)$。

$A' = (0-2, 0+4) = (-2, 4)$，$B' = (3-2, 0+4) = (1, 4)$，$C' = (3-2, 2+4) = (1, 6)$，$D' = (0-2, 2+4) = (-2, 6)$。

---

**2.** $R_{45°}: (1, 0) \mapsto (\cos 45°, \sin 45°) = \left(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2}\right)$。

---

**3.** 旋转 $180°$ 就是关于原点的中心对称：$(0, 3) \mapsto (0, -3)$。

---

**4.** 绕 $C(1, 1)$ 旋转。先平移：$P - C = (2-1, 1-1) = (1, 0)$。

绕原点旋转 $90°$：$(1, 0) \mapsto (0, 1)$。

平移回：$(0+1, 1+1) = (1, 2)$。

像为 $(1, 2)$。

---

**5.** $R_{30°} = \begin{pmatrix} \cos 30° & -\sin 30° \\ \sin 30° & \cos 30° \end{pmatrix} = \begin{pmatrix} \frac{\sqrt{3}}{2} & -\frac{1}{2} \\ \frac{1}{2} & \frac{\sqrt{3}}{2} \end{pmatrix}$。

$(1, 0) \mapsto \left(\frac{\sqrt{3}}{2}, \frac{1}{2}\right)$。$\left(\frac{\sqrt{3}}{2}\right)^2 + \left(\frac{1}{2}\right)^2 = \frac{3}{4} + \frac{1}{4} = 1$。在单位圆上。✓

---

**6.** $T_{\vec{v}_2} \circ T_{\vec{v}_1}(x, y) = T_{\vec{v}_2}(x+a_1, y+b_1) = (x+a_1+a_2, y+b_1+b_2) = T_{\vec{v}_1+\vec{v}_2}(x,y)$。$\blacksquare$

---

**7.** $R_{\theta_1} R_{\theta_2} = \begin{pmatrix} \cos\theta_1 & -\sin\theta_1 \\ \sin\theta_1 & \cos\theta_1 \end{pmatrix}\begin{pmatrix} \cos\theta_2 & -\sin\theta_2 \\ \sin\theta_2 & \cos\theta_2 \end{pmatrix}$

$= \begin{pmatrix} \cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2 & -\cos\theta_1\sin\theta_2 - \sin\theta_1\cos\theta_2 \\ \sin\theta_1\cos\theta_2 + \cos\theta_1\sin\theta_2 & -\sin\theta_1\sin\theta_2 + \cos\theta_1\cos\theta_2 \end{pmatrix}$

$= \begin{pmatrix} \cos(\theta_1+\theta_2) & -\sin(\theta_1+\theta_2) \\ \sin(\theta_1+\theta_2) & \cos(\theta_1+\theta_2) \end{pmatrix} = R_{\theta_1+\theta_2}$。$\blacksquare$

---

**8.** 旋转后 $(3\cos\theta - 4\sin\theta, 3\sin\theta + 4\cos\theta)$。平移后 $y$ 坐标 $= 3\sin\theta + 4\cos\theta - 1 = 0$。

$3\sin\theta + 4\cos\theta = 1$。令 $r = 5$，$3\sin\theta + 4\cos\theta = 5\sin(\theta + \phi)$，其中 $\tan\phi = \frac{4}{3}$，$\phi = \arctan\frac{4}{3}$。

$5\sin(\theta + \phi) = 1$，$\sin(\theta + \phi) = \frac{1}{5}$。

$\theta + \phi = \arcsin\frac{1}{5}$ 或 $\theta + \phi = \pi - \arcsin\frac{1}{5}$。

$\theta = \arcsin\frac{1}{5} - \arctan\frac{4}{3}$ 或 $\theta = \pi - \arcsin\frac{1}{5} - \arctan\frac{4}{3}$。

数值：$\arctan\frac{4}{3} \approx 0.9273$，$\arcsin\frac{1}{5} \approx 0.2014$。

$\theta \approx -0.7259$（加 $2\pi$ 得 $\approx 5.557$）或 $\theta \approx \pi - 0.2014 - 0.9273 \approx 1.013$。

---

## §2 反射

**1.**
(a) $(3, 5) \mapsto (3, -5)$
(b) $(3, 5) \mapsto (-3, 5)$
(c) $(3, 5) \mapsto (5, 3)$

---

**2.** $y = -x$ 的方向角 $\alpha = 135° = \frac{3\pi}{4}$。

$M_{3\pi/4} = \begin{pmatrix} \cos\frac{3\pi}{2} & \sin\frac{3\pi}{2} \\ \sin\frac{3\pi}{2} & -\cos\frac{3\pi}{2} \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$。

验证：$(1, 0) \mapsto (0, -1)$，$(0, 1) \mapsto (-1, 0)$。交换坐标并取负。✓

---

**3.** 直线 $y = x + 1$。平移 $(0, -1)$ 使其变为 $y = x$（过原点）。

点 $(4, 1)$ 平移为 $(4, 0)$。关于 $y = x$ 反射：$(4, 0) \mapsto (0, 4)$。平移回：$(0, 4+1) = (0, 5)$。

像为 $(0, 5)$。

验证：中点 $= (2, 3)$。$3 = 2 + 1$。✓ 斜率 $= \frac{5-1}{0-4} = -1$，与 $y = x$ 垂直。✓

---

**4.** $M_\alpha^2 = \begin{pmatrix} \cos 2\alpha & \sin 2\alpha \\ \sin 2\alpha & -\cos 2\alpha \end{pmatrix}^2$

$= \begin{pmatrix} \cos^2 2\alpha + \sin^2 2\alpha & \cos 2\alpha\sin 2\alpha - \sin 2\alpha\cos 2\alpha \\ \sin 2\alpha\cos 2\alpha - \cos 2\alpha\sin 2\alpha & \sin^2 2\alpha + \cos^2 2\alpha \end{pmatrix}$

$= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$。$\blacksquare$

---

**5.** $\alpha = 30°$。$M_{30°} = \begin{pmatrix} \cos 60° & \sin 60° \\ \sin 60° & -\cos 60° \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & \frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & -\frac{1}{2} \end{pmatrix}$。

$(1, 0) \mapsto \left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right)$。这是 $60°$ 方向上的单位向量——正好是 $(1,0)$ 关于 $30°$ 线的对称点。✓

---

**6.** $\ell_1: y = 1$。$M_{\ell_1}(x, y) = (x, 2-y)$。

$\ell_2: y = 4$。$M_{\ell_2}(x, y) = (x, 8-y)$。

$M_{\ell_2} \circ M_{\ell_1}(x, y) = M_{\ell_2}(x, 2-y) = (x, 8-(2-y)) = (x, 6+y)$。

这是沿 $(0, 6)$ 的平移。$6 = 2 \times (4-1) = 2d$。✓

---

**7.** $M_{\ell_1} = M_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$，$M_{\ell_2} = M_{y=x} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$。

$M_{\ell_2} M_{\ell_1} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = R_{90°}$。✓

夹角 $= 45°$，旋转 $= 2 \times 45° = 90°$。✓

---

## §3 缩放与相似变换

**1.** $k = \frac{1}{2}$。$P' = (2, 3)$, $Q' = (1, 0)$, $R' = (4, 1)$。

面积比 $= k^2 = \frac{1}{4}$。

原三角形面积 $= \frac{1}{2}|4(0-2)+2(2-6)+8(6-0)| = \frac{1}{2}|-8-8+48| = 16$。

像三角形面积 $= \frac{1}{2}|2(0-1)+1(1-3)+4(3-0)| = \frac{1}{2}|-2-2+12| = 4$。

$\frac{4}{16} = \frac{1}{4} = k^2$。✓

---

**2.** $x' = 1 + 3(2-1) = 4$, $y' = 1 + 3(4-1) = 10$。像为 $(4, 10)$。

---

**3.** $D_k(\vec{u}) = k\vec{u}$, $D_k(\vec{v}) = k\vec{v}$。两向量 $\vec{u}$, $\vec{v}$ 的夹角 $\cos\theta = \frac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|}$。

缩放后 $\cos\theta' = \frac{(k\vec{u})\cdot(k\vec{v})}{|k\vec{u}||k\vec{v}|} = \frac{k^2(\vec{u}\cdot\vec{v})}{k^2|\vec{u}||\vec{v}|} = \cos\theta$。

角度不变。$\blacksquare$

---

**4.** 旋转 $60°$：$(3, 1) \mapsto (3\cos 60° - \sin 60°, 3\sin 60° + \cos 60°) = \left(\frac{3}{2} - \frac{\sqrt{3}}{2}, \frac{3\sqrt{3}}{2} + \frac{1}{2}\right) = \left(\frac{3-\sqrt{3}}{2}, \frac{3\sqrt{3}+1}{2}\right)$。

缩放 $k = 2$：$\left(3-\sqrt{3}, 3\sqrt{3}+1\right) \approx (1.268, 6.196)$。

---

**5.** 乘以 $w = re^{i\theta}$ 等价于：先绕原点旋转 $\theta$，再以原点为中心缩放 $r$（即相似变换，相似比 $r$，旋转角 $\theta$）。这正是复数乘法的几何本质。

---

## §4 变换的复合与变换群

**1.** $R_{60°} M_x = \begin{pmatrix} \frac{1}{2} & -\frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & \frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & -\frac{1}{2} \end{pmatrix}$。

$\det = -\frac{1}{4} - \frac{3}{4} = -1$。这是反射。$\cos 2\alpha = \frac{1}{2}$，$\sin 2\alpha = \frac{\sqrt{3}}{2}$，$2\alpha = 60°$，$\alpha = 30°$。

关于 $y = \tan 30° \cdot x = \frac{x}{\sqrt{3}}$ 的反射。

---

**2.** $S \circ T = R_{60°} M_x$（如上）= 关于 $30°$ 线的反射。

$T \circ S = M_x R_{60°} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} \frac{1}{2} & -\frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & -\frac{\sqrt{3}}{2} \\ -\frac{\sqrt{3}}{2} & -\frac{1}{2} \end{pmatrix}$。

$\cos 2\alpha = \frac{1}{2}$，$\sin 2\alpha = -\frac{\sqrt{3}}{2}$，$2\alpha = -60°$，$\alpha = -30°$。

关于 $y = -\tan 30° \cdot x$ 的反射。$S \circ T \neq T \circ S$。

---

**3.** 正三角形 $D_3$（6 个元素）：

旋转：$e$（$0°$），$r$（$120°$），$r^2$（$240°$）。

反射：$s_1$, $s_2$, $s_3$（关于三条对称轴）。

---

**4.** $T$ 是等距变换且 $T(O) = O$。$T$ 的矩阵 $A$ 满足 $A^TA = I$（正交矩阵），$\det A = \pm 1$。

$\det A = 1$：保向正交矩阵 = 旋转矩阵 $R_\theta$。

$\det A = -1$：反向正交矩阵 = 反射矩阵 $M_\alpha$。$\blacksquare$

---

**5.** 非正方形矩形的对称：$R_0$（恒等），$R_{180°}$，关于长轴反射 $M_1$，关于短轴反射 $M_2$。共 $4$ 个元素。

$G \cong \mathbb{Z}_2 \times \mathbb{Z}_2$（Klein 四元群）。

---

**6.** $D_4 = \{e, r, r^2, r^3, s, sr, sr^2, sr^3\}$，其中 $r = R_{90°}$, $s = M_x$。

关系：$r^4 = e$, $s^2 = e$, $srs = r^{-1}$。

乘法表（省略完整 $8 \times 8$，关键规律）：

$r^i \cdot r^j = r^{i+j \bmod 4}$，$s r^i \cdot r^j = s r^{i+j \bmod 4}$，$r^i \cdot s r^j = s r^{-i+j \bmod 4}$，$s r^i \cdot s r^j = r^{-i+j \bmod 4}$。

---

**7.** 设 $T$ 是保向等距变换。

情况 1：$T$ 有不动点 $P$（$T(P) = P$）。通过平移可以假设 $P = O$。由第 4 题，固定原点的保向等距变换是旋转。

情况 2：$T$ 没有不动点。设 $T(P) = P'$（$P \neq P'$）。令 $S$ 为沿 $\overrightarrow{PP'}$ 反方向的平移，则 $S \circ T$ 固定 $P$，且 $\det(S \circ T) = +1$。由情况 1，$S \circ T$ 是旋转 $R$。若 $R = \text{id}$，则 $T = S^{-1}$ 是平移。若 $R \neq \text{id}$（旋转角 $\neq 0$），$R$ 有唯一不动点（旋转中心），则 $T = S^{-1} \circ R$ 也是旋转（绕不同中心），但 $T$ 也没有不动点——矛盾（非零旋转总有不动点，加上平移后可能没有不动点，但 $S^{-1} \circ R$ 是一个绕某个中心的旋转，有不动点，矛盾）。

更精确地：$T = S^{-1} \circ R$ 是平移加旋转。若 $R$ 的旋转角 $\theta \neq 0$，则 $T$ 等价于绕某个平移后的中心旋转 $\theta$，仍有不动点——与假设矛盾。故 $R = \text{id}$，$T$ 是平移。$\blacksquare$
