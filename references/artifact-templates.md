# 产物模板

只复制当前阶段需要的模板。允许按项目知识库契约调整字段名，但不得删除核心门禁、来源、状态和版本信息。

## 1. 任务目标与范围确认

```markdown
# Prompt 生产任务
- 原始请求：
- 任务流程：Inspection / Creation / Revision / Eval-only
- Creation 清单来源：人员给定 / 目标驱动发现 / 不适用
- prompt 生产时是否已有清单：是 / 否 / 不适用
- 检验范围：单 prompt / 局部组合 / 整套系统 / 不适用
- 是否授权修改已有产物：是 / 否
- 目标系统或执行范围：
- 期望业务结果：
- 不可改变要求：
- 本次交付：
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

## 六项核心门禁
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

## 后续入口
- 补知识 / 启动 Revision / 补 eval / 核查运行时 / 外部评测
```

## 3. 知识覆盖表

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

## 5. 六项核心门禁摘要

| 门禁 | 生产前信息来源 | 显式产物路径 | 状态 | 失败/警告 | 回退阶段 |
| --- | --- | --- | --- | --- | --- |
| runtime-environment |  |  | pass/warning/fail |  |  |
| execution-context |  |  | pass/warning/fail |  |  |
| business-role |  |  | pass/warning/fail |  |  |
| responsibility-visibility |  |  | pass/warning/fail |  |  |
| attention-plan |  |  | pass/warning/fail |  |  |
| knowledge-conflicts |  |  | pass/warning/fail |  |  |

六项详细产物分别使用下列字段。

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

| 约束 | 影响 | 执行单元 | 主要归属 | 易失效时机/原因 | 注意力手段 | 注入方/时机 | 重复理由 | eval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### 知识疑点与冲突报告

| 疑点 | 来源 | 可疑原因 | 影响范围 | 关键阻塞 | 建议补充方 | 回退阶段 | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |

未发现时写：`已检查，未发现影响本次任务的明显知识问题。`

## 6. prompt 候选清单与架构

| ID | 类型 | 执行单元 | 加载时机 | 唯一职责 | 不承载内容 | 独立理由 | 所需知识/工具 | 对应 eval | 来源 | 置信度/待确认 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

同时保存原始清单和 Skill 建议清单，避免建议覆盖需求。

## 7. prompt 单元规格

```markdown
# Prompt Unit: <id>
- 类型与执行单元：
- 唯一职责：
- 加载时机与 message role：
- 输入和上下文契约：
- 工具契约：
- 输出契约：
- 规则骨架：
- 逐字 prompt：
- 不承载内容：
- 动态占位符及登记位置：
- 来源映射：
- 版本：
- 对应 eval：
- 单元校验状态：
```

## 8. eval 单元规格

```markdown
# Eval Unit: <prompt-id>
- 对应 prompt 与版本：
- 评测目标：
- 失败面：
- 测试输入与前置状态：
- 可验证项及黄金结果：
- judge rubric 与评分锚点：
- 一票否决项：
- 工具/运行时证据要求：
- 通过阈值：
- 外部执行环境：
- 当前状态：未执行 / 已执行
- 结果证据路径：
```

## 9. 运行时集成契约

| Prompt ID | 执行单元/触发 | role/顺序 | 动态变量、状态、历史 | 工具/schema | 输出/parser | anchor 钩子 | 异常路径 | prompt/schema/code/eval 版本 | 来源 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 10. 外部评测交接包

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

## 11. 检查点与分支记录

```markdown
# Task Checkpoint
- 原始任务标识与入口模式：
- 当前主线阶段/状态：
- 本阶段输入：
- 已确认判断：
- 已保存产物路径/版本：
- 未决事项：
- 当前分支与负责人：
- 下一步：
- 主线回归点：
```

## 12. 最终交付清单

```markdown
- [ ] prompts 与 evals 成对
- [ ] 来源映射完整
- [ ] 六项核心门禁产物完整且无关键失败
- [ ] prompt 清单、职责、加载关系完整
- [ ] 运行时集成契约完整
- [ ] 静态校验报告完整
- [ ] 外部评测证据状态真实
- [ ] 非阻塞事项和回退位置已记录
- [ ] 三个人工确认点有证据
- 最终状态：
```

## 13. 机器校验清单 `prompt-package.json`

把路径写成相对于该 JSON 所在目录的路径。来源在外部知识库时，使用相对于 `--knowledge-root` 的路径。

```json
{
  "package_version": "1",
  "delivery_status": "awaiting-external-evaluation",
  "artifacts": {
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
  "units": [
    {
      "id": "example-task",
      "prompt": "prompts/example-task.md",
      "eval": "evals/example-task.md",
      "version": "1.0.0",
      "eval_version": "1.0.0",
      "tools": ["example_tool"],
      "sources": ["topics/example/source.md"]
    }
  ]
}
```
