import random

def generate_code():
    return random.sample(range(10), 4)

def get_guess(index):
    while True:
        try:
            guess = int(input(f"Enter digit {index}: "))
            if guess < 0:
                print("Please enter a non-negative number.")
            elif guess > 9:
                print("Please enter a number between 0 and 9.")
            else:
                return guess
        except ValueError:
            print("Please enter a valid integer.")

def compare_digits(guess, code):
    correct_digits = sum(guess[i] == code[i] for i in range(4))
    misplaced_digits = len(set(guess) & set(code)) - correct_digits
    return correct_digits, misplaced_digits

def play_game():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("WELCOME TO CRACK THE CODE")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print()
    print("Rules:")
    print("1. Numbers are between 0-9")
    print("2. Do not enter numbers that are negative or exceed 9")
    print()

    code = generate_code()
    gameState = 0

    while gameState < 4:
        guess = []
        for i in range(1, 5):
            guess.append(get_guess(i))

        correct_digits, misplaced_digits = compare_digits(guess, code)

        if correct_digits == 4:
            print("Congratulations! You cracked the code!")
            print("The code was:", "".join(str(digit) for digit in code))
            return

        print()
        print("Correct digits:", correct_digits)
        print("Misplaced digits:", misplaced_digits)
        print()

        gameState += 1

    print("Game over! You couldn't crack the code.")
    print("The code was:", "".join(str(digit) for digit in code))

if __name__ == '__main__':
    play_game()
