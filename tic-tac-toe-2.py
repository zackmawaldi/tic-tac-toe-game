import random


def greeting():  # Greetings function
    global mode
    print("Welcome to Tic Tac Toe!")
    try:  # ensures user only inputs valid integers
        mode = int(input("Type in your mode:\n"
                         "1)Player v. Player\n"
                         "2)Player v. Bot\n"
                         "3)Bot v. Bot\n"
                         "Type here:"))
    except ValueError:
        print("Not an integer. Choose either 1 or 2.")


def assign(p_p2_b_choice, x_o):  # function that assigns p1, p2, or bot input to board location
    global a, b, c, d, e, f, g, h, i
    if p_p2_b_choice == 1:
        a = "{}".format(x_o)
    elif p_p2_b_choice == 2:
        b = "{}".format(x_o)
    elif p_p2_b_choice == 3:
        c = "{}".format(x_o)
    elif p_p2_b_choice == 4:
        d = "{}".format(x_o)
    elif p_p2_b_choice == 5:
        e = "{}".format(x_o)
    elif p_p2_b_choice == 6:
        f = "{}".format(x_o)
    elif p_p2_b_choice == 7:
        g = "{}".format(x_o)
    elif p_p2_b_choice == 8:
        h = "{}".format(x_o)
    elif p_p2_b_choice == 9:
        i = "{}".format(x_o)


def win_check(x_o):  # function checks if whether X or O won (has 3 X or O in a row)
    global a, b, c, d, e, f, g, h, i
    if a == b == c == "{}".format(x_o):  # if positions a, b, and c are all equal to X or O, print win & return True
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


def print_board():  # print current board with current variables on them (at start, they're all "-")
    global a, b, c, d, e, f, g, h, i
    print("[" + a + "]" + "[" + b + "]" + "[" + c + "]\n"
          "[" + d + "]" + "[" + e + "]" + "[" + f + "]\n"
          "[" + g + "]" + "[" + h + "]" + "[" + i + "]")


def ask_input(p1_p2):  # asks p1 for input when options are available
    global choices, p_choice, p2_choice
    if len(choices) == 0:  # if no more available spaces, pass
        pass
    elif p1_p2 == "p1":
        try:  # ensures user only inputs valid integers
            p_choice = int(input("Player 1, type a position.\n"
                                 "[1][2][3]\n"
                                 "[4][5][6]\n"
                                 "[7][8][9]\n"
                                 "---------"
                                 "Type here:"))
        except ValueError:
            print("Not an integer. Type 1, 2, 3, ..., 9.")
            p_choice = -1  # sets choice to an integer so the if statement "Not an available choice, try again." plays.
        if p_choice not in choices:
            print("Not an available choice, try again.")
            ask_input("p1")
        if p_choice in choices:
            choices.remove(p_choice)
    elif p1_p2 == "p2":
        try:  # ensures user only inputs valid integers
            p2_choice = int(input("Player 2, type a position.\n"
                                  "[1][2][3]\n"
                                  "[4][5][6]\n"
                                  "[7][8][9]\n"
                                  "---------"
                                  "Type here:"))
        except ValueError:
            print("Not an integer. Type 1, 2, 3, ..., 9.")
            p2_choice = -1  # sets choice to an integer so the if statement "Not an available choice, try again." plays.
        if p2_choice not in choices:
            print("Not an available choice, try again.")
            ask_input("p2")
        if p2_choice in choices:
            choices.remove(p2_choice)


def bot_input():  # changes list of available choices for bot, and assigns a bot input from new list
    global b_choice, choices, p_choice
    if len(choices) == 0:  # if no more available spaces, pass
        pass
    else:
        b_choice = random.choice(choices)  # assigns the bot's random choice to b_choice
        choices.remove(b_choice)  # removes bot's choice bot's future choices


def p_v_b_code():  # Player v. Bot mode function
    global p_choice, b_choice, mode
    print("Player is X. Bot is O.")
    while True:
        print_board()
        ask_input("p1")
        assign(p_choice, "X")
        bot_input()
        assign(b_choice, "O")
        if win_check("X"):
            print_board()
            break
        if win_check("O"):
            print_board()
            break
        if len(choices) == 0:  # if no more available spaces, call it a tie
            print("Game is a tie!")
            print_board()
            break
# The function loop above prints the board, asks for an input, assigns input to position on board, assigns a bot an
# input, assigns the bot's input to a position on the board, then checks if X or O has won or if there's a tie, if not,
# repeat until the last check part checks true.


def p_v_p_code():  # Player v. player mode function
    global p_choice, p2_choice, mode
    print("Player 1 is X. Player 2 is O.")
    while True:
        print_board()
        ask_input("p1")
        assign(p_choice, "X")
        print_board()
        ask_input("p2")
        assign(p2_choice, "O")
        if win_check("X"):
            print_board()
            break
        if win_check("O"):
            print_board()
            break
        if len(choices) == 0:  # if no more available spaces, call it a tie
            print("Game is a tie!")
            print_board()
            break

# The function loop above prints board, asks p1 for input, assigns p1's input on board, prints board, asks p2 for input,
# assigns p2's input on board, then checks if X or O has won, or there's a tie (no more board spaces). If not, repeat
# until the win checks check out True


def b_v_b_code():  # Player v. Bot mode function
    global b_choice, mode
    print("Player is X. Bot is O.")
    while True:
        print_board()
        bot_input()
        assign(b_choice, "X")
        bot_input()
        assign(b_choice, "O")
        if win_check("X"):
            print_board()
            break
        if win_check("O"):
            print_board()
            break
        if len(choices) == 0:  # if no more available spaces, call it a tie
            print("Game is a tie!")
            print_board()
            break


global p_choice, b_choice, mode, p2_choice

greeting()

choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# each int corresponds to position on board
# [1] [2] [3]
# [4] [5] [6]
# [7] [8] [9]

a, b, c, d, e, f, g, h, i = "-", "-", "-", "-", "-", "-", "-", "-", "-"  # variable a corresponds to position on board

while True:
    if mode == 1:
        p_v_p_code()
        break
    elif mode == 2:
        p_v_b_code()
        break
    elif mode == 3:
        b_v_b_code()
        break
    else:
        print("Mode unavailable.\n")
        greeting()
