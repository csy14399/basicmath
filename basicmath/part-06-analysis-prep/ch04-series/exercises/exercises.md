# 第 4 章 级数 — 练习题

## §1 无穷级数

1. ★☆☆ 判断以下级数的敛散性，若收敛则求和：
   (a) $\displaystyle\sum_{n=0}^{\infty}\left(\frac{2}{5}\right)^n$
   (b) $\displaystyle\sum_{n=1}^{\infty}\frac{3^n}{4^n}$
   (c) $\displaystyle\sum_{n=0}^{\infty}(-1)^n \cdot 2^n$

2. ★☆☆ 用伸缩级数方法求以下级数的和：
   (a) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(n+1)}$
   (b) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{(2n-1)(2n+1)}$

3. ★☆☆ 将以下循环小数写为分数：
   (a) $0.\overline{3}$
   (b) $0.\overline{12}$
   (c) $0.1\overline{6}$

4. ★☆☆ 用发散判别法证明以下级数发散：
   (a) $\displaystyle\sum_{n=1}^{\infty}\frac{2n}{n+3}$
   (b) $\displaystyle\sum_{n=1}^{\infty}\cos\frac{1}{n}$
   (c) $\displaystyle\sum_{n=1}^{\infty}(-1)^n$

5. ★★☆ 判断以下 $p$-级数的敛散性：
   (a) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{1.01}}$
   (b) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{0.99}}$
   (c) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n\sqrt{n}}$

6. ★★☆ 求 $\displaystyle\sum_{n=1}^{\infty}\frac{2^n + 1}{3^n}$ 的和。

7. ★★☆ 证明：若 $\sum a_n$ 收敛，则 $\sum a_n^2$ 不一定收敛。（提示：$a_n = 1/\sqrt{n}$ 不行——为什么？找一个 $a_n$ 使 $\sum a_n$ 收敛。）反过来，若 $a_n \geq 0$ 且 $\sum a_n$ 收敛，证明 $\sum a_n^2$ 收敛。

8. ★★☆ 证明伸缩级数 $\displaystyle\sum_{n=1}^{\infty}(\sqrt{n+1} - \sqrt{n})$ 发散。

9. ★★★ 证明 $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n(n+1)(n+2)(n+3)} = \frac{1}{18}$。

---

## §2 收敛判别法

1. ★☆☆ 用比较判别法判断以下级数的敛散性：
   (a) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2 + n}$
   (b) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{2^n + n}$
   (c) $\displaystyle\sum_{n=2}^{\infty}\frac{1}{\sqrt{n} - 1}$

2. ★☆☆ 用极限比较判别法判断以下级数的敛散性：
   (a) $\displaystyle\sum_{n=1}^{\infty}\frac{n^2+1}{n^4+3}$
   (b) $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2 + \sin n}$
   (c) $\displaystyle\sum_{n=1}^{\infty}\frac{3n+2}{n^2+n+1}$

3. ★★☆ 用比值判别法判断以下级数的敛散性：
   (a) $\displaystyle\sum_{n=1}^{\infty}\frac{n!}{10^n}$
   (b) $\displaystyle\sum_{n=1}^{\infty}\frac{2^n}{n^3}$
   (c) $\displaystyle\sum_{n=0}^{\infty}\frac{n^2}{3^n}$
   (d) $\displaystyle\sum_{n=1}^{\infty}\frac{(2n)!}{(n!)^2 \cdot 4^n}$

4. ★★☆ 用根值判别法判断以下级数的敛散性：
   (a) $\displaystyle\sum_{n=1}^{\infty}\left(\frac{n+1}{3n}\right)^n$
   (b) $\displaystyle\sum_{n=1}^{\infty}\frac{2^n}{n^n}$
   (c) $\displaystyle\sum_{n=1}^{\infty}\left(\frac{\ln n}{n}\right)^n$

5. ★★☆ 用 Leibniz 判别法判断以下交错级数的敛散性：
   (a) $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2}$
   (b) $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n \sqrt{n}}{n+1}$
   (c) $\displaystyle\sum_{n=2}^{\infty}\frac{(-1)^n}{\ln n}$

6. ★★☆ 对以下级数，判断是绝对收敛、条件收敛还是发散：
   (a) $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{n^3}$
   (b) $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{n^{1/3}}$
   (c) $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n n}{n+1}$
   (d) $\displaystyle\sum_{n=1}^{\infty}\frac{\cos(n\pi)}{n^2}$

7. ★★★ 证明：若 $a_n > 0$，$a_n$ 单调递减，且 $\sum a_n$ 收敛，则 $na_n \to 0$。（提示：Cauchy 凝聚判别法。）

8. ★★★ 证明 $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n(\ln n)^2}$ 收敛。（提示：用 Cauchy 凝聚判别法，或与积分 $\int 1/(x(\ln x)^2)\,dx$ 类比。）

---

## §3 幂级数初步

1. ★☆☆ 求以下幂级数的收敛半径：
   (a) $\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{2^n}$
   (b) $\displaystyle\sum_{n=0}^{\infty}n \cdot x^n$
   (c) $\displaystyle\sum_{n=0}^{\infty}\frac{x^n}{n!}$
   (d) $\displaystyle\sum_{n=1}^{\infty}\frac{x^n}{n^2}$

2. ★☆☆ 写出以下函数的 Maclaurin 展开（Taylor 展开以 $0$ 为中心），并标注收敛半径：
   (a) $f(x) = e^{-x^2}$
   (b) $f(x) = \dfrac{1}{1+x^2}$
   (c) $f(x) = x\sin x$

3. ★★☆ 求 $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}x^{2n}}{n}$ 的收敛半径和收敛域。这个级数表示什么函数？

4. ★★☆ 用 Taylor 展开计算 $\sqrt{e}$ 的近似值（取前 6 项），并估计误差。

5. ★★☆ 利用 $\dfrac{1}{1-x} = \sum x^n$ 求以下函数的幂级数展开：
   (a) $\dfrac{1}{(1-x)^2}$（提示：对两边求导）
   (b) $\dfrac{x}{(1-x)^2}$

6. ★★☆ 求 $\displaystyle\sum_{n=1}^{\infty}\frac{n}{2^n}$ 的值。（提示：利用上题结果，取 $x = 1/2$。）

7. ★★★ 利用 $\ln(1+x) = \sum (-1)^{n+1}x^n/n$ 证明：
   $$\ln 2 = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots$$

8. ★★★ 设 $\displaystyle f(x) = \sum_{n=0}^{\infty}a_n x^n$，收敛半径 $R > 0$。若 $f(x) = 0$ 对所有 $|x| < R$ 成立，证明 $a_n = 0$ 对所有 $n$ 成立。
