This repository contains the source of the **O15** Cosmochrony paper  
*Observable-Class Derivation Mismatch and the Heisenberg Transfer No-Go:
From Proxy Capacity to Block-Level Span Dynamics*.

**Version 1.15.2.** The non-equivalence theorem and aggregation no-go are unchanged.
This version makes the stronger conclusion explicit: the native Heisenberg identity is
$\Delta r_n=|S_n|\Sigma_n$, whereas the Born--Infeld square-root factor belongs to the LPS
model. The legacy C1/C2 formulas are phenomenological diagnostics, not native growth laws.

This work extends the **spectral admissibility sub-programme** by auditing the
derivation chain **O3–O7** in light of the exact Weil-block results of **O12–O14**.

While **O14** established that the exact observable does not satisfy the proxy-level
relation between the capacity exponent and the cascade exponent, it still left open
a crucial question: **where exactly does the derivation fail?**

The present work answers that question.

It shows that the mismatch is **not** due to:
- finite-size effects
- numerical instability
- central-phase bias
- or an insufficiently refined statistical aggregation of blocks

Instead, the failure occurs at the level of the **growth equation itself**:
the scalar observable entering the O6/O7 derivation is **not equivalent**
to the exact Weil-block observable measured in O12–O14.

---

# Core Result

The paper establishes that the structural relation
$\beta^* = \frac{1}{\delta + \tfrac12}$
derived in **O6–O7** is conditional on the changing-degree LPS model and
does **not transfer to the exact-block setting as constituted in the corpus**.

The main logical result is a **non-transferability theorem**:

- the exponent
  $\hat\delta_{\mathrm{exact}}$
  extracted from the block mean
  $\bar\Sigma_n = \frac{1}{q-1}\sum_c \Sigma_n^{(c)}$
  is **not**, in general, the exponent controlling the dynamic growth law of \(p(n)\)

Thus the O7 chain
$\bar\Sigma_n \sim n^{-\delta}
\quad \Longrightarrow \quad
\beta^* = \frac{1}{\delta + \tfrac12}$
fails in the exact Weil regime.

The native Heisenberg statement is instead

$\Delta r_n=|S_n|\Sigma_n\asymp n^{D-1-\delta}$

on a finite pre-saturation window. It contains neither the changing valence $p(n)$ nor a
native $c_{\mathrm{BI}}\sqrt p$ factor.

---

# Main Structural Results

The paper proves three central points.

## 1. Audit of the O3–O7 chain

The derivation is decomposed into its logical steps:

- **O3**: mass hierarchy from exit ranks
- **O6**: growth-law derivation
- **O7**: capacity reformulation

The result is:

- **O3 remains valid**
- **O6 remains valid in its scalar domain**
- the failure is localised at the point where a **scalar global observable**
  is implicitly substituted by a **mean over exact Weil blocks**

So the issue is not a mathematical error in O3–O7, but a **domain-of-validity failure**.

## 2. Non-equivalence of observables

The paper proves that the exact observable
$\bar\Sigma_n = \frac{1}{q-1}\sum_c \Sigma_n^{(c)}$
cannot be identified with the scalar redundancy observable entering the O6 growth law.

This establishes that:
- \(\hat\delta_{\mathrm{exact}}\) is a **measured block-mean exponent**
- it is not a scalar exponent that may be inserted into the O6 growth equation

## 3. Aggregation no-go

A new formal no-go result shows that **no choice of non-negative block weights**
can produce an aggregation exponent larger than the measured exact exponent.

If
$\hat\delta_{\mathrm{exact}} < 5.0,$
then any block-weighted aggregation still satisfies
$\alpha_{\mathrm{dyn}} \le \hat\delta_{\mathrm{exact}} < 5.0,$
which is far below the target range
$\delta \in [7.4, 10.6].$

This eliminates the entire class of explanations based on:
- better averaging
- better weighting
- better block statistics

The tension cannot be resolved by aggregation alone.

---

# Observable Hierarchy

To avoid mixing distinct objects, the paper introduces a strict hierarchy of symbols:

- \(\hat\delta_{\mathrm{exact}}\):  
  measured exponent from O12/O13 exact Weil-block capacity

- \(\alpha_{\mathrm{dyn}}\):  
  exponent of the block-weighted aggregation observable

- \(\delta_{\mathrm{eff}}\):  
  legacy endpoint diagnostic in C1

- \(\sigma(q)\):  
  additional denominator displacement in the legacy C2 diagnostic

This hierarchy is central to the paper:
the whole point of O15 is precisely that these quantities must **not** be conflated.

---

# Native Identity and Transfer Status

The paper proves the exact identity $\Delta r_n=|S_n|\Sigma_n$ and audits the attempted
transplantation of the LPS growth equation.

What is rigorously established:

- the scalar O6 law does not transfer
- no native pair-capacity growth carrier is defined
- aggregation alone cannot save the target range

What remains conjectural:

- a new native growth carrier, or an explicit two-substrate hypothesis
- any inter-$q$ estimator and its normalisation
- the coupling of a block observable to relational growth

