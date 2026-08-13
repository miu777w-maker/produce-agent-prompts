# 后端消息装配(模拟 · EX-04)

```python
# 模拟后端消息装配(故意与 Prompt 元信息不一致)
messages = assemble(
    user_msg,
    refund_policy,     # 实装顺序:refund_policy 在 order_context 之前
    order_context,
    agent_reply,
)
# 实装顺序:[user_msg, refund_policy, order_context, agent_reply]
```

> ⚠️ 与 Prompt 声明 `[user_msg, order_context, refund_policy, agent_reply]` 不符:
> `order_context` 与 `refund_policy` 顺序调换。
