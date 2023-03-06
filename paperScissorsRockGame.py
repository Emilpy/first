import random


def getPlayerName():
    name = input("Write your name: ")
    return name


playerName = getPlayerName()

print("Hello new player " + playerName)  # przywitanie


# player choise number 1 - paper 2 - scissors 3 - rock

def getPlayreItem():
    plyerItemChois = input(playerName + " your item: ")
    return plyerItemChois


playerItem = str(getPlayreItem())


def playerChoise(playerItem, playerName):
    if int(playerItem) == 1:
        print(playerName + " choise paper")
    elif int(playerItem) == 2:
        print(playerName + " choise scissors")
    elif int(playerItem) == 3:
        print(playerName + " choise rock")
    else:
        print("You chose wrong number. Try again!")


def randomNumber(rangeStart, rangeEnd):
    number = random.randint(rangeStart, rangeEnd)  # random math
    return number


computerNumber = (randomNumber(1, 3))


playerChoise(playerItem, playerName)
playerChoise(computerNumber, "Computer")


def game(player_num, computer_num):
    if int(player_num) == int(computer_num):
        print("We have REMIS")
    elif int(player_num) == 2 and int(computer_num) == 1 or int(player_num) == 1 and int(computer_num) == 2:  # scissor player win
        if int(player_num) == 2 and int(computer_num) == 1:
            print(playerName + " win")
        elif int(player_num) == 1 and int(computer_num) == 2:
            print("Computer win")
    elif int(player_num) == 3 and int(computer_num) == 1 or int(player_num) == 1 and int(computer_num) == 3:  # paper player win
        if int(player_num) == 1 and int(computer_num) == 3:
            print(playerName + " win")
        elif int(player_num) == 3 and int(computer_num) == 1:
            print("Computer win")
    elif int(player_num) == 3 and int(computer_num) == 2 or int(player_num) == 2 and int(computer_num) == 3:  # rock player win
        if int(player_num) == 3 and int(computer_num) == 2:
            print(playerName + " win")
        elif int(player_num) == 2 and int(computer_num) == 3:
            print("Computer win")
    else: print("End game")
    return


game(playerItem, computerNumber)








