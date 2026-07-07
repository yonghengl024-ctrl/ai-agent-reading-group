# Canonical Model Match

**Date:** 2026-06-18
**Stage:** 3b — Canonical Model Matching

---

## 1. Research Puzzle Summary

本项目研究一个风格化市场：企业选择产品质量与价格，消费者在质量偏好上异质，并根据净效用决定是否购买。核心问题是：产品质量升级何时提高消费者效用与消费者剩余，何时又会通过价格上升、市场参与变化与低类型消费者退出而使部分消费者受损。

**中心机制：** 企业质量升级选择与质量成本 → 质量—价格组合变化 → 消费者按类型重新排序并决定参与 → 个体效用、消费者剩余与总福利发生变化。

**主体与摩擦：** 一个具有市场势力的企业面对连续消费者类型。摩擦不是信息不对称本身，而是企业利用质量—价格组合筛选异质消费者，并在利润最大化与消费者福利之间产生扭曲。

**目标结果：** 均衡刻画、比较静态、消费者剩余分解、分配效应、企业选择与社会规划者选择之间的福利比较。

---

## 2. Candidate Families

### Candidate 1: Price Discrimination — Second-Degree / Versioning / Quality Ladders

- **Fit rationale:** `model_library/io/price-discrimination.md` 的 “When to Use This Model” 明确说明，该模型适用于“具有市场势力的企业面对异质支付意愿消费者”、研究“versioning, bundling, quality ladders, or menu design as discrimination instruments”的问题。该文件的 “Main Mechanism” 也说明二级价格歧视通过质量版本与自选择影响福利。
- **Key structural match:**
  - 企业具有市场势力；
  - 消费者在质量估值上异质；
  - 质量可以作为筛选工具；
  - 福利含义包括低类型扭曲、消费者剩余提取和可能的排除。
- **Potential gap:** 标准二级价格歧视通常强调菜单与自选择约束；本项目的基线可以更简单：先研究单一质量—价格对的升级，再把菜单/versioning 作为扩展。
- **Closest canonical ancestor:** Mussa and Rosen (1978), “Monopoly and product quality,” *Journal of Economic Theory* 18(2): 301–317, DOI: 10.1016/0022-0531(78)90085-6. 当前会话中通过 Crossref API 元数据验证了题名、作者、年份、期刊、卷期、页码与 DOI。

### Candidate 2: Screening / Mechanism Design under Adverse Selection

- **Fit rationale:** `model_library/screening.md` 的 “Canonical Economic Question” 是：当主体面对具有私人类型的代理人时，如何设计菜单使不同类型自我选择。其 “When to Use This Model” 包括非线性定价、价格歧视与 rent extraction vs. efficiency 的权衡。
- **Key structural match:**
  - 消费者类型 \(\theta\) 表示质量边际估值；
  - 企业可设计质量—支付组合；
  - 自选择、参与约束与信息租金决定质量扭曲；
  - “no distortion at the top / downward distortion below top” 可作为后续菜单扩展的理论谱系。
- **Potential gap:** 当前 Stage 1 与 Stage 3 的建议更偏向单一产品升级与统一价格，而不是完整菜单机制；若直接采用 screening，会增加 IC 约束并使模型比必要程度更复杂。
- **Closest canonical ancestor:** 与 Candidate 1 相同，二级价格歧视/质量版本化和 screening 在模型库中被明确连接；若采用完整菜单，则祖先是标准 hidden-type screening 模型。

### Candidate 3: Consumer Choice / Utility Maximization

- **Fit rationale:** `model_library/consumer-choice.md` 的 “When to Use This Model” 包括个体需求行为、价格变化的福利效应与家庭福利分析；“Agent Heterogeneity” 允许按偏好类型或收入异质性聚合需求。
- **Key structural match:**
  - 消费者在给定质量与价格下最大化效用；
  - 购买参与由净效用是否非负决定；
  - 消费者剩余与需求反应是核心对象。
- **Potential gap:** 纯消费者选择模型没有企业质量与价格选择，因此无法单独解释质量升级为什么发生，也无法生成企业—消费者福利冲突。
- **Closest canonical ancestor:** 标准效用最大化与消费者剩余分析；作为需求侧构件而非完整基线。

### Candidate 4: Hotelling / Product Differentiation

