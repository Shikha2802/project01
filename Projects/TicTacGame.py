def display_board(board):
    #row1=board[0:3]
    print(' | '.join(board[0:3]))
    print('--|---|---')
    print(' | '.join(board[3:6]))
    print('--|---|---')
    print(' | '.join(board[6::]))


def player_input():

#    player1  = input("Player 1: Please select you want to play as 'X' or 'O' : ")
    position = int(input("Please select the position(0-9) to place your move: "))

    while position not in [ 0,1,2,3,4,5,6,7,8,9]:
        print("Oops..!! wrong input..Try again.")
        position = int(input("Please select the position(0-9) to place your move: "))

    return position

def place_marker(test_board,marker,position):
    test_board[position] =marker

    return test_board


def win_check(test_board, marker):
    count =0
    win_combo = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 8)]
    for i in win_combo:
        #print(i)
        for place in i:

            if test_board[place] == marker:
                count = count+1
                #print(marker)
                if count == 3:
                    return True
                continue
        count = 0
    return False


def space_check(board, postion):
    pass

def full_board (board):

    for i in range(len(board)):

        if board[i] == " " :
            return True

    return False


def replay_game():
    replay = input("Want to play again? Press Y/N : ")

    return replay

replay = True

while replay :
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)
    on_game = full_board(board)
    player =['X', 'O']
    player1  = input("Player 1: Please select you want to play as 'X' or 'O' : ")
    while on_game :
        for marker in player:

            board_position = player_input()
            updated_board = place_marker(board,marker,board_position)
            display_board(updated_board)
            win = win_check(updated_board,marker)
            if win:

                print(f'{marker} won..!!!')
                break
            else:
                on_game = full_board(updated_board)
                if on_game :
                    continue
                else:
                    break

    on_game = full_board(updated_board)

    if not win:
        print("No winner...!")


    play_again = replay_game()



#res = display_board(board)