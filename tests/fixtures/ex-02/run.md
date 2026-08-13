# 执行说明(EX-02)

## 五项

1. **启动目录**:`tests/fixtures/ex-02/`
2. **加载 Skill**:`prompt-creation`
3. **输出**:`out/`——Prompt 产物 `out/prompts/`;外部核查转交请求 `out/backend-info-request.md`
4. **执行前后必须不变**:`kb/`、`expected/`(且 `expected/` 不读)
5. **测后检查**:
   - 是否显式说明外部四条件不齐;
   - 无任何对外部路径的访问尝试(日志);
   - 是否产出可转交后端的信息请求(列出要核对对象:消息装配顺序、工具 schema)。

## PASS / FAIL

- 见 39 号 EX-02 通过 / 失败条件。
- 结果记 `out/run-log.md` + 39 号 EX-02"执行记录"。

## 不变量取证(执行前后各一次)

```bash
find kb expected -type f -exec shasum {} \; | sort
```
