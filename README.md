# CodeAlpha_Hangman

# 📌 Hangman Game (Python)

## 🎯 Goal  
Create a simple text-based Hangman game where the player guesses a word one letter at a time.

---

## 🧩 Project Description  

This is a beginner-friendly Python project that implements a basic version of the classic Hangman game using the command line. The program randomly selects a word, and the player tries to guess it letter by letter within a limited number of attempts.

---

## 🔍 Simplified Scope  

- Uses a small list of **5 predefined words**  
- Maximum of **6 incorrect guesses allowed**  
- Built using **basic console input/output**  
- No graphics or external libraries required  

---

## 🛠️ Key Concepts Used  

- `random` module  
- `while` loop  
- `if-else` conditions  
- Strings  
- Lists  

---

## 🎮 How the Game Works  

1. The program selects a random word from a predefined list.  
2. The player inputs one letter per turn.  
3. If the guess is correct:  
   - The letter is revealed in the word.  
4. If the guess is incorrect:  
   - The remaining attempts decrease.  
5. The game continues until:  
   - The player guesses the word (Win 🎉), or  
   - The player runs out of attempts (Game Over 💀)  

---

## 📂 Project Structure  

hangman.py   # Main Python file containing the game logic


---

## ▶️ How to Run  

1. Install Python (if not already installed)  
2. Clone this repository:  
   ```bash
   git clone https://github.com/unknownmeh/CodeAlpha/hangman-game.git
3.Navigate to the folder:
    cd hangman-game
4. Run the game:
    python hangman.py


#Example Gameplay

Welcome to Hangman!  
Guess the word one letter at a time.  

Word: _ _ _ _ _  

Enter a letter: a  
❌ Wrong guess.  

Remaining attempts: 5  
