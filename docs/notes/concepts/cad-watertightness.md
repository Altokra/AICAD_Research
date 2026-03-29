---
title: CAD Watertightness
tags: [cad, watertight, mesh-repair, cae]
related:
  - cad-vs-cae
  - stl-format
  - step-format
  - cad-repair
status: to-learn
---

# CAD Watertightness (水密性)

## 定义

水密性 (Watertightness) 指一个三维实体的表面是**完全封闭**的，没有孔洞、间隙或自交。相当于一个"密封的气球"——内部和外部完全隔离。

## 直觉理解

```
水密模型 = 完整的气球皮
          - 没有破洞
          - 没有裂缝
          - 没有自交重叠

非水密 = 漏气的气球
       - 有小孔
       - 有裂缝
       - 有重叠（折叠）
```

## 为什么水密性重要？

### 1. CAE 分析的前提
```
CAD 模型 ──→ 必须是水密实体 ──→ 才能划分网格 ──→ 才能做 CAE
               ↓
          否则网格划分失败
          或仿真结果不准确
```

### 2. 3D 打印的前提
```
水密 STL ──→ 切片软件能识别内外 ──→ 正确打印
非水密 ──→ 切片软件无法判断 ──→ 打印失败
```

### 3. 体积计算
```
水密模型可以计算体积（MC 方程）
非水密模型体积计算错误
```

## 水密性的数学定义

一个实体是水密的当且仅当：

1. **每个边恰好被两个面共享**
   - 不能有"悬边"（只被一个面用）
   - 不能有"多重边"（被三个以上面共享）

2. **所有面法线指向一致**（通常指向外部）
   - 用于内外判断
   - 用于渲染着色

3. **没有自交**
   - 面片不能和自身交叉
   - 相邻面片不能穿插

4. **流形 (Manifold)**
   - 每个顶点周围的拓扑是合法的
   - 不是"非流形"结构

## 水密性缺陷类型

### 1. 孔洞 (Holes)
```
    ╭───╮
    │ ○ │    ← 缺少面片，形成孔洞
    ╰───╯
```

### 2. 间隙 (Gaps)
```
    ╭───╮     ╭───╮
    │   ╰─────╯   │    ← 面片之间有间隙
    │             │
    ╰─────────────╯
```

### 3. 悬边 (T-vertices)
```
    ●───────────●
    │╲         ╱│
    │ ╲       ╱  │    ← T 型顶点，边没连接
    │  ╲     ╱   │
    ●───●────────●    ← 悬边
```

### 4. 自交 (Self-intersection)
```
      ╱╲
     ╱  ╲
    ╱ ○──╲────
   ╱     ╲ ╱
  ╱──────╲╱
         ↑ 面片和自己交叉
```

### 5. 法线反转 (Flipped Normals)
```
正常：法线都指向外
异常：某些面法线指向内
```

### 6. 非流形边 (Non-manifold Edges)
```
   ●───●───●
   │ ╲ │ ╱ │    ← 同一个边被3个面共享
   │  ╲│╱  │
   │   ●   │
   │  ╱│╲  │
   ●───●───●
```

## 如何检测水密性？

### 1. 边连接性检查
```python
# 每个边应该恰好被 2 个面共享
for edge in edges:
    adjacent_faces = get_adjacent_faces(edge)
    if len(adjacent_faces) != 2:
        print(f"边 {edge} 有 {len(adjacent_faces)} 个相邻面，不是水密")
```

### 2. 使用 Trimesh 检测
```python
import trimesh

mesh = trimesh.load("model.stl")
print(f"水密性: {mesh.is_watertight}")

# 详细诊断
if not mesh.is_watertight:
    # 找出有问题的部分
    mesh.show()  # 可视化
    trimesh.repair.fill_holes(mesh)
```

### 3. 使用 Open3D 检测
```python
import open3d as o3d

mesh = o3d.io.read_triangle_mesh("model.stl")
print(f"Watertight: {mesh.is_watertight}")

# 检查法线一致性
mesh.compute_vertex_normals()
mesh.orient_normals_consistent_toward_point()
```

## 水密性修复方法

### 传统方法

| 方法 | 说明 |
|------|------|
| **填充孔洞** | 找到孔洞，用面片填补 |
| **缝合间隙** | 将间隙处的边/顶点缝合 |
| **去除重复** | 合并重复顶点 |
| **去除自交** | 检测并修复自交 |
| **重网格化** | 重新生成高质量网格 |

### 基于学习的方法

- **MeshCNN**：用神经网络学习网格修复
- **PointNet/PointNet++**：处理点云
- **GeoDiff**：扩散模型用于几何修复
- **Score-based修复**：类似图像修复

## 修复流程建议

```
1. 读取模型
       ↓
2. 检测水密性 (is_watertight)
       ↓
3. 如果不是水密：
   a. 修复法线 (orient_normals)
   b. 合并重复顶点 (merge_vertices)
   c. 填充孔洞 (fill_holes)
   d. 移除重复面
   e. 修复自交
       ↓
4. 再次检测水密性
       ↓
5. 如果成功，导出
   如果失败，可能需要重网格化
```

## 在本项目中的角色

```
CAD 生成模型 (可能有缺陷)
       ↓
自动检测水密性
       ↓
AI 驱动的修复
       ↓
可用于 CAE 分析 / 3D 打印
```

## 疑问 / 待解决

1. 复杂拓扑缺陷（如"甜甜圈"有穿透）如何修复？
2. 基于学习的修复方法有哪些最新进展？
3. 如何量化修复质量（修复后和原始设计的偏差）？

## 参考资料

- trimesh 文档 - 修复功能
- Open3D 网格处理教程
- MeshLab 工具
