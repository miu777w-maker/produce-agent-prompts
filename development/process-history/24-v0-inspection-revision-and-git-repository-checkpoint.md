# V0 Inspection 修订与 Git 仓库检查点

> 日期：2026-08-11  
> 状态：正式 Skill 已更新，本地仓库待初始化/提交，远端地址待用户提供。

## 已并入正式 Skill

- Inspection、Creation、Revision、Eval-only 四条任务流程分离；
- Inspection 独立重建应有 prompt 体系并对比现有清单；
- 体系错误后仍继续分层审查现有 prompt；
- Inspection 只写独立 Markdown 报告，不自动修改；
- 知识缺口不阻止无关检查，但阻止受影响部分判定通过，并产出补全请求；
- 正式包 manifest 校验与草稿轻量检查分开；
- 项目知识契约决定权威源与派生导航关系；
- 整套 Inspection 明确必读 references；
- 任务流程与 Creation 清单来源不再共用“入口模式”术语；
- 完整正式产物必须落盘，对话只返回摘要、路径、状态和下一入口。

## 仓库结构

仓库根目录：`/Users/miumiu777/Desktop/AI work/prd/produce-agent-prompts/`

- 根目录本身是可直接安装的 Skill；
- `development/process-history/` 保存 00–23 设计与约束；
- `development/execution-feedback/` 保存首次 Claude 真实执行报告；
- `development/INDEX.md` 说明设计脉络、更新流程和发布边界。

## 已完成验证

- `SKILL.md` 少于 500 行；
- 四条流程及 reference 路由存在；
- 仓库运行文件和维护索引完整；
- Python 校验脚本编译通过；
- 最小合法 prompt 包：16 项通过、0 警告、0 失败；
- 校验范围仍只代表确定性结构，不代表行为评测通过。

## 尚待完成

- 初始化本地 Git 并提交首个版本；
- 获取用户指定的 GitHub/GitLab/其他远端仓库地址；
- 添加远端并推送；
- 用更新后的 Skill 重跑资金安全顾问整套 Inspection；
- 分别演练 Creation、Revision 和 Eval-only。
