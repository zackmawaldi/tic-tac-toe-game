import random

greetings_msg = "Welcome to Tic Tac Toe! You are X."
print(greetings_msg)

choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# each int corresponds to position on board
# [1] [2] [3]
# [4] [5] [6]
# [7] [8] [9]

a, b, c, d, e, f, g, h, i = "-", "-", "-", "-", "-", "-", "-", "-", "-"  # variable a corresponds to position 1, etc


def assign(i_b_choice, x_o):  # function that assigns bot or user input to board location
    global a, b, c, d, e, f, g, h, i
    if i_b_choice == 1:
        a = "{}".format(x_o)
    elif i_b_choice == 2:
        b = "{}".format(x_o)
    elif i_b_choice == 3:
        c = "{}".format(x_o)
    elif i_b_choice == 4:
        d = "{}".format(x_o)
    elif i_b_choice == 5:
        e = "{}".format(x_o)
    elif i_b_choice == 6:
        f = "{}".format(x_o)
    elif i_b_choice == 7:
        g = "{}".format(x_o)
    elif i_b_choice == 8:
        h = "{}".format(x_o)
    elif i_b_choice == 9:
        i = "{}".format(x_o)


def win_check(x_o):  # function checks if whether X or O won (has 3 X or O in a row)
    global a, b, c, d, e, f, g, h, i
    if a == b == c == "{}".format(x_o):
        print("{} wins!".format(x_o))
        return True
    elif d == e == f == "{}".format(x_o):
        print("{} wins!".format(x_o))
        return True
    elif g == h == i == "{}".format(x_o):
        print("{} wins!".format(x_o))
        return True
    elif a == d == g == "{}".format(x_o):
        print("{} wins!".format(x_o))
        return True
    elif b == e == h == "{}".format(x_o):
        print("{} wins!".format(x_o))
        return True
    elif c == f == i == "{}".format(x_o):
        print("{} wins!".format(x_o))
        return True
    elif a == e == i == "{}".format(x_o):
        print("{} wins!".format(x_o))
        return True
    elif c == e == g == "{}".format(x_o):
        print("{} wins!".format(x_o))
        return True
    else:
        return False


def print_board():  # print current board
    global a, b, c, d, e, f, g, h, i
    print("[" + a + "]" + "[" + b + "]" + "[" + c + "]\n"
          "[" + d + "]" + "[" + e + "]" + "[" + f + "]\n"
          "[" + g + "]" + "[" + h + "]" + "[" + i + "]")


def ask_input():  # prints layout of choices w/ inputs numbers
    global i_choice, choices
    if len(choices) == 0:
        pass
    else:
        i_choice = int(input("Type a position.\n"
                             "[1][2][3]\n"
                             "[4][5][6]\n"
                             "[7][8][9]\n"
                             "---------"))
        if i_choice not in choices:
            print("Not an available choice, try again.")
            ask_input()


def bot_input():  # changes list of available choices for bot, and assigns a bot input from new list
    global b_choice, choices, i_choice
    if i_choice in choices:  # removes user taken spots from bot's choices
        choices.remove(i_choice)
    if len(choices) == 0:
        pass
    else:
        b_choice = random.choice(choices)  # assigns the bot's random choice to b_choice
        choices.remove(b_choice)  # removes bot's choice bot's future choices


global i_choice, b_choice

while True:
    print_board()
    ask_input()
    assign(i_choice, "X")
    bot_input()
    assign(b_choice, "O")
    if win_check("X"):
        print_board()
        break
    if win_check("O"):
        print_board()
        break
    if len(choices) == 0:
        print("Game is a tie!")
        print_board()
        break

# The loop above prints the board, asks for an input, assigns input to position on board, assigns a bot an input,
# assigns the bot's input to a position on the board, then checks if X or O has won or if there's a tie, if not,
# repeat until the last check part checks true.
