# D7 收口实施(审查第二轮:删减有效,差一次收口)

> 日期:2026-08-13
> 依据:审查第二轮结论 + 用户确认。本号记录 D7 收口。
> 状态:**D7 已实施 + sync + 自检通过**,仓库自洽,可读 / 可试运行。

## D7 实施(逐条)

### ① 加载时机统一(消除矛盾)
- `core-principles.md` "工具与授权"节改为:"启动只读七项 + 本任务权限行;仅外部访问 / 子Agent / 权限疑点时读共同协议"。与 `tool-permissions.md` + 各 skill 表述一致。

### ② 必要禁止写回各任务权限行(必要重复,非过度设计)
- **Prompt Creation** 补:保留元信息(不自动删)/ 定向检索(不扫描全库)/ 不以职责声明对冲 system-task 冲突。
- **Eval Creation** 补:Prompt-KB 冲突时标记而非迁就。
- **Runtime Validation** 显式:不静默选边 KB 或代码。

### ③ 删未来迁移占位
- 删 `core-principles.md` "各项详细判据(按需读)"整节(显式产物 / 失败条件 / 证据分级属开发计划,且与 D6-4 冲突)+ 第 3 行未来迁移引用。

### ④ Prompt Creation 不越权判断运行时
- 七项映射"运行环境"行:从"运行时是否真实可见"→"KB 是否有明确运行时依据 + Prompt 是否忠实采用 + 缺则停止,不写假定、不宣称已验证后端"(后端实证归 Runtime Validation)。

### ⑤ 占位 skill 防假可用
- 指挥官路由表 + description **移除** inspection / revision 可选项(不再作为当前可执行任务)。
- 占位 skill description 改"**【未实现·占位】**";正文加"**若被触发,返回'流程未实现',不得用通用能力临时完成**"。
- Inspection 职责"检查真实装配"→"**检查知识库声明的预期装配**"(它禁后端)。

### 降级
- 删各 production skill"(原型骨架)/ 正式迁移时填入"开发说明。
- 指挥官删"外部评测执行交接"路由(非并列用户任务,留 Eval 内部)。
- Runtime 报告标签 `validation-completed-with-blockers/passed` → **"有阻断 / 无阻断"**(连带 EX-05 + 39 号同步)。

## 最终运行层(8 文件 / 266 行)

| 文件 | 行 |
| --- | --- |
| `shared/core-principles.md` | 21 |
| `shared/tool-permissions.md` | 47 |
| `skills/produce-agent-prompts/SKILL.md` | 28 |
| `skills/prompt-creation/SKILL.md` | 39 |
| `skills/agent-eval-creation/SKILL.md` | 42 |
| `skills/runtime-integration-validation/SKILL.md` | 51 |
| `skills/prompt-inspection/SKILL.md` | 19(占位·未实现) |
| `skills/prompt-revision/SKILL.md` | 19(占位·未实现) |

**一次 prompt-creation 执行上下文**:指挥官(28)→ prompt-creation(39)→ core-principles(21)≈ 88 行;权限自包含 + 必要禁止内联,**不读 tool-permissions 全文**。

## sync + 自检

- `sync-shared.py`:6 skill `_shared/` 一致。
- `grep`:运行层无"原型骨架" / 旧状态名 / 未来迁移占位残留。

## 待审查 / 试运行

- 仓库自洽,可读。
- 按审查结论:**Prompt Creation + Agent Eval Creation 可进真实知识库试运行**;Runtime Validation 可受控试验;Inspection / Revision 等真正需要时再建最小流程。
