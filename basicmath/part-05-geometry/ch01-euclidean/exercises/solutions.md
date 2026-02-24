# 第 1 章 欧氏几何 — 练习题解答

## §1 公理化方法

**1.** 五条公设：(1) 两点确定一条线段；(2) 线段可无限延伸；(3) 以任意点为圆心和半径可画圆；(4) 所有直角相等；(5) 平行公设（同侧内角和小于 $180°$ 则两线相交）。

第五公设与前四条本质不同：它更复杂，更像定理而非公理。它的独立性直到 19 世纪才被证明（通过非欧几何的构造）。

---

**2.** 未定义术语是不通过其他术语来定义的基本概念（如点、线、面）。它们是必要的，因为定义需要用其他词语解释，若每个词都要定义就会导致无穷回归或循环定义。未定义术语的"含义"完全由公理隐式确定。

---

**3.** Playfair 公理：过直线外一点，恰好可以引一条平行线。它与 Euclid 的第五公设等价——在前四条公设的基础上，两者可以互相推导。

---

**4.** 一致性：不能同时推出 $P$ 和 $\neg P$。独立性：某条公理不能从其余公理推出。完备性：每个命题要么可证要么可否证。

一致性是最基本的——不一致的系统中任何命题都可以被证明（爆炸原理），整个系统毫无意义。

---

**5.** 零条。球面上任意两条大圆（"直线"）都相交于两个对径点，不存在"平行线"。这说明球面几何不满足第五公设（甚至连"至少一条平行线"都不存在），是一种非欧几何（椭圆几何）。

---

**6.** 非欧几何的存在性就是反驳。Lobachevsky / Bolyai / Gauss 构造了否定第五公设但满足前四条公设的一致几何体系（双曲几何）。如果第五公设能从前四条推出，否定它就会导致矛盾，非欧几何不可能一致——但它确实一致（有具体模型，如 Poincaré 圆盘）。因此第五公设不能从前四条推出。

---

**7.**
(a) 球面上不完全成立——对径点对有无穷多条大圆通过，不唯一。
(b) 球面上不成立——球面三角形内角和 $> 180°$。
(c) 球面上不成立——没有平行线。
(d) 球面上成立——直角仍然相等。

因此 (a), (b), (c) 在球面上不成立，(d) 成立。

---

## §2 三角形

**1.** $AB = DE = 5$（边），$\angle B = \angle E = 60°$（夹角），$BC = EF = 7$（边）。这是 **SAS** 条件（两边及夹角），因此 $\triangle ABC \cong \triangle DEF$。

---

**2.** $a = 8$, $b = 15$, $c = 17$。检查：$8^2 + 15^2 = 64 + 225 = 289 = 17^2$。满足 Pythagoras 定理，这是**直角三角形**（直角在 $C$，即 $\angle C = 90°$）。

面积 $= \frac{1}{2} \cdot 8 \cdot 15 = 60$。

---

**3.** $a = 13$, $b = 14$, $c = 15$。$s = \frac{13 + 14 + 15}{2} = 21$。

$S = \sqrt{21 \cdot (21-13) \cdot (21-14) \cdot (21-15)} = \sqrt{21 \cdot 8 \cdot 7 \cdot 6} = \sqrt{7056} = 84$。

---

**4.** $\angle C = 180° - 36° - 72° = 72°$。因为 $\angle B = \angle C = 72°$，三角形是等腰的，$AB = AC$（等角对等边，$\angle B$ 对 $AC$，$\angle C$ 对 $AB$，所以 $\angle B = \angle C \Rightarrow AC = AB$）。

---

**5.** 设等边三角形 $\triangle ABC$（$AB = BC = CA = a$）。从 $A$ 向 $BC$ 作垂线，垂足 $M$。

$\triangle ABM \cong \triangle ACM$（HL：$AB = AC$，$AM = AM$，$\angle AMB = \angle AMC = 90°$）。因此 $BM = CM$，即 $M$ 是 $BC$ 的中点——$AM$ 既是高线也是中线。

