from random import randrange
from brain_games.games.game import play_game

GCD_RULES = 'Find the greatest common divisor of given numbers.'


def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0


def gcd(m, n):
    d = 0

    while m != n:
        if is_even(m) and is_even(n):
            m /= 2
            n /= 2
            d += 1
        elif is_even(m) and is_odd(n):
            m /= 2
        elif is_odd(m) and is_even(n):
            n /= 2
        else:
            if m < n:
                n, m = m, n
            m = (m - n) / 2

    return round(2 ** d * m)


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
