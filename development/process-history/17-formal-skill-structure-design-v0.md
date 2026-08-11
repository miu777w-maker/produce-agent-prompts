# 系统 Agent 提示词生产 Skill：正式结构设计 V0

> 日期：2026-08-11  
> 当前主线：正式 Skill 结构设计  
> 状态：待第二个人工确认点确认；尚未创建 Skill 成品。

## 一、设计基线

正式 Skill 同时承担两类职责：

1. **生产前反向取证**：从合格提示词应满足的要求，反推出生产前必须获得、绑定和确认的信息；
2. **生产后正向校验**：检查生成的 prompts、evals 与运行时契约是否真正满足要求。

原始输入中的六点是不可删减的核心基线，但不是完整生产流程。知识发现、任务入口识别、prompt 清单推导、评测交接、更新影响分析和中断恢复属于实现稳定生产所需的增强能力。Skill 必须区分二者，不能把增强项伪装成原始要求。

## 二、建议名称

### 文件夹名称

`produce-agent-prompts`

### 选择理由

- 以动词开头，直接说明核心动作；
- 不绑定资金安全顾问或某种固定 Agent 架构；
- “prompts” 可同时覆盖整套系统提示词和局部提示词；
- evals、来源映射和运行时契约是提示词生产的配套产物，不需要全部塞进名称。

## 三、触发描述草案

> 从项目知识库发现和校验生产系统 Agent prompts 所需的目标、知识、运行时上下文与职责边界，推导或验证 prompt 清单，分阶段生成或更新 prompts、evals、来源映射和运行时集成契约。用于整套或局部 Agent 提示词的新建、改写、审查、知识变更影响分析；关键知识缺失时停止生成并提出补全请求。

该描述覆盖三种入口：

1. 人员已经给出 prompt 清单；
2. 人员只给目标，由 Skill 从知识库推导清单；
3. 知识、schema、流程或规则发生变化，需要分析并局部更新。

## 四、Skill 类型与自由度

- 类型：多阶段工作流 Skill；
- 高自由度：理解不同业务、识别知识主题、判断 prompt 架构候选；
- 中自由度：阶段推进、缺口分类、产物编写和评测设计；
- 低自由度：关键知识阻塞、六项核心门禁、状态枚举、来源映射、prompt/eval 配对和确定性校验。

## 五、文件结构

该文件夹本身就是独立仓库根目录，不嵌入当前 PRD 项目的某个 Skill 集合：

```text
produce-agent-prompts/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── workflow-and-state.md
│   ├── knowledge-discovery-and-gaps.md
│   ├── core-production-gates.md
│   ├── prompt-architecture-and-runtime.md
│   ├── validation-and-external-handoff.md
│   └── artifact-templates.md
└── scripts/
    └── validate_prompt_package.py
```

不创建 README、CHANGELOG、安装指南或其他辅助文档。

其中 `SKILL.md`、`references/` 和 `scripts/` 构成跨环境核心；`agents/openai.yaml` 只是 Codex 的可选界面适配文件，其他环境可以忽略，且任何核心能力都不得只写在该文件中。

## 六、各文件职责

### `SKILL.md`

只保留每次触发都必须知道的内容：

- 任务目标与边界；
- 三种入口模式；
- 八阶段主流程；
- 三个人工确认点；
- 关键知识缺失绝不生成；
- 核心状态和中断恢复规则；
- 每个阶段应读取哪一份 reference；
- 明确不负责实际代码实现和真实行为评测执行。

不在这里重复详细门禁、模板字段和案例说明，控制上下文成本。

### `references/workflow-and-state.md`

- 八阶段进入条件、动作、产物、退出条件；
- 明确清单、目标驱动、变化驱动三种入口的分流；
- 阶段状态、暂停、回退和恢复协议；
- 突发消息分类、分支记录和主线回归点；
- 三个人工确认点的具体确认对象。

### `references/knowledge-discovery-and-gaps.md`

- 话题优先、根卡、原子卡、引用/反链、全文搜索的发现顺序；
- 入库内容默认真实的项目约定；
- 明显错误、冲突、断链、版本异常和“非最终”信息的识别；
- 知识覆盖表和关键性判断；
- 面向项目人员、后端 Agent、前端 Agent的可复制补全请求；
- 补充知识必须入库后重新检索，不使用临时问答绕过门禁。

### `references/core-production-gates.md`

集中保存原始输入导出的六项核心门禁。每项同时定义：

1. 生产前必须获取的信息；
2. 必须形成的显式产物；
3. 生成前阻塞条件；
4. 生成后的检查方法；
5. 通过、警告、失败的判定。

六项为：

- Agent 运行环境说明；
- 关键执行时机上下文契约与概念引用绑定表；
- 业务与角色行为契约；
- prompt 职责与信息可见性矩阵；
- 关键约束与注意力安排；
- 知识疑点与冲突检查报告。

即使未发现疑点，也必须显式输出“未发现”的结论。

### `references/prompt-architecture-and-runtime.md`

