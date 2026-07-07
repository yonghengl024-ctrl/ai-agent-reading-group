# Assumption Audit

**Date:** 2026-06-18
**Stage:** 5 — Assumption Audit

---

## Extracted Assumptions

### [A1] 单企业市场势力

**Statement:** 市场中存在一个能够选择质量 \(q\) 与价格 \(p\) 的企业，企业具有市场势力并最大化利润。

**Where used in model:** Agents; Timing; Firm payoff; Equilibrium concept.

**Q1 — Necessity:** NECESSARY

**Justification:** 若企业没有市场势力，价格通常由竞争条件或边际成本决定，质量升级的价格传导与利润最大化扭曲会完全不同。

**Q2 — Economic motivation:** STRONG MOTIVATION

**Real-world counterpart:** 许多具有品牌、专利、差异化或平台控制力的企业可以同时选择质量与价格；但本模型不声称描述某个具体现实市场。

**Q3 — Standard in literature:** STANDARD

**Notes:** 垄断质量选择、质量版本化和价格歧视模型中的标准起点。

**Q4 — What breaks if relaxed:** 若引入竞争，均衡价格、质量选择和福利结论会取决于战略互动；需改用 oligopoly 或 Hotelling 扩展。

**Referee risk:** MEDIUM

**Binding:** YES

---

### [A2] 一维垂直质量

**Statement:** 产品质量由单一标量 \(q\in[0,\overline q]\) 表示，且所有消费者都认为更高 \(q\) 具有更高毛价值，只是重视程度不同。

**Where used in model:** Preferences; State variables; Outcome function.

**Q1 — Necessity:** PROBABLY NECESSARY

**Justification:** 一维质量使 cutoff 结构和清晰的质量升级比较静态成为可能。多维质量会引入水平错配，改变“升级”的含义。

**Q2 — Economic motivation:** WEAK MOTIVATION

**Real-world counterpart:** 某些产品有可排序质量维度，如耐用性、精度、安全性或服务可靠性；但许多真实产品质量是多维的。

**Q3 — Standard in literature:** STANDARD

**Notes:** 垂直差异化和质量选择模型的标准简化。

**Q4 — What breaks if relaxed:** 多维质量下，消费者可能对不同属性排序不一致，单一购买 cutoff 可能消失，赢家/输家不再按单调类型区间划分。

**Referee risk:** MEDIUM

**Binding:** YES

---

### [A3] 一维消费者类型与质量边际估值

**Statement:** 消费者类型 \(\theta\in[\underline\theta,overline\theta]\) 是一维标量，表示质量边际估值；\(0<\underline\theta<\overline\theta<\infty\)。

**Where used in model:** Agents; Information structure; Preferences; Demand cutoff.

**Q1 — Necessity:** NECESSARY

**Justification:** 类型异质性是分配效应、参与 cutoff 和质量升级导致部分消费者受损的核心来源。

**Q2 — Economic motivation:** STRONG MOTIVATION

**Real-world counterpart:** 消费者确实可能因收入、需求强度、使用频率或偏好不同而对质量有不同支付意愿。

**Q3 — Standard in literature:** STANDARD

**Notes:** 垂直差异化、screening、非线性定价中的常见设定。

**Q4 — What breaks if relaxed:** 若消费者同质，质量升级只需比较代表性消费者的质量收益与价格变化，分配与 cutoff 结果消失。

**Referee risk:** LOW

**Binding:** YES

---

### [A4] 连续分布、满支撑与正密度

**Statement:** 类型分布 \(F\) 连续可微，密度 \(f(\theta)>0\) 对所有 \(\theta\in\Theta\) 成立。

**Where used in model:** Timing; Information structure; Demand; Welfare integrals.

**Q1 — Necessity:** PROBABLY NECESSARY

**Justification:** 连续正密度支持 cutoff 分析和积分福利表达；但许多结果可在离散类型或弱连续条件下改写。

**Q2 — Economic motivation:** TECHNICAL ONLY

**Real-world counterpart:** 消费者类型连续分布是一种聚合近似，不是实证事实。

**Q3 — Standard in literature:** STANDARD

**Notes:** IO 与机制设计中用于可微比较静态的标准正则性假设。

**Q4 — What breaks if relaxed:** 离散类型下需求出现跳跃，价格最优化可能不光滑；比较静态和 cutoff 表达需要分段处理。

**Referee risk:** LOW

**Binding:** NO

