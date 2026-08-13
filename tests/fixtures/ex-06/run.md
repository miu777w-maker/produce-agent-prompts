# 执行说明(EX-06)

## 五项

1. **启动目录**:`tests/fixtures/ex-06/`
2. **加载 Skill**:`prompt-inspection`(**现阶段**;`prompt-revision` 原型后改加载它,补"修订产物不含对冲"验证)
3. **输出**:`out/inspection-report.md`
4. **执行前后必须不变**:`kb/`、`prompts/`、`expected/`(且 `expected/` 不读)
5. **测后检查(现阶段可执行部分 ①②)**:
   - 是否识别对冲语句及其位置;
   - 是否**归因到架构层**(system 与 task 在"写操作"上冲突,须修 KB / 装配,职责声明不作减免);
   - 是否未把对冲当作"已解决冲突"。
   - ③"修订产物不含对冲语句"待 Revision 原型后补测。

## PASS / FAIL

- 见 39 号 EX-06 通过 / 失败条件(现阶段判 ①②)。
- 结果记 `out/run-log.md` + 39 号 EX-06"执行记录"。

## 不变量取证(执行前后各一次)

```bash
find kb prompts expected -type f -exec shasum {} \; | sort
```
