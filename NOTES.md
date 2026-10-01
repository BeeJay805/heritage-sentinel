When i created the breakfast graph problem, I did not need to change the planner. The BFS algorithm
only depends on the functions available_action nd apply_action., and the start and goal states. This separation makes the program modular
because the search algorithm can be used for different problems.

Lab P3:
When I changed VARIABLES to use a set, I got different valid plans when I ran the program in separate processes. 
Python can put strings in a different set order each time it starts. The seed only controls the solver's shuffle, so it cannot control that change. I changed VARIABLES back to a list to keep the order consistent.

My old plan validator checked that every action was included and that prerequisites came first. Those checks were correct for the old rules, but they did not check the new funding limit.
This shows that tests and validators need to change when the requirements change, even if they passed before.