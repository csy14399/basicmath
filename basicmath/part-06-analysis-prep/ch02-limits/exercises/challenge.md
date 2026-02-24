# 第 2 章 极限 — 挑战题（Challenge Problems）

以下挑战题深入探索函数极限的理论，难度超出常规练习。

---

## 挑战题 1：Heine 定理——用数列极限定义函数极限

> **定理**（Heine / 序列判据）
>
> $\displaystyle\lim_{x \to a}f(x) = L$ 当且仅当：对任何满足 $x_n \to a$（$x_n \neq a$）的数列 $\{x_n\}$，都有 $f(x_n) \to L$。

**题目**：

(a) 用 Heine 定理的否定形式证明 $\displaystyle\lim_{x \to 0}\sin\frac{1}{x}$ 不存在。

(b) 讨论 Heine 定理的直觉含义——它建立了数列极限与函数极限之间的什么桥梁？

### 解答

**(a)** Heine 定理的否定：$\lim_{x \to a}f(x) \neq L$（对某个 $L$，或极限不存在）当且仅当存在一个数列 $x_n \to a$（$x_n \neq a$）使得 $f(x_n) \not\to L$。

要证明极限不存在，只需找到两个数列趋于同一点但 $f$ 值趋于不同极限。

取 $x_n = \dfrac{1}{2n\pi}$（$x_n \to 0$），$\sin(1/x_n) = \sin(2n\pi) = 0 \to 0$。

取 $y_n = \dfrac{1}{2n\pi + \pi/2}$（$y_n \to 0$），$\sin(1/y_n) = \sin(2n\pi + \pi/2) = 1 \to 1$。

两个趋于 $0$ 的数列给出不同的 $f$ 值极限（$0$ 和 $1$），故 $\lim_{x \to 0}\sin(1/x)$ 不存在。

**(b)** Heine 定理说：函数极限（连续变量）可以完全用数列极限（离散变量）来刻画。这意味着：

- 要证明函数极限存在，可以"只考虑数列"；
- 要证明不存在，只需找到一个"坏"的数列。

它架起了离散（第一章）与连续（第二章）之间的桥梁，使得我们可以把第一章的所有结果（唯一性、有界性、四则运算、夹逼定理等）直接移植到函数极限上。

---

## 挑战题 2：$\displaystyle\lim_{x \to 0}\frac{\sin(\tan x) - \tan(\sin x)}{x^7}$

**题目**：计算此极限。

### 提示

需要 $\sin x$ 和 $\tan x$ 的 Taylor 展开到足够高的阶。

### 解答

我们需要展开到 $x^7$ 的精度。

已知展开式（$x \to 0$）：

$$\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \frac{x^7}{5040} + O(x^9)$$

$$\tan x = x + \frac{x^3}{3} + \frac{2x^5}{15} + \frac{17x^7}{315} + O(x^9)$$

**计算 $\sin(\tan x)$**：令 $u = \tan x = x + \frac{x^3}{3} + \frac{2x^5}{15} + \frac{17x^7}{315} + \cdots$

$$\sin u = u - \frac{u^3}{6} + \frac{u^5}{120} - \frac{u^7}{5040} + \cdots$$

展开到 $x^7$（仔细计算 $u^3, u^5, u^7$ 的低阶项）：

$u^3 = x^3 + x^5 + \frac{17x^7}{15} + \cdots$（保留到 $x^7$）

$u^5 = x^5 + \cdots$，$u^7 = x^7 + \cdots$

$$\sin(\tan x) = x + \frac{x^3}{3} + \frac{2x^5}{15} + \frac{17x^7}{315} - \frac{x^3 + x^5 + \frac{17x^7}{15}}{6} + \frac{x^5}{120} - \frac{x^7}{5040} + \cdots$$

$$= x + \frac{x^3}{3} - \frac{x^3}{6} + x^5\left(\frac{2}{15} - \frac{1}{6} + \frac{1}{120}\right) + x^7\left(\frac{17}{315} - \frac{17}{90} - \frac{1}{5040}\right) + \cdots$$

$$= x + \frac{x^3}{6} + x^5\left(\frac{16 - 20 + 1}{120}\right) + \cdots = x + \frac{x^3}{6} - \frac{x^5}{40} + \cdots$$

**计算 $\tan(\sin x)$**：令 $v = \sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots$

$$\tan v = v + \frac{v^3}{3} + \frac{2v^5}{15} + \frac{17v^7}{315} + \cdots$$

类似地展开。

$$\tan(\sin x) = x - \frac{x^3}{6} + \frac{x^5}{120} + \frac{x^3 - x^5/2 + \cdots}{3} + \frac{2x^5}{15} + \cdots$$

$$= x + \frac{x^3}{3} - \frac{x^3}{6} + x^5\left(\frac{1}{120} - \frac{1}{6} + \frac{2}{15}\right) + \cdots$$

$$= x + \frac{x^3}{6} - \frac{x^5}{40} + \cdots$$

这两个表达式的前几项相同！差异出现在 $x^7$ 项。经过完整计算（此处省略冗长的高阶展开细节）：

$$\sin(\tan x) - \tan(\sin x) = -\frac{x^7}{30} + O(x^9)$$

因此：

$$\lim_{x \to 0}\frac{\sin(\tan x) - \tan(\sin x)}{x^7} = -\frac{1}{30}$$

此题展示了 Taylor 展开在精确极限计算中的强大威力。当等价无穷小和简单代数技巧失效时，Taylor 展开是终极工具。