$\angle BAM = \angle CAM$，即 $AM$ 也是角平分线。

由对称性，从 $B$ 和 $C$ 出发的特殊线段同样满足此性质。

---

**6.** 由角平分线定理：$\frac{BD}{DC} = \frac{AB}{AC} = \frac{10}{6} = \frac{5}{3}$。

$BD + DC = BC = 8$。设 $BD = 5k$，$DC = 3k$，$5k + 3k = 8$，$k = 1$。

$BD = 5$，$DC = 3$。

---

**7.** 在 $\triangle ABC$ 中，要证 $a < b + c$。延长 $BA$ 至 $D$ 使 $AD = AC$。则 $BD = BA + AD = c + b$。

$\triangle ACD$ 是等腰三角形（$AD = AC$），$\angle ACD = \angle ADC$。

$\angle BCD = \angle BCA + \angle ACD > \angle ACD = \angle ADC = \angle BDC$。

在 $\triangle BCD$ 中，$\angle BCD > \angle BDC$，所以 $BD > BC$（大角对大边），即 $b + c > a$。

---

**8.** $DE \parallel BC$，$\frac{AD}{AB} = \frac{AD}{AD + DB} = \frac{3}{3+6} = \frac{1}{3}$。

由相似（$\triangle ADE \sim \triangle ABC$，AA），$\frac{DE}{BC} = \frac{AD}{AB} = \frac{1}{3}$。

$DE = \frac{1}{3} \times 12 = 4$。

---

**9.** 设 $D$, $E$ 分别是 $AB$, $AC$ 的中点。$\frac{AD}{AB} = \frac{AE}{AC} = \frac{1}{2}$，$\angle A$ 公共。由 SAS 相似，$\triangle ADE \sim \triangle ABC$，比 $k = \frac{1}{2}$。

$DE = \frac{1}{2}BC$ 且 $\angle ADE = \angle ABC$（内错角相等），故 $DE \parallel BC$。$\blacksquare$

---

**10.** 设 $M$ 是 $BC$ 中点。设外心 $O$ 在中线 $AM$ 上。$O$ 到 $B$ 和 $C$ 等距（$O$ 在 $BC$ 中垂线上），$BC$ 中垂线过 $M$ 且垂直于 $BC$。

设垂心 $H$。$AH$ 延长交 $BC$ 于 $D$（$A$ 的垂足），$\angle ADC = 90°$。

在 $AM$ 上取 $G$ 使 $AG : GM = 2 : 1$。需要证明 $O$, $G$, $H$ 共线。

考虑向量方法（设 $O$ 为原点）：$\vec{OH} = \vec{OA} + \vec{OB} + \vec{OC}$（外心到垂心的向量等于三个顶点位置向量之和——可以验证）。

$\vec{OG} = \frac{\vec{OA} + \vec{OB} + \vec{OC}}{3} = \frac{1}{3}\vec{OH}$。

因此 $G$ 在 $OH$ 上，且 $OG : GH = 1 : 2$。$\blacksquare$

---

**11.** 内切圆与三条边 $BC$, $CA$, $AB$ 分别切于 $D$, $E$, $F$。$\triangle ABC$ 被分割为三个小三角形：$\triangle OBC$, $\triangle OCA$, $\triangle OAB$（$O = I$ 内心）。

每个小三角形的底是原三角形的一条边，高是内切圆半径 $r$（内心到每条边的距离为 $r$）。

$S = S_{\triangle IBC} + S_{\triangle ICA} + S_{\triangle IAB} = \frac{1}{2}ar + \frac{1}{2}br + \frac{1}{2}cr = \frac{r(a+b+c)}{2} = rs$。$\blacksquare$

---

**12.** $AB = AC = 10$，$BC = 12$。

(a) 从 $A$ 作 $BC$ 的垂线，垂足 $M$ 是 $BC$ 的中点（等腰三角形）。$BM = 6$。$AM = \sqrt{10^2 - 6^2} = \sqrt{64} = 8$。面积 $= \frac{1}{2} \times 12 \times 8 = 48$。

