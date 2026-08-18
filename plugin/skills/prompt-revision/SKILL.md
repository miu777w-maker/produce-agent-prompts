---
name: prompt-revision
description: 【未实现·占位】改写已有 Prompt。当前无主流程;若被触发,返回"prompt-revision 流程未实现",不得用通用能力临时完成。
---

# Prompt Revision(占位 · 未实现)

**状态:未实现**——主流程尚未建立。当前文件仅为占位,声明权限边界与职责。

> **若被触发**:返回"prompt-revision 当前流程未实现",**不得用通用能力临时完成**修订;请等建立最小流程后再用。

## 职责(建成后)
在授权范围内改写已有 Prompt。变更影响 Eval 时,**只记录 Eval 重新评估需求并交回 agent-eval-creation,不直接修改 Eval**。

## 本任务工具与授权(建成后)
只读知识库、授权范围内可写 Prompt;不访问后端、不写知识库、不修改 Eval(影响 Eval 只记录需求交回 agent-eval-creation)。涉及外部访问 / 子 Agent 时读 `${CLAUDE_PLUGIN_ROOT}/shared/tool-permissions.md` 共同清单。

## 共同原则
遵循 `${CLAUDE_PLUGIN_ROOT}/shared/core-principles.md`。
