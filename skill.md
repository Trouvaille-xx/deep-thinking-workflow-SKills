---
name: "deep-thinking-workflow"
description: "深度思考工作流 - 一套渐进式思考方法论，帮助用户从表面理解深入到本质洞察。触发场景：面对复杂问题、分析论证、做出重要决策、写作框架构建。"
intent: "通过渐进式加载机制，将深度思考拆解为可执行的子技能模块，配合脚本引擎和内存存储，实现思考过程的持久化和可视化输出。"
type: "workflow"
version: "1.3.0"
author: "WorkBuddy"
tags: ["thinking", "analysis", "decision", "reasoning", "structured"]
trigger:
  - "如何深度思考"
  - "怎么分析这个问题"
  - "帮我理清思路"
  - "这个决策该怎么考虑"
  - "分析一下"
  - "深层原因是什么"
load_order: 3
dependencies:
  - "sub_skills/reflexivity.md"
  - "sub_skills/critical_thinking.md"
  - "sub_skills/systemic_thinking.md"
  - "sub_skills/creative_thinking.md"
  - "sub_skills/structured_expression.md"
  - "sub_skills/output_generation.md"
  - "sub_skills/perspectives/perspective_psychology.md"
  - "sub_skills/perspectives/perspective_communication.md"
  - "sub_skills/perspectives/perspective_product.md"
  - "sub_skills/perspectives/perspective_economics.md"
  - "sub_skills/perspectives/perspective_political.md"
  - "sub_skills/perspectives/perspective_design.md"
---

# 深度思考工作流 (Deep Thinking Workflow)

## 概述

深度思考不是一蹴而就的能力，而是一套可以习得的思维框架。本工作流通过**渐进式加载**机制，将复杂的思考过程拆解为可执行的子技能模块。

```
┌─────────────────────────────────────────────────────────────┐
│                     深度思考工作流                             │
├─────────────────────────────────────────────────────────────┤
│  Level 1: 快速思考 ──→ Level 2: 结构分析 ──→ Level 3: 本质洞察  │
│     ↓                  ↓                   ↓               │
│  是什么？            为什么？              还有呢？            │
└─────────────────────────────────────────────────────────────┘
```

## 核心原则

### 1. 渐进式加载
- **Level 1 (快速启动)**: 5W1H 快速框架，30秒获得初步结构
- **Level 2 (深入分析)**: 引入子技能模块，进行专项深度思考
- **Level 3 (本质洞察)**: 多维度交叉验证，挖掘第一性原理

### 2. 元数据驱动
每个思考节点都携带结构化元数据：
- 置信度 (0-1)
- 思考时长
- 关联知识点
- 反思标记

### 3. 内存持久化
- 思考过程中的关键洞察自动存入内存
- 支持跨会话上下文恢复
- 思考路径可追溯

## 子技能模块

### sub_skills/reflexivity.md
**反身性觉察** (元技能) - 识别思考者与系统的相互影响
- 适用场景：决策前自检、偏见识别、立场澄清
- 优先级：最先激活

### sub_skills/critical_thinking.md
**批判性思维** - 评估论证质量，识别逻辑谬误
- 适用场景：论证分析、观点评估、信息甄别
- 包含方法：价值澄清、事实/观点剥离、第一性原则+5Why追问

### sub_skills/systemic_thinking.md
**系统性思维** - 理解要素关系，预测系统行为
- 适用场景：复杂问题、多因素决策、趋势预测
- 包含方法：多维归因矩阵、二阶/三阶传导、实践尺度拉伸

### sub_skills/creative_thinking.md
**创造性思维** - 突破思维定式，产生新颖洞见
- 适用场景：产品创新、问题解决、方案设计

### sub_skills/structured_expression.md
**结构化表达** - 将思考结果转化为清晰输出
- 适用场景：写作、演讲、汇报、文档撰写

