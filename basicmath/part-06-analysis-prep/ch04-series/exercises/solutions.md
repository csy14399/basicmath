# 第 4 章 级数 — 练习题解答

## §1 无穷级数

**1.**
(a) 几何级数，$a = 1$, $r = 2/5$。$|r| < 1$，收敛。$\sum = 1/(1-2/5) = 5/3$。

(b) $\sum (3/4)^n$（从 $n=1$ 开始）= $(3/4)/(1-3/4) = 3$。或 $\sum_{n=0}^{\infty}(3/4)^n - 1 = 4 - 1 = 3$。

(c) $a_n = (-1)^n \cdot 2^n$。$|a_n| = 2^n \to \infty \neq 0$。由发散判别法，**发散**。

---

**2.**
(a) $\dfrac{1}{n(n+1)} = \dfrac{1}{n} - \dfrac{1}{n+1}$。$S_n = 1 - \dfrac{1}{n+1} \to 1$。

(b) $\dfrac{1}{(2n-1)(2n+1)} = \dfrac{1}{2}\left(\dfrac{1}{2n-1} - \dfrac{1}{2n+1}\right)$。

$S_n = \dfrac{1}{2}\left(1 - \dfrac{1}{2n+1}\right) \to \dfrac{1}{2}$。

---

**3.**
(a) $0.\overline{3} = 3/10 + 3/100 + \cdots = \dfrac{3/10}{1-1/10} = \dfrac{1}{3}$。

(b) $0.\overline{12} = 12/100 + 12/10000 + \cdots = \dfrac{12/100}{1-1/100} = \dfrac{12}{99} = \dfrac{4}{33}$。

(c) $0.1\overline{6} = 0.1 + 0.0\overline{6} = 1/10 + \dfrac{6/100}{1-1/10} = 1/10 + 6/90 = 1/10 + 1/15 = 1/6$。

---

**4.**
(a) $\lim \dfrac{2n}{n+3} = 2 \neq 0$。发散。

(b) $\lim \cos(1/n) = \cos 0 = 1 \neq 0$。发散。

(c) $a_n = (-1)^n$ 不收敛于 $0$（振荡）。发散。

---

**5.**
(a) $p = 1.01 > 1$，**收敛**。

(b) $p = 0.99 < 1$，**发散**。

(c) $\dfrac{1}{n\sqrt{n}} = \dfrac{1}{n^{3/2}}$，$p = 3/2 > 1$，**收敛**。

---

**6.** $\sum \dfrac{2^n+1}{3^n} = \sum (2/3)^n + \sum (1/3)^n = \dfrac{1}{1-2/3} + \dfrac{1}{1-1/3} = 3 + 3/2 = 9/2$。

---

**7.** 若 $a_n = (-1)^{n+1}/n$，则 $\sum a_n = \ln 2$ 收敛，$a_n^2 = 1/n^2$，$\sum 1/n^2$ 收敛。这不行。

取 $a_n = (-1)^{n+1}/\sqrt{n}$。$\sum a_n$ 条件收敛，$a_n^2 = 1/n$，$\sum 1/n$ 发散。

若 $a_n \geq 0$ 且 $\sum a_n$ 收敛：$a_n \to 0$，故存在 $N$ 使 $n \geq N$ 时 $a_n < 1$。则 $a_n^2 < a_n$。由比较判别法 $\sum a_n^2$ 收敛。$\blacksquare$

---

**8.** $S_n = \sum_{k=1}^{n}(\sqrt{k+1}-\sqrt{k}) = \sqrt{n+1} - 1 \to \infty$。**发散**。

---

**9.** 部分分式：$\dfrac{1}{n(n+1)(n+2)(n+3)} = \dfrac{1}{3}\left(\dfrac{1}{n(n+1)(n+2)} - \dfrac{1}{(n+1)(n+2)(n+3)}\right)$。

伸缩：$S = \dfrac{1}{3} \cdot \dfrac{1}{1 \cdot 2 \cdot 3} = \dfrac{1}{18}$。$\blacksquare$

---

## §2 收敛判别法

**1.**
(a) $\dfrac{1}{n^2+n} < \dfrac{1}{n^2}$，$\sum 1/n^2$ 收敛。**收敛**。

(b) $\dfrac{1}{2^n+n} < \dfrac{1}{2^n}$，$\sum 1/2^n$ 收敛。**收敛**。

