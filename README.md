Link to the introductory course: https://vscodeedu.com/courses/intro-to-python

This is my biggest coding project yet where i used the method of recursive backtracking to bruteforce my way through the problem.
After struggling and being stuck for a while on my own, i saught the internet for help where i realized i was doing optimimisation instead of solving the actual problem. 
Here i gained the big insight that my mistake was that i was thinking about the problem like a human. I needed to think like a machine. 
Since machines compute way faster than humans bruteforcing becomes a non-trivial strategy. 
I optimized a little by eliminating the known numbers it provably was not (acording to the sudoku rules), and trying every combination of the possible correct numbers while checking for correctness along every step. If a number violates the rules of the sudoku, we backtrack to the last itteration and try the next number in the set of possible numbers for that specific cell.
