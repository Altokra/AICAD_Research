---
title: GDS3D 项目结构分析
type: project-analysis
status: in-progress
date: 2026-04-01
---

# GDS3D 项目结构分析

## 项目概述

**GDS3D** 是一个用于将 **IC（芯片）版图**渲染为 **3D 视图**的 C++ 程序。

| 项目信息 | |
|----------|------|
| **原作者** | Jasper Velner, Michiel Soer (特温特大学) |
| **fork 仓库** | https://github.com/Altokra/GDS3D |
| **基于** | gds2pov (Roger Light) |
| **语言** | C++ |
| **版本** | v1.9 |
| **许可证** | LGPL / GPL v2 |

---

## 项目目录结构

```
GDS3D/
├── libgdsto3d/                  # GDSII 解析 + 3D 生成
│   ├── gdsparse.cpp/h           # 解析 GDSII 文件
│   ├── gdsobject.cpp/h          # GDS 对象（单元）表示，一个完整的GDS单元
│   ├── gdsobjectlist.cpp/h     # 管理GDS单元
│   ├── gdselements.cpp/h        # GDS 图元（Boundary, Path, Text 等）主要定义计算模块，方便进行多边形运算
│   ├── gdspolygon.cpp/h         # 把多边形切为三角形，方便openGL渲染，其中用到了clipper库做布尔运算
│   ├── gdspath.cpp/h            # 将有宽度的线段转化为封闭多边形
│   ├── gdstext.cpp/h            # 标注文本处理
│   ├── gds_globals.cpp/h        # 全局定义，一些工具函数
│   ├── process_cfg.cpp/h        # 工艺配置文件解析
│   ├── assembly_cfg.cpp/h       # 装配配置
│   ├── Voronoi3D.cpp/h          # GMSH 导出用
│   │
│   ├── clipper/                 # 多边形布尔运算
│   │   ├── clipper.hpp/cpp
│   │   └── CMakeLists.txt
│   │
│   └── voro++/                  # Voronoi 图
│       ├── src/                 
│       ├── examples/            
│       └── zeo/                 
│
├── gdsoglviewer/               #  OpenGL 3D 渲染
│   ├── renderer.cpp/h           # OpenGL 渲染器（VBO, Shader, FBO）
│   ├── gdsobject_ogl.cpp/h      # OpenGL 对象绘制
│   ├── gdsparse_ogl.cpp/h       # OpenGL 解析接口
│   ├── geopolygon.cpp/h         # OpenGL 多边形
│   ├── outputStream.cpp/h       # GMSH 输出流
│   ├── ui_element.h             # UI 元素基类
│   ├── ui_highlight.cpp/h       # 网络高亮 UI
│   ├── ui_ruler.cpp/h           # 标尺 UI
│   ├── windowmanager.cpp/h       # 窗口管理
│   ├── listview.cpp/h           # 列表视图
│   ├── win_legend.cpp/h         # 图例窗口
│   ├── win_topmap.cpp/h         # 顶层单元选择窗口
│   ├── win_keymap.cpp/h         # 快捷键窗口
│   └── key_list.h              # 快捷键定义
│
├── math/                        # ★ 数学库
│   ├── VECTOR3D.cpp/h          # 三维向量
│   ├── VECTOR4D.cpp/h          # 四维向量
│   ├── MATRIX4X4.cpp/h         # 4x4 矩阵（变换矩阵）
│   ├── PLANE.cpp/h             # 平面
│   ├── FRUSTUM.cpp/h           # 视锥体（裁剪用）
│   ├── AA_BOUNDING_BOX.cpp/h   # 轴对齐包围盒
│   └── Maths.h                 # 公共头文件
│
├── skill/                       # Cadence Virtuoso插件
│   └── icdGDS3D.il             # Skill 脚本（Cadence 启动加载）
│
├── assembly/                    # 将多个芯片按照assembly中的规则同时渲染
│   └── as_example.assembly     # 多 GDS 装配定义

```

