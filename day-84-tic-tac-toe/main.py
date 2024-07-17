import random
game_array = ["", "", "", "", "", "", "", "", ""]


def game_table():
    print("--------")
    print(f"{game_array[0]} | {game_array[1]} | {game_array[2]}")
    print(game_array[3] + " | " + game_array[4] + " | " + game_array[5])
    print(game_array[6] + " | " + game_array[7] + " | " + game_array[8])
    print("--------")  # this can be better


def get_user_input():
    answer = int(input("Please enter the number of cell you want to put your X in (0-8): "))
    return answer


def get_random_input():
    rand_number = random.randint(0, 8)
    return rand_number


def arrange_array(index, key):
    game_array[index] = key


def who_won(s_array):
    winner = ""
    for string in s_array:
        if string == "XXX":
            winner = "X"
            break
        elif string == "OOO":
            winner = "O"
            break
        else:
            winner = ""
    return winner


def control_the_game():
    string_array = []
    for i in range(0, 7, 3):
        string = game_array[i] + game_array[i+1] + game_array[i+2]
        string_array.append(string)
    for j in range(0, 3):
        string = game_array[j] + game_array[j + 3] + game_array[j + 6]
        string_array.append(string)
    string_array.append(game_array[0] + game_array[4] + game_array[8])
    string_array.append(game_array[2] + game_array[4] + game_array[6])
    winner = who_won(string_array)
    if winner != "":
        return True
    else:
        return False


def user_play():
    user_input = get_user_input()
    if user_input < 0 or user_input > 8 or game_array[user_input] != "":
        print("enter a number between 0-8 and in empty cells")  # when its invalid for int?
        user_play()
    else:
        arrange_array(user_input, "X")


def random_play():
    random_input = get_random_input()
    if random_input < 0 or random_input > 8 or game_array[random_input] != "":
        random_play()
    else:
        arrange_array(random_input, "O")


def game_play():
    user_play()
    game_table()
    is_winner = control_the_game()
    if is_winner:
        print("X won!")
    elif "" not in game_array:
        print("Draw!")
    else:
        random_play()
        game_table()
        is_winner = control_the_game()
        if is_winner:
            print("O won!")
        else:
            game_play()


def main():
    game_table()
    game_play()


if __name__ == '__main__':
    main()
