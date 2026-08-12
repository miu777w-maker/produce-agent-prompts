# 工作流与状态协议

## 目录

- 稳定生产原则
- Prompt Creation 八阶段
- Eval Creation 阶段
- 人工确认点
- 阶段必读 reference
- 状态与检查点
- 中断与恢复

## 稳定生产原则

- 每阶段只承担一种主要判断并形成一种主要产物。
- 仅根据已保存、可定位的上游产物继续。
- 门禁未通过时停留或回退，不用猜测填空。
- 确认点是阶段转换的硬门，未确认不得进入下一阶段。
- 区分需求事实与 Skill 建议；建议不能静默改变范围。
- Prompt Creation 只生产 prompt，不生产 eval；Eval Creation 只生产 eval，不改 prompt。
- 持续记录主线、待办、分支和回归点。

## Prompt Creation 八阶段

本节完整适用于 Prompt Creation。Prompt Revision 复用受影响阶段但先做影响分析；Prompt Inspection 和 Eval Creation 使用 `task-protocols.md` 的独立流程与下文“Eval Creation 阶段”，不机械套用本节。

### 阶段 1：启动与恢复

读取原始需求、知识库契约、已有产物和最近检查点。发现未完成检查点时先让人员选择继续原任务或建立新任务；不要覆盖原状态。判断新任务或恢复任务，不重做已确认内容。

产物：任务状态卡。  
退出条件：原始输入、当前阶段、产物路径和回归点可定位。

### 阶段 2：目标解析与入口识别

保留原始需求，先识别任务流程（Prompt Inspection / Prompt Creation / Prompt Revision / Eval Creation）。用户未说明时提供选项；已说明时直接采用。Prompt Creation 再判断人员是否已有 prompt 清单。

随后明确目标系统、业务结果、范围、不可改变要求、交付类型和明确排除项。识别明确清单、目标驱动或变化驱动知识入口。把明确要求、知识库事实和 Skill 建议分栏记录。

产物：任务类型、目标与范围确认。  
退出条件：完成**确认点 1**（目标、范围、不可改变要求、清单来源）。人员不知道 prompt 清单不阻塞，但目标与范围未确认不得进入阶段 3。

### 阶段 3：知识发现与覆盖

按知识库契约定向检索（见 `knowledge-discovery-and-gaps.md`）：从任务目标推导调查主题，沿话题→根/综合卡→原子卡→链接/反链展开，区分必须读/只需知存在/明确无关/待定，记录读取范围与停止理由。建立任务覆盖表、来源映射和疑点报告。目标驱动时同时识别执行单元和规则作用域。

产物：知识覆盖表、来源映射、疑点与缺口、检索范围与停止理由。  
退出条件：关键输入均有来源，不存在未解决的关键缺口或冲突。

### 阶段 4：知识补全分支

仅在阶段 3 发现关键缺口时进入。生成包含问题、原因、期望证据、建议回答方和回写位置的请求。等待信息带来源进入知识库后重新检索。

产物：知识补全请求和阻塞记录。  
退出条件：补充内容已入库且可重新定位。  
回归点：始终返回阶段 3，不直接进入架构或生成。

### 阶段 5：prompt 清单与架构设计

推导或验证执行单元、prompt 清单、职责、信息可见范围、加载时机、文件边界、命名和运行时集成契约。形成七项核心门禁产物和规则归属映射。每项门禁必须产生对正式文件的具体约束。变化驱动时形成影响分析和拟修改清单。

产物：prompt 方案、七项核心门禁产物（含约束清单）、运行时集成契约、文件清单与命名依据。  
退出条件：七项门禁通过并完成**确认点 2**（最终 prompt 清单、职责、架构、上下文、加载时机、文件边界与命名）。未确认不得进入阶段 6 生成。

### 阶段 6：逐单元生成 prompt

按依赖顺序处理：共享底座、独立任务、必要 reminder/anchor。每次读取该单元的架构项和来源，先写规则骨架，再写逐字 prompt。**Prompt Creation 不生成 eval、不生成外部评测交接包。**

产物：单个 prompt 单元和来源映射。  
退出条件：当前单元通过需求、知识、运行时、职责、指令、注意力检查。

### 阶段 7：静态集成

按真实加载顺序重建关键时机上下文，检查跨层冲突、变量、工具、输出、上下游、异常路径，以及“预期文件清单 ↔ 实际文件”一一对应（少文件、合并文件、多造文件、错目录）。运行确定性校验。

产物：静态校验报告。  
退出条件：静态检查通过后标记 `prompt-static-passed`（eval 尚未独立就绪，不是最终通过）。若发现体系、清单或门禁问题，标记 `creation-revision-required` 并回到阶段 5。

### 阶段 8：交付与维护

核对需求覆盖、目录、命名、来源、版本和最小交付内容。按需追加确认门：存在明确跨责任方交接需求时，询问用户是否生成额外 md。记录非阻塞事项、更新入口和回退位置。

产物：完整交付包和最终状态。  
退出条件：完成**确认点 3**（最终交付）。Prompt Creation 本身止于 `prompt-static-passed`；`final-ready` 需 Eval Creation 外部通过后另行达成。

## Eval Creation 阶段

Eval Creation 独立于 Prompt Creation，可单独启动。下列阶段可按需精简，但不得跳过知识发现和场景架构。

### 阶段 E1：启动与评测目标解析

冻结原始需求，明确被测对象为**完整 Agent 的业务行为和系统能力**，界定评测范围（哪些执行单元、状态、工具、门禁、回复流程纳入被测）。

产物：评测目标与被测 Agent 行为范围。  
退出条件：完成**确认点 E1**（评测对象与范围）。

