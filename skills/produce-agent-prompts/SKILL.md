---
name: produce-agent-prompts
description: 指挥官(任务路由)。启用后先确定走哪个任务 skill——新建 prompt 用 prompt-creation;生成评测场景用 agent-eval-creation;生成 Rubric(评分细则)用 agent-rubric-creation(可独立调用,也可由 Eval 按条件调用);后端运行时校验用 runtime-integration-validation(用户授权后端仓库后)。各任务按各自方法执行(Prompt 用七项生产原则;Eval 用评测场景方法;Rubric 用事实维度 + 评分细则方法;Runtime 用预期—实际对照方法)。检验 / 改写已有 prompt 的能力(prompt-inspection / prompt-revision)尚未实现。
---

# Produce Agent Prompts(指挥官)

本 skill 只负责任务路由,不重复各任务方法正文。选定任务后,由目标任务 skill 按各自方法执行(Prompt 用七项生产原则;Eval 用评测场景方法;Rubric 用 Agent 事实维度 + 评分细则方法;Runtime 用预期—实际对照方法)。

## 关键概念:阶段同步 ≠ 生产绑定

Prompt、Eval、Rubric 生产是三条独立流程。知识库常说的“同步形成”指**项目阶段同步**(各任务在同一阶段一起规划、共享知识库),**不是生产绑定**(逐单元 1:1、以 prompt 或 eval 为知识源、文件数互相迁就)。各自从知识库独立推导。

## 任务路由

| 用户意图 | 任务 skill |
| --- | --- |
| 新建 prompt 体系(不产 eval) | `prompt-creation` |
| 生成评测场景(评测完整 Agent 业务行为,独立推导,不改 prompt) | `agent-eval-creation` |
| 生成 Rubric(评分细则;可独立调用,也可由 Eval 条件调用) | `agent-rubric-creation` |
| 后端运行时校验(用户授权后端仓库后) | `runtime-integration-validation` |

> `prompt-inspection` / `prompt-revision` **尚未实现**(占位 skill)。若用户要检查 / 改写已有 prompt,告知该能力未实现,**不要用通用能力临时完成**。外部评测执行交接不是独立任务,由 `agent-eval-creation` 在 eval 就绪时条件生成。

用户已明确任务时直接采用;未明确时提一个会改变流程的范围问题。一条流程完成后停止;只有用户明确启动才进入另一流程。

## 共同约束

各任务方法不同:prompt-creation 用七项生产原则;agent-eval-creation 用评测场景方法(利用 Agent 事实,不机械套用七项);agent-rubric-creation 用 Agent 事实维度 + 评分细则方法;runtime-integration-validation 用预期—实际对照方法。指挥官不复制各方法正文。
