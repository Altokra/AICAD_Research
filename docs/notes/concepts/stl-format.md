---
title: STL Format
tags: [cad, file-format, stl, mesh, 3d-print]
related:
  - cad-basics
  - step-format
  - obj-format
  - cad-watertightness
status: to-learn
---

# STL Format (Stereolithography)

## 定义

STL 是**三角网格**格式，用大量小三角形面片近似表示三维表面。主要用于**3D 打印**和**快速原型**。

## 直觉理解

就像用很多小三角形拼成一个曲面，每个三角形由三个顶点和一个法向量定义。放大看会有"棱角感"。

## 文件格式

### ASCII 格式
```
solid part_name
  facet normal 0.0 0.0 1.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 1.0 0.0 0.0
      vertex 0.5 1.0 0.0
    endloop
  endfacet
  ...
endsolid part_name
```

### Binary 格式（二进制）
```
[80 bytes 头部]
[4 bytes 三角形数量]
[每个三角形: 12 floats (3顶点×3 + 法向×3) + 2 bytes 属性]
```

## 关键特性

| 特性 | 说明 |
|------|------|
| **仅面片** | 只有顶点坐标和法向量 |
| **无拓扑** | 没有"边-面"关联信息 |
| **无材质** | 纯几何 |
| **无颜色** | 可选的 80 字节头部 |
| **无装配信息** | 单零件 |

## STL 的问题

### 1. 不是实体表示
```
STL  ≠ 实体模型
STL  = 表面网格（可能是非水密的！）
```

### 2. 缺少拓扑信息
- 不知道哪些面是相邻的
- 不知道哪些边被几个面共享
- 无法直接进行布尔运算

### 3. 水密性问题
```
非水密 STL 的表现：
- 有孔洞（面片缺失）
- 有间隙（面片不连续）
- 有自交（面片交叉）
```

## STL 在 3D 打印中的作用

```
CAD 模型 (STEP) ──→ STL 导出 ──→ 切片软件 ──→ 3D 打印机
                              ↓
                         识别轮廓
                         计算路径
```

### 为什么 3D 打印需要 STL？
- 打印机只需要表面形状
- 三角网格是数控机床的天然表示
- 格式简单，打印机容易解析

## 分辨率 / 精度

STL 精度由**弦高**和**角度容差**控制：

| 参数 | 说明 |
|------|------|
| **弦高 (Chord Height)** | 三角形到曲面的最大距离 |
| **角度容差 (Angle Tolerance)** | 相邻三角形法线的最大夹角 |

### 文件大小估算
```
三角形数量 ≈ (4πR²) / (平均三角形面积)
三角形数量 ≈ 曲面积 / (0.5 × 边长² × sin60°)
```

## Python 读写

### NumPy + Trimesh
```python
import trimesh
import numpy as np

# 读取
mesh = trimesh.load("model.stl")

# 属性
vertices = mesh.vertices  # (N, 3) 顶点
faces = mesh.faces        # (M, 3) 三角面片索引

# 检查水密性
print(mesh.is_watertight)

# 修复（如果需要）
if not mesh.is_watertight:
    mesh.fill_holes()
    mesh.fix_normals()
```

### Open3D
```python
import open3d as o3d

mesh = o3d.io.read_triangle_mesh("model.stl")
print(f"Vertices: {len(mesh.vertices)}")
print(f"Triangles: {len(mesh.triangles)}")
print(f"Watertight: {mesh.is_watertight}")
```

## STL vs STEP

| 维度 | STL | STEP |
|------|-----|------|
| **表示类型** | 网格 | B-Rep 实体 |
| **精度** | 近似（可配置） | 精确数学 |
| **拓扑** | 无 | 完整 |
| **布尔运算** | 需要先重建 | 直接支持 |
| **文件大小** | 小 | 中-大 |
| **3D 打印** | ✅ 必须 | ❌ 不直接支持 |

## 在本项目中的作用

```
CAD 模型 (STEP)
      ↓ 转换为
STL 网格
      ↓ 检测/修复
水密的 STL
      ↓ 可用于
CAE 分析 / 3D 打印 / 渲染
```

### 研究点
1. STEP → STL 转换的精度损失
2. 从 STL 重建 B-Rep（网格 → 实体）
3. STL 水密性自动修复

## 疑问 / 待解决

1. 如何判断一个 STL 模型是否是水密的（算法层面）？
2. 从三角网格如何重建实体几何（B-Rep）？
3. 为什么三角网格法向量必须指向外部？

## 参考资料

- Trimesh 文档
- Open3D 文档
- 《3D Printing with Autodesk》
