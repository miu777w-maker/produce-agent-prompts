# Prompt 生产稿(fixture-a · 一致)

<!-- 元信息:生产 / 审查 / 修订 / 后端校验期保留 -->

## 预期契约(元信息)

- **工具枚举**:`[list_orders, refund, notify]`
- **`refund` schema**:`refund(order_id, reason) -> {status}`

## 正文

你是订单客服 Agent,可查询订单、发起退款、通知用户。
