import time
import random
import utils
import score

def generate_sequence(difficulty):
    random_list = []
    for i in range(difficulty):
        random_list.append(random.randint(1,100))
    present_random_list(random_list)
    return random_list

def present_random_list(random_list):
    print(random_list)
    time.sleep(1.7)
    utils.screen_cleaner()

def get_list_from_user(difficulty):
    users_input_list = []
    while True:
        users_input_str = input(f'Guess the list of numbers devided by spaces ({difficulty} numbers): ')
        if check_input_list_from_user(users_input_str, difficulty) is True:
            for i in users_input_str.split():
                users_input_list.append(int(i))
            return users_input_list
        else: print('Invalid input!')
    print(users_input_list)

def check_input_list_from_user(input_str, difficulty):
    input_list = input_str.split()
    if len(input_list) != difficulty:
        return False
    for l in input_list:
        if not l.isdigit():
            return False
    return True

def is_list_equal(random_list, users_input_list):
    return random_list == users_input_list

def play(difficulty):
    random_list = generate_sequence(difficulty)
    users_input_list = get_list_from_user(difficulty)

    won_is_true = False
    if is_list_equal(random_list, users_input_list):
        score.add_score(difficulty)
        won_is_true = True
    return won_is_true

print('ok')