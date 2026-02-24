# 第 3 章 随机变量与分布 — 挑战题（Challenge Problems）

---

## 挑战题 1：赠券收集问题（Coupon Collector's Problem）

> **题目**：一种零食有 $n$ 种不同的赠券，每次购买随机得到一张（等概率，独立）。平均需要购买多少次才能集齐所有 $n$ 种赠券？

### 解答

设 $T$ = 集齐所有赠券的购买次数。将过程分阶段：

- **阶段 $i$**：已经有 $i-1$ 种不同赠券，等待得到第 $i$ 种新赠券。

在阶段 $i$，每次购买得到新赠券的概率为 $(n-i+1)/n$。所以阶段 $i$ 的等待时间 $T_i \sim \text{Geom}((n-i+1)/n)$。

$$T = T_1 + T_2 + \cdots + T_n$$

$$E[T] = \sum_{i=1}^{n} E[T_i] = \sum_{i=1}^{n} \frac{n}{n-i+1} = n \sum_{j=1}^{n} \frac{1}{j} = n \cdot H_n$$

其中 $H_n = 1 + 1/2 + 1/3 + \cdots + 1/n$ 是第 $n$ 个调和数（harmonic number）。

$H_n \approx \ln n + \gamma$（$\gamma \approx 0.5772$ 是 Euler-Mascheroni 常数）。

**例子**：集齐 $n = 50$ 种赠券平均需要 $50 \times H_{50} \approx 50 \times 4.499 \approx 225$ 次购买。

---

## 挑战题 2：Poisson 过程的叠加

> **题目**：设 $X \sim \text{Poi}(\lambda)$，$Y \sim \text{Poi}(\mu)$，$X$ 和 $Y$ 独立。证明 $X + Y \sim \text{Poi}(\lambda + \mu)$。

### 解答

$$P(X + Y = k) = \sum_{j=0}^{k} P(X = j) P(Y = k-j)$$

$$= \sum_{j=0}^{k} \frac{\lambda^j e^{-\lambda}}{j!} \cdot \frac{\mu^{k-j} e^{-\mu}}{(k-j)!} = e^{-(\lambda+\mu)} \sum_{j=0}^{k} \frac{\lambda^j \mu^{k-j}}{j!(k-j)!}$$

$$= \frac{e^{-(\lambda+\mu)}}{k!} \sum_{j=0}^{k} \binom{k}{j} \lambda^j \mu^{k-j} = \frac{e^{-(\lambda+\mu)}}{k!} (\lambda + \mu)^k$$

这正是 $\text{Poi}(\lambda + \mu)$ 的 PMF。$\blacksquare$

物理意义：如果两个独立的 Poisson 过程（速率分别为 $\lambda$ 和 $\mu$）合并，结果仍是 Poisson 过程，速率为 $\lambda + \mu$。
