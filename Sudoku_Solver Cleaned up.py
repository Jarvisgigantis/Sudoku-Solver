

def Convert_Sudocolumn(Sudoku:list[list[int]]) -> list[list[int]]:
    """
    This function takes in a Sudoku and outputs a new list of 9 lists of the columns of each row
    """
    Columns = []
    for col_idx in range(len(Sudoku)):
        Column = []
        for row in Sudoku:
            Column.append(row[col_idx])
        Columns.append(Column)
    return Columns


def Convert_Sudobox(Sudoku:list[list[int]]) -> list[list[int]]:
    """
    This function should be input a full sudoku and output a list of all the 9 3x3 grids or boxes.
    """
    Boxes = []
    for box_row in range(3):         # box_row: 0, 1, 2 (top → bottom)
        for box_col in range(3):     # box_col: 0, 1, 2 (left → right)
            box = []
            for r in range(3):       # rows inside the box
                for c in range(3):   # cols inside the box
                    row_idx = box_row * 3 + r
                    col_idx = box_col * 3 + c
                    box.append(Sudoku[row_idx][col_idx])
            Boxes.append(box)
    return Boxes


def check_distinct_list(Segment:list[int]) -> bool:
    """
    This function is supposed to take a list and outputs true if no numbers repeat or is no higher than 9. Otherwise output False. 0 is ignored.
    """
    used = []
    for i in Segment:
        if i == 0:
            continue
        if i > 9:
            return False
        if i in used:
            return False
        used.append(i)
    return True


def check_no_empty(Sudoku:list[list[int]]) -> bool:
    """
    Checks if the sudoku has any empty fields.
    """
    for row in Sudoku:
        for col in row:
            if col == 0:
                return False
    return True

def get_candidates(Sudoku:list[list[int]], row_idx: int, col_idx: int) -> set:
    """
    Get possible candidates for a single cell based on its row, column, and box.
    """
    if Sudoku[row_idx][col_idx] != 0:  # If the cell is already filled, return an empty set
        return set()

    full_set = set(range(1, 10))
    columns = Convert_Sudocolumn(Sudoku)
    boxes = Convert_Sudobox(Sudoku)
    box_index = (row_idx // 3) * 3 + (col_idx // 3)

    # Subtract numbers already present in the row, column, and box
    return full_set.difference(Sudoku[row_idx], columns[col_idx], boxes[box_index])



def solve(row,col,board):
    if row == len(board):
        return check_no_empty(board)
    if col == len(board[row]):
        col = 0
        return solve(row+1,col,board)
    
    if board[row][col] == 0:
        for value in get_candidates(board,row,col):
            board[row][col] = value
            columns = Convert_Sudocolumn(board)
            boxes = Convert_Sudobox(board)
            box_index = (row // 3) * 3 + (col // 3)
            if check_distinct_list(board[row]) == True and check_distinct_list(columns[col]) == True and check_distinct_list(boxes[box_index]) == True:
                if solve(row,col+1,board):
                    return True
            board[row][col] = 0
        return False
    else:
        return solve(row,col+1,board)
    
def finalsolve(Sudoku:list[list[int]]) -> list[list[int]]:
    if solve(0,0,Sudoku) == True:
        return Sudoku
    else:
        return "Cannot be solved."


Collected_sudoku = []
ikke_færdig = 0
while ikke_færdig < 9:
    user_sudoku1 = input(f"Indtast række {ikke_færdig + 1} af din Sudoku (9 tal, brug 0 for tomme felter): ")
    try:
        row = list(map(int, user_sudoku1.strip()))
        if len(row) != 9:
            print("Hver række skal indeholde præcis 9 tal. Prøv igen.")
            continue
        Collected_sudoku.append(row)
        ikke_færdig += 1
    except ValueError:
        print("Indtast kun tal. Prøv igen.")

print("Din indtastede Sudoku:")
for row in Collected_sudoku:
    print(row)

print("Det var så lidt:")
for row in (finalsolve(Collected_sudoku)):
    print(row)

input("Tryk enter for at lukke")
