---
name: prompt-creation
description: 新建 prompt 体系(不产 eval)。当用户想从项目知识库推导/生成 Agent 系统提示词(prompt 清单、职责、架构、运行时契约)时使用;也适用于"写 prompt""建 prompt 体系""生成系统提示词"等表述。遵循共同七项原则(shared/core-principles.md)。Prompt/Eval 独立生产。
hooks:
  UserPromptSubmit:
    - hooks:
        - type: command
          command: "${CLAUDE_PLUGIN_ROOT}/skills/prompt-creation/scripts/guard-principles.sh"
---

# Prompt Creation

新建 prompt 体系。**不生成 eval、不生成外部评测交接**。

## 共同原则
遵循 `${CLAUDE_PLUGIN_ROOT}/shared/core-principles.md`(plugin 内单一权威源)。本流程的七项执行映射见下。

## 本任务工具与授权
只读知识库、可写 Prompt;不访问后端、不写知识库、不产 Eval。**保留 Prompt 元信息**(不自动删);**定向检索**(不默认扫描全库);**不以职责声明对冲 system/task 冲突**(冲突须修知识库 / 装配)。关键资料缺失则停止并提出补充请求。涉及外部访问 / 子 Agent 时读 `${CLAUDE_PLUGIN_ROOT}/shared/tool-permissions.md` 共同清单。

## 五步主流程
1. **明确目标与范围**——目标 Agent/执行单元、范围、不可改变要求、清单来源(人员给定/目标驱动)。
2. **定向检索并形成正式文件清单**——文件数量、正式名称、目录、每份职责、运行时载体、加载时机。KB 有标准则服从,没有才提方案;关键资料缺失则停。
3. **按七项形成文件约束**——每个目标文件逐项落到具体结论(运行时看到什么/概念从哪来/需要哪些业务知识/负责和不负责什么/不该看到什么/哪些关键规则在此强调/有哪些冲突或待核验)。
4. **逐文件生成**——不私自命名、不合并、不多造文件、不产当前任务外的 eval 或交接。
5. **按七项及必要性倒查交付**——七项约束是否真进入正确文件;预期↔实际文件核对;每个执行单元是否只看到必需信息(信息可见性硬核对);证据不足诚实标记;每份额外产物是否必要。

## 本流程七项映射(指向 core-principles 权威定义)

| 七项 | prompt-creation 具体执行 |
| --- | --- |
| 需求先行 | 目标 Agent/执行单元、范围、不可改变要求、清单来源 |
| 运行环境 | 知识库是否有明确的运行时依据(工具/消息/状态/输出/异常);Prompt 是否忠实采用;缺依据则停止 + 补请求,**不写假定输入、不宣称已验证后端真实**(后端实证归 Runtime Validation) |
| 上下文绑定 | prompt 中术语/概念在执行时机是否有真实注入来源 |
| 业务背景 | 角色/目标/边界/语气是否忠实知识库 |
| 职责与可见性 | 每个执行单元是否只看到必需信息;职责唯一;共享底座不吞并局部细节 |
| 关键约束 | 高风险规则在有效载体/时机;anchor 有真实钩子和必要性 |
| 知识错误 | prompt 是否误读/漂移/引入无来源规则 |

## shared 读取

- 启动:`${CLAUDE_PLUGIN_ROOT}/shared/core-principles.md`(七项宪法)+ 本任务工具与授权行。
- 涉及外部访问 / 子 Agent 时:`${CLAUDE_PLUGIN_ROOT}/shared/tool-permissions.md` 共同清单。
- 每轮 UserPromptSubmit 自动注入压缩版 reminder(guard 脚本),上下文压缩后仍生效;完整流程以本 SKILL.md 为准。
