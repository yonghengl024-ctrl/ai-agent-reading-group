# Manuscript Skeleton

**Date:** 2026-06-18
**Stage:** 10 — Manuscript Skeleton

---

## Title Candidates

1. **Quality Upgrading and Consumer Utility** — Directly states the subject and keeps the title broad enough for a theoretical framework.
2. **When Better Quality Lowers Consumer Surplus** — Emphasizes the counterintuitive welfare reversal, but may overstate the generality.
3. **Quality, Prices, and Consumer Participation** — Highlights the three channels without overclaiming.
4. **Product Quality Upgrading and Welfare Incidence** — More technical; emphasizes distributional effects.
5. **Quality Upgrades under Market Power** — Centers the monopoly mechanism and firm incentives.

**Recommended title:** Quality Upgrading and Consumer Utility — concise, accurate, and suitable for the final PDF title format.

---

## Abstract Draft

This paper studies when product quality upgrading improves consumer utility and when it merely reallocates surplus across consumers. I develop a stylized monopoly model in which a firm chooses product quality and price, while consumers differ in their valuation of quality and decide whether to purchase. The model decomposes the consumer-surplus effect of a quality upgrade into direct quality gains, price pass-through, and participation effects. I show that, in an interior coverage region, a marginal upgrade raises consumer surplus if and only if the average quality valuation among current buyers exceeds the price pass-through scaled by marginal quality utility. The model also identifies a marginal wedge between private and planner valuations of quality. The central message is that quality upgrading is a distributional event, not merely a technical improvement.

---

## 1. Introduction

### Paragraph 1 — Opening Hook
**Topic sentence:** Product quality upgrading is often treated as an unambiguous improvement for consumers, but higher quality and higher consumer welfare are not the same object.

**Content:** Introduce the stylized puzzle: better product attributes can arrive with higher prices and changed participation. Avoid named industry claims unless verified.

**Goal:** Establish why quality upgrading creates an economic question rather than an engineering statement.

### Paragraph 2 — The Research Question
**Topic sentence:** This paper asks when a quality upgrade raises consumer utility and when it lowers consumer surplus for some consumers through price and participation effects.

**Content:** State the core question in the model: a firm chooses quality and price; consumers differ in quality valuations; welfare depends on gross utility, price, and participation.

**Goal:** Make the precise theoretical question clear.

### Paragraph 3 — Why It's Hard / Prior Approaches
**Topic sentence:** The difficulty is that quality affects consumers through several channels at once.

**Content:** Explain direct quality benefit, price pass-through, inframarginal buyers, marginal buyers, entrants, and exiters. Note that broad novelty claims are risky; the contribution is the decomposition and threshold.

**Goal:** Establish non-triviality.

### Paragraph 4 — Our Model
**Topic sentence:** I study a stylized monopoly quality-pricing model with heterogeneous consumers and endogenous market participation.

**Content:** One firm chooses \((q,p)\); consumer type \(\theta\) obtains \(\theta v(q)-p\); buys iff nonnegative; firm maximizes profit; planner benchmark defined separately.

**Goal:** Give high-level model before formal section.

### Paragraph 5 — Main Results
**Topic sentence:** The main results are threefold.

**Content:**
- Result 1: The quality effect on continuing buyers has a type threshold.
- Result 2: In an interior coverage region, consumer surplus rises iff average buyer valuation times marginal quality utility exceeds price pass-through.
- Result 3: For fixed coverage, the firm values marginal quality through the marginal buyer, while the planner values it through the average served buyer.
- Result 4: Under explicit pass-through conditions, objective quality can rise while low-valuation consumers lose and aggregate consumer surplus falls.

**Goal:** State what is established and what is conditional.

### Paragraph 6 — Economic Insight
**Topic sentence:** The central insight is that quality upgrading is a distributional event.

**Content:** Explain that high-valuation consumers may gain, low-valuation continuing buyers may lose, and marginal consumers may exit.

**Goal:** Tell the memorable story.

### Paragraph 7 — Related Literature
**Topic sentence:** The paper is closest to the monopoly product-quality tradition and uses that structure to study a quality-upgrade welfare decomposition.