---

### [A5] 准线性效用

**Statement:** 购买消费者的净效用为 \(u(\theta,q,p)=\theta v(q)-p\)，价格以线性方式进入效用。

**Where used in model:** Preferences; Purchase decision; Consumer surplus.

**Q1 — Necessity:** PROBABLY NECESSARY

**Justification:** 准线性效用使价格变化与质量收益可以直接相减，并使消费者剩余有简单表达。

**Q2 — Economic motivation:** WEAK MOTIVATION

**Real-world counterpart:** 当产品支出相对消费者收入较小，或收入效应可忽略时，准线性近似合理。

**Q3 — Standard in literature:** STANDARD

**Notes:** 局部福利分析和 IO 模型中的常见简化。

**Q4 — What breaks if relaxed:** 若存在显著收入效应，消费者剩余不再简单等于净效用积分，质量升级对低收入消费者的影响可能更强。

**Referee risk:** MEDIUM

**Binding:** YES

---

### [A6] 质量收益函数单调凹

**Statement:** \(v(0)=0\)、\(v'(q)>0\)、\(v''(q)\le0\)。质量提高增加毛效用，但边际收益弱递减。

**Where used in model:** Preferences; Utility decomposition; Planner benchmark.

**Q1 — Necessity:** PROBABLY NECESSARY

**Justification:** 单调性确保“质量升级”确实提高毛效用；凹性帮助得到唯一性和比较静态，但可能可弱化。

**Q2 — Economic motivation:** STRONG MOTIVATION

**Real-world counterpart:** 质量改善通常有正收益但边际递减，如耐用性、安全性或服务可靠性的提高。

**Q3 — Standard in literature:** STANDARD

**Notes:** 产品质量与消费者效用模型常用。

**Q4 — What breaks if relaxed:** 若 \(v'\le0\)，质量升级不再是升级；若 \(v\) 凸，可能产生角点、非唯一或过强的高质量偏好。

**Referee risk:** LOW

**Binding:** YES

---

### [A7] 质量成本递增且固定质量成本严格凸

**Statement:** 单位成本 \(c(q)\) 满足 \(c'(q)\ge0\)；固定质量成本 \(K(q)\) 满足 \(K(0)=0\)、\(K'(q)\ge0\)、\(K''(q)>0\)。

**Where used in model:** Firm payoff; Planner benchmark; Existence and interior characterization.

**Q1 — Necessity:** PROBABLY NECESSARY

**Justification:** 质量成本是价格上涨和企业质量选择扭曲的核心来源。严格凸性主要服务于内点和唯一性。

**Q2 — Economic motivation:** STRONG MOTIVATION

**Real-world counterpart:** 更高质量通常需要更高材料、研发、检验或服务成本，且高质量改进可能边际成本递增。

**Q3 — Standard in literature:** STANDARD

**Notes:** 质量选择模型中的常见成本结构。

**Q4 — What breaks if relaxed:** 若质量无成本，企业与规划者可能总是偏向最高质量；若成本非凸，可能出现多重局部最优。

**Referee risk:** LOW/MEDIUM

**Binding:** YES

---

### [A8] 质量与价格公开可观察

**Statement:** 消费者在购买前观察 \((q,p)\)，质量不是隐藏信息。

**Where used in model:** Timing; Information structure; Consumer strategy.

**Q1 — Necessity:** NECESSARY

**Justification:** 若质量不可观察，模型会变为逆向选择或信号传递；消费者对质量升级的效用反应也会取决于信念。

**Q2 — Economic motivation:** WEAK MOTIVATION

**Real-world counterpart:** 有些质量维度可通过标准、评测、品牌或体验观察；但许多质量是经验品或信任品属性。

**Q3 — Standard in literature:** COMMON BUT DISPUTED

**Notes:** 对风格化垂直质量模型标准，但在许多真实市场中较强。

**Q4 — What breaks if relaxed:** 需加入质量信号、声誉、认证或学习；质量升级可能无法完全转化为消费者感知效用。

**Referee risk:** MEDIUM

**Binding:** YES

---

### [A9] 企业可承诺质量与价格

**Statement:** 企业在消费者购买前承诺 \((q,p)\)，购买后不能降低质量或改价。

**Where used in model:** Timing; SPE; Consumer expectations.

**Q1 — Necessity:** NECESSARY

**Justification:** 若企业不能承诺质量，消费者会预期事后质量调整，均衡可能转为动态声誉或 hold-up 问题。

**Q2 — Economic motivation:** WEAK MOTIVATION

**Real-world counterpart:** 合同、质保、监管、品牌声誉或可验证标准可支持承诺；但并非所有市场都具备。

**Q3 — Standard in literature:** STANDARD

**Notes:** 静态产品质量模型通常假定可承诺质量。

**Q4 — What breaks if relaxed:** 需要动态模型；质量升级承诺可能不可信，福利结论可能反转。

**Referee risk:** MEDIUM

**Binding:** YES

---

### [A10] 消费者最多购买一单位

**Statement:** 每个消费者只作购买/不购买决定，不选择连续数量。

**Where used in model:** Consumer action space; Demand; Welfare integrals.

**Q1 — Necessity:** LIKELY DISPENSABLE

**Justification:** 单位需求简化了需求和 cutoff；连续数量需求可以作为扩展，但会改变公式。

**Q2 — Economic motivation:** STRONG MOTIVATION

**Real-world counterpart:** 许多耐用品、订阅服务或单件商品符合单位需求近似。

**Q3 — Standard in literature:** STANDARD

**Notes:** 离散购买和垂直差异化模型常用。

**Q4 — What breaks if relaxed:** 需求不再只是购买者质量；消费者可能同时调整数量与质量，福利分解更复杂。

**Referee risk:** LOW

**Binding:** NO

---

### [A11] 外部选项归一化为 0

**Statement:** 不购买效用 \(u_0(\theta)=0\)。

**Where used in model:** Purchase decision; Participation cutoff; Consumer surplus.

**Q1 — Necessity:** LIKELY DISPENSABLE

**Justification:** 常数外部选项可归一化为 0；若外部选项随类型变化，则结果会变得更复杂。

**Q2 — Economic motivation:** STRONG MOTIVATION

**Real-world counterpart:** 把不购买或消费外部替代品的效用作为基准。

**Q3 — Standard in literature:** STANDARD

**Notes:** 参与约束模型常用归一化。

**Q4 — What breaks if relaxed:** 类型依赖外部选项会改变参与 cutoff，可能产生反向或非单调参与。

**Referee risk:** LOW/MEDIUM

**Binding:** NO for normalization; YES if outside option is type-independent.

---

### [A12] 紧致质量与价格空间

**Statement:** 企业选择 \((q,p)\in[0,\overline q]\times[0,\overline p]\)，其中上界有限。

**Where used in model:** Action space; Existence.

**Q1 — Necessity:** PROBABLY NECESSARY

**Justification:** 用于保证最大化问题有解；但价格上界可能可由有限类型上界和零需求结构内生推出。

**Q2 — Economic motivation:** TECHNICAL ONLY

**Real-world counterpart:** 质量和价格存在技术、监管或市场可行边界，但显式上界主要是技术装置。

**Q3 — Standard in literature:** COMMON BUT DISPUTED

**Notes:** 紧致动作空间是存在性证明常见假设，但应避免看起来任意。

**Q4 — What breaks if relaxed:** 若动作空间非紧且利润不 coercive，最优解可能不存在或只存在 supremum。

**Referee risk:** MEDIUM

**Binding:** YES for existence proof; not necessarily for economic mechanism.

---

### [A13] 准线性价格支付且无预算约束

**Statement:** 消费者支付价格 \(p\) 不受显式收入或预算约束限制。

**Where used in model:** Consumer utility and purchase condition.

**Q1 — Necessity:** PROBABLY NECESSARY

**Justification:** 若引入预算约束，低收入消费者退出可能来自 liquidity 而非质量偏好或价格传导。

**Q2 — Economic motivation:** WEAK MOTIVATION

**Real-world counterpart:** 对小额商品合理；对大额耐用品、住房、医疗或教育等不一定合理。

**Q3 — Standard in literature:** STANDARD

**Notes:** 准线性 IO 模型常见。

**Q4 — What breaks if relaxed:** 需要二维类型（质量偏好和收入/预算），单 cutoff 结构可能失效。

**Referee risk:** MEDIUM

**Binding:** YES for one-dimensional tractability.

---

## Binding Assumptions Summary

The following assumptions are identified as BINDING — the main results likely depend on them fundamentally:

| Label | Assumption | Binding Reason |
|-------|-----------|----------------|
| A1 | 单企业市场势力 | 企业质量—价格选择和利润最大化扭曲依赖市场势力。 |
| A2 | 一维垂直质量 | 生成清晰质量升级和单调类型排序的基础。 |
| A3 | 一维消费者类型 | 分配效应、购买 cutoff 和赢家/输家区间依赖类型异质性。 |
| A5 | 准线性效用 | 允许质量收益与价格变化直接分解。 |
| A6 | 质量收益单调凹 | 确保质量升级具有正毛效用含义并支持比较静态。 |
| A7 | 质量成本递增/凸 | 生成价格传导和企业—规划者质量扭曲。 |
| A8 | 质量价格可观察 | 避免模型转向逆向选择或信号传递。 |
| A9 | 企业承诺 | 保证企业先选质量价格、消费者后购买的 SPE 结构。 |
| A12 | 紧致动作空间 | 支持均衡存在证明；需在后续弱化或解释。 |
| A13 | 无预算约束 | 保持一维类型 cutoff，避免收入约束混入机制。 |

---

## High Referee-Risk Assumptions

The following assumptions are likely to face referee challenges:

| Label | Assumption | Likely Objection | Suggested Response |
|-------|-----------|-----------------|-------------------|
| A2 | 一维垂直质量 | “真实质量是多维的，消费者不一定一致排序。” | 明确说明这是基线模型；多维质量作为扩展，当前目标是分离质量—价格—参与三渠道。 |
| A5/A13 | 准线性且无预算约束 | “低收入消费者的福利损失可能被低估。” | 把结果解释为支付意愿异质性模型，而非收入分配模型；后续可扩展到二维类型。 |
| A8 | 质量完全可观察 | “很多质量是经验品或信任品。” | 明确当前研究不是质量信号模型；若质量不可观察，应转入 signaling/adverse selection 扩展。 |
| A9 | 企业可承诺质量 | “企业可能事后降低质量。” | 以可验证标准、质保或声誉作为承诺动机；动态承诺问题作为扩展。 |
| A12 | 紧致价格上界 | “价格上界看起来任意。” | 在 Stage 6/7 中可证明最优价格不超过 \(\overline\theta v(q)\)，从而用需求为零的结构替代显式上界。 |

---

## Hidden Assumptions Found

The following assumptions are IMPLICIT in the model but not stated:

| Label | Hidden Assumption | Where It Matters |
|-------|------------------|-----------------|
| H1 | 消费者在无差异 \(\theta v(q)-p=0\) 时购买或不购买的 tie-breaking 不影响需求，因为该类型集合测度为零。 | Demand cutoff and existence. |
| H2 | 利润函数在边界 \(v(q)=0\) 处的需求定义需要单独处理。 | Demand and equilibrium at \(q=0\). |
| H3 | \(f\) 最好有界或至少积分良好，以保证 CS 和 TS 有限。 | Payoff consistency and welfare integrals. |
| H4 | 企业最优解可能在边界，后续命题若使用 FOC 必须明确内点条件。 | Stage 6 comparative statics. |
| H5 | 价格函数 \(p(q)\) 在质量升级比较静态中需要定义：是企业重新优化后的价格，还是外生 pass-through 规则。 | Quality-upgrade propositions. |

**Recommendation:** Make these assumptions explicit in Stage 6 (Proposition Generator) and in the final paper.

---

## Assumption Stacking Assessment

**Total explicit assumptions:** 13

**Total binding assumptions:** 10

**Assumption stacking risk:** MEDIUM

该模型的假设数量不低，但大部分是标准垂直质量/垄断定价模型中的常规结构。真正需要防止的是把一维质量、准线性效用、无预算约束和可观察质量同时解释为现实描述；它们应被明确标注为基线理论简化。Stage 6 的命题应分清哪些结果依赖质量成本、哪些依赖异质性，避免所有结论都由假设堆叠机械推出。

---

## Recommendations for Stage 6

Before generating propositions, consider:

1. 将价格空间上界弱化：证明任何最优价格可限制在 \([0,\overline\theta v(\overline q)]\) 或类似内生界内，以降低 A12 的 referee risk。
2. 每个核心命题必须明确质量升级后的价格 \(p_1) 是企业重新优化结果还是外生 pass-through 结果。
3. 至少生成一个非定义性福利命题：例如企业最优质量相对于总剩余最优或消费者剩余最优可能过高/过低的参数条件。
4. 将 tie-breaking、边界点和内点条件作为技术假设写入命题，避免后续证明出现漏洞。
