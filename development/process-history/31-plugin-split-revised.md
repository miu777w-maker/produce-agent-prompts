# Produce Agent Prompts:Plugin 多 skill 拆分方案 v2(吸收审查意见)

> 日期:2026-08-12  
> 状态:**修订提案,未实施,未修改任何运行 skill 文件**。  
> 依据:`30-proposed-plugin-split.md`(初稿)+ 审查 agent 意见(3.5/5,三项 5 分必改)。  
> 目标:落实三项必改与高分建议,升至 4.5/5 后进入实施。

## 一、审查结论与本次修订重点

审查认定拆分方向正确,但有两条旧惯性:① 把横切规则拆成更多共享文件;② 把原有完整流程原样迁入子 skill。本次修订围绕三项 5 分必改:

1. **七项成为所有任务 skill 共同引用的唯一宪法**,每个子 skill 建立自己的执行映射(含 Eval Creation——不能因不产 Prompt 就跳过七项);
2. **Prompt Creation 只保留一套最小主流程**,不再五步 + 八阶段映射 + 八阶段详细并存;
3. **明确 Claude Plugin 与 Codex/其他环境的打包、安装、共享读取契约**,解决"子 skill 独立安装"与"依赖仓库外 shared"的冲突。

并吸收高分建议:`progressive-disclosure` 并入 `core-principles`;`file-boundary` → `artifact-boundaries`;`eval-creation` → `agent-eval-creation`;外部交接条件生成;`handoff` 按需;八阶段移出正式 skill;相对路径修正。

## 二、精简结构(采用审查建议)

```text
produce-agent-prompts/                 # 仓库 = plugin 根
  .claude-plugin/plugin.json           # plugin 清单(Claude 端整包安装用)
  VERSION.md
  development/                         # 维护者区,含旧八阶段迁移参考
  scripts/
    validate_prompt_package.py         # plugin 级校验
    sync-shared.py                     # 发布同步脚本(见 §五)
  shared/                              # 源端单一权威,运行时靠发布同步或 plugin 整包
    core-principles.md                 # 七项唯一权威定义(含"七项反约束 Skill 自身")
    knowledge-discovery.md             # 定向检索与停止协议
    artifact-boundaries.md             # 任务/单元/载体/物理文件/目录边界与命名
    runtime-evidence.md                # 运行时证据分级 + 诚实状态
    handoff.md                         # 知识补全/工程取证/外部交接(仅按需)
  skills/
    produce-agent-prompts/SKILL.md     # 指挥官:只路由
    prompt-creation/(SKILL.md, templates/)
    agent-eval-creation/(SKILL.md, templates/)
    prompt-inspection/(SKILL.md, templates/)
    prompt-revision/(SKILL.md, templates/)
```

相比 30 号初稿:`progressive-disclosure.md` 并入 `core-principles.md`;`gates.md` → `core-principles.md`;`file-boundary.md` → `artifact-boundaries.md`;`runtime-honesty.md` → `runtime-evidence.md`;`handoff-conventions.md` → `handoff.md`;`eval-creation` → `agent-eval-creation`;指挥官 skill 与 plugin 同名 `produce-agent-prompts`(保留触发习惯)。

## 三、修正 1:七项作为唯一宪法 + 各 skill 执行映射

### 3.1 `shared/core-principles.md` 是七项的唯一权威定义

七项定义只在此文件出现一次。内容包括:每项的"生产前获取 / 显式产物 / 对正式产物的约束 / 失败条件 / 倒查",以及一条自反条款——

> **第四项(职责与渐进披露)反过来约束 Skill 自身**:Skill 也不加载当前任务用不到的流程、规则、知识和文件。删掉任意一条 Skill 规则,若不影响"写前找对范围 / 写时七点约束产物 / 写完发现错误并停止",即可精简。

(此条款即原 `progressive-disclosure.md` 的内容,并入第四项,不再单独成文。)

### 3.2 每个任务 skill 提供自己的七项执行映射(不复制正文)

四个任务 skill 都遵循七项,但映射不同。各 skill 的 SKILL.md 含一张"本流程的七项映射"表,指向 `core-principles.md` 的权威定义。

**prompt-creation 的七项映射**

| 七项 | 在本流程的具体执行 |
| --- | --- |
| 需求先行 | 目标 Agent/执行单元、范围、不可改变要求、清单来源(人员给定/目标驱动) |
| 运行环境 | prompt 声明的工具/消息/状态/输出/异常在运行时是否真实可见 |
| 上下文绑定 | prompt 中术语/概念在执行时机是否有真实注入来源 |
| 业务背景 | 角色/目标/边界/语气是否忠实知识库 |
| 职责与渐进披露 | 每个执行单元是否只看到必需信息;职责是否唯一;共享底座是否吞并局部细节 |
| 关键约束位置 | 高风险规则是否在有效载体/时机;anchor/reminder 是否有真实钩子和必要性 |
| 知识错误 | prompt 是否误读/漂移/引入无来源规则 |

**agent-eval-creation 的七项映射**

