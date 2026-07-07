# Candidate Propositions

**Date:** 2026-06-18
**Stage:** 6 — Proposition Generator

---

## Proposition Summary Table

| ID | Type | One-line statement | Role | Difficulty | Novelty |
|----|------|--------------------|------|-----------|---------|
| P_E1 | Existence | 在紧致质量/价格空间和连续收益下，存在一个 SPE，其中企业选择利润最大化质量—价格对，消费者按 cutoff 购买。 | SUPPORTING | EASY | LOW |
| P_U1 | Uniqueness | 若企业利润在 \((q,p)\) 上严格准凹，则 SPE 的质量—价格对唯一。 | SUPPORTING | EASY | LOW |
| P_C1 | Comparative Statics | 对持续购买者，质量升级的个体净效用变化存在类型阈值 \(\theta^G=\Delta p/\Delta v\)。 | SUPPORTING | EASY | LOW |
| P_C2 | Comparative Statics | 边际质量升级提高消费者剩余当且仅当购买者平均质量估值乘以边际质量收益超过价格传导。 | CORE | MEDIUM | MEDIUM |
| P_W1 | Welfare | 在给定覆盖集合下，利润最大化企业相对于总剩余规划者系统性低估高于边际消费者的质量收益。 | CORE | MEDIUM | MEDIUM |
| P_W2 | Welfare / Distribution | 存在参数区域中，客观质量上升且所有消费者毛效用上升，但低类型持续购买者受损且总消费者剩余下降。 | CORE | MEDIUM | MEDIUM |
| P_M1 | Mechanism / Decomposition | 质量升级的消费者剩余变化可分解为直接质量收益、价格传导和参与集合变化三项。 | SUPPORTING | EASY | MEDIUM |
| P_B1 | Boundary | 当类型异质性消失时，质量升级的分配冲突消失；当价格传导足够高时，几乎所有低/中类型消费者受损或退出。 | SUPPORTING | EASY | LOW |

---

## Dependency Graph

```text
P_E1 (Existence)
├── P_U1 (Uniqueness, depends on P_E1 plus strict quasi-concavity)
├── P_C1 (Individual gain cutoff, depends on primitives only)
│   └── P_W2 (Distributional welfare reversal, depends on P_C1 and P_M1)
├── P_M1 (Quality-utility decomposition, depends on CS definition)
│   └── P_C2 (Marginal CS threshold, depends on P_M1 and differentiability)
└── P_W1 (Firm-vs-planner quality wedge, depends on P_E1 and interior FOCs)

P_B1 (Boundary result, depends on P_C1/P_W2)
```

---

## Detailed Proposition Statements

---

### [P_E1] — Existence of SPE

**Statement:**
> Under assumptions A1–A13, plus continuity of \(v,c,K,F\) and compactness of \(Q\times P\), there exists a subgame perfect equilibrium in which the firm chooses \((q^M,p^M)\in\arg\max_{(q,p)\in Q\times P}\Pi(q,p)\), and consumers purchase if and only if \(\theta v(q^M)-p^M\ge0\).

**Formal statement (LaTeX-ready):**
```latex
\begin{proposition}[Equilibrium Existence]
Suppose Assumptions A1--A13 hold. Suppose further that
$Q=[0,\bar q]$, $P=[0,\bar p]$, $v$, $c$, and $K$ are continuous,
and $F$ is continuous on $\Theta$. Then there exists a subgame perfect
equilibrium $(q^M,p^M,a^*)$ such that
\[
(q^M,p^M)\in \arg\max_{(q,p)\in Q\times P}\Pi(q,p),
\]
and
\[
a^*_\theta(q,p)=1\quad\text{if and only if}\quad \theta v(q)-p\ge 0.
\]
\end{proposition}
```

**Required assumptions:** A1, A2, A3, A4, A5, A8, A9, A10, A11, A12; hidden assumptions H1–H3.

**Expected proof technique:** Backward induction plus Weierstrass theorem. Solve consumer subgame by pointwise utility comparison; then show firm payoff is continuous on compact \(Q\times P\).

**Proof difficulty:** EASY

**Novelty:** LOW

**Role:** SUPPORTING

**Economic content:** 该命题保证后续比较静态不是建立在空集合上；它本身不是论文贡献。

---

### [P_U1] — Conditional Uniqueness of the Equilibrium Quality-Price Pair

**Statement:**
> If, in addition to P_E1 assumptions, the induced profit function \(\Pi(q,p)\) is strictly quasi-concave on \(Q\times P\), then the equilibrium quality—price pair \((q^M,p^M)\) is unique. Consumer strategies are unique except possibly for a measure-zero indifferent type.

