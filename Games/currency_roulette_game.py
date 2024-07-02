import freecurrencyapi
import random
import WOG_Project.score as score

secret_number = random.randint(1, 100)

def get_money_interval():
    client = freecurrencyapi.Client('fca_live_v0krgxnFyGuWs5AzQjUXj64WKEv6nQuPyUHh6yKG')
    #gets the rate as float with 2 digits after the decimal point
    usd_to_ils_rate = round(float(client.latest(base_currency='USD', currencies=['ILS']).get('data').get('ILS')), 2)

    return secret_number * usd_to_ils_rate

def get_guess_from_user():
    while True:
        try:
            players_game_choise = round(float(input(f'Guess the value of {secret_number} USD in NIS: ')), 2)
            break
        except ValueError:
            print("Invalid input")
    return players_game_choise    

def compare_results(difficulty):
    interval = 10 - difficulty
    users_guess = get_guess_from_user()
    money_interval = get_money_interval()
    return (users_guess >= (money_interval - interval) and users_guess <= (money_interval + interval))

def play(difficulty):
    won_is_true = False
    if compare_results(difficulty):
        score.add_score(difficulty)
        won_is_true = True
    return won_is_true