(b) 先求 $\angle A$。由余弦定理：$\cos A = \frac{10^2 + 10^2 - 12^2}{2 \times 10 \times 10} = \frac{200 - 144}{200} = \frac{56}{200} = \frac{7}{25}$。$\sin A = \sqrt{1 - \frac{49}{625}} = \frac{24}{25}$。

正弦定理：$\frac{a}{\sin A} = 2R$，$\frac{12}{24/25} = 2R$，$R = \frac{12 \times 25}{2 \times 24} = \frac{25}{4}$。

(c) $s = \frac{10 + 10 + 12}{2} = 16$。$r = \frac{S}{s} = \frac{48}{16} = 3$。

---

## §3 圆

**1.** 圆心角 $120°$，圆周角 $= \frac{1}{2} \times 120° = 60°$。

---

**2.** $\angle A = 180° - 40° - 55° = 85°$。弧 $BC$ 的圆心角 $= 2\angle A = 2 \times 85° = 170°$。

---

**3.** 设圆心到弦的距离为 $d$。弦被垂径平分，半弦长 $= 3$。$d = \sqrt{r^2 - 3^2} = \sqrt{25 - 9} = 4$。

---

**4.** 设两弦 $AB$ 和 $CD$ 满足 $AB = CD$。从 $O$ 向 $AB$ 作垂线，垂足 $M$，$OM \perp AB$。从 $O$ 向 $CD$ 作垂线，垂足 $N$，$ON \perp CD$。

$AM = \frac{AB}{2}$，$CN = \frac{CD}{2}$（垂径定理），$AB = CD \Rightarrow AM = CN$。

$OA = OC = r$，$OM = \sqrt{r^2 - AM^2} = \sqrt{r^2 - CN^2} = ON$。$\blacksquare$

---

**5.** 相交弦定理：$PA \cdot PB = PC \cdot PD$。$4 \times 6 = 3 \times PD$，$PD = 8$。

---

**6.** 割线定理：$PA \cdot PB = PC \cdot PD$。$3 \times 12 = 4 \times PD$，$PD = 9$。

---

**7.** 切割线定理：$PT^2 = PA \cdot PB$。$64 = 4 \cdot PB$，$PB = 16$。弦 $AB = PB - PA = 16 - 4 = 12$。

---

**8.** 圆内接四边形对角互补。$\angle A + \angle C = 180°$，$\angle C = 100°$。$\angle B + \angle D = 180°$，$\angle D = 80°$。

---

**9.** 设切线 $\ell$ 切于 $A$，弦 $AB$。设弧 $AB$（不含切线方向的弧）为 $\alpha$。

作直径 $AC$。$\angle ABC = 90°$（Thales 定理）。

弦切角 $\angle(\ell, AB)$ 与 $\angle BAC$ 互余（$\ell \perp OA$，所以切线方向与 $OA$ 垂直）。

$\angle BAC = 90° - \angle ABC'$... 用更直接的方法：

设 $\angle(\ell, AB) = \beta$。连 $OA$，$\ell \perp OA$。$\angle OAB = 90° - \beta$。

$OA = OB = r$，$\triangle OAB$ 等腰，$\angle OBA = \angle OAB = 90° - \beta$。

圆心角 $\angle AOB = 180° - 2(90° - \beta) = 2\beta$。

弧 $AB$ 上的圆周角 $= \frac{1}{2} \angle AOB = \beta = $ 弦切角。$\blacksquare$

---

**10.** 由 Ptolemy 定理：$AC \cdot BD = AB \cdot CD + AD \cdot BC = 3 \times 5 + 6 \times 4 = 15 + 24 = 39$。

因此 $AC \cdot BD = 39$。

---

**11.** 设 $P$ 是圆外一点，$\odot O$ 半径 $r$。过 $P$ 向 $\odot O$ 引切线，切于 $T$。

