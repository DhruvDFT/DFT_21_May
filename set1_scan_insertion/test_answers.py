    import pytest, answers, re

    KEYWORDS = {
    "q1": [
        "separate",
        "test",
        "clock",
        "gating",
        "isolate"
    ],
    "q2": [
        "level‑shifter",
        "isolation",
        "domain",
        "voltage",
        "mux"
    ],
    "q3": [
        "hold",
        "time",
        "mux",
        "buffer",
        "reorder"
    ],
    "q4": [
        "unconnected",
        "dont_touch",
        "black",
        "box"
    ],
    "q5": [
        "routing",
        "congestion",
        "yield",
        "defect"
    ],
    "q6": [
        "shift",
        "cycles",
        "test",
        "time",
        "compression"
    ],
    "q7": [
        "retention",
        "clamp",
        "upf",
        "state"
    ],
    "q8": [
        "clock",
        "gating",
        "bypass",
        "static"
    ],
    "q9": [
        "scan_in",
        "scan_out",
        "port",
        "tie"
    ],
    "q10": [
        "glitch",
        "metastability",
        "setup"
    ],
    "q11": [
        "tri‑state",
        "disable",
        "direction"
    ],
    "q12": [
        "redundancy",
        "eco",
        "spare"
    ],
    "q13": [
        "compare",
        "netlist",
        "order"
    ],
    "q14": [
        "aliasing",
        "x‑handling",
        "compressed"
    ],
    "q15": [
        "stuck‑at",
        "bridge",
        "open"
    ]
}

    @pytest.mark.parametrize("qid, kw_list", KEYWORDS.items())
    def test_keywords(qid, kw_list):
        ans = answers.STUDENT_ANS.get(qid, "").lower()
        assert ans, f"Answer for {qid} is empty"
        for kw in kw_list:
            assert kw.lower() in ans, f"Missing keyword '{kw}' in {qid}"