(c) 对 $n \geq 2$，$\sqrt{n}-1 < \sqrt{n}$，故 $\dfrac{1}{\sqrt{n}-1} > \dfrac{1}{\sqrt{n}}$。$\sum 1/\sqrt{n}$ 发散。**发散**。

---

**2.**
(a) $\lim \dfrac{(n^2+1)/( n^4+3)}{1/n^2} = \lim \dfrac{n^2(n^2+1)}{n^4+3} = 1$。$\sum 1/n^2$ 收敛，**收敛**。

(b) 对大 $n$，$n^2 + \sin n > n^2/2$（因 $|\sin n| \leq 1$），故 $\dfrac{1}{n^2+\sin n} < \dfrac{2}{n^2}$。由比较判别法，**收敛**。

(c) $\lim \dfrac{(3n+2)/(n^2+n+1)}{1/n} = \lim \dfrac{n(3n+2)}{n^2+n+1} = 3$。$\sum 1/n$ 发散，**发散**。

---

**3.**
(a) $\dfrac{a_{n+1}}{a_n} = \dfrac{(n+1)!}{10^{n+1}} \cdot \dfrac{10^n}{n!} = \dfrac{n+1}{10} \to \infty$。$L > 1$，**发散**。

(b) $\dfrac{a_{n+1}}{a_n} = \dfrac{2^{n+1}}{(n+1)^3} \cdot \dfrac{n^3}{2^n} = 2\left(\dfrac{n}{n+1}\right)^3 \to 2$。$L = 2 > 1$，**发散**。

(c) $\dfrac{a_{n+1}}{a_n} = \dfrac{(n+1)^2}{3^{n+1}} \cdot \dfrac{3^n}{n^2} = \dfrac{1}{3}\left(\dfrac{n+1}{n}\right)^2 \to \dfrac{1}{3}$。$L < 1$，**收敛**。

(d) $a_n = \binom{2n}{n}/4^n$。$\dfrac{a_{n+1}}{a_n} = \dfrac{\binom{2n+2}{n+1}}{\binom{2n}{n}} \cdot \dfrac{1}{4} = \dfrac{(2n+2)(2n+1)}{(n+1)^2} \cdot \dfrac{1}{4} = \dfrac{2(2n+1)}{4(n+1)} \to 1$。判别法**失效**。（实际上此级数发散：$\binom{2n}{n}/4^n \sim 1/\sqrt{\pi n}$，与 $\sum 1/\sqrt{n}$ 同阶，发散。）

---

**4.**
(a) $|a_n|^{1/n} = \dfrac{n+1}{3n} \to \dfrac{1}{3}$。$L < 1$，**收敛**。

(b) $|a_n|^{1/n} = \dfrac{2}{n} \to 0$。$L < 1$，**收敛**。

(c) $|a_n|^{1/n} = \dfrac{\ln n}{n} \to 0$。$L < 1$，**收敛**。

---

**5.**
(a) $b_n = 1/n^2$：正、递减、$\to 0$。**收敛**（实际上绝对收敛）。

(b) $b_n = \sqrt{n}/(n+1)$：正；$b_n \to 0$（因 $\sqrt{n}/(n+1) \sim 1/\sqrt{n}$）。$b_n$ 最终递减（$n$ 足够大时 $b_{n+1}/b_n < 1$）。由 Leibniz 判别法，**收敛**。

(c) $b_n = 1/\ln n$：正、递减、$\to 0$。**收敛**。

---

**6.**
(a) $\sum |(-1)^n/n^3| = \sum 1/n^3$，$p = 3 > 1$，收敛。**绝对收敛**。

(b) $\sum |(-1)^n/n^{1/3}| = \sum 1/n^{1/3}$ 发散（$p = 1/3 < 1$）。由 Leibniz 判别法 $\sum (-1)^n/n^{1/3}$ 收敛。**条件收敛**。

(c) $|a_n| = n/(n+1) \to 1 \neq 0$。**发散**。

(d) $\cos(n\pi) = (-1)^n$。$\sum (-1)^n/n^2$。$\sum 1/n^2$ 收敛。**绝对收敛**。

---

**7.** 设 $\sum a_n$ 收敛。$S_{2n} - S_n = a_{n+1} + \cdots + a_{2n}$。因 $a_k$ 递减且为正，$S_{2n} - S_n \geq n \cdot a_{2n}$。由 Cauchy 准则，$S_{2n} - S_n \to 0$，故 $na_{2n} \to 0$。类似地 $(2n+1)a_{2n+1} \leq 2(S_{2n+1} - S_n) \to 0$。故 $na_n \to 0$。$\blacksquare$

