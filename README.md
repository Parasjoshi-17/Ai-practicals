# AI Lab Practicals — Python Code Collection

This folder contains 22 standalone Python programs, corresponding to the 22 practical statements in the supplied document **AI LAB PRACTICALS CHITS(26-27)1.docx**.

## Run a practical
Install Python 3.10 or later. Open a terminal in this folder and run, for example:

```bash
python 09_bfs_robot_path_planning.py
```

On Windows PowerShell, you can also use:

```powershell
py .\09_bfs_robot_path_planning.py
```

All programs use only Python's standard library. No third-party package installation is required.

## Important notes
- These are runnable study/reference implementations, not a claim that your instructor requires these exact implementations or sample inputs.
- Where the practical statement is broad, a standard illustrative problem/model has been selected (for example, Tic-Tac-Toe for Minimax and Alpha-Beta, and a small grid for robot path planning).
- The supplied water-jug statement asks for exactly 1 gallon in the 5-gallon jug using 2-gallon and 5-gallon jugs. The code includes the necessary fill operations as well as the listed empty/pour operations.
- The Blocks World practicals use a compact stack representation for demonstration. Goal Stack Planning in file 21 is a simplified teaching example; check your instructor's expected operator notation and goal configuration before using it as an exact lab submission.
- Chatbot answers are sample predefined responses, not verified institutional, hospital, railway, shopping or bank information. Banking and hospital examples deliberately direct users to official channels for sensitive or time-critical matters.
- A* and BFS 8-puzzle examples use a small solvable start state so they run quickly. The 8-puzzle search space can grow very large for harder states.
- Local Beam Search is heuristic and may return a local optimum; it does not guarantee the globally optimal TSP tour.

## Practical index
01. Simple Reflex Vacuum Cleaner Agent
02. Model-Based Grid Navigation Agent
03. A* Search — 8 Puzzle
04. Alpha-Beta Pruning — Tic-Tac-Toe
05. Tower of Hanoi — State Space Search
06. Sudoku — Backtracking and Constraint Propagation
07. Local Beam Search — TSP
08. BFS — 8 Puzzle
09. BFS — Robot Path Planning
10. BFS — Blocks World
11. DFS — Water Jug
12. DFS — Maze Solving
13. DFS — Blocks World
14. DFS — Missionaries and Cannibals
15. Backtracking — 8 Queens
16. College Enquiry Chatbot
17. Hospital Enquiry Chatbot
18. Railway Enquiry Chatbot
19. Online Shopping Assistant Chatbot
20. Banking Enquiry Chatbot
21. Goal Stack Planning — Blocks World
22. Minimax — Tic-Tac-Toe
