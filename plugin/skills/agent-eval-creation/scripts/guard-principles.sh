#!/bin/bash
# Guard principles hook for UserPromptSubmit. Injects a structured reminder
# (outer XML tag + markdown inside) to keep the AI aligned with agent-eval-creation.

INPUT=$(cat)
EVENT=$(jq -r '.hook_event_name' <<< "$INPUT")

REMINDER=$(cat <<'EOF'
<agent-eval-creation-reminder>
按你当前所处的流程位置,重点关注下方对应步骤的约束,同时兼顾全局原则。参照 agent-eval-creation 技能行事。

## 全局原则
- 评测对象是**完整 Agent 业务行为**,不是 prompt 文件;场景数来自业务风险,非 prompt 数。
- **默认禁止读取 Prompt 文件**(即使仓库内有也不主动读);只有用户明确强力要求才在授权下读,且知识库仍为唯一知识源。
- 不以 Prompt 复制 / 降低 / 缩窄评测;与 Prompt 理解不同时,标记冲突而非迁就。
- 权限:只读知识库、可写 Eval;不访问后端、不写知识库、不修改 prompt。
- 七项对应信息仅作**事实完整性检查**(需求范围 / 运行环境 / 上下文 / 角色边界 / 职责 / 关键约束 / 知识疑点),只取相关的,不要求逐项形成场景;事实一律从知识库检索。

## 流程(五步)
1. 明确评测目标与被测 Agent 行为范围——评测什么 Agent、哪些能力、哪些场景。
2. 独立从知识库检索评测依据——默认不读 Prompt。
3. 设计场景覆盖失败面——正常 / 边界 / 模糊 / 冲突 / 缺失 / 工具 / 对抗 / 长对话 / 组合 / 上下游。
4. 逐场景生成 eval——不为迎合 prompt 而复制 / 降低 / 缩窄。
5. 倒查交付——失败面覆盖、事实完整性、忠于 KB;eval 就绪时条件生成外部评测交接。

## 何时调用 Rubric
- 用户只要 Eval 场景:只生成 Eval。
- 用户要完整评测材料,或 KB 规定 Eval 必须配评分细则:条件调用 agent-rubric-creation(skill 间直调),传被评对象 / 业务目标 / 评价范围 / KB 依据位置;不把 Eval 临时判断当作 Rubric 的知识依据。
</agent-eval-creation-reminder>
EOF
)

jq -nc --arg event "$EVENT" --arg ctx "$REMINDER" '{
  hookSpecificOutput: {
    hookEventName: $event,
    additionalContext: $ctx
  }
}'
