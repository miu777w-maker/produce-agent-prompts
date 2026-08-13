# 测试 Fixture(开箱即跑层)

> 配套:`development/process-history/39-executable-regression-tests.md`。
> 状态:**7 个 fixture 全部补全**(ex-01 / 02 / 03a / 03b / 04 / 05 / 06)。尚未执行(待 Claude / Codex 真跑)。

## 用途

把 39 号的"文字描述 fixture"变成**固定目录 + 固定输入**,使不同执行者(Claude / Codex / 审查)跑同一场景能得到可比较的结果。

## 目录结构(每个 ex-NN/)

```text
ex-NN/
  kb/              # 知识库输入(通用结构,不写死项目字段)
  prompts/         # 已有 Prompt(按场景决定是否在访问范围)
  backend/         # 后端代码/Schema(EX-04/05 用,最小伪代码)
  expected/        # 隐藏的预期判定(对生产 Agent 不可见!)
  user-request.md  # 触发请求
  authorization.md # 访问范围 + 外部授权四条件
  run.md           # 执行五项(启动/加载/输出/不变/检查)
  out/             # 产物输出(执行时写,不污染 fixture 输入)
```

## expected/ 不可见规则

`expected/` 含正确答案(冲突源、应检出差异、正确状态)。**生产 Agent 不得读取 `expected/`**。执行者 / 审查用它判定 PASS / FAIL。每个 `run.md` 须把 `expected/` 列入"禁止访问"。

## 执行流程

1. 进入 `ex-NN/` 作为工作根;
2. 按 `run.md` 加载 Skill、读取 `user-request.md` + `authorization.md`;
3. Agent 在授权范围内执行,产物写 `out/`;
4. 执行者比对 `out/` 与 `expected/verdict.md`,按 39 号通过 / 失败条件记 PASS / FAIL;
5. 结果记回 39 号该条“执行记录”行 + 本目录 `out/run-log.md`。

## 何时运行测试

测试 fixture **不进入正常生产上下文**,仅在以下时机运行(避免每次生产 Prompt 都跑全部测试):

- Skill **发布新版本前**;
- **权限 / 职责 / 状态 / 知识来源规则发生改变后**;
- **真实执行暴露新型严重错误后**(据实补对应场景)。

## 当前完成度

| Fixture | 场景 | 主 Skill |
| --- | --- | --- |
| ex-01 | system/task 冲突阻断 | prompt-creation |
| ex-02 | 外部无授权访问停止 | prompt-creation |
| ex-03a | Eval 独立推导(隔离) | agent-eval-creation |
| ex-03b | Eval 抗 Prompt 污染 | agent-eval-creation |
| ex-04 | Runtime 只读不改 | runtime-integration-validation |
| ex-05 | validation 完成 vs 通过 | runtime-integration-validation |
| ex-06 | 职责声明不对冲(部分:inspection) | prompt-inspection |

> 全部 fixture 内容补全;**尚未执行**(待审查达标后 Claude / Codex 真跑)。
