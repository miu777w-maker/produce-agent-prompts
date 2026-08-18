# Produce Agent Prompts

> **v0.5.0(试用 / pre-release)**
>
> 一套 Claude Code / Codex skill,从一个项目知识库出发,稳定生产**可追溯、可接入运行时、可评测**的 Agent **Prompt / Eval / Rubric**。

## 这是什么 / 不是什么

**是**:面向"有项目知识库"的团队——Agent(或人)按统一方法,从知识库**独立推导**出整套 Agent 提示词、评测场景、评分细则,并在需要时对照后端真实实现做运行时校验。

**不是**:随手帮你写个 prompt 的工具。没有项目知识库,它发挥不了作用。

产出的是 **Skill 本身**(供 Claude Code / Codex 加载执行),不是某个具体业务的 prompt。

## 包含的 skill

各 skill 直连使用(无指挥官路由层),一次任务只加载一份 SKILL.md:

| Skill | 做什么 | 状态 |
| --- | --- | --- |
| `prompt-creation` | 新建 Prompt 体系(从知识库独立推导) | 可试运行 |
| `agent-eval-creation` | 生成评测场景(完整 Agent 业务行为;**默认不读 Prompt**) | 可试运行 |
| `agent-rubric-creation` | 生成评分细则(可观察、可打分、正交;可独立用,也可由 Eval 条件调用) | 待首次真实试运行 |
| `runtime-integration-validation` | 后端运行时校验(预期 vs 实际,**只读只报告**) | 原型 |
| `prompt-inspection` | 检查已有 Prompt(只报告) | 占位·未实现 |
| `prompt-revision` | 改写已有 Prompt | 占位·未实现 |

直接说你要做什么("新建 prompt""生成评测""生成评分细则"),Claude Code 按各 skill 的 description 自动路由;也可 `/produce-agent-prompts:<skill>` 显式调用。

## 核心理念

- **七类 Agent 事实**(所有任务共享):目标范围 / 运行环境 / 上下文绑定 / 业务角色 / 职责可见性 / 关键约束 / 知识疑点。各 skill 按自己职责**转化为不同产物**,不机械套同一流程。
- **三条独立流程**:Prompt / Eval / Rubric 各自从知识库独立推导,**互不当"正确答案"**,文件数不互相迁就。
- **知识库驱动,不越权**:默认只读项目知识库;不主动访问后端 / 其他仓库,除非用户明确授权(主动要求 + 地址 + 目的 + 范围,四条件齐备)。
- **关键资料缺失即停**:不编造、不假设,标记缺失并生成转交请求。
- **渐进式披露**:一次任务只加载当前 skill 需要的内容,不读其他流程 / 历史 / 测试。
- **简化优先**:不为"结构完整"预建状态机 / 占位能力;真实问题暴露再补最小规则。

→ 详见 [`PROJECT_CONSTITUTION.md`](./PROJECT_CONSTITUTION.md)(最高指令,修改 / 评审本仓库前必读)。

## 加载架构(v0.5)

为避免同一次任务多次加载 skill、以及上下文压缩后反复重载:

- **无指挥官**:直连任务 skill,一次任务只加载一份 SKILL.md;
- **单源 shared**:共享事实与授权协议只在 `plugin/shared/` 一份,各 skill 经 `${CLAUDE_PLUGIN_ROOT}` 引用,零复制;
- **guard reminder**:每个已实现 skill 配 UserPromptSubmit hook,每轮注入压缩版要点(七项 + 流程摘要 + 权限),**上下文压缩后仍生效**,无需重载 SKILL.md;
- **标准插件分发**:marketplace + plugin 结构,一条命令安装 / 更新。

## 安装

本仓库同时是 **marketplace** 和 **plugin**(结构同 cowork):

```
produce-agent-prompts/           marketplace 根
├── .claude-plugin/
│   └── marketplace.json         source 指向 ./plugin
└── plugin/                      实际分发的 plugin bundle
    ├── .claude-plugin/plugin.json
    ├── shared/                  共享事实 + 授权协议(单一权威源)
    └── skills/                  6 个 skill(各含 SKILL.md;已实现的含 scripts/guard-principles.sh)
```

### Claude Code(marketplace 安装)

```
/plugin marketplace add https://github.com/miu777w-maker/produce-agent-prompts.git
/plugin install produce-agent-prompts@produce-agent-prompts-market
```

更新:`/plugin marketplace update produce-agent-prompts-market`。

> **务必用 git 仓库地址添加**,不要用指向 marketplace.json 的裸 URL(裸 URL 只下载清单,相对路径 `./plugin` 指向的文件不会被下载)。
>
> 公司内网可用 GitLab 镜像:`http://gitlab.eidtokencloud.com/wangmiao/produce_agent_prompts`

### 本地开发加载

```bash
git clone https://github.com/miu777w-maker/produce-agent-prompts.git
cd produce-agent-prompts
claude --plugin-dir ./plugin
```

修改后 `/reload-plugins` 热加载。校验:

```bash
claude plugin validate .          # 校验 marketplace
claude plugin validate ./plugin   # 校验 plugin
```

### Codex / 其他宿主

参考 [`agents/openai.yaml`](./agents/openai.yaml);把 `plugin/skills/*/` 各自放到对应宿主的 skill 加载路径,`plugin/shared/` 一并放置并保持相对结构。本仓库宿主无关。

## 使用

1. 在你的项目(有知识库的)目录开 Claude Code 会话。
2. 说你要做什么:**新建 Prompt / 生成评测 / 生成评分细则 / 后端运行时校验**。
3. 对应 skill 被直接触发,按方法从你的知识库推导产出。

它会:定向读知识库 → 缺关键资料就停下问你 → 按知识库规定的名称 / 拆分产出 → 七类事实倒查。

## 仓库结构

```text
PROJECT_CONSTITUTION.md   最高指令(改 / 评仓库前必读)
AGENTS.md / CLAUDE.md     入口(指向 CONSTITUTION)
VERSION.md                版本与就绪度
.claude-plugin/           marketplace 清单
plugin/                   plugin bundle(skills + shared)
scripts/                  validate_prompt_package(产物 manifest 校验,与加载架构无关)
agents/                   平台适配(Codex)
```

历史归档(v0.3 references、开发过程、可执行测试 fixture)在 `archive/development-history` 分支,不在主分支出现,也不进任务上下文。

## 状态

**v0.5.0(试用 / pre-release)**——Prompt / Eval / Rubric 可进真实知识库试运行;Runtime 可受控试验;Inspection / Revision 占位未实现。成熟度与未覆盖范围详见 [`VERSION.md`](./VERSION.md)。
