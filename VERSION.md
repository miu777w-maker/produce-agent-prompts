# Version 0.5.0(试用 / pre-release)

> 状态:**试用版(pre-release)**。可进入真实任务试运行,**不宜标记为稳定发布版**。

## v0.5 主要变化(相对 v0.4:分层加载改造,参考 cowork)

- **删除指挥官 skill**(`produce-agent-prompts` 路由层):各任务 skill 直连使用,靠 frontmatter description 原生路由,一次任务只加载一份 SKILL.md(此前指挥官 + 任务 skill 至少 2 次加载)。
- **marketplace + plugin 结构**:仓库根为 marketplace(`.claude-plugin/marketplace.json`),实际分发 bundle 在 `plugin/`;安装改走 `/plugin marketplace add` + `/plugin install`,不再 rsync 散装副本。
- **单源 shared**:`core-principles.md` / `tool-permissions.md` 只在 `plugin/shared/` 一份,各 skill 经 `${CLAUDE_PLUGIN_ROOT}` 引用;删除 7 份 `_shared/` 副本与 `sync-shared.py`。
- **guard reminder(压缩存活)**:4 个已实现 skill 各配 UserPromptSubmit hook(`scripts/guard-principles.sh`),每轮注入压缩版要点(七项 + 流程摘要 + 权限行),上下文压缩后仍生效,不重载 SKILL.md;占位 skill 不配。
- **保留**:`scripts/validate_prompt_package.py`(产物 manifest 校验,与加载架构无关);宪法原则与各 skill 生产方法不变。

## Readiness(就绪度,如实)

- **Prompt Creation**:可真实知识库试运行;未端到端验证。
- **Agent Eval Creation**:可真实知识库试运行;**默认禁读 Prompt**;未端到端验证。
- **Agent Rubric Creation**:待首次真实试运行。
- **Runtime Integration Validation**:原型,可受控试验(需用户四条件授权后端);未真跑。
- **Prompt Inspection / Prompt Revision**:**占位未实现**(触发返回"流程未实现",不用通用能力临时完成)。
- **guard hooks**:4 个脚本过语法与输出结构测试;未在真实长会话压缩场景下验证。
- **七项宪法**:编号已修正、清晰,为所有任务唯一宪法;不需增加。

## v0.4 主要变化(相对 v0.3 单 skill + references)

- **架构**:从单 skill + 7 references → plugin 多 skill + 三层结构(提示词层 / 执行策略层 / 工具授权层)。
- **Prompt / Eval 独立生产**:两条独立流程,各自从知识库推导;阶段同步 ≠ 生产绑定。
- **权限自包含**:各 skill 写全本任务权限;**启动只读七项 + 本任务权限行**。
- **agent-eval-creation 默认禁读 Prompt**:即使仓库内有 prompts 目录 / 文件也不主动读,除非用户明确强力要求(此时 KB 仍为唯一知识源)。
- **删减轮 D1–D7**(依据审查"删比加重要")。
- **可执行测试**:`tests/fixtures/` 7 fixture(11 字段、二元判据、通用场景,不写死项目字段)。

## 不在 v0.5(维持现状 / 不预建)

- `references/`(v0.3 旧,**不在加载路径**,不双轨维护)。
- 旧四态状态机(已删 / 降级为报告标注)。
- 不新增原则 / 层 / 状态机。
- 指挥官式显式路由入口(已删;README 路由表供人查阅,Claude Code 原生路由)。

## Evidence

- 删减与测试:`development/process-history/39-executable-regression-tests.md` ~ `42-d7-closure-implementation.md`(archive 分支)。
- 仓库交接(最新):`development/process-history/43-repo-handoff-new-window.md`(archive 分支)。
- v0.3 基线:外部 archives `29-v0-3-revision-checkpoint.md`。