由切线定义，$PT$ 与 $\odot O$ 只有一个公共点 $T$。切线 $\perp$ 半径 $OT$（之前已证）。

切线长 $= PT = \sqrt{PO^2 - r^2}$（直角三角形 $\triangle OTP$，$\angle OTP = 90°$）。

若从 $P$ 引另一切线切于 $T'$，则 $PT' = \sqrt{PO^2 - r^2} = PT$。$\blacksquare$

---

## §4 面积与体积

**1.**
(a) $S = 12 \times 5 = 60$
(b) $S = \frac{1}{2}(4 + 10) \times 6 = 42$
(c) $S = \pi \times 7^2 = 49\pi$

---

**2.**
(a) $V = 20 \times 8 = 160$
(b) $V = \pi \times 9 \times 10 = 90\pi$
(c) $V = \frac{1}{3}\pi \times 16 \times 9 = 48\pi$

---

**3.** $V = \frac{4}{3}\pi \times 216 = 288\pi$。$S = 4\pi \times 36 = 144\pi$。

---

**4.** $V = \frac{1}{3}\pi r^2 h = 48\pi$，$r = 4$，$\frac{1}{3}\pi \times 16 \times h = 48\pi$，$h = 9$。

---

**5.** 三棱柱（底面积 $A$，高 $h$）可以被分割为三个三棱锥。由 Cavalieri 原理可证这三个三棱锥的体积相等（两两有相同的底面积和高）。三棱柱体积 $= Ah$，每个三棱锥 $= \frac{1}{3}Ah$。因此棱柱与棱锥体积之比 $= Ah : \frac{1}{3}Ah = 3 : 1$。

---

**6.** 立方体：$V = 8$（顶点），$E = 12$（边），$F = 6$（面）。$V - E + F = 8 - 12 + 6 = 2$。✓

体积 $= a^3$，表面积 $= 6a^2$。

---

**7.** 距底面高度 $t$ 处的截面是半径 $\rho = \sqrt{r^2 - t^2}$ 的圆，面积 $= \pi(r^2 - t^2)$。

半球体积 $= \int_0^r \pi(r^2 - t^2)\,dt$（需要积分工具）。

用 Cavalieri 原理：与"圆柱减圆锥"的参照体比较，截面积都是 $\pi(r^2 - t^2)$。

半球体积 $= \pi r^3 - \frac{1}{3}\pi r^3 = \frac{2}{3}\pi r^3$。✓

---

**8.** 在距顶点高度 $t$ 处，截面与底面相似。从顶点到截面的距离为 $t$，到底面的距离为 $h$。由相似比 $k = \frac{t}{h}$，截面的线性尺寸是底面的 $\frac{t}{h}$ 倍，面积为 $A \cdot \left(\frac{t}{h}\right)^2$。$\blacksquare$

---

**9.** 边长 $a$ 的正四面体。底面是边长 $a$ 的正三角形，面积 $A = \frac{\sqrt{3}}{4}a^2$。

底面中心到顶点距离 $= \frac{a}{\sqrt{3}}$。高 $h = \sqrt{a^2 - \frac{a^2}{3}} = a\sqrt{\frac{2}{3}} = \frac{a\sqrt{6}}{3}$。

体积 $= \frac{1}{3} \cdot \frac{\sqrt{3}}{4}a^2 \cdot \frac{a\sqrt{6}}{3} = \frac{a^3\sqrt{18}}{36} = \frac{a^3 \cdot 3\sqrt{2}}{36} = \frac{a^3\sqrt{2}}{12}$。

表面积 $= 4 \times \frac{\sqrt{3}}{4}a^2 = \sqrt{3}\,a^2$。

---

**10.** 正十二面体：$F = 12$（面），每面正五边形（5 条边），每条边被 2 个面共享。$E = \frac{12 \times 5}{2} = 30$。每顶点 3 个面汇聚，每面 5 个顶点。$V = \frac{12 \times 5}{3} = 20$。

Euler 公式：$V - E + F = 20 - 30 + 12 = 2$。✓
