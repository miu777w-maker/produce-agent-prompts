# 仓库交接 · 新窗口(2026-08-13)

> 用途:新会话/新窗口续接本仓库工作。**自包含**——据此 + 读运行层文件即可接手。
> 上一份交接:38 号(压缩前)。本份更新到 D1–D7 删减 + evals 默认禁读边界之后。

## 一、仓库是什么

`produce-agent-prompts`:**为写 Agent 提示词而生的 skill 仓库**。产出物是 Skill 本身(供 Claude/Codex 加载执行),不是某个业务的 Prompt。

- 路径:`/Users/miumiu777/Desktop/AI work/idiot/produce-agent-prompts`
- 分支:`v0.4-plugin-prototype`(`main` 停在 v0.3)。**当前改动未提交**;安装副本 `~/.claude/skills/` **未同步**(真跑前再同步)。

## 二、当前结构

**运行层**(Agent 执行任务时加载,8 文件):

| 文件 | 行 | 角色 |
| --- | --- | --- |
| `shared/core-principles.md` | 21 | 七项唯一权威 |
| `shared/tool-permissions.md` | 47 | 共同权限清单(无矩阵) |
| `skills/produce-agent-prompts/SKILL.md` | 28 | 指挥官路由 |
| `skills/prompt-creation/SKILL.md` | 39 | 新建 Prompt |
| `skills/agent-eval-creation/SKILL.md` | 42 | 新建/修订 Eval |
| `skills/runtime-integration-validation/SKILL.md` | 51 | 后端运行时校验 |
| `skills/prompt-inspection/SKILL.md` | 19 | **占位·未实现** |
| `skills/prompt-revision/SKILL.md` | 19 | **占位·未实现** |

- 同步:`scripts/sync-shared.py`(`shared/` → 各 skill `_shared/`;`sync` / `check`)。6 skill `_shared/` 一致。
- 验证体系(不进执行上下文):`tests/fixtures/`(7 fixture:ex-01/02/03a/03b/04/05/06)、`development/process-history/`(39–43)。
- 旧:`references/`(v0.3,**不在 v0.4 加载路径**,维持现状,不双轨维护)。

## 三、最近做了什么(删减轮 D1–D7)

起点:审查判断 skill"为保证正确而不断加结构",过度设计风险 4/5。判据:删某规则是否导致 ①范围错 ②内容错 ③越权 ④漏上线风险?都不会→删/降。

- **D1–D5**(40 号):core-principles 工具授权去重;权限行精简;删预建状态机;runtime 状态降级;叫停测试扩展。
- **D6**(41 号):七项编号修正(去数字用名称);权限自包含(删矩阵,各 skill 写全本任务权限);删不存在的 `_shared` 引用;闭环措辞(去"每项显式产物");建 inspection/revision 占位 skill;测试使用时机。
- **D7**(42 号):加载时机统一;必要禁止回写各任务权限行;删未来迁移占位;Prompt Creation 运行环境改"KB 依据不越权";占位 skill 防假可用(触发返回未实现);指挥官移除未实现项 + 外部交接路由;Runtime 标签→"有阻断/无阻断"。
- **evals 默认禁读 Prompt 边界**(用户意见):`agent-eval-creation` 默认**禁止读 Prompt 文件**(即使仓库内有),除非用户明确强力要求;例外时 KB 仍为唯一知识源。

## 四、当前状态(审查第二轮结论)

- **Prompt Creation + Agent Eval Creation:可进真实知识库试运行。**
- **Runtime Validation**:可受控试验(需用户四条件授权后端)。
- **Inspection / Revision:占位未实现**(触发返回"流程未实现",不用通用能力临时完成)。
- 七项:编号正确、清晰,不需增加。
- 运行层自检:无"原型骨架"/旧状态名/未来迁移/虚假 `_shared` 引用残留。

## 五、关键边界/约定(必守)

- 七项是所有任务唯一宪法(`core-principles` 权威);各任务只写"本任务怎么应用",不重述理论。
- 权限**自包含**在各 skill;**启动只读七项 + 本任务权限行**;仅外部访问/子Agent/权限疑点时读 `tool-permissions`。
- **agent-eval-creation 默认禁读 Prompt**(除非用户明确强力要求,且 KB 仍唯一源)。
- 占位 skill 未实现,触发返回未实现;不用通用能力临时完成。
- **不碰真实项目**(资金安全顾问 `legal_advice_prompt`)的 Prompt/Eval/KB/后端代码;不把项目字段(`event`/`event_context`/G1-G3/工具名)写进通用 skill。
- 清单不写成已通过;未经验证不写成既定事实。
- 提交/push 需用户确认(feature branch 可直接 push;`main` 需用户 `!`)。
- 不再加新原则/层/状态机(审查叫停);真实任务暴露缺口时补最小规则,不预告迁入旧体系。

## 六、下一步(候选,按需)

1. **真实知识库试运行** agent-eval-creation(写 evals)/ prompt-creation。
2. commit 当前改动到 `v0.4-plugin-prototype`。
3. 同步安装副本 + Claude/Codex 真跑 EX-01~07(验证测试能抓失败)。
4. 等真正需要时建 inspection/revision 最小流程。

## 七、文档索引

- `39-executable-regression-tests.md`:7 条可执行测试样本(11 字段)+ fixture 约定。
- `tests/fixtures/README.md`:fixture 结构 + 何时运行测试。
- `40-runtime-layer-reduction-and-test-review.md`:D1–D5 报告。
- `41-d6-reduction-implementation.md`:D6 实施。
- `42-d7-closure-implementation.md`:D7 收口(最新运行层状态)。
- `38-handoff-before-context-compaction.md`:上一份交接。
- 外部:`/Users/miumiu777/Desktop/AI work/prd/archives/2026-08-11-system-agent-prompt-production-skill/`(00 原始七项源头、28 v0.2 复盘、29 对照审查)。

## 八、新窗口接手要做的第一件事

读本仓库**运行层 8 文件**(第二节表)+ 本交接。要执行任务时:指挥官路由 → 目标 task skill → `_shared/core-principles.md` + 本任务权限行。
