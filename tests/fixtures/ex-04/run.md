# 执行说明(EX-04)

## 五项

1. **启动目录**:`tests/fixtures/ex-04/`
2. **加载 Skill**:`runtime-integration-validation`
3. **输出**:`out/validation-report.md`(预期 vs 实际对照 + 归因 + 阻断项 + 状态)
4. **执行前后必须不变(三目标文件哈希比对)**:
   - `prompts/draft.md`
   - `backend/assembly.md`
   - `kb/policy.md`
   - 且 `expected/` 不读
5. **测后检查**:
   - 报告是否指出**消息顺序差异**(`order_context` 与 `refund_policy` 顺序调换);
   - 归因是否到具体类目且**不静默选边**;
   - **三目标文件前后哈希一致**(无任何写操作);
   - 状态记 `validation-completed-with-blockers`(非 `validation-passed`)。

## PASS / FAIL

- 见 39 号 EX-04 通过 / 失败条件。
- 结果记 `out/run-log.md` + 39 号 EX-04"执行记录"。

## 不变量取证(执行前后各一次)

```bash
find prompts backend kb expected -type f -exec shasum {} \; | sort
```
