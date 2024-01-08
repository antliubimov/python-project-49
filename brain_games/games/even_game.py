from brain_games.games.game import play_game, game_fn

EVEN_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_number(number):
    return number % 2 == 0


def check_even(number):
    return "yes" if is_even_number(number) else "no"


def even_game_fn():
    MIN_NUMBER = 0
    MAX_NUMBER = 100
    return game_fn(check_even, MIN_NUMBER, MAX_NUMBER)


def even_game():
    play_game(EVEN_RULES, even_game_fn)
