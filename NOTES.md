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


Lab P5:

I guessed a-odd1 would be quarantined and the other four would be rejected, since my Lab 4 rules blocked crack on textile and corrosion on ceramic. The pipeline quarantined a-odd2 and a-odd3 instead. The pipeline was right because 6 of the reference reports are textile with a crack, so I removed those two rules.
The model treats crack and loose_base as independent, but if an object falls it could crack and come loose at the same time. It also doesn't know that crack plus loose_base means the report has to be major.
The model has 4 + 25 + 6 = 35 free parameters, which matches. 400 reports is enough, but with 40 some materials would only have 3 or 4 reports, so most of the numbers would come from smoothing. When I tried it with 40 the held-out quarantine rate went up to about 8%.
If a new survey team sends a combination that was never in the reference data, like corrosion on a stone statue with metal pins, the probability is 0 and log(0) gives an error. Then the whole batch crashes instead of just quarantining that one report.
The gap was small because the model only has 35 parameters for 400 reports, and the new batches came from the same generator as the reference data. It would be bigger with less data, a more complicated model, or data from different conditions. This is overfitting.
A rare but true report gets held and checked by a person who might think it's a typo, so it is slower but not thrown away. If losing a rare find is worse, I would lower the threshold, but then more typos would get accepted. a-odd3 scores -9.24, which is lower than every reference report, so the threshold would have to be really low to let it through.
Batch B can't be caught one report at a time because every report looks normal by itself. The problem is only in the totals, 40% textile instead of 10%, so only the chi-square batch test can see it.
For Part E I added a severity_mix check using chi-square with a critical value of 13.816. Changing every minor to major in a clean batch made it fire, and clean batches stayed quiet.