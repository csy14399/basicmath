# 第 4 章 反三角函数 — 练习题解答

## §1 反三角函数

**1.** 基本反三角函数值。

(a) $\arcsin\frac{\sqrt{3}}{2} = \frac{\pi}{3}$（因为 $\sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$ 且 $\frac{\pi}{3} \in [-\frac{\pi}{2}, \frac{\pi}{2}]$）

(b) $\arccos\frac{1}{2} = \frac{\pi}{3}$（因为 $\cos\frac{\pi}{3} = \frac{1}{2}$ 且 $\frac{\pi}{3} \in [0, \pi]$）

(c) $\arctan(-1) = -\frac{\pi}{4}$（因为 $\tan(-\frac{\pi}{4}) = -1$ 且 $-\frac{\pi}{4} \in (-\frac{\pi}{2}, \frac{\pi}{2})$）

(d) $\arcsin(-\frac{\sqrt{2}}{2}) = -\frac{\pi}{4}$

---

**2.** 更多基本值。

(a) $\arccos 0 = \frac{\pi}{2}$

(b) $\arctan\sqrt{3} = \frac{\pi}{3}$

(c) $\arcsin 1 = \frac{\pi}{2}$

(d) $\arccos(-1) = \pi$

---

**3.** 正向复合。

(a) $\sin(\arcsin\frac{3}{5}) = \frac{3}{5}$（正向复合直接等于原值）

(b) $\cos(\arccos(-\frac{1}{3})) = -\frac{1}{3}$

(c) $\tan(\arctan 100) = 100$

---

**4.** 反向复合。

(a) $\frac{\pi}{5} \in [-\frac{\pi}{2}, \frac{\pi}{2}]$，所以 $\arcsin(\sin\frac{\pi}{5}) = \frac{\pi}{5}$。

(b) $\frac{4\pi}{5} \notin [-\frac{\pi}{2}, \frac{\pi}{2}]$。$\sin\frac{4\pi}{5} = \sin(\pi - \frac{4\pi}{5}) = \sin\frac{\pi}{5}$。$\arcsin(\sin\frac{\pi}{5}) = \frac{\pi}{5}$。

(c) $\frac{5\pi}{3} \notin [0, \pi]$。$\cos\frac{5\pi}{3} = \cos(2\pi - \frac{5\pi}{3}) = \cos\frac{\pi}{3} = \frac{1}{2}$。$\arccos\frac{1}{2} = \frac{\pi}{3}$。

(d) $\frac{5\pi}{6} \notin (-\frac{\pi}{2}, \frac{\pi}{2})$。$\tan\frac{5\pi}{6} = -\tan\frac{\pi}{6} = -\frac{1}{\sqrt{3}}$。$\arctan(-\frac{1}{\sqrt{3}}) = -\frac{\pi}{6}$。

---

**5.** 交叉复合化简。

(a) 设 $\theta = \arccos x$，$\cos\theta = x$，$\theta \in [0, \pi]$，$\sin\theta \geq 0$。$\sin(\arccos x) = \sqrt{1 - x^2}$。

(b) 设 $\theta = \arcsin x$，$\sin\theta = x$，$\theta \in [-\pi/2, \pi/2]$，$\cos\theta \geq 0$。$\cos(\arcsin x) = \sqrt{1 - x^2}$。

(c) $\tan(\arcsin x) = \frac{\sin\theta}{\cos\theta} = \frac{x}{\sqrt{1-x^2}}$。

(d) $\sec(\arctan x) = \frac{1}{\cos(\arctan x)} = \frac{1}{1/\sqrt{1+x^2}} = \sqrt{1+x^2}$。

---

**6.** 精确值计算。

(a) $\cos(\arcsin\frac{5}{13}) = \sqrt{1 - \frac{25}{169}} = \sqrt{\frac{144}{169}} = \frac{12}{13}$。

(b) 设 $\theta = \arccos\frac{3}{5}$，$\cos\theta = \frac{3}{5}$，$\sin\theta = \frac{4}{5}$。$\tan\theta = \frac{4}{3}$。

(c) 设 $\theta = \arctan\frac{12}{5}$。直角三角形：对边 $12$，邻边 $5$，斜边 $13$。$\sin\theta = \frac{12}{13}$。

