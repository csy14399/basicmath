# 第 3 章 三角函数 — 练习题解答

## §1 三角函数的几何起源

**1.** 角度转弧度。

(a) $150° = 150 \cdot \frac{\pi}{180} = \frac{5\pi}{6}$

(b) $-45° = -45 \cdot \frac{\pi}{180} = -\frac{\pi}{4}$

(c) $720° = 720 \cdot \frac{\pi}{180} = 4\pi$

(d) $15° = 15 \cdot \frac{\pi}{180} = \frac{\pi}{12}$

---

**2.** 弧度转角度。

(a) $\frac{5\pi}{3} = \frac{5 \cdot 180}{3} = 300°$

(b) $\frac{7\pi}{4} = \frac{7 \cdot 180}{4} = 315°$

(c) $-\frac{\pi}{3} = -\frac{180}{3} = -60°$

(d) $\frac{11\pi}{6} = \frac{11 \cdot 180}{6} = 330°$

---

**3.** 三角函数值。

(a) $\sin\frac{3\pi}{4} = \sin(\pi - \frac{\pi}{4}) = \sin\frac{\pi}{4} = \frac{\sqrt{2}}{2}$

(b) $\cos\frac{5\pi}{3} = \cos(2\pi - \frac{\pi}{3}) = \cos\frac{\pi}{3} = \frac{1}{2}$

(c) $\tan\frac{5\pi}{6} = \tan(\pi - \frac{\pi}{6}) = -\tan\frac{\pi}{6} = -\frac{\sqrt{3}}{3}$

(d) $\sin(-\frac{\pi}{6}) = -\sin\frac{\pi}{6} = -\frac{1}{2}$

---

**4.** $\sin\theta = \frac{5}{13}$，第一象限。

$\cos\theta = \sqrt{1 - \frac{25}{169}} = \sqrt{\frac{144}{169}} = \frac{12}{13}$

$\tan\theta = \frac{5}{12}$，$\cot\theta = \frac{12}{5}$，$\sec\theta = \frac{13}{12}$，$\csc\theta = \frac{13}{5}$

---

**5.** $\tan\theta = -\frac{7}{24}$，第二象限。$\sin\theta > 0$，$\cos\theta < 0$。

$\sec^2\theta = 1 + \tan^2\theta = 1 + \frac{49}{576} = \frac{625}{576}$，$\cos^2\theta = \frac{576}{625}$，$\cos\theta = -\frac{24}{25}$。

$\sin\theta = \tan\theta \cdot \cos\theta = (-\frac{7}{24})(-\frac{24}{25}) = \frac{7}{25}$。

---

**6.** $\frac{\sin\theta \cdot \sec\theta}{\tan\theta} = \frac{\sin\theta \cdot \frac{1}{\cos\theta}}{\frac{\sin\theta}{\cos\theta}} = \frac{\frac{\sin\theta}{\cos\theta}}{\frac{\sin\theta}{\cos\theta}} = 1$

---

**7.** $(\sin\theta + \cos\theta)^2 = \sin^2\theta + 2\sin\theta\cos\theta + \cos^2\theta = 1 + 2\sin\theta\cos\theta = 1 + \sin 2\theta$。$\blacksquare$

---

**8.** $\theta = \frac{s}{r} = \frac{15}{10} = 1.5$ rad。$A = \frac{1}{2}r^2\theta = \frac{1}{2}(100)(1.5) = 75$ cm²。

---

**9.**

$$\frac{\tan\theta - \sin\theta}{\sin^3\theta} = \frac{\frac{\sin\theta}{\cos\theta} - \sin\theta}{\sin^3\theta} = \frac{\sin\theta\left(\frac{1}{\cos\theta} - 1\right)}{\sin^3\theta} = \frac{\frac{1-\cos\theta}{\cos\theta}}{\sin^2\theta} = \frac{1-\cos\theta}{\cos\theta \cdot \sin^2\theta}$$

$$= \frac{1-\cos\theta}{\cos\theta(1-\cos^2\theta)} = \frac{1-\cos\theta}{\cos\theta(1-\cos\theta)(1+\cos\theta)} = \frac{1}{\cos\theta(1+\cos\theta)} = \frac{\sec\theta}{1+\cos\theta}$$

$\blacksquare$

---

## §2 三角函数的性质与图像

**1.** (a) $T = \frac{2\pi}{3}$  (b) $T = \frac{2\pi}{1/2} = 4\pi$  (c) $T = \frac{\pi}{2}$

---

**2.** $A = 4$，$B = 2$，$C = -\frac{\pi}{3}$，$D = 1$。

