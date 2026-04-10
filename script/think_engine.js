/**
 * think_engine.js - 深度思考实时交互引擎
 * 提供浏览器端实时思考辅助，支持思考节点构建、路径可视化、置信度追踪
 *
 * Usage:
 *   const engine = new DeepThinkEngine();
 *   engine.analyze("问题描述").then(result => render(result));
 */

class ThinkingNode {
    constructor(id, type, content, confidence = 0.5) {
        this.id = id;
        this.type = type; // 'root' | 'question' | 'assumption' | 'evidence' | 'conclusion' | 'insight'
        this.content = content;
        this.confidence = confidence;
        this.children = [];
        this.metadata = {};
        this.timestamp = Date.now();
    }

    addChild(node) {
        this.children.push(node);
        node.parent = this;
    }

    toJSON() {
        return {
            id: this.id,
            type: this.type,
            content: this.content,
            confidence: this.confidence,
            children: this.children.map(c => c.id),
            metadata: this.metadata,
            timestamp: this.timestamp
        };
    }
}

class DeepThinkEngine {
    constructor(config = {}) {
        this.config = {
            maxDepth: config.maxDepth || 5,
            minConfidence: config.minConfidence || 0.3,
            autoSave: config.autoSave || true,
            ...config
        };
        this.nodes = new Map();
        this.root = null;
        this.currentNode = null;
        this.thinkingHistory = [];
    }

    /**
     * 创建思考根节点
     */
    createRoot(content) {
        const id = this.generateId('root');
        this.root = new ThinkingNode(id, 'root', content, 1.0);
        this.nodes.set(id, this.root);
        this.currentNode = this.root;
        return this.root;
    }

    /**
     * 添加思考节点
     */
    addNode(type, content, confidence = 0.5, metadata = {}) {
        if (!this.root) {
            throw new Error('请先创建根节点: createRoot()');
        }

        const id = this.generateId(type);
        const node = new ThinkingNode(id, type, content, confidence);
        node.metadata = metadata;

        this.currentNode.addChild(node);
        this.nodes.set(id, node);

        this.thinkingHistory.push({
            action: 'add',
            parentId: this.currentNode.id,
            nodeId: id,
            timestamp: Date.now()
        });

        this.currentNode = node;
        return node;
    }

    /**
     * 添加问题节点（Why追问）
     */
    why(content, confidence = 0.5) {
        return this.addNode('question', content, confidence, { technique: 'why' });
    }

    /**
     * 添加假设节点
     */
    assume(content, confidence = 0.5) {
        return this.addNode('assumption', content, confidence, { technique: 'assumption' });
    }

    /**
     * 添加证据节点
     */
    evidence(content, confidence = 0.5) {
        return this.addNode('evidence', content, confidence, { technique: 'evidence' });
    }

    /**
     * 添加洞察节点
     */
    insight(content, confidence = 0.8) {
        return this.addNode('insight', content, confidence, { technique: 'insight' });
    }

    /**
     * 添加结论节点
     */
    conclude(content, confidence = 0.7) {
        return this.addNode('conclusion', content, confidence, { technique: 'conclusion' });
    }

    /**
     * 回退到父节点
     */
    goBack() {
        if (this.currentNode.parent) {
            this.currentNode = this.currentNode.parent;
            return true;
        }
        return false;
    }

