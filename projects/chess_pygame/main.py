# main.py
from engine.board import Board
from ui.pygame_ui import ChessUI

board = Board()
ui = ChessUI(board)
ui.run()

