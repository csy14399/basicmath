# 第 5 章 抽象代数初步 — 挑战题（Challenge Problems）

以下挑战题综合运用群论的基本概念，难度超出常规练习。

---

## 挑战题 1：Cayley 定理——每个群都是置换群

> **Cayley 定理**（Arthur Cayley, 1854）
>
> 每个群 $G$ 都同构于某个置换群的子群。

**(a)** 对 $G$ 的每个元素 $g$，定义映射 $\lambda_g : G \to G$，$\lambda_g(x) = gx$（左乘映射）。证明 $\lambda_g$ 是双射（即 $\lambda_g$ 是 $G$ 上的一个置换）。

**(b)** 定义 $\phi : G \to S_G$（$S_G$ 是 $G$ 上的所有置换构成的群），$\phi(g) = \lambda_g$。证明 $\phi$ 是群同态：$\phi(gh) = \phi(g) \circ \phi(h)$。

**(c)** 证明 $\phi$ 是单射，从而 $G$ 同构于 $\phi(G) \leq S_G$。

**(d)** 将此定理应用于 $G = \mathbb{Z}/3\mathbb{Z}$：写出三个左乘映射对应的置换，验证它们构成 $S_3$ 的一个子群。

### 解答

**(a)** 单射：若 $\lambda_g(x) = \lambda_g(y)$，则 $gx = gy$，由消去律 $x = y$。

满射：对任意 $y \in G$，$x = g^{-1}y$ 满足 $\lambda_g(x) = g(g^{-1}y) = y$。$\blacksquare$

**(b)** 对任意 $x \in G$：

$$\phi(gh)(x) = \lambda_{gh}(x) = (gh)x = g(hx) = \lambda_g(\lambda_h(x)) = (\phi(g) \circ \phi(h))(x)$$

因此 $\phi(gh) = \phi(g) \circ \phi(h)$。$\blacksquare$

**(c)** 若 $\phi(g) = \phi(h)$，则 $\lambda_g = \lambda_h$，即对所有 $x$，$gx = hx$。取 $x = e$：$g = h$。$\blacksquare$

**(d)** $G = \{[0], [1], [2]\}$。将元素重命名为 $0, 1, 2$。

$\lambda_{[0]}$：$0 \to 0, 1 \to 1, 2 \to 2$。恒等置换 $e$。

$\lambda_{[1]}$：$0 \to 1, 1 \to 2, 2 \to 0$。循环置换 $(0\;1\;2)$。

$\lambda_{[2]}$：$0 \to 2, 1 \to 0, 2 \to 1$。循环置换 $(0\;2\;1)$。

$\{e, (0\;1\;2), (0\;2\;1)\}$ 构成 $S_3$ 的一个 $3$ 阶子群（即旋转子群），同构于 $\mathbb{Z}/3\mathbb{Z}$。✓

---

## 挑战题 2：群作用的轨道-稳定子定理

设有限群 $G$ 作用于有限集 $X$。对 $x \in X$，定义：

- **轨道**（orbit）：$\text{Orb}(x) = \{g \cdot x : g \in G\}$
- **稳定子**（stabilizer）：$\text{Stab}(x) = \{g \in G : g \cdot x = x\}$

**(a)** 证明 $\text{Stab}(x)$ 是 $G$ 的子群。

**(b)** 证明**轨道-稳定子定理**：$|\text{Orb}(x)| \cdot |\text{Stab}(x)| = |G|$。

**(c)** 应用：等边三角形的顶点集 $X = \{1, 2, 3\}$ 上 $S_3$ 的自然作用。计算顶点 $1$ 的轨道和稳定子，验证定理。

### 解答

**(a)** $e \cdot x = x$，故 $e \in \text{Stab}(x)$，非空。

若 $g, h \in \text{Stab}(x)$，则 $(gh) \cdot x = g \cdot (h \cdot x) = g \cdot x = x$，故 $gh \in \text{Stab}(x)$。

