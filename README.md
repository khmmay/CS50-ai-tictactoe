# ❌⭕ Tic Tac Toe AI (CS50 AI)

## 📌 Overview
This project implements an AI that plays Tic Tac Toe optimally using the **Minimax algorithm**.

The AI evaluates all possible game states and always chooses the move that maximizes its chances of winning (or at least drawing), making it impossible to beat.

---

## 🧠 How It Works

The game is modeled as a **state-space search problem**:

- Each board configuration represents a **state**
- Possible moves represent **actions**
- The AI explores all future states to make decisions

The AI uses:

👉 **Minimax Algorithm**

- Maximizing player (X) tries to maximize the score  
- Minimizing player (O) tries to minimize the score  

---

## 🎯 Game Logic

- **X** always goes first  
- Players alternate turns  
- The game ends when:
  - A player has three in a row  
  - The board is full (draw)

---

## ⚙️ Features

- Fully functional Tic Tac Toe game logic  
- AI that plays optimally (cannot be beaten)  
- Detects winners and terminal states  
- Evaluates board utility (win, loss, draw)  

---

## 📂 Project Structure

```
tictactoe/
│── tictactoe.py     # Game logic and AI (Minimax)
│── runner.py        # Optional graphical interface
```

---

## ▶️ Usage

Run the game:

```bash
python3 runner.py
```

---

## 🧪 Example Gameplay

- You play as **O**
- The AI plays as **X**
- The AI will:
  - Win if possible  
  - Force a draw otherwise  

---

## 🧩 Key Concepts

- Adversarial search  
- Minimax algorithm  
- Recursion  
- Game theory  
- State evaluation  

---

## 🚀 Possible Improvements

- Add alpha-beta pruning for efficiency  
- Improve UI/UX of the game interface  
- Allow difficulty levels (non-optimal AI)  
- Add multiplayer mode  

---

## 📚 Acknowledgements

This project is part of Harvard's **CS50: Introduction to Artificial Intelligence with Python**.

---

## 👨‍💻 Author

Karl Henrik May  
https://github.com/khmmay