    /**
     * 生成唯一ID
     */
    generateId(type) {
        return `${type}_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }

    /**
     * 计算路径置信度
     */
    calculatePathConfidence(node = this.root) {
        if (!node) return 0;
        if (node.children.length === 0) return node.confidence;

        const childConfidences = node.children.map(c => this.calculatePathConfidence(c));
        const avgConfidence = childConfidences.reduce((a, b) => a + b, 0) / childConfidences.length;

        return (node.confidence + avgConfidence) / 2;
    }

    /**
     * 获取思考树结构（用于可视化）
     */
    getTree() {
        if (!this.root) return null;

        const traverse = (node) => {
            return {
                ...node.toJSON(),
                children: node.children.map(traverse)
            };
        };

        return traverse(this.root);
    }

    /**
     * 导出为指定格式
     */
    export(format = 'json') {
        const tree = this.getTree();

        if (format === 'json') {
            return JSON.stringify({
                tree,
                statistics: this.getStatistics(),
                history: this.thinkingHistory
            }, null, 2);
        }

        if (format === 'markdown') {
            return this.toMarkdown(tree);
        }

        return tree;
    }

    /**
     * 转为 Markdown 格式
     */
    toMarkdown(node, level = 1) {
        if (!node) return '';

        const prefix = '#'.repeat(Math.min(level, 6));
        const confidenceBar = this.renderConfidenceBar(node.confidence);

        let md = `${prefix} ${node.content}\n\n`;
        md += `> 置信度: ${confidenceBar} ${(node.confidence * 100).toFixed(0)}%\n\n`;

        if (node.metadata?.technique) {
            md += `*类型: ${node.metadata.technique}*\n\n`;
        }

        node.children.forEach(child => {
            md += this.toMarkdown(child, level + 1);
        });

        return md;
    }

    /**
     * 渲染置信度条
     */
    renderConfidenceBar(value) {
        const filled = Math.round(value * 10);
        const empty = 10 - filled;
        return '█'.repeat(filled) + '░'.repeat(empty);
    }

    /**
     * 获取统计信息
     */
    getStatistics() {
        let nodeCount = 0;
        let typeCount = {};

        const traverse = (node) => {
            nodeCount++;
            typeCount[node.type] = (typeCount[node.type] || 0) + 1;
            node.children.forEach(traverse);
        };

        if (this.root) {
            traverse(this.root);
        }

        return {
            totalNodes: nodeCount,
            typeDistribution: typeCount,
            overallConfidence: this.calculatePathConfidence(),
            maxDepth: this.getMaxDepth(),
            thinkingDuration: this.thinkingHistory.length > 0
                ? Date.now() - this.thinkingHistory[0].timestamp
                : 0
        };
    }

    /**
     * 获取最大深度
     */
    getMaxDepth(node = this.root, currentDepth = 0) {
        if (!node || node.children.length === 0) {
            return currentDepth;
        }
        return Math.max(...node.children.map(c => this.getMaxDepth(c, currentDepth + 1)));
    }

    /**
     * 分析论证（批判性思维）
     */
    analyzeArgument(text) {
        this.createRoot(text);

        // 提取结论
        const conclusionMatch = text.match(/(因此?|所以?|结论|总之)[：:,]?\s*(.+?)[。.]/);
        if (conclusionMatch) {
            this.assume(`结论: ${conclusionMatch[2]}`, 0.8);
            this.goBack();
        }

        // 提取证据
        const evidencePattern = /(因为|由于|根据|数据显示)[：:,]?\s*(.+?)[。,]/g;
        let match;
        while ((match = evidencePattern.exec(text)) !== null) {
            this.evidence(match[2], 0.7);
            this.goBack();
        }

        // 检测谬误关键词
        const fallacyKeywords = {
            '稻草人': /所以你认为/,
            '诉诸权威': /(专家|权威)说/,
            '虚假两难': /不是.*就是/,
            '滑坡': /如果.*就会.*就会/
        };

        for (const [fallacy, pattern] of Object.entries(fallacyKeywords)) {
            if (pattern.test(text)) {
                this.insight(`⚠️ 检测到潜在${fallacy}`, 0.6);
                this.goBack();
            }
        }

        // 添加总结洞察
        this.insight('论证结构分析完成', this.calculatePathConfidence());

        return {
            result: this.export('json'),
            markdown: this.export('markdown'),
            statistics: this.getStatistics()
        };
    }

    /**
     * 渐进式思考引导
     */
    guideThinking(problem) {
        const steps = [
            {
                step: 1,
                question: '这个问题本质上是什么？',
                hint: '尝试用一句话重新描述问题',
                technique: 'reframe'
            },
            {
                step: 2,
                question: '为什么这个问题重要？',
                hint: '思考对谁重要，为什么',
                technique: 'why'
            },
            {
                step: 3,
                question: '有哪些假设前提？',
                hint: '什么条件必须成立结论才有效',
                technique: 'assumption'
            },
            {
                step: 4,
                question: '反例存在吗？',
                hint: '什么情况下这个结论会不成立',
                technique: 'counterexample'
            },
            {
                step: 5,
                question: '更本质的原因是什么？',
                hint: '继续追问Why，至少3层',
                technique: 'deep_why'
            }
        ];

        return {
            problem,
            steps,
            start: () => {
                this.createRoot(problem);
                return steps[0];
            },
            next: (currentStep, answer) => {
                const nodeMap = {
                    'reframe': 'assumption',
                    'why': 'assumption',
                    'assumption': 'evidence',
                    'counterexample': 'insight',
                    'deep_why': 'insight'
                };

                const nodeType = nodeMap[steps[currentStep - 1]?.technique] || 'question';
                this.addNode(nodeType, answer);

                const nextStep = steps[currentStep];
                return nextStep || { done: true };
            }
        };
    }
}

// 导出
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { DeepThinkEngine, ThinkingNode };
}

// 浏览器环境
if (typeof window !== 'undefined') {
    window.DeepThinkEngine = DeepThinkEngine;
    window.ThinkingNode = ThinkingNode;
}
