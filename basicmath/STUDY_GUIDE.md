# 基础数学：自学指南 (BasicMath: Study Guide)

> 本书面向成人自学者，尤其考虑到阿斯伯格（Asperger's）+ ADHD 的学习特点。我们相信：高智商与神经多样性可以成为数学学习的优势——深度思考、模式识别、对精确性的执着，都是数学之美所珍视的品质。本指南旨在帮助你建立适合自己的学习节奏，在严谨与弹性之间找到平衡。

---

## 1. 如何使用本教材 (How to Use This Textbook)

### 1.1 阅读策略 (Reading Strategies)

本教材按**推荐路径**设计为顺序阅读（详见 [DEPENDENCY_GRAPH.md](DEPENDENCY_GRAPH.md)）。

**但它不是小说**——你可以、也应该根据自己的兴趣灵活跳读。

- **跳过的规则**：只有在**确认已掌握该节内容**时才能跳过；请使用每节末的**自测题**验证。
- **若某节感觉太简单**：快速浏览，做 ★★★ 难度习题验证掌握程度。
- **若某节感觉太难**：先检查——你是否已完成所有先修内容？（每节开头会列明先修要求）

### 1.2 分支选择建议 (Branch Selection Guide)

- **主路径 (Main Path)**：Part 1 → 2 → 3 → 4 → 5 → 6（顺序推进）
- **Part 3 之后可分支**：
  - Part 7 → 8（组合 → 概率）可与 Part 4–6 并行
  - Part 9（线性代数）需在 Part 3 完成 + Part 5 Ch05（向量几何）完成后开始
- **欧氏几何 (Part 5 Ch01)** 可以提早起步，Part 1 完成后即可开始
- **跟随好奇心**：若某主题让你着迷，可通过各章的 `thinkers-corner.md` 深入探索

### 1.3 标记系统说明 (Marker System Reference)

| 标记 | 含义 |
|------|------|
| `[Bridge]` | 大学级别的预览内容，建立直觉，不求完全掌握 |
| `[暂认]` | 在严格证明之前先行使用的概念；后续会给出 justification |
| `[兑现]` | 先前假设的概念，现已被严格证明 |
| ★☆☆ / ★★☆ / ★★★ | 习题难度等级（由易到难） |
| ☐ / ☑ | 进度检查点（未完成 / 已完成） |
| ⚠️ | 常见错误或注意事项 |

---

## 2. 建议的学习节奏 (Recommended Study Rhythm)

### 2.1 时间规划 (Time Planning)

- 每节开头标有**预估学习时间**
- 一次学习时段理想为 **1–2 节**（约 2–4 小时）
- 全书预估总时长：**约 180–220 小时**
- 每天 1–2 小时：约 4–6 个月；每天 3–4 小时：约 2–3 个月
- **不要赶进度。理解优先于速度。**

### 2.2 利用超专注模式（Hyperfocus）

ADHD 学习者有时会进入**超专注 (Hyperfocus)**——这对数学学习是极强的优势。

- **当你感觉即将进入时**：减少干扰、备好水、设置温和的休息提醒
- **适合超专注的任务**：
  - 攻克一道有挑战性的证明
  - 完成一组 ★★★ 习题
  - 探索 `thinkers-corner.md` 中的拓展内容
- **超专注结束后**：记下你的收获（有助于巩固记忆）

### 2.3 日常学习结构 (Daily Study Structure)

1. **开场**（约 2 分钟）：回顾上一节的**要点回顾**
2. **定向**（约 5 分钟）：阅读新节的**全景图**和**动机**——帮助大脑建立预期
3. **主体学习**：主动式阅读（动笔，而非仅用眼）
4. **收尾**：完成**自测题**后再进入下一节
5. **小结**：更新进度，将 ☐ 改为 ☑

---

## 3. 卡住时的应对策略 (What to Do When Stuck)

### 3.1 诊断问题 (Diagnosing the Issue)

问自己：

1. **是先修知识缺口？** → 回到该节开头的先修链接
2. **是不认识的记号？** → 查阅 [appendices/symbol-table.md](appendices/symbol-table.md) 或 [appendices/notation-guide.md](appendices/notation-guide.md)
3. **是不熟悉的证明技巧？** → 复习 [appendices/proof-methods-ref.md](appendices/proof-methods-ref.md)
4. **是 [Bridge] 内容？** → 不必完全掌握；建立直觉即可继续

### 3.2 分解难点 (Breaking Down Difficulties)

