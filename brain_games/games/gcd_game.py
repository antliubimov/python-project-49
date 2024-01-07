from random import randrange
from brain_games.games.game import play_game

GCD_RULES = 'Find the greatest common divisor of given numbers.'


def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0


def gcd(a, b):
    m = a
    n = b
    d = 1

    while m != 0 and n != 0:
        if m % 2 == 0 and n % 2 == 0:
            d *= 2
            m /= 2
            n /= 2
        elif n % 2 == 1:
            m /= 2
        elif m % 2 == 1 and n % 2 == 0:
            n /= 2
        elif m % 2 == 1 and n % 2 == 1 and m >= n:
            m -= n
        elif m % 2 == 1 and n % 2 == 1 and m < n:
            n -= m

    return round(d * n) if m == 0 else round(d * m)


def gcd_game_fn():
    MIN_NUMBER = 0
    MAX_NUMBER = 100
    num1 = randrange(MIN_NUMBER, MAX_NUMBER)
    num2 = randrange(MIN_NUMBER, MAX_NUMBER)
    question = f'{num1} {num2}'
    answer = str(gcd(num1, num2))
    return (question, answer)


def gcd_game():
    play_game(GCD_RULES, gcd_game_fn)