若 $g \in \text{Stab}(x)$，则 $g^{-1} \cdot x = g^{-1} \cdot (g \cdot x) = (g^{-1}g) \cdot x = e \cdot x = x$，故 $g^{-1} \in \text{Stab}(x)$。

由子群判定法，$\text{Stab}(x) \leq G$。$\blacksquare$

**(b)** 定义映射 $f : G/\text{Stab}(x) \to \text{Orb}(x)$，$f(g\text{Stab}(x)) = g \cdot x$。

良定义：若 $g\text{Stab}(x) = h\text{Stab}(x)$，则 $h^{-1}g \in \text{Stab}(x)$，故 $h^{-1}g \cdot x = x$，$g \cdot x = h \cdot x$。

满射：对 $y \in \text{Orb}(x)$，$y = g \cdot x$ 对某 $g$，$f(g\text{Stab}(x)) = y$。

单射：若 $g \cdot x = h \cdot x$，则 $h^{-1}g \cdot x = x$，$h^{-1}g \in \text{Stab}(x)$，$g\text{Stab}(x) = h\text{Stab}(x)$。

因此 $|\text{Orb}(x)| = [G : \text{Stab}(x)] = |G| / |\text{Stab}(x)|$。$\blacksquare$

**(c)** $G = S_3$ 作用于 $X = \{1, 2, 3\}$。

$\text{Orb}(1) = \{g(1) : g \in S_3\} = \{1, 2, 3\} = X$（通过 $e(1)=1$，$r(1)=2$，$r^2(1)=3$）。

$\text{Stab}(1) = \{g \in S_3 : g(1) = 1\} = \{e, s_1\}$。

$|\text{Orb}(1)| \cdot |\text{Stab}(1)| = 3 \times 2 = 6 = |S_3|$。✓

---

## 挑战题 3：群同态基本定理的特例

设 $\phi : \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ 定义为 $\phi(k) = [k]$（自然映射）。

**(a)** 证明 $\phi$ 是群同态（$\phi(a + b) = \phi(a) + \phi(b)$）。

**(b)** 求 $\ker(\phi) = \{k \in \mathbb{Z} : \phi(k) = [0]\}$，证明它是 $\mathbb{Z}$ 的子群。

**(c)** 证明 $\ker(\phi) = n\mathbb{Z}$，并解释商群 $\mathbb{Z} / n\mathbb{Z}$ 的含义（为什么我们使用同样的记号）。

### 解答

**(a)** $\phi(a + b) = [a + b] = [a] + [b] = \phi(a) + \phi(b)$。$\blacksquare$

**(b)** $\ker(\phi) = \{k \in \mathbb{Z} : [k] = [0]\} = \{k : n \mid k\} = n\mathbb{Z}$。

$n\mathbb{Z}$ 是 $\mathbb{Z}$ 的子群（练习题 §1 例题 1 的推广）。$\blacksquare$

**(c)** $\ker(\phi) = n\mathbb{Z} = \{0, \pm n, \pm 2n, \ldots\}$。

$\mathbb{Z}$ 关于子群 $n\mathbb{Z}$ 的左陪集为 $k + n\mathbb{Z} = \{k + nm : m \in \mathbb{Z}\}$，这恰好是 $k$ 模 $n$ 的等价类 $[k]$。

共有 $n$ 个陪集：$n\mathbb{Z}, 1 + n\mathbb{Z}, \ldots, (n-1) + n\mathbb{Z}$。

商群 $\mathbb{Z}/n\mathbb{Z}$（群论定义 = 陪集集合 + 陪集运算）与之前定义的 $\mathbb{Z}/n\mathbb{Z}$（数论定义 = 模 $n$ 剩余类 + 模 $n$ 加法）完全一致。记号 $\mathbb{Z}/n\mathbb{Z}$ 既是数论记号，也是群论中的商群记号——两种含义完美吻合。$\blacksquare$
