# 产物模板

只复制当前阶段需要的模板。允许按项目知识库契约调整字段名，但不得删除核心门禁、来源、状态和版本信息。Prompt 与 Eval 各自独立成件，不要求配对。

## 1. 任务目标与范围确认

```markdown
# Prompt/Eval 生产任务
- 原始请求：
- 任务流程：Prompt Inspection / Prompt Creation / Prompt Revision / Eval Creation
- Prompt Creation 清单来源：人员给定 / 目标驱动发现 / 不适用
- prompt 生产时是否已有清单：是 / 否 / 不适用
- 检验范围：单 prompt / 局部组合 / 整套系统 / 不适用
- 是否授权修改已有产物：是 / 否
- 目标系统或执行范围：
- 期望业务结果：
- 不可改变要求：
- 本次交付（最小交付 + 按需追加）：
- 明确不包含：
- 已有 prompt 清单（如有）：
- Skill 建议（与原始要求分开）：
- 确认人/时间/证据：
```

## 2. Inspection 报告

```markdown
# Prompt System Inspection Report
- 报告文件/任务标识：
- 检验范围：单 prompt / 局部组合 / 整套系统
- 被检版本与产物路径：
- 权威知识、运行时事实与派生导航材料：
- 只报告、不修改：是
- 证据边界与未验证范围：

## 应有 prompt 体系
- 执行单元与关键时机：
- 应有 prompt 清单、职责与加载关系：

## 应有与现有清单对比
| 项目 | 分类 | 证据 | 影响 |
| --- | --- | --- | --- |

## 七项核心门禁
| 门禁 | 状态 | 证据 | 发现 |
| --- | --- | --- | --- |

## 静态集成检查

## 分级发现与归因
| 严重度 | 现象 | 原因归属 | 证据 | 置信度 | 影响范围 | 建议动作 | 回退阶段 |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 体系错误后的单元审查
- 上游错误派生问题：
- 单元自身问题：
- 重构后需复验：

## 知识缺口与补全任务

## 当前状态与允许声称的结论
- inspection-incomplete / inspection-blocked / inspection-failed / inspection-static-passed / awaiting-external-evaluation / external-failed / external-passed

## 后续入口
- 补知识 / 启动 Prompt Revision / 另启 Eval Creation / 核查运行时 / 外部评测
```

## 3. 知识覆盖表

```markdown
## 检索范围与停止理由
- 已读取范围（话题/资料/导航）：
- 分层处理（必须读 / 只需知存在 / 明确无关 / 待定）：
- 停止理由（覆盖维度齐全 / 无关键缺口 / 跨话题依赖已追踪 / 增量下降）：
- 可能遗漏与判定依据：
- 识别到的文件字段/命名/目录依据：
```

| 执行单元/候选 prompt | 信息维度 | 结论 | 来源与版本 | 适用范围 | 关键性 | 状态/缺口 |
| --- | --- | --- | --- | --- | --- | --- |
|  | 目标与需求 |  |  |  |  |  |
|  | 业务与角色 |  |  |  |  |  |
|  | 运行环境 |  |  |  |  |  |
|  | 时机上下文与概念绑定 |  |  |  |  |  |
|  | 职责、注意力与评测 |  |  |  |  |  |

## 4. 关键知识补全请求

```markdown
# 知识补全请求
- 关联任务与当前阶段：
- 已知事实及来源：
- 缺失/冲突问题：
- 为什么关键：
- 影响的 prompts/evals：
- 需要返回的事实、schema、代码证据或业务决策：
- 建议回答方：项目人员 / 后端 Agent / 前端 Agent / 其他
- 回写知识库要求：来源、版本、适用范围、建议位置
- 回写后重跑门禁：
- 主线回归点：阶段 3 知识发现与覆盖
```

需要交给不同责任方时，每项请求单独保存为 Markdown 文件，不只放在报告附录。

## 5. 运行时工程取证请求

```markdown
# Runtime Evidence Request
- 关联任务与受影响 prompts：
- 当前已知设计及知识来源：
- 无法确认的运行时供给：消息 / 变量 / 状态 / 历史 / 工具 / 输出 / 钩子 / 异常 / 版本
- 为什么阻塞可接入或静态结论：
- 需要返回：文件路径、关键符号、schema、装配/注入/聚合代码、测试和版本证据
- 建议回答方：后端 Agent / 前端 Agent / 运行平台负责人
- 证据建议保存位置：
- 回填后重跑的门禁与静态检查：
```

## 6. 七项核心门禁摘要

