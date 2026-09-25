# tests/test_planner.py
from src.restoration_graph import ACTIONS, START, GOAL, available_actions, apply_action
from src.planner import bfs_search

def is_valid_plan(plan, actions=ACTIONS):
    """A plan is valid if every action's prerequisites are satisfied by
    the actions before it, and every required action appears exactly once."""
    completed = set()
    for action in plan:
        if action in completed:
            return False          # duplicate action
        if not actions[action]["requires"].issubset(completed):
            return False          # prerequisite violated
        completed.add(action)
    return completed == set(actions.keys())


def test_finds_a_valid_plan():
    plan = bfs_search(START, GOAL, available_actions, apply_action)
    assert plan is not None
    assert is_valid_plan(plan)


def test_trivial_already_done():
    # start == goal: the plan should be empty, not None, not a crash
    plan = bfs_search(GOAL, GOAL, available_actions, apply_action)
    assert plan == []


def test_plan_has_no_duplicate_actions():
    plan = bfs_search(START, GOAL, available_actions, apply_action)
    assert len(plan) == len(set(plan))


def test_no_solution_returns_none():

    impossible_goal = GOAL | {"fake_action"}

    plan = bfs_search(
        START,
        impossible_goal,
        available_actions,
        apply_action
    )

    assert plan is None



def test_large_action_set_terminates():

    actions = {}

    for i in range(15):
        actions[str(i)] = {
            "requires": set() if i == 0 else {str(i - 1)}
        }

    def get_actions(state):
        return [
            action for action in actions
            if action not in state
               and actions[action]["requires"].issubset(state)
        ]

    def do_action(state, action):
        return state | {action}

    start = frozenset()
    goal = frozenset(actions)

    plan = bfs_search(start, goal, get_actions, do_action)

    assert plan is not None