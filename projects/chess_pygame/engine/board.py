# engine/board.py

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.turn = "white"
        self.setup_board()
        # Track whether kings and rooks have moved (for castling)
        self.has_moved = {
            ("king", "white"): False,
            ("king", "black"): False,
            ("rook", "white", 0): False,
            ("rook", "white", 7): False,
            ("rook", "black", 0): False,
            ("rook", "black", 7): False
        }

    def setup_board(self):
        # Pawns
        for i in range(8):
            self.board[1][i] = ("pawn", "black")
            self.board[6][i] = ("pawn", "white")
        # Rooks
        self.board[0][0] = self.board[0][7] = ("rook", "black")
        self.board[7][0] = self.board[7][7] = ("rook", "white")
        # Knights
        self.board[0][1] = self.board[0][6] = ("knight", "black")
        self.board[7][1] = self.board[7][6] = ("knight", "white")
        # Bishops
        self.board[0][2] = self.board[0][5] = ("bishop", "black")
        self.board[7][2] = self.board[7][5] = ("bishop", "white")
        # Queens
        self.board[0][3] = ("queen", "black")
        self.board[7][3] = ("queen", "white")
        # Kings
        self.board[0][4] = ("king", "black")
        self.board[7][4] = ("king", "white")

    def move_piece(self, start, end):
        r1, c1 = start
        r2, c2 = end
        piece = self.board[r1][c1]

        # Track king/rook moves
        if piece[0] == "king":
            self.has_moved[(piece[0], piece[1])] = True
        if piece[0] == "rook":
            self.has_moved[(piece[0], piece[1], c1)] = True

        self.board[r2][c2] = piece
        self.board[r1][c1] = None
        # Switch turn
        self.turn = "black" if self.turn == "white" else "white"

