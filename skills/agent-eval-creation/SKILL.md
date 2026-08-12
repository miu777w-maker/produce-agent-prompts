---
name: agent-eval-creation
description: 从知识库独立推导,评测完整 Agent 业务行为的 evals。不以 prompt 为知识源,不修改 prompt。遵循共同七项原则(_shared/core-principles.md)。也承担“新建或修订整体 Eval”入口。Prompt/Eval 独立生产。
---

# Agent Eval Creation(原型骨架)

评测**完整 Agent 业务行为**(非 prompt 文件)。独立从知识库推导,**不以 prompt 为知识源,不修改 prompt**。一个 eval 场景可跨多 prompt/状态/工具/门禁/异常/回复流程;场景数来自业务,非 prompt 数。本 skill 也承担 Eval 修订入口(新建或修订整体 Eval)。本文件是原型骨架;正式内容在正式迁移时填入。

## 共同原则
遵循 `_shared/core-principles.md`。本流程的七项执行映射见下。

## 主流程(Eval 侧)
1. **明确评测目标与被测 Agent 行为范围**——评测什么 Agent、哪些能力、哪些场景。
2. **独立从知识库检索评测依据**——不读 prompt 作知识源。
3. **按七项形成 eval 场景约束**——失败面覆盖(正常/边界/模糊/冲突/缺失/工具/对抗/长对话/组合/上下游)。
4. **逐场景生成 eval**——不为迎合 prompt 而复制/降低/缩窄;与 prompt 理解不同时标记冲突而非迁就。
5. **按七项倒查交付**——eval 就绪时条件生成外部评测交接。

## 本流程七项映射(Eval 侧)

| 七项 | agent-eval-creation 具体执行 |
| --- | --- |
| 需求先行 | 评测什么 Agent、哪些能力、哪些场景;被测对象是完整 Agent 业务行为 |
| 运行环境 | Agent 在评测环境中收到什么(消息/状态/工具/历史) |
| 上下文绑定 | 测试场景提供的状态是否足以支撑判定 |
| 业务背景 | 正确行为来自哪些知识(独立追溯,不以 prompt 为源) |
| 职责与可见性 | 评测场景是否重复/遗漏/越界;场景数来自业务非 prompt 数 |
| 关键约束 | 是否覆盖高风险/边界/对抗;一票否决只用于破坏正确性/安全/运行契约 |
| 知识错误 | 评测标准是否冲突;与 prompt 理解不同时标记而非迁就 |

## Eval 修订入口
本 skill 承担“新建或修订整体 Eval”。Prompt Revision 发现变更影响 Eval 时,**只记录 Eval 重新评估需求并交回本 skill**,不在 Prompt Revision 中直接修改 Eval(除非用户另行启动并授权)。

## shared 按需读取(渐进披露)

- 启动:`_shared/core-principles.md`
- 确定知识范围时:`_shared/knowledge-discovery.md`(正式迁移)
- 处理运行时证据缺口时:`_shared/runtime-evidence.md`(正式迁移)
- 外部评测交接(条件,eval 就绪时):`_shared/handoff.md`

## 状态(原型占位)
正式迁移时填入。原型阶段:`eval-design-not-ready` → `awaiting-external-evaluation`(eval 就绪)。
