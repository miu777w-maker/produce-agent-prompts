# Produce Agent Prompts:Plugin 拆分 v2 审查修正 + 原型验证计划

> 日期:2026-08-12  
> 状态:**修正补丁 + 原型计划,未实施,未修改任何运行 skill 文件**。  
> 依据:`31-plugin-split-revised.md`(v2)+ 审查(4.4/5,4 点修正到 4.7,下一阶段=跨平台原型验证)。  
> 本文件是 31 号的修正补丁,不重复其全文;正式结构以 31 + 本文件为准。

## 一、4 点实施前修正(落实审查)

### 修正 1:Revision 不得自动同步修改 Eval(5 分)

改 31 号 §三 prompt-revision 七项映射最后一行。

- 旧:"prompt 与 eval 各自是否需同步"——"同步"易被执行 Agent 理解为"改 Prompt 时同步改 Eval"。
- 新:**"识别该变更是否影响独立 Eval 体系;若影响,仅记录 Eval 重新评估需求并交回 `agent-eval-creation` 流程,不在 Prompt Revision 中直接修改 Eval,除非用户另行启动并授权 Eval 修订。"**
- Eval 修订入口:暂由 `agent-eval-creation` 承担"新建或修订整体 Eval";未来若频次足够,再拆 `agent-eval-revision`。Prompt Revision 只改获授权的 Prompt 范围,可发现 Eval 受影响,但不跨入 Eval 修改。

### 修正 2:Inspection 只在显式范围加载 Eval(4 分)

改 31 号 §三 prompt-inspection 映射与 prompt-inspection skill:

- 检查 Prompt 时**默认不加载 Eval**;
- 仅当用户选"整体系统检查"或**明确把 Eval 纳入范围**时才加载;
- 检查 Eval 时**不得以现有 Prompt 作为正确答案**(Eval 独立追溯);
- 可检查 Prompt 与 Eval 是否冲突,但**归因必须回到知识库、目标和运行时事实**,不默认因"完整审查"而加载全部 Eval。

### 修正 3:统一 skill 内 `_shared/`,消除两套引用路径(5 分)

改 31 号 §五(发布同步)。31 号写了三种引用态(源 `../../shared/` + Claude 根 `shared/` + 发布 `_shared/`),审查指出同一份 SKILL.md 在不同发布形态需不同路径,有风险。改为**单一运行契约**:

- **源仓库 `shared/`**:七项等横切协议的**唯一权威**(开发与审查以此为准)。
- **每个 skill 运行时引用 skill 内 `_shared/xxx.md`**(不是 `../../shared/`)。
- **`_shared/` 是构建产物**:由 `scripts/sync-shared.py` 从根 `shared/` 生成,进入 git,但有一致性脚本防止漂移。
- **所有宿主(Claude / Codex)运行时统一读 skill 内 `_shared/`**;Claude Plugin 也用 skill 内 `_shared/`,**不建立第二种读取方式**。
- 根 `shared/` 不被任何运行时直接引用,只作权威源 + 同步源。

代价:仓库存在生成副本 `_shared/`;换得:运行契约单一、跨环境一致、无需重写引用。

### 修正 4:重新审查校验脚本(5 分)

审查担心脚本仍带"一 Prompt 一 Eval"假设。**澄清**:脚本在 v0.3(commit `1417742`)已去除该假设——改为 `prompt_units` 与 `eval_scenarios` 独立校验、拒绝 legacy `units`、加 `file_field` 唯一性与 status/eval 一致性检查(见 `29-v0-3-revision-checkpoint.md` 的脚本回归证据)。

重新判断归属:

- **检查对象**:正式产物包 `prompt-package.json` 的结构;Prompt/Eval 分离后仍成立(包内 `prompt_units` 和 `eval_scenarios` 各自独立校验,不要求配对)。
- **不专属单一 skill**:它是包级校验,产生包的 skill(prompt-creation、agent-eval-creation)都用。
- **发布归属**:plugin 根 `scripts/` 保留权威源;发布同步时复制到产生包的 skill 的 `scripts/`(走与 `_shared/` 一致的同步机制)。
- **需复核**:分离后哪些校验项归 prompt-creation 产物、哪些归 eval-creation 产物、是否有该拆成两个脚本的部分——留到正式迁移时逐项判断,不在原型阶段做。

