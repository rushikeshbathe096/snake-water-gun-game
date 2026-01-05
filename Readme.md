# Snake Water Gun – Adaptive AI Game (Python)

A command-line implementation of the classic Snake–Water–Gun game, built as a system-level Python project rather than a simple script.

The focus of this project is clean architecture, AI abstraction, player behavior tracking, analytics, and data visualization.

---

## Features

- Modular and maintainable Python codebase  
- Pluggable AI system using a common interface  
- Adaptive AI that learns from player move history  
- Player behavior tracking  
- Game statistics (wins, losses, draws, move frequency)  
- Data visualization using matplotlib  
- Works in headless environments (WSL / Linux servers)

---

## How the Adaptive AI Works

- The game records the player’s past moves.
- The AI identifies the most frequently used move.
- It selects a counter-move based on the game rules.
- If no history is available, the AI falls back to random behavior.

The logic is simple, explainable, and easily extensible.

---

## Analytics & Visualization

The system tracks:
- Player move frequency
- Game outcomes (win / lose / draw)

Plots are generated using matplotlib and saved as image files:
- `plots/move_frequency.png`
- `plots/game_results.png`

This approach avoids GUI dependencies and works well in WSL and server environments.

---

## Installation & Running

### Requirements
- Python 3.x


### Install dependencies
```bash
pip install -r requirements.txt
