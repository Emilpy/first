import random

borad = ["[ ]", "[ ]", "[ ]",
         "[ ]", "[ ]", "[ ]",
         "[ ]", "[ ]", "[ ]", ]  # lists
board1 = ("[x]", "[ ]", "[ ]",
          "[ ]", "[ ]", "[ ]",
          "[ ]", "[ ]", "[ ]",)  # touples

print(borad[1])
print(board1)

board1 = ["[x]", "[ ]", "[ ]",
          "[ ]", "[ ]", "[ ]",
          "[ ]", "[x]", "[ ]", ]
print(board1)

# borad[0]= "-" # Traceback (most recent call last):
#   File "F:\Pycharm\pythonProjects\first\tiotoctoagame.py", line 7, in <module>
#     borad[0]= "-"
# TypeError: 'tuple' object does not support item assignment

print(type(borad))

print(borad[0])
borad[0] = "[o]"
print(borad[0])
print("--------------")


# borad[0] = "[O]"
# print(borad[0])

# losowanie liczby przez komutere
def comuter_random_number():
    random_number = random.randint(1, 9)
    return random_number


random_num = comuter_random_number()
print(random_num)

pattern_x = "[x]"
pattern_o = "[o]"

print("-----------------")

# board1[random_num] = pattern_x
board_new = board1
board2 = board_new
print(board2)
random_num = comuter_random_number()
# board2[random_num] = pattern_x
board_new = board2
board3 = board_new
print(board3)
print("-----------------")


def update_board(pattern, number, board):
    old_board = board
    # old_board[number] = pattern
    new_board = old_board
    return new_board


# new_ = update_board(pattern_o, random_num, board1)
# board1 = new_
# board1 = board1
# new_2 = update_board(pattern_o, random_num, board1)
# board1 = new_2
# board1 = board1

print(board1)
print(board1)
print("=========================")

board4 = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]

print(type(board4))
print("Start board")
print(board4)


# winner = False


def get_user_number():
    number = (input("Enter number: "))
    return number


board4 = ["0", "-", "0",
          "-", "-", "-",
          "-", "-", "-"]

user_number = get_user_number()
board4[int(user_number)] = "o"

print(board4)


def winner_pattern():
    winner = False
    while not winner:
        print("winner_pattern")
        print(board4)
        if (board4[0] == board4[1] == board4[2]) and (board4[0] != "-"):
            print("winner 012")
            winner = True
            return winner
        elif (board4[3] == board4[4] == board4[5]) and (board4[3] != "-"):
            print("winner 345")
            winner = True
        elif (board4[6] == board4[7] == board4[8]) and (board4[6] != "-"):
            print("winner 678")
            winner = True
        elif (board4[0] == board4[3] == board4[6]) and (board4[0] != "-"):
            print("winner 036")
            winner = True
        elif (board4[1] == board4[4] == board4[7]) and (board4[1] != "-"):
            print("winner 147")
            winner = True
        elif (board4[2] == board4[5] == board4[8]) and (board4[2] != "-"):
            print("winner 258")
            winner = True
        elif (board4[0] == board4[4] == board4[8]) and (board4[0] != "-"):
            print("winner 048")
            winner = True
        else:
            return


winner_pattern()

# 3 x 3
borad_x = 3
borad_y = 3

# for n in range(3):
#     print(n)


# for n in range(3):
#     board4[n] = "x"

print(len(board4))
