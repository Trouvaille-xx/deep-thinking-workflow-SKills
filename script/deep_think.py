#!/usr/bin/env python3
"""
deep_think.py - 深度思考分析引擎
深度思考工作流的核心脚本，提供思考路径分析、置信度计算、逻辑结构解析

Usage:
    python deep_think.py --input "问题描述" --level 2 --skill critical
    python deep_think.py --analyze argument.txt --output json
"""

import json
import re
import sys
import argparse
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
from enum import Enum


class SkillType(Enum):
    CRITICAL = "critical_thinking"
    SYSTEMIC = "systemic_thinking"
    CREATIVE = "creative_thinking"
    EXPRESSION = "structured_expression"


@dataclass
class ThinkingNode:
    """思考节点"""
    id: str
    type: str  # question, assumption, evidence, conclusion, fallacy
    content: str
    confidence: float = 0.5
    parent_id: Optional[str] = None
    children_ids: List[str] = None
    metadata: Dict = None

    def __post_init__(self):
        if self.children_ids is None:
            self.children_ids = []
        if self.metadata is None:
            self.metadata = {}


@dataclass
class ThinkingResult:
    """思考结果"""
    skill_used: str
    input_text: str
    reasoning_path: List[Dict]
    key_insights: List[str]
    confidence_scores: Dict[str, float]
    alternative_paths: List[str]
    next_steps: List[str]
    metadata: Dict

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2)

    def to_markdown(self) -> str:
        md = f"## {self.skill_used} 分析结果\n\n"
        md += f"**输入**: {self.input_text}\n\n"
        md += "### 思考路径\n"
        for i, step in enumerate(self.reasoning_path, 1):
            md += f"{i}. {step.get('node', '...')} (置信度: {step.get('confidence', 0):.0%})\n"
        md += "\n### 关键洞察\n"
        for insight in self.key_insights:
            md += f"- {insight}\n"
        md += "\n### 置信度评分\n"
        for k, v in self.confidence_scores.items():
            bar = "█" * int(v * 10) + "░" * (10 - int(v * 10))
            md += f"- {k}: [{bar}] {v:.0%}\n"
        return md


