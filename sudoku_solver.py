def solveBoard(board: list[list[int]]) -> bool:
    """solve the Sudoku board using backtracking."""
    empty_cell = findEmpty(board)
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    for i in range(1, 10):
        if validBoard(board, i, (row, col)):
            board[row][col] = i

            if solveBoard(board):
                return True

            board[row][col] = 0
    return False

def printBoard(board: list[list[int]])-> None:
    """Print the Sudoku board."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def validBoard(board: list[list[int]], num: int, pos: tuple[int, int]) -> bool:
    """Check if the board is valid."""
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    x_box = pos[1] // 3
    y_box = pos[0] // 3

    for i in range(y_box * 3, y_box * 3 + 3):
        for j in range(x_box * 3, x_box * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def findEmpty(board: list[list[int]]) -> tuple[int, int]:
    """Find the first empty cell in the board."""
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None

def main():
    board_1 = [
        [7, 5, 9, 8, 0, 6, 1, 2, 4],
        [3, 2, 8, 1, 4, 7, 6, 9, 5],
        [6, 4, 1, 5, 9, 2, 7, 3, 8],
        [1, 8, 4, 9, 7, 5, 3, 6, 2],
        [5, 9, 7, 2, 0, 3, 8, 4, 1],
        [2, 6, 0, 4, 8, 1, 5, 7, 9],
        [8, 7, 2, 3, 5, 4, 9, 1, 6],
        [9, 1, 6, 7, 2, 8, 4, 5, 3],
        [4, 0, 5, 6, 1, 9, 2, 8, 0]
    ]
    solution_board_1 = [
        [7, 5, 9, 8, 3, 6, 1, 2, 4],
        [3, 2, 8, 1, 4, 7, 6, 9, 5],
        [6, 4, 1, 5, 9, 2, 7, 3, 8],
        [1, 8, 4, 9, 7, 5, 3, 6, 2],
        [5, 9, 7, 2, 6, 3, 8, 4, 1],
        [2, 6, 3, 4, 8, 1, 5, 7, 9],
        [8, 7, 2, 3, 5, 4, 9, 1, 6],
        [9, 1, 6, 7, 2, 8, 4, 5, 3],
        [4, 3, 5, 6, 1, 9, 2, 8, 7]
    ]
    solveBoard(board_1)
    assert board_1 == solution_board_1 

    board_2 = [
        [7, 5, 9, 8, 0, 6, 1, 2, 4],
        [3, 2, 8, 1, 4, 7, 6, 9, 5],
        [6, 4, 1, 5, 9, 2, 7, 0, 8],
        [1, 8, 4, 9, 7, 5, 3, 6, 2],
        [5, 9, 7, 2, 0, 3, 8, 0, 1],
        [0, 6, 0, 4, 8, 1, 5, 7, 9],
        [8, 7, 2, 3, 5, 4, 9, 1, 6],
        [9, 1, 6, 7, 2, 8, 4, 5, 3],
        [4, 0, 5, 6, 1, 9, 2, 8, 0]
    ]
    solution_board_2 = [
        [7, 5, 9, 8, 3, 6, 1, 2, 4],
        [3, 2, 8, 1, 4, 7, 6, 9, 5],
        [6, 4, 1, 5, 9, 2, 7, 3, 8],
        [1, 8, 4, 9, 7, 5, 3, 6, 2],
        [5, 9, 7, 2, 6, 3, 8, 4, 1],
        [2, 6, 3, 4, 8, 1, 5, 7, 9],
        [8, 7, 2, 3, 5, 4, 9, 1, 6],
        [9, 1, 6, 7, 2, 8, 4, 5, 3],
        [4, 3, 5, 6, 1, 9, 2, 8, 7]
    ]
    solveBoard(board_2)
    assert board_2 == solution_board_2 

    board_3 = [
        [0, 0, 0, 8, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 9, 0, 0, 3, 6, 0],
        [5, 0, 7, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 4, 9, 0, 0],
        [0, 0, 0, 7, 2, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 8, 0]
    ]
    solution_board_3 = [
        [7, 5, 9, 8, 3, 6, 1, 2, 4],
        [3, 2, 8, 1, 4, 7, 6, 9, 5],
        [6, 4, 1, 5, 9, 2, 7, 3, 8],
        [1, 8, 4, 9, 7, 5, 3, 6, 2],
        [5, 9, 7, 2, 6, 3, 8, 4, 1],
        [2, 6, 3, 4, 8, 1, 5, 7, 9],
        [8, 7, 2, 3, 5, 4, 9, 1, 6],
        [9, 1, 6, 7, 2, 8, 4, 5, 3],
        [4, 3, 5, 6, 1, 9, 2, 8, 7]
    ]
    solveBoard(board_3)
    assert board_3 == solution_board_3

    print("All test cases pass") 

if __name__ == "__main__":
    main()