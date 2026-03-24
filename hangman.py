import random

# Predefined words
words = ["python", "apple", "tiger", "ocean", "robot"]

# Select random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Game loop
while wrong_guesses < max_wrong:
    
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord:", display_word)

    # Check win
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess.")
        print("Remaining attempts:", max_wrong - wrong_guesses)

# If player loses
if wrong_guesses == max_wrong:
    print("\n💀 Game Over! The word was:", word)