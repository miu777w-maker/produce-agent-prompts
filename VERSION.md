# Version 0.4.0(试用 / pre-release)

> 状态:**试用版(pre-release)**。可进入真实任务试运行,**不宜标记为稳定发布版**。
> 主语言变更:本版起 VERSION.md 改用中文,与运行层 / 过程历史一致(v0.3 为英文)。

## Readiness(就绪度,如实)

- **Prompt Creation**:可真实知识库试运行;未端到端验证。
- **Agent Eval Creation**:可真实知识库试运行;**默认禁读 Prompt**;未端到端验证。
- **Runtime Integration Validation**:原型,可受控试验(需用户四条件授权后端);未真跑。
- **Prompt Inspection / Prompt Revision**:**占位未实现**(触发返回"流程未实现",不用通用能力临时完成)。
- **测试**:7 条可执行 fixture(EX-01 / 02 / 03a / 03b / 04 / 05 / 06)就位,**尚未执行**。
- **七项宪法**:编号已修正、清晰,为所有任务唯一宪法;不需增加。

## v0.4 主要变化(相对 v0.3 单 skill + references)

- **架构**:从单 skill + 7 references → **plugin 多 skill + 三层结构**。
  - 多 skill:指挥官(`produce-agent-prompts`)+ 3 任务 skill(`prompt-creation` / `agent-eval-creation` / `runtime-integration-validation`)+ 2 占位(`prompt-inspection` / `prompt-revision`,未实现)。
  - 三层:提示词层(`shared/core-principles.md` 七项权威)/ 执行策略层(各 `SKILL.md` 主流程)/ 工具授权层(`shared/tool-permissions.md` 共同清单)。
- **Prompt / Eval 独立生产**:两条独立流程,各自从知识库推导;阶段同步 ≠ 生产绑定。
- **权限自包含**:各 skill 写全本任务权限;**启动只读七项 + 本任务权限行**;仅外部访问 / 子 Agent / 权限疑点时读共同协议。
- **agent-eval-creation 默认禁读 Prompt**:即使仓库内有 prompts 目录 / 文件也不主动读,除非用户明确强力要求(此时 KB 仍为唯一知识源)。
- **删减轮 D1–D7**(依据审查"删比加重要"):去重复概念定义、删预建状态机、删未来迁移占位、删不存在的 `_shared` 引用、占位 skill 防假可用、Runtime 报告标注"有阻断 / 无阻断"(去状态机形式)。
- **同步机制**:`scripts/sync-shared.py`(`shared/` → 各 skill `_shared/`;`sync` / `check`)。
- **可执行测试**:`tests/fixtures/` 7 fixture(11 字段、二元判据、通用场景,不写死项目字段)。

## 不在 v0.4(维持现状 / 不预建)

- `references/`(v0.3 旧,**不在 v0.4 加载路径**,不双轨维护)。
- 旧四态状态机(已删 / 降级为报告标注)。
- 不全量迁移旧 references 判据(真实缺口出现时补最小规则,不预告迁入旧体系)。
- 不新增原则 / 层 / 状态机(审查叫停)。

## Evidence

- 删减与测试:`development/process-history/39-executable-regression-tests.md` ~ `42-d7-closure-implementation.md`。
- 仓库交接(最新):`development/process-history/43-repo-handoff-new-window.md`。
- 上一份交接:`38-handoff-before-context-compaction.md`。
- v0.3 基线:外部 archives `29-v0-3-revision-checkpoint.md`。
