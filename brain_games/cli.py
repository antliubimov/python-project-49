import prompt


def greeting():
    print("Welcome to the Brain Games!")


def welcome_user():
    greeting()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name
