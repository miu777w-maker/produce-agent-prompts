# 运行层删减审查报告(D1–D5)+ 测试体系审视

> 日期:2026-08-13
> 用途:交审查 agent。**自包含**——据此可逐条判断删减是否到位、测试去留是否合理。
> 状态:**D1–D5 已在工作区执行(未提交)**。计划经用户批准后落地;用户随后要求"先出报告交审、审完再动手",故停止后续动作(sync / 安装副本 / 新删减)。审查可逐条定夺保留 / 调整 / 回滚。

## 一、背景与判据

审查最新判断:Skill 已"为保证正确而不断加结构",复杂度超核心任务。评分:核心思想 4.8、职责边界 4.5、渐进披露 3.5、**执行简洁 3/5**、**过度设计风险 4/5**。

单条判据:**删除某规则,是否导致 ①Prompt 范围错误 ②内容错误 ③越权访问 ④无法发现上线风险?都不会 → 从运行 Skill 删除或降到开发历史。**

目标:**复杂性留在验证体系(`tests/`、`process-history/`),不进入每次任务的执行上下文。**

## 二、范围

- **删减对象 = 运行层**(执行任务时载入):6 文件。
- **不动 = 验证体系**:`tests/`、`development/process-history/`、`references/`(v0.3 旧,已不在 v0.4 加载路径)。
- 不改项目 Prompt / Eval / KB / 后端代码。

## 三、删减 D1–D5(逐条:改前 → 改后 + 判据)

### D1 · 消除 core-principles ↔ tool-permissions 概念边界重复
- **改前**:`shared/core-principles.md` 19–31 行有完整"工具使用与授权协议"节(三层能力定义:逻辑授权 / 技术能力 / 技术限制 + 概念边界 + 启动前必读),与 `tool-permissions.md` 7–17 行**重复定义**。
- **改后**:该节压缩为一句——"工具与授权见 `_shared/tool-permissions.md`(任务启动前必读:本任务权限行 + 禁止清单 + 外部访问四条件)。本文件只定义七项原则。"
- **判据**:三层能力全文留在 `tool-permissions.md`(权威),不丢信息;core-principles 回归"七项唯一完整定义"。✅
- **行数**:37 → 27。

### D2 · 精简 3 个 task skill 权限行(不复述矩阵)
- **改前**:prompt-creation / agent-eval-creation / runtime-integration-validation 各自"本任务工具与授权"行**完整复述**了 `tool-permissions.md` 矩阵的本任务行(KB 读 / Prompt 写 / Eval 不访问 / 后端禁止 / ...)。
- **改后**:改为"启动读 `_shared/tool-permissions.md` 本任务权限行 + 禁止清单" + **本任务最关键的一两条禁止**(如 prompt-creation:不访问后端、不写 KB、不产 eval)。
- **判据**:矩阵是权威,skill 只指向 + 点关键禁止;Agent 启动读权威文件即获完整权限,不丢信息。✅

### D3 · 删除预建未执行的状态机(prompt-creation / agent-eval-creation)
- **改前**:prompt-creation `design-not-ready → prompt-static-passed`;agent-eval-creation `eval-design-not-ready → awaiting-external-evaluation`。均为原型占位、未真实执行。
- **改后**:删除两处"状态(原型占位)"节;产物完成即交付。
- **判据**:状态名预建,删除不影响范围 / 内容 / 越权 / 上线风险(由七项 + 权限保证);审查"为尚未真实出现的问题预先增加状态 → 删"。✅
- **行数**:prompt-creation 44 → 41;agent-eval-creation 46 → 43。

### D4 · runtime 三态:保留"完成≠通过",降为报告标注(去状态机形式)
- **改前**:runtime-integration-validation 状态节定义 `validation-completed-with-blockers` / `validation-passed` / `final-runtime-prompt` 三态**状态机**(P0-1 改,37 号审查要"完成 vs 通过"区分)。
- **改后**:节标题"状态"→"**报告标注(完成 ≠ 通过)**";两标签保留为**报告标签(非流转状态机)**;新增"不预设正式状态机,首次真实执行后再定"。`final-runtime-prompt` "不由本任务产生"边界保留。
- **判据**:化解 37 号(要区分)与本次(状态太多)的张力——概念区分保留不丢正确性,去掉为未执行定稿流程预建的"状态机形式"。✅
- **兼容性**:EX-05(ex-05 fixture + 39 号)测"报告标注是否正确反映阻断",与降级后一致,**无需改测试**。

