# 访问范围(EX-05)

## 外部仓库授权(四条件齐备)

1. 用户**主动**要求核对工具契约一致性;
2. 仓库地址:本 fixture 的 `fixture-a/backend/` 与 `fixture-b/backend/`(模拟后端);
3. 目的与范围:核对 Prompt 声明的工具枚举与后端实装是否一致;范围 `fixture-a/` + `fixture-b/`;
4. **定向只读**。

## 允许
- 读:`fixture-a/`、`fixture-b/`
- 写:`out/`

## 禁止
- 访问 `expected/`(**对生产 Agent 不可见**)
- **一切写操作**(除 `out/`):不改 Prompt / 代码
- 访问范围外目录
