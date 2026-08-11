# 四类任务协议

## 目录

- 共同规则
- Inspection
- Creation
- Revision
- Eval-only
- 流程交接

## 共同规则

- 为每个任务建立独立标识、目录、检查点和状态。
- 先确认项目知识契约：权威正文、派生导航、草稿、运行时/代码事实和评测证据分别是什么。
- 共享知识发现、来源追溯、六项核心基线和静态/外部评测边界。
- 完整产物写入独立文件；对话仅返回摘要、路径、状态和下一决策。
- 不在一种任务中未经授权执行另一种任务。

## Inspection

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

单 prompt/局部范围可缩减，但不得跳过知识、六项门禁和直接运行时契约。

### 检验步骤

1. 冻结范围、版本、只报告边界和证据契约。
2. 从目标、知识和运行时重建应有体系。
3. 对比应有与现有清单：`matched`、`missing`、`extra`、`wrong-split`、`wrong-merge`、`mis-scoped`、`uncertain`。
4. 对应有/现有单元执行六项门禁和单元质量检查。
5. 按真实装配顺序完成静态集成检查。
6. 区分问题现象与原因归属。
7. 写入独立 Markdown 检验报告和知识补全请求。

体系或清单错误时仍继续审查现有 prompt，但分成：上游错误派生问题、单元自身问题、重构后需复验项。不要假设错误体系下的所有局部结论都会在新体系中继续成立。

### 归因

现象使用：错误、疏漏、多余、冲突、不可验证。原因使用：需求/范围、知识、架构/清单、prompt 生成、运行时/code/schema、eval、尚不能归因。每条发现记录证据、置信度、影响范围、建议动作和回退阶段。

知识缺口不阻止完成其他范围和报告，但受影响结论标记 `uncertain`/`blocked-by-knowledge`，不得判为通过，并同步输出可执行的补全请求。

### 交付和状态

报告至少包括证据边界、应有体系、清单差异、六项门禁、静态集成、分级发现、归因、补全任务、状态和后续入口。状态使用：`inspection-incomplete`、`inspection-failed`、`inspection-static-passed`、`awaiting-external-evaluation`、`external-failed`、`external-passed`。Inspection 不产生 `final-ready`，不自动进入 Revision。

## Creation

从目标和权威知识新建体系。人员已有清单时验证并保留原始清单；人员不知道时推导候选清单。完成知识覆盖、六项门禁和架构确认后，逐单元生成 prompt + eval，再做静态集成和外部评测交接。

不要把现有草稿默认当作正确架构；作为参考时标明证据等级。完整流程使用 `workflow-and-state.md` 的八阶段和三个确认点。

## Revision

以明确变更、知识变化或 inspection 报告为输入。先归因和影响分析，再列出新增、修改、合并、拆分、删除和无需变化项。确认修改授权和影响范围后，只改受影响内容，同步 prompts/evals/来源/运行时契约，形成新版本、差异说明和回退位置。

不覆盖旧版本，不因单个问题无证据重写整套系统。完成静态检查后进入外部评测；失败回到最早产生问题的阶段。

## Eval-only

以已确认 prompts、知识来源、运行时契约和评测目标为输入。只生成或补齐确定性检查、rubric/judge、测试集要求和外部交接。发现 prompt、知识或架构问题时写入独立发现并建议启动 Inspection 或 Revision，不在本任务越权修改。

## 流程交接

`Inspection → 独立报告 → 用户明确启动 Revision`  
`Creation → 新版本 → 外部评测失败归因 → 用户启动 Revision`  
`知识/规则变化 → Revision`  
`Creation/Revision 缺少评测 → Eval-only`

交接时继承证据，不继承未确认结论；保存上一个任务的最终状态和下一个任务的新检查点。
