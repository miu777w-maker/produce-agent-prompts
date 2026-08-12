---
name: produce-agent-prompts
description: 从项目知识库发现并校验 Agent 提示词所需的目标、知识、运行时上下文与职责边界，推导或验证 prompt 清单，分阶段生成或更新 prompts、evals、来源映射和运行时集成契约。用于整套或局部 Agent 提示词的新建、改写、审查及知识变更影响分析；关键知识缺失时停止生成并提出补全请求。
---

# Produce Agent Prompts

从项目知识库稳定生产可追溯、可接入、可评测的 Agent prompts。把提示词质量要求同时用于生产前取证和生产后校验。不要一步生成整套结果。

## 保持边界

- 直接负责 prompts、配套 evals、来源映射、六项核心门禁产物、运行时集成契约、静态校验和外部评测交接包。
- 不直接实现项目后端或前端代码，不把静态检查称为真实行为通过，不把某个案例的架构固化成通用规则。
- 优先使用项目知识库；把入库知识视为项目事实，除非存在明显错误、冲突、断链、版本异常或显式非最终限定。
- 遇到影响目标、架构、运行时或关键规则的知识缺口时停止生成。先输出补全请求，待内容带来源进入知识库后重新检索。
- 区分原始要求、知识库事实、人员确认、Skill 建议和外部评测证据，不静默互相替代。

## 选择任务流程

启用后先明确本次任务，不直接开始正文检索或生成。为提出有意义的范围问题，可以先轻量查看顶层目录、README、索引和 prompt/eval 文件名，不读取正文或形成结论。若发现未完成检查点，先询问继续原任务还是建立新任务；新任务提供：

1. **Inspection**：检验已有 prompts 的生产范围、清单、单元质量和系统组合；只生成独立 Markdown 报告，不修改。
2. **Creation**：新建 prompt 体系；同步生成 evals、来源映射和运行时契约。
3. **Revision**：根据明确变更、知识变化或 inspection 报告修改/优化已有体系，形成可回退的新版本。
4. **Eval-only**：为已确认的 prompts 编写或补齐 evals，不擅自重写 prompts。

用户已在请求中明确任务时直接采用，不重复提问。每次只问一个会改变流程的关键问题。

四条流程共享知识发现和六项核心基线，但任务状态、产物和授权边界独立。一个流程完成后停止；只有用户明确启动时才进入另一流程。完整协议见 [references/task-protocols.md](references/task-protocols.md)。

整套系统 Inspection 必须先依据目标、权威知识和运行时事实独立重建应有 prompt 体系，再与现有文件对比；不得把现有文件列表当作正确范围。

Creation 再识别 prompt 清单来源：

- **人员给定清单**：保留原始清单，用知识库验证完整性与架构匹配。
- **目标驱动发现**：人员不知道需要哪些 prompts 时，从目标、执行单元、规则作用域和运行时契约推导清单。

人员不知道需要哪些 prompts 不构成阻塞；无法从知识库还原执行单元和关键契约才构成阻塞。

## Creation 八阶段主流程

本节完整适用于 Creation。Revision 只复用受影响阶段；Inspection 与 Eval-only 使用各自协议，不机械套用八阶段。

1. 启动或恢复任务，冻结原始输入并定位回归点。
2. 明确任务流程、目标、系统范围、不可改变要求和交付范围。
3. 检索知识库并建立覆盖与来源映射。
4. 仅在有关键缺口时进入知识补全分支；补全后返回阶段 3。
5. 推导或验证 prompt 清单、职责、架构、运行时和六项核心门禁产物。
6. Creation/Revision 按依赖顺序逐个生成或修改 prompt 单元及其 eval；Inspection 跳过生成，Eval-only 只处理评测。
7. 完成确定性检查、静态集成校验并形成外部评测交接包。
8. 形成可追溯交付、状态和后续更新入口。

每个阶段保存输入、判断、产物路径、未决事项、分支和下一步。详细进入/退出条件及中断协议见 [references/workflow-and-state.md](references/workflow-and-state.md)。

## 按任务设置确认点

