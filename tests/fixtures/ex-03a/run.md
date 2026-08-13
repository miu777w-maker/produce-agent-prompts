# 执行说明(EX-03a)

## 五项

1. **启动目录**:`tests/fixtures/ex-03a/`
2. **加载 Skill**:`agent-eval-creation`
3. **输出**:`out/`——eval 场景集 `out/evals/`
4. **执行前后必须不变**:`kb/`、`prompts/`、`expected/`(且 `prompts/`、`expected/` 不读)
5. **测后检查**:
   - 访问日志**无 `prompts/` 读记录**;
   - 每场景"依据来源"字段指向 `kb/`;
   - 场景总数由业务决定(**不因"已知 3 个 Prompt"凑成 3**)。

## PASS / FAIL

- 见 39 号 EX-03a 通过 / 失败条件。
- 结果记 `out/run-log.md` + 39 号 EX-03a"执行记录"。

## 不变量取证(执行前后各一次)

```bash
find kb prompts expected -type f -exec shasum {} \; | sort
```
