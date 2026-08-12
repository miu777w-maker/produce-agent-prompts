---
name: produce-agent-prompts
description: 从项目知识库发现并校验 Agent 提示词与评测所需的目标、知识、运行时上下文与职责边界，独立推导 prompt 清单与 eval 场景，分阶段生成或更新 prompts、evals、来源映射和运行时集成契约。Prompt 生产与 Eval 生产是两条独立流程。用于整套或局部 Agent 提示词或评测的新建、改写、审查及知识变更影响分析；关键知识缺失时停止生成并提出补全请求。
---

# Produce Agent Prompts

从项目知识库稳定生产可追溯、可接入、可评测的 Agent prompts 与 evals。Prompt 生产与 Eval 生产是两条独立流程，共享同一知识库这一“共同课本”，但各自独立推导，只在实际评测阶段汇合。把质量要求同时用于生产前取证和生产后校验。不要一步生成整套结果。

## 保持边界

- 直接负责 prompts、evals、来源映射、核心门禁产物、运行时集成契约、静态校验和外部评测交接包。
- 不直接实现项目后端或前端代码，不把静态检查称为真实行为通过，不把某个案例的架构固化成通用规则。
- 优先使用项目知识库；把入库知识视为项目事实，除非存在明显错误、冲突、断链、版本异常或显式非最终限定。
- 遇到影响目标、架构、运行时或关键规则的知识缺口时停止生成。先输出补全请求，待内容带来源进入知识库后重新检索。
- 区分原始要求、知识库事实、人员确认、Skill 建议和外部评测证据，不静默互相替代。

## 关键概念：阶段同步 ≠ 生产绑定

项目知识库常说提示词与评价“同步形成”。这里的“同步”指**项目阶段同步**——在同一项目阶段，Prompt 生产任务与 Eval 生产任务被一起规划、共享同一目标和知识库；**不指生产绑定**。Skill 禁止以下“生产绑定”行为：

- 逐单元 1:1 同步生产（生成一个 prompt 同时生成对应 eval）；
- 以已生成的 prompt 作为 eval 的知识来源；
- 让 eval 文件数量、拆分或要求迁就 prompt 文件。

正确做法：Prompt 与 Eval 各自从知识库独立推导；两者仅在项目阶段上协同，在生产上完全独立。

## 选择任务流程

启用后先明确本次任务，不直接开始正文检索或生成。为提出有意义的范围问题，可以先轻量查看顶层目录、README、索引和 prompt/eval 文件名，不读取正文或形成结论。若发现未完成检查点，先询问继续原任务还是建立新任务。

五条流程分属两组，入口、状态机和授权边界各自独立：

**Prompt 生产组**

1. **Prompt Inspection**：检验已有 prompts 的生产范围、清单、单元质量和系统组合；只生成独立 Markdown 报告，不修改。
2. **Prompt Creation**：新建 prompt 体系；不默认生成 eval。
3. **Prompt Revision**：根据明确变更、知识变化或 inspection 报告修改/优化已有体系，形成可回退新版本。

**Eval 生产组**

4. **Eval Creation**：从知识库和 Agent 目标独立推导，生产评测**完整 Agent 业务行为**的 evals；不以 prompt 为知识源，不修改 prompt。

**执行交接环节**

5. **外部评测执行交接**：仅在 Eval Creation 完成、eval 准备执行时生成交接包；不是一个独立生产流程。

用户已在请求中明确任务时直接采用，不重复提问。每次只问一个会改变流程的关键问题。一条流程完成后停止；只有用户明确启动时才进入另一流程。完整协议见 [references/task-protocols.md](references/task-protocols.md)。

整套系统 Prompt Inspection 必须先依据目标、权威知识和运行时事实独立重建应有 prompt 体系，再与现有文件对比；不得把现有文件列表当作正确范围。

Prompt Creation 再识别 prompt 清单来源：

- **人员给定清单**：保留原始清单，用知识库验证完整性与架构匹配。
- **目标驱动发现**：人员不知道需要哪些 prompts 时，从目标、执行单元、规则作用域和运行时契约推导清单。

人员不知道需要哪些 prompts 不构成阻塞；无法从知识库还原执行单元和关键契约才构成阻塞。

## Prompt Creation 八阶段主流程

本节完整适用于 Prompt Creation。Prompt Revision 复用受影响阶段；Prompt Inspection 与 Eval Creation 使用各自协议，不机械套用八阶段。

