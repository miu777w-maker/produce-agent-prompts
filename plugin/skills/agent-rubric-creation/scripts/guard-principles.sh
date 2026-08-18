#!/bin/bash
# Guard principles hook for UserPromptSubmit. Injects a structured reminder
# (outer XML tag + markdown inside) to keep the AI aligned with agent-rubric-creation.

INPUT=$(cat)
EVENT=$(jq -r '.hook_event_name' <<< "$INPUT")

REMINDER=$(cat <<'EOF'
<agent-rubric-creation-reminder>
按你当前所处的流程位置,重点关注下方对应步骤的约束,同时兼顾全局原则。参照 agent-rubric-creation 技能行事。

## 全局原则
- Rubric 评价**完整 Agent 实际表现**(可观察行为与结果),不是 Prompt 文本写作质量。
- 条目必须**可验证**(基于消息 / 工具调用 / 输出等证据)、**可打分**(明确标度)、尽量**正交**(条目归属唯一维度,同一错误不重复处罚);可设一票否决(仅破坏正确性 / 安全 / 运行契约的严重错误)。
- **默认禁止读取 Prompt 文件**(即使仓库内有也不主动读);只有用户明确强力要求才在授权下读,且知识库仍为唯一知识源;不以 Prompt 复制 / 降低 / 缩窄评分。
- 权限:只读知识库、可写 Rubric;不访问后端、不写知识库、不修改 Prompt;不生成 Eval 测试场景 / 用户输入 / 测试数据 / 执行方法。
- 七项对应信息仅作**事实完整性检查**,只取与评分对象相关的,不要求逐项形成条目;事实一律从知识库检索。

## 流程(五步)
1. 明确评测对象与范围——被评 Agent、可观察行为、评判者(人工 / Judge Agent)、评分用途。
2. 从知识库检索与评分对象有关的事实——运行环境 / 上下文 / 角色边界 / 职责 / 关键约束 / 知识疑点。
3. 按任务选择评分维度——事实准确 / 完成结果 / 指令遵循 / 工具权限边界 / 语气 / 简洁度,按任务挑,不机械全含。
4. 逐条目编写——可观察、可打分、正交;与 Prompt 理解不同时依 KB,标记冲突而非迁就。
5. 倒查交付——每条目可验证 / 可打分;忠于 KB、无 Eval 体系外溢;命名 / 拆分服从 KB 规范。
</agent-rubric-creation-reminder>
EOF
)

jq -nc --arg event "$EVENT" --arg ctx "$REMINDER" '{
  hookSpecificOutput: {
    hookEventName: $event,
    additionalContext: $ctx
  }
}'
