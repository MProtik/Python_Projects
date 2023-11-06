import time
import os

def display_board2(board):
    os.system("clear")  # Remember, this only works in jupyter!
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def player_input():
    choice = "l"
    while choice.lower() not in ["x", "o"]:
        choice = input("player1....Choose your marker between marker --> X or O\n->")
    if choice.lower() == "x":
        return ("X", "O")
    else:
        return ("O", "X")
    
def place_marker(board, marker, position):
    board[int(position)] = marker
    return board

def match(nums):
    win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in win:
        code = i
        code.append("x")
        for num in nums:
            if num == code[0]:
                code.pop(0)
                if (code[0] == "x") == True:
                    return True
                else:
                    continue
                
    return False

def win_check(board, mark):
    marks = []
    for i in range(1, 10):
        if board[i] == mark:
            marks.append(i)
    return match(marks)

def match1(nums):
    win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in win:
        code = i
        code.append("x")
        for num in nums:
            if num == code[0]:
                code.pop(0)
                if (code[0] == "x") == True:
                    return True
                else:
                    continue
                
    return False

def choose_first_player():
    if randint(0, 1) == 0:
        return "Player1"
    else:
        return "Player2"
    
def is_empty(board, position):
    if board[position] == " ":
        return True
    else:
        return False
    
def full_board_check(board):
    if 0 in board:
        return False
    else:
        return True
    
def player_choice(board):
    space = False
    while not space:
        choose = int(input("Choose your position-->"))
        if choose > 0 and choose < 10: 
            space = is_empty(board, choose) 
        else:
            continue
    return choose

def replay():
    desicion = "0"
    while desicion.lower() not in ["y", "n"]:
        desicion = input("Do you want to play again..??(y/n)")
        if desicion.lower() == "y":
            return True
        elif desicion.lower() == "n":
            return False

def spark(Congratulations):    
    s = Congratulations
    for i in range(5):
        os.system("clear")
        print(s,end="")
        time.sleep(1)
    print("..!!")
        
print('Welcome to Tic Tac Toe!\nBest of luck\nNOW BEGIN..!!')
dic = {"y": True, "n": False, "Y": True, "N": False}
while True:    
    board = ['#', " ", " ", " ", " ", " ", " ", " ", " ", " "]
    player1, player2 = player_input()
    print(player1, player2)
    play_game = input("Are you ready to play-->(y/n)")
    for i in range(1, 10):
        os.system("clear")
        if play_game == False:
            break
        display_board2(board)
        if i%2 != 0:
            print("player1's turn")
            choice = player_choice(board)
            board = place_marker(board, player1, choice)
            if win_check(board, player1) == True:
                os.system("clear")
                spark("congratulations..player1 win")
                print("congratulations..player1 win")
                display_board2(board)
                break
            
        else:
            print("player2's turn")
            choice = player_choice(board)
            board = place_marker(board, player2, choice)
            if win_check(board, player2) == True:
                os.system("clear")
                spark("congratulations..player2 win")
                print("congratulations..player2 win")
                display_board2(board)
                break
    display_board2(board)
    print("Game Ended")
    
    if not replay():
        break