### 阶段 E2：知识发现与覆盖

**独立从知识库检索**评测依据（业务目标、角色行为、门禁判定标准、工具契约、异常路径、评测方法论），不读取已有 prompt 作为知识源。建立覆盖表、来源映射和疑点报告。

产物：评测知识覆盖表、来源映射（`评测目标 → 知识来源`）。  
退出条件：评测所需业务事实均有来源，无关键缺口。

### 阶段 E3：知识补全分支

仅在 E2 发现关键缺口时进入，规则同 Prompt Creation 阶段 4。回归点为 E2。

### 阶段 E4：eval 场景与架构设计

按业务场景和失败面设计 eval：场景拆分（数量来自业务场景与评测执行方式，不来自 prompt 数）、可验证项与 judge 项、一票否决项、通过阈值、所需工具/状态/运行日志。每条 eval 必须可独立追溯到知识库。

产物：eval 场景清单、rubric/judge 架构、失败面覆盖。  
退出条件：完成**确认点 E2**（eval 场景清单、失败面、rubric 架构）。

### 阶段 E5：逐场景生成 eval

按场景生成 eval 文件。不得为迎合已有 prompt 而复制、降低或缩窄要求。与 prompt 对同一知识理解不同时标记冲突。

产物：单个 eval 文件和来源映射。  
退出条件：当前场景通过失败面覆盖、可验证性、judge 可执行性检查。

### 阶段 E6：静态检查与外部评测交接

静态检查 eval 内部一致性、场景覆盖、工具/状态可供给性。eval 准备执行时生成外部评测交接包。

产物：eval 静态检查报告、外部评测交接包（仅就绪时）。  
退出条件：静态通过标记 `awaiting-external-evaluation`。

### 阶段 E7：交付

核对场景覆盖、来源、版本。  
退出条件：完成**确认点 E3**（最终交付）。

## 人工确认点

确认点是不可跳过的阶段转换门：

**Prompt Creation**

1. 目标、范围、不可改变要求和清单来源（阶段 2 → 3）；
2. 最终 prompt 清单、职责、架构、上下文、加载时机、文件边界与命名（阶段 5 → 6）；
3. 最终交付（阶段 8）。

**Eval Creation**

1. 评测对象与范围（E1 → E2）；
2. eval 场景清单、失败面、rubric 架构（E4 → E5）；
3. 最终交付（E7）。

**Prompt Revision** 确认变更目标/授权、影响范围、新版本交付。**Prompt Inspection** 确认检验范围与“只报告不修改”。

关键知识需要业务决策时属于阻塞取证，不增加常规确认点。

## 阶段必读 reference

进入每个阶段前必须确认已读取对应 reference，不得视为“按需可选”：

| 阶段 | 必读 reference |
| --- | --- |
| 目标解析（阶段 2 / E1） | `task-protocols.md` |
| 知识发现（阶段 3 / E2） | `knowledge-discovery-and-gaps.md` |
| 知识补全（阶段 4 / E3） | `knowledge-discovery-and-gaps.md` |
| 清单与架构（阶段 5） | `prompt-architecture-and-runtime.md`、`core-production-gates.md` |
| eval 场景架构（E4） | `prompt-architecture-and-runtime.md`、`validation-and-external-handoff.md` |
| 逐单元生成（阶段 6 / E5） | `artifact-templates.md`、`core-production-gates.md` |
| 静态集成（阶段 7 / E6） | `validation-and-external-handoff.md` |
| 交付（阶段 8 / E7） | `artifact-templates.md` |

## 状态与检查点

使用两组状态：

阶段状态：`not-started`、`in-progress`、`waiting-for-knowledge`、`blocked-on-confirmation`、`passed`。  
交付状态：`design-not-ready`、`static-failed`、`creation-revision-required`、`prompt-static-passed`、`awaiting-external-evaluation`、`external-failed`、`external-passed`、`final-ready`。

- `blocked-on-confirmation`：等待人工确认点，未确认不得推进。
- `creation-revision-required`：静态检查发现体系、清单或门禁问题，需回到架构阶段，不得乐观标为 `awaiting-external-evaluation`。
- `prompt-static-passed`：Prompt 静态通过，但 Eval 尚未独立就绪。
- `awaiting-external-evaluation`：Eval 已就绪并准备执行。
- `final-ready`：Prompt 与 Eval 外部关键路径均通过且最终交付确认完成。

Prompt Inspection 使用 `inspection-incomplete`、`inspection-blocked`、`inspection-failed`、`inspection-static-passed`，不要套用 `design-not-ready` 表达已完成但待证据的审查。

每个检查点记录：

- 原始任务标识和任务流程；
- 任务流程：prompt-inspection / prompt-creation / prompt-revision / eval-creation；
- 当前主线阶段与状态；
- 本阶段输入和已确认判断；
- 产物路径与版本；
- 关键缺口和非阻塞事项；
- 当前分支、负责人和等待对象；
- 下一动作与主线回归点。

恢复时先读最近检查点，再读取当前阶段需要的上游产物。不要重新解释已冻结的原始需求。

## 中断与恢复

收到突发信息时先分类：

- **当前阶段补充**：纳入当前产物，继续原门禁。
- **上游修正**：记录来源，回到最早受影响阶段，重审下游产物。
- **临时分支**：保存回归点，建立独立目标与待办；完成后评估影响并返回原阶段。
- **任务替换**：冻结旧任务状态，建立新的原始需求，不混写产物。
- **无关插入**：处理后返回当前检查点，不改变范围。

每次中断都说明分类、受影响阶段、是否回退或建分支，以及处理后回到哪里。
