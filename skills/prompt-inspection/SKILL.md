---
name: prompt-inspection
description: 【未实现·占位】检查已有 Prompt(只报告)。当前无主流程;若被触发,返回"prompt-inspection 流程未实现",不得用通用能力临时完成。
---

# Prompt Inspection(占位 · 未实现)

**状态:未实现**——主流程尚未建立。当前文件仅为占位,声明权限边界与职责。

> **若被触发**:返回"prompt-inspection 当前流程未实现",**不得用通用能力临时完成**检查;请等建立最小流程后再用。

## 职责(建成后)
检查已有 Prompt(对照七项 + **知识库声明的预期装配**),只报告问题,**不修改 Prompt**。真实装配核验归 Runtime Validation(本任务不访问后端)。

## 本任务工具与授权(建成后)
只读知识库、只读 Prompt;Eval 仅用户显式范围读;不访问后端、不写知识库、不修改 Prompt(只报告)。涉及外部访问 / 子 Agent 时读 `_shared/tool-permissions.md` 共同清单。

## 共同原则
遵循 `_shared/core-principles.md`。
