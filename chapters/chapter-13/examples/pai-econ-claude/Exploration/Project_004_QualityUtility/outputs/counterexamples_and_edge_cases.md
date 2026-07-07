# Counterexamples and Edge Cases

**Date:** 2026-06-18
**Stage:** 8 — Counterexample Finder

---

## Summary Table

| Proposition | Attempts | Breaks Found | Severity | Status |
|------------|---------|-------------|---------|--------|
| P_E1 | 8 | 1 boundary vulnerability | LOW/MEDIUM | CONDITIONAL |
| P_U1 | 8 | 0 | — | ROBUST |
| P_C1 | 8 | 0 | — | ROBUST |
| P_C2 | 8 | 1 scope vulnerability | MEDIUM | CONDITIONAL |
| P_W1 | 8 | 1 genuine break if interpreted as global quality ordering | HIGH for strong version; MEDIUM after weakening | NEEDS FIX |
| P_W2 | 8 | 1 scope vulnerability if price must be equilibrium-reoptimized | MEDIUM | CONDITIONAL |
| P_M1 | 8 | 0 | — | ROBUST |
| P_B1 | 8 | 1 wording vulnerability | LOW | CONDITIONAL |

---

## [P_E1] — Counterexample Analysis

### Attempt 1: Two-Type Reduction
**Tried:** Two consumer types \(\theta_L<\theta_H\), one firm, compact \((q,p)\).

**Result:** SURVIVES — The consumer best-response rule remains cutoff-like: high type may buy while low type does not. Existence follows by finite action/reduced compact optimization if demand is defined consistently.

### Attempt 2: Extreme Parameter Values
**Tried:** \(q=0\), \(p=0\), and \(v(0)=0\).

**Result:** CONDITIONAL / EDGE CASE — At \((q,p)=(0,0)\), all consumers are indifferent because \(\theta v(0)-0=0\). Demand depends on tie-breaking. This does not destroy existence, but it makes the induced demand correspondence multi-valued unless tie-breaking or demand selection is specified.

### Attempt 3: Degenerate Distribution
**Tried:** All mass on a single type.

**Result:** SURVIVES — Existence still holds; cutoff analysis becomes trivial.

### Attempt 4: Corner Solutions
**Tried:** Optimal solution at \(q=0\), \(q=\overline q\), \(p=0\), or zero demand.

**Result:** SURVIVES WITH EDGE CASE — Existence survives, but later FOC-based propositions cannot use interior conditions at corners.

### Attempt 5: Relaxing Binding Assumption A12
**Tried:** Remove compact price/quality bounds.

**Result:** ⚠️ BREAKS — Assumption relaxation.

Counterexample: If \(Q\) or \(P\) is noncompact and no coercivity or finite-demand bound is imposed, the firm's profit maximization problem may fail to attain a maximum.

What fails: P_E1's existence proof via Weierstrass no longer works.

Severity: MEDIUM.

Fix options:
  Option A: Keep compact \(Q\) and prove an endogenous finite price bound.
  Option B: Replace compactness with coercivity / profit goes to negative infinity as quality cost grows.
  Option C: Restrict Stage 6 existence claim to compact feasible sets.

### Attempt 6: Alternative Equilibrium
**Tried:** Multiple firm maximizers.

**Result:** SURVIVES — P_E1 only claims existence, not uniqueness.

### Attempt 7: Strategic Manipulation
**Tried:** Consumers collude or manipulate information.

**Result:** SURVIVES — Consumers are atomistic and individual purchase decisions do not affect price or quality.

### Attempt 8: Existence Failure Check
**Tried:** Discontinuous demand at cutoff and \(q=0\).

**Result:** CONDITIONAL — Existence survives if payoff is upper semicontinuous or if tie-breaking/demand selection is fixed. Needs a technical lemma.

**P_E1 Overall verdict:** CONDITIONAL — robust under compactness and clear tie-breaking; vulnerable if compactness is removed.

---

## [P_U1] — Counterexample Analysis

### Attempt 1: Two-Type Reduction
**Tried:** Two types with strict quasi-concavity imposed on \(\Pi\).

**Result:** SURVIVES — Strict quasi-concavity rules out multiple maximizers.

