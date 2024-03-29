from math import sqrt, floor
from brain_games.games.game import play_game, game_fn

PRIME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    if number < 2:
        return False
    max_delim = floor(sqrt(number)) + 1
    for i in range(2, max_delim):
        if number % i == 0:
            return False
    return True


def check_prime(number):
    return 'yes' if is_prime_number(number) else 'no'


def prime_game_fn():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    return game_fn(check_prime, MIN_NUMBER, MAX_NUMBER)


def prime_game():
    play_game(PRIME_RULES, prime_game_fn)
