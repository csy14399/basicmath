# 第 4 章 期望与方差 — 挑战题（Challenge Problems）

---

## 挑战题 1：Jensen 不等式

> **题目**：设 $g$ 是**凸函数**（convex），$X$ 是随机变量。证明
>
> $$g(E[X]) \leq E[g(X)]$$

### 解答

凸函数的定义：对任意 $x_0$，存在支撑线 $l(x) = g(x_0) + g'(x_0)(x - x_0)$ 使得 $g(x) \geq l(x)$ 对所有 $x$ 成立。

取 $x_0 = E[X] = \mu$。则 $g(X) \geq g(\mu) + g'(\mu)(X - \mu)$。

取期望：$E[g(X)] \geq g(\mu) + g'(\mu) E[X - \mu] = g(\mu) + g'(\mu) \cdot 0 = g(\mu) = g(E[X])$。$\blacksquare$

**推论**：

- $g(x) = x^2$（凸）$\Rightarrow$ $(E[X])^2 \leq E[X^2]$，即 $\text{Var}(X) = E[X^2] - (E[X])^2 \geq 0$。
- $g(x) = -\ln x$（凸）$\Rightarrow$ $-\ln E[X] \leq E[-\ln X]$，即 $\ln E[X] \geq E[\ln X]$（AM-GM 不等式的推广）。

---

## 挑战题 2：协方差与相关系数

> **题目**：定义协方差 $\text{Cov}(X, Y) = E[(X-\mu_X)(Y-\mu_Y)]$ 和相关系数 $\rho = \text{Cov}(X,Y)/(\sigma_X \sigma_Y)$。
>
> 证明 $|\rho| \leq 1$（Cauchy-Schwarz 不等式的概率版）。

### 解答

对任意 $t \in \mathbb{R}$，$\text{Var}(X + tY) \geq 0$。

$$\text{Var}(X + tY) = \text{Var}(X) + 2t\text{Cov}(X,Y) + t^2\text{Var}(Y) \geq 0$$

这是 $t$ 的二次多项式且 $\geq 0$，所以判别式 $\leq 0$：

$$4\text{Cov}(X,Y)^2 - 4\text{Var}(X)\text{Var}(Y) \leq 0$$

$$\text{Cov}(X,Y)^2 \leq \text{Var}(X)\text{Var}(Y)$$

$$\left|\frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}\right| \leq 1 \quad \blacksquare$$

$|\rho| = 1$ 当且仅当 $Y = aX + b$（线性关系）。