## 二、2 个 4 分建议

### 建议 1:`core-principles.md` 内部分层(避免启动读全文)

若 core-principles 含每项完整证据要求/失败条件/倒查,所有子 skill 启动都加载整套详细规则,违背渐进披露。分层:

- **开头:七项简明宪法**(所有任务启动读,很短,每项一两句);
- **后部:各项详细判据**(仅在相应任务步骤需要时读)。

审查标准是**启动实际加载量,不是文件数**。倾向:**单文件、内部明确分层**(开头标"启动读",后部标"按需读"),不拆文件;若单文件无法兼顾"开头极短 + 后部详尽",再拆 `core-principles.md`(宪法)+ `core-gates-detail.md`(判据,按需)。

### 建议 2:指挥官只一句共同约束,不复制七项概要

指挥官 SKILL.md **不写七项概要**,只一句:

> 选定任务后,由目标任务 skill 加载 `_shared/core-principles.md` 并执行。

避免"指挥官概要 + core-principles 正文 + 子 skill 映射"三个表达版本。

## 三、原型验证计划(审查建议的下一阶段)

审查明确:下一阶段是**跨平台目录与加载契约原型验证**,不是完整迁移。原型不迁移正式内容、不删旧结构。

### 原型构成(最小)

- `.claude-plugin/plugin.json`;
- `skills/produce-agent-prompts/SKILL.md`(指挥官,只路由 + 一句共同约束);
- `skills/prompt-creation/SKILL.md`、`skills/agent-eval-creation/SKILL.md`(两个最小子 skill,各含七项映射骨架 + 五步/对应主流程骨架 + 引用 `_shared/`);
- `shared/core-principles.md`(七项简明宪法);
- `scripts/sync-shared.py` + 一致性检查(生成并校验各 skill 的 `_shared/` 不漂移)。

### 6 个验证项(审查列出)

1. Claude 能否发现指挥官 + 子 skill;
2. Codex 能否独立安装其中任一 skill;
3. 两边能否读取 skill 内 `_shared/`;
4. 指挥官路由后是否只加载目标 skill;
5. 直接调子 skill 是否无需先加载指挥官;
6. 更新根 `shared/` 后,发布同步能否检测并消除 `_shared/` 副本漂移。

### 验证方法与所需协助

- **Claude 端(1、3、4、5、6)**:我可搭建原型并本地验证。
- **Codex 端(2、3 的 Codex 侧)**:**需用户协助实测**——我不掌握 Codex 的 skill/agent 安装机制与目录读取规则。实施前需用户说明 Codex skill 形态(目录结构、清单格式、是否支持 skill 内子目录引用),或由用户在 Codex 环境跑一次安装与读取验证。

### 原型与现有结构共存

- 原型在**新 git 分支**(如 `v0.4-plugin-prototype`)搭建;`main` 保持 v0.3 已发布状态。
- 原型阶段**不删**旧 `SKILL.md` / `references/`,**不迁移**正式内容;两者并存于不同分支。
- 原型验证通过后,再按 31 号 §八迁移映射做正式迁移并删旧,合并到 main。

### 原型不包含

四个流程的正式内容(七项详细判据、检索停止协议、artifact-boundaries 详细、templates、脚本拆分判断)——均留到正式迁移。

## 四、下一步选择

- **选项 A**:先把 4 点修正 + 2 建议并出提案 v3(31+32 合并再审),审到 4.7 再进原型;
- **选项 B(推荐)**:4 点修正已明确,直接进入原型搭建(最小结构,不迁移正式内容,在新分支),原型验证 + Codex 实测通过后再正式迁移。审查已批准"进入结构验证原型",4 点修正在原型结构里直接落实(Revision 措辞与 Inspection 边界是 skill 内容、`_shared/` 统一是原型结构核心、脚本审查是原型一部分),不必再单独审文字提案。

若选 B,我先需要用户回答一个问题以避免返工:**Codex 的 skill 形态是什么**(目录结构、清单文件、是否允许 skill 内 `_shared/` 子目录)?这决定原型 `_shared/` 契约能否在 Codex 成立,是验证项 2、3 的前提。
