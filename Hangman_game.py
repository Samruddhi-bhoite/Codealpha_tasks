import random

words = ["laptop", "cricket", "sky", "computer", "book"]
word = random.choice(words)

display = ["_"] * len(word)
attempts = 6
guessed = set()

print("Welcome to Hangman!")
print("Guess the word:", " ".join(display))

while attempts > 0 and "_" in display:
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single valid letter!")
        continue

    if guess in guessed:
        print("You already guessed that letter!")
        continue

    guessed.add(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    print(" ".join(display))

if "_" not in display:
    print("Congratulations You win!")
    print("The word was:", word)
else:
    print("You lost! The word was:", word)