- 将问题拆成更小的部分
- 先用具体数值试算（代入数字）
- 画图、画示意图
- 写出你**已经理解**的部分，再找出具体缺口
- 尝试运行 Python 示例代码——可视化往往能打开理解之门

### 3.3 何时跳过 (When to Skip)

- **非 [Bridge] 内容**：若卡住超过 30 分钟，标上 ☐，2–3 天后回头再试
- **[Bridge] 内容**：若卡住超过 15 分钟，可先行跳过（这是预览材料）
- **绝不跳过整章**——至少阅读**全景图**、**动机**和**要点回顾**

### 3.4 回退策略 (Fallback Strategy)

- 每节都会列出先修内容——必要时回到相应章节
- 每个 Part 配有 `review.md`——在继续前行前可用于巩固
- [DEPENDENCY_GRAPH.md](DEPENDENCY_GRAPH.md) 展示完整的依赖关系

---

## 4. ADHD 友好的学习技巧 (ADHD-Friendly Study Tips)

### 4.1 时间分块（Time Boxing）

- 使用**番茄工作法 (Pomodoro)**：25 分钟专注 + 5 分钟休息；或 50+10 用于深度工作
- 每节的预估学习时间可帮你规划需要多少个番茄钟
- 追踪已完成的节数以保持动力（☐ → ☑）

### 4.2 环境设置 (Environment Setup)

- **减少干扰**：手机远离、浏览器仅开一个标签页
- **备好草稿纸**——数学需要书写
- **为本教材准备专用笔记本**
- **背景**：安静或纯器乐（无歌词）

### 4.3 恢复学习（Re-entry After a Break）

间隔数天或数周后重新开始时：

1. 阅读最近 2–3 节已完成的**要点回顾**
2. **重做自测题**（不看答案）——检验你保留了哪些内容
3. **若通过**：从上次中断处继续
4. **若未通过**：重读该节（第二次会更快）

### 4.4 保持动力 (Maintaining Motivation)

- 每章的 `thinkers-corner.md` 专为智力刺激设计
- 当常规内容显得枯燥时，可做一次「好奇心休息」，进入 thinkers-corner
- **可视化追踪进度**：统计完成的章节数，庆祝里程碑
- 记住：本教材尊重你的智商——挑战本身就是回报

---

## 5. 推荐辅助工具 (Recommended Supplementary Tools)

### 5.1 数学可视化 (Mathematical Visualization)

- **[GeoGebra](https://www.geogebra.org/)** — 交互式几何与函数绘图  
  - 特别推荐：几何作图、函数图像探索、圆锥曲线动态演示

- **[Desmos](https://www.desmos.com/)** — 函数图像计算器  
  - 特别推荐：快速绘制函数、验证三角恒等式、参数方程可视化

### 5.2 计算与编程 (Computation & Programming)

- **Python** — 所有代码示例均使用 Python（参见 `code/requirements.txt`）
  - 安装：`pip install -r code/requirements.txt`
  - 常用库：matplotlib（绘图）、numpy（数值计算）、sympy（符号运算）

- **[Wolfram Alpha](https://www.wolframalpha.com/)** — 快速验证计算

### 5.3 笔记工具 (Note-Taking Tools)

- **纸笔笔记本**（强烈推荐用于数学）——书写有助于记忆
- **数字笔记**：任意支持 LaTeX 的 Markdown 编辑器（如 VS Code + Markdown+Math 扩展）

---

## 6. 习题使用建议 (How to Use the Exercises)

### 6.1 自测题 (Self-Check Questions)

- **每次都要做**，在进入下一节之前
- 通常 5–10 分钟即可完成，用于验证基本理解
- 使用 `<details>` 折叠区**先尝试再查看答案**

### 6.2 分级习题 (Tiered Exercises)

| 难度 | 建议 |
|------|------|
| ★☆☆ 基础题 | 独立思考 5 分钟后可查看解答 |
| ★★☆ 中等题 | 独立思考至少 15 分钟再查看 |
| ★★★ 困难题 | 建议尝试至少 30 分钟，允许搁置后重来 |

- **先写出自己的尝试**（即使不完整），再对照解答
- 标记未独立解决的题目，日后回来重做

### 6.3 挑战题 (Challenge Problems)

- 可选，但强烈推荐——有助于智力激发
- 常综合多个章节的内容
- 查看提示不必感到羞愧——竞赛数学的技巧会随时间积累

---

*祝你学习愉快。数学世界欢迎每一位愿意深入探索的心灵。*  
*返回 [README.md](README.md) | 学习路径参见 [DEPENDENCY_GRAPH.md](DEPENDENCY_GRAPH.md)*
