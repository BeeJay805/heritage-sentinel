# Overview:
In this project I am making a program to plan repairs for a historical object. Lab 1 used BFS to find an order for the actions. For this lab I used a CSP to give each action a time slot and check the funding limit.

# Current Status:
- `src/planner.py` still has the BFS search. `src/breakfast_graph.py` is another problem it can run on.
- `src/csp.py` has the backtracking solver. `src/restoration_csp.py` has the rules for the repair actions.
- The rules make sure each action has its own slot, required actions come first, and the first two slots stay under the tranche cap.
- `config.json` has the seed and tranche cap. `src/main_csp.py` prints the settings with the plan.
- `tests/test_planner.py` and `tests/test_csp.py` check the planners and the new funding rule.

Run `python src/main_csp.py` from the project folder to see a plan.
Run `python -m pytest` to run the tests.

