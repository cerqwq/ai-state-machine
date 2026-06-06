"""
AI State Machine - AI状态机工具
支持状态机设计、状态管理、转换规则
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIStateMachineTools:
    """
    AI状态机工具
    支持：设计、管理、转换
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_state_machine(self, entity: str, states: List[str]) -> Dict:
        """设计状态机"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        states_text = ", ".join(states)

        prompt = f"""请为{entity}设计状态机：

状态：{states_text}

请返回JSON格式：
{{
    "states": [
        {{"name": "状态名", "description": "描述", "actions": ["动作"]}}
    ],
    "transitions": [
        {{"from": "源状态", "to": "目标状态", "event": "事件", "condition": "条件"}}
    ],
    "initial_state": "初始状态",
    "final_states": ["最终状态"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"state_machine": content}

    def generate_state_machine_code(self, entity: str, states: Dict, framework: str = "python") -> str:
        """生成状态机代码"""
        if not self.client:
            return "LLM客户端未配置"

        states_text = json.dumps(states, ensure_ascii=False)

        prompt = f"""请为{entity}生成状态机代码：

状态定义：{states_text}
框架：{framework}

要求：
1. 完整的状态机类
2. 状态转换
3. 事件处理
4. 回调函数"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def design_workflow_state_machine(self, workflow: str) -> Dict:
        """设计工作流状态机"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{workflow}设计工作流状态机：

请返回JSON格式：
{{
    "phases": [
        {{"name": "阶段", "states": ["状态"], "transitions": ["转换"]}}
    ],
    "parallel_states": ["并行状态"],
    "error_states": ["错误状态"],
    "recovery": "恢复策略"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"workflow_sm": content}

    def generate_xstate_config(self, entity: str, states: Dict) -> str:
        """生成XState配置"""
        if not self.client:
            return "LLM客户端未配置"

        states_text = json.dumps(states, ensure_ascii=False)

        prompt = f"""请为{entity}生成XState配置：

状态：{states_text}

要求：
1. 完整的XState机器定义
2. 状态转换
3. 动作
4. 守卫"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def analyze_state_behavior(self, state_machine: Dict, scenarios: List[str]) -> Dict:
        """分析状态行为"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        sm_text = json.dumps(state_machine, ensure_ascii=False)
        scenarios_text = ", ".join(scenarios)

        prompt = f"""请分析状态机行为：

状态机：{sm_text}
场景：{scenarios_text}

请返回JSON格式：
{{
    "coverage": "覆盖率",
    "deadlocks": ["死锁"],
    "unreachable": ["不可达状态"],
    "recommendations": ["建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def generate_state_diagram(self, entity: str, states: Dict) -> str:
        """生成状态图"""
        if not self.client:
            return "LLM客户端未配置"

        states_text = json.dumps(states, ensure_ascii=False)

        prompt = f"""请为{entity}生成Mermaid状态图：

状态：{states_text}

请返回Mermaid格式的状态图代码："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AIStateMachineTools:
    """创建状态机工具"""
    return AIStateMachineTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI State Machine Tools")
    print()

    # 测试
    sm = tools.design_state_machine("订单", ["待支付", "已支付", "已发货", "已完成", "已取消"])
    print(json.dumps(sm, ensure_ascii=False, indent=2))