- **Fit rationale:** `model_library/hotelling-product-differentiation.md` 的 “Canonical Economic Question” 涉及企业如何选择产品特征与价格，以及消费者异质偏好如何决定市场分割；“When to Use This Model” 包括产品特征维度上的差异化与价格竞争。
- **Key structural match:**
  - 产品质量可被视为产品特征；
  - 消费者偏好异质；
  - 价格与特征共同决定购买选择。
- **Potential gap:** Hotelling 更适合水平差异化或多企业竞争；本项目当前强调一维垂直质量升级和单企业质量—价格选择。若直接采用 Hotelling，会把核心问题转向竞争定位，而不是质量升级—效用联通。
- **Closest canonical ancestor:** Hotelling/空间竞争模型族；本项目只把它作为 oligopoly/competition 扩展。

---

## 3. Recommended Baseline

**Recommended Baseline: Price Discrimination / Monopoly Product Quality Choice with Heterogeneous Consumers**

**Primary justification:**
最佳基线是一个具有市场势力的单企业质量—价格选择模型：企业先选择质量 \(q\) 和价格 \(p\)，消费者具有类型 \(\theta\)，并根据 \(\theta v(q)-p\ge 0\) 决定是否购买。这个基线继承了质量版本化和二级价格歧视文献中“质量作为筛选工具”的思想，但先不引入完整菜单；这样能直接对应 Stage 1 的问题：质量升级如何通过直接效用、价格和参与门槛影响消费者效用。该基线也与 Persona Council 的建议一致：先做一维质量、一维类型、参与 cutoff 和 firm-vs-planner 比较。

**Canonical baseline setup:**
- **Agents:** 一个风险中性的垄断企业；一单位质量需求的连续消费者群体。
- **Consumer type:** \(\theta\in[\underline\theta,\overline\theta]\)，表示质量边际估值或质量偏好强度。
- **Utility:** 若购买，消费者类型 \(\theta\) 的净效用为 \(u(\theta,q,p)=\theta v(q)-p\)；若不购买，效用为 0。
- **Firm objective:** 企业选择 \((q,p)\) 最大化利润 \(\Pi(q,p)=(p-c(q))D(q,p)-K(q)\)，其中 \(D(q,p)\) 由购买 cutoff 决定。
- **Equilibrium concept:** 单企业最优化 + 消费者最优购买反应；可称为垄断定价—质量选择均衡，或两阶段完全信息博弈的子博弈精炼均衡。
- **Welfare benchmark:** 社会规划者选择 \(q\) 与服务集合以最大化总剩余；并与企业私有最优进行比较。

**Inheritance list:**
- 从价格歧视/质量版本化模型继承：异质消费者、质量作为筛选维度、市场势力企业、消费者参与约束、质量—价格组合决定福利分配。
- 从消费者选择模型继承：给定 \((q,p)\) 下的消费者效用最大化、购买/不购买选择、消费者剩余计算。
- 从 screening 谱系继承但简化：类型 \(\theta\) 的单交叉结构，即高类型对质量的边际估值更高。

**What must be added or modified:**
1. **质量升级比较静态：** 明确比较 \((q,p(q))\) 到 \((q',p(q'))\) 时消费者效用的分解，而不仅是求解一次性最优质量。
2. **效用联通分解：** 将消费者净效用变化分解为质量效用增益、价格变化损失和参与状态变化三项，并明确赢家/输家类型区间。

---

## 4. Recommended Extensions

### Recommended Extension 1: Full Screening / Nonlinear Pricing Menu

- **Why natural:** 一旦单一质量—价格基线完成，企业可扩展为提供质量菜单 \((q(\theta),t(\theta))\)，对应二级价格歧视与版本化。
- **Additional mechanism:** IC 约束、信息租金、低类型质量扭曲和可能的排除。
- **When to pursue:** 在基线刻画完成后，用于分析多版本产品是否改善或恶化消费者剩余分布。

### Recommended Extension 2: Hotelling / Differentiated Oligopoly

- **Why natural:** 若研究者希望引入竞争，则质量升级可能既影响消费者效用，也影响竞争强度与企业定位。
- **Additional mechanism:** 质量差异化放松或加剧价格竞争，竞争对手反应改变升级的福利效应。
- **When to pursue:** 只有在单企业基线完成后作为扩展；否则会混淆质量升级机制与竞争定位机制。

