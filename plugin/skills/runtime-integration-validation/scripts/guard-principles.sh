#!/bin/bash
# Guard principles hook for UserPromptSubmit. Injects a structured reminder
# (outer XML tag + markdown inside) to keep the AI aligned with runtime-integration-validation.

INPUT=$(cat)
EVENT=$(jq -r '.hook_event_name' <<< "$INPUT")

REMINDER=$(cat <<'EOF'
<runtime-integration-validation-reminder>
按你当前所处的流程位置,重点关注下方对应步骤的约束,同时兼顾全局原则。参照 runtime-integration-validation 技能行事。

## 全局原则
- **双环境定位**:本任务在后端仓库环境验证"实际怎样";"应该怎样"归 Creation / Inspection / Revision;互不替代、互不静默覆盖。
- **只读、只报告**:不改 Prompt、不改代码、不改 KB;不决定产品应迁就代码;不重审业务知识(角色 / 业务 / 语气 / 产品决策归人员)。
- **不静默选边 KB 或代码**:差异先归因。代码证"当前实际值",KB 证"预期设计",修哪边由人员裁定。
- **外部访问四条件**(齐备才进入):用户主动明确要求 + 提供后端仓库地址 + 说明目的范围 + 仅授权范围定向只读。缺任一即停,不越权获取。

## 流程(五步)
1. 确认授权——四条件齐备才进入。
2. 建立对照——读带元信息的 Prompt 生产稿(预期契约)+ KB 依据;按授权范围读后端代码 / Schema / 装配 / 钩子。
3. 逐项对照——装配顺序 / 每 Agent 实收消息 / 动态注入 / 工具契约 / 输出消费 / 异常 / 文件名 vs 配置 / 跨层冲突。
4. 差异归因(四类,不静默选边)——Prompt 误写 / KB 过时 / 后端偏差 / 无法判断。
5. 产出报告——预期 vs 实际对照表 + 归因 + 上线阻断项 + KB 补充请求 + 工程修改请求 + Prompt 问题(转 Prompt Revision)。

## 报告标注(完成 ≠ 通过)
有未解决上线阻断项 → 标"有阻断(未通过)",不可定稿,回验前不升通过;阻断清零 → 标"无阻断(可定稿)",转人员定稿。`final-runtime-prompt` 不由本任务产生——不删元信息、不改产物。
</runtime-integration-validation-reminder>
EOF
)

jq -nc --arg event "$EVENT" --arg ctx "$REMINDER" '{
  hookSpecificOutput: {
    hookEventName: $event,
    additionalContext: $ctx
  }
}'
