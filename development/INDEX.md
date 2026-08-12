# Skill 设计与更新索引

本仓库根目录本身是可直接安装的 `produce-agent-prompts` Skill。运行文件包括：

- `SKILL.md`：核心触发与工作流；
- `references/`：按任务读取的详细协议和模板；
- `scripts/`：确定性校验工具；
- `agents/`：可选平台适配。

`development/` 只保存 Skill 的生成依据、设计过程、审验记录和更新约束。正常运行时不读取该目录；它用于维护者理解“为什么这样设计、如何安全更新”。

## 最高基线

1. `process-history/00-original-task-input.md`：原始输入和用户修正，始终是最高验收基线；
2. `process-history/16-context-compaction-checkpoint.md`：正式编写前的完整设计检查点；
3. `process-history/18-skill-first-draft-checkpoint.md`：首版成品状态与待办；
4. `process-history/21-first-claude-execution-feedback-intake.md`：首次真实执行反馈归类；
5. `process-history/22-inspection-subprotocol-design-v0.md`：Inspection 独立子协议；
6. `process-history/23-task-workflow-separation-v0.md`：Inspection、Creation、Revision、Eval-only 分离原则。
7. `process-history/29-v0-3-revision-checkpoint.md`：首次 Creation 复盘后的 v0.3 修订——Prompt/Eval 完全分离、七项核心门禁、文件边界与命名协议、定向检索停止协议。

## 设计脉络

- `01`–`05`：任务主线、原始输入映射、信息获取和知识库形态；
- `06`–`09`：prompt 架构、阶段工作流、校验与外部评测；
- `10`：资金安全顾问案例走查；
- `11`–`15`：六项核心门禁、代码边界、就绪审计和目标驱动清单发现；
- `17`：正式文件结构；
- `19`–`20`：初版审验中暂存的 inspection 范围/归因和知识补全产物问题。
- `28`–`29`：首次真实 Creation 复盘（外部归档 28）与 v0.3 修订（29）；Prompt 与 Eval 完全分离，新增文件边界协议、定向检索停止协议和最小交付。

## 更新流程

1. 先保存新反馈或原始请求，不直接改运行文件；
2. 区分 Skill 问题、项目知识问题、被检 prompts 问题和执行者偏差；
3. 把拟修改原则写入 `development/process-history/`，保留来源和证据边界；
4. 确认后再修改根目录的 `SKILL.md`、`references/`、`scripts/` 或平台适配；
5. 运行结构检查、脚本测试和对应任务模式的真实场景回归；
6. 记录已验证模式与未验证范围；
7. 提交 Git 版本；
8. 从 Git 版本更新个人或项目安装副本，不直接在安装副本中形成唯一修改。

当前发布状态见根目录 `VERSION.md`。不要把“协议已写入”与“端到端真实验证完成”混为一谈。

## 发布边界

- 不因一次 inspection 结果宣称四种任务流程全部通过；
- 不把资金安全顾问的业务规则固化进通用 Skill；
- 不把静态校验称为外部行为通过；
- 不在 Inspection 中自动进入 Revision；
- 不删除原始输入或用后续分析覆盖它；
- 每次版本至少说明修改原因、验证证据和未覆盖范围。
