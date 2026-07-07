# Model Primitives

**Date:** 2026-06-18
**Stage:** 4 — Model Primitives

---

## Model Overview

本模型是一个风格化的垄断质量—价格选择模型。一个具有市场势力的企业选择产品质量 \(q\) 与统一价格 \(p\)。消费者在质量偏好上异质，类型为 \(\theta\)，购买产品时获得净效用 \(\theta v(q)-p\)，不购买时获得外部选项 0。产品质量升级一方面提高购买者的毛效用，另一方面通过质量成本与企业最优定价改变价格，并移动购买参与门槛。因此，模型能够同时刻画质量升级的直接效用收益、价格传导损失、参与/排除效应，以及企业私有质量选择与社会规划者质量选择之间的偏离。

本阶段继承 Stage 3b 的 canonical handoff：基线为 monopoly product-quality choice / price discrimination 谱系；采用单一质量—价格对而非完整质量菜单；将完整 screening 菜单留作扩展。

---

## 1. Agents

| Label | Name | Count | Characteristics |
|-------|------|-------|----------------|
| \(F\) | 企业 / monopolist | 1 | 风险中性；具有市场势力；选择质量 \(q\) 与价格 \(p\) 以最大化利润 |
| \(C_\theta\) | 消费者类型 \(\theta\) | 连续统，总质量 1 | 类型 \(\theta\in\Theta=[\underline\theta,\overline\theta]\)，其中 \(0<\underline\theta<\overline\theta<\infty\)；\(\theta\) 表示对质量的边际估值 |
| \(SP\) | 社会规划者 | 基准对象，不是博弈参与者 | 用于福利比较；选择质量和服务集合以最大化消费者剩余或总剩余 |

---

## 2. Timing

1. 自然确定消费者类型分布 \(F(\theta)\)。分布函数 \(F:\Theta\to[0,1]\) 连续可微，密度 \(f(\theta)>0\) 对所有 \(\theta\in\Theta\) 成立，并且 \(F\) 是共同知识。
2. 企业观察分布 \(F\)、质量收益函数 \(v\)、单位生产成本函数 \(c\)、固定质量成本函数 \(K\)，但不观察单个消费者的具体类型 \(\theta\)。
3. 企业选择质量 \(q\in Q=[0,\overline q]\) 与价格 \(p\in P=[0,\overline p]\)，其中 \(0<\overline q<\infty\)，\(0<\overline p<\infty\)。
4. 所有消费者观察 \((q,p)\)，每个消费者 \(C_\theta\) 私下知道自己的 \(\theta\)。
5. 每个消费者选择购买 \(a(\theta)\in\{0,1\}\)，其中 \(a=1\) 表示购买，\(a=0\) 表示不购买。
6. 需求、利润、消费者效用与福利实现。

**Game type:** 有限阶段、顺序行动、静态一次性市场博弈。

**Commitment:** 企业在消费者购买前承诺质量 \(q\) 与价格 \(p\)。消费者观察后作出购买决定。企业不能在消费者购买后调整价格或降低质量。

---

## 3. Information Structure

**Complete / Incomplete information:**
企业与消费者对模型结构、函数 \(v,c,K\)、类型分布 \(F\) 和所选 \((q,p)\) 具有共同知识；单个消费者类型 \(\theta\) 是消费者自己的私人信息。因此，消费者侧存在私人类型，但企业只通过分布形成需求。

**Private information:**
- 每个消费者 \(C_\theta\) 私下观察自身类型 \(\theta\in\Theta=[\underline\theta,\overline\theta]\)。
- 企业不观察个体 \(\theta\)，但知道 \(F\) 与 \(f\)。

**Public information:**
- 质量 \(q\)、价格 \(p\)、质量收益函数 \(v\)、成本函数 \(c,K\)、类型分布 \(F\) 均为公共信息。

**Signals:**
- 基线模型无信号结构。质量完全可观察；因此本模型不是逆向选择或信号传递模型。

**Common knowledge:**
- 所有主体理性、博弈时序、可行动作、收益函数、外部选项、类型分布和企业承诺能力均为共同知识。

---

## 4. Preferences

### 消费者 \(C_\theta\)

