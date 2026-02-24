# 第 5 章 大数定律 — 练习题解答

**1.** $E[\bar{X}_{50}] = 5$。$\text{Var}(\bar{X}_{50}) = 4/50 = 0.08$。

---

**2.** $P(|\bar{X}_{200} - 5| \geq 0.5) \leq \text{Var}(\bar{X}_{200})/0.5^2 = (4/200)/0.25 = 0.02/0.25 = 0.08$。

即不超过 $8\%$。

---

**3.** 需要 $\sigma^2/(n \epsilon^2) \leq \delta$，即 $n \geq \sigma^2/(\epsilon^2 \delta) = 1/(0.01 \times 0.05) = 2000$。

至少 $n = 2000$。

---

**4.** $\sigma^2 = 0.3 \times 0.7 = 0.21$。$\text{Var}(\bar{X}_{1000}) = 0.21/1000 = 0.00021$。

$P(|\bar{X}_{1000} - 0.3| \geq 0.05) \leq 0.00021/0.0025 = 0.084$。

不超过 $8.4\%$。

---

**5.** $\mu = 600$，$\sigma = \sqrt{1000 \times 0.6 \times 0.4} = \sqrt{240} \approx 15.49$。

$P(X \leq 580) = P\!\left(Z \leq \frac{580-600}{15.49}\right) = P(Z \leq -1.29) \approx \Phi(-1.29) \approx 0.099$。

约 $9.9\%$。

---

**6.** $X \sim B(500, 0.02)$，$\mu = 10$，$\sigma = \sqrt{500 \times 0.02 \times 0.98} = \sqrt{9.8} \approx 3.13$。

$P(X > 15) = P\!\left(Z > \frac{15-10}{3.13}\right) = P(Z > 1.60) \approx 1 - 0.9452 = 0.0548$。

约 $5.5\%$。

（也可以用 Poisson 近似：$X \approx \text{Poi}(10)$，$P(X > 15) \approx 0.049$。）

---

**7.** 设每局庄家期望赢利 $= 100 \times 0.02 = 2$ 元。$\mu = 2$。

每局方差估计：假设每局赢/输约 $100$ 元，$\sigma \approx 100$。

日利润期望 $= 10000 \times 2 = 20{,}000$ 元。

日利润标准差 $= 100 \times \sqrt{10000} = 10{,}000$ 元。

由 CLT，日利润 $\approx N(20000, 10000^2)$。

$P(\text{日亏损}) = P(Z < -2) \approx 2.3\%$。

赌场在 $97.7\%$ 的天里盈利。长期来看，大数定律保证累积利润趋近 $20{,}000$ 元/天。

---

**8.** $I = \int_0^1 e^{-x^2}dx = E[e^{-U^2}]$，其中 $U \sim \text{Uniform}(0,1)$。

方法：生成 $U_1, \ldots, U_n \sim \text{Uniform}(0,1)$，计算 $\hat{I} = \frac{1}{n}\sum_{i=1}^n e^{-U_i^2}$。

误差分析：$g(U) = e^{-U^2}$，$E[g(U)] = I$，$\text{Var}(g(U)) = E[e^{-2U^2}] - I^2 < 1$。

$\text{SD}(\hat{I}) = \sigma_g / \sqrt{n}$。取 $n = 10{,}000$，误差量级 $\sim 0.01$。

精确值 $I = \frac{\sqrt{\pi}}{2}\text{erf}(1) \approx 0.7468$。

---

**9.** $\hat{p} = 0.55$，$n = 400$。估计标准误 $\text{SE} = \sqrt{\hat{p}(1-\hat{p})/n} = \sqrt{0.2475/400} \approx 0.0249$。

$95\%$ 置信区间：$\hat{p} \pm 1.96 \times \text{SE} = 0.55 \pm 0.049 = [0.501, 0.599]$。

---

**10.** $P(X_n = n^2) = 1/n$，$P(X_n = 0) = 1 - 1/n$。

$X_n \xrightarrow{P} 0$（因为 $P(|X_n| \geq \epsilon) = P(X_n = n^2) = 1/n \to 0$）。

但 $E[X_n] = n^2 \cdot (1/n) + 0 \cdot (1-1/n) = n \to \infty \neq 0$。

期望不收敛到 $0$！原因是大值虽然概率越来越小，但值增长太快，"拉高"了期望。

这说明依概率收敛不保证期望的收敛（需要一致可积性条件）。