---

## 核心模块详解

### 1. libgdsto3d（核心逻辑层）

**职责**：GDSII 文件解析 → 几何建模 → 3D 结构生成

| 文件 | 作用 |
|------|------|
| `gdsparse.cpp` | GDSII 二进制格式解析，提取层、边界、路径等 |
| `gdsobject.cpp` | 表示 GDS 中的一个 cell/单元，包含多边形、路径、引用 |
| `gdspolygon.cpp` | 多边形处理：三角剖分 (tesselate)、合并 (merge)、相交检测 |
| `gdspath.cpp` | 路径处理（GDS 中的 Path 图元） |
| `process_cfg.cpp` | 解析工艺定义文件 (.txt)，获取层高、厚度、颜色 |
| `Voronoi3D.cpp` | 生成 GMSH 导出用的 Voronoi 剖分 |

**关键概念**：
- **GDSII 层次结构**：Library → Structure(Cell) → Elements (Boundary/Path/Text/SRef/ARef)
- **多边形三角剖分**：将 2D 多边形转换为三角形网格用于 3D 渲染
- **Clipper 库**：多边形布尔运算（合并、相交），用于 via 层和金属层的合并

### 2. gdsoglviewer（渲染层）

**职责**：OpenGL 3D 可视化渲染

| 文件 | 作用 |
|------|------|
| `renderer.cpp` | OpenGL 渲染器：VBO、Shader、FBO、屏幕截图 |
| `gdsobject_ogl.cpp` | 将 GDS 对象渲染为 OpenGL 图元 |
| `outputStream.cpp` | GMSH 文件输出（.geo 格式） |
| `ui_highlight.cpp` | 网络高亮追踪 UI |
| `ui_ruler.cpp` | 标尺测量 UI |

**技术亮点**：
- **VBO (Vertex Buffer Object)**：GPU 顶点缓冲，性能优化
- **Shader**：GLSL 顶点/片元着色器
- **FBO (Framebuffer Object)**：离屏渲染
- **视锥体裁剪**：只渲染可见区域

### 3. math（数学库）

**职责**：提供 3D 图形学所需的数学基础

| 类 | 作用 |
|----|------|
| `VECTOR3D` | 三维向量：点积、叉积、归一化、旋转 |
| `VECTOR4D` | 四维向量（齐次坐标） |
| `MATRIX4X4` | 4x4 变换矩阵：平移、旋转、缩放 |
| `PLANE` | 平面：点法式、距离计算 |
| `FRUSTUM` | 视锥体：6 个裁剪平面 |
| `AA_BOUNDING_BOX` | 轴对齐包围盒：碰撞检测 |

---

## 数据流

```
GDSII 文件 (.gds)
      ↓ gdsparse.cpp
GDSObjectList (层次结构)
      ↓
GDSPolygon 列表 (2D 多边形)
      ↓ process_cfg.cpp (获取层高厚度)
3D 多边形 (有 Height/Thickness)
      ↓ geopolygon.cpp (三角剖分)
三角形网格
      ↓ renderer.cpp (VBO 渲染)
OpenGL 3D 视图
```

---

## 关键代码文件速查

| 功能 | 文件 |
|------|------|
| 解析 GDSII | `libgdsto3d/gdsparse.cpp` |
| 多边形三角剖分 | `libgdsto3d/gdspolygon.cpp` |
| 工艺文件解析 | `libgdsto3d/process_cfg.cpp` |
| 3D 渲染 | `gdsoglviewer/renderer.cpp` |
| GMSH 导出 | `gdsoglviewer/outputStream.cpp` + `Voronoi3D.cpp` |
| 网络追踪 | `gdsoglviewer/ui_highlight.cpp` |
| 矩阵/向量运算 | `math/MATRIX4X4.cpp`, `math/VECTOR3D.cpp` |

---

## 学习路线图

### 第一阶段：环境搭建并复现（1天）04/01/2026

