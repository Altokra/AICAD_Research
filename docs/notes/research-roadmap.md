---
title: 研究学习路线图
type: roadmap
status: in-progress
last_updated: 2026-03-29
---

# CAD-AI 研究学习路线图

> 根据与师兄的讨论整理，包含所有需要学习的知识点

---

## 一、基础知识 (Foundation)

### 1.1 CAD 基本原理
**目标**：理解 CAD 是什么、CAD 内核的原理

**知识点**：
- CAD（Computer-Aided Design）定义与发展历程
- CAD 系统架构（内核 + 几何引擎 + UI）
- 主流 CAD 内核：Parasolid、ACIS、OpenCASCADE
- 边界表示法 (B-Rep)
- 实体建模与参数化建模
- 历史树 (Feature History)

**学习资源**：
- 书籍：《CAD Principles and Practices》

**笔记**：
- [[cad-basics]]

---

### 1.2 CAD 与 CAE 的关系
**目标**：理解 CAD 和 CAE 的区别与联系

**知识点**：
- CAE（Computer-Aided Engineering）定义
- CAD 建模 → CAE 分析的流程
- 网格划分 (Meshing) 的重要性
- 水密性 (Watertightness) 为什么关键
- CAD 修复在 CAE 流程中的位置

**笔记**：
- [[cad-vs-cae]]

---

### 1.3 三维几何文件格式
**目标**：深入理解 STEP、STL、IGES、OBJ 格式

**知识点**：

| 格式 | 全称 | 特点 | 用途 |
|------|------|------|------|
| STEP | STandard Exchange of Product | ASCENT II 文本格式，B-Rep 表示 | CAD 数据交换标准 |
| STL | Stereolithography | 三角网格，只有面片信息 | 3D 打印、快速原型 |
| IGES | Initial Graphics Exchange Specification | 老了，NURBS + 实体 | CAD 数据交换 |
| OBJ | Wavefront Object | 简单的顶点/面片数据 | 图形学、渲染 |

**关键理解**：
- STL 是"面片"表示，不是实体表示
- STEP 是完整的实体几何信息
- 格式转换可能丢失信息（水密性问题来源）

**笔记**：
- [[step-format]]
- [[stl-format]]
- [[iges-format]]
- [[obj-format]]

---

## 二、核心算法与技术 (Core Techniques)

### 2.1 Transformer 与 Attention
**目标**：掌握 Transformer 架构，这是 CV 和 NLP 领域的核心

**学习路径**：

1. **Attention Is All You Need** (必读)
   - [[attention-is-all-you-need]] - 已读
   - [[self-attention]]
   - [[multi-head-attention]]
   - [[scaled-dot-product-attention]]
   - [[positional-encoding]]
   - [[transformer-architecture]]

2. **前置知识**（可选但推荐）
   - RNN / LSTM 的问题
   - Seq2Seq 架构
   - 早期 Attention 机制

3. **延伸学习**
   - Vision Transformer (ViT)
   - DETR (DEtection TRansformer)
   - Diffusion Transformer

---

### 2.2 计算机视觉基础
**目标**：理解 CV 领域的基本概念和方法

**知识点**：
- 卷积神经网络 (CNN) 基础
- 目标检测 (Object Detection)
- 图像分割 (Segmentation)
- 点云处理 (Point Cloud)

**与本项目的关系**：
- CAD 模型可以被渲染成多视角图像
- 点云是三维重建的中间表示
- 几何深度学习

---

## 三、CAD 生成与修复 (CAD Generation & Repair)

### 3.1 CAD 自动生成
**目标**：了解 AI 如何生成 CAD 模型

**方向**：
- **文本到 CAD**：Text-to-CAD
- **图像到 CAD**：Image-to-CAD / Sketch-to-CAD
- **基于 Diffusion 的生成**：Point-E、Shap-E 等
- **基于 Transformer 的生成**：Transformer 用于序列生成

**相关工作**：
- CAD生成相关论文（待调研）

**笔记**：
- [[cad-generation]]

---

### 3.2 CAD 水密性修复
**目标**：理解并解决 CAD 模型的水密性问题

**核心问题**：
- 什么是水密性 (Watertightness)
- 非水密模型的问题（无法 CAE 分析）
- 常见缺陷：孔洞、间隙、自交