---

## 5. Excluded Families

- **Indirect Utility / Expenditure Minimization:** 适合作为福利测度工具，但不是企业质量升级与定价的完整基线。
- **Adverse Selection:** 若产品质量对消费者不可观察，该模型才是核心；当前设定中质量是公开可观察的产品属性。
- **Signaling:** 不适合当前基线，因为没有知情方先行动以传递类型或质量信息。
- **Moral Hazard:** 不适用；核心不是不可观察努力。
- **Mechanism Design:** 过于一般；screening/二级价格歧视已覆盖本项目所需的机制设计结构。
- **Oligopoly Competition:** 可作为扩展，但当前 Stage 1 与 Stage 3 推荐从单企业质量—价格选择开始。
- **Two-Sided Markets / Platforms:** 当前没有双边外部性或平台两侧结构。
- **Rational Inattention / Search / Costly Information:** 当前没有消费者信息处理或搜索摩擦。
- **General Equilibrium / Trade / Labor / Human Capital Families:** 当前研究不涉及一般均衡、国际贸易、人力资本、教育、自动化或劳动市场，因此不适用。

---

## 6. Relabeling Check

**Is the proposed model a superficial relabeling of a classic model?**

**Answer: Not automatically, but relabeling risk is real.**

若模型只写成 \(u=\theta q-p\)，再证明“价格涨幅大于质量收益时消费者受损”，这会成为经典垂直质量/价格歧视模型的表面改名。因此 Stage 4 和 Stage 6 必须加入非平凡结构：质量升级作为企业选择或外生技术改进引起的 \((q,p,D)\) 联动，并证明消费者效用变化可被分解为质量收益、价格传导和参与状态变化，同时与企业私有最优和社会规划者最优进行比较。

**Genuinely new elements required for non-relabeling:**
1. 明确的 “quality-utility linkage decomposition”：\(\Delta u_\theta=\theta\Delta v-\Delta p\)，并把参与状态变化单独纳入 ex ante consumer surplus。
2. 明确刻画赢家/输家类型区间：高类型、低类型、边际退出者受到不同影响。
3. 企业私有质量选择与消费者剩余最大化质量之间的扭曲条件，而不是单纯的质量偏好异质性。

---

## 7. Primitives Inheritance Handoff

```text
CANONICAL MODEL MATCH HANDOFF TO STAGE 4
==========================================
Baseline model family:    Price Discrimination / Monopoly Product Quality Choice
Canonical ancestor:       Mussa and Rosen (1978), “Monopoly and product quality,” Journal of Economic Theory 18(2): 301–317, DOI 10.1016/0022-0531(78)90085-6; verified in current session via Crossref API metadata.

Inherit from the canonical model:
  - Agents:               one monopolist/firm with market power; continuum of consumers indexed by quality valuation θ.
  - Timing:               firm chooses quality q and price p; consumers observe (q,p), then buy or exit.
  - Information structure: quality and price are public; consumer type θ is privately known to the consumer, but in the single-price baseline the firm only needs the distribution F.
  - Equilibrium concept:  firm profit maximization with consumer best responses; equivalently SPE of a two-stage complete-information game with private consumer types aggregated through demand.
  - Key constraint type:  consumer participation / individual rationality u(θ,q,p) ≥ 0; feasibility q ≥ 0, p ≥ 0; firm cost and demand feasibility.

Modify from the canonical model:
  - Single product rather than full quality menu: begin with one quality-price pair to isolate upgrade effects.
  - Quality-upgrade comparative static: compare baseline and upgraded quality regimes, not only the static optimal product line.

New elements not in the canonical model:
  - Quality-utility decomposition: separate direct quality gain, price pass-through, and participation/exclusion effects.
  - Distributional welfare map: identify which consumer types gain, lose, enter, or exit after quality upgrading.
  - Firm-vs-planner distortion: compare profit-maximizing quality to consumer-surplus- or total-surplus-maximizing quality.

Confirmed NOT a superficial relabeling: yes, conditional on Stage 4 and Stage 6 retaining the decomposition, participation/exclusion, and firm-vs-planner distortion results. Without those elements, the setup risks collapsing into a standard vertical-quality monopoly model.
```