- 从目标和知识推导执行单元与 prompt 候选的方法；
- prompt 合并、拆分和职责边界判断；
- 渐进式披露、最小可见信息和轻量上下文预算；
- 加载节点、message role、装配顺序和动态注入；
- 状态、历史、工具 schema、调用条件、结果消费者；
- 输出结构、parser、anchor/reminder、异常路径；
- prompt/schema/code/eval 的版本对应；
- 指令与数据的信任边界。

### `references/validation-and-external-handoff.md`

- 单 prompt、prompt/eval 配对和系统集成检查；
- 确定性检查、行为评测和人工决策的边界；
- 正常、边界、冲突、缺失、工具、对抗、长对话和上下游案例设计；
- 外部评测交接包；
- “待外部评测”与“外部已通过”的证据边界；
- 失败归因和回退阶段；
- 更新模式下的影响分析、安全差异交付和回退位置。

### `references/artifact-templates.md`

集中保存精简模板，避免零散复制：

- 任务目标与范围确认；
- 知识覆盖表；
- 关键知识补全请求；
- 六项核心门禁产物；
- prompt 清单与职责矩阵；
- prompt 单元规格；
- eval 单元规格；
- 运行时集成契约；
- 外部评测交接包；
- 阶段检查点、分支记录与恢复点；
- 最终交付清单。

模板提供必要字段，不把资金安全顾问案例内容固化进去。

### `scripts/validate_prompt_package.py`

只执行可确定判断，不冒充模型行为评测：

- prompt 与 eval 是否成对；
- 文件命名和必填清单是否完整；
- 引用的知识来源是否存在；
- 占位符是否在运行时契约中登记；
- 工具名称是否在工具契约中登记；
- 六项核心门禁产物是否存在；
- 版本对应是否完整；
- 输出机器可读的通过、警告和失败报告。

脚本不判断语气是否自然、规则是否真正有效或模型行为是否通过。

## 七、渐进式披露路由

每次任务只读取必要 reference：

- 启动、恢复或突发分支：读取 `workflow-and-state.md`；
- 搜索知识或发现缺口：读取 `knowledge-discovery-and-gaps.md`；
- 开始设计或生成前：必须读取 `core-production-gates.md`；
- 推导清单、划分 prompt、定义运行时：读取 `prompt-architecture-and-runtime.md`；
- 生成 eval、静态检查或交接：读取 `validation-and-external-handoff.md`；
- 需要产出具体文档时：读取 `artifact-templates.md`。

references 保持一层，不让 reference 再承担新的路由入口。

## 八、建议保存位置

第一版在本机生成一个独立文件夹：

`/Users/miumiu777/Desktop/AI work/prd/produce-agent-prompts/`

该目录本身就是未来 Git 仓库的根目录，用户可以直接把整个文件夹上传到 Git 仓库。它不属于资金安全顾问知识库，也不依赖当前 PRD 项目的其他文件才能运行。

设计过程与决策档案仍保存在当前 `archives/` 中，但正式 Skill 成品必须自包含；不得通过相对路径引用这些设计档案，也不得引用本机资金安全顾问案例路径。

## 九、跨环境可移植性约束

- 目标环境包括 Codex、Claude，以及其他支持文件夹式 Skill 和 `SKILL.md` 的 Agent 环境；
- `SKILL.md` 只使用通用的 `name` 和 `description` frontmatter；
- 核心指令使用环境无关表述，不假设一定存在 Codex、Claude 或某个特定知识库产品；
- 把“搜索知识库、读取文件、执行脚本、向人员索取信息”描述为能力要求，并要求运行环境先声明可用工具；
- 某环境缺少搜索、文件写入或脚本执行能力时，Skill 必须降级为生成明确的人工操作请求，不能假装已完成；
- `agents/openai.yaml` 不承载核心规则，仅用于 Codex 展示和默认触发语句；
- 不要求 Claude 等非 Codex 环境识别 `agents/openai.yaml`；忽略该文件不能损失任何核心能力；
- Python 校验脚本保持标准库实现，避免绑定某个平台 SDK；
- 所有 reference 使用仓库内相对路径，整个文件夹移动或上传后仍能解析；
- 资金安全顾问只用于测试，不写入正式 Skill 的固定规则或路径。

## 十、与原始输入的对应关系

| 原始要求 | 正式承载位置 |
| --- | --- |
| 运行时工作环境 | `core-production-gates.md` + `prompt-architecture-and-runtime.md` |
| 执行时上下文与明确概念对应 | `core-production-gates.md` + artifact 模板 |
| 业务、角色、语气和行为 | `core-production-gates.md` |
| 职责、去重和渐进式披露 | `core-production-gates.md` + `prompt-architecture-and-runtime.md` |
| 关键约束与 Anchor | `core-production-gates.md` + 运行时集成契约 |
| 可疑知识错误 | `knowledge-discovery-and-gaps.md` + `core-production-gates.md` |
| 整理成稳定生产 Skill | `SKILL.md` + workflow、templates、validator |

## 十一、第二个人工确认点

正式创建前需要确认：

- 名称和触发范围是否准确；
- 文件拆分是否符合渐进式披露；
- 六项原始基线是否被集中、明确承载；
- 校验脚本是否保持在确定性检查边界；
- 独立仓库根目录与跨环境约束是否合适。

确认后回到主线，进入 Skill 初始化与编写。