**Formal statement:**
```latex
\begin{proposition}[Conditional Uniqueness]
Suppose the assumptions of Proposition P\_E1 hold and the induced profit
function $\Pi(q,p)$ is strictly quasi-concave on $Q\times P$. Then the
set $\arg\max_{(q,p)\in Q\times P}\Pi(q,p)$ is a singleton. Hence the
SPE quality-price pair $(q^M,p^M)$ is unique. Consumer purchase decisions
are unique for all types except possibly the cutoff type
$\theta^M=p^M/v(q^M)$, which has measure zero under a continuous type distribution.
\end{proposition}
```

**Required assumptions:** P_E1 assumptions plus strict quasi-concavity of \(\Pi\).

**Expected proof technique:** Strict quasi-concavity implies unique maximizer; cutoff indifference is measure-zero under continuous \(F\).

**Proof difficulty:** EASY

**Novelty:** LOW

**Role:** SUPPORTING

**Economic content:** 唯一性让后续比较静态更清晰，但该命题主要是技术支撑。

---

### [P_C1] — Individual Gain Threshold for Continuing Buyers

**Statement:**
> Consider a quality upgrade from \((q_0,p_0)\) to \((q_1,p_1)\), with \(q_1>q_0\) and \(\Delta v=v(q_1)-v(q_0)>0\). For any consumer type that buys in both regimes, net utility increases if and only if \(\theta>\theta^G\equiv\Delta p/\Delta v\), decreases if and only if \(\theta<\theta^G\), and is unchanged if \(\theta=\theta^G\).

**Formal statement:**
```latex
\begin{proposition}[Individual Gain Threshold]
Let $(q_0,p_0)$ and $(q_1,p_1)$ be two quality-price regimes with
$q_1>q_0$ and $\Delta v\equiv v(q_1)-v(q_0)>0$. Let
$\Delta p\equiv p_1-p_0$. For any type $\theta$ that purchases under both
regimes,
\[
\Delta u_\theta = \theta\Delta v-\Delta p.
\]
Therefore $\Delta u_\theta>0$ if and only if
$\theta>\theta^G\equiv \Delta p/\Delta v$.
\end{proposition}
```

**Required assumptions:** A2, A3, A5, A6, A8, A10, A11.

**Expected proof technique:** Direct subtraction of utility across regimes.

**Proof difficulty:** EASY

**Novelty:** LOW

**Role:** SUPPORTING

**Economic content:** 该命题定义了质量升级的个体赢家/输家 cutoff，但过于直接，不能作为核心贡献。

---

### [P_C2] — Marginal Consumer-Surplus Threshold for Quality Upgrading

**Statement:**
> Let \(p(q)\) be a differentiable equilibrium or pass-through price schedule. In an interior market-coverage region where \(\theta^*(q)=p(q)/v(q)\in(\underline\theta,\overline\theta)\), a marginal quality increase raises aggregate consumer surplus if and only if the average quality valuation among current buyers times marginal quality utility exceeds price pass-through:
> \[
> \mathbb E[\theta\mid \theta\ge\theta^*(q)]v'(q)>p'(q).
> \]

**Formal statement:**
```latex
\begin{proposition}[Consumer-Surplus Threshold for Quality Upgrading]
Suppose Assumptions A2--A6, A8, A10, A11, and A13 hold. Let $p(q)$ be
differentiable and suppose the induced participation cutoff
$\theta^*(q)=p(q)/v(q)$ lies in $(\underline\theta,\overline\theta)$.
Then
\[
\frac{dCS(q,p(q))}{dq}
= D(q,p(q))\left(\mathbb E[\theta\mid \theta\ge\theta^*(q)]v'(q)-p'(q)\right).
\]
Hence a marginal quality upgrade increases consumer surplus if and only if
\[
\mathbb E[\theta\mid \theta\ge\theta^*(q)]v'(q)>p'(q).
\]
\end{proposition}
```

**Required assumptions:** A2, A3, A4, A5, A6, A8, A10, A11, A13; hidden assumptions H1, H3, H5; differentiability of \(p(q)\).

**Expected proof technique:** Leibniz rule/envelope argument. The boundary term vanishes because the cutoff type receives zero net utility.

**Proof difficulty:** MEDIUM

**Novelty:** MEDIUM

**Role:** CORE

