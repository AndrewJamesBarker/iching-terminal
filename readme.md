Original data generously provided by [adamblvck/iching-wilhelm-dataset](https://github.com/adamblvck/iching-wilhelm-dataset/tree/master), which I then refined by correcting data type inconsistencies and converting into a clean JSON format.

# Terminal I Ching

A command-line tool to consult the I Ching (Book of Changes).

## 🌱 How to Use

1. **Clone the repository**

   ```bash
   git clone git@github.com:AndrewJamesBarker/iching-terminal.git
   cd iching-terminal
   ```

2. **Run the program from /iching-terminal dir**

   ```bash
   python3 -m iching

   ```

When you ask a question, a hexagram is formed by simulating three coin tosses for each of the six lines. Each toss yields either 2 (tails) or 3 (heads), and the sum of the three values determines the line: an odd total creates a solid yang line (⚊), while an even total creates a broken yin line (⚋).

## 📦 Structure

* `main.py` – Program entry point
* `iching/` – Game logic and data
* `assets/json/hexagrams_full.json` – Full I Ching hexagram dataset as a json object.


---

