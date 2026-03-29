---
title: OBJ Format
tags: [cad, file-format, obj, graphics]
related:
  - cad-basics
  - stl-format
status: to-learn
---

# OBJ Format

## 定义

OBJ (Wavefront Object) 是 **Alias|Wavefront** 公司开发的**简单三维模型格式**，主要用于**图形学**（渲染、游戏、影视），而非 CAD 工程。

## 直觉理解

OBJ 就像一张"购物清单"：列出所有顶点在哪里，所有面片怎么连接。简单直观，但只包含基本几何信息。

## 文件格式

OBJ 是**纯文本**格式（.obj）：

```
# 注释以 # 开头

# 顶点 (vertices)
v 0.0 0.0 0.0      # 顶点1
v 1.0 0.0 0.0      # 顶点2
v 0.5 1.0 0.0      # 顶点3
v 0.5 0.5 1.0      # 顶点4（可选的第四个是w坐标）

# 法向量 (normals)
vn 0.0 0.0 1.0    # 法向量1

# 纹理坐标 (texture coordinates)
vt 0.0 0.0        # 纹理坐标1
vt 1.0 0.0        # 纹理坐标2

# 面 (faces) - 用顶点索引
f 1 2 3           # 三角形：顶点1-2-3
f 1 3 4           # 三角形：顶点1-3-4

# 也可以带纹理和法向量
f 1/1/1 2/2/1 3/3/1    # 顶点/纹理/法向量
```

## 支持的元素

| 元素 | 前缀 | 说明 |
|------|------|------|
| 顶点 | `v` | x, y, z, (可选 w) |
| 纹理坐标 | `vt` | u, v, (可选 w) |
| 法向量 | `vn` | nx, ny, nz |
| 面 | `f` | 顶点索引，可带纹理/法向量 |
| 曲线 | `c` | 贝塞尔曲线 |
| 曲线点 | `cstype` | 曲线类型 |

## 材质 (MTL)

OBJ 通常配合 .mtl 文件存储材质：

```
# mymodel.mtl
newmtl material_name
Kd 1.0 1.0 1.0    # 漫反射颜色 (RGB)
Ks 0.5 0.5 0.5    # 镜面反射颜色
Ns 100.0           # 镜面指数
d 1.0              # 透明度
```

## OBJ 的特点

### 优点
- **极其简单**：容易解析、容易生成
- **人类可读**：直接用文本编辑器查看
- **广泛支持**：几乎所有 3D 软件都支持
- **小文件**：比 STL ASCII 更紧凑

### 缺点
- **无拓扑信息**：面片之间无连接关系
- **无层级结构**：无法表示装配体
- **无材质信息**（单独存 MTL）
- **无精确曲面**：只有三角/四边形面片

## OBJ vs STL

| 维度 | OBJ | STL |
|------|-----|-----|
| **顶点定义** | 共享（去重） | 每个三角形重复 |
| **法向量** | ✅ 支持 | ❌ 不支持 |
| **纹理坐标** | ✅ 支持 | ❌ 不支持 |
| **材质** | ✅ (MTL) | ❌ |
| **拓扑** | 无 | 无 |
| **文件大小** | 较小 | 较大 |

## Python 读写

### NumPy + Trimesh
```python
import trimesh

# 读取（自动识别格式）
mesh = trimesh.load("model.obj")

# 读取 OBJ + MTL
mesh = trimesh.load("model.obj", process=False)

# 属性
vertices = mesh.vertices
faces = mesh.faces
visual = mesh.visual  # 颜色/材质

# 导出
mesh.export("output.obj")
```

### 使用 numpy 直接解析
```python
import numpy as np

vertices = []
faces = []

with open("model.obj", "r") as f:
    for line in f:
        if line.startswith("v "):
            vertices.append([float(x) for x in line.split()[1:]])
        elif line.startswith("f "):
            # 处理 f v1 v2 v3 ... 格式
            parts = line.split()[1:]
            face = [int(p.split("/")[0]) - 1 for p in parts]  # 索引从1开始
            faces.append(face)

vertices = np.array(vertices)
faces = np.array(faces)
```

## 在本项目中的位置

### 用途
```
OBJ 文件
  ↓ 读取
三角网格
  ↓ 处理
水密性检查/修复
  ↓
可用于渲染 / 3D 打印
```

### 与其他格式的转换
```
STEP (CAD) → STL/OBJ (Mesh) → 处理/修复
     ↑              ↓
     ←── 转换 ←──
```

## 应用场景

| 领域 | 用途 |
|------|------|
| **游戏** | 模型导入、渲染 |
| **影视** | 特效、动画 |
| **深度学习** | 3D 重建输入/输出 |
| **3D 打印** | 格式转换中间态 |
| **CAD/CAM** | 快速查看几何 |

## 在图形学中的地位

OBJ 是**入门级**格式。专业工作流通常用：
- **FBX**：动画、绑定
- **glTF**：WebGL、游戏实时
- ** Alembic**：影视特效

## 疑问 / 待解决

1. OBJ 面索引从 1 开始 vs Python 从 0 开始，容易出错如何避免？
2. 为什么 OBJ 不存储拓扑信息，有什么影响？
3. 如何用 OBJ + MTL 渲染出带颜色的模型？

## 参考资料

- Wavefront OBJ 文件格式规范
- trimesh 文档
