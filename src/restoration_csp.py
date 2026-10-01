# restoration_csp.py — problem definition only.
from restoration_graph import ACTIONS


VARIABLES = list(ACTIONS.keys())
DOMAINS = {a: list(range(1, len(VARIABLES) + 1)) for a in VARIABLES}


def build_constraints(actions=ACTIONS, tranche_cap=4):
    constraints = []

    # Every action gets its own slot.
    for i, a in enumerate(VARIABLES):
        for b in VARIABLES[i + 1:]:
            constraints.append(((a, b), lambda x, y: x != y))

    # Required actions must come first.
    for action in VARIABLES:
        for required in actions[action]["requires"]:
            constraints.append(((required, action), lambda x, y: x < y))

    # The first two slots share one funding tranche.
    def within_tranche(*slots):
        return sum(actions[a]["cost"] for a, slot in zip(VARIABLES, slots)
                   if slot <= 2) <= tranche_cap

    constraints.append((tuple(VARIABLES), within_tranche))
    return constraints
