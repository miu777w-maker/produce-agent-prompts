# Produce Agent Prompts:Plugin 多 skill 拆分方案(提案,待审查)

> 日期:2026-08-12  
> 状态:**提案,未实施,未修改任何运行 skill 文件(SKILL.md / references/ / scripts/)**。  
> 依据:审查 agent 的渐进式披露意见 + 用户"SKILL.md 只做指挥官、按执行方式拆成不同 skill"指示 + cowork 插件范式。

## 一、背景与依据

审查 agent 指出:当前 references 是**按主题横切**(门禁/检索/架构/校验/模板/工作流),一个 Prompt Creation 任务要跨读 6 个横切文件才能拼出完整执行方式;这是"路由到主题"而非"路由到执行方式",是渐进式披露没做好的结构性根因。

用户指示:把不同执行方式拆成不同 skill,SKILL.md 只做指挥官;并认可 cowork 插件"一个仓库含多个 skill、skill 间可互相调用"的范式。

cowork 实际结构(已核查 `~/.claude/plugins/marketplaces/idiot-cowork/cowork/`):一个 plugin = `.claude-plugin/plugin.json` + `skills/` 下多个独立 skill 目录;每个 skill 自包含(SKILL.md + 专属 references + scripts);**无 plugin 级 shared 目录**;共享靠符号链接(如 `clarify-production/ADR-FORMAT.md@ → grill-with-docs/ADR-FORMAT.md`)和文字引用其他 skill 路径。

本方案目标:把 produce-agent-prompts 从"单 skill + 横切 references"重构为"plugin + 指挥官 skill + 按执行方式纵切的子 skill + plugin 级 shared",使路由直接命中一个自包含执行单元,实现渐进式披露在任务路由层的彻底化。

## 二、范式选择

**plugin + 多 skill + 指挥官**(对标 cowork,叠加指挥官):

- 一个指挥官 skill `orchestrate` 负责**任务路由 + 共享设计原则概要**(轻量)。
- 每个执行方式是一个**独立子 skill**,自包含,路由命中时才加载。
- 横切共享协议放 **plugin 级 `shared/`**,各 skill 引用(相对路径,显式可移植;不走符号链接,理由见 §八)。
- plugin.json 声明元数据。

与纯 cowork 式(去中心、无指挥官)的区别:保留指挥官,因为五个流程共享大量概念(七项门禁、知识发现、文件边界、Prompt/Eval 分离、渐进披露),指挥官能保证共享原则一致传达、并在用户不确定时帮选流程;同时每个子 skill 也自描述触发条件、可独立调用(兼顾 cowork 的去中心优点)。

## 三、目标结构

```text
produce-agent-prompts/                 # 仓库 = plugin 根
  .claude-plugin/plugin.json           # plugin 清单(name/version/description)
  VERSION.md                           # 仓库根,维护者用
  development/                         # 仓库根,维护者用(不进任何 skill)
  scripts/
    validate_prompt_package.py         # plugin 级校验脚本,各 skill 引用
  shared/                              # plugin 级横切共享协议
    progressive-disclosure.md          # 渐进式披露原则(四层 + 反过来约束 Skill 自己 + 三件事判据)
    gates.md                           # 七项核心门禁(含信息可见性硬核对)
    knowledge.md                       # 定向检索与停止协议
    file-boundary.md                   # 文件边界与命名协议
    runtime-honesty.md                 # 运行时证据不足分级 + 诚实状态
    handoff-conventions.md             # 知识补全 / 工程取证 / 外部评测交接通用约定
  skills/
    orchestrate/                       # 指挥官(默认入口)
      SKILL.md
    prompt-creation/
      SKILL.md
      templates/                       # prompt-production-basis / prompt-unit / prompt-static-check
    eval-creation/
      SKILL.md
      templates/                       # eval-scenario / eval-production-basis / external-handoff
    prompt-inspection/
      SKILL.md
      templates/                       # inspection-report
    prompt-revision/
      SKILL.md
```

## 四、每个 skill 的职责与 SKILL.md 大纲

### orchestrate(指挥官,默认入口)

