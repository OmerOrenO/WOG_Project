from Games.app import welcome, start_play
import utils
import score

welcome()
while True:
    utils.screen_cleaner()
    if start_play() == True:
        print('YOU WON!')
    else:
        print('YOU LOSE, YOU LOSERRRR!!!')    
    score.print_score_from_file()
    another_game = input('Would you like to play another game? [Y/N]: ')
    if another_game.capitalize() != 'Y':
        break