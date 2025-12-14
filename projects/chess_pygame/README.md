# Chess Pygame

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pygame](https://img.shields.io/badge/Project-Pygame-success)

**Created by SIMOEEEEX**

---

## Description

**Chess Pygame** is a Python-based chess game built with **Pygame**.  
It features a **graphical board**, piece movement, and basic game logic.

> ⚠️ Note: Check detection and castling (rook + king special moves) are **not implemented**.

---

## Features

- 🖥️ Interactive **Pygame GUI**
- ♟️ Standard chess pieces
- 🔄 Turn-based gameplay (White / Black)
- 📦 Piece images loaded from `assets/pieces`
- 🎨 Dark and light square board coloring
- 🔹 Highlights legal moves for selected pieces
- 🖤 Modern minimal theme

---

## Installation

1. Make sure Python 3 is installed  
2. Install Pygame

```bash
pip install pygame

...
Run the game:

bash
Copy code
python main.py
Controls
Click a piece to select it

Click a valid square to move the piece

Legal moves are highlighted with blue circles.

Notes / Limitations
✅ Standard piece movements are implemented

⚠️ Check detection is incomplete

⚠️ Castling (king + rook) does not work

No AI / computer opponent (two-player mode only)

No en passant or promotion rules fully handled

File Structure
markdown
Copy code
chess_pygame/
├── assets/
│   └── pieces/
├── engine/
│   ├── board.py
│   ├── moves.py
│   ├── check.py
│   └── __init__.py
├── ui/
│   ├── pygame_ui.py
│   └── __init__.py
└── main.py
License
MIT License