- 职责:任务路由 + 共享设计原则入口。**不含任何流程执行细节**。
- SKILL.md 大纲:
  - 保持边界(总纲);
  - 渐进式披露原则(概要,详见 `shared/progressive-disclosure.md`);
  - 关键概念:阶段同步 ≠ 生产绑定;
  - 选择任务流程:路由到 4 个子 skill(prompt-creation / eval-creation / prompt-inspection / prompt-revision);外部评测交接挂在 eval-creation 之后,不是独立 skill;
  - 共享原则清单(指向 `shared/*`):门禁、检索、文件边界、诚实状态、交接约定;
  - 何时用哪个 skill 的决策指引 + 每个子 skill 的触发条件摘要。

### prompt-creation

- 职责:新建 prompt 体系;**不产 eval、不产外部交接**。
- SKILL.md 大纲:
  - 五步最小闭环主线 + 五步↔八阶段映射;
  - 八阶段详细(产物 / 进入退出条件 / 确认点);
  - 引用 `shared/gates.md`(七项门禁约束)、`shared/knowledge.md`、`shared/file-boundary.md`、`shared/runtime-honesty.md`;
  - 引用本 skill `templates/`(prompt-production-basis、prompt-unit、prompt-static-check);
  - 最小交付 + 按需追加(Prompt 侧)。

### eval-creation

- 职责:从知识库独立推导,评测**完整 Agent 业务行为**(非 prompt 文件);不改 prompt。
- SKILL.md 大纲:
  - 被测对象 = 完整 Agent 业务行为;独立推导;不以 prompt 为知识源;无 `eval → prompt` 依赖;
  - Eval Creation 阶段(E1–E7);
  - 行为案例设计(失败面:正常/边界/模糊/冲突/缺失/工具/对抗/长对话/组合/上下游);
  - 引用 `shared/knowledge.md`、`shared/runtime-honesty.md`、`shared/handoff-conventions.md`;
  - 引用本 skill `templates/`(eval-scenario、eval-production-basis、external-handoff);
  - 最小交付(Eval 侧);外部评测交接仅在 eval 就绪时生成。

### prompt-inspection

- 职责:检验已有 prompt 体系;只报告不修改。
- SKILL.md 大纲:
  - 目标与范围、必读资源、检验步骤、归因、七项门禁的 Inspection 视角、已有 eval 审查(范围含 eval 时)、状态汇聚;
  - 引用 `shared/gates.md`、`shared/knowledge.md`、`shared/file-boundary.md`、`shared/runtime-honesty.md`;
  - 引用本 skill `templates/`(inspection-report)。

### prompt-revision

- 职责:改写已有 prompt 体系,形成可回退新版本;不产 eval。
- SKILL.md 大纲:
  - 归因与影响分析、授权确认、只改受影响内容、新版本/差异/回退;
  - 变化驱动影响分析(知识/需求 → 执行单元 → prompt 规则 → 运行时契约);
  - 引用 `shared/*`(同 inspection)。

## 五、shared/ 共享协议归属

| shared 文件 | 内容来源(现有) | 被哪些 skill 引用 |
| --- | --- | --- |
| progressive-disclosure.md | 新写(审查 agent 原则) | 全部 |
| gates.md | `core-production-gates.md`(七项门禁 + 信息可见性硬核对) | prompt-creation、prompt-inspection、prompt-revision |
| knowledge.md | `knowledge-discovery-and-gaps.md`(定向检索与停止) | 全部 |
| file-boundary.md | `prompt-architecture-and-runtime.md` 的"文件边界与命名协议"节 | prompt-creation、prompt-inspection、prompt-revision |
| runtime-honesty.md | `validation-and-external-handoff.md` 的"运行时证据不足" + 状态分级 | 全部 |
| handoff-conventions.md | 知识补全 / 工程取证 / 外部评测交接通用约定 | eval-creation、prompt-creation(按需追加) |

引用方式:相对路径文字引用(如 `shared/gates.md`、`../shared/gates.md`),显式可移植。不走符号链接(理由见 §八-2)。

## 六、从现有结构的迁移映射

