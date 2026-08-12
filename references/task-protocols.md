# 任务协议

## 目录

- 共同规则
- Prompt Inspection
- Prompt Creation
- Prompt Revision
- Eval Creation
- 外部评测执行交接
- 流程交接

## 共同规则

- 为每个任务建立独立标识、目录、检查点和状态。
- 先确认项目知识契约：权威正文、派生导航、草稿、运行时/代码事实和评测证据分别是什么。
- 共享知识发现、来源追溯、七项核心基线和静态/外部评测边界。
- **Prompt 生产组（Inspection / Creation / Revision）不生成 eval；Eval 生产组不修改 prompt。** 不在一种任务中未经授权执行另一种任务。
- 文件边界与命名优先服从知识库（见 `prompt-architecture-and-runtime.md`）。
- 产物遵循最小交付 + 按需追加（见 `SKILL.md`）。
- 完整产物写入独立文件；对话仅返回摘要、路径、状态和下一决策。

## Prompt Inspection

### 目标与范围

检查生产范围、应有 prompt 清单、现有单元质量、系统组合、知识忠实度和运行时真实性。范围分为单 prompt、局部组合和整套系统。

整套系统 inspection 必须先依据目标、权威知识和运行时事实独立重建应有执行单元与 prompt 清单，再与现有 prompts 对比。不要把现有文件列表当作正确范围。

### 必读资源

整套系统 inspection 必须读取：

- `knowledge-discovery-and-gaps.md`；
- `core-production-gates.md`；
- `prompt-architecture-and-runtime.md`；
- `validation-and-external-handoff.md`；
- 形成报告时读取 `artifact-templates.md`。

单 prompt/局部范围可缩减，但不得跳过知识、七项门禁和直接运行时契约。

### 检验步骤

1. 冻结范围、版本、只报告边界和证据契约。
2. 从目标、知识和运行时重建应有体系。
3. 对比应有与现有清单：`matched`、`missing`、`extra`、`wrong-split`、`wrong-merge`、`mis-scoped`、`uncertain`。
4. 对应有/现有单元执行七项门禁和单元质量检查。
5. 按真实装配顺序完成静态集成检查。
6. 区分问题现象与原因归属。
7. 写入独立 Markdown 检验报告和知识补全请求。

体系或清单错误时仍继续审查现有 prompt，但分成：上游错误派生问题、单元自身问题、重构后需复验项。不要假设错误体系下的所有局部结论都会在新体系中继续成立。

### 归因

现象使用：错误、疏漏、多余、冲突、不可验证。原因使用：需求/范围、知识、架构/清单、prompt 生成、运行时/code/schema、eval、尚不能归因。每条发现记录证据、置信度、影响范围、建议动作和回退阶段。

知识缺口不阻止完成其他范围和报告，但受影响结论标记 `uncertain`/`blocked-by-knowledge`，不得判为通过，并同步输出可执行的补全请求。

### 七项门禁的 Inspection 视角

| 门禁 | Inspection 判断 |
| --- | --- |
| 需求先行与范围推导 | 目标、范围、不可改变要求是否明确；应有清单是否从知识库正确推导，是否把现有文件列表误当作正确范围。 |
| 运行环境 | 现有 prompt 声明或依赖的消息、变量、状态、工具、输出和异常是否有运行时证据；无代码/schema 证据时标待核验，不判可接入通过。 |
| 时机上下文与概念绑定 | 每个指代、字段和上游概念是否在目标调用时机真实可见；需要但未供给时归因到运行时/架构缺口。 |
| 业务与角色 | 身份、目标、行为和边界是否忠实于权威知识，并保留非最终、例外和范围限定。 |
| 职责与可见性 | 应有清单是否完整，职责是否错位、重叠或遗漏，局部 Agent 是否读取无关信息，重复是否有运行时理由。 |
| 约束与注意力 | 高风险约束是否位于有效载体和时机；anchor/reminder 是否有真实钩子、必要性和漂移测试。 |
| 知识疑点 | 现有 prompt 是否误读、遗漏或新增无来源规则；知识本身冲突时区分知识问题与生成问题。 |

门禁级别使用 `pass`、`warning`、`fail`、`blocked`：`blocked` 表示检查动作已完成，但关键结论等待知识或运行时证据，不等于发现确定错误。

### 已有 eval 审查（范围含 eval 时）

仅当检验范围明确包含 eval 时执行，且 eval 视为独立产物审查，不作为 prompt 的附属：

