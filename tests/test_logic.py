import json, random
import pytest
from logic import forward_chain, explain
from report_rules import CLAUSES
import validate as validator
from validate import validate, to_facts

def load(path="data/reports.jsonl"):
    with open(path) as f:
        return {r["id"]: r for r in map(json.loads, f)}

REPORTS = load()

def test_chain_derives_transitively():
    known, _ = forward_chain({"a"}, [(frozenset({"a"}), "b"), (frozenset({"b"}), "c")])
    assert known == {"a", "b", "c"}

def test_cycle_terminates():
    known, _ = forward_chain({"a"}, [
        (frozenset({"a"}), "b"),
        (frozenset({"b"}), "a"),
    ])
    assert known == {"a", "b"}

def test_clause_order_irrelevant():
    facts = to_facts(REPORTS["r9"])
    expected, _ = forward_chain(facts, CLAUSES)
    for seed in range(20):
        shuffled = CLAUSES[:]
        random.Random(seed).shuffle(shuffled)
        got, _ = forward_chain(facts, shuffled)
        assert got == expected

@pytest.mark.parametrize("rid", ["r1", "r3", "r5", "r7"])
def test_valid_reports_accepted(rid):
    ok, reasons, _ = validate(REPORTS[rid])
    assert ok and reasons == []

@pytest.mark.parametrize("rid,reason", [
    ("r2", "invalid:structural_risk_marked_minor"),
    ("r4", "invalid:rot_on_inorganic"),
    ("r6", "invalid:corrosion_on_organic"),
    ("r8", "invalid:none_but_damaged"),
])
def test_each_rule_fires_alone(rid, reason):
    ok, reasons, _ = validate(REPORTS[rid])
    assert not ok and reasons == [reason]

def test_multiple_violations_all_reported():
    ok, reasons, _ = validate(REPORTS["r9"])
    assert not ok
    assert reasons == [
        "invalid:rot_on_inorganic",
        "invalid:structural_risk_marked_minor",
    ]

@pytest.mark.parametrize("rid,frag", [("r10", "missing field"), ("r11", "unknown material")])
def test_schema_errors_are_not_logic_errors(rid, frag):
    ok, reasons, proofs = validate(REPORTS[rid])
    assert not ok and reasons[0].startswith("schema:") and frag in reasons[0] and proofs == {}

def test_proofs_bottom_out_in_given_facts():
    _, reasons, proofs = validate(REPORTS["r2"])
    leaves = [line for line in proofs[reasons[0]] if "because" not in line]
    assert leaves
    assert all("(given)" in line for line in leaves)

def test_deleting_a_rule_is_caught():
    original = validator.CLAUSES
    try:
        validator.CLAUSES = [
            clause for clause in original
            if clause[1] != "invalid:rot_on_inorganic"
        ]
        ok, reasons, _ = validate(REPORTS["r4"])
        assert ok and reasons == []
    finally:
        validator.CLAUSES = original
    ok, reasons, _ = validate(REPORTS["r4"])
    assert not ok and reasons == ["invalid:rot_on_inorganic"]


@pytest.mark.parametrize("rid,near_miss,reason", [
    ("r12", {"id": "near12", "material": "textile", "damage": ["fading"], "severity": "minor"},
     "invalid:crack_on_textile"),
    ("r13", {"id": "near13", "material": "ceramic", "damage": ["crack"], "severity": "minor"},
     "invalid:corrosion_on_ceramic"),
])
def test_new_rules_fire_but_near_misses_do_not(rid, near_miss, reason):
    ok, reasons, _ = validate(REPORTS[rid])
    assert not ok and reasons == [reason]
    ok, reasons, _ = validate(near_miss)
    assert ok and reasons == []