Creation 保留三个确认点：目标与范围、prompt 清单与架构、最终交付。Revision 确认变更目标/授权、影响范围和新版本交付。Inspection 通常只确认检验范围与“只报告不修改”；Eval-only 确认评测对象和范围。

其他阶段自动推进。只有关键知识缺失、重大冲突或上游结论被修改时暂停。

## 执行核心门禁

在逐字生成任何 prompt 前，显式形成并检查：

1. Agent 运行环境说明；
2. 关键执行时机上下文契约与概念引用绑定表；
3. 业务与角色行为契约；
4. prompt 职责与信息可见性矩阵；
5. 关键约束与注意力安排；
6. 知识疑点与冲突检查报告。

把六项同时视为生产前所需信息和生产后验收基线。任何关键项失败时不得生成。即使未发现疑点，也显式记录结论。开始架构设计或生成前完整读取 [references/core-production-gates.md](references/core-production-gates.md)。

## 按需读取资源

- 检索知识、判断覆盖或提出补全请求时，读取 [references/knowledge-discovery-and-gaps.md](references/knowledge-discovery-and-gaps.md)。
- 推导清单、划分职责、定义加载时机或运行时契约时，读取 [references/prompt-architecture-and-runtime.md](references/prompt-architecture-and-runtime.md)。
- 设计 eval、做集成检查、更新影响分析或外部交接时，读取 [references/validation-and-external-handoff.md](references/validation-and-external-handoff.md)。
- 写阶段产物时，读取 [references/artifact-templates.md](references/artifact-templates.md)，只使用本阶段需要的模板。

## 处理环境能力差异

先识别当前环境能够检索、读取、写入和执行哪些工具。不要假设一定存在某个产品或工具名。

- 能直接检索知识库时，按知识发现协议执行。
- 只能读取文件时，使用话题索引、链接和文本搜索能力完成等价检索。
- 不能写入知识库时，生成可复制的补全或沉淀请求，明确等待外部写入。
- 不能执行脚本或模型评测时，生成交接命令/要求并把状态标记为待执行。
- 缺少执行证据时，不声称已搜索、已写入、已校验或已通过。

## 生成和校验规则

- 一次只处理一个最小可独立验收的 prompt 单元，并同步生成对应 eval。
- 建立“原始需求 → 知识来源 → prompt 规则 → eval 条目”的追溯链。
- 把动态数据留在运行时上下文，把确定性程序逻辑优先交给 code/schema，不强行写成 prompt。
- 只在约束关键、容易漂移且运行时确有注入钩子时设计 reminder/anchor。
- 仅对已经形成 `prompt-package.json` 的正式包运行 [scripts/validate_prompt_package.py](scripts/validate_prompt_package.py)；没有 manifest 的草稿执行轻量确定性检查，并记录尚未形成可机器校验正式包。行为效果必须由外部模型和运行环境执行。
- 使用状态：`design-not-ready`、`static-failed`、`awaiting-external-evaluation`、`external-failed`、`external-passed`、`final-ready`。
- 没有外部结果时，最高只能到 `awaiting-external-evaluation`。

## 处理突发消息

把新信息归类为当前阶段补充、上游修正、临时分支、任务替换或无关插入。临时分支前保存回归点；结束后判断是否影响主线产物并返回原阶段。上游修正时回到最早受影响阶段，不只修改最后的 prompt。

## 最终交付

把完整 inspection 报告、prompts、evals、契约、差异说明和评测交接写入独立文件。对话只返回摘要、关键阻塞、文件路径、状态和下一决策入口，不把正式产物只留在聊天中。

优先遵循项目已有产物契约；未约定时使用任务根目录下的 `inspection/`、`creation/`、`revision/`、`evals/`。不要把过程报告或草稿写入权威知识目录。面向不同责任方的知识补全请求和运行时工程取证请求分别写成独立 Markdown 文件。

Creation/Revision 交付 prompts、evals、来源映射、六项门禁产物、prompt 总览与加载关系、运行时集成契约、静态校验报告、外部评测交接包、状态与未决事项。只在外部评测证据完整且关键路径通过后标记 `final-ready`。
