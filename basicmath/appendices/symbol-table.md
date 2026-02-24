# 附录 B：符号索引（Symbol Table）

本附录按类别列出本书中使用的全部数学符号。每个符号给出 LaTeX 代码、中英文名称、含义和首次定义位置。

---

## B.1 集合论符号（Set Theory Symbols）

| 符号 | LaTeX | 名称 | 含义 | 首次定义 |
|------|-------|------|------|----------|
| $\in$ | `\in` | 属于（element of） | $x \in A$：$x$ 是 $A$ 的元素 | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $\notin$ | `\notin` | 不属于（not element of） | $x \notin A$：$x$ 不是 $A$ 的元素 | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $\subseteq$ | `\subseteq` | 子集（subset） | $A \subseteq B$：$A$ 中每个元素都属于 $B$ | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $\subsetneq$ | `\subsetneq` | 真子集（proper subset） | $A \subsetneq B$：$A \subseteq B$ 且 $A \neq B$ | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $\supseteq$ | `\supseteq` | 超集（superset） | $B \supseteq A$：$B$ 包含 $A$ 的所有元素 | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $\cup$ | `\cup` | 并集（union） | $A \cup B = \{x : x \in A \text{ 或 } x \in B\}$ | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $\cap$ | `\cap` | 交集（intersection） | $A \cap B = \{x : x \in A \text{ 且 } x \in B\}$ | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $\setminus$ | `\setminus` | 差集（set difference） | $A \setminus B = \{x : x \in A,\, x \notin B\}$ | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $A^c$ | `A^c` | 补集（complement） | $A^c = U \setminus A$（相对于全集 $U$） | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $\emptyset$ | `\emptyset` | 空集（empty set） | 无元素的集合 | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $\mathcal{P}(A)$ | `\mathcal{P}(A)` | 幂集（power set） | $A$ 的所有子集的集合 | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $A \times B$ | `A \times B` | 笛卡尔积（Cartesian product） | 有序对 $(a,b)$ 的集合 | [Part 1 Ch02 §2](../part-01-foundations/ch02-sets/02-relations.md) |
| $A \triangle B$ | `A \triangle B` | 对称差（symmetric difference） | $(A \setminus B) \cup (B \setminus A)$ | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $\bigcup_{i \in I}$ | `\bigcup` | 广义并集（generalized union） | 索引族的并 | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $\bigcap_{i \in I}$ | `\bigcap` | 广义交集（generalized intersection） | 索引族的交 | [Part 1 Ch02 §1](../part-01-foundations/ch02-sets/01-sets-operations.md) |
| $|A|$ | `|A|` | 基数（cardinality） | 集合的"大小" | [Part 1 Ch02 §4](../part-01-foundations/ch02-sets/04-cardinality.md) |
| $\aleph_0$ | `\aleph_0` | 阿列夫零（aleph-null） | 可数无穷集的基数 | [Part 1 Ch02 §4](../part-01-foundations/ch02-sets/04-cardinality.md) |

---

## B.2 逻辑符号（Logic Symbols）

| 符号 | LaTeX | 名称 | 含义 | 首次定义 |
|------|-------|------|------|----------|
| $\neg$ | `\neg` | 否定（negation） | 逻辑非 | [Part 1 Ch01 §1](../part-01-foundations/ch01-logic/01-propositions.md) |
| $\wedge$ | `\wedge` | 合取（conjunction） | 逻辑与 | [Part 1 Ch01 §1](../part-01-foundations/ch01-logic/01-propositions.md) |
| $\vee$ | `\vee` | 析取（disjunction） | 逻辑或（包含或） | [Part 1 Ch01 §1](../part-01-foundations/ch01-logic/01-propositions.md) |
| $\to$ | `\to` | 蕴含（implication） | 若…则… | [Part 1 Ch01 §1](../part-01-foundations/ch01-logic/01-propositions.md) |
| $\leftrightarrow$ | `\leftrightarrow` | 双条件（biconditional） | 当且仅当 | [Part 1 Ch01 §1](../part-01-foundations/ch01-logic/01-propositions.md) |
| $\forall$ | `\forall` | 全称量词（universal quantifier） | 对所有 | [Part 1 Ch01 §2](../part-01-foundations/ch01-logic/02-predicates.md) |
| $\exists$ | `\exists` | 存在量词（existential quantifier） | 存在 | [Part 1 Ch01 §2](../part-01-foundations/ch01-logic/02-predicates.md) |
| $\exists!$ | `\exists!` | 唯一存在（unique existential） | 存在唯一 | [Part 1 Ch01 §2](../part-01-foundations/ch01-logic/02-predicates.md) |
| $\Rightarrow$ | `\Rightarrow` | 推出（implies） | 推理中"因此" | [Part 1 Ch01 §1](../part-01-foundations/ch01-logic/01-propositions.md) |
| $\Leftrightarrow$ | `\Leftrightarrow` | 等价（equivalent） | 推理中"当且仅当" | [Part 1 Ch01 §1](../part-01-foundations/ch01-logic/01-propositions.md) |
| $\equiv$ | `\equiv` | 逻辑等价（logically equivalent） | 两命题的真值表相同 | [Part 1 Ch01 §1](../part-01-foundations/ch01-logic/01-propositions.md) |
| $\square$ | `\square` | 证毕（QED） | 证明结束标记 | [Part 1 Ch03 §1](../part-01-foundations/ch03-proof-methods/01-direct-proof.md) |

