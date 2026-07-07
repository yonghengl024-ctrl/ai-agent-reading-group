# Proof Sketches

**Date:** 2026-06-18
**Stage:** 7 — Proof Sketches

---

## [P_E1] — Proof Sketch: Equilibrium Existence

**Claim (restated):**
> Under assumptions A1–A13, plus continuity of \(v,c,K,F\) and compactness of \(Q\times P\), there exists a subgame perfect equilibrium in which the firm chooses \((q^M,p^M)\in\arg\max_{(q,p)\in Q\times P}\Pi(q,p)\), and consumers purchase if and only if \(\theta v(q^M)-p^M\ge0\).

**Proof strategy:** 后向归纳 + Weierstrass 最大值定理。

**Key technique:** 消费者子博弈逐点最优化；企业利润函数在紧致集合上达到最大值。

**Proof sketch:**

1. **消费者子博弈最优反应** [SOLID]
   给定任意公开观察到的 \((q,p)\)，类型 \(\theta\) 消费者在购买效用 \(\theta v(q)-p\) 与不购买效用 0 之间选择较大者。由 A5、A8、A10、A11，购买规则为 \(a_\theta(q,p)=1\) 当且仅当 \(\theta v(q)-p\ge0\)。

2. **需求由 cutoff 诱导** [SOLID]
   若 \(v(q)>0\)，购买条件等价于 \(\theta\ge p/v(q)\)。由 A3、A4，需求在内点区域为 \(D(q,p)=1-F(p/v(q))\)，边界区域为全覆盖或零覆盖。

3. **处理无差异类型** [SOLID]
   若 \(\theta v(q)-p=0\)，消费者购买或不购买都最优。由 A4 的连续分布和 H1，无差异类型集合测度为零，因此不影响需求、利润或福利积分。

4. **企业目标函数定义良好** [PLAUSIBLE]
   企业利润为 \(\Pi(q,p)=[p-c(q)]D(q,p)-K(q)\)。在 \(v(q)>0\) 且 cutoff 不跳到边界的区域，\(D\) 连续；边界处需要按 Stage 4 的全覆盖/零覆盖定义检查连续性。若 \(v(0)=0\) 处单独定义需求，则可保持上半连续或通过限制 \(q>0\) 保持连续。

5. **企业最优解存在** [PLAUSIBLE]
   若 \(\Pi\) 连续，且 \(Q\times P\) 紧致，则由最大值定理存在 \((q^M,p^M)\in\arg\max\Pi(q,p)\)。A12 提供紧致性；A6、A7 提供函数连续性，但需要补充 \(D\) 在 \(q=0\) 的处理。

6. **构造 SPE** [SOLID]
   令企业选择任一利润最大化 \((q^M,p^M)\)，消费者在所有历史后按第 1 步规则购买。消费者策略在每个子博弈中最优；企业给定诱导需求选择最优 \((q,p)\)。因此该策略组合构成 SPE。

**Additional lemmas needed:**
- **Lemma E1.1:** 在包含 \(q=0\) 的域上，需求函数可定义为使 \(\Pi(q,p)\) 上半连续或连续。用于严谨应用最大值定理。
- **Lemma E1.2:** 最优价格可限制在有限区间，例如 \([0,\overline\theta v(\overline q)]\)，从而降低 A12 的任意性。

**Hardest step:** Step 4 — 需求函数在 \(q=0\) 和覆盖边界处的连续性需要细致处理。

**Rigor summary:** MOSTLY SOLID

**To complete this proof, one would need to:**
- 明确 \(q=0\) 时购买效用与需求的约定。
- 证明企业利润在所选动作空间上连续或至少上半连续。

---

## [P_U1] — Proof Sketch: Conditional Uniqueness

**Claim (restated):**
> If, in addition to P_E1 assumptions, the induced profit function \(\Pi(q,p)\) is strictly quasi-concave on \(Q\times P\), then the equilibrium quality—price pair \((q^M,p^M)\) is unique. Consumer strategies are unique except possibly for a measure-zero indifferent type.

**Proof strategy:** 严格准凹函数的最大化。

**Key technique:** 严格准凹性推出最大点唯一；连续分布推出 cutoff 类型测度为零。

**Proof sketch:**

1. **存在性沿用 P_E1** [SOLID]
   在 P_E1 条件下，\(\arg\max_{Q\times P}\Pi(q,p)\) 非空。

