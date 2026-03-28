This repository contains the source of the **O15** Cosmochrony paper  
[*Scalar-to-Block Breakdown of the δ → β* Map:
Why the O7 Growth Law Does Not Transfer to Exact Weil Capacity on Heisenberg Graphs*](out/SpectralO15.pdf).

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
derived in **O6–O7** is **valid only for a scalar global observable** and
does **not transfer automatically** to the exact-block setting.

The main logical result is a **non-transferability theorem**:

- the exponent
  $\hat\delta_{\mathrm{exact}}
  \]
  extracted from the block mean
  $\bar\Sigma_n = \frac{1}{q-1}\sum_c \Sigma_n^{(c)}
  \]
  is **not**, in general, the exponent controlling the dynamic growth law of \(p(n)\)

Thus the O7 chain
$\bar\Sigma_n \sim p(n)^{-\delta}
\quad \Longrightarrow \quad
\beta^* = \frac{1}{\delta + \tfrac12}
\]
fails in the exact Weil regime.

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
$\bar\Sigma_n = \frac{1}{q-1}\sum_c \Sigma_n^{(c)}
\]
cannot be identified with the scalar redundancy observable entering the O6 growth law.

This establishes that:
- \(\hat\delta_{\mathrm{exact}}\) is a **measured block-mean exponent**
- not automatically the **dynamic exponent** that controls \(p(n)\)

## 3. Aggregation no-go

A new formal no-go result shows that **no choice of non-negative dynamic weights**
on the blocks can produce a dynamic exponent larger than the measured exact exponent.

If
$\hat\delta_{\mathrm{exact}} < 5.0,
\]
then any block-weighted aggregation still satisfies
$\alpha_{\mathrm{dyn}} \le \hat\delta_{\mathrm{exact}} < 5.0,
\]
which is far below the target range
$\delta \in [7.4, 10.6].
\]

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
  true dynamic exponent entering the modified growth law

- \(\delta_{\mathrm{eff}}\):  
  recast exponent in the conservative scenario C1

- \(\sigma(q)\):  
  structural correction in the stronger scenario C2

This hierarchy is central to the paper:
the whole point of O15 is precisely that these quantities must **not** be conflated.

---

# Effective Growth Law: Status

The paper introduces an **effective growth law under exact-block normalisation**,
but explicitly classifies it as a **hypothesis**, not a theorem.

What is rigorously established:

- the scalar O6 law does not transfer
- a corrected dynamic observable is required
- aggregation alone cannot save the target range

What remains conjectural:

- the precise \(1/q\) normalisation entering the exact-block growth law
- the exponent-level translation involving \(\log q / \log n^*\)
- the final exact form of the modified growth equation

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

> “What is the correct dynamic observable that replaces the scalar O6/O7 quantity in the exact Weil-block regime?”

That is a much sharper and more calculable question.

---

# Structural Role of O15

O15 follows the chain:

- **O12**: exact Weil-block extraction
- **O13**: asymptotic elimination of the finite-size hypothesis
- **O14**: observable-level mismatch identified and corrected
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

Instead:

👉 the O7 scalar growth law is **not the correct equation** in the exact-block regime

This means that the remaining gap must be addressed at the level of:

- the dynamic observable
- the growth equation
- and possibly the representation-dependent structure of Weil blocks

---

# Outcome

O15 does **not** resolve the S2 tension completely.

What it does resolve is the **location and nature** of the problem.

The paper establishes that:

- the scalar-to-block passage is the actual failure point
- the block aggregation route cannot restore the target range
- the next step must operate on the exact dynamic observable itself

So O15 transforms S2 from a broad tension into a concrete programme.

---

# Residual Open Problem

The remaining open problem is now sharply defined:

- what is the correct exact-block observable
  $R_n^{\mathrm{eff}}
  \]
  entering the growth equation for \(p(n)\)?

Two scenarios remain:

## C1 — Conservative recast
A corrected dynamic observable yields a modified exponent
$\delta_{\mathrm{eff}},
\]
but the functional form
$\beta^* = \frac{1}{\delta_{\mathrm{eff}} + \tfrac12}
\]
survives.

## C2 — Structural revision
The exact Weil-block regime requires a further correction
$\sigma(q),
\]
so that the O7 map itself must be structurally revised.

O15 does not decide between C1 and C2,
but shows that the decision must come from the exact dynamic observable,
not from aggregation or reweighting.

---

# Open Directions

1. **Extraction of \(R_n^{\mathrm{eff}}\) (O15-O1)**  
   Build the true dynamic observable from the existing O12/O13 block data

2. **Test of Scenario C1**  
   Determine whether the conservative recast can survive once
   \(R_n^{\mathrm{eff}}\) is measured directly

3. **Derivation of \(\sigma(q)\) if C1 fails**  
   Derive the structural correction from the Weil-block representation itself

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
- that \(\hat\delta_{\mathrm{exact}}\) is the dynamic exponent
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

J. Beau, Scalar-to-Block Breakdown of the δ → β* Map:
Why the O7 Growth Law Does Not Transfer to Exact Weil Capacity on Heisenberg Graphs,
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
of the exact-block growth law, and direct extraction methods for
$R_n^{\mathrm{eff}}$ are welcome.

Please open an issue to discuss conceptual points,
technical details, or possible extensions.
