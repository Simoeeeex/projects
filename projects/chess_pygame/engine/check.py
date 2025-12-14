# engine/check.py
from engine import moves

def find_king(board, color):
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece and piece[0] == "king" and piece[1] == color:
                return (r, c)
    return None

def is_in_check(board, color):
    # If Board object
    if hasattr(board, "board"):
        board = board.board

    kr, kc = find_king(board, color)
    if kr is None:
        return False

    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece and piece[1] != color:
                name = piece[0]
                tmp_obj = type("tmp", (), {"board": board})()
                moves_list = []
                if name == "pawn":
                    moves_list = moves.get_pawn_moves(tmp_obj, r, c, piece[1])
                elif name == "rook":
                    moves_list = moves.get_rook_moves(tmp_obj, r, c, piece[1])
                elif name == "bishop":
                    moves_list = moves.get_bishop_moves(tmp_obj, r, c, piece[1])
                elif name == "knight":
                    moves_list = moves.get_knight_moves(tmp_obj, r, c, piece[1])
                elif name == "queen":
                    moves_list = moves.get_queen_moves(tmp_obj, r, c, piece[1])
                # Ignore enemy king
                if (kr, kc) in moves_list:
                    return True
    return False

