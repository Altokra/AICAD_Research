---
title: PyTorch Learning Path
tags: [pytorch, deep-learning, python, tools]
related:
  - cad-basics
status: to-learn
---

# PyTorch Learning Path

## 为什么学 PyTorch

- **主流深度学习框架**：学术界和工业界都在用
- **动态图**：调试方便，Pythonic
- **生态丰富**：Lightning, Transformers, TorchVision 等
- **本项目需要**：CAD + AI 需要 PyTorch 实现模型

## 学习路线

```
阶段 1: 基础 (1-2 周)
├── Tensor 操作
├── 自动求导 (Autograd)
└── 数据加载 (Dataset/DataLoader)

阶段 2: 模型构建 (2-3 周)
├── nn.Module
├── 常用层 (Linear, Conv2d, etc.)
├── 优化器 (Adam, SGD)
└── 训练循环

阶段 3: 进阶 (2-4 周)
├── GPU 加速
├── 常用模块
│   ├── torchvision (图像)
│   ├── torchtext (文本)
│   └── torchaudio (音频)
├── 自定义数据集
└── 模型保存/加载

阶段 4: 实战 (持续)
├── 复现论文
├── 参加比赛
└── 做项目
```

## 基础概念

### Tensor (张量)

PyTorch 的核心数据结构，相当于 NumPy 的 ndarray，但可以在 GPU 上运算。

```python
import torch

# 创建 Tensor
x = torch.tensor([1.0, 2.0, 3.0])        # 从列表
x = torch.zeros(3, 4)                     # 全零
x = torch.randn(2, 3)                     # 正态分布随机
x = torch.arange(0, 10, step=2)           # 序列
x = torch.linspace(0, 1, steps=100)       # 线性分布

# NumPy 互转
import numpy as np
np_array = x.numpy()                      # Tensor → NumPy
x = torch.from_numpy(np_array)            # NumPy → Tensor

# 属性
print(x.shape)                            # 形状
print(x.dtype)                            # 数据类型
print(x.device)                           # CPU 或 GPU
```

### 自动求导 (Autograd)

PyTorch 自动计算梯度的核心。

```python
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x ** 2
z = y.sum()  # z = 1 + 4 + 9 = 14

z.backward()  # 计算梯度
print(x.grad)  # dz/dx = 2x = [2, 4, 6]
```

### GPU 加速

```python
# 检查 GPU 是否可用
print(torch.cuda.is_available())

# 移动到 GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
x = x.to(device)

# 在 GPU 上创建 Tensor
x = torch.randn(1000, 1000, device='cuda')
```

## 模型构建

### nn.Module

所有神经网络的基类。

```python
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 256)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

model = SimpleNet()
print(model)
```

### 常用层

| 层 | 说明 |
|---|---|
| `nn.Linear(in, out)` | 全连接层 |
| `nn.Conv2d(in, out, kernel)` | 卷积层 |
| `nn.MaxPool2d(kernel)` | 最大池化 |
| `nn.BatchNorm2d(channels)` | 批归一化 |
| `nn.ReLU/Sigmoid/Tanh` | 激活函数 |
| `nn.Dropout(p)` | Dropout 正则化 |
| `nn.LSTM/GRU` | 循环层 |
| `nn.Transformer` | Transformer 层 |

### 前向传播

```python
# 输入必须是 batch
x = torch.randn(32, 784)  # batch_size=32, features=784
output = model(x)
print(output.shape)  # torch.Size([32, 10])
```

## 数据加载

### Dataset

```python
from torch.utils.data import Dataset

class MyDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

dataset = MyDataset(data, labels)
```

### DataLoader

```python
from torch.utils.data import DataLoader

loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True,       # 训练时 shuffle
    num_workers=4,      # 多进程加载
    pin_memory=True     # GPU 加速
)

for batch_data, batch_labels in loader:
    # 训练循环中迭代
    pass
```

## 训练循环

```python
# 损失函数
criterion = nn.CrossEntropyLoss()

# 优化器
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 训练循环
for epoch in range(num_epochs):
    for batch_data, batch_labels in train_loader:
        # 1. 前向传播
        outputs = model(batch_data)
        loss = criterion(outputs, batch_labels)

        # 2. 反向传播
        optimizer.zero_grad()  # 梯度清零
        loss.backward()

        # 3. 更新参数
        optimizer.step()

    print(f"Epoch {epoch}, Loss: {loss.item()}")
```

## 模型保存与加载

```python
# 保存整个模型
torch.save(model, 'model.pth')

# 保存参数（推荐）
torch.save(model.state_dict(), 'model_weights.pth')

# 加载
model = SimpleNet()
model.load_state_dict(torch.load('model_weights.pth'))
model.eval()  # 推理模式
```

## 常用技巧

### 学习率调度

```python
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)

for epoch in range(100):
    train(...)
    scheduler.step()
```

### 早停

```python
best_loss = float('inf')
patience = 5
counter = 0

for epoch in range(num_epochs):
    val_loss = validate(model)
    if val_loss < best_loss:
        best_loss = val_loss
        torch.save(model.state_dict(), 'best_model.pth')
        counter = 0
    else:
        counter += 1
        if counter >= patience:
            break
```

### GPU 训练

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

for batch_data, batch_labels in train_loader:
    batch_data = batch_data.to(device)
    batch_labels = batch_labels.to(device)
    # 训练...
```

## 进阶模块

### torchvision (图像)

```python
import torchvision
import torchvision.transforms as transforms

# 预处理
transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485], std=[0.229])
])

# 加载数据集
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = DataLoader(trainset, batch_size=32, shuffle=True)
```

### torchaudio (音频)
### torchtext (文本)

## 调试技巧

### 1. 用 Python 调试器

```python
import pdb
pdb.set_trace()
```

### 2. 检查梯度

```python
print(model.fc1.weight.grad)  # 检查梯度
```

### 3. 检测 NaN

```python
if torch.isnan(loss):
    print("Loss is NaN!")
```

### 4. eval 模式

```python
model.eval()  # 关闭 Dropout，使用 BatchNorm 统计值
```

## 常见错误

| 错误 | 原因 | 解决 |
|------|------|------|
| 维度不匹配 | 输入/输出形状错误 | 检查每一层的输入输出 |
| CUDA OOM | 显存不足 | 减小 batch_size |
| 梯度为 None | 没调用 backward | 检查是否 zero_grad |
| 推理结果差 | 没 eval | 记得 model.eval() |

## 学习资源

| 资源 | 链接 |
|------|------|
| 官方教程 | https://pytorch.org/tutorials |
| 官方文档 | https://pytorch.org/docs |
| 书籍 | 《动手学深度学习》 (D2L) |

## 在本项目中的应用

```
CAD 文件 ──→ 预处理 ──→ Tensor ──→ PyTorch 模型
                                       ↓
                                  预测/生成
                                       ↓
                                  结果处理 ──→ 输出 CAD
```

## 疑问 / 待解决

1. 如何处理大规模 3D 数据集（内存问题）？
2. 如何在 PyTorch 中高效处理网格/点云？
3. 如何用预训练模型微调？

## 参考资料

- PyTorch 官方教程
- 《动手学深度学习》(D2L)
- PyTorch Discord 社区
