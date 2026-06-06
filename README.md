# 🔄 AI State Machine

AI状态机工具，支持状态机设计、状态管理、转换规则。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 状态机设计
- 💻 状态机代码生成
- 🔄 工作流状态机
- ⚛️ XState配置生成
- 📊 状态行为分析
- 📊 状态图生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_state_machine import create_tools

tools = create_tools()

# 状态机设计
sm = tools.design_state_machine("订单", ["待支付", "已支付", "已发货", "已完成"])

# 状态机代码
code = tools.generate_state_machine_code("订单", states, "python")

# 工作流状态机
workflow_sm = tools.design_workflow_state_machine("订单处理")

# XState配置
xstate = tools.generate_xstate_config("订单", states)

# 状态行为分析
analysis = tools.analyze_state_behavior(state_machine, scenarios)

# 状态图
diagram = tools.generate_state_diagram("订单", states)
```

## 📁 项目结构

```
ai-state-machine/
├── tools.py       # 状态机工具核心
└── README.md
```

## 📄 许可证

MIT License