1. **克隆并编译**
   ```bash
   # Linux
   make -C linux

   # Windows
   # 用 Visual Studio 打开 win32/GDS3D.sln
   ```

2. **运行示例**
   ```bash
   # Linux
   ./RunLinux.sh

   # Windows
   win32\GDS3D.exe -p techfiles/example.txt -i gds/example.gds
   ```

### 第二阶段：核心流程（3-5 天）

**目标**：理解 GDSII → 3D 视图的完整流程

| 步骤 | 学习内容 | 关键文件 |
|------|----------|----------|
| 1 | GDSII 格式入门 | `gdsparse.cpp` |
| 2 | 工艺定义文件格式 | `process_cfg.cpp`, `techfiles/*.txt` |
| 3 | 多边形三角剖分原理 | `gdspolygon.cpp` |
| 4 | 层次结构展开 | `gdsobject.cpp`, `gdsobjectlist.cpp` |

**推荐实验**：
- 写一个小程序，只解析 GDSII 并打印各层信息
- 修改工艺文件，观察渲染变化

### 第三阶段：3D 渲染（3-5 天）

**目标**：理解 OpenGL 渲染管线

| 步骤 | 学习内容 | 关键文件 |
|------|----------|----------|
| 1 | OpenGL 基础概念 | `renderer.cpp` |
| 2 | VBO 与顶点缓冲 | `renderer.cpp` |
| 3 | Shader 基础 | `renderer.cpp` (loadShaderProgram) |
| 4 | 视锥体裁剪 | `math/FRUSTUM.cpp` |

**推荐实验**：
- 在渲染循环中加日志，观察调用顺序
- 修改颜色/透明度，观察效果

### 第四阶段：高级功能（2-3 天）

| 功能 | 描述 | 文件 |
|------|------|------|
| **网络高亮** | 追踪信号路径 | `ui_highlight.cpp` |
| **GMSH 导出** | 有限元分析 | `outputStream.cpp`, `Voronoi3D.cpp` |
| **爆炸图** | 层间间隙 | `renderer.cpp` |
| **装配** | 多 GDS 合并 | `assembly_cfg.cpp` |

### 第五阶段：项目贡献（持续）

1. 修复 `FIXME.txt` 中的问题
2. 添加新工艺文件支持
3. 优化性能
4. 编写测试

---

## 与本项目的关系

```
GDS3D                          AICAD_Research
─────────────────────────────────────────────────────
IC 版图文件 (GDSII)    ←→    CAD 文件 (STEP/STL/IGES)
芯片 3D 渲染           ←→    CAD 模型 3D 渲染
工艺定义文件           ←→    CAD 参数配置
GMSH 导出 (CAE)        ←→    有限元分析集成
```

**可借鉴的思想**：
1. **格式解析**：如何读取复杂二进制格式
2. **层次结构**：如何处理嵌套的层次模型
3. **三角剖分**：2D 多边形 → 3D 网格
4. **OpenGL 渲染**：实时 3D 可视化技术

---

## 疑问记录

1. GDSII 和 STEP 都是"数据交换格式"，有什么区别？
2. Voronoi 剖分在 CAD/CAE 中有什么应用？
3. Clipper 库的多边形布尔运算原理是什么？

---
## 代码更新


### stl导出

新增stl_report.cpp/h,实现导出功能

更改win_keymap.cpp设置快捷键O注释

更改gdsparse_ogl.cp绑定按键


### step导出

导入OCCT开源库

配置hxx/lib/dll

编写step_export.cpp/h

待优化（导出速度，导出大小）




## 参考资料

- 原项目 GitHub: https://github.com/trilomix/GDS3D
- GDSII 格式: https://en.wikipedia.org/wiki/GDSII
- Clipper 库: http://www.angusj.com/delphi/clipper.php
- Voro++ 库: https://math.lbl.gov/voro++/
- Gmsh: http://gmsh.info/
