import os
import utils

def add_score(difficulty):
    try:    
        calculated_new_score_add = difficulty * 3 + 5
        # if os.path.exists(utils.SCORES_FILE_NAME) == False:
        if os.path.exists(utils.SCORES_FILE_NAME):
        # Read the current score
            with open(utils.SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read())
        else:
            current_score = 0
        
        new_score = current_score + calculated_new_score_add
       
        with open(utils.SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))
    
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An I/O error occurred while operating on the file.")
    except Exception as e:
        print("An error occurred:", e)

def print_score_from_file():
    try:    
        with open(utils.SCORES_FILE_NAME, 'r') as scores_file:
            saved_score = scores_file.read()
            if len(saved_score) == 0:
                saved_score = 0
            else:
                saved_score = int(saved_score)
            print('New Score = ', saved_score)
    
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An I/O error occurred while operating on the file.")
    except Exception as e:
        print("An error occurred:", e)
