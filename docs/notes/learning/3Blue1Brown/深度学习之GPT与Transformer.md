---
type: video
title: "深度学习之GPT与Transformer"
channel_creator: 
url: 
platform: # YouTube / Bilibili / Coursera 等
duration: 
tags:
  - video/tutorial
date_watched: 2026-04-02
---

> [!info] 视频简介
> 这个视频主要讲了什么？适合什么人群看？我为什么要看这个视频？

## ⏱️ 1. 时间戳与核心笔记 (Timestamps & Notes)
> 建议格式：`[时间] - 关键概念` (配合视频截图更佳)

- **00:00** - 概念A的引入
- **05:30** - 核心操作演示
	- *补充细节*：...
	- ![[Pasted image...]] (这里粘贴截图)
- **12:15** - 常见错误排查与总结

## 🧠 2. 核心知识总结 (Key Takeaways)

### 总览

- GPT

*Generative Pre-trained Transformer*

预测下一段文本


- token

输入会被切分为许多小片段 *token*，而每个 token 对应一个向量（一组数字）

我们希望将token的意义进行编码


- attention
然后丢到 Attention 模块里去，让这些token互相“交流”，改变编码，即，寻找上下文中能够更新另一些token含义的token，以及更新为何种含义

-  Multilayer Perception
/feed-forward 

并行处理更新后的token


Attention和MP的本质是大量矩阵乘法


### Embedding matirx


我们第一个遇到的矩阵 $W_E$
存储了预先设置的单词（token）对应的向量
初值随机，基于数据学习



### 输出

下一个可能token的概率分布

使用 *Unembedding matrix* $W_u$ 与最后一个token的向量相乘，接着通过softmax得到下一个词的概率分布

### softmax

将任意数列转化为合理概率分布


temperature  当t越大，概率分布越平均，即更有可能选到冷门词汇

logits->probabiilities


### large language models

1. pretraining
2. RLHF(Reinforcement Learning with Human Feedback)

## ❓ 3. 疑问与解答 (Q&A)
- **问题**：py model？
- **解答**：（自己查阅资料后的补充说明，或链接到其他笔记 [[解答笔记]]）

## 🔨 4. 实践练习 (Practice)
- （如果是操作类视频，记录你跟着实操的代码或步骤）
-