振幅 $4$，周期 $\frac{2\pi}{2} = \pi$，相移 $-\frac{-\pi/3}{2} = \frac{\pi}{6}$（右移），中线 $y = 1$。

---

**3.** $\sin 1 \approx 0.841$，$\sin 2 \approx 0.909$，$\sin 3 \approx 0.141$。

$1$ rad $\approx 57.3°$，$2$ rad $\approx 114.6°$，$3$ rad $\approx 171.9°$。

$\sin$ 在 $[\pi/2, \pi]$ 上递减，$\pi/2 \approx 1.571$。$\sin 1 < \sin(\pi/2) = 1$。

$\sin 2 = \sin(\pi - 2) = \sin(1.14...) > \sin 1$（因为 $1 < 1.14 < \pi/2$）。

$\sin 3 = \sin(\pi - 3) = \sin(0.14...)$ 很小。

因此 $\sin 3 < \sin 1 < \sin 2$。

---

**4.** $f(x) = 2\sin x + 3\cos x = \sqrt{4+9}\sin(x+\varphi) = \sqrt{13}\sin(x+\varphi)$。

最大值 $\sqrt{13}$，最小值 $-\sqrt{13}$。

---

**5.** $y = \sin x$ 在 $[0,\pi]$ 上：最大值 $1$，在 $x = \frac{\pi}{2}$ 时取到。

$y = \sin(2x+\frac{\pi}{6})$ 在 $[0, \frac{\pi}{2}]$ 上：$2x + \frac{\pi}{6} \in [\frac{\pi}{6}, \pi + \frac{\pi}{6}]$。$\sin$ 在 $\frac{\pi}{2}$ 时取最大值 $1$。$2x + \frac{\pi}{6} = \frac{\pi}{2}$，$x = \frac{\pi}{6}$。最大值 $1$，在 $x = \frac{\pi}{6}$ 时取到。

---

**6.** $|\sin x|$ 将 $\sin x$ 的负半部翻到正半部。最小正周期为 $\pi$（原来的一半）。

---

**7.** $f(x) = \sin x + |\sin x|$。当 $\sin x \geq 0$（$x \in [2k\pi, (2k+1)\pi]$）时 $f(x) = 2\sin x$；当 $\sin x < 0$ 时 $f(x) = 0$。最小正周期 $2\pi$。

---

**8.** $A = \frac{7-1}{2} = 3$，$D = \frac{7+1}{2} = 4$。$\frac{2\pi}{B} = 6 \implies B = \frac{\pi}{3}$。

最大值在 $x = 1$ 时取到：$\cos(\frac{\pi}{3} \cdot 1 + C) = 1$，$\frac{\pi}{3} + C = 0$，$C = -\frac{\pi}{3}$。

$$y = 3\cos\left(\frac{\pi}{3}x - \frac{\pi}{3}\right) + 4$$

---

## §3 三角恒等式

**1.** (a) $\cos 15° = \cos(45°-30°) = \cos 45°\cos 30° + \sin 45°\sin 30° = \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2}\cdot\frac{1}{2} = \frac{\sqrt{6}+\sqrt{2}}{4}$

(b) $\sin\frac{7\pi}{12} = \sin(\frac{\pi}{3}+\frac{\pi}{4}) = \sin\frac{\pi}{3}\cos\frac{\pi}{4}+\cos\frac{\pi}{3}\sin\frac{\pi}{4} = \frac{\sqrt{3}}{2}\cdot\frac{\sqrt{2}}{2}+\frac{1}{2}\cdot\frac{\sqrt{2}}{2} = \frac{\sqrt{6}+\sqrt{2}}{4}$

(c) $\tan 75° = \tan(45°+30°) = \frac{1+\frac{\sqrt{3}}{3}}{1-\frac{\sqrt{3}}{3}} = \frac{3+\sqrt{3}}{3-\sqrt{3}} = \frac{(3+\sqrt{3})^2}{(3-\sqrt{3})(3+\sqrt{3})} = \frac{12+6\sqrt{3}}{6} = 2+\sqrt{3}$

---

**2.** $\sin\alpha = 4/5$，$\cos\alpha = 3/5$。$\cos\beta = -12/13$，$\sin\beta = 5/13$（第二象限）。

$\sin(\alpha+\beta) = \sin\alpha\cos\beta+\cos\alpha\sin\beta = \frac{4}{5}\cdot(-\frac{12}{13})+\frac{3}{5}\cdot\frac{5}{13} = \frac{-48+15}{65} = -\frac{33}{65}$

