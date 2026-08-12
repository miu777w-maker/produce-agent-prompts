# Produce Agent Prompts V0.3 修订检查点

> 日期：2026-08-12  
> 状态：运行文件修订完成，脚本语法与最小包校验通过，七场景静态回归进行中，待 Git 提交和推送。  
> 上一版本：v0.2.0（commit `40e33b4`）。

## 修订定位

基于原始七项重点、首次真实 Creation 的执行交接报告和实际产物，修订并发布 v0.3.0。本轮只改 Skill 仓库本身，不修改资金安全顾问项目的现有 Prompt / Eval / 知识库（见“未加入”）。

## 依据来源

- 原始任务输入：`00-original-task-input.md`（七项核心重点的源头）；
- 首次 Creation 复盘与交接：外部归档 `28-v0-2-creation-retrospective-and-next-session-handoff.md`；
- 首次 Creation 执行交接报告：`/Users/miumiu777/Desktop/AI work/idiot/legal_advice_prompt/skill_feedback/2026-08-12-creation-skill-handoff.md`；
- 用户在本修订会话中的三条裁定（见下）。

## 用户裁定（本轮最高输入）

1. **流程模型**：Prompt Production 与 Eval Creation 完全拆为两个独立一级流程。
2. **“同步”的真正含义**：知识库评测卡的“同步形成”指**项目阶段同步**（Prompt 任务与 Eval 任务在同一项目阶段一起规划），**不是 Skill 层面的生产绑定**。知识库表述本身无错；是 v0.2 Skill 把它误读为逐单元 1:1 同步生产。因此本轮不引入“裁定优先级压过知识库”的重机制，而是修正 Skill 的误读、正确实现知识库本意。
3. **最小交付**：采用三类结构 + **按需追加确认门**——存在明确跨责任方交接需求（如给后端的问题清单、运行时工程取证、知识补全）时，询问用户是否生成额外 md；额外 md 必须有明确消费者。

此外沿用一条分级裁定：运行时证据缺失按层次分级——业务语义层缺失且知识库无法补全 → 阻断；工程实现细节缺失（不影响 prompt 文本语义）→ 仅标 warning。

## 本版修改（对应分级结论的必须项）

| 编号 | 改动 | 落地文件 |
| --- | --- | --- |
| M1 | Prompt/Eval 完全分离，删除逐单元同步生产 | 全部运行文件 + 脚本 |
| M2 | Eval 评完整 Agent、独立从 KB 推导 | SKILL、task-protocols、workflow-and-state(Eval Creation 阶段)、validation、artifact-templates(模板9/14/17)、脚本 |
| M3 | 文件边界与命名优先服从 KB；file_field 默认对应独立物理文件 | SKILL、prompt-architecture-and-runtime(新增“文件边界与命名协议”)、artifact-templates(模板7/8)、脚本(file_field 唯一性) |
| M4 | 六项→七项门禁；每项产约束并交付前倒查 | SKILL、core-production-gates、task-protocols、artifact-templates(模板2/6) |
| M5 | 确认点设为不可跳过的阶段转换硬门 | SKILL、workflow-and-state(确认点 + blocked-on-confirmation) |
| M6 | 大型知识库定向检索与停止协议 | knowledge-discovery-and-gaps(重写“按任务检索”为“定向检索与停止协议”)、workflow-and-state(阶段3) |
| M7 | 产物必要性与最小交付 + 按需追加 | SKILL(最终交付)、artifact-templates(模板15/16/17) |
| M8 | 阶段→必读 reference 强制勾核清单 | SKILL(阶段必读)、workflow-and-state(阶段必读表) |
| M9 | 运行时证据缺失的诚实状态与分级 | SKILL、core-production-gates(分级)、validation(运行时证据不足) |
| S1 | 状态机补 `creation-revision-required` / `prompt-static-passed` | SKILL、workflow-and-state、validation、脚本(ALLOWED_STATUSES) |
| S5 | 静态校验基准不再要求 Prompt/Eval 1:1 | validation、artifact-templates(模板13/14)、脚本(prompt_units/eval_scenarios 独立) |
| S6 | VERSION.md → v0.3.0 就绪度与变更说明 | VERSION.md、本文件 |

## 关键概念（写入 SKILL.md）

**阶段同步 ≠ 生产绑定**：项目阶段同步允许（两条流程在同一阶段并行规划、共享知识库）；生产绑定禁止（逐单元 1:1、eval 以 prompt 为知识源、eval 文件数迁就 prompt 数）。

## 未加入（本轮明确不动）

- **W1** 不修改项目知识库评测卡的“同步形成”表述——KB 无错，是 Skill 误读；改为 Skill 正确实现 KB 本意。知识库的 F1（门禁工具调用）/F2（角色卡非最终）回写交 knowledge-zettel，本轮不动。
- **W2** 不修改、不重新生成资金安全顾问项目的现有 5 Prompt / 5 Eval / 5 creation 文件；待 v0.3 发布后用新版本重新启动纯 Prompt Creation。
- 不新增输入供给独立门禁；不强制 transcript；不绑定宿主记忆系统；不把未验证流程宣称成熟。

## 验证结果

- 校验脚本 `python3 -m py_compile`：通过；
- 七场景静态回归：见下方“回归”节（进行中）；
- 以上为协议和确定性验证，不等于 Creation 实际生成质量或外部行为通过。

## 回归（七场景）

1. 只生成 Prompt 不生成 Eval —— SKILL 阶段6、task-protocols Prompt Creation、workflow-and-state 阶段6 均明确不生成 eval：通过。
2. 只生成整体 Agent Eval，不读 Prompt 作知识源 —— task-protocols Eval Creation、workflow-and-state E2、artifact-templates 模板9/17、validation 追溯链：通过。
3. KB 定义两个文件时禁止合并 —— prompt-architecture-and-runtime“文件边界与命名协议”+ 脚本 file_field 唯一性警告：通过。
4. KB 有命名标准时禁止自行命名 —— prompt-architecture-and-runtime 命名协议 + artifact-templates 模板7“文件字段/命名依据”列：通过。
5. 大型 KB 定向检索并有停止理由 —— knowledge-discovery-and-gaps“定向检索与停止协议”+ workflow-and-state 阶段3 产物含停止理由：通过。
6. 运行时证据不足时不得判 pass —— core-production-gates 分级 + validation“运行时证据不足时” + artifact-templates 模板16：通过。
7. 非必要过程文件不得生成 —— SKILL 最小交付 + 按需追加 + artifact-templates 模板15/16/17：通过。

## 下一主线

用 v0.3 在资金安全顾问项目知识库重新启动**纯 Prompt Creation**（依据 KB 重新确认正式文件级清单，移除自加命名前缀，拆分应独立的 reminder，重新检查门禁 Agent 的信息可见性）。Prompt 通过正确的静态生产校验后，再**独立启动 Eval Creation**。