| 门禁 | 生产前信息来源 | 显式产物路径 | 对正式文件的约束 | 状态 | 失败/警告/阻塞 | 回退阶段 |
| --- | --- | --- | --- | --- | --- | --- |
| requirements-scope |  |  |  | pass/warning/blocked/fail |  |  |
| runtime-environment |  |  |  | pass/warning/blocked/fail |  |  |
| execution-context |  |  |  | pass/warning/blocked/fail |  |  |
| business-role |  |  |  | pass/warning/blocked/fail |  |  |
| responsibility-visibility |  |  |  | pass/warning/blocked/fail |  |  |
| attention-plan |  |  |  | pass/warning/blocked/fail |  |  |
| knowledge-conflicts |  |  |  | pass/warning/blocked/fail |  |  |

七项详细产物分别使用下列字段。

### 需求先行与范围推导

```markdown
- 原始要求与目标：
- 系统范围与不可改变要求：
- 交付范围与明确排除：
- prompt 清单来源（人员给定 / 目标驱动）：
- 原始清单（若有，原样保留）：
```

### Agent 运行环境说明

```markdown
- 执行单元与触发条件：
- 可见消息角色与装配顺序：
- 动态变量、状态、历史与知识：
- 工具、schema、调用条件与消费者：
- 输出、parser 与下游：
- reminder/anchor 钩子：
- 异常路径：
- 版本对应：
- 来源：
```

### 执行时机上下文契约

| 时机/节点 | 完整消息顺序 | 动态上下文 | 工具 | 上游输入 | 缺失/异常行为 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |

### 概念引用绑定表

| prompt 中的概念/指代 | 明确定义 | 注入来源 | 可见时机 | 缺失行为 | 验证方式 |
| --- | --- | --- | --- | --- | --- |

### 业务与角色行为契约

```markdown
- 业务目标与服务对象：
- Agent 身份和业务结果：
- 明确不做：
- 目标优先级：
- 行为与安全边界：
- 语气和沟通要求：
- 术语定义：
- 信息不足/拒绝/冲突/越界/异常行为：
- 来源与限定：
```

### prompt 职责与信息可见性矩阵

| 载体 | 唯一主要职责 | 必须知道 | 可以知道 | 不应知道 | 上游 | 下游 | 来源 |
| --- | --- | --- | --- | --- | --- | --- | --- |

### 关键约束与注意力安排

| 约束 | 影响 | 执行单元 | 主要归属 | 易失效时机/原因 | 注意力手段 | 注入方/时机 | 重复理由 |
| --- | --- | --- | --- | --- | --- | --- | --- |

### 知识疑点与冲突报告

| 疑点 | 来源 | 可疑原因 | 影响范围 | 关键阻塞 | 建议补充方 | 回退阶段 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |

未发现时写：`已检查，未发现影响本次任务的明显知识问题。`

## 7. prompt 候选清单与架构

| ID | 类型 | 执行单元 | 加载时机 | 唯一职责 | 不承载内容 | 独立理由 | 所需知识/工具 | 文件字段/命名依据 | 来源 | 置信度/待确认 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

同时保存原始清单和 Skill 建议清单，避免建议覆盖需求。

## 8. prompt 单元规格

```markdown
# Prompt Unit: <id>
- 类型与执行单元：
- 唯一职责：
- 加载时机与 message role：
- 文件字段/命名依据：
- 输入和上下文契约：
- 工具契约：
- 输出契约：
- 规则骨架：
- 逐字 prompt：
- 不承载内容：
- 动态占位符及登记位置：
- 来源映射：
- 版本：
- 单元校验状态：
```

## 9. eval 场景规格

Eval 被测对象为完整 Agent 业务行为，独立从知识库推导，不以 prompt 为知识源。

```markdown
# Eval Scenario: <id>
- 被测 Agent 业务行为/系统能力：
- 评测目标：
- 跨越的执行单元/prompt/状态/工具/门禁/异常/回复流程：
- 失败面：
- 测试输入与前置状态：
- 可验证项及黄金结果：
- judge rubric 与评分锚点：
- 一票否决项：
- 工具/运行时证据要求：
- 通过阈值：
- 知识来源（独立于 prompt，评测目标 → 知识来源）：
- 外部执行环境：
- 当前状态：未执行 / 已执行
- 结果证据路径：
```

## 10. 运行时集成契约

| Prompt ID | 执行单元/触发 | role/顺序 | 动态变量、状态、历史 | 工具/schema | 输出/parser | anchor 钩子 | 异常路径 | prompt/schema/code 版本 | 来源 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 11. 外部评测交接包

仅在 Eval Creation 完成、eval 准备执行时生成。

```markdown
# External Evaluation Handoff
- 系统、范围与版本：
- prompts/evals/schema/契约路径：
- 模型、参数、工具和环境：
- 测试集与用例 ID：
- 前置状态和执行顺序：
- 可验证项、judge rubric、否决项和阈值：
- 必须保存的输出、工具调用、错误和版本证据：
- 结果回传格式、位置和负责人：
- 当前状态：awaiting-external-evaluation
```

