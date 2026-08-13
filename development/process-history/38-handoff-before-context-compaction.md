# 任务交接(上下文压缩前)

> 日期:2026-08-13  
> 用途:上下文压缩 / 新会话续接。**自包含**——据此可继续,不必重读全部历史。

## 一、仓库与分支状态

- 仓库:`/Users/miumiu777/Desktop/AI work/idiot/produce-agent-prompts`
- 当前分支:`v0.4-plugin-prototype`(`main` 停在 v0.3 `1417742` + 提案 `9a6ccf6`;v0.4 原型基线 `ba106aa`)
- **未提交增量**(7 改 + 9 新):33–37 号文档、`shared/tool-permissions.md`、`skills/runtime-integration-validation/`、`shared/core-principles.md` 概念边界节、三 task skill 权限行、各 `_shared/` 同步、指挥官 description/路由
- 远端:`origin/v0.4-plugin-prototype` 停在 `ba106aa`,**本轮增量未 push**
- 安装副本:`~/.claude/skills/` = v0.4 四 skill(指挥官 / prompt-creation / agent-eval-creation / runtime-integration-validation),各含 `_shared/core-principles.md` + `_shared/tool-permissions.md`

## 二、当前结构(v0.4 三层原型,已实施)

- **提示词层**:`shared/core-principles.md`(七项宪法 + 工具授权概念边界 + 启动前必读)
- **执行策略层**:各 `skills/<task>/SKILL.md` 主流程(指挥官 / prompt-creation / agent-eval-creation / runtime-integration-validation 已建;**inspection / revision 未建**)
- **工具使用与授权层**:`shared/tool-permissions.md`(5 任务矩阵 + 外部访问四条件 + 禁止清单 + 逻辑授权/技术能力/技术限制区分 + 子 Agent 默认禁+授权例外)
- 同步:`scripts/sync-shared.py`(`shared/` → 各 skill `_shared/`,`check` 防漂移)
- 已实证:Claude 发现四 skill(系统 skill 列表)、sync 一致、权限行 + 启动读 + 指挥官路由齐全

## 三、最新审查结论(37 号 4.1/5,作可执行测试仅 2.8/5)

- **37 号是"回归需求清单",不是"已执行回归测试"**。不得把"清单写出"记录为"回归通过"。
- 三个必补:
  1. 每条缺 11 字段(场景编号 / 适用 Skill / 前置材料 / 用户请求 / 允许访问范围 / 预期动作 / 预期产物 / 禁止行为 / 通过条件 / 失败条件 / 证据位置)→ 转可执行测试场景。
  2. 原始七项覆盖偏科,补 6 类:①目标反推清单(不只照单)②角色/目标/边界缺失阻断 ③运行时输入缺失禁写假定 ④概念 KB 有但执行不可见报错 ⑤Anchor 无必要或无装配位置不创建 ⑥当前任务不加载其他流程与无关知识。
  3. `validation-passed` 混了"完成"与"通过"→ 分 `validation-completed-with-blockers` / `validation-passed`(无未解决阻断)/ `final-runtime-prompt`(人工删元信息后)。
- **纠偏:停止加原则/层,转向可执行测试。**

## 四、下一步任务(优先级,**均未开始**)

**P0**
1. 修正 validation 定义:`runtime-integration-validation/SKILL.md` + 37 号第 25 条 → `validation-completed-with-blockers` / `validation-passed` / `final-runtime-prompt`。
2. 把 37 号最高风险条目转**可执行测试样本**(5–6 条,11 字段)。候选:层 4 system/task 冲突、外部仓库无授权访问、Eval 独立非 1:1、Runtime 只读不改、validation 状态区分。先小批给审查 agent 评"是否真能执行、能否稳定判通过/失败"。

**P1**
3. 补七项 6 类场景(转可执行样本)。
4. inspection / revision 原型(复检现有 Prompt 需要;矩阵已列权限行)。

**P2(暂缓)**
- 正式迁移旧 `references/`(等可执行测试 + Codex 实测通过)。
- 四态机器状态机(等首次 runtime 真实执行后定)。
- Codex 实测(待用户:独立装 skill + 读 `_shared/` + 权限协议)。

## 五、边界守恒(必须遵守)

- **不加新原则/层**(审查叫停);转向可执行测试。
- 不全量迁移旧 `references/`、不删旧结构。
- 不改资金安全顾问项目 Prompt / Eval / KB / 后端代码。
- 不把项目字段(`event`/`event_context`/G1-G3/工具名)写进通用 Skill。
- 未经验证方案不写成既定事实;**清单不写成已通过**。
- 提交/push 需用户确认(feature branch 可直接 push;`main` 需用户 `!`)。
- 外部仓库访问需用户四条件授权;不主动访问后端。

## 六、已确认关键决策(不再重议)

- Agent = 提示词 + 执行策略 + 工具及其范畴 → Skill 三层。
- 七项是所有任务唯一宪法;各任务七项映射不同。
- Prompt/Eval 独立生产(阶段同步 ≠ 生产绑定)。
- KB 环境(应该怎样)vs 后端环境(实际怎样),互不替代/覆盖。
- "工具使用与授权协议":Skill 规定**逻辑授权**,不冒充系统权限(技术能力/限制由宿主)。
- 第五 skill `runtime-integration-validation`:只读只报告;不吞并 Inspection;不重审角色/业务/语气/产品。
- 元信息生命周期:生产/审查/修订/后端校验期保留,定稿人工删,Skill 不擅删;"进入模型"是实验变量非错误。
- 代码证"当前实际",KB 证"预期设计",差异归因四类,不自动覆盖。
- 职责声明禁对冲 system 冲突(冲突须修架构/装配)。
- 状态两态 + blockers 区分;不引入四套机器状态(首次执行后再定)。
- 精简判据 5 条(含"上线前能逐项对照后端真实实现");生产期元信息不属无用复杂度。

## 七、文档索引

- 本仓库 `development/process-history/`:30 初稿 / 31 v2 / 32 审查修正+原型计划 / 33 走查吸收 / 34 暂停恢复 / 35 三层结构 / 36 工具权限层实施 / 37 回归清单 / **38 本交接**
- 外部:`29-skill-vs-semantic-prompt-generation-review.md`(对照审查)、`28-...-handoff.md`(v0.2 复盘)、`00-original-task-input.md`(原始七项源头)——均在 `/Users/miumiu777/Desktop/AI work/prd/archives/2026-08-11-system-agent-prompt-production-skill/`
- 项目实证:`legal_advice_prompt/对照审查交接报告.md`(Skill 版)、`legal_advice_prompt/prompts_handcraft/对照审查交接报告.md`(直接语义版)、`legal_advice_prompt/Prompt修订报告_第二轮.md`(后端取证)

## 八、压缩前可选动作

- 工作区增量(33–37 + 实施)压缩后仍在(压缩只丢上下文,不丢文件)。
- 若想保险,可先 wip commit 到 v0.4 分支(不 push),保存进度;否则保持工作区即可。
