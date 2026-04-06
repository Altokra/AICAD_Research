---
type: video
title: "Transformer 的核心"
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

### query矩阵与key矩阵

query matrix-> $W_Q$

得到查询矩阵

key matrix -> $W_k$

key倾向于解答Query

所有的KQ相乘之后得到相关程度，再通过softmax函数变成0-1 的==相关度==
 
![[Pasted image 20260403192419.png]]


论文中的表达如下
$$
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}(\frac{QK^T}{\sqrt{d_k}})V
$$

- masking
防止后方token影响前方token


### Value矩阵

在我们的attention pattern里加入Vmatrix，得到许多 $\Delta E$ 

得到更加精确的嵌入向量


==single head of attention==


value down/value up


### 多次self-attention


multi-headed attention
## ❓ 3. 疑问与解答 (Q&A)
- **问题**：视频中某个地方没看懂 / 没讲透？
- **解答**：（自己查阅资料后的补充说明，或链接到其他笔记 [[解答笔记]]）

## 🔨 4. 实践练习 (Practice)
- （如果是操作类视频，记录你跟着实操的代码或步骤）
-