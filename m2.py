from gamelogic import generate_sec_num, check_guess
from Score import calculate_score


def play_game():

    print("I have selected a number between 1 & 100")
    print("You have 7 attempts")

    secret_number = generate_sec_num()

    max_attempts = 7

    for attempt in range(1, max_attempts + 1):

        # Take user's guess
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a No b/w 1 and 100.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue
        result = check_guess(guess, secret_number)

        print(result)

        if result == "Correct!":

            print("\nCongratulations!")
            print(f"You guessed the number in {attempt} attempts.")

            player_score = calculate_score(attempt)
            print(f"Your score: {player_score}")

            return

        attempts_remaining = max_attempts - attempt
        print(f"Attempts remaining: {attempts_remaining}")

    print("\nGame Over!")
    print(f"The secret number was: {secret_number}")


while True:

    play_game()

    choice = input("\nDo you want to play again? (y/n): ").lower()

    if choice != "y":
        print("\nThanks for playing! 👋")
        break