"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Pavel Vít
email: vitp2@email.cz
"""

import random
import time

LINE = "-" * 62


def generate_secret_number():
    first = random.choice("123456789")  
    pool = [d for d in "0123456789" if d != first]  
    rest = random.sample(pool, 3)  
    return first + "".join(rest)


def is_valid_guess(guess):
    """
    Checks whether the user's input is valid:
    - exactly 4 digits
    - all digits are unique
    - does not start with 0
    - contains only numbers
    Additionally: prints detailed feedback if invalid.
    """
    errors = []

    if not guess.isdigit():
        errors.append("Your guess must contain digits only.")
    if len(guess) != 4:
        errors.append("Your guess must have 4 digits.")
    if guess and guess[0] == "0":
        errors.append("Your guess must not start with 0.")
    if len(set(guess)) != len(guess):
        errors.append("Digits must be unique.")

    if errors:
        print("\n".join(f"- {e}" for e in errors))
        print(LINE)
        return False
    return True


def evaluate_guess(secret, guess):
    """
    Compares the user's input with the secret number:
    - bulls: correct digit in the correct position
    - cows: correct digit, but in the wrong position
    """
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows


def pluralize(count, word):
    """Adds the ending 's' to the word if the number is not 1 (according to English grammar)."""
    return f"{count} {word}" + ("" if count == 1 else "s")


def format_time(seconds):
    """Converts seconds to 'X minutes, Y seconds' format."""
    minutes = seconds // 60
    sec = seconds % 60
    if minutes > 0:
        return f"{minutes} minute{'s' if minutes != 1 else ''}, {sec} second{'s' if sec != 1 else ''}"
    return f"{sec} second{'s' if sec != 1 else ''}"


def main():
    """Main function to run the Bulls and Cows game."""
    print("Hi there!")
    print(LINE)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(LINE)

    secret = generate_secret_number()
    attempts = 0
    start_time = time.time()

    while True:
        guess = input(f"Enter a number:\n{LINE}\n>>> ").strip()


        if not is_valid_guess(guess):
            print(
                "Invalid input! Please enter a 4-digit number with unique digits "
                "and not starting with 0."
            )
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret, guess)

        if bulls == 4:
            duration = round(time.time() - start_time)
            print("Correct, you've guessed the right number")
            print(f"in {pluralize(attempts, 'guess')}!")
            print(LINE)
            print("That's amazing!")
            print(f"Time taken: {format_time(duration)}")
            break
        else:
            print(f"{pluralize(bulls, 'bull')}, {pluralize(cows, 'cow')}")
            elapsed_time = round(time.time() - start_time)
            print(f"Time elapsed: {format_time(elapsed_time)}")
            print(LINE)


if __name__ == "__main__":

    main()
