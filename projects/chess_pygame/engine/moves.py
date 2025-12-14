# engine/moves.py
from copy import deepcopy

def in_bounds(r, c):
    return 0 <= r < 8 and 0 <= c < 8

# -------------------- PAWN --------------------
def get_pawn_moves(board_obj, r, c, color):
    board = board_obj.board
    moves = []
    direction = -1 if color == "white" else 1

    # Forward one
    if in_bounds(r + direction, c) and board[r + direction][c] is None:
        moves.append((r + direction, c))
        # Forward two from starting row
        if (color == "white" and r == 6) or (color == "black" and r == 1):
            if board[r + 2*direction][c] is None:
                moves.append((r + 2*direction, c))

    # Captures
    for dc in [-1, 1]:
        nr, nc = r + direction, c + dc
        if in_bounds(nr, nc):
            target = board[nr][nc]
            if target is not None and target[1] != color:
                moves.append((nr, nc))

    return moves

# -------------------- ROOK --------------------
def get_rook_moves(board_obj, r, c, color):
    board = board_obj.board
    moves = []
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        while in_bounds(nr, nc):
            target = board[nr][nc]
            if target is None:
                moves.append((nr, nc))
            else:
                if target[1] != color:
                    moves.append((nr, nc))
                break
            nr += dr
            nc += dc
    return moves

# -------------------- BISHOP --------------------
def get_bishop_moves(board_obj, r, c, color):
    board = board_obj.board
    moves = []
    directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        while in_bounds(nr, nc):
            target = board[nr][nc]
            if target is None:
                moves.append((nr, nc))
            else:
                if target[1] != color:
                    moves.append((nr, nc))
                break
            nr += dr
            nc += dc
    return moves

# -------------------- KNIGHT --------------------
def get_knight_moves(board_obj, r, c, color):
    board = board_obj.board
    moves = []
    jumps = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    for dr, dc in jumps:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc):
            target = board[nr][nc]
            if target is None or target[1] != color:
                moves.append((nr, nc))
    return moves

# -------------------- QUEEN --------------------
def get_queen_moves(board_obj, r, c, color):
    return get_rook_moves(board_obj, r, c, color) + get_bishop_moves(board_obj, r, c, color)

# -------------------- KING --------------------
def get_king_moves(board_obj, r, c, color, check_func=None):
    board = board_obj.board
    moves = []
    directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc):
            target = board[nr][nc]
            if target is None or target[1] != color:
                # Simulate move to avoid check
                tmp_board = [row.copy() for row in board]
                tmp_board[nr][nc] = tmp_board[r][c]
                tmp_board[r][c] = None
                if check_func is None or not check_func(tmp_board, color):
                    moves.append((nr, nc))
    return moves

# -------------------- LEGAL MOVES --------------------
def get_legal_moves(board_obj, position, check_func=None):
    r, c = position
    board = board_obj.board
    piece = board[r][c]
    if not piece:
        return []
    name, color = piece

    if name == "pawn":
        return get_pawn_moves(board_obj, r, c, color)
    elif name == "rook":
        return get_rook_moves(board_obj, r, c, color)
    elif name == "bishop":
        return get_bishop_moves(board_obj, r, c, color)
    elif name == "knight":
        return get_knight_moves(board_obj, r, c, color)
    elif name == "queen":
        return get_queen_moves(board_obj, r, c, color)
    elif name == "king":
        return get_king_moves(board_obj, r, c, color, check_func)
    return []

