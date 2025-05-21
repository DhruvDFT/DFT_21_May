# MBIST & Memory Repair

**Q1.** In a split‑rail SRAM macro with write‑assist, which DFT considerations ensure MBIST will not damage the cell during high‑voltage stress patterns?

**Q2.** Describe the impact of two‑port RAM address collisions on March algorithm fault detection.

**Q3.** Explain how redundancy‑aware BIRA (Built‑In Repair Analysis) alters the pass/fail criteria compared to traditional MBIST.

**Q4.** Why is it important to decouple memory power domains during retention test modes?

**Q5.** Outline a debug flow for a memory macro that consistently fails March‑C‑ minus test but passes March‑B‑.

**Q6.** How do you select an address scrambling seed for fuse‑based repair without revealing customer IP topology?

**Q7.** Explain the difference between wordline‑short and bitline‑short faults and how each manifests in MBIST signature analysis.

**Q8.** What additional DFT hooks are required to support soft‑repair via eFuse after package assembly?

**Q9.** In NVM (eFlash) macros, why is coupling fault testing more complex, and how do you approximate it with limited states?

**Q10.** How does built‑in self‑repair logic interact with ECC on safety‑critical memories (e.g., automotive ASIL‑D level)?

**Q11.** Describe a power‑aware MBIST schedule to minimize IR drop when testing hundreds of small SRAMs in parallel.

**Q12.** What is the role of pipeline registers in high‑frequency MBIST controllers and how do they influence test time?

**Q13.** Suggest a scheme to log fail addresses without extending test time in an on‑chip context with limited scan IO.

**Q14.** Compare the diagnostic resolution of MBIST‑based fail address capture versus functional LBIST signature mismatch.

**Q15.** How would you qualify partial redundancy coverage when only a subset of spares can be activated per bank?
