import prompt
from brain_games.cli import welcome_user


def view_rules(rules):
    print(rules)


def wrongAnswer(question_answer, answer):
    print(f"'{question_answer}' is wrong answer ;(. Correct answer was '{answer}'.")


def play_game(rules, game_fn):
    name = welcome_user()
    view_rules(rules)
    ATTEMPTS_COUNT = 3
    attempts = 0
    while attempts < ATTEMPTS_COUNT:
        question, answer = game_fn()
        print(f"Question: {question}")
        question_answer = prompt.string("Your answer: ")
        if answer != question_answer:
            wrongAnswer(question_answer, answer)
            print(f"Let's try again, {name}")
            break
        attempts += 1
        print("Correct!")

    if attempts == ATTEMPTS_COUNT:
        print(f"Congratulations, {name}")
    return