2. **严格准凹性排除两个不同最大点** [SOLID]
   若存在两个不同最大点 \(x_1=(q_1,p_1)\) 和 \(x_2=(q_2,p_2)\)，严格准凹性意味着对任意 \(\lambda\in(0,1)\)，\(\Pi(\lambda x_1+(1-\lambda)x_2)>\min\{\Pi(x_1),\Pi(x_2)\}\)，与二者同为全局最大矛盾。

3. **质量—价格对唯一** [SOLID]
   因而企业均衡选择 \((q^M,p^M)\) 唯一。

4. **消费者策略几乎处处唯一** [SOLID]
   对 \(\theta\ne p^M/v(q^M)\)，购买与不购买严格排序。只有 cutoff 类型可能无差异；由 A4 连续分布，其测度为零。

**Additional lemmas needed:**
- 无；但需在应用中给出使 \(\Pi\) 严格准凹的原始条件。

**Hardest step:** 不是证明本命题，而是为具体 \(v,c,K,F\) 验证 \(\Pi\) 严格准凹。

**Rigor summary:** NEAR-COMPLETE

**To complete this proof, one would need to:**
- 若论文需要唯一性，补充原始 primitives 下的严格准凹充分条件。

---

## [P_C1] — Proof Sketch: Individual Gain Threshold

**Claim (restated):**
> Consider a quality upgrade from \((q_0,p_0)\) to \((q_1,p_1)\), with \(q_1>q_0\) and \(\Delta v=v(q_1)-v(q_0)>0\). For any consumer type that buys in both regimes, net utility increases if and only if \(\theta>\theta^G\equiv\Delta p/\Delta v\), decreases if and only if \(\theta<\theta^G\), and is unchanged if \(\theta=\theta^G\).

**Proof strategy:** 直接计算。

**Key technique:** 准线性效用差分。

**Proof sketch:**

1. **写出两个制度下的效用** [SOLID]
   持续购买者在制度 \(i\in\{0,1\}\) 下净效用为 \(u_i(\theta)=\theta v(q_i)-p_i\)。

2. **计算差分** [SOLID]
   \(\Delta u_\theta=u_1(\theta)-u_0(\theta)=\theta[v(q_1)-v(q_0)]-(p_1-p_0)=\theta\Delta v-\Delta p\)。

