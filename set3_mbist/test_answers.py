    import pytest, answers, re

    KEYWORDS = {
    "q1": [
        "write",
        "assist",
        "stress",
        "voltage",
        "safe"
    ],
    "q2": [
        "collision",
        "two‑port",
        "march"
    ],
    "q3": [
        "bira",
        "redundancy",
        "fuse"
    ],
    "q4": [
        "power",
        "domain",
        "retention"
    ],
    "q5": [
        "coupling",
        "decoder",
        "timing"
    ],
    "q6": [
        "scramble",
        "seed",
        "security"
    ],
    "q7": [
        "wordline",
        "bitline",
        "signature"
    ],
    "q8": [
        "efuse",
        "scan",
        "repair"
    ],
    "q9": [
        "coupling",
        "erase",
        "charge"
    ],
    "q10": [
        "ecc",
        "repair",
        "priority"
    ],
    "q11": [
        "ir",
        "drop",
        "stagger"
    ],
    "q12": [
        "pipeline",
        "throughput"
    ],
    "q13": [
        "compression",
        "fail",
        "address"
    ],
    "q14": [
        "resolution",
        "bitmap"
    ],
    "q15": [
        "coverage",
        "redundancy",
        "bank"
    ]
}

    @pytest.mark.parametrize("qid, kw_list", KEYWORDS.items())
    def test_keywords(qid, kw_list):
        ans = answers.STUDENT_ANS.get(qid, "").lower()
        assert ans, f"Answer for {qid} is empty"
        for kw in kw_list:
            assert kw.lower() in ans, f"Missing keyword '{kw}' in {qid}"