## 12. 检查点与分支记录

```markdown
# Task Checkpoint
- 原始任务标识与任务流程：
- 任务流程：prompt-inspection / prompt-creation / prompt-revision / eval-creation
- 当前主线阶段/状态：
- 本阶段输入：
- 已确认判断：
- 已保存产物路径/版本：
- 未决事项：
- 当前分支与负责人：
- 下一步：
- 主线回归点：
```

## 13. 最终交付清单

```markdown
Prompt 侧
- [ ] prompts 完整，文件清单与知识库定义一一对应（无少文件/合并/多造/错目录/自行命名）
- [ ] prompt 来源映射完整
- [ ] 七项核心门禁产物完整且无关键失败
- [ ] prompt 清单、职责、加载关系完整
- [ ] 运行时集成契约完整
- [ ] 静态校验报告完整
- [ ] 运行时证据缺口按 warning/阻断分级诚实标注

Eval 侧（由独立 Eval Creation 产生）
- [ ] evals 完整，被测对象为完整 Agent 业务行为
- [ ] eval 来源映射完整（独立于 prompt）
- [ ] 场景按失败面覆盖

整体
- [ ] 外部评测证据状态真实
- [ ] 非阻塞事项和回退位置已记录
- [ ] 人工确认点有证据
- 最终状态：
```

## 14. 机器校验清单 `prompt-package.json`

把路径写成相对于该 JSON 所在目录的路径。来源在外部知识库时，使用相对于 `--knowledge-root` 的路径。Prompt 与 Eval 独立注册，不要求配对、数量相等或版本匹配。

```json
{
  "package_version": "2",
  "delivery_status": "prompt-static-passed",
  "artifacts": {
    "requirements_scope": "artifacts/requirements-scope.md",
    "runtime_environment": "artifacts/runtime-environment.md",
    "execution_context": "artifacts/execution-context.md",
    "business_role": "artifacts/business-role.md",
    "responsibility_visibility": "artifacts/responsibility-visibility.md",
    "attention_plan": "artifacts/attention-plan.md",
    "knowledge_conflicts": "artifacts/knowledge-conflicts.md",
    "runtime_contract": "artifacts/runtime-contract.md",
    "source_mapping": "artifacts/source-mapping.md"
  },
  "runtime": {
    "variables": ["event_summary"],
    "tools": ["example_tool"]
  },
  "prompt_units": [
    {
      "id": "example-task",
      "prompt": "prompts/example-task.md",
      "file_field": "gate/example",
      "version": "1.0.0",
      "tools": ["example_tool"],
      "sources": ["topics/example/source.md"]
    }
  ],
  "eval_scenarios": [
    {
      "id": "example-scenario",
      "eval": "evals/example-scenario.md",
      "scope": "完整 Agent 业务行为",
      "version": "1.0.0",
      "sources": ["topics/example/source.md"]
    }
  ]
}
```

## 15. Prompt Creation 最小交付：`prompt-production-basis.md`

Prompt Creation 的核心过程产物，合并目标范围、正式文件清单、职责、命名依据、来源映射、运行时契约、概念绑定、知识冲突和用户裁定，避免重复落盘。

```markdown
# Prompt Production Basis
- 目标与范围（含不可改变要求、明确排除）：
- prompt 清单来源（人员给定 / 目标驱动）与原始清单：
- 正式 prompt 文件清单（文件字段 / 命名依据 / 独立理由 / 是否合并及依据）：
- 职责与信息可见性矩阵：
- 运行时集成契约：
- 概念引用绑定表：
- 关键约束与注意力安排：
- 七项门禁约束（每项对正式文件的具体约束）：
- 知识冲突与用户裁定（含待回写项）：
- 来源映射：
- 检索范围与停止理由（引自知识覆盖）：
```

## 16. Prompt Creation 最小交付：`prompt-static-check.md`

```markdown
# Prompt Static Check
- 确定性检查（文件/字段/占位符/工具名/schema/结构/数量）：
- 静态集成检查（跨层冲突/变量/工具/上下游/异常/并行共享）：
- 预期文件清单 ↔ 实际文件核对（少文件/合并文件/多造文件/错目录/自行命名）：
- 运行时证据缺口（warning / 阻断分级）：
- 七项门禁交付前倒查：
- 状态与未决事项：
```

## 17. Eval Creation 最小交付：`eval-production-basis.md`

```markdown
# Eval Production Basis
- 评测目标与被测 Agent 业务行为范围：
- eval 场景清单（按业务场景与失败面拆分，数量不等于 prompt 数）：
- 知识来源（独立于 prompt；评测目标 → 知识来源）：
- rubric/judge 架构与一票否决：
- 与 prompt 的理解差异/冲突标记（若有）：
- 来源映射：
```