---

## B.3 数集符号（Number Set Symbols）

| 符号 | LaTeX | 名称 | 含义 | 首次定义 |
|------|-------|------|------|----------|
| $\mathbb{N}$ | `\mathbb{N}` | 自然数集（natural numbers） | $\{0, 1, 2, 3, \ldots\}$ | [Part 2 Ch01 §1](../part-02-numbers/ch01-number-systems/01-natural-integers.md) |
| $\mathbb{Z}$ | `\mathbb{Z}` | 整数集（integers） | $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$ | [Part 2 Ch01 §1](../part-02-numbers/ch01-number-systems/01-natural-integers.md) |
| $\mathbb{Z}^+$ | `\mathbb{Z}^+` | 正整数集（positive integers） | $\{1, 2, 3, \ldots\}$ | [Part 2 Ch01 §1](../part-02-numbers/ch01-number-systems/01-natural-integers.md) |
| $\mathbb{Q}$ | `\mathbb{Q}` | 有理数集（rational numbers） | 可以表示为整数之比的数 | [Part 2 Ch01 §2](../part-02-numbers/ch01-number-systems/02-rationals.md) |
| $\mathbb{R}$ | `\mathbb{R}` | 实数集（real numbers） | 满足完备性公理的有序域 | [Part 2 Ch01 §3](../part-02-numbers/ch01-number-systems/03-reals.md) |
| $\mathbb{R}^+$ | `\mathbb{R}^+` | 正实数集（positive reals） | $\{x \in \mathbb{R} : x > 0\}$ | [Part 2 Ch01 §3](../part-02-numbers/ch01-number-systems/03-reals.md) |
| $\mathbb{C}$ | `\mathbb{C}` | 复数集（complex numbers） | $\{a + bi : a, b \in \mathbb{R}\}$ | [Part 2 Ch01 §4](../part-02-numbers/ch01-number-systems/04-complex.md) |
| $\mathbb{R}^n$ | `\mathbb{R}^n` | $n$ 维实向量空间 | $n$ 元实数组的集合 | [Part 9 Ch01 §1](../part-09-linear-algebra/ch01-vector-spaces/01-vector-space-intuition.md) |

---

## B.4 代数符号（Algebra Symbols）

