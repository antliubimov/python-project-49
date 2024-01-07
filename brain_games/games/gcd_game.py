from random import randrange
from brain_games.games.game import play_game

GCD_RULES = 'Find the greatest common divisor of given numbers.'


def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0


def gcd(m, n):
    if m == 0:
        return round(n)
    elif n == 0:
        return round(m)
    elif m == n:
        return round(m)
    elif (m == 1 and n > 0) or (n == 1 and m > 0):
        return 1
    elif is_even(m) and is_even(n):
        gcd(m/2, n/2) * 2
    elif is_even(m) and is_odd(n):
        gcd(m/2, n)
    elif is_odd(m) and is_even(n):
        gcd(m, n/2)
    elif is_odd(m) and is_odd(n):
        if n > m:
            gcd(m, (n - m)/2)
        else:
            gcd((m - n)/2, n)


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
