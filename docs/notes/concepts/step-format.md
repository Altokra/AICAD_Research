---
title: STEP Format
tags: [cad, file-format, step]
related:
  - cad-basics
  - iges-format
  - stl-format
status: to-learn
---

# STEP Format (STEP)

## 定义

STEP (STandard for Exchange of Product model data) 是 ISO 10303 标准定义的**工业产品数据交换标准**。

## 直觉理解

STEP 是 CAD 文件的"通用语言"，就像 USB 接口是各种设备的通用连接方式。不同 CAD 软件通过 STEP 交换数据。

## 标准版本

| 版本 | 名称 | 说明 |
|------|------|------|
| AP203 | 配置文件控制设计 | 机械零件 |
| AP214 | 汽车设计 | 汽车工业 |
| AP242 | Managed Model Based 3D | 最新，涵盖所有 |

## 文件结构

STEP 文件是**纯文本**格式（.step, .stp）：

```
ISO-10303-21;
HEADER;
FILE_DESCRIPTION(('PMIL'),'2;1');
FILE_NAME('part.step','2024-01-01',(...),(...),(...));
FILE_SCHEMA(('AUTOMOTIVE_DESIGN'));
ENDSEC;
DATA;
#1=CARTESIAN_POINT('',(0.,0.,0.));
#2=DIRECTION('',(0.,0.,1.));
#3=AXIS2_PLACEMENT_3D('',#1,#2,...);
...
ENDSEC;
END-ISO-10303-21;
```

### 三个部分

1. **HEADER**：文件描述（作者、日期、标准）
2. **DATA**：实体数据（几何、拓扑）
3. **END-ISO-10303-21**：文件结束

## 核心概念：EXPRESS 语言

STEP 使用 EXPRESS 语言描述数据模型：

```express
ENTITY advanced_face;
  face_geometry : surface;
  same_sense : boolean;
END_ENTITY;
```

## 支持的几何类型

| 类型 | 说明 |
|------|------|
| **B-Rep** | 完整的边界表示 |
| NURBS 曲面 | 精确曲面 |
| 实体 (Solid) | 完整实体 |
| 曲线 | NURBS 曲线 |
| 点 | 离散点 |

## 与其他格式的对比

| 特性 | STEP | IGES | STL |
|------|------|------|-----|
| **精度** | 精确（数学） | 精确（数学） | 近似（三角网格） |
| **几何信息** | 完整 B-Rep | 完整 | 只有面片 |
| **文件大小** | 中等 | 大 | 小-中等 |
| **兼容性** | 很好 | 一般（老） | 最好 |

## Python 读写

### OpenCASCADE
```python
import OCP
from OCP.STEPControl import STEPControl_Reader

reader = STEPControl_Reader()
reader.ReadFile("model.step")
reader.TransferRoots()
shape = reader.OneShape()
```

### 其他库
- **pythonocc**：OpenCASCADE 的 Python 绑定
- **build123d**：较新的 Python CAD 库
- **cadquery**：Python 参数化 CAD

## 在本项目中的作用

```
STEP 文件 ──→ 读取几何 ──→ 处理/修复 ──→ 输出
   ↓
完整实体信息
可以转换为其他格式
```

### 应用场景
1. 从开源数据集读取 CAD 模型
2. 读取原始设计文件
3. 作为中间格式转换

## 局限性

1. **文件大**：文本格式冗长
2. **解析慢**：需要完整解析才能提取几何
3. **不支持纹理/材质**：纯几何
4. **版本兼容**：不同软件版本支持不同 AP

## 疑问 / 待解决

1. STEP 文件如何解析 NURBS 曲面参数？
2. 如何从 STEP 提取 B-Rep 信息用于分析？
3. STEP 到 STL 的转换精度如何控制？

## 参考资料

- ISO 10303 官方文档
- OpenCASCADE STEP 读写示例