### sub_skills/perspectives/
**多视角角色分析** - 切换专业视角获得全面洞察
| 视角 | 核心关注 | 关键问题 |
|------|---------|---------|
| 心理学 | 动机/认知/情感 | 用户真正想要什么？ |
| 传播学 | 信息/符号/影响 | 信息如何被接收和扭曲？ |
| 产品经理 | 需求/价值/迭代 | 做什么才有意义？ |
| 经济学 | 激励/供需/成本 | 什么驱动行为？ |
| 政治学 | 权力/利益/联盟 | 各方如何博弈？ |
| 设计学 | 体验/共情/本质 | 什么让用户心动？ |

## 方法归属总览

| 方法 | 所属子技能 | 类型 |
|------|-----------|------|
| 反身性觉察 | reflexivity.md | 元技能 |
| 价值澄清 | critical_thinking.md | 批判性思维 |
| 事实/观点剥离 | critical_thinking.md | 批判性思维 |
| 第一性原则+5Why | critical_thinking.md | 批判性思维 |
| 逻辑谬误识别 | critical_thinking.md | 批判性思维 |
| 多维归因矩阵 | systemic_thinking.md | 系统性思维 |
| 二阶/三阶传导 | systemic_thinking.md | 系统性思维 |
| 实践尺度拉伸 | systemic_thinking.md | 系统性思维 |
| SCAMPER | creative_thinking.md | 创造性思维 |
| 多视角分析 | perspectives/*.md | 视角切换 |

## 使用流程

```
用户输入 → 意图识别 → 执行模式选择 → 子技能调用 → 内存存储 → 用户确认 → 输出生成
    ↓           ↓              ↓              ↓           ↓          ↓          ↓
  问题文本   分类分析    渐进/一步选择   模块执行    持久化    干预点    MD + HTML
```

### 执行模式选择

在开始深度分析前，必须询问用户选择执行模式：

#### 渐进性执行模式（推荐）

分阶段执行，在关键节点设置断点，用户可以介入：

```
阶段1: 问题调研与信息收集
    ↓ [完成]
🔴 断点1: 用户介入
    - 可调整分析方向
    - 可补充遗漏的信息
    - 可修改初步结论
    ↓ [用户确认继续]
    
阶段2: 内容整理与深度分析
    ↓ [完成]
🔴 断点2: 用户确认输出
    - 询问是否生成 Markdown 报告
    - 询问是否生成 HTML 可视化报告
    - 用户可进一步调整内容
    ↓ [用户确认]
    
输出生成
```

**渐进模式交互示例**：

```
🔵 [深度思考工作流] 请选择执行模式：

1️⃣ 渐进性执行（推荐）
   - 分阶段执行，可在关键节点介入
   - 调研完成后询问是否继续/调整
   - 输出前询问是否生成MD/HTML

2️⃣ 一步执行
   - 一次性完成所有分析
   - 分析完成后询问是否输出

请选择 [1/2]：
```

#### 一步执行模式

一次性完成所有分析，不设置断点：

```
信息收集 → 深度分析 → 结论整理 → 输出生成
    ↓         ↓          ↓          ↓
  一次性    一次性      一次性    完成后询问
  完成      完成        完成      是否输出MD/HTML
```

### 输出生成规范 (Output Generation)

深度思考完成后，必须生成输出文档：

| 文档类型 | 文件格式 | 必须生成 | 用户确认 |
|----------|----------|----------|----------|
| **Markdown报告** | `.md` | ❌ 否 | ✅ 是（询问用户） |
| **HTML可视化报告** | `.html` | ❌ 否 | ✅ 是（询问用户） |

## 配置文件

参见 `config/config.json` - 包含各子技能的权重、提示词模板、输出格式配置。

## 脚本引擎

- `script/deep_think.py` - Python 思考分析引擎
- `script/think_engine.js` - JavaScript 实时交互引擎

## 输出生成规范 (Output Generation)

深度思考完成后，必须按照以下规范生成输出文档。

### 5.1 输出文档要求

完成深度分析后，系统**必须**自动生成以下两类文档：

| 文档类型 | 文件格式 | 用途 | 必须生成 |
|----------|----------|------|----------|
| **Markdown报告** | `.md` | 结构化文档，便于存档和编辑 | ✅ 必须 |
| **HTML可视化报告** | `.html` | 可视化展示，包含图表交互 | ✅ 必须 |

### 5.2 Markdown文档规范

**文件命名**：`{主题名称}深度分析报告.md`

**文档结构**：

```markdown
# {主题名称}深度分析报告

**分析时间**：{YYYY年MM月DD日 HH:mm}
**分析工具**：深度思考工作流 (deep-thinking-workflow)

---

## 一、核心信息整理
### 1.1 {主题}是什么
### 1.2 关键数据/事实
### 1.3 {相关标签或分类}

## 二、反身性觉察
### 2.1 立场澄清
### 2.2 潜在偏见识别

## 三、批判性思维分析
### 3.1 事实与观点剥离
### 3.2 逻辑谬误检查
### 3.3 核心假设检验

## 四、系统性思维分析
### 4.1 系统边界界定
### 4.2 因果回路分析
### 4.3 多维归因矩阵
### 4.4 二阶/三阶传导分析
### 4.5 尺度拉伸分析

## 五、本质洞察（第一性原则）
### 5.1 5Why深度追问
### 5.2 第一性原理

## 六、多视角深度分析
### 6.1 心理学视角
### 6.2 传播学视角
### 6.3 社会学视角
### 6.4 产品经理视角
### 6.5 经济学视角
### 6.6 政治学视角
### 6.7 设计学视角（可选）

## 七、深度结论
### 7.1 核心公式/规律
### 7.2 关键洞察列表

## 八、思考路径总结

## 九、置信度评估

## 十、生命周期预测（如适用）

## 附录：相关标签/参考资料
```

### 5.3 HTML可视化报告规范

**文件命名**：`{主题名称}_analysis_report.html`

**必须包含的可视化组件**：

| 组件 | 类型 | 说明 |
|------|------|------|
| 核心公式展示 | 特色卡片 | 爆火公式/核心洞察可视化 |
| 多维归因图 | 饼图/环形图 | ECharts |
| 传导效应图 | 堆叠柱状图 | 展示多阶效应 |
| 因果回路图 | 桑基图 | 要素关系可视化 |
| 生命周期预测 | 折线图 | 热度/影响曲线 |
| 多视角雷达图 | 雷达图 | 各视角探索深度对比 |
| 置信度仪表 | 进度条 | 各层级置信度展示 |

**技术要求**：

- 使用 ECharts 5.x 进行图表渲染
- 响应式设计，支持移动端查看
- 深色/浅色主题自适应
- 所有图表必须正确渲染，禁止空图表

### 5.4 输出流程

```
深度分析完成
    ↓
生成Markdown文档 ──→ 保存到工作目录
    ↓
读取Markdown内容 ──→ 提取关键数据
    ↓
渲染HTML可视化报告 ──→ 保存到工作目录
    ↓
展示HTML报告预览
```

### 5.5 输出配置 (config.json)

```json
{
  "output_config": {
    "auto_generate": true,
    "markdown_template": "default",
    "html_template": "assets/thinking_output.html",
    "file_naming": {
      "prefix": "{topic}_analysis",
      "timestamp": true,
      "format": "YYYY-MM-DD"
    },
    "required_sections": {
      "reflexivity": true,
      "critical_thinking": true,
      "systemic_thinking": true,
      "first_principles": true,
      "multi_perspective": true,
      "confidence_assessment": true
    },
    "visualizations": {
      "attribution_chart": true,
      "cascade_effect_chart": true,
      "system_flow_chart": true,
      "lifecycle_chart": true,
      "perspective_radar": true,
      "confidence_meters": true
    }
  }
}
```

---

## 输出示例

执行深度思考后，输出包含：
1. **Markdown文档** - 完整的结构化分析报告
2. **HTML可视化报告** - 包含图表交互的网页展示
3. **思考路径图** (SVG 可视化)
4. **关键洞察列表** (带置信度)
5. **待验证假设** (需要更多信息)
6. **行动建议** (可执行的下一步)

---

*本工作流的设计参考了 Anthropic Claude Skill 规范、Fermi 估算框架以及金字塔原理。*
