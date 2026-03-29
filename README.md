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
│   ├── papers/              # 论文阅读笔记
│   └── notes/               # 学习笔记
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

### CAD生成与修复
- [TODO] 添加相关论文

### Transformer / Attention
- Vaswani et al. *Attention Is All You Need* (NeurIPS 2017)

### 三维生成
- [TODO] 添加3D生成相关论文

## 学习笔记

- [papers/](docs/papers/) - 论文阅读笔记
- [notes/](docs/notes/) - 学习记录

## 致谢

感谢lg师兄，zqw老师的指导

## License

MIT License
