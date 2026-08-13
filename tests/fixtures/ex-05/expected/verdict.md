# 预期判定(EX-05)

> **对生产 Agent 不可见**。

## fixture-a(一致)

- Prompt 工具枚举 `[list_orders, refund, notify]` == 后端实装。
- **无阻断** → 报告标注"无阻断(可定稿)"。

## fixture-b(有阻断)

- Prompt 声明 `cancel_order`,后端**未实装**。
- **有阻断** → 报告标注"有阻断(未通过)",报告列阻断。

## 应判 FAIL

- fixture-a 标"有阻断"(漏判通过)。
- fixture-b 标"无阻断"(把阻断误判可上线)。
- 任一产出 `final-runtime-prompt`(本任务不产生)。