### Attempt 2: Extreme Parameter Values
**Tried:** Boundary optimum.

**Result:** SURVIVES — Strict quasi-concavity can still yield a unique boundary optimum.

### Attempt 3: Degenerate Distribution
**Tried:** Single type.

**Result:** SURVIVES if strict quasi-concavity is maintained. If strict quasi-concavity fails, uniqueness may fail, but that is outside the proposition.

### Attempt 4: Corner Solutions
**Tried:** Full exclusion or full coverage.

**Result:** SURVIVES under strict quasi-concavity.

### Attempt 5: Relaxing strict quasi-concavity
**Tried:** Drop the strict quasi-concavity assumption.

**Result:** SURVIVES AS STATED — The proposition explicitly requires strict quasi-concavity. Dropping it creates multiplicity but does not refute the conditional claim.

### Attempt 6: Alternative Equilibrium
**Tried:** Multiple consumer tie-breaking rules at cutoff.

**Result:** SURVIVES — Consumer strategies may differ on a measure-zero type only; the proposition allows this.

### Attempt 7: Strategic Manipulation
**Tried:** Deviations after firm choice.

**Result:** SURVIVES — Consumers individually best respond.

### Attempt 8: Existence Failure Check
**Tried:** No maximizer.

**Result:** SURVIVES conditional on P_E1 assumptions. If P_E1 fails, P_U1 is not reached.

**P_U1 Overall verdict:** ROBUST.

---

## [P_C1] — Counterexample Analysis

### Attempt 1: Two-Type Reduction
**Tried:** Two continuing buyer types.

**Result:** SURVIVES — The threshold \(\theta^G=\Delta p/\Delta v\) correctly separates gainers and losers.

### Attempt 2: Extreme Parameter Values
**Tried:** \(\Delta p=0\), \(\Delta p<0\), and very high \(\Delta p\).

**Result:** SURVIVES — If \(\Delta p=0\), all continuing buyers gain; if \(\Delta p<0\), all continuing buyers gain more; if \(\Delta p\) is high, only sufficiently high types gain.

### Attempt 3: Degenerate Distribution
**Tried:** Single type.

**Result:** SURVIVES — There is no distributional split, but the threshold statement for the single type remains true.

### Attempt 4: Corner Solutions
**Tried:** No continuing buyers.

**Result:** SURVIVES VACUOUSLY — The proposition applies to types that buy in both regimes; if there are none, it is vacuously true but economically empty.

### Attempt 5: Relaxing A5 quasi-linearity
**Tried:** Nonlinear price utility.

**Result:** CONDITIONAL — The exact threshold \(\Delta p/\Delta v\) can fail if price enters utility nonlinearly. This confirms A5 is binding.

### Attempt 6: Alternative Equilibrium
**Tried:** Multiple equilibria.

**Result:** SURVIVES — It is a comparison between two regimes, not an equilibrium selection result.

### Attempt 7: Strategic Manipulation
**Tried:** Consumer deviation.

**Result:** SURVIVES — Utility comparison directly governs purchase utility.

### Attempt 8: Existence Failure Check
**Tried:** Undefined \(\Delta v\).

**Result:** SURVIVES under A6 and \(q_1>q_0\), because \(\Delta v>0\).

**P_C1 Overall verdict:** ROBUST.

---

## [P_C2] — Counterexample Analysis

### Attempt 1: Two-Type Reduction
**Tried:** Two-type distribution.

**Result:** CONDITIONAL — The derivative expression becomes a discrete sum and may be nonsmooth when the cutoff crosses a type. The continuous-distribution version survives, but discrete types require a modified finite-difference statement.

### Attempt 2: Extreme Parameter Values
**Tried:** Cutoff at \(\underline\theta\) or \(\overline\theta\).

**Result:** SURVIVES AS STATED — P_C2 assumes an interior cutoff. At boundary coverage, the formula must be adjusted.

### Attempt 3: Degenerate Distribution
**Tried:** No heterogeneity.

**Result:** CONDITIONAL — Conditional expectation remains defined if there are buyers, but the distributional meaning disappears. The derivative threshold still has a representative-consumer interpretation.

### Attempt 4: Corner Solutions
**Tried:** Full coverage and zero coverage.

