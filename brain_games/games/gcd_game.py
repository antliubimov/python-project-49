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
    if n == 0 or m == n:
        return round(m)
    if (m == 1 and n > 0) or (n == 1 and m > 0):
        return 1

    result = 0

    if is_even(m):
        if is_even(n):
            result = gcd(m/2, n/2) * 2
        else:
            result = gcd(m/2, n)
    elif is_odd(m):
        if is_even(n):
            result = gcd(m, n/2)
        else:
            if n > m:
                result = gcd(m, (n - m)/2)
            else:
                result = gcd((m - n)/2, n)
    return result


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
