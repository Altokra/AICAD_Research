# CAD-AI-Research

> AI-driven CAD Generation and Repair Research

## 项目简介

本项目聚焦于**CAD智能生成与修复**领域，研究利用深度学习技术（Transformer、Diffusion等）实现：
- CAD模型自动生成
- CAD水密性（Watertightness）修复
- 三维几何文件（STEP/STL/IGES/OBJ）处理

## 环境配置

### 依赖环境
- Python >= 3.8
- PyTorch >= 2.0
- CUDA >= 11.8（GPU训练）

### 安装依赖

```bash
conda create -n cad-ai python=3.10
conda activate cad-ai

# PyTorch (根据你的CUDA版本选择)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# 基础依赖
pip install numpy pandas matplotlib pandas
pip install scikit-learn open3d trimesh

# Jupyter
conda install jupyter notebook
```

### 项目结构

```
.
├── README.md
├── .gitignore
├── requirements.txt
├── data/                    # 数据目录
│   ├── raw/                 # 原始CAD文件 (STEP/STL/IGES)
│   ├── processed/           # 预处理后的数据
│   └── outputs/             # 生成/修复结果
├── docs/                    # 文档
│   ├── papers/              # 论文PDF
│   │   └── attention_is_all_your_need.pdf
│   ├── notes/               # 学习笔记
│   │   ├── concepts/        # 原子化概念笔记
│   │   ├── papers/          # 论文阅读笔记
│   │   ├── learning/       # 学习心得/视频笔记
│   │   └── templates/      # 笔记模板
├── notebooks/               # Jupyter notebooks
│   └── experiments/         # 实验notebooks
├── src/                     # 源代码
│   ├── data/                # 数据处理
│   ├── models/              # 模型定义
│   ├── utils/               # 工具函数
│   └── visualization/       # 可视化
├── configs/                 # 配置文件
├── checkpoints/             # 模型权重
├── logs/                    # 训练日志
├── scripts/                 # 脚本
│   ├── train.sh
│   └── eval.sh
└── tests/                   # 单元测试
```

## 主要内容

### 核心模块

| 模块 | 说明 |
|------|------|
| `src/data/` | CAD文件读取、预处理、水密性检测 |
| `src/models/` | Transformer/Diffusion模型 |
| `src/utils/` | 几何操作、评估指标 |
| `src/visualization/` | 三维模型可视化 |

### 数据集

- [TODO] 补充数据集说明

### 模型

- [TODO] 补充模型说明

## 使用说明

### 训练

```bash
python scripts/train.sh --config configs/default.yaml
```

### 评估

```bash
python scripts/eval.sh --checkpoint checkpoints/best.pth
```

## 相关论文

### Transformer / Attention
- Vaswani et al. *Attention Is All You Need* (NeurIPS 2017) [[笔记]](docs/notes/papers/attention-is-all-you-need.md)

### CAD 生成
- [TODO] CAD 生成相关论文

### CAD 修复 / 水密性
- [TODO] CAD 修复相关论文

### 3D 生成
- Point-E (OpenAI, 2022)
- Shap-E (OpenAI, 2023)
- DreamFusion (Google, 2022)
- CADGPT (2023)

## 学习笔记

- [papers/](docs/papers/) - 论文PDF
- [notes/](docs/notes/) - 学习记录

## 研究路线图

详见 [docs/notes/research-roadmap.md](docs/notes/research-roadmap.md)

### 基础知识

| 概念 | 笔记位置 | 状态 |
|------|----------|------|
| [[cad-basics]] | CAD 基础原理 | 待学习 |
| [[cad-vs-cae]] | CAD 与 CAE 区别 | 待学习 |
| [[step-format]] | STEP 格式 | 待学习 |
| [[stl-format]] | STL 格式 | 待学习 |
| [[iges-format]] | IGES 格式 | 待学习 |
| [[obj-format]] | OBJ 格式 | 待学习 |

### 核心算法

| 概念 | 笔记位置 | 状态 |
|------|----------|------|
| [[transformer-architecture]] | Transformer 架构 | 待学习 |
| [[self-attention]] | 自注意力机制 | 待学习 |
| [[multi-head-attention]] | 多头注意力 | 待学习 |
| [[scaled-dot-product-attention]] | 缩放点积注意力 | 待学习 |
| [[positional-encoding]] | 位置编码 | 待学习 |

### 研究方向

| 方向 | 笔记位置 | 状态 |
|------|----------|------|
| [[cad-watertightness]] | CAD 水密性 | 待学习 |
| [[cad-generation]] | CAD 自动生成 | 待学习 |
| [[cad-repair]] | CAD 智能修复 | 待学习 |
| [[top-conferences]] | 顶会指南 | 待学习 |
| [[pytorch-learning]] | PyTorch 学习路径 | 待学习 |




## 开源代码学习


### GDS3D

#### 04/01/2026

clone仓库 ，

复现
Debug\GDS3D.exe" -p "techfiles"" -i "gds"

复现基本成功
---

klayout ==> 0.30.7







## TODO

### 辅助学习

[zhihu](https://www.zhihu.com/question/61077555/answer/2914496700)

[limu](https://www.bilibili.com/video/BV1pu411o7BE/?vd_source=66f42ac67f5881b4de8c76d2e71a1137)

[3Blue1Brown](bilibili.com/video/BV1TZ421j7Ke/?spm_id_from=333.788.recommend_more_video.1&trackid=web_related_0.router-related-2479604-9shrk.1775111670857.989)


[Michael Nielsen](http://neuralnetworksanddeeplearning.com/)


## 致谢

感谢lg师兄，zqw老师的指导

## License

MIT License
