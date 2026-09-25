When i created the breakfast graph problem, I did not need to change the planner. The BFS algorithm
only depends on the functions available_action nd apply_action., and the start and goal states. This separation makes the program modular
because the search algorithm can be used for different problems. 

The no-solution test showed me that BFS must exhaust the frontier and return None when the goal cannot be reached instead of assuming every problem has a valid solution.