- 质量收益函数：\(v:Q\to\mathbb R_+\)，满足 \(v(0)=0\)、\(v'(q)>0\)、\(v''(q)\le 0\)。
- 若购买，类型 \(\theta\) 的净效用为
  \[
  u(\theta,q,p)=\theta v(q)-p.
  \]
- 若不购买，外部选项效用为
  \[
  u_0(\theta)=0.
  \]
- 消费者选择购买当且仅当
  \[
  \theta v(q)-p\ge 0.
  \]
- 消费者风险中性；无动态贴现。

### 企业 \(F\)

- 单位生产成本函数：\(c:Q\to\mathbb R_+\)，满足 \(c'(q)\ge0\)，并允许 \(c''(q)\ge0\)。
- 固定质量成本函数：\(K:Q\to\mathbb R_+\)，满足 \(K(0)=0\)、\(K'(q)\ge0\)、\(K''(q)>0\)。
- 给定 \((q,p)\)，需求为 \(D(q,p)\)，定义见第 6 节。
- 企业利润为
  \[
  \Pi(q,p)=[p-c(q)]D(q,p)-K(q).
  \]
- 企业选择 \((q,p)\in Q\times P\) 最大化 \(\Pi(q,p)\)。企业风险中性。

### 社会规划者 \(SP\)

- 社会规划者不是博弈参与者，仅用于基准比较。
- 总剩余基准下，规划者选择 \(q\) 和服务集合 \(S\subseteq\Theta\) 最大化
  \[
  W(q,S)=\int_S [\theta v(q)-c(q)]f(\theta)d\theta-K(q),
  \]
  其中价格只是转移，不进入总剩余。
- 消费者剩余基准下，规划者可比较消费者剩余最大化质量与企业利润最大化质量的差异。

---

## 5. Action and Strategy Spaces

### 企业 \(F\)

- **Action space:**
  \[
  A_F=Q\times P=[0,\overline q]\times[0,\overline p].
  \]
- **Strategy:** 在基线一次性模型中，企业策略是选择一个质量—价格对 \((q,p)\)。
- **Constraints:** \(q\ge0\)、\(p\ge0\)、成本函数有限；若 \(D(q,p)=0\)，利润为 \(-K(q)\)。

### 消费者 \(C_\theta\)

- **Action space:**
  \[
  A_C=\{0,1\},
  \]
  其中 1 表示购买，0 表示不购买。
- **Strategy:**
  \[
  a_\theta(q,p)=
  \begin{cases}
  1, & \text{if } \theta v(q)-p\ge0,\\
  0, & \text{if } \theta v(q)-p<0.
  \end{cases}
  \]
- **Constraints:** 消费者最多购买一单位产品；无借贷或预算约束，价格支付已通过准线性效用表示。

---

## 6. State Variables and Outcome Space

**State variables:**
- \(\theta\in\Theta=[\underline\theta,\overline\theta]\)：消费者质量偏好类型。
- \(F(\theta)\)：类型分布函数；\(f(\theta)>0\)：密度。
- \(q\in Q=[0,\overline q]\)：产品质量。
- \(p\in P=[0,\overline p]\)：价格。
- \(v(q)\)：质量带来的毛效用强度。
- \(c(q)\)：单位生产成本。
- \(K(q)\)：固定质量成本。

**Outcome space:**
- 质量—价格对 \((q,p)\in Q\times P\)。
- 消费者购买函数 \(a_\theta(q,p)\in\{0,1\}\)。
- 需求 \(D(q,p)\in[0,1]\)。
- 利润 \(\Pi(q,p)\in\mathbb R\)。
- 消费者剩余 \(CS(q,p)\in\mathbb R_+\)。
- 总剩余 \(TS(q,p)\in\mathbb R\)。

**Outcome function:**

当 \(v(q)>0\) 时，购买 cutoff 为
\[
\theta^*(q,p)=\frac{p}{v(q)}.
\]
实际参与门槛为
\[
\hat\theta(q,p)=\max\{\underline\theta,\min\{\theta^*(q,p),\overline\theta\}\}.
\]
若 \(\theta^*(q,p)\le\underline\theta\)，所有消费者购买；若 \(\theta^*(q,p)>\overline\theta\)，无人购买。需求为
\[
D(q,p)=1-F(\theta^*(q,p))
\]
在 interior 情形 \(\theta^*(q,p)\in[\underline\theta,\overline\theta]\) 下成立；边界情形按上述全覆盖或零覆盖处理。

消费者剩余为
\[
CS(q,p)=\int_{\{\theta:\theta v(q)-p\ge0\}}[\theta v(q)-p]f(\theta)d\theta.
\]
总剩余为
\[
TS(q,p)=\int_{\{\theta:\theta v(q)-p\ge0\}}[\theta v(q)-c(q)]f(\theta)d\theta-K(q).
\]

质量升级从 \((q_0,p_0)\) 到 \((q_1,p_1)\)，其中 \(q_1>q_0\)。对持续购买者 \(\theta\) 的净效用变化为
\[
\Delta u_\theta=\theta[v(q_1)-v(q_0)]-(p_1-p_0).
\]
进入者、退出者和持续非购买者通过购买集合变化单独计入 ex ante 消费者剩余变化。

---

## 7. Equilibrium Concept Candidates

### Candidate A: Subgame Perfect Equilibrium (SPE)

- **When appropriate:** 企业先选择 \((q,p)\)，消费者观察后购买或退出；这是一个顺序行动博弈。
- **What it requires:** 消费者在每个观察到的 \((q,p)\) 后最优选择购买；企业预见消费者需求函数并选择利润最大化 \((q,p)\)。
- **Potential issues:** 若没有紧致动作空间和连续收益，均衡存在可能需要额外条件；本模型通过 \(Q\) 与 \(P\) 紧致、函数连续来避免该问题。

### Candidate B: Monopoly Quality-Pricing Optimum with Consumer Best Responses

- **When appropriate:** 关注单企业质量与价格选择时，可把均衡写为企业最大化问题加消费者最优反应。
- **What it requires:** 给定 \((q,p)\)，消费者需求 \(D(q,p)\) 明确；企业选择 \((q,p)\in Q\times P\) 最大化 \(\Pi(q,p)\)。
- **Potential issues:** 这不是标准命名的博弈均衡概念，但与本模型的 SPE 等价。

### Candidate C: Bayesian Nash Equilibrium (BNE)

- **When appropriate:** 若把每个消费者类型的购买策略视为类型依赖策略，且企业只知道类型分布，则可用 BNE 表述。
- **What it requires:** 类型空间、先验分布、类型条件策略。
- **Potential issues:** 对本模型而言 BNE 表述较重；由于企业先动并承诺 \((q,p)\)，SPE 更直接。

### ★ Recommended equilibrium concept: Subgame Perfect Equilibrium (SPE)

**Justification:**
本模型具有清晰的顺序时序：企业先承诺质量与价格，消费者后观察并购买或退出。因此 SPE 能自然刻画“企业预见需求反应并选择 \((q,p)\)”的逻辑。形式上，SPE 等价于企业在消费者最优购买规则诱导出的需求函数上求解利润最大化问题。

---

## 8. Social Planner Benchmarks

### First-Best Total Surplus Benchmark

社会规划者选择质量 \(q\in Q\) 与服务集合 \(S\subseteq\Theta\) 最大化总剩余：
\[
\max_{q\in Q,S\subseteq\Theta} \int_S [\theta v(q)-c(q)]f(\theta)d\theta-K(q).
\]
给定 \(q\)，最优服务规则为服务所有满足
\[
\theta v(q)-c(q)\ge0
\]
的消费者。因此规划者 cutoff 为
\[
\theta^{SP}(q)=\frac{c(q)}{v(q)}
\]
在 interior 情形下成立。第一最佳质量 \(q^{FB}\) 解决
\[
q^{FB}\in\arg\max_{q\in Q}\int_{\theta\ge\theta^{SP}(q)}[\theta v(q)-c(q)]f(\theta)d\theta-K(q).
\]

### Consumer-Surplus Benchmark

为了直接研究“消费者效用联通”，也定义消费者剩余最大化基准。给定企业成本传导规则或给定价格函数 \(p(q)\)，消费者剩余最大化质量为
\[
q^{CS}\in\arg\max_{q\in Q} CS(q,p(q)).
\]
该基准用于比较利润最大化质量 \(q^M\) 是否过高或过低，以及质量升级是否提高消费者剩余。

### Firm Optimum

企业均衡质量—价格为
\[
(q^M,p^M)\in\arg\max_{(q,p)\in Q\times P}\Pi(q,p).
\]
比较 \(q^M\)、\(q^{FB}\) 和 \(q^{CS}\) 将给出企业私有激励与消费者/社会最优之间的质量扭曲。

---

## 9. Internal Consistency Check

| Check | Status | Notes |
|-------|--------|-------|
| All variables defined before use | ✓ | 所有核心符号 \(\theta,F,f,q,p,v,c,K,D,CS,TS,\Pi\) 均已定义并给出域。 |
| Equilibrium concept compatible with action/information space | ✓ | 企业先动、消费者后动，SPE 与时序和策略空间一致。 |
| Budget/resource constraints consistent across agents | ✓ | 消费者准线性效用中价格支付明确；企业成本与需求一致。 |
| Timing internally consistent (no conditioning on future events) | ✓ | 企业只基于已知分布选择；消费者只基于观察到的 \((q,p)\) 和自身类型选择。 |
| Model generates the tension from Stage 1 | ✓ | 质量提高同时改变 \(\theta v(q)\)、价格和参与 cutoff，可生成直接效用增益与价格/排除效应之间的张力。 |

**Outstanding issues:**
- Stage 5 需要审查准线性效用、单维垂直质量、企业承诺质量、紧致价格上界 \(\overline p\) 等假设的经济含义。
- Stage 6 需要避免只提出定义性命题，必须推导非平凡的阈值、分配或 firm-vs-planner 扭曲结果。

---

## Notation Summary

| Symbol | Meaning | Domain |
|--------|---------|--------|
| \(F\) | 企业 / monopolist | 单一主体 |
| \(C_\theta\) | 类型为 \(\theta\) 的消费者 | 连续统，质量 1 |
| \(SP\) | 社会规划者基准 | 非博弈参与者 |
| \(\theta\) | 消费者质量偏好类型 | \([\underline\theta,\overline\theta]\)，\(0<\underline\theta<\overline\theta<\infty\) |
| \(F(\theta)\) | 类型分布函数 | CDF on \(\Theta\) |
| \(f(\theta)\) | 类型密度 | \(f(\theta)>0\) on \(\Theta\) |
| \(q\) | 产品质量 | \([0,\overline q]\) |
| \(p\) | 产品价格 | \([0,\overline p]\) |
| \(v(q)\) | 质量带来的毛效用函数 | \(\mathbb R_+\)，\(v(0)=0,v'>0,v''\le0\) |
| \(c(q)\) | 单位生产成本 | \(\mathbb R_+\)，\(c'\ge0\) |
| \(K(q)\) | 固定质量成本 | \(\mathbb R_+\)，\(K(0)=0,K'\ge0,K''>0\) |
| \(a_\theta(q,p)\) | 类型 \(\theta\) 的购买决策 | \(\{0,1\}\) |
| \(\theta^*(q,p)\) | 购买 cutoff | \(p/v(q)\) when \(v(q)>0\) |
| \(D(q,p)\) | 市场需求 | \([0,1]\) |
| \(u(\theta,q,p)\) | 购买时净效用 | \(\theta v(q)-p\) |
| \(\Pi(q,p)\) | 企业利润 | \([p-c(q)]D(q,p)-K(q)\) |
| \(CS(q,p)\) | 消费者剩余 | \(\int_{\theta v(q)-p\ge0}[\theta v(q)-p]f(\theta)d\theta\) |
| \(TS(q,p)\) | 总剩余 | \(\int_{\theta v(q)-p\ge0}[\theta v(q)-c(q)]f(\theta)d\theta-K(q)\) |
| \(q^M,p^M\) | 企业均衡质量与价格 | \(\arg\max\Pi(q,p)\) |
| \(q^{FB}\) | 第一最佳总剩余质量 | \(\arg\max W(q,S)\) |
| \(q^{CS}\) | 消费者剩余最大化质量 | \(\arg\max CS(q,p(q))\) |