$\cos(\alpha-\beta) = \cos\alpha\cos\beta+\sin\alpha\sin\beta = \frac{3}{5}\cdot(-\frac{12}{13})+\frac{4}{5}\cdot\frac{5}{13} = \frac{-36+20}{65} = -\frac{16}{65}$

---

**3.** $\sin\frac{\pi}{8} = \sin\frac{\pi/4}{2} = \sqrt{\frac{1-\cos(\pi/4)}{2}} = \sqrt{\frac{1-\frac{\sqrt{2}}{2}}{2}} = \sqrt{\frac{2-\sqrt{2}}{4}} = \frac{\sqrt{2-\sqrt{2}}}{2}$

---

**4.** $\frac{1-\cos 2x}{\sin 2x} = \frac{2\sin^2 x}{2\sin x\cos x} = \frac{\sin x}{\cos x} = \tan x$

---

**5.** $\frac{\sin 3\alpha}{\sin\alpha} - \frac{\cos 3\alpha}{\cos\alpha} = \frac{\sin 3\alpha\cos\alpha - \cos 3\alpha\sin\alpha}{\sin\alpha\cos\alpha} = \frac{\sin(3\alpha-\alpha)}{\sin\alpha\cos\alpha} = \frac{\sin 2\alpha}{\frac{1}{2}\sin 2\alpha} = 2$。$\blacksquare$

---

**6.** $\cos 3x - \cos 7x = -2\sin\frac{3x+7x}{2}\sin\frac{3x-7x}{2} = -2\sin 5x \sin(-2x) = 2\sin 5x\sin 2x$

---

**7.** $\sin 75°\cos 15° = \frac{1}{2}[\sin(75°+15°)+\sin(75°-15°)] = \frac{1}{2}[\sin 90°+\sin 60°] = \frac{1}{2}[1+\frac{\sqrt{3}}{2}] = \frac{2+\sqrt{3}}{4}$

---

**8.** $2\cos^2 x - 3\cos x + 1 = 0$，$(2\cos x-1)(\cos x-1) = 0$。

$\cos x = \frac{1}{2}$：$x = \frac{\pi}{3}$ 或 $x = \frac{5\pi}{3}$。

$\cos x = 1$：$x = 0$。

解集 $\{0, \frac{\pi}{3}, \frac{5\pi}{3}\}$。

---

**9.** $\sin x + \sqrt{3}\cos x = 2\sin(x+\frac{\pi}{3}) = \sqrt{3}$。

$\sin(x+\frac{\pi}{3}) = \frac{\sqrt{3}}{2}$。

$x+\frac{\pi}{3} = \frac{\pi}{3}+2k\pi$ 或 $x+\frac{\pi}{3} = \pi-\frac{\pi}{3}+2k\pi = \frac{2\pi}{3}+2k\pi$。

$x = 2k\pi$ 或 $x = \frac{\pi}{3}+2k\pi$。

在 $[0, 2\pi)$ 中：$x = 0$ 或 $x = \frac{\pi}{3}$。

---

**10.** 由 $\tan(\alpha+\beta)$ 公式，$20°+40° = 60°$，$\tan 60° = \sqrt{3}$。

$\sqrt{3} = \frac{\tan 20°+\tan 40°}{1-\tan 20°\tan 40°}$

$\tan 20° + \tan 40° = \sqrt{3}(1-\tan 20°\tan 40°) = \sqrt{3} - \sqrt{3}\tan 20°\tan 40°$

$\tan 20° + \tan 40° + \sqrt{3}\tan 20°\tan 40° = \sqrt{3}$

---

**11.** $\sin^2\alpha + \sin^2\beta - \sin^2\alpha\sin^2\beta + \cos^2\alpha\cos^2\beta$

$= \sin^2\alpha + \sin^2\beta(1-\sin^2\alpha) + \cos^2\alpha\cos^2\beta$

$= \sin^2\alpha + \sin^2\beta\cos^2\alpha + \cos^2\alpha\cos^2\beta$

$= \sin^2\alpha + \cos^2\alpha(\sin^2\beta + \cos^2\beta)$

$= \sin^2\alpha + \cos^2\alpha = 1$。$\blacksquare$

---

**12.** $(1+\tan\alpha)(1+\tan\beta) = 1 + \tan\alpha + \tan\beta + \tan\alpha\tan\beta$。

由 $\alpha+\beta = \frac{\pi}{4}$：$\tan(\alpha+\beta) = 1 = \frac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}$。

$\tan\alpha+\tan\beta = 1-\tan\alpha\tan\beta$。

代入：$1 + (1-\tan\alpha\tan\beta) + \tan\alpha\tan\beta = 1 + 1 = 2$。$\blacksquare$
