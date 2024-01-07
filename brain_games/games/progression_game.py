from random import randrange, randint
from brain_games.games.game import play_game


PROGRESSION_RULES = 'What number is missing in the progression?'


def progression_game_fn():
    MIN_STEP = 1
    MAX_STEP = 10
    PROGRESSION_LENGTH = 10
    MIN_NUMBER = 0
    MAX_NUMBER = 100
    step = randint(MIN_STEP, MAX_STEP)
    progression_start = randint(MIN_NUMBER, MAX_NUMBER)
    progression_end = progression_start + step * PROGRESSION_LENGTH
    progression = list(range(progression_start, progression_end, step))
    answer_index = randrange(0, PROGRESSION_LENGTH - 1)
    answer = str(progression[answer_index])
    progression[answer_index] = '..'
    question = ' '.join(str(x) for x in progression)
    return (question, answer)


def progression_game():
    play_game(PROGRESSION_RULES, progression_game_fn)