**Economic content:** 该命题给出“质量升级是否改善消费者效用联通”的核心阈值：不是看质量本身是否提高，而是看购买者平均质量估值的边际收益是否超过价格传导。

---

### [P_W1] — Firm-vs-Planner Quality Wedge under Fixed Coverage

**Statement:**
> 在同一购买覆盖集合下，利润最大化企业按边际购买者的质量估值选择质量，而总剩余规划者按所有被服务消费者的平均质量估值选择质量。只要购买者类型存在非退化异质性，平均被服务类型严格高于边际类型；因此企业相对于覆盖集合固定的总剩余规划者系统性低估质量的社会边际收益。

**Formal statement:**
```latex
\begin{proposition}[Firm-vs-Planner Quality Wedge]
Fix an interior cutoff $\theta^*\in(\underline\theta,\overline\theta)$ and suppose
Assumptions A1--A7, A10--A13 hold. Let
\[
\bar\theta(\theta^*)\equiv \mathbb E[\theta\mid \theta\ge\theta^*].
\]
A firm that internalizes the marginal buyer's willingness to pay chooses quality
according to the marginal condition
\[
\theta^* v'(q)=c'(q)+K'(q)/D,
\]
whereas a coverage-constrained total-surplus planner chooses quality according to
\[
\bar\theta(\theta^*)v'(q)=c'(q)+K'(q)/D.
\]
If the type distribution is non-degenerate above $\theta^*$, then
$\bar\theta(\theta^*)>\theta^*$, so the planner's marginal benefit of quality
exceeds the firm's at the same coverage level.
\end{proposition}
```

**Required assumptions:** A1, A2, A3, A4, A5, A6, A7, A10, A11, A12, A13; interiority; non-degenerate type distribution above cutoff.

**Expected proof technique:** Compare first-order conditions for firm and coverage-constrained planner; use \(\mathbb E[\theta\mid\theta\ge\theta^*]>\theta^*\).

**Proof difficulty:** MEDIUM

**Novelty:** MEDIUM

**Role:** CORE

**Economic content:** 企业用边际消费者定价和选择质量，但质量改善同时惠及所有已购买消费者；因此企业可能低估质量升级对 inframarginal consumers 的总福利收益。这不是简单的“价格涨跌”命题，而是一个 firm-vs-planner wedge。

---

### [P_W2] — Distributional Welfare Reversal from Quality Upgrading

**Statement:**
> 存在一组满足模型假设的质量升级 \((q_0,p_0)\to(q_1,p_1)\)，其中 \(q_1>q_0\) 且所有持续购买者的毛效用 \(\theta v(q)\) 上升，但低类型持续购买者净效用下降，并且 aggregate consumer surplus 下降。该结果发生当价格传导阈值 \(\theta^G=\Delta p/\Delta v\) 落在持续购买者集合内部，且价格传导超过购买者加权平均质量收益。

**Formal statement:**
```latex
\begin{proposition}[Distributional Welfare Reversal]
Suppose Assumptions A2--A6, A8, A10, A11, and A13 hold. Consider two
quality-price regimes $(q_0,p_0)$ and $(q_1,p_1)$ with $q_1>q_0$,
$\Delta v=v(q_1)-v(q_0)>0$, and $\Delta p=p_1-p_0>0$. Let
$B_i=\{\theta:\theta v(q_i)-p_i\ge0\}$ and let $B_{01}=B_0\cap B_1$ denote
continuing buyers. If
\[
\inf B_{01}<\theta^G\equiv\Delta p/\Delta v<\sup B_{01},
\]
then some continuing buyers gain and some continuing buyers lose. Moreover,
if
\[
\int_{B_1}\bigl[\theta v(q_1)-p_1\bigr]f(\theta)d\theta
<
\int_{B_0}\bigl[\theta v(q_0)-p_0\bigr]f(\theta)d\theta,
\]
then aggregate consumer surplus falls despite the objective quality increase.
Such parameter values exist whenever price pass-through can be sufficiently large
while leaving a positive measure of buyers served.
\end{proposition}
```

**Required assumptions:** A2, A3, A4, A5, A6, A8, A10, A11, A13; H1, H3, H5.

**Expected proof technique:** Constructive argument using P_C1 threshold plus continuity of CS in \((q,p)\); choose \(\Delta p\) large enough to reduce CS but not so large as to eliminate all buyers.

**Proof difficulty:** MEDIUM

**Novelty:** MEDIUM

**Role:** CORE

**Economic content:** 该命题形式化说明“质量更高”与“消费者更好”可以分离：技术质量进步可能同时带来高类型获益、低类型受损和 aggregate consumer surplus 下降。