---

**8.** Cauchy 凝聚判别法：$\sum a_n$ 与 $\sum 2^n a_{2^n}$ 同敛散。

$2^n a_{2^n} = \dfrac{2^n}{2^n \cdot (\ln 2^n)^2} = \dfrac{1}{(n\ln 2)^2} = \dfrac{1}{n^2 \cdot (\ln 2)^2}$。

$\sum \dfrac{1}{n^2(\ln 2)^2}$ 是 $p = 2$ 的 $p$-级数（乘常数），收敛。所以 $\sum \dfrac{1}{n(\ln n)^2}$ **收敛**。$\blacksquare$

---

## §3 幂级数初步

**1.**
(a) $a_n = 1/2^n$。$|a_{n+1}/a_n| = 1/2$。$R = 2$。

(b) $a_n = n$。$|a_{n+1}/a_n| = (n+1)/n \to 1$。$R = 1$。

(c) $a_n = 1/n!$。$|a_{n+1}/a_n| = 1/(n+1) \to 0$。$R = \infty$。

(d) $a_n = 1/n^2$。$|a_{n+1}/a_n| = n^2/(n+1)^2 \to 1$。$R = 1$。端点：$x = 1$: $\sum 1/n^2$ 收敛；$x = -1$: $\sum (-1)^n/n^2$ 绝对收敛。收敛域 $[-1, 1]$。

---

**2.**
(a) $e^{-x^2} = \sum (-1)^n x^{2n}/n!$，$R = \infty$。

(b) $\dfrac{1}{1+x^2} = \dfrac{1}{1-(-x^2)} = \sum (-1)^n x^{2n}$，$|x^2| < 1$ 即 $|x| < 1$，$R = 1$。

(c) $x\sin x = x \cdot \sum (-1)^n x^{2n+1}/(2n+1)! = \sum (-1)^n x^{2n+2}/(2n+1)!$，$R = \infty$。

---

**3.** $a_n x^{2n}$，令 $u = x^2$。$\sum (-1)^{n+1}u^n/n$，这就是 $\ln(1+u)$。$R_u = 1$，即 $|x^2| < 1$，$R = 1$。

收敛域：$x = 1$: $\sum (-1)^{n+1}/n = \ln 2$ 收敛；$x = -1$: 同样收敛。端点 $x^2 = 1$ 都收敛。收敛域 $[-1, 1]$。

级数表示 $\ln(1+x^2)$。

---

**4.** $\sqrt{e} = e^{1/2} = \sum (1/2)^n/n! = 1 + 1/2 + 1/8 + 1/48 + 1/384 + 1/3840 \approx 1.64872$。

精确值 $\sqrt{e} \approx 1.64872$。误差 $< 1/(6! \cdot 2^6) \approx 2.2 \times 10^{-5}$。

---

**5.**
(a) 对 $\sum x^n = 1/(1-x)$ 两边求导：$\sum nx^{n-1} = 1/(1-x)^2$，$|x| < 1$。

(b) 乘 $x$：$\sum nx^n = x/(1-x)^2$，$|x| < 1$。

---

**6.** 由上题 (b)，$\sum n x^n = x/(1-x)^2$。取 $x = 1/2$：

$$\sum_{n=1}^{\infty}\frac{n}{2^n} = \frac{1/2}{(1/2)^2} = \frac{1/2}{1/4} = 2$$

---

**7.** $\ln(1+x) = \sum_{n=1}^{\infty}(-1)^{n+1}x^n/n$ 在 $x = 1$ 处收敛（Abel 定理保证端点极限等于函数值，或直接由 Leibniz 判别法知级数收敛，且可证其和为 $\ln 2$）。取 $x = 1$：$\ln 2 = 1 - 1/2 + 1/3 - 1/4 + \cdots$。$\blacksquare$

---

**8.** $f(x) = 0$ 意味着 $f(0) = a_0 = 0$。于是 $f(x) = x \cdot g(x)$，其中 $g(x) = \sum a_{n+1}x^n$。$g(x) = f(x)/x = 0$ 对 $x \neq 0$ 成立。由极限连续性 $g(0) = a_1 = 0$。归纳即得 $a_n = 0$ 对所有 $n$ 成立。$\blacksquare$
