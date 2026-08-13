# 工具使用与授权协议 · 第五 Skill 原型实施

> 日期:2026-08-13  
> 依据:35 号(4.7/5,批准原型实施)+ 审查概念边界 + 三点补充。  
> 状态:本轮在 `v0.4-plugin-prototype` 分支**增量实施原型**;未全量迁移旧 references,未删旧结构,未改项目 Prompt/Eval/KB/代码。

## 一、必须补的概念边界(审查)

- 第三层准确命名为 **"工具使用与授权协议"**(不叫"工具及权限范畴层",不暗示能强制)。
- **Skill 规定宿主 Agent 在特定任务中的行为、流程和授权边界;工具本身由宿主提供,技术权限由运行环境强制。Skill 的权限协议不冒充系统级权限控制。**
- 三层能力区分:
  - **逻辑授权**:Skill 规定本任务能不能做某事(如访问后端仓库)。
  - **技术能力**:宿主实际向 Agent 提供哪些工具(如文件系统读取)。
  - **技术限制**:沙箱或权限系统是否真正阻止。
- 表述修正(替换 35 号"升级为可执行权限协议"):**"使外部边界成为任务执行前必须检查和遵守的授权协议;如宿主支持权限隔离,再同步配置技术权限。"**

## 二、三点补充(审查)

1. **权限协议启动前必读(5 分)**:任务 Skill 启动 → 读取本任务权限行 + 禁止清单 + 外部访问授权条件 → 再进行任何知识库搜索、文件读取或写入。不能"需要访问外部仓库时再读"——决定访问前必须知道有无授权。
2. **区分规则约束与技术权限(4 分)**:`tool-permissions.md` 约束 Agent 行为(逻辑授权),未必能从技术上撤销工具。宿主若给整个文件系统读能力,Skill 只能告诉它不要访问后端仓库,不能保证系统层阻止。
3. **"调其他 Agent"不宜永久全禁(3 分)**:默认禁止直接联系其他项目 Agent 取正式知识;但**用户明确授权且宿主支持范围继承时**,可调用受控子 Agent 协助只读检查(继承相同仓库/范围/只读;发现属本次证据,不自动写回 KB)。表述为"默认禁止,除非用户明确授权且宿主支持范围继承"。

## 三、第五 Skill 批准

- 名称 **`runtime-integration-validation`**(检查对象含消息装配/动态上下文/工具 Schema/输出消费/异常路径/文件配置/注入钩子,不只 Prompt 文本)。
- 只读边界:输入(带元信息生产稿 + KB 依据 + 用户授权后端仓库 + 授权范围)→ 输出(预期 vs 实际对照 / 差异归因 / 上线阻断项 / KB 补充请求 / 工程修改请求)→ 默认**只读、只报告**。
- **不顺便**:改 Prompt、改代码、改 KB、决定产品迁就代码、重审全部业务知识。

## 四、状态(两态,不引入四套机器状态)

`validation-passed`(验证完成、可定稿,元信息仍在)→ 人员手动定稿删元信息 → `final-runtime-prompt`(运行稿)。生产稿/后端校验候选/待定稿先作文档生命周期说明,首次 Runtime Validation 执行后再判断是否需程序化状态。

## 五、本轮实施清单(审查授权 7 项)

1. `shared/tool-permissions.md`:5 任务权限矩阵 + 外部访问四条件 + 禁止清单 + 启动前必读 + 逻辑/技术能力区分 + 子 Agent 规则。
2. `skills/runtime-integration-validation/SKILL.md`:最小原型(目标/职责/七项映射对照版/主流程/权限行/只读边界)。
3. 五任务权限行:`tool-permissions.md` 矩阵列五行;已建 skill(prompt-creation/agent-eval-creation/runtime-integration-validation)在 SKILL.md 声明本任务权限行;inspection/revision 暂在矩阵声明(原型后建)。
4. `shared/core-principles.md`:加"工具使用与授权协议"概念边界节 + 启动前必读要求。
5. 指挥官 `skills/produce-agent-prompts/SKILL.md`:路由加 runtime-integration-validation(用户授权后)。
6. 回归测试场景清单(20+ 条分类归宿)。
7. Claude/Codex 验证(Claude 本地结构 + 加载;Codex 待用户实测)。

## 六、实施记录

本轮在 `v0.4-plugin-prototype` 分支完成的增量:

- **新增** `shared/tool-permissions.md`:三层能力区分 + 启动前必读 + 5 任务权限矩阵 + 外部访问四条件 + 禁止清单 + 子 Agent 规则。
- **新增** `skills/runtime-integration-validation/SKILL.md`:第五 skill 最小原型(只读边界 + 核验范围限定 + 主流程 + 七项映射对照版 + 权限行)。
- **增补** `shared/core-principles.md`:新增"工具使用与授权协议"节(概念边界:逻辑授权/技术能力/技术限制,Skill 不冒充系统权限 + 启动前必读)。
- **更新** `skills/prompt-creation/SKILL.md`、`skills/agent-eval-creation/SKILL.md`:各加"本任务工具与授权"权限行 + 启动前必读引用。
- **更新** `skills/produce-agent-prompts/SKILL.md`(指挥官):路由表加 `runtime-integration-validation`。
- **新增** `development/process-history/37-regression-scenarios.md`:26 条回归场景按归属层分类。

sync-shared 验证:4 skill(produce-agent-prompts / prompt-creation / agent-eval-creation / runtime-integration-validation)的 `_shared/` 各含 `core-principles.md` + `tool-permissions.md`,`check` 一致(2 文件 × 4 skill)。三个 task skill 均含"本任务工具与授权"权限行与"启动后先读本权限行"。指挥官路由含第五 skill。

未做(遵守审查边界):全量迁移旧 references、删旧结构、宣称第五 skill 成熟、写死项目字段、改资金安全顾问 Prompt/后端代码。

## 七、本轮仍不做

全量迁移旧 references;删除旧结构;宣称第五 Skill 已成熟;把项目字段(event/event_context/G1-G3/工具名)写入通用规则;自动修改资金安全顾问 Prompt 或后端代码。