3. **使用质量升级条件** [SOLID]
   由 \(q_1>q_0\) 和 A6 的 \(v'(q)>0\)，有 \(\Delta v>0\)。

4. **求符号阈值** [SOLID]
   \(\Delta u_\theta>0\) 等价于 \(\theta>\Delta p/\Delta v\)。等号和小于情形同理。

**Additional lemmas needed:**
- 无。

**Hardest step:** 无实质困难；该命题主要是支撑性分解。

**Rigor summary:** NEAR-COMPLETE

**To complete this proof, one would need to:**
- 在正式论文中明确该命题只适用于持续购买者；进入者和退出者由 P_M1 处理。

---

## [P_C2] — Proof Sketch: Consumer-Surplus Threshold for Quality Upgrading

**Claim (restated):**
> Let \(p(q)\) be a differentiable equilibrium or pass-through price schedule. In an interior market-coverage region where \(\theta^*(q)=p(q)/v(q)\in(\underline\theta,\overline\theta)\), a marginal quality increase raises aggregate consumer surplus if and only if the average quality valuation among current buyers times marginal quality utility exceeds price pass-through:
> \[
> \mathbb E[\theta\mid \theta\ge\theta^*(q)]v'(q)>p'(q).
> \]

**Proof strategy:** Leibniz 积分求导 + cutoff 边界项消失。

**Key technique:** 包含内生下限的积分求导；边际参与者净效用为零。

**Proof sketch:**

1. **写出内点消费者剩余** [SOLID]
   在 \(\theta^*(q)=p(q)/v(q)\in(\underline\theta,\overline\theta)\) 下，购买者为 \([\theta^*(q),\overline\theta]\)。因此
   \[
   CS(q)=\int_{\theta^*(q)}^{\overline\theta}[\theta v(q)-p(q)]f(\theta)d\theta.
   \]

2. **验证被积函数可微** [PLAUSIBLE]
   由 A4、A6 和假设 \(p(q)\) 可微，被积函数关于 \(q\) 可微。若 \(f\) 连续且有界，可交换求导和积分；该条件在 A4/H3 中应明确补充。

3. **应用 Leibniz rule** [SOLID]
   对 \(CS(q)\) 求导得到内部项加边界项：
   \[
   \frac{dCS}{dq}=\int_{\theta^*}^{\overline\theta}[\theta v'(q)-p'(q)]f(\theta)d\theta - [\theta^*v(q)-p(q)]f(\theta^*)\theta^{*\prime}(q).
   \]

4. **边界项消失** [SOLID]
   因为 \(\theta^*(q)=p(q)/v(q)\)，cutoff 类型满足 \(\theta^*v(q)-p(q)=0\)。所以边界项为零。

5. **整理为条件期望形式** [SOLID]
   内部项等于
   \[
   v'(q)\int_{\theta^*}^{\overline\theta}\theta f(\theta)d\theta-p'(q)\int_{\theta^*}^{\overline\theta}f(\theta)d\theta.
   \]
   令 \(D(q)=1-F(\theta^*)\)，可写为
   \[
   D(q)\left(\mathbb E[\theta\mid\theta\ge\theta^*]v'(q)-p'(q)\right).
   \]

6. **符号判定** [SOLID]
   内点覆盖下 \(D(q)>0\)，因此 \(dCS/dq>0\) 当且仅当括号内表达式为正。

**Additional lemmas needed:**
- **Lemma C2.1:** 在 A4/H3 条件下，Leibniz rule 可用于该消费者剩余积分。
- **Lemma C2.2:** 内点覆盖保证 \(D(q)>0\)。

**Hardest step:** Step 2 — 需要补充足够正则性，尤其 \(p(q)\) 的来源若是企业重新优化，则需由最大值/隐函数定理保证可微。

**Rigor summary:** MOSTLY SOLID

**To complete this proof, one would need to:**
- 明确 \(p(q)\) 是外生 pass-through 规则还是均衡价格函数。
- 若 \(p(q)\) 来自企业重新优化，证明局部唯一和可微性。

---

## [P_W1] — Proof Sketch: Firm-vs-Planner Quality Wedge

**Claim (restated):**
> 在同一购买覆盖集合下，利润最大化企业按边际购买者的质量估值选择质量，而总剩余规划者按所有被服务消费者的平均质量估值选择质量。只要购买者类型存在非退化异质性，平均被服务类型严格高于边际类型；因此企业相对于覆盖集合固定的总剩余规划者系统性低估质量的社会边际收益。

**Proof strategy:** 比较固定覆盖下的企业和规划者一阶条件。

**Key technique:** FOC 比较；条件均值大于截断下界。

**Proof sketch:**

1. **固定覆盖集合** [SOLID]
   固定 interior cutoff \(\theta^*\)，购买者集合为 \([\theta^*,\overline\theta]\)，需求 \(D=1-F(\theta^*)\)。该命题不是完整内生覆盖比较，而是固定覆盖下的边际质量 wedge。

2. **规划者边际收益** [SOLID]
   固定覆盖下，总剩余为
   \[
   TS(q)=\int_{\theta^*}^{\overline\theta}[\theta v(q)-c(q)]f(\theta)d\theta-K(q).
   \]
   对 \(q\) 求导得到
   \[
   TS_q=D\bar\theta(\theta^*)v'(q)-Dc'(q)-K'(q),
   \]
   其中 \(\bar\theta(\theta^*)=\mathbb E[\theta\mid\theta\ge\theta^*]\)。

3. **企业在固定 cutoff 下的价格关系** [PLAUSIBLE]
   若覆盖 cutoff 固定为 \(\theta^*\)，则价格满足 \(p=\theta^*v(q)\)，因为边际消费者无差异。企业固定覆盖下利润为
   \[
   \Pi(q)=[\theta^*v(q)-c(q)]D-K(q).
   \]
   这一步把“企业按边际消费者估值质量”形式化，但依赖固定覆盖解释。

4. **企业边际收益** [SOLID]
   对上述固定覆盖利润求导：
   \[
   \Pi_q=D\theta^*v'(q)-Dc'(q)-K'(q).
   \]

5. **比较边际收益** [SOLID]
   二者差异为
   \[
   TS_q-\Pi_q=D[\bar\theta(\theta^*)-\theta^*]v'(q).
   \]
   由 A6，\(v'(q)>0\)；由非退化类型分布，\(\bar\theta(\theta^*)>\theta^*\)。因此规划者质量边际收益更高。

6. **推出质量 wedge 的方向** [PLAUSIBLE]
   若企业和规划者面临相同边际成本且目标函数满足单峰/凹性，则企业固定覆盖质量选择低于规划者固定覆盖质量选择。该方向需要凹性或单交叉条件；否则只能说“在同一点上规划者边际收益更高”，不能直接推出全局质量排序。

**Additional lemmas needed:**
- **Lemma W1.1:** 对非退化截断分布，\(\mathbb E[\theta\mid\theta\ge\theta^*]>\theta^*\)。
- **Lemma W1.2:** 若企业和规划者目标在 \(q\) 上严格凹，则边际收益比较可推出 \(q^{SP}>q^F\)。

**Hardest step:** Step 6 — 从边际收益 wedge 推出质量水平排序需要额外凹性/单峰条件。

**Rigor summary:** SKETCH

**To complete this proof, one would need to:**
- 明确该命题是否只主张边际收益 wedge，还是主张质量水平排序。
- 若主张质量水平排序，加入目标函数凹性条件并证明。

---

## [P_W2] — Proof Sketch: Distributional Welfare Reversal

**Claim (restated):**
> 存在一组满足模型假设的质量升级 \((q_0,p_0)\to(q_1,p_1)\)，其中 \(q_1>q_0\) 且所有持续购买者的毛效用 \(\theta v(q)\) 上升，但低类型持续购买者净效用下降，并且 aggregate consumer surplus 下降。该结果发生当价格传导阈值 \(\theta^G=\Delta p/\Delta v\) 落在持续购买者集合内部，且价格传导超过购买者加权平均质量收益。

**Proof strategy:** 构造性存在证明。

**Key technique:** P_C1 的个体阈值 + P_M1 的 CS 分解 + 参数连续性。

**Proof sketch:**

1. **选择任意正质量升级** [SOLID]
   取 \(q_1>q_0\)。由 A6，\(\Delta v=v(q_1)-v(q_0)>0\)。因此所有持续购买者毛效用 \(\theta v(q)\) 上升。

2. **选择价格变化使 gain cutoff 位于持续购买者内部** [PLAUSIBLE]
   选择 \(\Delta p\) 使 \(\theta^G=\Delta p/\Delta v\) 位于 \(B_{01}\) 内部。这需要 \(p_1=p_0+\Delta p\) 不使购买集合变化到空集；在连续类型和有限上界下可通过选择中等 \(\Delta p\) 实现。

3. **低类型持续购买者受损，高类型持续购买者获益** [SOLID]
   由 P_C1，任何持续购买者的净效用变化为 \(\theta\Delta v-\Delta p\)。因此 \(\theta<\theta^G\) 的持续购买者受损，\(\theta>\theta^G\) 的持续购买者获益。

4. **构造 aggregate CS 下降** [PLAUSIBLE]
   由 P_M1，\(\Delta CS\) 等于持续购买者效用变化积分加进入/退出项。选择 \(\Delta p\) 足够大，使持续购买者价格损失和退出损失超过高类型质量收益；同时保持一部分高类型仍购买。

5. **证明存在非空参数区域** [GAP]
   需要给出显式构造，例如令 \(\theta\sim U[0,1]\)、\(v(q)=q\)、取 \((q_0,p_0)) 和 \((q_1,p_1))，直接计算 \(CS_1<CS_0\) 且存在持续购买者赢家/输家。当前草图尚未完成闭式例子。

6. **结论** [PLAUSIBLE]
   一旦 Step 5 的显式例子成立，即可证明存在满足条件的参数区域；由连续性，例子附近的小邻域也保持该性质。

**Additional lemmas needed:**
- **Lemma W2.1:** 存在显式数值例子满足：\(q_1>q_0\)、部分持续购买者受损、且 \(CS_1<CS_0\)。
- **Lemma W2.2:** 消费者剩余关于 \((q,p)\) 连续，从而例子对应开放参数区域。

**Hardest step:** Step 5 — 必须补充一个明确可计算的例子；否则该命题有“由高价格传导假设直接推出结论”的风险。

**Rigor summary:** SKETCH

**To complete this proof, one would need to:**
- 构造并验证一个均匀分布、线性 \(v\) 下的闭式例子。
- 明确 \(p_1\) 是否必须是企业重新优化价格；若必须，构造难度更高。

---

## [P_M1] — Proof Sketch: Quality-Utility Decomposition

**Claim (restated):**
> 任何质量升级对消费者剩余的影响都可以分解为三个部分：持续购买者的直接质量收益、持续购买者的价格损失、以及购买集合变化导致的进入/退出项。

**Proof strategy:** 集合分解。

**Key technique:** 将 \(B_0\cup B_1\) 分成持续购买者、进入者和退出者。

**Proof sketch:**

1. **定义购买集合** [SOLID]
   对 \(i=0,1\)，令 \(B_i=\{\theta:\theta v(q_i)-p_i\ge0\}\)。消费者剩余为 \(CS_i=\int_{B_i}[\theta v(q_i)-p_i]f(\theta)d\theta\)。

2. **分解集合** [SOLID]
   将类型空间分为 \(B_{01}=B_0\cap B_1\)、进入者 \(E=B_1\setminus B_0\)、退出者 \(X=B_0\setminus B_1\) 和持续非购买者。

3. **持续非购买者贡献为零** [SOLID]
   持续非购买者在两个制度下都不进入消费者剩余积分，贡献差额为 0。

4. **对三类集合分别相减** [SOLID]
   对 \(B_{01}\)，贡献为效用差 \(\theta[v(q_1)-v(q_0)]-(p_1-p_0)\)；对 \(E\)，贡献为新制度净效用；对 \(X\)，贡献为旧制度净效用的负值。

5. **合并得到公式** [SOLID]
   把三项相加即得到 Stage 6 中的分解公式。

**Additional lemmas needed:**
- 无。

**Hardest step:** 无；该命题是会计恒等式。

**Rigor summary:** NEAR-COMPLETE

**To complete this proof, one would need to:**
- 在最终论文中说明该命题是分解框架，不是独立福利定理。

---

## [P_B1] — Proof Sketch: Boundary Cases

**Claim (restated):**
> 当消费者类型退化为单一类型时，质量升级不会产生类型间分配冲突；当价格传导相对于质量收益趋近于最高类型估值时，几乎所有低/中类型消费者受损或退出。

**Proof strategy:** 使用 P_C1 的阈值并取极限。

**Key technique:** 退化分布和连续分布的尾部测度极限。

**Proof sketch:**

1. **单类型情形** [SOLID]
   若 \(\Theta=\{\theta_0\}\)，所有持续购买者具有同一 \(\Delta u=\theta_0\Delta v-\Delta p\)。因此不存在类型间赢家/输家分化。

2. **高传导阈值定义** [SOLID]
   由 P_C1，持续购买者获益当且仅当 \(\theta>\theta^G=\Delta p/\Delta v\)。

3. **阈值趋近上界** [SOLID]
   若 \(\theta^G\uparrow\overline\theta\)，获益者集合包含在 \((\theta^G,\overline\theta]\) 中。

4. **连续分布下尾部测度趋零** [SOLID]
   由 A4 连续分布且 \(\overline\theta\) 无原子，\(1-F(\theta^G)\to0\)。因此获益持续购买者测度趋零。

**Additional lemmas needed:**
- 无。

**Hardest step:** 无实质困难；需修正正式表述中“受损或退出”的精确定义。

**Rigor summary:** NEAR-COMPLETE

**To complete this proof, one would need to:**
- 区分“持续购买但受损”与“退出”两类，避免一句话覆盖两种不同现象。

---

## Overall Proof Landscape

| Proposition | Rigor Level | Hardest Step | Lemmas Needed |
|------------|------------|-------------|--------------|
| P_E1 | MOSTLY SOLID | 需求/利润在 \(q=0\) 和边界处的连续性 | 2 |
| P_U1 | NEAR-COMPLETE | 验证原始条件下的严格准凹 | 0–1 |
| P_C1 | NEAR-COMPLETE | 无 | 0 |
| P_C2 | MOSTLY SOLID | \(p(q)\) 的可微来源 | 2 |
| P_W1 | SKETCH | 从边际 wedge 推出质量水平排序 | 2 |
| P_W2 | SKETCH | 构造显式参数例子 | 2 |
| P_M1 | NEAR-COMPLETE | 无 | 0 |
| P_B1 | NEAR-COMPLETE | 表述精确化 | 0 |

**Most vulnerable proposition:** P_W2 — 需要显式构造或参数区域，否则容易被批评为“高价格传导导致福利下降”的同义反复。

**Most complete proof:** P_C1 和 P_M1 — 但它们是支撑性而非核心贡献。

**Priority for formalization:**
1. **P_C2** — 最强核心命题，证明路线清晰，应首先形式化。
2. **P_W2** — 最脆弱核心命题，需要显式例子或改写为条件命题。
3. **P_W1** — 需决定命题只主张边际 wedge，还是主张质量水平排序。
