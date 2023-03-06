import random


def get_player_name():  # get player name
    name = input("Write your name: ")
    return name


player_name = get_player_name()

print("Hello new player " + player_name)  # greeting


# player choise number 1 - paper 2 - scissors 3 - rock

def get_playre_item():
    plyer_item_chois = input(player_name + " your item: ")
    return plyer_item_chois


playerItem = str(get_playre_item())


def player_choise(player_item, player_name):
    if int(player_item) == 1:
        print(player_name + " choise paper")
    elif int(player_item) == 2:
        print(player_name + " choise scissors")
    elif int(player_item) == 3:
        print(player_name + " choise rock")
    else:
        print("You chose wrong number. Try again!")


def random_number(rangeStart, rangeEnd):
    number = random.randint(rangeStart, rangeEnd)  # random math
    return number


computer_number = (random_number(1, 3))

player_choise(playerItem, player_name)
player_choise(computer_number, "Computer")


def game(player_num, computer_num):
    if int(player_num) == int(computer_num):
        print("We have REMIS")
    elif int(player_num) == 2 and int(computer_num) == 1 or int(player_num) == 1 and int(
            computer_num) == 2:  # scissor player win
        if int(player_num) == 2 and int(computer_num) == 1:
            print(player_name + " win")
        elif int(player_num) == 1 and int(computer_num) == 2:
            print("Computer win")
    elif int(player_num) == 3 and int(computer_num) == 1 or int(player_num) == 1 and int(
            computer_num) == 3:  # paper player win
        if int(player_num) == 1 and int(computer_num) == 3:
            print(player_name + " win")
        elif int(player_num) == 3 and int(computer_num) == 1:
            print("Computer win")
    elif int(player_num) == 3 and int(computer_num) == 2 or int(player_num) == 2 and int(
            computer_num) == 3:  # rock player win
        if int(player_num) == 3 and int(computer_num) == 2:
            print(player_name + " win")
        elif int(player_num) == 2 and int(computer_num) == 3:
            print("Computer win")
    else:
        print("End game")
    return


game(playerItem, computer_number)
