---
name: "multi-choice-skill"
description: "跨平台多选交互模板"
platforms:
  - workbuddy
  - claude
  - cursor
  - trae
---

## 多选交互模板

### 标准格式

#### Q1: [问题标题]
**问题**: [具体问题]

**选项**:
- **A**: [选项1描述]
- **B**: [选项2描述]
- **C**: [选项3描述]

**默认值**: [默认选择]

---

### 使用说明

#### WorkBuddy
使用 `ask_followup_question` 工具，传入 JSON 配置。

#### Claude / Trae
在回复中直接展示多选题，用清晰的格式引导用户输入选项。

#### Cursor
通过 MCP 工具或对话交互实现。