| 符号 | LaTeX | 名称 | 含义 | 首次定义 |
|------|-------|------|------|----------|
| $=$ | `=` | 等号（equals） | 两边表示同一数学对象 | [Part 2 Ch01 §1](../part-02-numbers/ch01-number-systems/01-natural-integers.md) |
| $\neq$ | `\neq` | 不等号（not equal） | 两边不相等 | [Part 2 Ch01 §1](../part-02-numbers/ch01-number-systems/01-natural-integers.md) |
| $<, >, \leq, \geq$ | `<, >, \leq, \geq` | 不等号（inequalities） | 严格/非严格大小比较 | [Part 2 Ch01 §1](../part-02-numbers/ch01-number-systems/01-natural-integers.md) |
| $\approx$ | `\approx` | 约等于（approximately equal） | 近似相等 | [Part 2 Ch01 §3](../part-02-numbers/ch01-number-systems/03-reals.md) |
| $:=$ | `:=` | 定义为（defined as） | 左端被定义为右端 | [Part 1 Ch01 §1](../part-01-foundations/ch01-logic/01-propositions.md) |
| $+, -, \times, \div$ | `+, -, \times, \div` | 四则运算 | 加、减、乘、除 | [Part 2 Ch01 §1](../part-02-numbers/ch01-number-systems/01-natural-integers.md) |
| $\cdot$ | `\cdot` | 乘法/点积（multiplication/dot） | 视上下文为标量乘法或内积 | [Part 2 Ch01 §1](../part-02-numbers/ch01-number-systems/01-natural-integers.md) |
| $a^n$ | `a^n` | 幂（power） | $a$ 的 $n$ 次方 | [Part 2 Ch01 §1](../part-02-numbers/ch01-number-systems/01-natural-integers.md) |
| $\sqrt{a}$, $\sqrt[n]{a}$ | `\sqrt{a}`, `\sqrt[n]{a}` | 根号（radical） | 平方根 / $n$ 次根 | [Part 2 Ch01 §2](../part-02-numbers/ch01-number-systems/02-rationals.md) |
| $|x|$ | `|x|` | 绝对值（absolute value） | $x$ 到原点的距离 | [Part 2 Ch01 §3](../part-02-numbers/ch01-number-systems/03-reals.md) |
| $n!$ | `n!` | 阶乘（factorial） | $n! = 1 \times 2 \times \cdots \times n$ | [Part 7 Ch02 §1](../part-07-combinatorics/ch02-permutations-combinations/01-permutations.md) |
| $\binom{n}{k}$ | `\binom{n}{k}` | 组合数（binomial coefficient） | $\frac{n!}{k!(n-k)!}$ | [Part 7 Ch02 §2](../part-07-combinatorics/ch02-permutations-combinations/02-combinations.md) |
| $P(n,r)$ 或 $A_n^r$ | `P(n,r)` | 排列数（permutation） | $\frac{n!}{(n-r)!}$ | [Part 7 Ch02 §1](../part-07-combinatorics/ch02-permutations-combinations/01-permutations.md) |
| $\sum$ | `\sum` | 求和（summation） | 有限或无穷求和 | [Part 2 Ch01 §1](../part-02-numbers/ch01-number-systems/01-natural-integers.md) |
| $\prod$ | `\prod` | 求积（product） | 有限或无穷乘积 | [Part 2 Ch01 §1](../part-02-numbers/ch01-number-systems/01-natural-integers.md) |
| $\gcd(a,b)$ | `\gcd(a,b)` | 最大公因数（greatest common divisor） | $a$ 与 $b$ 的最大公因数 | [Part 2 Ch03 §1](../part-02-numbers/ch03-number-theory/01-divisibility.md) |
| $\text{lcm}(a,b)$ | `\text{lcm}(a,b)` | 最小公倍数（least common multiple） | $a$ 与 $b$ 的最小公倍数 | [Part 2 Ch03 §1](../part-02-numbers/ch03-number-theory/01-divisibility.md) |
| $a \mid b$ | `a \mid b` | 整除（divides） | $a$ 整除 $b$：$\exists k \in \mathbb{Z},\, b = ka$ | [Part 2 Ch03 §1](../part-02-numbers/ch03-number-theory/01-divisibility.md) |
| $a \nmid b$ | `a \nmid b` | 不整除（does not divide） | $a$ 不整除 $b$ | [Part 2 Ch03 §1](../part-02-numbers/ch03-number-theory/01-divisibility.md) |
| $a \equiv b \pmod{m}$ | `a \equiv b \pmod{m}` | 同余（congruence） | $m \mid (a - b)$ | [Part 2 Ch03 §3](../part-02-numbers/ch03-number-theory/03-congruence.md) |
| $\phi(n)$ | `\phi(n)` | 欧拉函数（Euler's totient） | 小于 $n$ 且与 $n$ 互素的正整数个数 | [Part 2 Ch03 §4](../part-02-numbers/ch03-number-theory/04-euler-fermat.md) |

---

## B.5 函数符号（Function Symbols）

