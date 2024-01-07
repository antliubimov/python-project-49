from random import randrange
from math import sqrt, floor
from brain_games.games.game import play_game

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
    MIN_NUMBER = 0
    MAX_NUMBER = 100
    question = randrange(MIN_NUMBER, MAX_NUMBER)
    answer = check_prime(question)
    return (question, answer)


def even_game():
    play_game(PRIME_RULES, prime_game_fn)