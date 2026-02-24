# 第 1 章 数列 — 挑战题（Challenge Problems）

以下挑战题综合运用数列和极限的知识，难度超出常规练习。

---

## 挑战题 1：Cesàro 均值

> **定理**（Cesàro 均值）
>
> 若 $\lim_{n \to \infty} a_n = L$，则 $\displaystyle\lim_{n \to \infty} \frac{a_1 + a_2 + \cdots + a_n}{n} = L$。

**题目**：证明此定理。然后说明逆命题不成立（给出反例）。

### 提示

将 $\dfrac{1}{n}\sum_{k=1}^{n} a_k - L = \dfrac{1}{n}\sum_{k=1}^{n}(a_k - L)$ 分成前 $N$ 项和后 $n - N$ 项。前 $N$ 项是有限和，除以 $n$ 趋于零；后面的项中每个 $|a_k - L|$ 都小于 $\epsilon$。

### 解答

设 $\epsilon > 0$。由 $a_n \to L$，存在 $N_0$ 使得 $k > N_0$ 时 $|a_k - L| < \epsilon/2$。

$$\left|\frac{1}{n}\sum_{k=1}^{n}(a_k - L)\right| \leq \frac{1}{n}\sum_{k=1}^{N_0}|a_k - L| + \frac{1}{n}\sum_{k=N_0+1}^{n}|a_k - L|$$

$$< \frac{C}{n} + \frac{n - N_0}{n} \cdot \frac{\epsilon}{2}$$

其中 $C = \sum_{k=1}^{N_0}|a_k - L|$ 是固定常数。取 $N_1$ 使得 $n > N_1$ 时 $C/n < \epsilon/2$。

对 $n > \max(N_0, N_1)$：

$$\left|\frac{1}{n}\sum_{k=1}^{n}a_k - L\right| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$

$\blacksquare$

**反例**：$a_n = (-1)^{n+1}$，即 $1, -1, 1, -1, \ldots$。$\{a_n\}$ 发散。

但 Cesàro 均值 $\sigma_n = \dfrac{1}{n}\sum_{k=1}^n a_k$：当 $n$ 为偶数时 $\sigma_n = 0$，当 $n$ 为奇数时 $\sigma_n = 1/n \to 0$。因此 $\sigma_n \to 0$，Cesàro 均值收敛。

故逆命题不成立——Cesàro 均值收敛不意味着原数列收敛。

---

## 挑战题 2：Euler-Mascheroni 常数

**题目**：定义 $\gamma_n = \displaystyle\sum_{k=1}^{n}\frac{1}{k} - \ln n$。

(a) 证明 $\{\gamma_n\}$ 单调递减（$n \geq 1$）。
(b) 证明 $\{\gamma_n\}$ 有下界 $0$。
(c) 由此说明 $\{\gamma_n\}$ 收敛。其极限 $\gamma = \lim_{n \to \infty}\gamma_n$ 称为 **Euler-Mascheroni 常数**，$\gamma \approx 0.5772$。

### 解答

**(a)** $\gamma_{n+1} - \gamma_n = \dfrac{1}{n+1} - \ln(n+1) + \ln n = \dfrac{1}{n+1} - \ln\dfrac{n+1}{n} = \dfrac{1}{n+1} - \ln\left(1 + \dfrac{1}{n}\right)$。

由不等式 $\ln(1+x) > \dfrac{x}{1+x}$（对 $x > 0$），取 $x = 1/n$：

$$\ln\left(1 + \frac{1}{n}\right) > \frac{1/n}{1 + 1/n} = \frac{1}{n+1}$$

因此 $\gamma_{n+1} - \gamma_n < 0$，$\{\gamma_n\}$ 严格递减。

**(b)** 由 $\ln(1+x) \leq x$（对 $x > 0$），有 $\ln\dfrac{k+1}{k} \leq \dfrac{1}{k}$。因此：

$$\ln n = \sum_{k=1}^{n-1}\ln\frac{k+1}{k} \leq \sum_{k=1}^{n-1}\frac{1}{k} < \sum_{k=1}^{n}\frac{1}{k}$$

故 $\gamma_n = \displaystyle\sum_{k=1}^{n}\frac{1}{k} - \ln n > 0$。

**(c)** $\{\gamma_n\}$ 单调递减且有下界 $0$，由单调有界定理收敛。$\blacksquare$

---

## 挑战题 3：嵌套根号

**题目**：定义 $a_1 = \sqrt{2}$，$a_2 = \sqrt{2 + \sqrt{2}}$，$a_3 = \sqrt{2 + \sqrt{2 + \sqrt{2}}}$，一般地 $a_{n+1} = \sqrt{2 + a_n}$。

(a) 证明 $a_n < 2$ 对所有 $n$ 成立。
(b) 证明 $\{a_n\}$ 严格递增。
(c) 由 (a)(b) 推出 $\{a_n\}$ 收敛，并求其极限。
(d) **[挑战]** 证明 $a_n = 2\cos\dfrac{\pi}{2^{n+1}}$，并由此给出极限的另一种推导。

### 解答

**(a)** 归纳法。$a_1 = \sqrt{2} < 2$。若 $a_k < 2$，则 $a_{k+1} = \sqrt{2 + a_k} < \sqrt{2 + 2} = 2$。✓

**(b)** 证 $a_{n+1} > a_n$，等价于 $a_{n+1}^2 > a_n^2$（正数），即 $2 + a_n > a_n^2$，即 $a_n^2 - a_n - 2 < 0$，即 $(a_n - 2)(a_n + 1) < 0$。由 $0 < a_n < 2$，有 $a_n - 2 < 0$ 和 $a_n + 1 > 0$，故乘积 $< 0$。✓

**(c)** 单调递增有上界 $\Rightarrow$ 收敛。设极限 $L = \lim a_n$，由 $a_{n+1} = \sqrt{2 + a_n}$ 取极限：$L = \sqrt{2 + L}$，$L^2 = 2 + L$，$L^2 - L - 2 = 0$，$(L-2)(L+1) = 0$。由 $L > 0$，$L = 2$。

**(d)** 令 $\theta_n = \pi/2^{n+1}$，则 $2\cos\theta_{n+1} = 2\cos(\theta_n/2)$。由半角公式 $\cos(\theta/2) = \sqrt{(1+\cos\theta)/2}$：

$$2\cos\frac{\theta_n}{2} = 2\sqrt{\frac{1+\cos\theta_n}{2}} = \sqrt{2(1+\cos\theta_n)} = \sqrt{2 + 2\cos\theta_n}$$

因此若 $a_n = 2\cos\theta_n$，则 $a_{n+1} = \sqrt{2 + a_n} = \sqrt{2 + 2\cos\theta_n} = 2\cos\theta_{n+1}$。

验证基例：$a_1 = \sqrt{2} = 2\cos(\pi/4)$ ✓。

由归纳法，$a_n = 2\cos\dfrac{\pi}{2^{n+1}}$。

极限：$\lim a_n = 2\cos\left(\lim \dfrac{\pi}{2^{n+1}}\right) = 2\cos 0 = 2$。✓

这给出了一个关于 $\pi$ 的优美无穷积：

$$\frac{\pi}{2} = \prod_{n=1}^{\infty}\frac{1}{\cos(\pi/2^{n+1})}$$

即 Vieta 乘积的一个变体。