**Result:** ⚠️ BREAKS — Scope vulnerability.

Counterexample: If \(\theta^*(q)\le\underline\theta\), all consumers buy, and the lower integration bound is fixed at \(\underline\theta\), not \(p(q)/v(q)\). The stated formula using the conditional mean above \(\theta^*(q)\) is no longer correct.

What fails: The interior-cutoff expression cannot be applied outside its stated domain.

Severity: MEDIUM.

Fix options:
  Option A: Keep P_C2 explicitly restricted to interior market coverage.
  Option B: Add separate full-coverage and zero-coverage corollaries.
  Option C: Use clipped cutoff \(\hat\theta(q,p)=\max\{\underline\theta,\min\{p/v(q),\overline\theta\}\}\) and derive piecewise formulas.

### Attempt 5: Relaxing differentiability of \(p(q)\)
**Tried:** Kinked pass-through schedule.

**Result:** CONDITIONAL — Derivative formula fails at kinks; can be replaced by one-sided derivatives or finite changes.

### Attempt 6: Alternative Equilibrium
**Tried:** Multiple equilibrium prices for same \(q\).

**Result:** CONDITIONAL — If \(p(q)\) is equilibrium selected, P_C2 depends on the selected branch.

### Attempt 7: Strategic Manipulation
**Tried:** None relevant.

**Result:** SURVIVES.

### Attempt 8: Existence Failure Check
**Tried:** No interior coverage.

**Result:** SURVIVES AS STATED, but economically the proposition becomes inapplicable.

**P_C2 Overall verdict:** CONDITIONAL — strong core result, but must be stated as an interior-coverage proposition with separate boundary cases.

---

## [P_W1] — Counterexample Analysis

### Attempt 1: Two-Type Reduction
**Tried:** Two types with fixed coverage containing both types.

**Result:** SURVIVES for marginal wedge — the average served type exceeds the marginal served type if both types served and not all mass at the cutoff.

### Attempt 2: Extreme Parameter Values
**Tried:** All served consumers arbitrarily close to the cutoff type.

**Result:** SURVIVES BUT WEAK — The wedge becomes arbitrarily small, though still positive with nondegenerate support.

### Attempt 3: Degenerate Distribution
**Tried:** All served consumers have the same type.

**Result:** SURVIVES AS STATED if non-degeneracy is required; otherwise the strict wedge fails.

### Attempt 4: Corner Solutions
**Tried:** Full exclusion or single marginal type served.

**Result:** CONDITIONAL — The fixed-coverage FOC comparison is not meaningful if demand is zero or the served set has measure zero.

### Attempt 5: Relaxing concavity / single-peakedness
**Tried:** Nonconcave quality benefits or costs generating multiple local optima.

**Result:** ⚠️ BREAKS — Strong interpretation.

Counterexample: Even if the planner's marginal benefit exceeds the firm's at a given \(q\), nonconcavity can make the firm's global optimum at a higher local peak than the planner's global optimum. Thus the marginal wedge does not imply global quality ordering without additional curvature.

What fails: The statement “therefore enterprise quality is below planner quality” fails if the proposition is read as a global quality-level comparison.

Severity: HIGH for the strong version; MEDIUM if weakened to a marginal-wedge result.

Fix options:
  Option A: Weaken P_W1 to a marginal wedge proposition only.
  Option B: Add strict concavity / single-crossing assumptions to infer quality-level ordering.
  Option C: State global ordering only in a corollary under additional sufficient conditions.

### Attempt 6: Alternative Equilibrium
**Tried:** Multiple firm optima.

**Result:** CONDITIONAL — Global ordering may depend on equilibrium selection; marginal wedge remains valid at a fixed cutoff.

### Attempt 7: Strategic Manipulation
**Tried:** Consumer manipulation of cutoff.

**Result:** SURVIVES — Consumers are atomistic.

### Attempt 8: Existence Failure Check
**Tried:** No interior cutoff.

**Result:** CONDITIONAL — The proposition requires fixed interior coverage.

**P_W1 Overall verdict:** NEEDS FIX — robust as a marginal wedge, unsafe as global quality ordering without extra curvature.

---

## [P_W2] — Counterexample Analysis

### Attempt 1: Two-Type Reduction
**Tried:** Low and high type, quality increase, price increase.

