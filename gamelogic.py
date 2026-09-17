import random


def generate_sec_num():
    return random.randint(1, 100)


def check_guess(guess, secret_number):

    if guess > secret_number:
        return "Too High!"
    elif guess < secret_number:
        return "Too Low!"
    else:
        return "Correct!"