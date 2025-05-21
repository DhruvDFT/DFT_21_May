    import pytest, answers, re

    KEYWORDS = {
    "q1": [
        "continuity",
        "probe",
        "schematic"
    ],
    "q2": [
        "diagnostic",
        "n‑detect",
        "partition"
    ],
    "q3": [
        "clock",
        "skew",
        "reset"
    ],
    "q4": [
        "signature",
        "suspect",
        "bitmap"
    ],
    "q5": [
        "mapping",
        "coordinates",
        "sdc"
    ],
    "q6": [
        "leakage",
        "io",
        "clamp"
    ],
    "q7": [
        "hierarchical",
        "memory",
        "uninit"
    ],
    "q8": [
        "bypass",
        "mux",
        "isolate"
    ],
    "q9": [
        "cell‑aware",
        "layout",
        "defect"
    ],
    "q10": [
        "slice",
        "binary",
        "bisect"
    ],
    "q11": [
        "probe",
        "scan",
        "id"
    ],
    "q12": [
        "sdf",
        "annotation",
        "delay"
    ],
    "q13": [
        "resistive",
        "parametric",
        "delay"
    ],
    "q14": [
        "cec",
        "equivalence",
        "patch"
    ],
    "q15": [
        "pareto",
        "yield",
        "trend"
    ]
}

    @pytest.mark.parametrize("qid, kw_list", KEYWORDS.items())
    def test_keywords(qid, kw_list):
        ans = answers.STUDENT_ANS.get(qid, "").lower()
        assert ans, f"Answer for {qid} is empty"
        for kw in kw_list:
            assert kw.lower() in ans, f"Missing keyword '{kw}' in {qid}"