**Result:** SURVIVES — It is easy to make low type lose and high type gain by choosing \(\theta^G\) between the two types.

### Attempt 2: Extreme Parameter Values
**Tried:** Very high price increase.

**Result:** CONDITIONAL — Too high a price can eliminate all buyers, which may still reduce consumer surplus but eliminates the “some continuing buyers gain” part.

### Attempt 3: Degenerate Distribution
**Tried:** Single type.

**Result:** SURVIVES AS A LIMIT — Distributional split disappears; P_W2 requires heterogeneity and is not meant for degenerate distributions.

### Attempt 4: Corner Solutions
**Tried:** All consumers exit after upgrade.

**Result:** CONDITIONAL — Consumer surplus falls, but the proposition’s claim about low-type continuing buyers and winners/losers no longer applies.

### Attempt 5: Requiring equilibrium-reoptimized prices
**Tried:** Interpret \((q_0,p_0)\) and \((q_1,p_1)\) as both firm-optimal prices for their quality levels.

**Result:** ⚠️ BREAKS / SCOPE VULNERABILITY.

Counterexample: The proposition as written allows arbitrary regimes or arbitrary pass-through. If instead \(p_i\) must be the firm's reoptimized equilibrium price at \(q_i\), one cannot guarantee that sufficiently high pass-through is feasible without specifying costs and demand. For some cost functions and distributions, equilibrium pass-through may be low enough that aggregate CS does not fall.

What fails: The broad “such parameter values exist whenever price pass-through can be sufficiently large” is valid for exogenous pass-through, but not automatically for equilibrium pass-through.

Severity: MEDIUM.

Fix options:
  Option A: State P_W2 as an exogenous/pass-through regime comparison.
  Option B: Provide a specific equilibrium example with chosen \(v,c,K,F\) in which firm reoptimization generates the reversal.
  Option C: Weaken the claim to “if pass-through satisfies [explicit inequality], then CS falls.”

### Attempt 6: Alternative Equilibrium
**Tried:** Multiple equilibrium prices after upgrade.

**Result:** CONDITIONAL — P_W2 may hold for one selected equilibrium but not another unless price selection is specified.

### Attempt 7: Strategic Manipulation
**Tried:** None relevant.

**Result:** SURVIVES.

### Attempt 8: Existence Failure Check
**Tried:** No feasible \(p_1\) leaving positive measure of buyers.

**Result:** SURVIVES if price is freely chosen within feasible range and type support has high enough upper bound; conditional otherwise.

**P_W2 Overall verdict:** CONDITIONAL — keep only with explicit pass-through condition or provide a concrete equilibrium example.

---

## [P_M1] — Counterexample Analysis

### Attempt 1: Two-Type Reduction
**Tried:** Two types, each classified as continuing, entrant, exiter, or nonbuyer.

**Result:** SURVIVES — The set decomposition remains exact.

### Attempt 2: Extreme Parameter Values
**Tried:** No entrants, no exiters, or no continuing buyers.

**Result:** SURVIVES — Empty-set integrals are zero.

### Attempt 3: Degenerate Distribution
**Tried:** Single type.

**Result:** SURVIVES — The decomposition becomes a one-point analog.

### Attempt 4: Corner Solutions
**Tried:** Full coverage or zero coverage.

**Result:** SURVIVES — The relevant sets adjust automatically.

### Attempt 5: Relaxing binding assumptions
**Tried:** Drop monotonicity of \(v\).

**Result:** SURVIVES as an accounting identity, though the interpretation as quality upgrading fails.

### Attempt 6: Alternative Equilibrium
**Tried:** Multiple equilibria.

**Result:** SURVIVES — The identity applies to any two regimes.

### Attempt 7: Strategic Manipulation
**Tried:** Not relevant.

**Result:** SURVIVES.

### Attempt 8: Existence Failure Check
**Tried:** Undefined purchase sets.

**Result:** SURVIVES if purchase utility is defined.

**P_M1 Overall verdict:** ROBUST.

---

## [P_B1] — Counterexample Analysis

### Attempt 1: Two-Type Reduction
**Tried:** Two types and high pass-through.

**Result:** SURVIVES — As threshold rises, fewer types gain.

