secret_word = "python"

while True:
    guess = input("Guess the correct language:").strip().lower()
    if guess == secret_word:
        print("Congratulations! You guessed correctly.")
        break
    else:
        print("Incorrect guess. Try again.")