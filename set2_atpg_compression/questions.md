# ATPG & Compression

**Q1.** You observe low transition‑fault coverage even after generating 5 million patterns on a 7 nm CPU core. List two likely root causes and remedies.

**Q2.** How does fault collapsing improve ATPG efficiency and what information must always be preserved after collapsing?

**Q3.** Describe a scenario where X‑blocking during ATPG leads to over‑masking and lowers coverage.

**Q4.** Explain how on‑chip decompressor width affects pattern count and tester memory.

**Q5.** In an LBIST flow, why is pseudo‑random phase often followed by deterministic top‑up patterns?

**Q6.** How can you estimate optimal compression ratio before silicon if scan‑compression IP is already fixed?

**Q7.** What are “test points” in ATPG and when should they be inserted?

**Q8.** During pattern validation, you see unknowns propagating to signature registers through MUXes controlled by configurable fuses. Suggest a fix.

**Q9.** Explain how OOC (Out‑of‑Cone) faults can inflate reported coverage in partial‑scan designs.

**Q10.** What vector translation issues can surface when moving patterns from simulation‑based ATPG to tester format (WGL/STIL)?

**Q11.** Why is slack‑based back‑annotation essential when generating transition‑delay patterns on advanced nodes?

**Q12.** Describe a method to debug "aborted faults" that persist across pattern generation iterations.

**Q13.** How does physical location of decompressors influence IR drop during high‑speed scan shift?

**Q14.** What is the trade‑off between shift‑frequency and capture‑frequency in at‑speed test?

**Q15.** Suggest two metrics besides traditional fault coverage that you would present to management to justify ATPG quality.