| 符号 | LaTeX | 名称 | 含义 | 首次定义 |
|------|-------|------|------|----------|
| $f: A \to B$ | `f: A \to B` | 函数（function） | 从 $A$ 到 $B$ 的映射 | [Part 1 Ch02 §3](../part-01-foundations/ch02-sets/03-functions-as-sets.md) |
| $f(x)$ | `f(x)` | 函数值（function value） | $f$ 在 $x$ 处的输出 | [Part 1 Ch02 §3](../part-01-foundations/ch02-sets/03-functions-as-sets.md) |
| $f \circ g$ | `f \circ g` | 复合（composition） | $(f \circ g)(x) = f(g(x))$ | [Part 1 Ch02 §3](../part-01-foundations/ch02-sets/03-functions-as-sets.md) |
| $f^{-1}$ | `f^{-1}` | 反函数（inverse） | $f^{-1}(y) = x \Leftrightarrow f(x) = y$ | [Part 1 Ch02 §3](../part-01-foundations/ch02-sets/03-functions-as-sets.md) |
| $\text{id}_A$ | `\text{id}_A` | 恒等函数（identity） | $\text{id}_A(x) = x$ | [Part 1 Ch02 §3](../part-01-foundations/ch02-sets/03-functions-as-sets.md) |
| $e^x$ 或 $\exp(x)$ | `e^x`, `\exp(x)` | 指数函数（exponential） | 以 $e$ 为底的指数函数 | [Part 4 Ch02 §1](../part-04-functions/ch02-exponential-log/01-exponential.md) |
| $\ln x$ | `\ln x` | 自然对数（natural logarithm） | 以 $e$ 为底的对数 | [Part 4 Ch02 §2](../part-04-functions/ch02-exponential-log/02-logarithm.md) |
| $\log_a x$ | `\log_a x` | 对数（logarithm） | 以 $a$ 为底的对数 | [Part 4 Ch02 §2](../part-04-functions/ch02-exponential-log/02-logarithm.md) |
| $\sin, \cos, \tan$ | `\sin, \cos, \tan` | 正弦/余弦/正切 | 基本三角函数 | [Part 4 Ch03 §1](../part-04-functions/ch03-trigonometric/01-unit-circle.md) |
| $\csc, \sec, \cot$ | `\csc, \sec, \cot` | 余割/正割/余切 | 倒数三角函数 | [Part 4 Ch03 §1](../part-04-functions/ch03-trigonometric/01-unit-circle.md) |
| $\arcsin, \arccos, \arctan$ | `\arcsin, \arccos, \arctan` | 反三角函数（inverse trig） | 三角函数的反函数（限制定义域后） | [Part 4 Ch04 §1](../part-04-functions/ch04-inverse-trig/01-inverse-trig.md) |
| $\lfloor x \rfloor$ | `\lfloor x \rfloor` | 下取整（floor） | 不超过 $x$ 的最大整数 | [Part 2 Ch01 §3](../part-02-numbers/ch01-number-systems/03-reals.md) |
| $\lceil x \rceil$ | `\lceil x \rceil` | 上取整（ceiling） | 不小于 $x$ 的最小整数 | [Part 2 Ch01 §3](../part-02-numbers/ch01-number-systems/03-reals.md) |

---

## B.6 几何符号（Geometry Symbols）

| 符号 | LaTeX | 名称 | 含义 | 首次定义 |
|------|-------|------|------|----------|
| $\vec{AB}$ | `\vec{AB}` | 有向线段（directed segment） | 从 $A$ 到 $B$ 的向量 | [Part 5 Ch05 §1](../part-05-geometry/ch05-vectors/01-vector-operations.md) |
| $\overline{AB}$ | `\overline{AB}` | 线段（segment） | 连接 $A$ 与 $B$ 的线段 | [Part 5 Ch01 §1](../part-05-geometry/ch01-euclidean/01-axioms-triangles.md) |
| $\angle ABC$ | `\angle ABC` | 角（angle） | 以 $B$ 为顶点的角 | [Part 5 Ch01 §1](../part-05-geometry/ch01-euclidean/01-axioms-triangles.md) |
| $\triangle ABC$ | `\triangle ABC` | 三角形（triangle） | 顶点为 $A, B, C$ 的三角形 | [Part 5 Ch01 §1](../part-05-geometry/ch01-euclidean/01-axioms-triangles.md) |
| $\parallel$ | `\parallel` | 平行（parallel） | 两直线不相交 | [Part 5 Ch01 §1](../part-05-geometry/ch01-euclidean/01-axioms-triangles.md) |
| $\perp$ | `\perp` | 垂直（perpendicular） | 两直线成 $90°$ 角 | [Part 5 Ch01 §1](../part-05-geometry/ch01-euclidean/01-axioms-triangles.md) |
| $\cong$ | `\cong` | 全等（congruent） | 形状和大小完全相同 | [Part 5 Ch01 §1](../part-05-geometry/ch01-euclidean/01-axioms-triangles.md) |
| $\sim$ | `\sim` | 相似（similar） | 形状相同、大小可能不同 | [Part 5 Ch01 §2](../part-05-geometry/ch01-euclidean/02-similarity-circles.md) |
| $(x, y)$ | `(x, y)` | 坐标（coordinates） | 平面上点的位置 | [Part 5 Ch02 §1](../part-05-geometry/ch02-analytic/01-coordinate-lines.md) |
| $(r, \theta)$ | `(r, \theta)` | 极坐标（polar coordinates） | 距离和角度表示的位置 | [Part 4 Ch05 §2](../part-04-functions/ch05-parametric-polar/02-polar.md) |
| $d(A, B)$ | `d(A, B)` | 距离（distance） | 两点之间的距离 | [Part 5 Ch02 §1](../part-05-geometry/ch02-analytic/01-coordinate-lines.md) |

