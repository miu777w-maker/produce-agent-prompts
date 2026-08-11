# Produce Agent Prompts：首版成品检查点

> 日期：2026-08-11  
> 主线阶段：正式 Skill 编写与静态校验  
> 状态：首版文件完成，待场景演练与最终验收。

## 一、正式成品位置

`/Users/miumiu777/Desktop/AI work/prd/produce-agent-prompts/`

该文件夹是独立、自包含的未来 Git 仓库根目录，不依赖当前设计档案或资金安全顾问知识库路径。

## 二、已完成

- 初始化标准 Skill 文件夹；
- 完成跨环境核心 `SKILL.md`；
- 完成六份渐进式披露 references；
- 完成标准库确定性校验脚本；
- 保留 Codex 可选 `agents/openai.yaml`，不承载核心规则；
- 明确 Codex、Claude 及其他文件夹式 Skill 环境的可移植性；
- 用最小合格 prompt 包测试校验脚本，得到 16 项通过、0 警告、0 失败；
- 运行等价结构检查，确认 frontmatter、名称、文件、引用入口和主文件行数符合通用要求。
- 根据首版评审补充启用后的任务预检：先区分 prompts、evals、inspection；生产 prompts 时再判断人员是否已有清单；已有未完成任务时先恢复或新建。
- 根据首版评审明确混合知识处理边界：Agent 在理解和架构映射时区分知识作用，但不设为独立硬门禁；仅在多 Agent、作用域混淆、来源冲突或需要人工审阅时输出知识作用地图。

## 三、校验环境说明

官方 `quick_validate.py` 因本机缺少 `yaml` 模块未能运行。该失败不是 Skill 内容失败。已改用不依赖第三方库的等价检查验证：

- frontmatter 仅含 `name` 和 `description`；
- 名称字符和长度；
- 必需文件存在；
- `SKILL.md` 少于 500 行；
- 自带脚本可以编译和执行。

## 四、尚未完成

1. 目标驱动整套系统场景演练；
2. 明确清单的局部 prompt 场景演练；
3. 关键知识缺口阻塞与补全回归演练；
4. 突发分支和主线恢复演练；
5. 变化驱动影响分析演练；
6. 对照原始六点和后续明确要求完成最终验收；
7. 根据演练结果修订正式 Skill；
8. 最终交付确认。
9. 处理暂存任务 `19-pending-inspection-scope-and-attribution.md`：补审 inspection 是否覆盖 prompt 生产范围、清单完整性、知识库对照及错误/疏漏归因。
10. 处理暂存任务 `20-pending-knowledge-gap-deliverable-audit.md`：验证 Skill 是否能把关键知识缺口转化为可直接交给项目人员或前后端 Agent 的补全产物。
11. 复核 `21-first-claude-execution-feedback-intake.md` 中 P1–P5 的归因与建议，再决定正式修改范围。
12. 将 `22-inspection-subprotocol-design-v0.md` 和 `23-task-workflow-separation-v0.md` 并入正式 Skill：inspection、creation、revision、eval-only 四条流程分离，完整报告写入独立 Markdown 文件。

## 五、当前回归点

主线：Skill 场景演练。  
优先下一步：先用目标驱动的整套系统任务检验 Skill 能否从知识库推导 prompt 清单，并在关键知识缺失时正确停止。  
当前没有正在执行的分支；有 2 个已登记暂存项和 1 份待复核的真实执行反馈。

## 六、当前暂存分支

- 暂存项：Prompt 检验范围与问题归因；
- 记录位置：`19-pending-inspection-scope-and-attribution.md`；
- 当前动作：只登记，不立即修改正式 Skill；
- 回归条件：完成 Claude 初版审验或用户要求提前讨论；
- 主线不变：初版审验。
- 暂存项：提示词缺失知识补全产物审验；
- 记录位置：`20-pending-knowledge-gap-deliverable-audit.md`；
- 当前动作：验证已有机制是否足够，不立即扩张正式 Skill；