---

**7.** 设 $\theta = \arctan\frac{1}{3}$，$\tan\theta = \frac{1}{3}$。

$$\cos(2\theta) = \frac{1-\tan^2\theta}{1+\tan^2\theta} = \frac{1 - 1/9}{1 + 1/9} = \frac{8/9}{10/9} = \frac{4}{5}$$

---

**8.** 设 $\alpha = \arcsin\frac{3}{5}$，$\beta = \arccos\frac{5}{13}$。

$\sin\alpha = \frac{3}{5}$，$\cos\alpha = \frac{4}{5}$。$\cos\beta = \frac{5}{13}$，$\sin\beta = \frac{12}{13}$。

$$\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta = \frac{3}{5}\cdot\frac{5}{13} + \frac{4}{5}\cdot\frac{12}{13} = \frac{15}{65} + \frac{48}{65} = \frac{63}{65}$$

---

**9.** 设 $\alpha = \arcsin x$。则 $\sin\alpha = x$，$\alpha \in [-\pi/2, \pi/2]$。

$\cos(\frac{\pi}{2} - \alpha) = \sin\alpha = x$ 且 $\frac{\pi}{2} - \alpha \in [0, \pi]$。

所以 $\arccos x = \frac{\pi}{2} - \alpha = \frac{\pi}{2} - \arcsin x$，即 $\arcsin x + \arccos x = \frac{\pi}{2}$。$\blacksquare$

---

**10.** $\arccos(-x) = \frac{\pi}{2} - \arcsin(-x) = \frac{\pi}{2} + \arcsin x = \frac{\pi}{2} + (\frac{\pi}{2} - \arccos x) = \pi - \arccos x$。$\blacksquare$

---

**11.** 设 $\alpha = \arctan\frac{1}{2}$，$\beta = \arctan\frac{1}{3}$。$\frac{1}{2}\cdot\frac{1}{3} = \frac{1}{6} < 1$，可直接用加法公式：

$$\arctan\frac{1}{2} + \arctan\frac{1}{3} = \arctan\frac{\frac{1}{2}+\frac{1}{3}}{1-\frac{1}{2}\cdot\frac{1}{3}} = \arctan\frac{\frac{5}{6}}{\frac{5}{6}} = \arctan 1 = \frac{\pi}{4}$$

$\blacksquare$

---

**12.** 设 $x > 0$，$\alpha = \arctan x$，$\beta = \arctan\frac{1}{x}$。则 $\alpha \in (0, \frac{\pi}{2})$，$\beta \in (0, \frac{\pi}{2})$。

$\tan\alpha = x$，$\tan\beta = \frac{1}{x}$。$\tan\alpha \cdot \tan\beta = 1$。

$$\tan(\alpha + \beta) = \frac{x + 1/x}{1 - x\cdot(1/x)} = \frac{x+1/x}{0}$$

分母为零，分子 $x + 1/x > 0$，所以 $\tan(\alpha+\beta)$ 趋向 $+\infty$，即 $\alpha + \beta = \frac{\pi}{2}$。

（更严格地：$\alpha + \beta \in (0, \pi)$ 且 $\tan(\alpha+\beta)$ 无定义，所以 $\alpha + \beta = \frac{\pi}{2}$。）$\blacksquare$

---

**13.** 在 $[0, 2\pi)$ 中的解。

(a) $\sin x = \frac{\sqrt{3}}{2}$：$x = \frac{\pi}{3}$ 或 $x = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$。

(b) $\cos x = -\frac{\sqrt{2}}{2}$：$\arccos(-\frac{\sqrt{2}}{2}) = \frac{3\pi}{4}$。$x = \frac{3\pi}{4}$ 或 $x = 2\pi - \frac{3\pi}{4} = \frac{5\pi}{4}$。

(c) $\tan x = -\sqrt{3}$：$\arctan(-\sqrt{3}) = -\frac{\pi}{3}$。$x = -\frac{\pi}{3} + \pi = \frac{2\pi}{3}$ 或 $x = -\frac{\pi}{3} + 2\pi = \frac{5\pi}{3}$。

---

**14.** 通解。

