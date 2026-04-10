# 深度思考工作流 (Deep Thinking Workflow)

> 一套渐进式思考方法论，帮助用户从表面理解深入到本质洞察。

## 快速开始

### 基本用法

```
用户: 如何深度思考？
助手: 请描述你想要深入思考的问题或话题...
```

### 执行模式选择

**1️⃣ 渐进性执行（推荐）**
- 分阶段执行，在关键节点设置断点供用户介入
- 调研完成后询问是否继续/调整
- 输出前询问是否生成MD/HTML报告

**2️⃣ 一步执行**
- 一次性完成所有分析（Level 1-3 全链路）
- 分析完成后询问是否输出报告

### 层级加载

| 层级 | 触发条件 | 深度 | 耗时 |
|------|---------|------|------|
| Level 1 | 快速分析 | 5W1H框架 | ~30秒 |
| Level 2 | 深入分析 | 批判性思维/系统性思维 | ~2分钟 |
| Level 3 | 本质洞察 | 多维度交叉验证 + 第一性原则 | ~10分钟 |

## 目录结构

```
deep-thinking-workflow/
├── skill.md                          # 主技能入口
├── README.md                         # 说明文档
├── sub_skills/                       # 子技能模块
│   ├── reflexivity.md               # 反身性觉察（元技能）
│   ├── critical_thinking.md          # 批判性思维
│   ├── systemic_thinking.md         # 系统性思维
│   ├── creative_thinking.md         # 创造性思维
│   ├── structured_expression.md      # 结构化表达
│   ├── output_generation.md         # 输出生成（渐进/一步模式、MD/HTML模板）
│   └── perspectives/                 # 多视角角色分析
│       ├── perspective_psychology.md     # 心理学视角
│       ├── perspective_communication.md  # 传播学视角
│       ├── perspective_product.md        # 产品经理视角
│       ├── perspective_economics.md      # 经济学视角
│       ├── perspective_political.md       # 政治学视角
│       └── perspective_design.md          # 设计学视角
├── config/
│   └── config.json                  # 配置文件
├── script/
│   ├── deep_think.py                # Python 分析引擎
│   └── think_engine.js              # JavaScript 交互引擎
├── references/
│   └── reading-list.md              # 参考书单与资源
└── assets/
    └── thinking_output.html         # HTML 输出模板
```

## 子技能说明

### 元技能

#### 1. 反身性觉察 (Reflexivity)
识别思考者与系统的相互影响，避免认知偏见。

**适用场景**: 决策前自检、偏见识别、立场澄清
**优先级**: 最先激活

### 核心子技能

#### 2. 批判性思维 (Critical Thinking)
评估论证质量，识别逻辑谬误，检验假设前提。

**适用场景**: 分析观点可靠性、评估论证强度、识别认知偏见

**方法列表**：
- 价值澄清
- 事实/观点剥离
- 第一性原则 + 5Why追问
- 逻辑谬误识别

#### 3. 系统性思维 (Systemic Thinking)
理解要素关系，识别反馈循环，预测系统行为。

**适用场景**: 复杂问题分析、多因素决策、变革干预设计

**方法列表**：
- 多维归因矩阵
- 二阶/三阶传导分析
- 实践尺度拉伸

#### 4. 创造性思维 (Creative Thinking)
突破思维定式，产生新颖洞见，连接跨域知识。

**适用场景**: 产品创新、问题解决、方案设计

**方法**: SCAMPER

#### 5. 结构化表达 (Structured Expression)
将思考结果转化为清晰输出。

**适用场景**: 写作、演讲、汇报、文档撰写

### 输出子技能

#### 6. 输出生成 (Output Generation)
支持用户选择执行模式，在关键节点设置断点，生成Markdown和HTML可视化报告。

**执行模式**：
- **渐进性执行**（推荐）：分阶段暂停，用户可介入调整
- **一步执行**：一次性完成，结束时统一询问输出

**输出格式**：
- **Markdown报告**: 结构化文档，便于存档和编辑
- **HTML可视化报告**: 包含ECharts图表交互展示

**断点设计**：
```
🔴 断点1: 调研完成 → 询问用户是否继续/补充/调整方向
🔴 断点2: 分析完成 → 询问用户是否生成MD/HTML报告
```

### 多视角分析

#### 7. 多视角角色分析 (Perspectives)

| 视角 | 核心关注 | 关键问题 |
|------|---------|---------|
| 心理学 | 动机/认知/情感 | 用户真正想要什么？ |
| 传播学 | 信息/符号/影响 | 信息如何被接收和扭曲？ |
| 产品经理 | 需求/价值/迭代 | 做什么才有意义？ |
| 经济学 | 激励/供需/成本 | 什么驱动行为？ |
| 政治学 | 权力/利益/联盟 | 各方如何博弈？ |
| 设计学 | 体验/共情/本质 | 什么让用户心动？ |

## 配置说明

编辑 `config/config.json` 自定义：

```json
{
  "load_config": {
    "default_level": 1,
    "max_level": 3,
    "auto_escalation": true
  },
  "output_config": {
    "auto_generate": true,
    "markdown_template": "default",
    "html_template": "assets/thinking_output.html",
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

## 脚本使用

### Python 引擎

```bash
# 快速分析
python script/deep_think.py --input "你的问题"

# 批判性思维分析
python script/deep_think.py --input "你的论证" --skill critical

# 从文件分析
python script/deep_think.py --file argument.txt --output markdown
```

### JavaScript 引擎

```javascript
const { DeepThinkEngine } = require('./script/think_engine.js');

const engine = new DeepThinkEngine();
const result = engine.analyzeArgument("你的论证...");

console.log(result.markdown);
```

## 输出示例

### Markdown报告结构

```markdown
# {主题名称}深度分析报告

## 一、核心信息整理
## 二、反身性觉察
## 三、批判性思维分析
## 四、系统性思维分析
## 五、本质洞察（第一性原则）
## 六、多视角深度分析
## 七、深度结论
## 八、思考路径总结
## 九、置信度评估
## 十、生命周期预测
```

### HTML可视化组件

| 组件 | 类型 | 说明 |
|------|------|------|
| 核心公式展示 | 特色卡片 | 爆火公式/核心洞察可视化 |
| 多维归因图 | 饼图/环形图 | ECharts |
| 传导效应图 | 堆叠柱状图 | 展示多阶效应 |
| 因果回路图 | 桑基图 | 要素关系可视化 |
| 生命周期预测 | 折线图 | 热度/影响曲线 |
| 多视角雷达图 | 雷达图 | 各视角探索深度对比 |
| 置信度仪表 | 进度条 | 各层级置信度展示 |

### JSON输出结构

```json
{
  "skill": "critical_thinking",
  "conclusion": "应该辍学去创业",
  "evidence_strength": 0.4,
  "hidden_assumptions": [
    {"assumption": "成功企业家都辍学", "plausibility": 0.3}
  ],
  "fallacies_detected": [
    {"name": "稻草人", "severity": "high"}
  ],
  "confidence": 0.35
}
```

## 设计原则

1. **渐进式加载** - 按需加载子技能，避免认知过载
2. **元数据驱动** - 每个思考节点携带置信度、来源等元数据
3. **内存持久化** - 思考过程自动存储，支持跨会话恢复
4. **结构化输出** - JSON/Markdown/HTML 多格式支持
5. **用户全程介入** - 断点设计确保用户掌控分析方向

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

## 参考资料

详见 [references/reading-list.md](references/reading-list.md)

---

*版本: 1.1.0 | 作者: WorkBuddy | 基于 Claude Skill 规范设计*
