# Produce Agent Prompts V0.2 发布检查点

> 日期：2026-08-12  
> 状态：正式文件完成，规则级验证通过，待 Git 提交和推送。

## 发布定位

- Inspection：经过两次整套系统真实执行，第二次回归通过；
- Creation：协议就绪，即将进入首次真实知识库生产；
- Revision、Eval-only：协议存在但未端到端验证；
- 外部评测到 final-ready：尚未端到端验证。

## 本版修改

- 新增 `inspection-blocked` 与状态汇聚；
- 增加六项门禁的 Inspection 视角；
- 集中运行时证据不足时的分组、降级和工程取证；
- 增加已有 eval 的审查检查表；
- 明确八阶段属于 Creation；
- 将独立重建应有 prompt 清单提升为核心规则；
- 允许范围确认前的轻量 orient；
- 提供可覆盖的默认输出目录；
- 知识补全与运行时取证分别落为独立 Markdown；
- 新增 `VERSION.md`，明确已验证和未验证能力。

## 未加入

- 不新增输入供给独立门禁；
- 不增加一页式 references；
- 不强制 transcript；
- 不绑定宿主记忆系统；
- 不把未验证流程宣称成熟。

## 验证结果

- Inspection blocked 状态：通过；
- Inspection fail 优先于 blocked：通过；
- Creation 关键知识缺口停止生成：通过；
- Creation 就绪后逐单元 prompt + eval：通过；
- 运行时证据分组和统一取证：通过；
- 独立重建 prompt 清单核心规则：通过；
- Creation 八阶段标识：通过；
- 补全与取证独立落盘：通过；
- 校验脚本最小合法包：16 项通过、0 警告、0 失败；
- 跨平台结构：通过，`SKILL.md` 111 行。

以上为协议和确定性验证，不等于 Creation 实际生成质量或外部行为通过。

## 下一主线

用 V0.2 在项目知识库中启动首次正式 Creation。执行时按 `26-v0-2-release-scope-and-first-principles-audit.md` 的十项观察清单留存反馈。