### D5 · 叫停 P1 测试扩展(39 号下一步第 5 步)
- **改前**:39 号下一步第 5 步"再扩展六个原始七项场景为可执行样本"。
- **改后**:"**暂不扩展**;先 Claude/Codex 真跑现有 7 条,确认能抓失败;达标后再决定是否扩展。"
- **判据**:审查"不要把全部 26 条改成正式测试""保留少量高风险"。✅

## 四、运行层删减前后

| 文件 | 删前 | 删后 | 涉及 |
| --- | --- | --- | --- |
| `shared/core-principles.md` | 37 | 27 | D1 |
| `skills/prompt-creation/SKILL.md` | 44 | 41 | D2, D3 |
| `skills/agent-eval-creation/SKILL.md` | 46 | 43 | D2, D3 |
| `skills/runtime-integration-validation/SKILL.md` | 53 | 53 | D2, D4(去状态机形式,行数持平) |
| `shared/tool-permissions.md` | 65 | 65 | 未动(权限唯一权威) |
| `skills/produce-agent-prompts/SKILL.md` | 29 | 29 | 未动(纯路由) |
| **总** | **274** | **258** | |

> 行数减少有限;**价值在消除三类重复 + 去预建状态机**,使一次任务执行不再载入冗余概念 / 状态。

## 五、测试体系审视(39 号 + 7 fixture / 45 文件)

| 维度 | 判断 | 依据 |
| --- | --- | --- |
| 定位 | **验证体系侧,不进执行上下文** | 运行层 6 文件**无一处引用 `tests/`**;Agent 执行任务不载入测试 |
| 去留 | **保留** | 审查明确"保留少量高风险回归测试";7 条是**上一轮审查明确要求**建(非 26 条全改);删测试 → "无法发现上线风险"(判据④) |
| 扩展 | **叫停**(D5) | 审查"先真跑这六条";P1 六类→26 条暂不做 |
| 内部冗余 | 无明显可删 | 39 号 11 字段格式是审查要的;fixture 的 user-request / authorization / run / expected 结构是审查给的模板 |

**结论:测试体系不过度——正落在"验证体系"侧,是审查认可的少量高风险集。**

## 六、不删清单(审查保留项,确认删减后仍可定位)

| 审查保留项 | 删减后定位 |
| --- | --- |
| 七项原则 | core-principles(D1 后更纯) |
| 五任务边界 | 各 SKILL 职责声明 + 指挥官路由 |
| KB / 后端来源边界 | core-principles 七项第 2/7 项 + 各 skill |
| 外部仓库授权四条件 | tool-permissions(D1 后唯一权威) |
| 缺关键资料停止 | prompt-creation 五步第 2 步 + tool-permissions 禁止清单 |
| Prompt / Eval 独立 | 指挥官概念节 + agent-eval-creation |
| 文件范围服从 KB | prompt-creation 五步第 2 步 |
| Runtime 只读只报告 | runtime SKILL 只读边界节(保留) |
| 元信息定稿前保留 | core-principles 七项 + 各处约定(D4 保留"不由本任务产生") |
| 少量高风险测试 | tests/ 7 fixture(验证体系,不动) |

**删减只去重复 / 去预建状态,不丢必要规则。**

## 七、当前状态与可回滚性

- D1–D5 **已改工作区,未提交**。
- git 状态:`core-principles.md` / `prompt-creation/SKILL.md` / `agent-eval-creation/SKILL.md` = **M**(相对 HEAD ba106aa);`runtime-integration-validation/SKILL.md` / `39-executable-regression-tests.md` = **??**(对 HEAD 是新文件)。
- **可逐条回滚**:D1–D5 每条改动独立,审查不要某条可手动还原该段(改前内容已记录在本报告"改前")。
- ⚠️ `git checkout` 会回到 v0.4 基线 ba106aa(连带丢 P0-1 等本轮更早改动),**不推荐**用于回滚单条。
- **未做**(待审查定稿):`_shared/` 同步、`~/.claude/skills/` 安装副本更新、真跑 EX-01。

## 八、待审查确认

1. D1–D5 每条是否到位 / 需调整 / 需回滚。
2. 测试体系(39 号 + 7 fixture)去留是否认同。
3. D4 的"标签保留 + 去状态机形式"是否恰当化解 37 号与本次审查的张力。
4. 定稿后是否:同步 `_shared/` → 更新安装副本 → Claude/Codex 真跑 EX-01。

## 九、边界守恒

- 不碰 `tests/`、`references/`;`process-history/` 仅 39 号一处文案(D5)+ 本 40 号新增。
- 不改项目 Prompt / Eval / KB / 后端代码;不写死项目字段。
- 提交 / push 需用户确认(feature branch 可直接 push;main 需用户 `!`)。