class DeepThinkEngine:
    """深度思考引擎"""

    # 常见逻辑谬误模式
    FALLACY_PATTERNS = {
        "strawman": (r"所以你认为", "稻草人谬误 - 攻击弱化后的观点"),
        "authority": (r"(专家|权威|大师)说", "诉诸权威 - 权威不等于正确"),
        "emotion": (r"(可怜|可怕|恐怖|激动)", "诉诸情感 - 情感不等于事实"),
        "false_dilemma": (r"不是.*就是", "虚假两难 - 只给两个极端选项"),
        "slippery_slope": (r"如果.*就会.*就会", "滑坡谬误 - 无限推演"),
        "circular": (r"因为.*所以.*因为", "循环论证 - 结论包含前提"),
        "ad_hominem": (r"(你|他|她).*(也是|也一样)", "人身攻击 - 攻击人不攻击论点"),
    }

    # 批判性思维关键词
    CRITICAL_TRIGGERS = [
        "分析", "评估", "论证", "观点", "相信", "认为",
        "应该", "必须", "证明", "证据", "逻辑"
    ]

    # 系统性思维关键词
    SYSTEMIC_TRIGGERS = [
        "系统", "因素", "原因", "影响", "关系", "反馈",
        "循环", "长期", "短期", "相互作用", "复杂"
    ]

    # 创造性思维关键词
    CREATIVE_TRIGGERS = [
        "创新", "创意", "新方案", "如何改进", "头脑风暴",
        "突破", "重新", "换个角度", "如果"
    ]

    def __init__(self, config_path: Optional[str] = None):
        self.config = self._load_config(config_path) if config_path else {}
        self.nodes: Dict[str, ThinkingNode] = {}

    def _load_config(self, path: str) -> Dict:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Failed to load config: {e}")
            return {}

    def detect_skill_type(self, text: str) -> SkillType:
        """检测适合的技能类型"""
        text_lower = text.lower()

        critical_score = sum(1 for t in self.CRITICAL_TRIGGERS if t in text_lower)
        systemic_score = sum(1 for t in self.SYSTEMIC_TRIGGERS if t in text_lower)
        creative_score = sum(1 for t in self.CREATIVE_TRIGGERS if t in text_lower)

        scores = {
            SkillType.CRITICAL: critical_score,
            SkillType.SYSTEMIC: systemic_score,
            SkillType.CREATIVE: creative_score,
            SkillType.EXPRESSION: 1  # 始终可以考虑
        }

        return max(scores, key=scores.get)

    def analyze_argument(self, text: str) -> ThinkingResult:
        """分析论证结构"""
        nodes = []
        insights = []

        # 提取结论
        conclusion_match = re.search(r"(因此?|所以?|结论|总之)[：:,]?\s*(.+?)[。.]", text)
        conclusion = conclusion_match.group(2) if conclusion_match else "未明确"

        # 提取证据
        evidence_pattern = r"(因为|由于|根据|数据显示|研究表明)[：:,]?\s*(.+?)[。,]"
        evidence_list = re.findall(evidence_pattern, text)

        # 检测谬误
        fallacies = []
        for name, (pattern, desc) in self.FALLACY_PATTERNS.items():
            if re.search(pattern, text):
                fallacies.append({"type": name, "description": desc})

        # 计算置信度
        confidence = 0.5
        if len(evidence_list) >= 2:
            confidence += 0.2
        if len(fallacies) == 0:
            confidence += 0.2
        if conclusion_match:
            confidence += 0.1
        confidence = min(confidence, 0.95)

        # 构建推理路径
        reasoning_path = [
            {"node": "识别结论", "content": conclusion, "confidence": 0.9},
            {"node": "提取证据", "content": f"找到{len(evidence_list)}条证据", "confidence": 0.8},
            {"node": "检测谬误", "content": f"发现{len(fallacies)}个潜在谬误", "confidence": 0.7 if fallacies else 0.9},
        ]

        # 生成洞察
        insights.append(f"论证的核心结论是：{conclusion}")
        if evidence_list:
            insights.append(f"提供了{len(evidence_list)}条支持证据")
        if fallacies:
            insights.append(f"需要注意的逻辑问题：{'、'.join([f['description'] for f in fallacies])}")
        else:
            insights.append("未发现明显逻辑谬误")

        return ThinkingResult(
            skill_used="critical_thinking",
            input_text=text,
            reasoning_path=reasoning_path,
            key_insights=insights,
            confidence_scores={
                "论证强度": confidence,
                "证据质量": len(evidence_list) / 5 if evidence_list else 0.3,
                "逻辑性": 1 - len(fallacies) * 0.2
            },
            alternative_paths=["考虑反例", "验证数据来源", "寻找替代解释"],
            next_steps=["收集更多证据", "检验假设前提", "考虑反对意见"],
            metadata={"fallacies": fallacies, "evidence_count": len(evidence_list)}
        )

    def analyze_system(self, text: str) -> ThinkingResult:
        """系统性分析"""
        insights = []

        # 识别要素（名词短语）
        elements = re.findall(r"[\w\u4e00-\u9fff]{2,}(?=因素|要素|组成|部分|模块|系统)", text)

        # 识别关系
        relations = re.findall(r"(\w+)(导致|影响|促进|制约|依赖)(\w+)", text)

        # 构建简单因果链
        if relations:
            insights.append(f"识别到{len(relations)}个因果关系")
            for rel in relations[:3]:
                insights.append(f"{rel[0]}{rel[1]}{rel[2]}")
        else:
            insights.append("需要更多信息来识别因果关系")

        reasoning_path = [
            {"node": "边界识别", "content": "定义分析范围", "confidence": 0.8},
            {"node": "要素提取", "content": f"发现{len(elements)}个关键要素", "confidence": 0.7},
            {"node": "关系映射", "content": f"识别{len(relations)}条连接", "confidence": 0.6},
        ]

        return ThinkingResult(
            skill_used="systemic_thinking",
            input_text=text,
            reasoning_path=reasoning_path,
            key_insights=insights,
            confidence_scores={
                "系统清晰度": len(elements) / 10,
                "关系完整性": len(relations) / 5,
                "分析深度": 0.6
            },
            alternative_paths=["深入某个要素", "追踪完整反馈回路", "识别延迟效应"],
            next_steps=["画出因果回路图", "识别增强/平衡回路", "找到杠杆点"],
            metadata={"elements": elements, "relations": relations}
        )

    def generate_ideas(self, problem: str) -> ThinkingResult:
        """激发创意"""
        ideas = []

        # SCAMPER 启发
        scarecrow = {
            "substitute": f"将{problem}中的某个要素替换会怎样？",
            "combine": f"能否将{problem}与其他领域组合？",
            "adapt": f"类似问题在其他场景怎么解决的？",
            "modify": f"放大或缩小{problem}的某个方面？",
            "put_other": f"{problem}的核心本质可以用于什么新场景？",
            "eliminate": f"如果去掉{problem}的某个部分呢？",
            "reverse": f"反过来看{problem}会是什么？"
        }

        for tech, prompt in scarecrow.items():
            ideas.append({"technique": tech, "prompt": prompt, "novelty": 7})

        reasoning_path = [
            {"node": "问题重定义", "content": problem, "confidence": 0.9},
            {"node": "SCAMPER发散", "content": "7个技术方向", "confidence": 0.8},
            {"node": "评估收敛", "content": f"初步产生{len(ideas)}个想法", "confidence": 0.7},
        ]

        return ThinkingResult(
            skill_used="creative_thinking",
            input_text=problem,
            reasoning_path=reasoning_path,
            key_insights=[f"使用{len(scarecrow)}种创意技术产生了初步想法"],
            confidence_scores={
                "创新性": 0.7,
                "可行性": 0.6,
                "相关性": 0.8
            },
            alternative_paths=["类比启发", "随机词连接", "极端假设"],
            next_steps=["选择一个方向深化", "寻找支持案例", "小规模测试"],
            metadata={"ideas": ideas, "techniques_used": list(scarecrow.keys())}
        )

    def run(self, text: str, skill: Optional[str] = None, level: int = 1) -> ThinkingResult:
        """运行分析"""
        # 自动检测技能类型
        if not skill:
            skill_type = self.detect_skill_type(text)
        else:
            skill_type = SkillType(skill)

        if skill_type == SkillType.CRITICAL:
            return self.analyze_argument(text)
        elif skill_type == SkillType.SYSTEMIC:
            return self.analyze_system(text)
        elif skill_type == SkillType.CREATIVE:
            return self.generate_ideas(text)
        else:
            return self.analyze_argument(text)


def main():
    parser = argparse.ArgumentParser(description="深度思考分析引擎")
    parser.add_argument("--input", "-i", help="输入文本")
    parser.add_argument("--file", "-f", help="输入文件路径")
    parser.add_argument("--skill", "-s", choices=["critical", "systemic", "creative", "expression"])
    parser.add_argument("--level", "-l", type=int, default=1, help="分析深度等级")
    parser.add_argument("--output", "-o", choices=["json", "markdown"], default="json")
    parser.add_argument("--config", "-c", help="配置文件路径")

    args = parser.parse_args()

    # 获取输入
    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
    elif args.input:
        text = args.input
    else:
        print("Error: 请提供 --input 或 --file")
        sys.exit(1)

    # 运行分析
    engine = DeepThinkEngine(args.config)
    result = engine.run(text, args.skill, args.level)

    # 输出
    if args.output == "json":
        print(result.to_json())
    else:
        print(result.to_markdown())


if __name__ == "__main__":
    main()
