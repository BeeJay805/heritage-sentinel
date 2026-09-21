ACTIONS = {
    "toast_bread": {"requires": set()},
    "add_butter": {"requires": {"toast_bread"}},
    "eat_toast": {"requires": {"add_butter"}},
}

START = frozenset()
GOAL = frozenset(ACTIONS.keys())

def available_actions(state):
    return [
        action for action, info in ACTIONS.items()
        if action not in state and info["requires"].issubset(state)
    ]

def apply_action(state, action):
    return state | {action}