"""
o15_o1_nogo_verification.py
Verification of open direction O15-O1 (Section 8, SpectralO15.tex): compute
R_eff from the real O12/O13 pipeline, check the exact identity
R_eff = Sigma_bar * (1 + V_n) of Proposition "Exact identity" (prop:exact-identity),
and check the covariance/OLS-slope hypothesis of Corollary "Aggregation
bound for the dynamical weights" (cor:nogo): does log(1+V_n) have
non-negative OLS slope against log(n) over the fitting window?

This is a per-prime, standalone script (each prime run as an independent
process) with unbuffered output, so progress is visible on the expensive
primes (151, 211 take tens of minutes) rather than only at process exit.
Per-block cost is highly variable (single-digit seconds to 10+ minutes,
depending on the sampled block's saturation depth), so the printed ETA is a
rough running-average estimate, not a reliable countdown -- treat it as an
order-of-magnitude guide, not a promise.

Usage:
    python3 o15_o1_nogo_verification.py <q>

Results (including per-block timings, for future ETA calibration) are
written to results/o15_o1_q<q>.json, so a run's exact numeric output is a
citable artefact on disk, not only a terminal transcript.

Status as of this script's addition (v1.16.1): run and confirmed at q=151
only. The other four tested primes (29, 61, 101, 211) remain open --
O15-O1 is partially, not fully, completed. See the README and
SpectralO15.tex Section 8 for the exact q=151 result and its scope.
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import numpy as np
from spectral_O12 import (RNG_BASE, build_generators, bfs_shells, sample_generic_blocks,
                           compute_block_capacity, ols_loglog)

PARAMS = {
    29:  dict(m_block=50, n_max=8,  bfs_frac=0.99, window=(2, 5)),
    61:  dict(m_block=15, n_max=10, bfs_frac=0.99, window=(2, 7)),
    101: dict(m_block=20, n_max=20, bfs_frac=0.99, window=(3, 10)),
    151: dict(m_block=10, n_max=37, bfs_frac=0.29, window=(3, 12)),
    211: dict(m_block=10, n_max=50, bfs_frac=0.11, window=(3, 13)),
}


def _fmt_eta(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.0f}s"
    m, s = divmod(seconds, 60)
    return f"{m:.0f}m{s:02.0f}s"


def main(q: int) -> None:
    p = PARAMS[q]
    t0 = time.time()
    print(f"q={q}: starting (m_block={p['m_block']}, n_max={p['n_max']}, "
          f"bfs_frac={p['bfs_frac']})", flush=True)

    rng = np.random.default_rng(RNG_BASE + q)
    gens = build_generators(q)

    print(f"q={q}: running BFS...", flush=True)
    shells = bfs_shells(None, None, gens, q, p["bfs_frac"])
    n_shells = len(shells)
    bfs_elapsed = time.time() - t0
    print(f"q={q}: BFS done, {n_shells} shells, {sum(len(s) for s in shells)} nodes "
          f"({bfs_elapsed:.1f}s elapsed)", flush=True)

    blocks = sample_generic_blocks(q, p["m_block"], rng)
    m_block = p["m_block"]

    all_delta_r = []
    block_times = []
    for i, c_block in enumerate(blocks):
        t_block_start = time.time()
        _, delta_r_vals, _, _ = compute_block_capacity(shells, c_block, q, gens, n_max=p["n_max"])
        pad = n_shells - len(delta_r_vals)
        if pad > 0:
            delta_r_vals = np.concatenate([delta_r_vals, np.zeros(pad)])
        all_delta_r.append(delta_r_vals[:n_shells])
        block_times.append(time.time() - t_block_start)

        elapsed = time.time() - t0
        done = i + 1
        remaining = m_block - done
        avg_per_block = (elapsed - bfs_elapsed) / done
        eta = avg_per_block * remaining
        print(f"q={q}: block {done}/{m_block} done ({elapsed:.1f}s elapsed, "
              f"this block {block_times[-1]:.1f}s, "
              f"ETA {_fmt_eta(eta)} at current average -- per-block cost varies "
              f"widely, treat as rough)", flush=True)
    all_delta_r = np.array(all_delta_r)
    shell_sizes = np.array([len(s) for s in shells])

    sigma = all_delta_r / shell_sizes[None, :]
    sigma_bar = sigma.mean(axis=0)

    with np.errstate(divide="ignore", invalid="ignore"):
        V_n = np.where(sigma_bar > 1e-15, sigma.var(axis=0) / sigma_bar**2, np.nan)

    dr_sum = all_delta_r.sum(axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        w = np.where(dr_sum[None, :] > 0, all_delta_r / dr_sum[None, :], 0.0)
    R_eff = (w * sigma).sum(axis=0)

    identity_check = sigma_bar * (1 + V_n)
    resid = float(np.nanmax(np.abs(R_eff - identity_check)))

    n0, n1 = p["window"]
    ns = np.arange(n_shells)
    delta_hat, _, r2_d = ols_loglog(ns, sigma_bar, n0, n1)
    alpha_dyn, _, r2_a = ols_loglog(ns, R_eff, n0, n1)

    Vwin = V_n[n0:n1 + 1]
    mono = bool(np.all(np.diff(1 + Vwin) >= -1e-9))

    # OLS slope of log(1+V_n) against log(n), n>=1 to avoid log(0)
    win_idx = np.arange(n0, n1 + 1)
    win_idx = win_idx[win_idx >= 1]
    logn = np.log(win_idx.astype(float))
    g = np.log(1 + V_n[win_idx])
    slope_g = float(np.polyfit(logn, g, 1)[0]) if len(win_idx) >= 2 else float("nan")

    total_elapsed = time.time() - t0
    print(f"\nq={q} RESULT ({total_elapsed:.1f}s total):", flush=True)
    print(f"  max|R_eff - Sigma_bar*(1+V_n)| = {resid:.3e}  (should be ~0)", flush=True)
    print(f"  delta_hat={delta_hat:.4f}  alpha_dyn={alpha_dyn:.4f}  "
          f"alpha_dyn<=delta_hat: {alpha_dyn <= delta_hat}", flush=True)
    print(f"  (1+V_n) pointwise non-decreasing on window: {mono}", flush=True)
    print(f"  OLS slope of log(1+V_n) vs log(n) on window: {slope_g:.4f}  "
          f"(non-negative: {slope_g >= 0})", flush=True)
    print(f"  V_n[window]={np.round(Vwin, 4).tolist()}", flush=True)

    results_dir = Path(__file__).parent / "results"
    results_dir.mkdir(exist_ok=True)
    out_path = results_dir / f"o15_o1_q{q}.json"
    with open(out_path, "w") as f:
        json.dump({
            "q": q,
            "params": p,
            "rng_base": RNG_BASE,
            "seed": RNG_BASE + q,
            "n_shells": n_shells,
            "total_elapsed_s": total_elapsed,
            "bfs_elapsed_s": bfs_elapsed,
            "block_times_s": block_times,
            "max_abs_residual_identity": resid,
            "delta_hat": float(delta_hat),
            "alpha_dyn": float(alpha_dyn),
            "alpha_dyn_leq_delta_hat": bool(alpha_dyn <= delta_hat),
            "V_n_window": np.round(Vwin, 6).tolist(),
            "one_plus_Vn_pointwise_nondecreasing": mono,
            "ols_slope_log1pVn_vs_logn": slope_g,
            "ols_slope_nonnegative": bool(slope_g >= 0),
        }, f, indent=2)
    print(f"\n  Results written to {out_path}", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]))
