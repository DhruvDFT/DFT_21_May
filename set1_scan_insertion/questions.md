# Scan Insertion Fundamentals

**Q1.** During scan insertion, what is the primary reason for requiring separate scan enable clock gating from functional mode?

**Q2.** In a low‑power design using multi‑voltage islands, describe a challenge that could arise when inserting scan chains across domains and how to mitigate it.

**Q3.** Why can mux‑D scan cells cause hold‑time violations on short combinational paths, and what two design techniques reduce this risk?

**Q4.** Your scan stitching tool reports an excessive number of "unassigned flop" warnings. List two likely root causes.

**Q5.** Explain how physical placement of scan chains can influence test time and yield.

**Q6.** Describe the trade‑off between a single long scan chain versus multiple shorter balanced chains.

**Q7.** What DRC checks should be run after scan stitching to ensure scan test will not overwrite retention registers?

**Q8.** How does scan insertion interact with clock‑gating cells that gate leaf clocks?

**Q9.** In an SoC with hierarchical synthesis, what extra constraints are needed to guarantee top‑level scan connectability?

**Q10.** What is the effect of inserting asynchronous scan enable on an internally generated test clock?

**Q11.** Describe how bidirectional I/O cells should be handled during scan mode to avoid bus contention.

**Q12.** Why might a designer insert spare scan cells and how are they managed in ATPG?

**Q13.** Outline a flow to validate that scan chain ordering file matches the physical netlist post‑place‑and‑route.

**Q14.** How can scan compression hardware complicate traditional scan insertion DFT rule checks?

**Q15.** List two common defects scan insertion aims to detect that are not easily found by functional simulation.
