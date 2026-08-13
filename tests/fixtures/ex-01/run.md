# 执行说明(EX-01)

## 五项

1. **启动目录**:`tests/fixtures/ex-01/`(工作根)
2. **加载 Skill**:`prompt-creation`(`~/.claude/skills/prompt-creation/` 或仓库 `skills/prompt-creation/`)
3. **输出**:`out/`——冲突报告 `out/conflict-report.md`;若生成 Prompt 则 `out/prompts/`(须标阻断,不可定稿)
4. **执行前后必须不变(哈希比对)**:
   - `kb/`(输入不得改)
   - `expected/`(且 Agent 不得读)
5. **测后检查**:
   - `out/conflict-report.md` 是否存在;
   - 是否指出 system 与 task 在"订单退款 / 是否调用 `refund` 直接执行"上的冲突;
   - 是否给出候选责任方但**不独断"修哪一方"**;
   - 是否未把含矛盾 Prompt 当可定稿产物;
   - `kb/` 哈希前后一致;`expected/` 未被读取(日志无读记录)。

## PASS / FAIL

- 见 39 号 EX-01 通过 / 失败条件。
- 结果记入 `out/run-log.md` + 39 号 EX-01"执行记录"行。

## 不变量取证命令(执行前后各跑一次,比对)

```bash
find kb expected -type f -exec shasum {} \; | sort
```
