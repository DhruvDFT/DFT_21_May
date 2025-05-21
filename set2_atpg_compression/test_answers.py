    import pytest, answers, re

    KEYWORDS = {
    "q1": [
        "slow",
        "timing",
        "correlation",
        "path‑delay"
    ],
    "q2": [
        "equivalence",
        "dominance",
        "representative"
    ],
    "q3": [
        "unknown",
        "mask",
        "x‑block"
    ],
    "q4": [
        "pattern",
        "count",
        "tester",
        "memory"
    ],
    "q5": [
        "pseudo‑random",
        "deterministic",
        "top‑up"
    ],
    "q6": [
        "simulation",
        "toggle",
        "inflation"
    ],
    "q7": [
        "observability",
        "controllability",
        "insert"
    ],
    "q8": [
        "tie‑off",
        "mask",
        "bypass"
    ],
    "q9": [
        "outside",
        "partial",
        "exclude"
    ],
    "q10": [
        "endianness",
        "pin",
        "padding"
    ],
    "q11": [
        "slack",
        "timing",
        "annotate"
    ],
    "q12": [
        "diagnose",
        "constraints",
        "redundant"
    ],
    "q13": [
        "ir",
        "drop",
        "power"
    ],
    "q14": [
        "power",
        "yield",
        "frequency"
    ],
    "q15": [
        "defect",
        "dppm",
        "pattern"
    ]
}

    @pytest.mark.parametrize("qid, kw_list", KEYWORDS.items())
    def test_keywords(qid, kw_list):
        ans = answers.STUDENT_ANS.get(qid, "").lower()
        assert ans, f"Answer for {qid} is empty"
        for kw in kw_list:
            assert kw.lower() in ans, f"Missing keyword '{kw}' in {qid}"