| 现有文件 | 去向 |
| --- | --- |
| `SKILL.md` | → `skills/orchestrate/SKILL.md`(精简为指挥官)+ `shared/progressive-disclosure.md` |
| `task-protocols.md` | 拆分:Inspection→prompt-inspection;Creation→prompt-creation;Revision→prompt-revision;Eval Creation→eval-creation;交接→`shared/handoff-conventions.md` |
| `workflow-and-state.md` | 八阶段→prompt-creation;Eval 阶段→eval-creation;确认点/状态/中断→各 skill + `shared/runtime-honesty.md` |
| `core-production-gates.md` | → `shared/gates.md` |
| `knowledge-discovery-and-gaps.md` | → `shared/knowledge.md` |
| `prompt-architecture-and-runtime.md` | 文件边界节→`shared/file-boundary.md`;执行单元地图/运行时契约/职责矩阵→prompt-creation(inspection/revision 引用);变化驱动影响分析→prompt-revision |
| `validation-and-external-handoff.md` | 运行时证据/状态→`shared/runtime-honesty.md`;行为案例设计→eval-creation;外部交接→`shared/handoff-conventions.md`;静态集成→各 skill |
| `artifact-templates.md` | 按流程拆:模板1目标确认→orchestrate;2 inspection→prompt-inspection;6 门禁→`shared/gates.md`;7/8/15/16→prompt-creation templates;9/17/11→eval-creation templates;10 运行时契约→`shared/`;13 最终交付→各 skill;14 manifest→`scripts/` 引用 |
| `scripts/validate_prompt_package.py` | → `scripts/`(plugin 级,不变) |
| `VERSION.md`、`development/` | 保留仓库根 |

## 七、触发方式变化

- 现:`/produce-agent-prompts` 触发单个 skill。
- 新:plugin 安装后——
  - `/produce-agent-prompts`(指挥官 orchestrate)→ 路由到子 skill;或
  - 直接 `/prompt-creation`、`/eval-creation`、`/prompt-inspection`、`/prompt-revision`(对标 cowork 每个 skill 可独立触发)。
- 指挥官 SKILL.md 的 description 引导选流程;每个子 skill 的 description 自描述触发条件(对标 cowork)。
- **未决**:plugin 名与指挥官 skill 名是否都用 `produce-agent-prompts`(保留用户习惯),需确认(见 §九-5)。

## 八、取舍与风险

1. **指挥官 vs 去中心**:保留指挥官(符合用户诉求)+ 子 skill 自描述独立触发(对标 cowork)。代价:共享原则在指挥官有概要、在 shared 有详述,轻微重复,用"概要 + 详见 shared"控制。
2. **shared 引用:相对路径 vs 符号链接**:cowork 用符号链接;本方案推荐**相对路径文字引用**(更显式、可移植、不依赖文件系统;符号链接在某些部署/Windows 下不稳定)。这是审查点。
3. **plugin 安装迁移**:仓库要加 `.claude-plugin/plugin.json`;安装从"复制单 skill"变"plugin 安装";`~/.claude/skills/` 同步方式要调整为 plugin 安装路径。迁移成本中等。
4. **横切→纵切重组工作量**:需逐文件按 §六迁移,避免信息丢失或重复。实施时按"先建 shared → 再建各 skill → 再迁移内容 → 再删旧 references → 回归"的顺序,保证可回退。
5. **无 plugin 级 shared 的纯 cowork 式**:本方案选择加 `shared/`(比 cowork 多一层),因为本 skill 的横切协议(七项门禁等)体量大、被多 skill 引用,plugin 级 shared 比符号链接到某个 skill 内更清晰。这也是审查点。

## 九、请审查 agent 重点审查的点

1. 指挥官 + 四个子 skill 的职责边界是否清晰,有无重叠或遗漏;外部评测交接不作为独立 skill 而挂在 eval-creation 之后是否合理。
2. `shared/` 的切分是否合理:哪些是真正横切共享(应进 shared),哪些应留在具体 skill 内(不共享)。
3. §六迁移映射有无信息丢失:现有 references 的每段内容是否都有明确去向。
4. 引用方式选择(相对路径 vs 符号链接)。
5. 触发体验:指挥官路由 + 子 skill 独立触发的命名与 plugin 名是否冲突;`produce-agent-prompts` 名字保留策略。
6. 是否过度:指挥官 + shared + 子 skill 三层是否比"纯 cowork 去中心式"更重,是否可进一步精简。

## 十、实施前置条件

本提案审查通过后,再制定分步实施计划(建 plugin 骨架 → 迁移 shared → 迁移各 skill → 删旧 references → 静态回归 → 同步安装)。实施前再次确认 §九 的未决项。
