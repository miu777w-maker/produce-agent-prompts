# Produce Agent Prompts

> **v0.4.0(试用 / pre-release)**
>
> 一套 Claude Code / Codex skill,从一个项目知识库出发,稳定生产**可追溯、可接入运行时、可评测**的 Agent **Prompt / Eval / Rubric**。

## 这是什么 / 不是什么

**是**:面向"有项目知识库"的团队——Agent(或人)按统一方法,从知识库**独立推导**出整套 Agent 提示词、评测场景、评分细则,并在需要时对照后端真实实现做运行时校验。

**不是**:随手帮你写个 prompt 的工具。没有项目知识库,它发挥不了作用。

产出的是 **Skill 本身**(供 Claude Code / Codex 加载执行),不是某个具体业务的 prompt。

## 包含的 skill

| Skill | 做什么 | 状态 |
| --- | --- | --- |
| `produce-agent-prompts` | 指挥官:按你的意图路由到对应任务 | 可用 |
| `prompt-creation` | 新建 Prompt 体系(从知识库独立推导) | 可试运行 |
| `agent-eval-creation` | 生成评测场景(完整 Agent 业务行为;**默认不读 Prompt**) | 可试运行 |
| `agent-rubric-creation` | 生成评分细则(可观察、可打分、正交) | 待首次真实试运行 |
| `runtime-integration-validation` | 后端运行时校验(预期 vs 实际,**只读只报告**) | 原型 |
| `prompt-inspection` | 检查已有 Prompt(只报告) | 占位·未实现 |
| `prompt-revision` | 改写已有 Prompt | 占位·未实现 |

启用 `produce-agent-prompts`(指挥官),告诉它你要做什么,它会路由到对应任务 skill。

## 核心理念

- **七类 Agent 事实**(所有任务共享):目标范围 / 运行环境 / 上下文绑定 / 业务角色 / 职责可见性 / 关键约束 / 知识疑点。各 skill 按自己职责**转化为不同产物**,不机械套同一流程。
- **三条独立流程**:Prompt / Eval / Rubric 各自从知识库独立推导,**互不当"正确答案"**,文件数不互相迁就。
- **知识库驱动,不越权**:默认只读项目知识库;不主动访问后端 / 其他仓库,除非用户明确授权(主动要求 + 地址 + 目的 + 范围,四条件齐备)。
- **关键资料缺失即停**:不编造、不假设,标记缺失并生成转交请求。
- **渐进式披露**:一次任务只加载当前 skill 需要的内容,不读其他流程 / 历史 / 测试。
- **简化优先**:不为"结构完整"预建状态机 / 占位能力;真实问题暴露再补最小规则。

→ 详见 [`PROJECT_CONSTITUTION.md`](./PROJECT_CONSTITUTION.md)(最高指令,修改 / 评审本仓库前必读)。

## 安装

### Claude Code

```bash
git clone https://github.com/miu777w-maker/produce-agent-prompts.git
cd produce-agent-prompts

# 把 7 个 skill 复制到 Claude Code 的 skills 目录
rsync -a skills/ ~/.claude/skills/
```

重开会话,Claude Code 即发现这些 skill。

> 公司内网可用 GitLab 镜像:`http://gitlab.eidtokencloud.com/wangmiao/produce_agent_prompts`

### Codex / 其他宿主

参考 [`agents/openai.yaml`](./agents/openai.yaml);把 `skills/*/` 各自放到对应宿主的 skill 加载路径。本仓库宿主无关(没有 rsync / git push 等宿主特定操作写进 skill)。

## 使用

1. 在你的项目(有知识库的)目录开 Claude Code 会话。
2. 触发 `produce-agent-prompts`。
3. 说你要做什么:**新建 Prompt / 生成评测 / 生成评分细则 / 后端运行时校验**。
4. 它路由到对应 skill,按方法从你的知识库推导产出。

它会:定向读知识库 → 缺关键资料就停下问你 → 按知识库规定的名称 / 拆分产出 → 七类事实倒查。

## 仓库结构

```text
PROJECT_CONSTITUTION.md   最高指令(改 / 评仓库前必读)
AGENTS.md / CLAUDE.md     入口(指向 CONSTITUTION)
VERSION.md                版本与就绪度
skills/                   7 个 skill(各含 SKILL.md + _shared/)
shared/                   共享事实(core-principles)+ 工具授权(tool-permissions)
scripts/                  sync-shared.py(同步 _shared)、validate_prompt_package
agents/                   平台适配(Codex)
.claude-plugin/           plugin 元数据
```

历史归档(v0.3 references、开发过程、可执行测试 fixture)在 `archive/development-history` 分支,不在主分支出现,也不进任务上下文。

## 状态

**v0.4.0(试用 / pre-release)**——Prompt / Eval / Rubric 可进真实知识库试运行;Runtime 可受控试验;Inspection / Revision 占位未实现。成熟度与未覆盖范围详见 [`VERSION.md`](./VERSION.md)。
