---
title: CAD Basics
tags: [cad, fundamentals]
related:
  - cad-vs-cae
  - step-format
  - stl-format
  - cad-watertightness
status: to-learn
---

# CAD Basics

## 定义

CAD (Computer-Aided Design) 是**计算机辅助设计**的缩写，指使用计算机软件创建、修改、分析和优化设计方案的技术。

## 直觉理解

CAD 就是"用电脑画三维零件"，像 SolidWorks、AutoCAD、Fusion 360 都是 CAD 软件。

## CAD 系统架构

```
┌─────────────────────────────────────┐
│           CAD 系统                    │
├─────────────────────────────────────┤
│  UI 层 (用户界面)                     │
├─────────────────────────────────────┤
│  几何引擎 (几何计算、布尔运算)          │
├─────────────────────────────────────┤
│  CAD 内核 (B-Rep、CSG 核心)           │
│  - Parasolid (Siemens)              │
│  - ACIS (Dassault)                   │
│  - OpenCASCADE (开源)                │
└─────────────────────────────────────┘
```

## 几何表示方法

### 1. B-Rep (Boundary Representation)
- **定义**：通过边界描述实体——顶点、边、面
- **优点**：精确表示、可编辑特征
- **用途**：CAD 软件内部表示

### 2. CSG (Constructive Solid Geometry)
- **定义**：用基本体素（方块、圆柱、球等）通过布尔运算构建
- **优点**：简单、节省内存
- **用途**：早期 CAD 系统

### 3. 网格表示 (Mesh)
- **定义**：用三角面片近似表示曲面
- **优点**：渲染简单、3D 打印友好
- **缺点**：精度有限、不是精确表示

## 建模方法

### 参数化建模 (Parametric Modeling)
- 尺寸作为参数，修改参数自动更新模型
- 特征树 (Feature Tree) 记录建模历史
- **例子**：SolidWorks、Fusion 360

### 直接建模 (Direct Modeling)
- 直接推拉面/边，不依赖历史
- 更灵活但难以精确控制
- **例子**：SketchUp、Fusion 360 混合模式

### 自由曲面建模 (Freeform Surface)
- NURBS 曲面
- 汽车、航空外形设计
- **例子**：CATIA、Rhinoceros

## 主流 CAD 内核

| 内核 | 公司 | 特点 |
|------|------|------|
| **Parasolid** | Siemens | 工业级、最多软件采用 |
| **ACIS** | Dassault (Spatial) | 法国血统，CATIA 基础 |
| **OpenCASCADE** | 开源 | 免费，社区活跃 |
| **CGM** | Airbus | 内部使用，开源 |

### OpenCASCADE (OCC)
- **开源**：LGPL 协议
- **语言**：C++，有 Python 绑定 (pythonocc)
- **功能**：几何造型、曲面、布尔运算、STEP/IGES 读写
- **用途**：学术研究、小型项目

```python
# OpenCASCADE Python 示例
import pythonocc
```

## 常用 CAD 文件格式

| 格式 | 类型 | 说明 |
|------|------|------|
| [[step-format|STEP]] | 实体 | 国际标准，完整几何信息 |
| [[iges-format|IGES]] | 实体/曲面 | 老格式，数据交换 |
| [[stl-format|STL]] | 网格 | 三角面片，3D 打印 |
| [[obj-format|OBJ]] | 网格 | 简单，图形学常用 |
| SLDPRT | 实体 | SolidWorks 专有 |
| DWG | 2D/3D | AutoCAD 格式 |

## 关键概念

### 历史树 (Feature History)
- 记录每一步操作
- 可撤回、重做、修改参数
- 参数化建模的核心

### 约束 (Constraints)
- 几何约束：平行、垂直、相切
- 尺寸约束：长度、角度、半径

### 装配 (Assembly)
- 零件之间的配合关系
- 约束：匹配、对齐、角度

## CAD 在工程中的流程

```
概念设计 → CAD 建模 → CAE 分析 → 制造
   ↓           ↓           ↓
 草图      零件设计     网格划分
                          ↓
                      结果评估
```

## 与本项目的关系

- CAD 是研究对象
- 需要读写 STEP/STL 文件
- 需要理解 B-Rep 和网格的区别
- 水密性问题直接影响 CAE 分析

## 疑问 / 待解决

1. CAD 内核是如何实现布尔运算的？
2. 参数化建模的特征树如何存储和回放？
3. NURBS 曲面的数学原理是什么？

## 参考资料

- 《CAD Principles and Practices》- Michel A. G. Halici
- OpenCASCADE 官方文档
- Parasholid 技术文档
