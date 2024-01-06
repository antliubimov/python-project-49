from random import randrange, choice
from brain_games.games.game import play_game


CALC_RULES = 'What is the result of the expression?'


def calc_game_fn():
    MIN_NUMBER = 0
    MAX_NUMBER = 100
    SIGNS = ('+', '-', '*')
    sign = choice(SIGNS)
    num1 = randrange(MIN_NUMBER, MAX_NUMBER)
    num2 = randrange(MIN_NUMBER, MAX_NUMBER)
    question = f'{num1} {sign} {num2}'
    answer = 0

    if sign == '+':
        answer = num1 + num2
    elif sign == '-':
        answer = num1 - num2
    elif sign == '*':
        answer = num1 * num2

    return (question, str(answer))


def calc_game():
    play_game(CALC_RULES, calc_game_fn)
