# 第 4 章 反三角函数 — 挑战题（Challenge Problems）

以下挑战题综合运用反三角函数和三角恒等式的深层知识。

---

## 挑战题 1：Machin 公式与 $\pi$ 的计算

### 背景

1706 年，英国数学家 John Machin 用以下公式计算出 $\pi$ 的 100 位小数：

$$\frac{\pi}{4} = 4\arctan\frac{1}{5} - \arctan\frac{1}{239}$$

### 任务

(a) 证明 Machin 公式。

(b) 解释为什么这个公式比 $\frac{\pi}{4} = \arctan 1$ 更适合数值计算。

### 提示

反复使用 $\arctan$ 加法公式。先计算 $2\arctan\frac{1}{5}$，再计算 $4\arctan\frac{1}{5}$，最后减去 $\arctan\frac{1}{239}$。

### 解答

**步骤 1**：$2\arctan\frac{1}{5}$。

$$2\arctan\frac{1}{5} = \arctan\frac{2 \cdot \frac{1}{5}}{1 - \frac{1}{25}} = \arctan\frac{2/5}{24/25} = \arctan\frac{10}{24} = \arctan\frac{5}{12}$$

**步骤 2**：$4\arctan\frac{1}{5} = 2 \cdot 2\arctan\frac{1}{5} = 2\arctan\frac{5}{12}$。

$$2\arctan\frac{5}{12} = \arctan\frac{2 \cdot \frac{5}{12}}{1 - \frac{25}{144}} = \arctan\frac{10/12}{119/144} = \arctan\frac{120}{119}$$

**步骤 3**：$4\arctan\frac{1}{5} - \arctan\frac{1}{239}$。

注意 $\frac{120}{119} > 0$ 且 $\frac{1}{239} > 0$，但这里是减法。

$$4\arctan\frac{1}{5} - \arctan\frac{1}{239} = \arctan\frac{120}{119} - \arctan\frac{1}{239}$$

$$= \arctan\frac{\frac{120}{119} - \frac{1}{239}}{1 + \frac{120}{119}\cdot\frac{1}{239}}$$

分子：$\frac{120 \cdot 239 - 119}{119 \cdot 239} = \frac{28680 - 119}{28441} = \frac{28561}{28441}$。

分母：$1 + \frac{120}{119 \cdot 239} = \frac{28441 + 120}{28441} = \frac{28561}{28441}$。

$$= \arctan\frac{28561/28441}{28561/28441} = \arctan 1 = \frac{\pi}{4}$$

$\blacksquare$

**(b)** 用 Taylor 级数 $\arctan x = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots$ 计算时，$x$ 越小，级数收敛越快。$\arctan 1$ 的级数（Leibniz 公式 $\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \cdots$）收敛极其缓慢——需要数百万项才能得到几位精度。而 $\arctan\frac{1}{5}$ 和 $\arctan\frac{1}{239}$ 的级数收敛非常快，因为 $\frac{1}{5}$ 和 $\frac{1}{239}$ 远小于 $1$。

---

## 挑战题 2：反三角函数的无穷级数

### 问题

证明以下恒等式：

$$\sum_{k=1}^{n} \arctan\frac{1}{2k^2} = \arctan\frac{n}{n+1}$$

### 提示

用 $\arctan$ 加法公式证明 $\arctan\frac{1}{2k^2} = \arctan(k+1) - \arctan k$，然后用伸缩求和（telescoping sum）。

### 解答

**关键观察**：我们需要验证 $\arctan\frac{1}{2k^2} = \arctan(k+1) - \arctan k$。

由 $\arctan$ 减法公式（当 $ab > -1$ 时）：

$$\arctan a - \arctan b = \arctan\frac{a-b}{1+ab}$$

取 $a = k+1$，$b = k$：

$$\arctan(k+1) - \arctan k = \arctan\frac{(k+1)-k}{1+k(k+1)} = \arctan\frac{1}{1+k^2+k}$$

等等，我们得到的是 $\frac{1}{k^2+k+1}$，而不是 $\frac{1}{2k^2}$。让我们重新考虑。

实际上，正确的分解是：

$$\arctan\frac{1}{2k^2} = \arctan(2k+1) - \arctan(2k-1)$$

验证：

$$\arctan(2k+1) - \arctan(2k-1) = \arctan\frac{(2k+1)-(2k-1)}{1+(2k+1)(2k-1)} = \arctan\frac{2}{1+4k^2-1} = \arctan\frac{2}{4k^2} = \arctan\frac{1}{2k^2}$$

✓

因此：

$$\sum_{k=1}^{n}\arctan\frac{1}{2k^2} = \sum_{k=1}^{n}\left[\arctan(2k+1) - \arctan(2k-1)\right]$$

这是伸缩求和：

$$= \arctan(2n+1) - \arctan 1 = \arctan(2n+1) - \frac{\pi}{4}$$

但我们需要证明这等于 $\arctan\frac{n}{n+1}$。

$$\arctan(2n+1) - \frac{\pi}{4} = \arctan\frac{(2n+1)-1}{1+(2n+1)\cdot 1} = \arctan\frac{2n}{2n+2} = \arctan\frac{n}{n+1}$$

（使用 $\arctan a - \arctan b = \arctan\frac{a-b}{1+ab}$，其中 $a = 2n+1$，$b = 1$。因为 $ab = 2n+1 > 0$，条件满足。）

$\blacksquare$

**推论**：令 $n \to \infty$：

$$\sum_{k=1}^{\infty}\arctan\frac{1}{2k^2} = \lim_{n \to \infty}\arctan\frac{n}{n+1} = \arctan 1 = \frac{\pi}{4}$$

这给出了 $\frac{\pi}{4}$ 的另一个级数表示。
