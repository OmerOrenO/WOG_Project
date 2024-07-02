import sys
import os
import time
# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the WOG_Project directory (two levels up)
wog_project_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))

# Add the WOG_Project directory to sys.path
sys.path.append(wog_project_dir)

# Now import the utils module and guess_game
import WOG_Project.utils as utils
import WOG_Project.Games.guess_game as guess_game
import WOG_Project.Games.currency_roulette_game as currency_roulette_game
import WOG_Project.Games.memory_game as memory_game 
import WOG_Project.score as score


games_list = [memory_game, guess_game, currency_roulette_game]

def welcome():
    players_name = input('Enter your name: ')
    print(f"Hi {players_name} and welcome to to the World of Games: The Epic Journey")
    time.sleep(3)
    

def play():
    players_game_choise = 0
    while True:
        try:
            players_game_choise = int(input('''Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
            2. Guess Game - guess a number and see if you chose like the computer.
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n'''))

            if players_game_choise not in {1, 2, 3}:
                print('Please try again entering a valid NUMBER BETWEEN 1-3')
            else:
                break
        except ValueError:
            print('Please enter a valid integer.')

    while True:
        try:
            games_difficulty = int(input('Please enter the difficulty between 1-5: '))
            if games_difficulty not in {1, 2, 3, 4, 5}:
                print('Please try again entering a valid number between 1-5.')
            else:
                break
        except ValueError:
            print('Please enter a valid integer.')

    
    return games_list[players_game_choise - 1].play(games_difficulty)

def start_play():
    while True:
        utils.screen_cleaner()
        if play() == True:
            print('YOU WON!')
        else:
            print('YOU LOSE, YOU LOSERRRR!!!')    
        score.print_score_from_file()
        another_game = input('Would you like to play another game? [Y/N]: ')
        if another_game.capitalize() != 'Y':
            break

# if __name__ == "__main__":
# #     welcome()
#     print(start_play())