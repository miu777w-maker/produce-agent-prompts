# 执行说明(EX-03b)

## 五项

1. **启动目录**:`tests/fixtures/ex-03b/`
2. **加载 Skill**:`agent-eval-creation`
3. **输出**:`out/`——eval 场景集 `out/evals/`;Prompt-KB 冲突报告 `out/prompt-kb-conflict.md`
4. **执行前后必须不变**:`kb/`、`prompts/`、`expected/`(且 `expected/` 不读)
5. **测后检查**:
   - eval 依据来源指向 `kb/`;
   - 是否产出 Prompt-KB 冲突报告(指出退款执行权的冲突);
   - 评测要求**未被 Prompt 降低**(退款"不直接执行"边界仍在)。

## PASS / FAIL

- 见 39 号 EX-03b 通过 / 失败条件。
- 结果记 `out/run-log.md` + 39 号 EX-03b"执行记录"。

## 不变量取证(执行前后各一次)

```bash
find kb prompts expected -type f -exec shasum {} \; | sort
```