---

### [P_M1] — Quality-Utility Decomposition

**Statement:**
> 任何质量升级对消费者剩余的影响都可以分解为三个部分：持续购买者的直接质量收益、持续购买者的价格损失、以及购买集合变化导致的进入/退出项。

**Formal statement:**
```latex
\begin{proposition}[Quality-Utility Decomposition]
Let $(q_0,p_0)$ and $(q_1,p_1)$ be two quality-price regimes. Define
$B_i=\{\theta:\theta v(q_i)-p_i\ge0\}$, $B_{01}=B_0\cap B_1$,
$E=B_1\setminus B_0$, and $X=B_0\setminus B_1$. Then
\[
\Delta CS
=\int_{B_{01}}\left[\theta(v(q_1)-v(q_0))-(p_1-p_0)\right]f(\theta)d\theta
+\int_E [\theta v(q_1)-p_1]f(\theta)d\theta
-\int_X [\theta v(q_0)-p_0]f(\theta)d\theta.
\]
\end{proposition}
```

**Required assumptions:** A2, A3, A4, A5, A8, A10, A11, A13.

**Expected proof technique:** Set decomposition of the purchase sets \(B_0\) and \(B_1\).

**Proof difficulty:** EASY

**Novelty:** MEDIUM as an organizing framework, LOW as a mathematical identity.

**Role:** SUPPORTING

**Economic content:** 该命题为全文提供“质量—效用联通”的会计框架，但它本身更像分解工具，不应被包装成最主要的新定理。

---

### [P_B1] — Boundary Cases: No Heterogeneity and Extreme Pass-Through

**Statement:**
> 当消费者类型退化为单一类型时，质量升级不会产生类型间分配冲突；当价格传导相对于质量收益趋近于最高类型估值时，几乎所有低/中类型消费者受损或退出。

**Formal statement:**
```latex
\begin{proposition}[Boundary Cases]
Consider a quality upgrade with $\Delta v>0$ and $\Delta p>0$.
(i) If $\Theta$ collapses to a singleton $\{\theta_0\}$, then all continuing
buyers have the same sign of utility change, given by
$\theta_0\Delta v-\Delta p$.
(ii) If $\theta^G=\Delta p/\Delta v\uparrow\overline\theta$, then the set of
continuing buyers who gain has measure converging to zero under any continuous
type distribution with no atom at $\overline\theta$.
\end{proposition}
```

**Required assumptions:** A2, A3, A4, A5, A6, A8, A10, A11.

**Expected proof technique:** Direct application of P_C1 threshold and continuity of \(F\).

**Proof difficulty:** EASY

**Novelty:** LOW

**Role:** SUPPORTING

**Economic content:** 该命题说明消费者异质性是分配冲突的必要来源，而高价格传导会把质量升级变成主要有利于最高估值消费者的变化。

---

## What the Model CANNOT Establish

The following claims are OUT OF SCOPE for this model and should not be made:

- 不能声称质量升级在真实市场中通常提高或降低消费者福利；当前模型是风格化理论结构，不是经验结论。
- 不能声称多维质量、水平差异化或消费者错配已被处理；基线只有一维垂直质量。
- 不能声称竞争市场或寡头市场中的质量升级具有同样结论；当前基线是单企业市场势力。
- 不能声称质量不可观察时结果仍成立；若质量不可观察，需要 signaling/adverse selection 扩展。
- 不能声称低收入消费者的预算约束已被建模；当前类型 \(\theta\) 表示质量估值而非收入。
- 不能把 P_C1 或 P_M1 单独当成主要创新；它们是支撑性分解工具。

---

## Contribution Assessment

**Core propositions count:** 3

**Overall strength of contribution:** MODERATE

该命题组可以构成一个清晰的理论框架：P_C2 给出消费者剩余改善的边际阈值，P_W1 给出企业与规划者之间的质量选择 wedge，P_W2 给出质量升级导致分配性福利反转的存在结果。贡献强度取决于 Stage 7 能否把 P_W1 和 P_W2 证明为非定义性结论，而不只是把假设重写为结论。

**What would strengthen the contribution:**
- 将 P_W1 从固定覆盖集合推广到企业最优覆盖与规划者最优覆盖的完整比较。
- 在特定分布（如均匀分布）和函数形式下给出闭式阈值，使 P_C2/P_W2 更具可读性。
- 在扩展中加入质量菜单，比较单一升级与版本化升级对消费者剩余分布的影响。
