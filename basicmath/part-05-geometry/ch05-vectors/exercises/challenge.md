# 第 5 章 向量几何 — 挑战题（Challenge Problems）

以下挑战题综合运用向量几何的知识，难度超出常规练习。

---

## 挑战题 1：用向量证明 Euler 线

**题目**：用向量方法证明三角形的**外心** $O$、**重心** $G$ 和**垂心** $H$ 共线，且 $G$ 将 $OH$ 按 $1:2$ 分割，即 $\overrightarrow{OG} = \frac{1}{3}\overrightarrow{OH}$。

### 解答

设三角形 $ABC$ 外接圆圆心为 $O$（取为原点），位置向量 $\vec{a} = \overrightarrow{OA}$, $\vec{b} = \overrightarrow{OB}$, $\vec{c} = \overrightarrow{OC}$。

由 $O$ 是外心：$|\vec{a}| = |\vec{b}| = |\vec{c}| = R$（外接圆半径）。

**重心**：$G = \frac{\vec{a}+\vec{b}+\vec{c}}{3}$。

**声明**：垂心 $H = \vec{a} + \vec{b} + \vec{c}$。

**验证**：需证 $\overrightarrow{AH} \perp \overrightarrow{BC}$。

$\overrightarrow{AH} = \vec{a}+\vec{b}+\vec{c} - \vec{a} = \vec{b}+\vec{c}$。

$\overrightarrow{BC} = \vec{c} - \vec{b}$。

$\overrightarrow{AH} \cdot \overrightarrow{BC} = (\vec{b}+\vec{c})\cdot(\vec{c}-\vec{b}) = |\vec{c}|^2 - |\vec{b}|^2 = R^2 - R^2 = 0$。✓

类似可验证 $\overrightarrow{BH} \perp \overrightarrow{AC}$ 和 $\overrightarrow{CH} \perp \overrightarrow{AB}$。

因此 $H = \vec{a}+\vec{b}+\vec{c} = 3G$。

$$\overrightarrow{OG} = G - O = G = \frac{1}{3}(\vec{a}+\vec{b}+\vec{c}) = \frac{1}{3}H = \frac{1}{3}\overrightarrow{OH}$$

$O$, $G$, $H$ 共线，且 $\overrightarrow{OG} = \frac{1}{3}\overrightarrow{OH}$，即 $G$ 将 $OH$ 按 $1:2$ 分割。$\blacksquare$

> 对比 Part 5 Ch01 中用综合方法证明 Euler 线需要较长的推理链。向量证明仅用了几行计算——这展示了选择正确坐标系（以外心为原点）的威力。

---

## 挑战题 2：用混合积求异面直线的距离

**题目**：两条异面直线 $\ell_1$ 和 $\ell_2$ 分别过点 $A_1$, $A_2$，方向向量为 $\vec{d}_1$, $\vec{d}_2$。证明它们之间的距离为：

$$d(\ell_1, \ell_2) = \frac{|\overrightarrow{A_1 A_2} \cdot (\vec{d}_1 \times \vec{d}_2)|}{|\vec{d}_1 \times \vec{d}_2|}$$

并用此公式求直线 $\ell_1: \frac{x-1}{2} = \frac{y}{1} = \frac{z+1}{-1}$ 和 $\ell_2: \frac{x}{1} = \frac{y-1}{-1} = \frac{z-2}{3}$ 的距离。

### 解答

**证明**：

$\vec{n} = \vec{d}_1 \times \vec{d}_2$ 是两条直线的公垂线方向。两条直线之间的距离等于 $\overrightarrow{A_1 A_2}$ 在 $\vec{n}$ 方向上的投影的绝对值：

$$d = |\text{comp}_{\vec{n}}\overrightarrow{A_1 A_2}| = \frac{|\overrightarrow{A_1 A_2} \cdot \vec{n}|}{|\vec{n}|} = \frac{|\overrightarrow{A_1 A_2} \cdot (\vec{d}_1 \times \vec{d}_2)|}{|\vec{d}_1 \times \vec{d}_2|}$$

$\blacksquare$

**应用**：

$A_1 = (1, 0, -1)$, $\vec{d}_1 = (2, 1, -1)$。$A_2 = (0, 1, 2)$, $\vec{d}_2 = (1, -1, 3)$。

$\overrightarrow{A_1 A_2} = (-1, 1, 3)$。

$\vec{d}_1 \times \vec{d}_2 = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 2 & 1 & -1 \\ 1 & -1 & 3 \end{vmatrix} = (3-1, -1-6, -2-1) = (2, -7, -3)$。

$\overrightarrow{A_1 A_2} \cdot (\vec{d}_1 \times \vec{d}_2) = -2 - 7 - 9 = -18$。

$|\vec{d}_1 \times \vec{d}_2| = \sqrt{4+49+9} = \sqrt{62}$。

$$d = \frac{18}{\sqrt{62}} = \frac{18\sqrt{62}}{62} = \frac{9\sqrt{62}}{31}$$

---

## 挑战题 3：向量证明 Ceva 定理

**题目**：用向量方法证明 **Ceva 定理**：

> 在三角形 $ABC$ 中，点 $D$, $E$, $F$ 分别在 $BC$, $CA$, $AB$ 上。$AD$, $BE$, $CF$ 三线共点的充要条件是：
>
> $$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = 1$$

### 解答

设 $A$, $B$, $C$ 的位置向量为 $\vec{a}$, $\vec{b}$, $\vec{c}$。

$D$ 在 $BC$ 上，$BD:DC = \lambda:1$，则 $D = \frac{\vec{c} + \lambda\vec{b}}{1+\lambda} = \frac{\vec{c} + \lambda\vec{b}}{1+\lambda}$。

等等，用更清晰的参数：$D$ 将 $BC$ 按 $BD:DC = p:1$ 分割，$D = \frac{\vec{c} + p\vec{b}}{1+p}$。

类似地：$E$ 将 $CA$ 按 $CE:EA = q:1$ 分割，$F$ 将 $AB$ 按 $AF:FB = r:1$ 分割。

$AD$, $BE$, $CF$ 三线共点于 $P$。

设 $P = \alpha\vec{a} + \beta\vec{b} + \gamma\vec{c}$（重心坐标），$\alpha + \beta + \gamma = 1$。

$P$ 在 $AD$ 上：$P = (1-t)\vec{a} + tD = (1-t)\vec{a} + t\frac{\vec{c}+p\vec{b}}{1+p}$。

比较系数：$\alpha = 1-t$，$\beta = \frac{tp}{1+p}$，$\gamma = \frac{t}{1+p}$。

因此 $p = \frac{\beta}{\gamma}$，即 $BD:DC = \beta:\gamma$。

类似地，$CE:EA = \gamma:\alpha$，$AF:FB = \alpha:\beta$。

$$\frac{BD}{DC} \cdot \frac{CE}{EA} \cdot \frac{AF}{FB} = \frac{\beta}{\gamma} \cdot \frac{\gamma}{\alpha} \cdot \frac{\alpha}{\beta} = 1$$

$\blacksquare$

> 向量证明的优雅之处在于：重心坐标自然地出现，三个比值的乘积因约分而等于 $1$。