(a) $\sin 2x = \frac{1}{2}$：$2x = n\pi + (-1)^n\frac{\pi}{6}$，$x = \frac{n\pi}{2} + (-1)^n\frac{\pi}{12}$，$n \in \mathbb{Z}$。

(b) $\cos(x + \frac{\pi}{3}) = \frac{1}{2}$：$x + \frac{\pi}{3} = 2n\pi \pm \frac{\pi}{3}$。

取 $+$：$x = 2n\pi$。取 $-$：$x = 2n\pi - \frac{2\pi}{3}$。$n \in \mathbb{Z}$。

(c) $\tan 3x = 1$：$3x = n\pi + \frac{\pi}{4}$，$x = \frac{n\pi}{3} + \frac{\pi}{12}$，$n \in \mathbb{Z}$。

---

**15.** $2\sin^2 x - \sin x - 1 = 0$。

$(2\sin x + 1)(\sin x - 1) = 0$。

$\sin x = -\frac{1}{2}$：$x = \frac{7\pi}{6}$ 或 $x = \frac{11\pi}{6}$。

$\sin x = 1$：$x = \frac{\pi}{2}$。

解集：$\left\{\frac{\pi}{2}, \frac{7\pi}{6}, \frac{11\pi}{6}\right\}$。

---

**16.** $\cos 2x + \sin x = 0$。用 $\cos 2x = 1 - 2\sin^2 x$：

$$1 - 2\sin^2 x + \sin x = 0 \implies 2\sin^2 x - \sin x - 1 = 0$$

$(2\sin x + 1)(\sin x - 1) = 0$。与第 15 题相同。

解集：$\left\{\frac{\pi}{2}, \frac{7\pi}{6}, \frac{11\pi}{6}\right\}$。

---

**17.** $\sin x - \sqrt{3}\cos x = 1$。

辅助角公式：$\sin x - \sqrt{3}\cos x = 2\sin(x - \frac{\pi}{3})$。

$$2\sin\left(x - \frac{\pi}{3}\right) = 1 \implies \sin\left(x - \frac{\pi}{3}\right) = \frac{1}{2}$$

$$x - \frac{\pi}{3} = n\pi + (-1)^n\frac{\pi}{6}$$

$n = 0$：$x = \frac{\pi}{3} + \frac{\pi}{6} = \frac{\pi}{2}$。

$n = 1$：$x = \frac{\pi}{3} + \pi - \frac{\pi}{6} = \frac{\pi}{3} + \frac{5\pi}{6} = \frac{7\pi}{6}$。

在 $[0, 2\pi)$ 中的解集：$\left\{\frac{\pi}{2}, \frac{7\pi}{6}\right\}$。

验证：$\sin\frac{\pi}{2} - \sqrt{3}\cos\frac{\pi}{2} = 1 - 0 = 1$ ✓；$\sin\frac{7\pi}{6} - \sqrt{3}\cos\frac{7\pi}{6} = -\frac{1}{2} - \sqrt{3}(-\frac{\sqrt{3}}{2}) = -\frac{1}{2} + \frac{3}{2} = 1$ ✓。

---

**18.** $\sin A = \frac{7}{25}$，$\angle C = 90°$。

$\cos A = \sqrt{1 - \frac{49}{625}} = \sqrt{\frac{576}{625}} = \frac{24}{25}$。

$\tan A = \frac{7}{24}$。

$\cos B = \sin A = \frac{7}{25}$（互余关系）。

$A = \arcsin\frac{7}{25} = \arctan\frac{7}{24}$，$B = \frac{\pi}{2} - A = \arccos\frac{7}{25} = \arctan\frac{24}{7}$。

---

**19.** $\arctan 1 + \arctan 2 + \arctan 3$。

先算 $\arctan 2 + \arctan 3$：$2 \times 3 = 6 > 1$ 且 $2, 3 > 0$，

$$\arctan 2 + \arctan 3 = \pi + \arctan\frac{2+3}{1-6} = \pi + \arctan(-1) = \pi - \frac{\pi}{4} = \frac{3\pi}{4}$$

$$\arctan 1 + \frac{3\pi}{4} = \frac{\pi}{4} + \frac{3\pi}{4} = \pi$$
