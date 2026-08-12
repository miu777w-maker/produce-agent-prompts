---
name: produce-agent-prompts
description: 指挥官(任务路由)。启用后先确定走哪个任务 skill——新建 prompt 用 prompt-creation;独立评测完整 Agent 业务行为用 agent-eval-creation;检验/改写(原型后)。选定任务后由目标任务 skill 加载共同七项原则并执行。Prompt 生产与 Eval 生产是两条独立流程。
---

# Produce Agent Prompts(指挥官)

本 skill 只负责任务路由,不重复七项原则正文。选定任务后,由目标任务 skill 加载 `_shared/core-principles.md` 并执行。

## 关键概念:阶段同步 ≠ 生产绑定

Prompt 生产与 Eval 生产是两条独立流程。知识库常说的“同步形成”指**项目阶段同步**(两任务在同一阶段一起规划、共享知识库),**不是生产绑定**(逐单元 1:1、eval 以 prompt 为知识源、eval 文件数迁就 prompt 数)。两者各自从知识库独立推导。

## 任务路由

| 用户意图 | 任务 skill |
| --- | --- |
| 新建 prompt 体系(不产 eval) | `prompt-creation` |
| 评测完整 Agent 业务行为(独立推导,不改 prompt) | `agent-eval-creation` |
| 检验已有 prompt(只报告) | `prompt-inspection`(原型后) |
| 改写已有 prompt | `prompt-revision`(原型后) |
| 外部评测执行交接 | `agent-eval-creation` 完成、eval 准备执行时**条件生成** |

用户已明确任务时直接采用;未明确时提一个会改变流程的范围问题。一条流程完成后停止;只有用户明确启动才进入另一流程。

## 共同约束

选定任务后,由目标任务 skill 加载 `_shared/core-principles.md` 共同七项原则并执行。指挥官不复制七项概要。