| 七项 | 在本流程的具体执行 |
| --- | --- |
| 需求先行 | 评测什么 Agent、哪些能力、哪些场景;被测对象是完整 Agent 业务行为 |
| 运行环境 | Agent 在评测环境中会收到什么(消息/状态/工具/历史) |
| 上下文绑定 | 测试场景提供的状态是否足以支撑判定 |
| 业务背景 | 正确行为来自哪些知识(独立追溯,不以 prompt 为源) |
| 职责与渐进披露 | 评测场景是否重复、遗漏或越界;场景数来自业务而非 prompt 数 |
| 关键约束位置 | 是否覆盖高风险、边界和对抗用例;一票否决是否只用于破坏正确性/安全/运行契约 |
| 知识错误 | 评测标准是否存在冲突;与 prompt 理解不同时是否标记而非迁就 |

**prompt-inspection 的七项映射**

| 七项 | 在本流程的具体执行 |
| --- | --- |
| 需求先行 | 应有清单是否从知识库正确推导;是否把现有文件列表误当作正确范围 |
| 运行环境 | 现有 prompt 依赖的消息/工具/输出是否有运行时证据 |
| 上下文绑定 | 每个指代/字段在目标调用时机是否真实可见 |
| 业务背景 | 身份/目标/边界是否忠实知识库,保留非最终/例外 |
| 职责与可见性 | 应有清单是否完整,职责是否错位/重叠,局部 Agent 是否读无关信息 |
| 关键约束 | 高风险约束是否在有效载体;anchor 是否有钩子+必要性+漂移测试 |
| 知识错误 | 现有 prompt 是否误读/漂移/无来源;eval(若在范围)是否独立可追溯 |

**prompt-revision 的七项映射**

| 七项 | 在本流程的具体执行 |
| --- | --- |
| 需求先行 | 变更目标/授权/影响范围;回归到最早受影响阶段 |
| 运行环境 | 变更是否影响运行时契约(工具/消息/状态/输出/异常) |
| 上下文绑定 | 变更是否破坏概念绑定与注入来源 |
| 业务背景 | 变更是否忠实知识库,不新增无来源身份/承诺 |
| 职责与可见性 | 变更是否破坏职责矩阵与最小可见信息 |
| 关键约束 | 变更是否影响 anchor/约束位置及其运行时钩子 |
| 知识错误 | 变更是否引入冲突或漂移;prompt 与 eval 各自是否需同步 |

## 四、修正 2:Prompt Creation 只保留一套最小主流程

正式 skill 中**只保留一套**对执行 Agent 可见的主流程:

1. 明确目标与范围(含清单来源);
2. 定向检索并形成正式文件清单;
3. 按七项形成文件约束;
4. 逐文件生成(不私自命名/合并/多造;不产当前任务外的 eval 或交接);
5. 按七项及必要性倒查交付(含信息可见性核对与"预期↔实际"文件核对)。

旧八阶段**不进入正式 skill**。它的阶段产物/状态/确认点细节中,仍有效的部分拆入上述五步或 `shared/`;完整八阶段作为版本迁移与开发者参考,留在 `development/`(如 `development/legacy-eight-stage-reference.md`),执行 Agent 不读。

(确认点硬门、知识补全分支、中断恢复等仍保留,但挂在五步的相应步骤上,不再独立编号为"阶段 N"。)

## 五、修正 3:可移植契约(打包 / 安装 / 共享读取)

### 5.1 核心矛盾

"子 skill 独立安装"与"依赖仓库根 `shared/`"冲突:若只复制 `skills/prompt-creation/`,shared 丢失;且不能假设所有宿主允许 skill 读取自身目录外的 `../../shared/`。

### 5.2 契约:源端单一权威 + 发布同步自包含

- **源仓库**:`shared/` 是七项等横切协议的**单一权威**。各 skill 的 SKILL.md 用相对路径引用(`../../shared/core-principles.md`),仅供开发与审查阅读,不作为跨环境运行时依赖。
- **发布同步**:`scripts/sync-shared.py` 在发布前把 `shared/` 内容同步进每个 skill 目录内的 `_shared/`(或按需内联),生成**自包含**的发布 skill。发布后的单 skill 可在任意宿主独立安装,不依赖仓库根,不需越过 skill 目录读资源。
- **Claude 端(一等)**:额外提供 `.claude-plugin/plugin.json`,支持**整包安装**——此时 `shared/` 在 plugin 根,skill 直接引用(类似 cowork 用符号链接在 skill 间共享),无需同步。Claude 端两种方式都支持:开发/完整用整包 plugin;分发用同步后的自包含单 skill。
- **Codex / 其他环境**:用发布同步后的自包含 skill 安装。源端 `shared/` 保持单一权威,避免多份漂移。
- **相对路径修正**:源端引用写作 `../../shared/core-principles.md`(skill 在 `skills/<name>/`,shared 在仓库根,上两级;30 号初稿误写成 `../shared/`)。发布同步后,运行时引用变为 `_shared/core-principles.md`(skill 内),不再越目录。

### 5.3 待验证(实施前必须实测)

