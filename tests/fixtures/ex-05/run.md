# 执行说明(EX-05)

## 五项

1. **启动目录**:`tests/fixtures/ex-05/`
2. **加载 Skill**:`runtime-integration-validation`
3. **输出**:`out/fixture-a-report.md` + `out/fixture-b-report.md`(各含状态)
4. **执行前后必须不变**:`fixture-a/`、`fixture-b/`、`expected/`(且 `expected/` 不读)
5. **测后检查**:
   - **fixture-a** 报告标注"无阻断(可定稿)" 且无阻断(工具枚举一致);
   - **fixture-b** 报告标注"有阻断(未通过)" 且列出阻断(`cancel_order` 声明但后端未实现);
   - 两个 fixture 的 Prompt / 代码前后哈希一致(无写操作);
   - 不产出 `final-runtime-prompt`。

## PASS / FAIL

- 见 39 号 EX-05 通过 / 失败条件。
- 结果记 `out/run-log.md` + 39 号 EX-05"执行记录"。

## 不变量取证(执行前后各一次)

```bash
find fixture-a fixture-b expected -type f -exec shasum {} \; | sort
```
