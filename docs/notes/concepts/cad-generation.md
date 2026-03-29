---
title: CAD Generation with AI
tags: [ai, cad, generation, deep-learning]
related:
  - cad-basics
  - transformer
  - cad-watertightness
status: to-learn
---

# CAD Generation with AI

## 定义

使用人工智能（深度学习）技术自动生成 CAD 模型，替代传统的手动建模过程。

## 生成任务的类型

### 1. Text-to-CAD
```
输入：文字描述 "a cylindrical gear with 20 teeth"
输出：CAD 模型
```

### 2. Image-to-CAD / Sketch-to-CAD
```
输入：图片 / 草图
输出：CAD 模型
```

### 3. Point Cloud-to-CAD
```
输入：三维点云（扫描数据）
输出：CAD 实体模型
```

### 4. CAD-to-CAD (Conditional Generation)
```
输入：粗糙 CAD 模型 / 参数
输出：更精细的 CAD 模型
```

## 传统方法 vs 深度学习方法

### 传统 CAD 生成
| 方法 | 说明 |
|------|------|
| 布尔运算 | 体素拼装 |
| 拉伸/旋转 | 2D → 3D |
| 参数化建模 | 尺寸驱动 |

### 深度学习方法

| 方法 | 代表工作 | 输出 |
|------|---------|------|
| **GAN** | 3D-GAN,GANocs | 体素/点云 |
| **VAE** | ShapeVAE, PointCaps | 隐表示 |
| **Diffusion** | Point-E, Shap-E, DreamFusion | 点云/NeRF |
| **Transformer** | Lambert, CADGPT | 序列/参数 |

## 主流方法详解

### 1. 点云生成 (Point Cloud Generation)

**Point-E** (OpenAI, 2022)
- 从文本生成 3D 点云
- 两阶段：先低分辨率再高分辨率
- 30 秒生成一个点云

**PointNet++**
- 处理点云的深度网络
- 可以从点云分类、分割

### 2. 隐式表示 (Implicit Representation)

**DeepSDF**
- 用 SDF (Signed Distance Field) 表示形状
- 网络学习 SDF 函数
- 可以表示任意精细的曲面

**Occupancy Networks**
- 用神经网络表示空间占用

### 3. 扩散模型 (Diffusion)

**Shap-E** (OpenAI, 2023)
- 文本/图像 → 3D 隐式表示
- 可导出为纹理网格

**DreamFusion** (Google, 2022)
- 文本 → 3D NeRF
- 分数蒸馏采样

### 4. Transformer 序列方法

**CADGPT** (2023)
- 将 CAD 参数序列化为 token
- 用 GPT 类模型生成 CAD 建模命令
- 输出直接是可编辑的 CAD 模型

**Lambert** (2022)
- Transformer 处理 CAD B-Rep 数据
- 学习 CAD 序列表示

### 5. 神经辐射场 (NeRF)

**NeRF**
- 用神经网络表示场景
- 从多视角图像重建 3D
- 不直接生成 CAD，但生成可渲染的 3D

## 评估指标

| 指标 | 说明 |
|------|------|
| **Chamfer Distance** | 两点云之间距离 |
| **Earth Mover's Distance (EMD)** | 点云匹配质量 |
| **F1 Score** | 精度/召回平衡 |
| **IoU** | 体素重叠率 |
| **CD-PSNR** | 点云到网格的投影质量 |

## 生成质量挑战

### 1. 水密性问题
```
AI 生成的模型经常不是水密的
- 表面有孔洞
- 几何有缺陷
- 不能直接用于 CAE
```

### 2. 精度问题
```
神经网络生成的是近似几何
- 不精确
- 有噪声
- 不满足工程公差
```

### 3. 多样性问题
```
模型可能缺乏多样性
- 模式坍塌
- 生成重复形状
```

## 修复的重要性

```
AI 生成 ──→ 缺陷检测 ──→ 智能修复 ──→ 可用 CAD
              ↓                    ↓
          水密性检查             水密模型
```

**为什么需要修复？**
1. 生成的模型 80%+ 都有水密性问题
2. 直接生成水密模型很难
3. 修复比重新生成更高效

## 本项目中的定位

```
目标：用 AI 生成 CAD，同时保证水密性

研究方向：
1. 如何生成更高质量的 CAD 几何？
2. 如何自动检测生成模型的缺陷？
3. 如何用 AI 修复 CAD 水密性问题？
4. 生成 → 修复 → CAE 一体化流程
```

## 重要论文 (待精读)

| 论文 | 年 | 方向 |
|------|-----|------|
| Point-E | 2022 | 扩散点云 |
| Shap-E | 2023 | 隐式 3D |
| DreamFusion | 2022 | NeRF |
| CADGPT | 2023 | CAD 序列 |
| Lambert | 2022 | B-Rep Transformer |

## 疑问 / 待解决

1. 如何评估生成的 CAD 模型是否"正确"？
2. CAD 生成如何与参数化建模结合？
3. 从点云/图像到精确 CAD 实体的重建方法？
4. 如何保证生成 + 修复的端到端流程？

## 参考资料

- Shape-E 论文 (arXiv)
- DreamFusion 论文
- CADGPT 论文