- Codex 的 skill/agent 安装机制:是否支持自包含 skill 目录;是否需要特定清单格式。
- `sync-shared.py` 的同步策略(整体复制 `_shared/` 子目录 vs 按引用内联)与冲突处理。
- Claude Plugin 整包安装时,skill 引用 plugin 根 `shared/` 的实际可用性(参照 cowork 符号链接先例验证)。

若实测发现某环境既不支持 plugin 整包、也不支持 skill 内子目录引用,则退化为"每个 skill 内联必需 shared 内容 + 构建期一致性检查"——仍保证单一权威(源端)与可移植(发布端)。

## 六、shared 按需读取(防止 shared 变成新横切负担)

拆出 shared 不自动等于渐进式披露。每个任务 skill 必须明确"何时读哪个 shared",启动时不全读:

| 时机 | 读取的 shared |
| --- | --- |
| 启动 | `core-principles.md`(七项概要 + 自反条款) |
| 确定知识范围/检索 | `knowledge-discovery.md` |
| 确定文件/任务/载体清单 | `artifact-boundaries.md` |
| 处理运行时证据缺口 | `runtime-evidence.md` |
| 确有跨责任方交接需求(按需) | `handoff.md` |

`handoff.md` 默认不读。缺口能在当前任务内解决时不生成独立交接文件;只有跨人员/跨 Agent/跨环境才读 `handoff.md` 并生成对应文件。

## 七、其他修正

- **命名**:`core-principles.md`(七项唯一权威,含渐进披露自反条款)、`artifact-boundaries.md`(管任务/单元/载体/物理文件/目录,不只文件)、`agent-eval-creation`(明确评测对象是完整 Agent)、`runtime-evidence.md`、`handoff.md`。
- **外部评测交接**:作为 agent-eval-creation 的**条件产物**,不默认生成。仅当 eval 已完成 + 已知评测环境/接收方 + 用户准备进入实际评测 + 交接文件有明确消费者时才生成。未来若"设计 eval"与"组织执行"频繁由不同人负责,可再拆第五个 skill;现在不提前拆。
- **三类交接不默认生成**:知识补全、工程取证、外部交接都按需;缺口能在任务内解决时不落独立文件。
- **八阶段移出正式 skill**:见 §四。

## 八、迁移映射(更新)

| 现有文件 | 去向 |
| --- | --- |
| `SKILL.md` | → `skills/produce-agent-prompts/SKILL.md`(指挥官,精简到只路由)+ `shared/core-principles.md`(七项 + 自反条款) |
| `core-production-gates.md` | → `shared/core-principles.md` |
| `knowledge-discovery-and-gaps.md` | → `shared/knowledge-discovery.md` |
| `prompt-architecture-and-runtime.md` | 文件边界/命名 → `shared/artifact-boundaries.md`;执行单元地图/运行时契约/职责矩阵/影响分析 → 拆入对应 task skill(prompt-creation 为主;inspection/revision 引用) |
| `validation-and-external-handoff.md` | 运行时证据/状态 → `shared/runtime-evidence.md`;行为案例设计 → `skills/agent-eval-creation/`;外部交接 → `shared/handoff.md`;静态集成 → 各 task skill |
| `workflow-and-state.md` | 八阶段 → `development/legacy-eight-stage-reference.md`;五步主线 + 确认点 + 中断恢复 → `skills/prompt-creation/SKILL.md`;Eval 阶段 → `skills/agent-eval-creation/SKILL.md` |
| `task-protocols.md` | Inspection → `skills/prompt-inspection/`;Creation → `skills/prompt-creation/`;Revision → `skills/prompt-revision/`;Eval → `skills/agent-eval-creation/`;交接 → `shared/handoff.md` |
| `artifact-templates.md` | 按流程拆到各 skill `templates/`;门禁摘要 → 引用 `core-principles.md`;manifest → `scripts/` 引用 |
| `scripts/validate_prompt_package.py` | → `scripts/`(不变) |

## 九、仍待确认的点

1. Codex skill 安装机制实测结果(决定发布同步策略细节)。
2. `sync-shared.py` 同步策略:`_shared/` 子目录复制 vs 按引用内联(影响 skill 体积与一致性检查方式)。
3. Claude Plugin 整包安装时 skill 引用 plugin 根 `shared/` 的可用性验证。
4. 指挥官 skill 与 plugin 同名 `produce-agent-prompts` 是否在所有宿主都能保留 `/produce-agent-prompts` 触发。
5. 四个 task skill 的触发命令名(prompt-creation / agent-eval-creation / prompt-inspection / prompt-revision)是否合用户习惯。

## 十、实施前置条件

本 v2 提案再审通过(目标 4.5/5)后,按"建 plugin 骨架 → 建 `shared/`(单一权威)→ 建四个 task skill(各含七项映射 + 五步/对应主流程 + shared 按需读取表 + templates)→ 写 `sync-shared.py` → 迁移内容并删旧 references → 静态回归 → Codex/Claude 双环境实测 → 同步安装"实施。实施前完成 §九 的实测与确认。
