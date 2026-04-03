---
name: sequence-transduction
description: 序列转导模型，将一个序列转换为另一个序列的深度学习模型
tags: [transformer, nlp, generation]
status: 待学习
created: 2026-04-01
updated: 2026-04-01
links:
  - "[[transformer-architecture]]"
  - "[[self-attention]]"
  - "[[encoder-decoder]]"
---

# Sequence Transduction Models

## 定义

**Sequence Transduction（序列转导）** — 将输入序列映射到输出序列的任务。

## 核心范式

```
输入序列 → Encoder → Decoder → 输出序列
```

典型的 seq2seq（sequence-to-sequence）任务。

## 常见任务

| 任务 | 输入 | 输出 |
|------|------|------|
| 机器翻译 | 中文句子 | 英文句子 |
| 语音识别 | 音频波形 | 文本 |
| 文本摘要 | 长文章 | 短摘要 |
| 代码生成 | 自然语言描述 | 代码 |
| CAD 生成 | 条件/约束 | CAD 数据 |

## 传统方法 vs Transformer

| 传统方法 | Transformer |
|----------|-------------|
| RNN/LSTM | Self-Attention |
| 顺序计算，难以并行 | 并行计算 |
| 长距离依赖难捕捉 | 全局注意力 |

## 与 CAD 修复/生成的关系

CAD 生成可以看作一种 sequence transduction：
- 输入：设计约束、参数化描述
- 输出：几何数据（BREP、Mesh、坐标序列）

这也是为什么 Transformer 在 CAD 智能生成领域有应用前景。

## 学习资源

- Attention Is All You Need（原始论文）
- [TODO] 补充更多资源

## 状态

- [ ] 理解基本概念
- [ ] 阅读相关论文
- [ ] 了解在 CAD 领域的应用