- eval 是否独立从知识库可追溯，是否以 prompt 为隐性知识源而迁就、降低或缩窄要求；
- eval 被测对象是否为完整 Agent 业务行为，而非单段 prompt 文本；
- 确定性可验证项与 judge 主观项是否分开，条目是否正交；
- 正常、边界、模糊、冲突、缺失、工具、对抗、长对话、组合和上下游案例是否按风险覆盖；
- 一票否决是否只用于破坏正确性、安全或运行契约的行为；
- reminder/anchor 是否有针对重注入与漂移效果的测试；
- eval 所需工具调用、状态和运行日志是否能由外部环境提供。

### 交付和状态

报告至少包括证据边界、应有体系、清单差异、七项门禁、eval 审查（如适用）、静态集成、分级发现、归因、补全任务、状态和后续入口。

状态汇聚：

- `inspection-incomplete`：约定范围或必要检查动作尚未完成；
- `inspection-blocked`：必要检查已执行，但至少一个关键门禁等待知识、代码、schema 或运行时证据，不能判静态通过；
- `inspection-failed`：存在有充分证据的关键错误；即使同时有 blocked 项，整体仍为 failed，并另列阻塞；
- `inspection-static-passed`：范围、清单、七项门禁、eval（如适用）和静态集成均完成且无关键 fail/blocked；
- 静态通过后才能进入 `awaiting-external-evaluation`，收到证据后使用 `external-failed`/`external-passed`。

Inspection 不产生 `final-ready`，不自动进入 Revision。

## Prompt Creation

从目标和权威知识新建 prompt 体系。人员已有清单时验证并保留原始清单；人员不知道时推导候选清单。完成知识覆盖、七项门禁和架构确认后，**逐单元生成 prompt（不生成 eval）**，再做静态集成。

外部评测交接、eval 体系和逐 prompt eval **不属于本流程**。

不要把现有草稿默认当作正确架构；作为参考时标明证据等级。完整流程使用 `workflow-and-state.md` 的八阶段和三个确认点。

## Prompt Revision

以明确变更、知识变化或 inspection 报告为输入。先归因和影响分析，再列出新增、修改、合并、拆分、删除和无需变化项。确认修改授权和影响范围后，只改受影响 prompt 与相关运行时契约、来源映射，形成新版本、差异说明和回退位置。

不覆盖旧版本，不因单个问题无证据重写整套系统。Prompt Revision 不生成 eval；现有 eval 若需调整，建议另启 Eval Creation。完成静态检查后回到相应状态；失败回到最早产生问题的阶段。

## Eval Creation

从知识库和 Agent 目标**独立推导**，生产评测**完整 Agent 业务行为**的 eval。

- 被测对象是完整 Agent 的业务行为和系统能力，不是 prompt 文件。一个 eval 场景可跨多个 prompt、上下文、状态、工具调用、门禁、异常和回复流程。
- eval 文件数量和拆分来自业务场景及评测执行方式，**不来自 prompt 文件数量**；不建立“一份 prompt 对应一份 eval”的映射。
- 溯源为 `评测目标 → 知识来源 → eval 场景`，**不是 `eval → prompt`**。生成 eval 时不参考已生成 prompt 来复制、降低或缩窄评测要求。
- prompt 只在实际评测阶段作为 Agent 实现的一部分进入被测系统。
- eval 与 prompt 对同一知识产生不同理解时，标记知识/需求/推导冲突，不让 eval 迁就 prompt；必要时建议启动 Prompt Inspection 或 Revision。
- 不修改 prompt。发现 prompt、知识或架构问题时写入独立发现并建议相应流程，不在本任务越权修改。

完整阶段序列使用 `workflow-and-state.md` 的“Eval Creation 阶段”。外部评测执行交接仅在 eval 准备执行时生成。

## 外部评测执行交接

不是一个独立生产流程，而是 Eval Creation 完成、eval 准备执行时的交接环节。交接内容见 `validation-and-external-handoff.md`。不得把未执行、抽样不足或无法追溯的结果标为通过。

## 流程交接

`Prompt Inspection → 独立报告 → 用户明确启动 Prompt Revision`  
`Prompt Creation → 新版本 → 外部评测失败归因 → 用户启动 Prompt Revision`  
`Eval Creation → eval 就绪 → 外部评测执行交接 → 结果归因`  
`知识/规则变化 → Prompt Revision；评测需求变化 → Eval Creation`

交接时继承证据，不继承未确认结论；保存上一个任务的最终状态和下一个任务的新检查点。