**修复方法**：
- 基于几何的修复（传统方法）
- 基于学习的修复（深度学习）

**相关论文**：
- 待调研

**笔记**：
- [[cad-watertightness]]

---

## 四、论文与学术 (Papers & Academia)

### 4.1 顶级会议
**目标**：了解领域内的顶级学术会议

| 会议 | 全称 | 领域 | 难度 |
|------|------|------|------|
| CVPR | Computer Vision and Pattern Recognition | 计算机视觉 | 很高 |
| ICCV | International Conference on Computer Vision | 计算机视觉 | 很高 |
| ECCV | European Conference on Computer Vision | 计算机视觉 | 高 |
| NeurIPS | Neural Information Processing Systems | 机器学习/AI | 很高 |
| ICLR | International Conference on Learning Representations | 深度学习 | 很高 |
| ICML | International Conference on Machine Learning | 机器学习 | 很高 |
| SIGGRAPH | Special Interest Group on GRAPHics | 图形学 | 高 |
| ICRA | International Conference on Robotics and Automation | 机器人 | 高 |

**CAD 相关**：
- Eurographics
- ACM TOG (Transactions on Graphics)
- CAD Journal

**笔记**：
- [[top-conferences]]

---

### 4.2 论文搜索与阅读
**目标**：掌握如何找论文、读论文

**资源**：
- arXiv (arxiv.org) - 预印本
- Google Scholar
- Semantic Scholar
- Connected Papers

**如何找 CAD 修复相关论文**：
- 搜索关键词：CAD repair, watertight, mesh repair, 3D generation
- 跟踪顶会论文

---

## 五、工具与技术栈 (Tools & Tech Stack)

### 5.1 Python 环境
**Anaconda / Miniconda**：
- 创建独立环境
- 管理依赖
- conda vs pip

**环境配置建议**：
```
conda create -n cad-ai python=3.10
conda activate cad-ai
pip install torch torchvision torchaudio
```

**笔记**：
- [[conda-setup]]

---

### 5.2 PyTorch 深度学习框架
**学习路径**：

1. **基础**：
   - Tensor 操作
   - 自动求导 (Autograd)
   - Dataset / DataLoader

2. **模型构建**：
   - nn.Module
   - 常用层 (Linear, Conv2d, etc.)
   - 优化器 (Adam, SGD)

3. **训练流程**：
   - 前向传播
   - 反向传播
   - 验证与测试

4. **进阶**：
   - GPU 加速
   - 分布式训练
   - Lightning / HuggingFace

**笔记**：
- [[pytorch-learning]]

---

### 5.3 CAD 处理工具

| 工具 | 语言 | 用途 |
|------|------|------|
| Open3D | Python | 3D 数据处理 |
| Trimesh | Python | 网格处理 |
| PyMeshLab | Python | 网格修复 |
| OpenCASCADE | C++/Python | CAD 几何内核 |
| Blender | Python | 3D 编辑 |
| Gmsh | C++ | 网格划分 |

---

## 六、项目研究方向 (Research Directions)

### 6.1 短期目标 (1-3个月)
- [x] 学习 Transformer 基础
- [ ] 掌握 CAD 文件格式
- [ ] 了解水密性问题
- [ ] 跑通基础实验

### 6.2 中期目标 (3-6个月)
- [ ] 精读 5-10 篇相关论文
- [ ] 复现 1-2 篇论文代码
- [ ] 确定具体研究方向

### 6.3 长期目标 (6个月+)
- [ ] 发表论文
- [ ] 构建完整系统

---

## 七、待调研清单 (To-Do Research)

- [ ] CAD 自动生成相关论文
- [ ] CAD 水密性修复相关论文
- [ ] CVPR 2025 中相关工作
- [ ] Transformer 在 3D 领域的应用
- [ ] Diffusion Model 用于几何生成

---

## 学习顺序建议

```
第1阶段：CAD基础（2周）
  ↓
第2阶段：Transformer（3-4周）
  ↓
第3阶段：CAD文件格式 + 水密性（2周）
  ↓
第4阶段：论文调研 + 确定方向（持续）
  ↓
第5阶段：复现 + 创新
```