1. 启动或恢复任务，冻结原始输入并定位回归点。
2. 明确任务流程、目标、系统范围、不可改变要求和交付范围。
3. 检索知识库并建立覆盖与来源映射。
4. 仅在有关键缺口时进入知识补全分支；补全后返回阶段 3。
5. 推导或验证 prompt 清单、职责、架构、运行时和核心门禁产物。
6. 按依赖顺序逐个生成 prompt 单元。**Prompt Creation 不生成 eval。**
7. 完成确定性检查和静态集成校验。
8. 形成可追溯交付、状态和后续更新入口。

每个阶段保存输入、判断、产物路径、未决事项、分支和下一步。进入每个阶段前必须确认已读取该阶段必读的 reference（见下文“阶段必读 reference”）。详细进入/退出条件及中断协议见 [references/workflow-and-state.md](references/workflow-and-state.md)。

## 按任务设置确认点

确认点是**不可跳过的阶段转换门**，不是可选沟通：

- **Prompt Creation** 保留三个确认点：① 目标与范围 → ② prompt 清单与架构 → ③ 最终交付。未通过确认点不得进入下一阶段（①→检索，②→生成，③→交付）。
- **Prompt Revision** 确认变更目标/授权、影响范围和新版本交付。
- **Prompt Inspection** 通常只确认检验范围与“只报告不修改”。
- **Eval Creation** 确认评测对象（完整 Agent 行为）、场景范围和最终交付。

其他阶段自动推进。只有关键知识缺失、重大冲突或上游结论被修改时暂停。

## 执行核心门禁

在逐字生成任何 prompt 前，显式形成并检查**七项核心门禁**：

1. **需求先行与范围推导**：目标、范围、不可改变要求和 prompt 清单来源是否明确，是否从知识库正确推导。
2. **Agent 运行环境**：工具、消息、状态、输出消费者和异常路径。
3. **关键时机上下文与概念绑定**：术语/代词/概念在该执行时机是否有真实可见的输入与定义。
4. **业务与角色行为**：角色身份、服务对象、目标、语气、行为边界和业务约束。
5. **prompt 职责与信息可见性**：每部分唯一职责、去重、渐进式披露、最小可见信息。
6. **关键约束与注意力安排**：重要易漂移要求的有效位置；anchor/reminder 必须有运行时钩子和必要性。
7. **知识疑点与冲突**：明显错误、冲突、断链、版本问题或非最终内容，按来源和责任方处理。

七项门禁是闭环，不只是填表：每项必须**分析 → 形成显式产物 → 产生对正式文件的具体约束 → 交付前与最终文件反向核对**。任一核心门禁未满足，不得把任务标记为完成或静态通过。即使未发现疑点，也显式记录结论。开始架构设计或生成前完整读取 [references/core-production-gates.md](references/core-production-gates.md)。

## 文件边界与命名优先服从知识库

正式产物的文件数量、拆分、目录、命名和标识体系优先服从知识库：

- 知识库明确规定或能唯一推导文件名/目录/字段名/标识时，原样遵循。
- 知识库定义的“文件字段”默认对应**独立物理文件**；知识库显式说明“可合并/同文件”时才合并。任务边界、门禁归属或“提示词对”关系不代表可以合并成一个文件。
- 不得为排序、可读性或偏好自加前缀、简称或平行命名体系。
- 命名标准冲突或无法唯一确定时，标记冲突并请求确认。仅当知识库确无命名依据时才提候选，候选必须标为建议，落盘前确认。
- 交付前必须检查“预期文件清单 ↔ 实际文件”一一对应，识别少文件、合并文件、多造文件和错目录。

详细规则见 [references/prompt-architecture-and-runtime.md](references/prompt-architecture-and-runtime.md) 的“文件边界与命名协议”。

## 阶段必读 reference

以下对应关系是**进入阶段前的强制勾核清单**，不是“按需可选”。漏读会导致产物偏离协议：

- 检索知识、判断覆盖或提出补全请求时，读取 [references/knowledge-discovery-and-gaps.md](references/knowledge-discovery-and-gaps.md)。
- 推导清单、划分职责、定义加载时机、运行时契约或文件边界时，读取 [references/prompt-architecture-and-runtime.md](references/prompt-architecture-and-runtime.md)。
- 设计 eval、做集成检查、更新影响分析或外部交接时，读取 [references/validation-and-external-handoff.md](references/validation-and-external-handoff.md)。
- 写阶段产物时，读取 [references/artifact-templates.md](references/artifact-templates.md)，只复制本阶段需要的模板。
- 推进八阶段、设置确认点或处理中断时，读取 [references/workflow-and-state.md](references/workflow-and-state.md)。