**Content:** Cite only verified Mussa and Rosen (1978) as the canonical ancestor. Describe other streams without unverified citations: vertical differentiation, price discrimination, consumer surplus, and product-quality regulation.

**Key papers to cite:** Mussa and Rosen (1978), verified in `outputs/references_verified.md`.

**Goal:** Position honestly without unverified citations.

### Paragraph 8 — Organization
**Content:** The rest of the paper is organized as follows. Section 2 presents the model. Section 3 contains the main results. Section 4 discusses robustness, boundary cases, and extensions. Section 5 concludes. Proofs are collected in the Appendix.

---

## 2. Model

### 2.1 Environment
**Key content to include:**
- One firm with market power.
- Continuum of consumers indexed by \(\theta\in[\underline\theta,\overline\theta]\).
- Firm chooses quality \(q\) and price \(p\).
- Consumers observe \((q,p)\) and decide whether to buy.

### 2.2 Preferences and Payoffs
**Key content to include:**
- Consumer utility: \(u(\theta,q,p)=\theta v(q)-p\).
- Outside option normalized to 0.
- Firm profit: \(\Pi(q,p)=[p-c(q)]D(q,p)-K(q)\).
- Demand cutoff: \(\theta^*(q,p)=p/v(q)\) in interior regions.

### 2.3 Strategies and Information
**Key content to include:**
- Quality and price are public.
- Consumer type is privately known to consumer; firm knows distribution.
- Consumer strategy is purchase iff utility is nonnegative.

### 2.4 Assumptions
Use numbered assumptions:
- A1: single firm with market power.
- A2: one-dimensional vertical quality.
- A3: one-dimensional consumer quality valuation.
- A4: continuous type distribution with positive density.
- A5: quasi-linear utility.
- A6: increasing concave quality value.
- A7: increasing quality costs.
- A8: quality and price observable.
- A9: firm commits to quality and price.
- A10: unit demand.
- A11: outside option normalized to zero.
- A12: compact feasible quality/price domain or endogenous finite bounds.
- A13: no explicit budget constraint.

**Binding assumptions requiring defense:** A1, A2, A3, A5, A6, A7, A8, A9, A12, A13.

### 2.5 Equilibrium Concept
State SPE: firm chooses \((q,p)\), consumers observe and best respond. Equivalent to firm maximizing profit over induced demand.

### 2.6 Benchmarks
- First-best total surplus benchmark.
- Consumer-surplus benchmark under a price schedule.

---

## 3. Main Results

### 3.1 Existence and Basic Characterization

**Opening:** The model first establishes a well-defined equilibrium object.

**Proposition P_E1:** Existence of SPE.
- Proof: Appendix A.
- Interpretation: existence supports later welfare analysis but is not the contribution.

**Proposition P_U1:** Conditional uniqueness under strict quasi-concavity.
- Proof: Appendix A.
- Remark: strict quasi-concavity is sufficient, not automatic.

### 3.2 Individual and Aggregate Effects of Quality Upgrading

**Proposition P_C1:** Individual gain threshold.
- Interpretation: high types gain if quality benefits exceed common price increase; low types may lose.

**Proposition P_M1:** Quality-utility decomposition.
- Interpretation: aggregate CS change equals continuing-buyer net change plus entrant surplus minus exiter surplus.

**Proposition P_C2:** Interior consumer-surplus threshold.
- Core result.
- Include explicit interior cutoff condition.
- Add boundary remark for full/zero coverage.

### 3.3 Welfare Wedges and Distribution

**Proposition P_W1:** Firm-vs-planner marginal wedge.
- State as marginal wedge under fixed coverage.
- Global ordering only as optional corollary under strict concavity.

**Proposition P_W2:** Distributional welfare reversal under pass-through.
- State as pass-through comparison.
- Avoid claiming universal equilibrium reoptimization result.

**Proposition P_B1:** Boundary cases.
- Split homogeneous-consumer case from high-pass-through case.

---

## 4. Discussion

### 4.1 Robustness
Discuss:
- Interior versus boundary coverage.
- Compactness and endogenous price bounds.
- Tie-breaking at \((q,p)=(0,0)\).
- No top atom condition for boundary results.

