When i created the breakfast graph problem, I did not need to change the planner. The BFS algorithm
only depends on the functions available_action nd apply_action., and the start and goal states. This separation makes the program modular
because the search algorithm can be used for different problems.

Lab P3:
When I changed VARIABLES to use a set, I got different valid plans when I ran the program in separate processes. 
Python can put strings in a different set order each time it starts. The seed only controls the solver's shuffle, so it cannot control that change. I changed VARIABLES back to a list to keep the order consistent.

My old plan validator checked that every action was included and that prerequisites came first. Those checks were correct for the old rules, but they did not check the new funding limit.
This shows that tests and validators need to change when the requirements change, even if they passed before.

Lab P4:

The loop stops because `known` only grows, and there are only so many rule conclusions to add.
`explain` sorts premises so the proof prints in the same order each time.
My guesses matched the results: r1, r3, r5, and r7 are valid. r2, r4, r6, r8, and r9 break rules. r10 and r11 have missing or unknown fields.
Changing rule order can change which proof gets saved, so the order should stay fixed for audit logs.My two new rules reject a crack on textile and corrosion on ceramic.
A Horn rule cannot tell that damage is missing. We could add a `no_damage` fact, but then we have to assume the report's damage list is complete.
