import prompt
from random import randrange
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    CORRECT_ANSWERS_COUNT = 3
    answer_count = 0
    while answer_count < CORRECT_ANSWERS_COUNT:
        number = randrange(100)
        answer = "yes" if number % 2 == 0 else "no"
        print(f"Question: {number}")
        your_answer = prompt.string("Your answer: ")
        if answer != your_answer:
            print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {name}")
            return
        answer_count += 1
        print("Correct!")

    print(f"Congratulations, {name}")
