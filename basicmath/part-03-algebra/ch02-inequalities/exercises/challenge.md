# 第 2 章 不等式 — 挑战题（Challenge Problems）

以下挑战题综合运用经典不等式，难度超出常规练习。

---

## 挑战题 1：Schur 不等式

设 $a, b, c \geq 0$ 且 $t \geq 0$。证明 **Schur 不等式**：

$$a^t(a - b)(a - c) + b^t(b - a)(b - c) + c^t(c - a)(c - b) \geq 0$$

特别地，当 $t = 1$ 时：

$$a^3 + b^3 + c^3 + abc \geq ab(a + b) + bc(b + c) + ca(c + a)$$

等价地（设 $p = a + b + c$，$q = ab + bc + ca$，$r = abc$）：

$$p^3 - 4pq + 9r \geq 0$$

### 提示

- 不妨设 $a \geq b \geq c \geq 0$（对称性）。
- 提取公因式，注意各项的符号。

### 解答

不妨设 $a \geq b \geq c \geq 0$。

$$S = a(a-b)(a-c) + b(b-a)(b-c) + c(c-a)(c-b)$$

$a - b \geq 0$，$a - c \geq 0$，$b - c \geq 0$，$b - a \leq 0$，$c - a \leq 0$，$c - b \leq 0$。

所以第一项 $\geq 0$，第三项 $\geq 0$（两个负因子），第二项 $\leq 0$。

改写：

$$S = a(a-b)(a-c) + c(a-c)(b-c) - b(a-b)(b-c)$$

$$= (a-b)[(a)(a-c) - b(b-c)] + c(a-c)(b-c)$$

$$= (a-b)[a^2 - ac - b^2 + bc] + c(a-c)(b-c)$$

$$= (a-b)[(a^2 - b^2) - c(a - b)] + c(a-c)(b-c)$$

$$= (a-b)^2(a + b - c) + c(a-c)(b-c)$$

- $(a-b)^2 \geq 0$，且 $a + b - c \geq a + b - a = b \geq 0$（因为 $c \leq a$，又 $b \geq c \geq 0$），所以第一项 $\geq 0$。
- $(a - c) \geq 0$，$(b - c) \geq 0$，$c \geq 0$，所以第二项 $\geq 0$。

因此 $S \geq 0$。$\blacksquare$

---

## 挑战题 2：Cauchy-Schwarz 的积分类比

设 $f, g$ 是 $[a, b]$ 上的连续函数。（以下假设你对积分有直觉，不需要严格的积分理论。）

**Cauchy-Schwarz 不等式的积分形式**声称：

$$\left(\int_a^b f(x)g(x)\,dx\right)^2 \leq \left(\int_a^b f(x)^2\,dx\right)\left(\int_a^b g(x)^2\,dx\right)$$

**(a)** 仿照有限和的证明（构造关于 $t$ 的二次函数），说明如何"证明"积分形式的 Cauchy-Schwarz 不等式。

**(b)** 用 (a) 的结果证明：对 $[0, 1]$ 上的连续函数 $f$，

$$\left(\int_0^1 f(x)\,dx\right)^2 \leq \int_0^1 f(x)^2\,dx$$

### 解答大纲

**(a)** 构造 $h(t) = \int_a^b [f(x) - tg(x)]^2\,dx \geq 0$（被积函数非负，积分非负）。

展开：$h(t) = \int f^2 - 2t\int fg + t^2\int g^2$。

这是 $t$ 的二次函数（若 $\int g^2 > 0$），$h(t) \geq 0$ 对一切 $t$ 成立。

判别式 $\Delta \leq 0$：$4(\int fg)^2 - 4(\int f^2)(\int g^2) \leq 0$，即

$$\left(\int fg\right)^2 \leq \left(\int f^2\right)\left(\int g^2\right)$$

**(b)** 取 $g(x) = 1$，$a = 0$，$b = 1$：

$$\left(\int_0^1 f(x) \cdot 1\,dx\right)^2 \leq \left(\int_0^1 f(x)^2\,dx\right)\left(\int_0^1 1^2\,dx\right) = \int_0^1 f(x)^2\,dx$$

---

## 挑战题 3：等周不等式的代数版本

在平面上，一个 $n$ 边形的顶点为 $(x_1, y_1), \ldots, (x_n, y_n)$（按顺序排列）。

**(a)** 设 $n$ 边形的周长为 $L$，面积为 $A$。**等周不等式**（isoperimetric inequality）声称

$$4\pi A \leq L^2$$

等号成立当且仅当图形是圆。

对于给定周长 $L$，面积最大的 $n$ 边形是什么形状？（不需严格证明，只需给出答案并用 AM-GM 或其他不等式给出直觉论证。）

**(b)** 对于**正 $n$ 边形**（所有边等长、所有角相等），边长为 $s$ 时面积为 $A_n = \frac{ns^2}{4}\cot\frac{\pi}{n}$。验证当 $n \to \infty$ 时，$\frac{4\pi A_n}{L_n^2} \to 1$（趋向等周不等式的等号条件），其中 $L_n = ns$。

### 解答大纲

**(a)** 给定周长 $L$ 的 $n$ 边形中，面积最大的是**正 $n$ 边形**。

直觉论证：由对称性和 AM-GM 不等式的精神（"均匀分配时极值最优"），所有边等长时面积最大；进一步，所有内角也应相等。

**(b)** $L_n = ns$，$A_n = \frac{ns^2}{4}\cot\frac{\pi}{n}$。

$$\frac{4\pi A_n}{L_n^2} = \frac{4\pi \cdot \frac{ns^2}{4}\cot\frac{\pi}{n}}{n^2 s^2} = \frac{\pi \cot\frac{\pi}{n}}{n} = \frac{\pi}{n} \cdot \frac{\cos\frac{\pi}{n}}{\sin\frac{\pi}{n}}$$

$$= \frac{\frac{\pi}{n}}{\sin\frac{\pi}{n}} \cdot \cos\frac{\pi}{n}$$

当 $n \to \infty$：$\frac{\pi}{n} \to 0$，$\frac{\pi/n}{\sin(\pi/n)} \to 1$，$\cos\frac{\pi}{n} \to 1$。

所以 $\frac{4\pi A_n}{L_n^2} \to 1$。

这表明正 $n$ 边形在 $n \to \infty$ 时趋向于圆，等周不等式的等号"几乎"成立。$\blacksquare$
