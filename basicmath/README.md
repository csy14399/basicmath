# 基础数学：从根基到大学之门 (BasicMath: From Foundations to the Gate of University)

## 项目简介 (Project Description)

本教材为**成人自学**设计，从数学逻辑一路铺陈到线性代数入门。结构系统、层次分明，每个概念都回答「为什么」——直觉先行，严谨紧随。

A systematically structured mathematics textbook designed for adult self-learners, covering from mathematical logic to introductory linear algebra. Every concept answers "why". Intuition-first, then rigorous treatment.

---

## 目标读者 (Target Reader)

- 已有高中数学基础（函数、初等三角）的**成人自学者**
- 高智力水平，擅长精确定义与系统化思维
- 适合阿斯伯格与 ADHD 特质：偏好结构化、视觉辅助与清晰的逻辑链条

---

## 内容范围 (Scope)

| 层次 | 说明 |
|------|------|
| **核心层** | 大学前数学的扎实掌握 |
| **桥梁层** [Bridge] | 初次接触大学数学的内容，在标题中用 `[Bridge]` 标注 |

---

## 内容总览 (Content Overview)

| 部分 | 主题 |
|------|------|
| Part 1 | **基础**：逻辑、集合论、证明方法 |
| Part 2 | **数系与数论** |
| Part 3 | **代数** |
| Part 4 | **函数** |
| Part 5 | **几何** |
| Part 6 | **分析预备** |
| Part 7 | **组合数学** |
| Part 8 | **概率论** |
| Part 9 | **线性代数初步** [Bridge] |

---

## 如何使用本教材 (How to Use This Textbook)

- 建议从 [STUDY_GUIDE.md](STUDY_GUIDE.md) 开始，按推荐学习路径阅读
- 了解章节依赖关系，可参阅 [DEPENDENCY_GRAPH.md](DEPENDENCY_GRAPH.md)

---

## 文件结构 (File Structure)

```
basicmath/
├── part-01-foundations/     # 逻辑、集合、证明
├── part-02-numbers/        # 数系与数论
├── part-03-algebra/        # 代数
├── part-04-functions/      # 函数
├── part-05-geometry/       # 几何
├── part-06-analysis-prep/  # 分析预备
├── part-07-combinatorics/  # 组合数学
├── part-08-probability/    # 概率论
├── part-09-linear-algebra/ # 线性代数初步 [Bridge]
├── code/                   # 代码示例（按 part 组织）
├── images/                 # 插图（含 AI/代码生成）
└── appendices/             # 附录与符号说明
```

每部分下按章节（chapter）组织，每章含主文与 `exercises/` 练习目录。

---

## 技术需求 (Technical Requirements)

- **编辑器**：VS Code 或 Cursor，搭配数学渲染扩展（如 Markdown+Math）
- **Python**：3.8+，用于运行书中的代码示例
- **依赖**：参见 [code/requirements.txt](code/requirements.txt)

---

## 约定与标记 (Conventions)

- 符号与记法详见 [appendices/notation-guide.md](appendices/notation-guide.md)
- 标记体系：`[Bridge]`（桥梁内容）、`[暂认]`/`[兑现]`（直觉先行再严格化）、难度星级 ★☆☆/★★☆/★★★

---

*欢迎从 Part 1 开始，稳扎稳打地搭建你的数学地基。*
