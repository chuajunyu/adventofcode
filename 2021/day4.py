from tools import extract_input

FILENAME = "input.txt"
input = extract_input(FILENAME)

numbers = input[0].split(',')

boards = []
board = []
for line in input[2:]:
    if line == "":
        boards.append(board)
        board = []
    else:
        row = line.split(' ')  # This can result in empty elements due to 2 blanks in a row
        row = [num for num in row if len(num) > 0]  # Removes empty elements
        board.append(row)
boards.append(board)


def check_winner(board):
    """
    Checks if the board has won
    If it is, return the sum of all the remaining numbers, Else False
    """
    to_win = len(board[0])
    winner = False

    for row in board:
        checked_row = [True for num in row if num == 'X']
        if len(checked_row) == to_win:
            winner = True
            break
    for pos in range(len(board[0])):
        if winner:  # If board has already won, no need to check columns
            break
        check_col = [True for row in board if row[pos] == "X"]
        if len(check_col) == to_win:
            winner = True
            break
    
    if winner:
        remain = [int(num) for row in board for num in row if num != 'X']
        score = sum(remain)
        return score
    else:
        return False


def play(numbers, boards):
    """
    Replaces the called numbers in the boards with 'X'
    If the board has won, its score is appended to a list
    Boards that have won is removed from the list of boards that will continue in the next round
    The list of winning scores is returned
    """
    winning_scores = []
    to_continue = []
    for called in numbers:
        for board in boards:
            for row in board:
                if called in row:
                    row[row.index(called)] = "X"
            win = check_winner(board)
            if win:
                winning_scores.append(win * int(called))
            else:
                to_continue.append(board)
        boards = to_continue
        to_continue = []
        if len(boards) == 0:
            return winning_scores
            

scores = play(numbers, boards)
print('Part 1: ', scores[0])
print('Part 2: ', scores[-1])
