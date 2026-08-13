# D6 删减实施(审查 4.0/5 后的小型修订)

> 日期:2026-08-13
> 依据:40 号报告 → 审查 4.0/5(D1–D5 保留)+ D6 五项;用户确认(含 D6-2 占位 skill 选择)。
> 状态:**D6 已实施 + sync 完成**,仓库 skills/ 自洽,待审查直接读仓库评判。

## D6 实施(逐条 + 判据)

### D6-1 · 七项编号修正(事实错误)
- `core-principles.md` 第 5 行"**第四项(职责与渐进披露)**" → "**"职责与信息可见性"原则**"(去数字,用名称,防再次漂移);"写时七点约束产物" → "写时约束正式产物"。

### D6-2 · 权限自包含(反向 D2 的"指向矩阵")
- 各 skill 权限行改**自包含**(写全本任务权限,不再指向矩阵找行)。
- `tool-permissions.md` **删 5 任务矩阵**,瘦身为"概念边界 + 外部四条件 + 共同禁止清单 + 子 Agent"(65 → 47 行);任务启动只读本任务 SKILL 权限行,涉及外部访问 / 子 Agent 才读本文件。
- **新建占位 skill**:`prompt-inspection`(17 行)、`prompt-revision`(17 行)——各声明职责 + 自包含权限行 + "主流程待原型化"。
- 指挥官路由"`(原型后)`" → "`(占位)`"。

### D6-3 · 删不存在的 `_shared` 引用(可用性阻断)
- 删 prompt-creation / agent-eval-creation / runtime 的 `knowledge-discovery` / `artifact-boundaries` / `runtime-evidence` / `handoff` 引用(均不存在);改为"启动读 core-principles + 本任务权限行;其余 `_shared/` 尚未建立"。
- 自检:`grep` 运行层**无残留**虚假引用;`references/core-production-gates.md`(core-principles 引用的正式迁移来源)**存在**。

### D6-4 · 七项闭环措辞(去"每项显式产物"暗示)
- "每项必须 分析 → 显式产物 → ..." → "**逐项分析并约束正式产物**;只记录阻断 / 缺失 / 冲突 / 必要追溯,**不强制每项生成独立过程文件**"。

### D6-5 · 测试使用时机
- `tests/README.md` 加"何时运行测试":仅用于新版发布前 / 权限·职责·状态·知识来源规则变更后 / 真实执行暴露新型严重错误后;**不每次生产都跑**。

## 最终运行层状态

| 文件 | 行 | 说明 |
| --- | --- | --- |
| `shared/core-principles.md` | 27 | 纯七项 + 工具授权指向(D1/D6-1/D6-4) |
| `shared/tool-permissions.md` | 47 | 共同清单(删矩阵,D6-2) |
| `skills/produce-agent-prompts/SKILL.md` | 29 | 指挥官路由(inspection/revision 标占位) |
| `skills/prompt-creation/SKILL.md` | 39 | 权限自包含 + 删虚假引用 |
| `skills/agent-eval-creation/SKILL.md` | 42 | 同上 |
| `skills/runtime-integration-validation/SKILL.md` | 53 | 权限自包含 + 删虚假引用 + 报告标注(D4) |
| `skills/prompt-inspection/SKILL.md` | 17 | **新占位** |
| `skills/prompt-revision/SKILL.md` | 17 | **新占位** |

**一次 prompt-creation 执行上下文**:指挥官(29)→ prompt-creation(39)→ core-principles(27)= 约 95 行;权限自包含在 prompt-creation 权限行,**不读 tool-permissions 全文**。符合审查目标最小结构。

## sync 验证

`sync-shared.py sync` + `check`:6 个 skill 的 `_shared/`(core-principles + tool-permissions)全部一致。

## 待审查(用户将让审查直接读仓库)

1. 运行层自洽性(无虚假引用、权限自包含、七项编号正确)。
2. 占位 skill(prompt-inspection / prompt-revision)形式是否合适。
3. "一次任务的最小执行上下文"是否真正达成。
