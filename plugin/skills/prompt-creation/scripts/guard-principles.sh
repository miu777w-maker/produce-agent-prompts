#!/bin/bash
# Guard principles hook for UserPromptSubmit. Injects a structured reminder
# (outer XML tag + markdown inside) to keep the AI aligned with prompt-creation.

INPUT=$(cat)
EVENT=$(jq -r '.hook_event_name' <<< "$INPUT")

REMINDER=$(cat <<'EOF'
<prompt-creation-reminder>
按你当前所处的流程位置,重点关注下方对应步骤的约束,同时兼顾全局原则。参照 prompt-creation 技能行事。

## 全局原则(七项宪法压缩版)
- 需求先行:目标 Agent / 范围 / 不可改变要求 / 清单来源不明,则停下问,不猜。
- 运行环境:工具 / 消息 / 状态 / 输出消费 / 异常路径须有知识库依据;缺依据则停 + 补请求,不写假定输入,不宣称已验证后端。
- 上下文绑定:prompt 中术语 / 概念在执行时机必须有真实注入来源。
- 业务与角色:角色 / 目标 / 边界 / 语气忠实知识库,不引入无来源规则。
- 职责与可见性:每个执行单元只看到必需信息;职责唯一;不默认扫描全库。
- 关键约束:高风险规则放在有效载体 / 时机;anchor 须有真实钩子和必要性。
- 知识疑点:错误 / 冲突 / 断链 / 版本问题按来源处理,不静默选边。
- 权限:只读知识库、可写 Prompt;不访问后端、不写知识库、不产 Eval;保留 Prompt 元信息;不以职责声明对冲 system/task 冲突。

## 流程(五步)
1. 明确目标与范围——目标 Agent / 执行单元、范围、不可改变要求、清单来源。
2. 定向检索并形成正式文件清单——数量 / 正式名称 / 目录 / 职责 / 运行时载体 / 加载时机;KB 有标准则服从,关键资料缺失则停。
3. 按七项形成文件约束——每个目标文件逐项落到具体结论。
4. 逐文件生成——不私自命名、不合并、不多造文件、不产 eval 或交接。
5. 按七项及必要性倒查交付——约束是否真进入正确文件;信息可见性硬核对;证据不足诚实标记。
</prompt-creation-reminder>
EOF
)

jq -nc --arg event "$EVENT" --arg ctx "$REMINDER" '{
  hookSpecificOutput: {
    hookEventName: $event,
    additionalContext: $ctx
  }
}'
