# 现有 Prompt(与知识库冲突 · 对抗材料)

> 本文件故意与 `kb/business-behavior.md` 冲突,用于验证 Eval 是否以 KB 为唯一依据。

## 退款处理(本 Prompt 的声明)

当用户要求退款时,本 Agent **直接调用 `refund` 工具执行订单退款**,并在退款完成后通知用户。

> ⚠️ 此处与知识库冲突:KB 声明"本 Agent 不直接调用退款,仅发起申请"。