This distinction is made explicit throughout the paper.

---

# Why O15 Matters

O15 is a **clarification paper**, but a decisive one.

It converts the S2 tension from:

- an unexplained discrepancy
- or a possible numerical artefact
- or a vague structural problem

into a **well-posed mathematical programme**.

After O15, the remaining issue is no longer:

> “Why does the exact exponent disagree with the target?”

but rather:

> “Which native Heisenberg growth process, if any, can carry the block-level pair observable?”

That is a much sharper and more calculable question.

---

# Structural Role of O15

O15 follows the chain:

- **O12**: exact Weil-block extraction
- **O13**: asymptotic elimination of the finite-size hypothesis
- **O14**: observable and estimator layers separated
- **O15**: derivation-level failure localised at the growth equation

So O15 is the paper that establishes:

- the issue is **not observational**
- the issue is **not numerical**
- the issue is **not statistical**
- the issue is **dynamic and structural**

---

# What O15 Adds

O15 introduces several key advances:

- a full **audit of the O3–O7 derivation chain**
- a precise theorem on **non-transferability of the scalar proxy derivation**
- a formal **aggregation no-go**
- a strict hierarchy of exponents and correction terms
- an explicit separation between:
    - **proved statements**
    - **structural hypotheses**
    - **open derivational tasks**
- a reformulation of the remaining problem as a **calculable next step**

---

# Interpretation of the Result

The central conceptual outcome is:

- the exact-block mismatch is **not due to bad measurement**
- it is **not due to finite size**
- it is **not due to central-phase bias**
- it is **not due to poor averaging across blocks**

Instead, the O7 scalar growth law has no established native carrier in the
fixed-degree Heisenberg cascade.

This means that the remaining gap must be addressed at the level of:

- the native growth observable
- an equation derived on the same substrate
- and possibly the representation-dependent structure of Weil blocks

---

# Outcome

O15 does **not** resolve the S2 tension completely.

What it does resolve is the **location and nature** of the problem.

The paper establishes that:

- the scalar-to-block passage is the actual failure point
- the block aggregation route cannot restore the target range
- the next step must derive a native carrier on the Heisenberg substrate itself

So O15 transforms S2 from a broad tension into a concrete programme.

---

# Residual Open Problem

The remaining open problems are now sharply separated:

- measure $R_n^{\mathrm{eff}}$ to quantify aggregation
- construct a native pair-capacity growth carrier, or state a new two-substrate hypothesis

Two historical diagnostics are retained for traceability:

## C1 — Imported reciprocal form
The legacy endpoint bookkeeping defines
$\delta_{\mathrm{eff}},$
and inserts it into
$\beta^* = \frac{1}{\delta_{\mathrm{eff}} + \tfrac12}$
as a phenomenological comparison.

## C2 — Additional denominator term
The second diagnostic introduces
$\sigma(q),$
chosen to quantify the displacement needed to hit the reference window.

Neither diagnostic is a native Heisenberg growth law.

---

# Open Directions

1. **Extraction of \(R_n^{\mathrm{eff}}\) (O15-O1)**
   Quantify the aggregation observable from the existing O12/O13 block data

2. **Native growth carrier**
   Construct a Heisenberg process carrying the pair observable

3. **Inter-$q$ estimator**
   Define its target before assigning a $q$-normalisation exponent

4. **Representation-level growth law**  
   Clarify how Born–Infeld boundedness translates from relational variables
   to block-internal representation degrees of freedom

5. **Extension beyond the lepton sector**  
   Investigate whether the same scalar-to-block breakdown appears in
   quark or neutrino-related observables

---

# Status

The programme is now:

- free of algebraic obstruction (**O6**)
- free of geometric obstruction (**O8–O9**)
- free of proxy-level representation obstruction (**O10–O11**)
- exact at the Weil-block level (**O12**)
- asymptotically stabilised (**O13**)
- observable-level mismatch identified (**O14**)
- growth-equation mismatch localised (**O15**)

It does not assume:

- that the O7 scalar map extends to exact Weil blocks
- that block averaging can recover the target
- that \(\hat\delta_{\mathrm{exact}}\) is an exponent entering a native growth equation
- that the remaining tension is merely numerical

---

# Repository Structure

```text
paper/
├── out/      # Compiled O15 PDF
├── tex/      # LaTeX sources
└── README.md
```
# Citation

If you reference this work, please cite:

J. Beau, Observable-Class Derivation Mismatch and the Heisenberg Transfer No-Go:
From Proxy Capacity to Block-Level Span Dynamics,
Zenodo, 2026.

# Acknowledgements

Portions of the derivations, conceptual synthesis, numerical strategy,
and editorial refinement benefited from iterative interactions with
large language models used as analytical assistants.
All theoretical results, computations, and interpretations remain the
sole responsibility of the author.

# Contributions

This repository is intended as a research reference.

Critical feedback, independent verification, alternative derivations
of a native block-level growth carrier, and direct extraction methods for
$R_n^{\mathrm{eff}}$ are welcome.

Please open an issue to discuss conceptual points,
technical details, or possible extensions.