### Attempt 2: Extreme Parameter Values
**Tried:** \(\Delta v\to0\).

**Result:** CONDITIONAL — If \(\Delta v\) is near zero, \(\theta^G=\Delta p/\Delta v\) can explode; the result should assume \(\Delta v>0\).

### Attempt 3: Degenerate Distribution
**Tried:** Single type.

**Result:** SURVIVES — Distributional conflict disappears.

### Attempt 4: Corner Solutions
**Tried:** No continuing buyers.

**Result:** ⚠️ BREAKS — Wording vulnerability.

Counterexample: If high pass-through causes all consumers to exit, the statement “almost all low/middle types are harmed or exit” is too imprecise because there are no continuing buyers to be harmed. Exit is the only channel.

What fails: The proposition mixes “continuing buyers lose” and “consumers exit” without separating them.

Severity: LOW.

Fix options:
  Option A: Split P_B1 into two statements: one about continuing-buyer gains, one about exit.
  Option B: State the result in terms of the measure of gainers among continuing buyers.
  Option C: Add a condition that the continuing-buyer set remains positive measure.

### Attempt 5: Relaxing continuous distribution
**Tried:** Atom at \(\overline\theta\).

**Result:** CONDITIONAL — If there is an atom at the top type, the measure of gainers need not converge to zero as \(\theta^G\uparrow\overline\theta\).

### Attempt 6: Alternative Equilibrium
**Tried:** Multiple regimes.

**Result:** SURVIVES as a regime-comparison statement.

### Attempt 7: Strategic Manipulation
**Tried:** Not relevant.

**Result:** SURVIVES.

### Attempt 8: Existence Failure Check
**Tried:** Undefined \(\theta^G\) when \(\Delta v=0\).

**Result:** SURVIVES under \(\Delta v>0\), which follows from quality increase and A6.

**P_B1 Overall verdict:** CONDITIONAL — needs wording precision and no atom at upper bound.

---

## Consolidated Fixes Required

The following fixes are REQUIRED before the paper can proceed:

| Counterexample | Affected Proposition | Recommended Fix | Fix Type |
|---------------|---------------------|----------------|---------|
| CE_1 | P_E1 | Keep compact action space or prove endogenous finite price/quality bounds; specify tie-breaking at \((q,p)=(0,0)\). | ASSUMPTION / TECHNICAL LEMMA |
| CE_2 | P_C2 | Restrict theorem to interior market coverage and add separate boundary-case formulas. | CLAIM / SCOPE |
| CE_3 | P_W1 | Weaken to a marginal-wedge proposition unless strict concavity/single-peakedness is added for global quality ordering. | CLAIM |
| CE_4 | P_W2 | State as pass-through regime comparison, or provide a concrete equilibrium example with firm-reoptimized prices. | CLAIM / SCOPE |
| CE_5 | P_B1 | Split gainers among continuing buyers from exiters; require positive continuing-buyer measure and no top atom. | CLAIM |

---

## Edge Cases to Document in the Paper

| Edge Case | Proposition | How to Handle |
|-----------|------------|--------------|
| \(q=0,p=0\) makes all consumers indifferent | P_E1 | Add tie-breaking note; measure-zero issue does not apply when all types indifferent. |
| Full coverage or zero coverage | P_C2 | Provide boundary formulas or explicitly restrict main theorem to interior coverage. |
| Degenerate type distribution | P_W2, P_B1 | State heterogeneity is necessary for distributional conflict. |
| Multiple firm optima | P_U1, P_W2 | Use selection rule or restrict to strict quasi-concavity. |
| Equilibrium vs exogenous pass-through | P_C2, P_W2 | Clearly define whether \(p(q)\) is exogenous, selected, or equilibrium-reoptimized. |

---

## Robustness Summary

**Overall robustness assessment:** MODERATE

The supporting propositions P_U1, P_C1, and P_M1 are robust. The central proposition P_C2 is strong but must remain explicitly interior. The two welfare propositions require refinement: P_W1 should be stated as a marginal wedge unless stronger curvature assumptions are added, and P_W2 needs either a clear pass-through condition or an explicit equilibrium example. These are fixable issues, but they should be resolved before Stage 9 interpretation and final manuscript drafting.
