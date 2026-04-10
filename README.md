# 深度思考工作流 (Deep Thinking Workflow)

> 一套渐进式思考方法论，帮助用户从表面理解深入到本质洞察。

## 快速开始

### 基本用法

```
用户: 如何深度思考？
助手: 请描述你想要深入思考的问题或话题...
```

### 层级加载

| 层级 | 触发条件 | 深度 | 耗时 |
|------|---------|------|------|
| Level 1 | 快速分析 | 5W1H框架 | ~30秒 |
| Level 2 | 深入分析 | 批判性思维/系统性思维 | ~2分钟 |
| Level 3 | 本质洞察 | 多维度交叉验证 | ~10分钟 |

## 目录结构

```
workflow-skills/
├── skill.md                          # 主技能入口
├── README.md                         # 说明文档
├── sub_skills/                       # 子技能模块
│   ├── critical_thinking.md         # 批判性思维
│   ├── systemic_thinking.md         # 系统性思维
│   ├── creative_thinking.md         # 创造性思维
│   └── structured_expression.md     # 结构化表达
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

### 1. 批判性思维 (Critical Thinking)
评估论证质量，识别逻辑谬误，检验假设前提。

**适用场景**: 分析观点可靠性、评估论证强度、识别认知偏见

### 2. 系统性思维 (Systemic Thinking)
理解要素关系，识别反馈循环，预测系统行为。

**适用场景**: 复杂问题分析、多因素决策、变革干预设计

### 3. 创造性思维 (Creative Thinking)
突破思维定式，产生新颖洞见，连接跨域知识。

**适用场景**: 产品创新、问题解决、方案设计

### 4. 结构化表达 (Structured Expression)
将思考结果转化为清晰输出。

**适用场景**: 写作、演讲、汇报、文档撰写

## 配置说明

编辑 `config/config.json` 自定义：

```json
{
  "load_config": {
    "default_level": 1,           // 默认加载层级
    "max_level": 3,               // 最大层级
    "auto_escalation": true       // 自动升级
  },
  "sub_skills_config": {
    "critical_thinking": {
      "enabled": true,
      "weight": 0.3               // 子技能权重
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

## 参考资料

详见 [references/reading-list.md](references/reading-list.md)

---

*版本: 1.0.0 | 作者: WorkBuddy | 基于 Claude Skill 规范设计*
