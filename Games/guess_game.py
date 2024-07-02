import random
import WOG_Project.score as score
# from WOG_Project.utils import *
# from WOG_Project.Games.guess_game import *
def generate_number(difficulty):
    return random.randint(0, difficulty)

def get_guess_from_user(difficulty):

    while True:
        try:
            players_game_choise = int(input(f'Please enter an int between 0-{difficulty}: '))
        
            if players_game_choise < 0 or players_game_choise > difficulty:
                raise ValueError
        except ValueError:
            print("Invalid input")
        else:
            return players_game_choise
    
def compare_results(guess_from_user, secret_number):
    return guess_from_user == secret_number

def play(difficulty):
    won_is_true = False
    if compare_results(get_guess_from_user(difficulty), generate_number(difficulty)) == True:
        score.add_score(difficulty)
        won_is_true = True
    return won_is_true