---

## B.7 分析符号（Analysis Symbols）

| 符号 | LaTeX | 名称 | 含义 | 首次定义 |
|------|-------|------|------|----------|
| $\lim_{x \to a} f(x)$ | `\lim_{x \to a}` | 极限（limit） | $x$ 趋于 $a$ 时的极限 | [Part 6 Ch02 §1](../part-06-analysis-prep/ch02-limits/01-function-limits.md) |
| $\lim_{n \to \infty} a_n$ | `\lim_{n \to \infty}` | 数列极限（sequence limit） | 数列的极限 | [Part 6 Ch01 §2](../part-06-analysis-prep/ch01-sequences/02-sequence-limits.md) |
| $x \to a^+$ | `x \to a^+` | 右极限（right limit） | $x$ 从右侧趋于 $a$ | [Part 6 Ch02 §1](../part-06-analysis-prep/ch02-limits/01-function-limits.md) |
| $x \to a^-$ | `x \to a^-` | 左极限（left limit） | $x$ 从左侧趋于 $a$ | [Part 6 Ch02 §1](../part-06-analysis-prep/ch02-limits/01-function-limits.md) |
| $\epsilon$ | `\epsilon` | epsilon | 任意小正数 | [Part 6 Ch01 §2](../part-06-analysis-prep/ch01-sequences/02-sequence-limits.md) |
| $\delta$ | `\delta` | delta | 对应 $\epsilon$ 的正数 | [Part 6 Ch02 §1](../part-06-analysis-prep/ch02-limits/01-function-limits.md) |
| $\{a_n\}$ | `\{a_n\}` | 数列（sequence） | 以自然数为下标的有序数列 | [Part 6 Ch01 §1](../part-06-analysis-prep/ch01-sequences/01-sequence-concepts.md) |
| $\sum_{n=1}^{\infty} a_n$ | `\sum_{n=1}^{\infty}` | 无穷级数（infinite series） | 无穷多项的和 | [Part 6 Ch04 §1](../part-06-analysis-prep/ch04-series/01-series-convergence.md) |
| $S_n$ | `S_n` | 部分和（partial sum） | $S_n = \sum_{k=1}^{n} a_k$ | [Part 6 Ch04 §1](../part-06-analysis-prep/ch04-series/01-series-convergence.md) |
| $f'(x)$ | `f'(x)` | 导数（derivative） | 函数在 $x$ 处的变化率 | [Part 6 Ch05 §1](../part-06-analysis-prep/ch05-calculus-intuition/01-derivative-intuition.md) |
| $\frac{df}{dx}$ | `\frac{df}{dx}` | 导数（Leibniz 记号） | 同 $f'(x)$ | [Part 6 Ch05 §1](../part-06-analysis-prep/ch05-calculus-intuition/01-derivative-intuition.md) |
| $\int_a^b f(x)\,dx$ | `\int_a^b f(x)\,dx` | 定积分（definite integral） | 曲线下的"面积" | [Part 6 Ch05 §2](../part-06-analysis-prep/ch05-calculus-intuition/02-integral-intuition.md) |
| $\sup A$ | `\sup A` | 上确界（supremum） | $A$ 的最小上界 | [Part 2 Ch02 §1](../part-02-numbers/ch02-real-numbers/01-completeness.md) |
| $\inf A$ | `\inf A` | 下确界（infimum） | $A$ 的最大下界 | [Part 2 Ch02 §1](../part-02-numbers/ch02-real-numbers/01-completeness.md) |
| $\max$, $\min$ | `\max`, `\min` | 最大/最小值 | 集合中的最大/最小元素 | [Part 2 Ch01 §1](../part-02-numbers/ch01-number-systems/01-natural-integers.md) |
| $O(g(x))$ | `O(g(x))` | 大 O 记号（big-O） | 渐近上界 | [Part 6 Ch02 §2](../part-06-analysis-prep/ch02-limits/02-limit-techniques.md) |
| $o(g(x))$ | `o(g(x))` | 小 o 记号（little-o） | 渐近可忽略 | [Part 6 Ch02 §2](../part-06-analysis-prep/ch02-limits/02-limit-techniques.md) |

---

## B.8 概率符号（Probability Symbols）

| 符号 | LaTeX | 名称 | 含义 | 首次定义 |
|------|-------|------|------|----------|
| $\Omega$ | `\Omega` | 样本空间（sample space） | 所有可能结果的集合 | [Part 8 Ch01 §1](../part-08-probability/ch01-axioms/01-sample-events.md) |
| $P(A)$ | `P(A)` | 概率（probability） | 事件 $A$ 发生的概率 | [Part 8 Ch01 §1](../part-08-probability/ch01-axioms/01-sample-events.md) |
| $P(A \mid B)$ | `P(A \mid B)` | 条件概率（conditional probability） | 已知 $B$ 发生时 $A$ 的概率 | [Part 8 Ch02 §1](../part-08-probability/ch02-conditional/01-conditional-probability.md) |
| $X, Y, Z$ | `X, Y, Z` | 随机变量（random variable） | 从样本空间到实数的函数 | [Part 8 Ch03 §1](../part-08-probability/ch03-random-variables/01-discrete-rv.md) |
| $E[X]$ 或 $\mu$ | `E[X]` | 期望（expectation） | 随机变量的平均值 | [Part 8 Ch04 §1](../part-08-probability/ch04-expectation-variance/01-expectation.md) |
| $\text{Var}(X)$ 或 $\sigma^2$ | `\text{Var}(X)` | 方差（variance） | 随机变量的离散程度 | [Part 8 Ch04 §2](../part-08-probability/ch04-expectation-variance/02-variance.md) |
| $\sigma$ | `\sigma` | 标准差（standard deviation） | $\sigma = \sqrt{\text{Var}(X)}$ | [Part 8 Ch04 §2](../part-08-probability/ch04-expectation-variance/02-variance.md) |
| $\binom{n}{k} p^k (1-p)^{n-k}$ | — | 二项分布概率（binomial） | $B(n, p)$ 的概率质量函数 | [Part 8 Ch03 §2](../part-08-probability/ch03-random-variables/02-common-distributions.md) |
| $X \sim B(n,p)$ | `X \sim B(n,p)` | 服从分布（distributed as） | $X$ 服从参数为 $n, p$ 的二项分布 | [Part 8 Ch03 §2](../part-08-probability/ch03-random-variables/02-common-distributions.md) |
| $\bar{X}$ | `\bar{X}` | 样本均值（sample mean） | $\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i$ | [Part 8 Ch05 §1](../part-08-probability/ch05-law-of-large-numbers/01-lln-intuition.md) |

---

## B.9 线性代数符号（Linear Algebra Symbols）

| 符号 | LaTeX | 名称 | 含义 | 首次定义 |
|------|-------|------|------|----------|
| $\mathbf{v}, \mathbf{w}$ | `\mathbf{v}` | 向量（vector） | 向量空间中的元素 | [Part 9 Ch01 §1](../part-09-linear-algebra/ch01-vector-spaces/01-vector-space-intuition.md) |
| $\mathbf{0}$ | `\mathbf{0}` | 零向量（zero vector） | 加法单位元 | [Part 9 Ch01 §1](../part-09-linear-algebra/ch01-vector-spaces/01-vector-space-intuition.md) |
| $\mathbf{e}_i$ | `\mathbf{e}_i` | 标准基向量（standard basis） | 第 $i$ 个分量为 $1$ 的向量 | [Part 9 Ch01 §2](../part-09-linear-algebra/ch01-vector-spaces/02-linear-independence.md) |
| $\text{span}(\mathbf{v}_1, \ldots, \mathbf{v}_k)$ | `\text{span}` | 生成空间（span） | 向量组的所有线性组合 | [Part 9 Ch01 §2](../part-09-linear-algebra/ch01-vector-spaces/02-linear-independence.md) |
| $\dim V$ | `\dim V` | 维数（dimension） | 向量空间基的元素个数 | [Part 9 Ch01 §2](../part-09-linear-algebra/ch01-vector-spaces/02-linear-independence.md) |
| $A^T$ | `A^T` | 转置（transpose） | 行列互换 | [Part 9 Ch02 §2](../part-09-linear-algebra/ch02-matrices/02-special-matrices.md) |
| $A^{-1}$ | `A^{-1}` | 逆矩阵（inverse matrix） | $AA^{-1} = I$ | [Part 9 Ch02 §2](../part-09-linear-algebra/ch02-matrices/02-special-matrices.md) |
| $I_n$ | `I_n` | 单位矩阵（identity matrix） | 对角元素全 $1$，其余全 $0$ | [Part 9 Ch02 §2](../part-09-linear-algebra/ch02-matrices/02-special-matrices.md) |
| $\det(A)$ | `\det(A)` | 行列式（determinant） | 方阵到标量的函数 | [Part 9 Ch04 §1](../part-09-linear-algebra/ch04-determinants/01-determinants.md) |
| $\text{rank}(A)$ | `\text{rank}(A)` | 秩（rank） | 最大线性无关列数 | [Part 9 Ch03 §2](../part-09-linear-algebra/ch03-linear-systems/02-solution-structure.md) |
| $\text{null}(A)$ | `\text{null}(A)` | 零空间（null space） | $\{\mathbf{x} : A\mathbf{x} = \mathbf{0}\}$ | [Part 9 Ch03 §2](../part-09-linear-algebra/ch03-linear-systems/02-solution-structure.md) |
| $[A \mid \mathbf{b}]$ | `[A \mid \mathbf{b}]` | 增广矩阵（augmented matrix） | 系数矩阵附加常数列 | [Part 9 Ch03 §1](../part-09-linear-algebra/ch03-linear-systems/01-gaussian-elimination.md) |
| $\text{tr}(A)$ | `\text{tr}(A)` | 迹（trace） | 对角元素之和 | [Part 9 Ch02 §1](../part-09-linear-algebra/ch02-matrices/01-matrix-operations.md) |

---

## B.10 特殊常数（Special Constants）

| 符号 | LaTeX | 名称 | 近似值 | 首次定义 |
|------|-------|------|--------|----------|
| $\pi$ | `\pi` | 圆周率（pi） | $3.14159\ldots$ | [Part 4 Ch03 §1](../part-04-functions/ch03-trigonometric/01-unit-circle.md) |
| $e$ | `e` | 自然底数（Euler's number） | $2.71828\ldots$ | [Part 4 Ch02 §1](../part-04-functions/ch02-exponential-log/01-exponential.md) |
| $i$ | `i` | 虚数单位（imaginary unit） | $i^2 = -1$ | [Part 2 Ch01 §4](../part-02-numbers/ch01-number-systems/04-complex.md) |
| $\phi$ | `\phi` | 黄金比例（golden ratio） | $\frac{1+\sqrt{5}}{2} \approx 1.61803\ldots$ | [Part 6 Ch01 §1](../part-06-analysis-prep/ch01-sequences/01-sequence-concepts.md) |
| $\gamma$ | `\gamma` | Euler-Mascheroni 常数 | $0.57721\ldots$ | [Part 6 Ch04 §1](../part-06-analysis-prep/ch04-series/01-series-convergence.md) |
| $\infty$ | `\infty` | 无穷（infinity） | 非实数符号，表示"无界增长" | [Part 6 Ch01 §2](../part-06-analysis-prep/ch01-sequences/02-sequence-limits.md) |

---

## 使用说明

- 对某个符号不确定时，可在此表中快速查找。
- "首次定义"指向该符号被正式引入和定义的章节。该符号可能在更早的章节中以直觉的方式提及。
- 更多关于记号约定的讨论，参见[附录 A：记号约定说明](notation-guide.md)。
