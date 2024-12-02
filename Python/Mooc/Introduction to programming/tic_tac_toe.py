# Write your solution here
def play_turn(board:list, x:int, y:int, piece:str):
    if x < 3 and y < 3 and x > -1 and y > -1:
        place = board[y][x]
        if place != "X" and place != "O":
            board[y][x] = piece
            return True
    return False
if __name__ == "__main__":
    game_board = 
    print(play_turn([['X', '', 'X'], ['', 'X', 'O'], ['', 'X', '']], 2, -1, "X"))
    print(game_board)