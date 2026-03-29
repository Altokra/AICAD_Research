---
title: Attention Is All You Need
authors: Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin
venue: NeurIPS
year: 2017
tags: [transformer, attention, seq2seq]
paper_url: https://arxiv.org/abs/1706.03762
status: read
---

# Attention Is All You Need

## 论文信息

- **Google Brain / Google Research**
- **NeurIPS 2017**
- **引用数**：非常高的影响力

## 核心贡献

- 提出 **Transformer** 模型
- **完全摒弃 RNN**，仅使用注意力机制（Attention）
- 实现真正的并行计算

## 模型架构

### Encoder
- 6层相同结构堆叠
- 每层包含：
  1. **Multi-Head Self-Attention**
  2. **Feed-Forward Network**
  3. 残差连接 + LayerNorm

### Decoder
- 6层相同结构堆叠
- 每层包含：
  1. **Masked Multi-Head Self-Attention**（防止看到未来位置）
  2. **Encoder-Decoder Attention**（cross attention）
  3. Feed-Forward Network
  4. 残差连接 + LayerNorm

## 核心机制

### Scaled Dot-Product Attention

```
Attention(Q,K,V) = softmax(QK^T / √d_k) V
```

- √d_k 缩放因子防止点积过大导致的梯度消失

### Multi-Head Attention

```
MultiHead(Q,K,V) = Concat(head_1,...,head_h) W^O
where head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)
```

- 多头让模型关注不同位置的多种表示子空间

### Positional Encoding

```
PE(pos,2i)   = sin(pos / 10000^(2i/d))
PE(pos,2i+1) = cos(pos / 10000^(2i/d))
```

- 使用正弦/余弦函数，无需学习
- 为序列注入位置信息

## 创新点

1. **并行计算**：摆脱 RNN 的顺序依赖
2. **长距离依赖**：注意力机制直接连接任意位置
3. **Multi-Head**：多子空间表示
4. **残差连接**：缓解深层网络训练困难
5. **Label Smoothing**：正则化

## 实验结果

| 任务 | 数据集 | 结果 |
|------|--------|------|
| 机器翻译 | WMT 2014 英德 | 28.4 BLEU (Best) |
| 机器翻译 | WMT 2014 英法 | 41.8 BLEU (Best) |

- 训练时间显著少于同期其他模型
- 推理速度更快

## 与其他概念的联系

- [[self-attention]] - 基础注意力机制
- [[multi-head-attention]] - 多头扩展
- [[scaled-dot-product-attention]] - 核心计算
- [[positional-encoding]] - 位置信息注入
- [[transformer-architecture]] - 整体架构

## 疑问 / 待深入

1. 为什么用正弦/余弦函数而不是学习到的位置嵌入？
2. Masked Attention 具体如何实现？
3. LayerNorm vs BatchNorm 的选择原因？

## 参考资料

- 原论文：[arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
- 图解博客：The Illustrated Transformer (Jay Alammar)