## 处理环境能力差异

先识别当前环境能够检索、读取、写入和执行哪些工具。不要假设一定存在某个产品或工具名。

- 能直接检索知识库时，按知识发现协议执行。
- 只能读取文件时，使用话题索引、链接和文本搜索能力完成等价检索。
- 不能写入知识库时，生成可复制的补全或沉淀请求，明确等待外部写入。
- 不能执行脚本或模型评测时，生成交接命令/要求并把状态标记为待执行。
- 缺少执行证据时，不声称已搜索、已写入、已校验或已通过。

## 生成和校验规则

- 一次只处理一个最小可独立验收的 prompt 单元（Prompt 流程）或一个业务场景的 eval（Eval 流程）。
- Prompt 与 Eval 各自建立独立追溯链：`原始需求 → 知识来源 → prompt 规则` 和 `评测目标 → 知识来源 → eval 场景`。不得形成 `eval → prompt` 的事实依赖。
- 把动态数据留在运行时上下文，把确定性程序逻辑优先交给 code/schema，不强行写成 prompt。
- 只在约束关键、容易漂移且运行时确有注入钩子时设计 reminder/anchor。
- 仅对已经形成 `prompt-package.json` 的正式包运行 [scripts/validate_prompt_package.py](scripts/validate_prompt_package.py)；没有 manifest 的草稿执行轻量确定性检查，并记录尚未形成可机器校验正式包。行为效果必须由外部模型和运行环境执行。
- 诚实状态：缺少运行时代码、schema 或真实装配证据时，只能标记“设计假设/待代码核验”，不得写成已验证 `pass`。没有外部行为评测证据时，最高只能到 `awaiting-external-evaluation`。详见 [references/validation-and-external-handoff.md](references/validation-and-external-handoff.md) 的“运行时证据不足时”。

状态：`design-not-ready`、`static-failed`、`creation-revision-required`、`prompt-static-passed`、`awaiting-external-evaluation`、`external-failed`、`external-passed`、`final-ready`。

- `creation-revision-required`：静态检查发现体系、清单或门禁问题，需回到架构阶段修订，**不得**乐观标为 `awaiting-external-evaluation`。
- `prompt-static-passed`：Prompt 静态通过，但 Eval 尚未独立就绪。
- `awaiting-external-evaluation`：Eval 已就绪并准备执行。
- `final-ready`：Prompt 与 Eval 外部关键路径均通过且最终交付确认完成。

## 处理突发消息

把新信息归类为当前阶段补充、上游修正、临时分支、任务替换或无关插入。临时分支前保存回归点；结束后判断是否影响主线产物并返回原阶段。上游修正时回到最早受影响阶段，不只修改最后的 prompt。

## 最终交付

把完整 inspection 报告、prompts、evals、契约、差异说明和评测交接写入独立文件。对话只返回摘要、关键阻塞、文件路径、状态和下一决策入口，不把正式产物只留在聊天中。

遵循**最小交付 + 按需追加**原则。Prompt Creation 默认最小交付：

```text
prompts/
  知识库规定的正式 prompt 文件
creation/
  prompt-production-basis.md   # 合并：目标范围/正式文件清单/职责/命名依据/来源映射/运行时契约/概念绑定/知识冲突/用户裁定
  prompt-static-check.md       # 静态校验报告
  task-state.md                # 仅在中断恢复、裁定或持续协作需要时保留
```

按需追加确认门：存在明确跨责任方交接需求时（如给后端的问题清单、运行时工程取证、知识补全），**询问用户是否生成额外 md**；生成的额外 md 必须有明确消费者，不重复记录同一清单。Prompt Creation 不生成逐 prompt eval、eval 体系、外部评测交接包或无消费者阶段报告。

Eval Creation 默认最小交付：`evals/`（基于业务场景和评测执行方式的 eval 文件，数量不等于 prompt 数）+ `eval-production-basis.md` + `eval-static-check.md`；`external-evaluation-handoff.md` 仅在 eval 准备执行时生成。

优先遵循项目已有产物契约；未约定时使用任务根目录下的 `inspection/`、`creation/`、`revision/`、`eval-creation/`、`evals/`。不要把过程报告或草稿写入权威知识目录。面向不同责任方的知识补全请求和运行时工程取证请求分别写成独立 Markdown 文件。

只有在外部评测证据完整且关键路径通过后标记 `final-ready`。
