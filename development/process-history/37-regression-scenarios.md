# 回归场景清单(三层结构 + 工具权限 + 第五 Skill)

> 日期:2026-08-13  
> 26 条,按归属层分类。原型阶段先记录;正式迁移后随各 skill / shared 落地为可执行检查。未写死项目字段。

## 结构与范围(prompt-creation)

1. KB 定义 N 文件时准确生成 N(本项目实证:8);2. 不私自命名/合并/多造;3. Prompt Creation 不产 Eval 与外部交接;20. 无明确消费者的过程文件不生成。

## 层 4 · 真实装配与跨层冲突(core-principles 层4 + runtime-integration-validation)

4. **system 与 task 相互冲突必须 fail**(如"不负责门禁" vs 要求执行门禁);5. 执行单元看到明显无关规则触发渐进披露问题;6. **职责矩阵与真实消息装配不一致不能通过**;22. **职责声明不得对冲 system 冲突,冲突须修架构/装配**(职责声明不作减免)。

## 运行时诚实(core-principles + runtime-evidence)

7. 无代码/Schema/日志时知识库阶段不得声称运行时已验证;26. **代码证"当前实际"、KB 证"预期设计",差异归因(四类),不自动以任一方覆盖**。

## 元信息生命周期(core-principles + 元信息约定)

8. 生产阶段保留元信息;9. 未经授权不自动删元信息;10. 后端校验前不删元信息;11. 实验必须记录元信息是否进入模型上下文;25. `validation-passed` 与 `final-runtime-prompt`(人工删元信息后)分离,不混淆。

## 工具使用与授权(tool-permissions + 各 task skill)

12. 默认不主动访问其他仓库;13. 用户未给仓库地址/范围时必须停止外部核查;14. 用户明确授权后只在指定仓库和范围只读;21. **任务启动先读本任务权限行,再任何搜索/读写**。

## Runtime Integration Validation(第五 skill)

15. 工具字段与后端 Schema 不一致时发现并归因;16. 动态上下文注入位置与 KB 描述不一致时发现并归因;17. 后端事实与 KB 冲突时不静默选边;23. **Runtime Validation 不改 Prompt/KB/代码,只读只报告**;24. **Runtime Validation 不重审角色/业务/语气/产品决策**(不吞并 Inspection)。

## 任务独立性(agent-eval-creation + prompt-revision)

18. Eval 独立从 KB 与完整 Agent 目标推导,不形成 Prompt→Eval 一一对应;19. Revision 不因 Prompt 变化自动跨流程修改 Eval。

## 归宿说明

- 结构/范围/Eval 独立/Revision 独立 → 各 task skill 七项映射 + 主流程。
- 层4/跨层冲突/真实装配 → core-principles 层4 硬核对 + runtime-integration-validation。
- 运行时诚实/差异归因 → core-principles + runtime-evidence(正式迁移)+ runtime-integration-validation。
- 元信息 → core-principles 元信息约定(四态先作生产约定)。
- 工具权限/外部边界/启动读 → tool-permissions.md + 各 skill 权限行。
- Runtime Validation 只读边界/范围 → runtime-integration-validation SKILL.md。

正式迁移后,每条转为对应载体里的可执行检查项或测试用例。
