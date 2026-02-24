# 第 2 章 实数的深入 — 挑战题

以下题目超出常规练习的难度，适合深入探索。

---

**C1.** ★★★★ 证明：$\mathbb{R}$ 中不存在最小的正实数。进一步，证明对任意 $\varepsilon > 0$，存在 $\delta > 0$ 使得 $\delta < \varepsilon$。（这个结论看似显然，但请从有序域公理和阿基米德性质出发严格证明。）

<details>
<summary>提示</summary>

对第一部分，假设 $\varepsilon_0 > 0$ 是最小正实数，考虑 $\varepsilon_0 / 2$。对第二部分，取 $\delta = \varepsilon / 2$。
</details>

<details>
<summary>解答</summary>

假设存在最小正实数 $\varepsilon_0 > 0$。则 $\varepsilon_0 / 2 > 0$（由有序域公理，$\varepsilon_0 > 0$ 且 $1/2 > 0$，故 $\varepsilon_0 / 2 > 0$）。又 $\varepsilon_0 / 2 < \varepsilon_0$，与 $\varepsilon_0$ 的最小性矛盾。

对第二部分：给定 $\varepsilon > 0$，取 $\delta = \varepsilon / 2$。则 $\delta > 0$（同上）且 $\delta = \varepsilon/2 < \varepsilon$。$\blacksquare$
</details>

---

**C2.** ★★★★ 设 $S \subseteq \mathbb{R}$ 非空有上界，$\alpha = \sup S$。证明：存在序列 $\{s_n\} \subseteq S$ 使得 $s_n \to \alpha$（即 $\lim_{n\to\infty} s_n = \alpha$）。

（这需要你使用极限的 $\varepsilon$-$N$ 定义：$s_n \to \alpha$ 意味着对任意 $\varepsilon > 0$，存在 $N \in \mathbb{N}$ 使得当 $n > N$ 时 $|s_n - \alpha| < \varepsilon$。）

<details>
<summary>提示</summary>

对每个 $n \in \mathbb{N}^+$，取 $\varepsilon = 1/n$，利用上确界的逼近性质选取 $s_n$。
</details>

<details>
<summary>解答</summary>

对每个 $n \in \mathbb{N}^+$，由上确界的逼近性质（命题 2），存在 $s_n \in S$ 使得 $\alpha - 1/n < s_n \leq \alpha$。

现在验证 $s_n \to \alpha$。给定 $\varepsilon > 0$，由阿基米德性质，存在 $N \in \mathbb{N}^+$ 使得 $1/N < \varepsilon$。则当 $n \geq N$ 时：

$$|s_n - \alpha| = \alpha - s_n < 1/n \leq 1/N < \varepsilon$$

故 $s_n \to \alpha$。$\blacksquare$
</details>

---

**C3.** ★★★★★ 在 Dedekind 切割的框架下，定义两个切割 $(L_1, R_1)$ 和 $(L_2, R_2)$ 的**加法**，并证明加法的结合律。

<details>
<summary>提示</summary>

定义 $L_1 + L_2 = \{\ell_1 + \ell_2 : \ell_1 \in L_1, \ell_2 \in L_2\}$，$R = \mathbb{Q} \setminus (L_1 + L_2)$。需要验证 $(L_1 + L_2, R)$ 是合法的 Dedekind 切割。
</details>

<details>
<summary>解答</summary>

**定义**：设 $(L_1, R_1)$ 和 $(L_2, R_2)$ 是两个 Dedekind 切割。定义

$$L = \{\ell_1 + \ell_2 : \ell_1 \in L_1,\; \ell_2 \in L_2\}, \quad R = \mathbb{Q} \setminus L$$

**验证 $(L, R)$ 是 Dedekind 切割**：

(D1) 取 $\ell_1 \in L_1, \ell_2 \in L_2$，则 $\ell_1 + \ell_2 \in L$，故 $L \neq \varnothing$。取 $r_1 \in R_1, r_2 \in R_2$，则 $r_1 + r_2 \in R$（否则 $r_1 + r_2 = \ell_1 + \ell_2$ 对某些 $\ell_i \in L_i$，则 $r_1 - \ell_1 = \ell_2 - r_2$，但左边 $\geq 0$（$r_1 \geq$ 所有 $\ell_1$）右边 $< 0$（$\ell_2 < r_2$），矛盾——除非等于 $0$，此时 $r_1 = \ell_1$ 和 $\ell_2 = r_2$，但 $L_i \cap R_i = \varnothing$）。故 $R \neq \varnothing$。

(D2)(D3) 由定义。

(D4) 设 $\ell \in L, r \in R$。则 $\ell = \ell_1 + \ell_2$。假设 $r \leq \ell$。则 $r = \ell_1 + (\ell_2 - (\ell - r))$。因 $\ell - r \geq 0$，$\ell_2 - (\ell - r) \leq \ell_2 \in L_2$（$L_2$ 对小于其元素的有理数封闭），故 $r \in L$，与 $r \in R$ 矛盾。

(D5) 设 $\ell = \ell_1 + \ell_2 \in L$。因 $L_1$ 无最大元素，存在 $\ell_1' \in L_1$ 使 $\ell_1' > \ell_1$。则 $\ell_1' + \ell_2 > \ell$ 且 $\ell_1' + \ell_2 \in L$。

**结合律**：设三个切割分别对应 $L_1, L_2, L_3$。

$(L_1 + L_2) + L_3 = \{(\ell_1 + \ell_2) + \ell_3 : \ell_i \in L_i\} = \{\ell_1 + \ell_2 + \ell_3 : \ell_i \in L_i\}$

$L_1 + (L_2 + L_3) = \{\ell_1 + (\ell_2 + \ell_3) : \ell_i \in L_i\} = \{\ell_1 + \ell_2 + \ell_3 : \ell_i \in L_i\}$

由有理数加法的结合律，两个集合相等。$\blacksquare$
</details>
