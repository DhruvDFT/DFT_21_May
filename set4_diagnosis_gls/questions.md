# Diagnosis & GLS Debug

**Q1.** You receive silicon with high stuck‑at fail rate localized to a single chain; list three debug steps before suspecting scan stitching errors.

**Q2.** Explain how ATPG diagnostic patterns differ from production patterns and give one benefit and one drawback.

**Q3.** A gate‑level simulation (GLS) of at‑speed patterns shows mismatch only on the first capture cycle; suggest likely causes.

**Q4.** How does signature‑based diagnosis narrow down failing net suspects without full‑vector re‑simulation?

**Q5.** Describe a flow to correlate bitmap fails from tester with logical fail nodes in Verdi or Debussy.

**Q6.** During scan shift on ATE, you observe excessive leakage current; what design‑level DFT checks could have prevented this?

**Q7.** Explain cross‑module path tracing in hierarchical GLS when diagnosing X‑propagation due to uninitialized memories.

**Q8.** In an ASIC using distributed decompression, how can you isolate a stuck‑open fault inside the decompressor fabric?

**Q9.** Describe how cell‑aware test data improves big‑data‑based diagnosis resolution on modern FinFET libraries.

**Q10.** What is "pattern slicing" and why is it useful in post‑silicon debug of intermittent failures?

**Q11.** Suggest two hardware hooks to speed up root‑cause finding of scan chain order swaps after late ECO.

**Q12.** During failure triage, tester logs show negative capture slack but simulation does not; propose a root cause and fix.

**Q13.** Explain how ATPG “exact gate” models assist in distinguishing resistive opens from shorts in diagnosis.

**Q14.** How can you use combinational equivalence checking (CEC) to verify ECO patches applied after diagnosis?

**Q15.** Outline a KPI dashboard you would present to management summarizing week‑over‑week defect pareto evolution.
