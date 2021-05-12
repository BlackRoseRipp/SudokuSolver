import solver
import puzzle

print("Welcome to Sudoku Solver!")
user = input("Do you have your own puzzle?(Y/N)")

puzzleBoard = []
if user == "Y":
    userBoard = input("Give your puzzle as an array of rows that have an array of columns each: ")
    puzzleBoard = userBoard
else:
    puzzleBoard = puzzle.getPuzzle()

puzzle.printPuzzle(puzzleBoard)

giveUp = input("Do you wish to give up? (Y/N)")
while(giveUp != "Y"):
    giveUp = input("Do you wish to give up yet? (Y/N)")

print("-------------------------------------------------")
if (solver.SudukoSolver(puzzleBoard, 0, 0)):
    print("Here is your completed puzzle!")
    puzzle.printPuzzle(puzzleBoard)
else:
    print("Solution does not exist :(")