### 4.2 Extensions
Potential extensions:
- Full screening / nonlinear pricing menu.
- Oligopoly and product differentiation.
- Unobservable quality, certification, or signaling.
- Income constraints and multidimensional types.

### 4.3 Policy Implications
Careful language only:
- Quality standards may have distributional consequences.
- Access policies may be needed if upgrading raises prices and excludes low-valuation consumers.
- The model does not prove a general policy rule.

---

## 5. Conclusion

### Opening
Quality upgrading raises gross utility but can lower net utility for some consumers when price pass-through is large. In interior regions, consumer surplus rises only when average buyer quality valuation dominates pass-through. Private and social valuations of marginal quality can diverge because firms focus on marginal buyers while planners count all served buyers.

### Central Message
Quality upgrading is not merely a technical improvement; it changes prices, participation, and distribution. The welfare effect depends on who values quality, who pays for it, and who remains in the market.

### Open Questions
1. How do these results change under oligopolistic quality competition?
2. Can equilibrium reoptimization generate the welfare reversal without imposing pass-through directly?
3. How does quality uncertainty change the link between objective quality and consumer utility?

### Closing
A theory of quality upgrading must track not only how products improve, but how markets translate those improvements into prices and participation.

---

## Appendix A: Proofs

### Proof of Proposition P_E1
**Structure:** consumer best responses; demand cutoff; firm optimization; SPE construction.

**Lemmas required:**
- Lemma A.1: demand/profit continuity or upper semicontinuity.
- Lemma A.2: finite endogenous price bound.

**Rigor level:** MOSTLY SOLID.

### Proof of Proposition P_U1
**Structure:** strict quasi-concavity implies unique maximizer; cutoff indifference measure zero.

**Rigor level:** NEAR-COMPLETE.

### Proof of Proposition P_C1
**Structure:** direct utility subtraction.

**Rigor level:** NEAR-COMPLETE.

### Proof of Proposition P_C2
**Structure:** write CS integral; apply Leibniz rule; boundary term vanishes; sign condition.

**Lemmas required:** differentiability and interior coverage.

**Rigor level:** MOSTLY SOLID.

### Proof of Proposition P_W1
**Structure:** compare firm and planner marginal quality benefits under fixed coverage.

**Lemmas required:** truncated conditional mean exceeds cutoff; optional concavity for global ordering.

**Rigor level:** SKETCH.

### Proof of Proposition P_W2
**Structure:** construct or state pass-through condition; apply threshold and CS decomposition.

**Lemmas required:** explicit example or sufficient inequality.

**Rigor level:** SKETCH.

### Proof of Proposition P_M1
**Structure:** set decomposition.

**Rigor level:** NEAR-COMPLETE.

### Proof of Proposition P_B1
**Structure:** apply gain threshold and limiting measure argument.

**Rigor level:** NEAR-COMPLETE.

---

## Notation Table

| Symbol | Meaning | First defined |
|--------|---------|-------------|
| \(q\) | product quality | Section 2 |
| \(p\) | price | Section 2 |
| \(\theta\) | consumer quality valuation | Section 2 |
| \(F,f\) | type distribution and density | Section 2 |
| \(v(q)\) | quality value function | Section 2 |
| \(c(q)\) | unit cost | Section 2 |
| \(K(q)\) | fixed quality cost | Section 2 |
| \(D(q,p)\) | demand | Section 2 |
| \(CS\) | consumer surplus | Section 3 |
| \(TS\) | total surplus | Section 3 |

---

## Pre-Submission Checklist

### Content
- [ ] Every proposition has a proof or proof sketch.
- [ ] Every proposition has an economic interpretation paragraph.
- [ ] Every assumption has a one-sentence economic justification.
- [ ] Abstract claims are supported by body results.
- [ ] Related work includes only verified citations.
- [ ] Limitations and counterexamples are stated explicitly.

### Style
- [ ] Every claim is epistemically labeled.
- [ ] No vague “mild regularity conditions.”
- [ ] Equilibrium concept is specified when discussing equilibrium.
- [ ] Welfare claims specify benchmark.
- [ ] All notation is defined at first use.

### To Complete Before Submission
- [ ] Formalize P_W1 and P_W2 or weaken them further.
- [ ] Add explicit example for P_W2.
- [ ] Verify any additional references before adding them.
