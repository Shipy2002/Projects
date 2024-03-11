# defining all modules
import random
import time
import sys

# toss_list = ["ODD", "EVEN"]#toss list
CHOICE = ["BAT", "BOWL"]  # Choice
delay = 0.5  # delay given in seconds


def toss():  # from toss to choice of catting or bowling
    user_toss = to_get_valid_str_inputs("ODD", "EVEN")
    comp_toss_input = random.randint(1, 6)  # generating num from 1 to 6 randomly
    user_toss_input = to_get_valid_input()
    print("Computer toss value: ", comp_toss_input)
    if user_toss == "EVEN":  # this nested if else block is used to decide toss winner
        if (user_toss_input + comp_toss_input) % 2 == 0:
            print("You Have won the toss")
            toss_winner = 1
        else:
            print("Comp have won the toss")
            toss_winner = 0
    else:
        if (user_toss_input + comp_toss_input) % 2 == 1:
            print("You Have won the toss")
            toss_winner = 1
        else:
            print("Comp have won the toss")
            toss_winner = 0
    if toss_winner == 1:  # this if else block is to get to know if user is going to bat or bowl
        user_bat_or_bowl = to_get_valid_str_inputs("BAT", "BOWL")
    else:
        user_bat_or_bowl = random.choice(CHOICE)
        if user_bat_or_bowl == "BAT":
            print("Computer chose to BOWL first..")
        else:
            print("Computer chose to BAT first..")
    return user_bat_or_bowl


def to_get_valid_input():
    user_input = input("Enter any number from 1 to 6: ")
    while True:
        if user_input.isnumeric():  # if entered value is number but not in given range then ask for input again
            while int(user_input) not in range(1, 7):
                print("You did not enter any one number from 1 to 6!!!")
                user_input = input("ENTER NUMBER ONLY FROM 1 TO 6: ")
                time.sleep(delay)
            break
        elif not user_input.isnumeric():  # this is used when entered is not a number
            user_input = input("ENTER NUMBER ONLY FROM 1 TO 6(not letters): ")
    return int(user_input)


def to_get_valid_str_inputs(choice1, choice2):  # to get exact input the program need from user
    time.sleep(delay)
    input_from_user = input("Choose " + choice1 + " or " + choice2 + ": ").upper().strip()
    while True:
        if input_from_user == choice1:
            print("Your Choice " + choice1)
            break
        elif input_from_user == choice2:
            print("Your Choice " + choice2)
            break
        else:
            input_from_user = input("Enter the valid input:(" + choice1 + " or " + choice2 + ") ").upper()
    return input_from_user


def batting():
    score_user = 0  # initializing score
    print("Start Batting: \n")
    while True:
        user_batting = to_get_valid_input()
        comp_batting = random.randint(1, 6)
        if user_batting != comp_batting:
            print("Computer Bowled " + str(comp_batting))
            time.sleep(delay)
            score_user += user_batting
            print("Current Score: " + str(score_user))
            time.sleep(delay)
        else:
            print("Computer Bowled " + str(comp_batting))
            time.sleep(delay)
            print("Out!!!")
            print("you scored " + str(score_user))
            time.sleep(delay)
            print("Target to defend: ", score_user + 1)
            break
    print("Start bowling")
    score_comp = 0
    while True:
        user_batting = to_get_valid_input()
        comp_batting = random.randint(1, 6)
        if user_batting != comp_batting:
            print("Computer scored " + str(comp_batting))
            time.sleep(delay)
            score_comp += comp_batting
            print("Current Score: " + str(score_comp))
            time.sleep(delay)
            if score_comp > score_user:
                winner = to_check_winner(score_user, score_comp)
                return winner
            else:
                print("Need to defend " + str(score_user + 1 - score_comp) + " runs to win!")
        else:
            print("Computer Bowled " + str(comp_batting))
            time.sleep(delay)
            print("Out!!!")
            print("computer scored " + str(score_comp))
            time.sleep(delay)
            winner = to_check_winner(score_user, score_comp)
            break

    return winner


def bowling():
    print("Start bowling")
    score_comp = 0
    while True:
        user_batting = to_get_valid_input()
        comp_batting = random.randint(1, 6)
        if user_batting != comp_batting:
            print("Computer scored " + str(comp_batting))
            time.sleep(delay)
            score_comp += comp_batting
            print("Current Score: " + str(score_comp))
            time.sleep(delay)
        else:
            print("Computer Bowled " + str(comp_batting))
            time.sleep(delay)
            print("Out!!!")
            print("computer scored " + str(score_comp))
            time.sleep(delay)
            print("Target to attain: ", score_comp + 1)
            break
    score_user = 0
    print("Start Batting: \n")
    while True:
        user_batting = to_get_valid_input()
        comp_batting = random.randint(1, 6)
        if user_batting != comp_batting:
            print("Computer Bowled " + str(comp_batting))
            time.sleep(delay)
            score_user += user_batting
            print("Current Score: " + str(score_user))
            if score_user > score_comp:
                winner = to_check_winner(score_user, score_comp)
                return winner
            else:
                print("Need " + str(score_comp + 1 - score_user) + " runs to win!")
            time.sleep(delay)
        else:
            print("Computer Bowled " + str(comp_batting))
            time.sleep(delay)
            print("Out!!!")
            print("you scored " + str(score_user))
            time.sleep(delay)
            winner = to_check_winner(score_user, score_comp)
            break
    return winner


def to_check_winner(user, comp):
    if user > comp:
        win = "User"
    elif comp > user:
        win = "Computer"
    else:
        win = "Game Draw"
    return win


def game_flow():
    user_is = toss()
    if user_is == "BAT":
        win = batting()
        time.sleep(delay)
        print("Thanks for playing!! WINNER:" + win)
        sys.exit(1)
    else:
        win = bowling()
        print("Thanks for playing!! WINNER:" + win)
        sys.exit(1)


if __name__ == "__main__":
    game_flow()
