# ui/pygame_ui.py
import pygame
import os
from engine.moves import get_legal_moves

TILE = 80
WIDTH = HEIGHT = TILE*8
WHITE = (240,217,181)
GREEN = (181,136,99)
BLUE = (0,0,255)

def detect_piece_images(folder="assets/pieces"):
    pieces={}
    type_map={"p":"pawn","r":"rook","n":"knight","b":"bishop","q":"queen","k":"king"}
    color_map={"l":"white","d":"black"}
    for f in os.listdir(folder):
        if f.lower().endswith(".png"):
            try:
                piece=color_map.get(f[7].lower())
                type_=type_map.get(f[6].lower())
            except:
                continue
            if piece and type_:
                pieces[(type_,piece)]=f
    return pieces

class ChessUI:
    def __init__(self, board):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Chess")
        self.board = board
        self.selected=None
        self.legal_moves=[]
        self.PIECE_MAP=detect_piece_images()
        self.images=self.load_images()
        for color in ("white","black"):
            for piece in ("pawn","rook","knight","bishop","queen","king"):
                if (piece,color) not in self.images:
                    raise RuntimeError(f"Missing image for {(piece,color)}")

    def load_images(self):
        images={}
        for key,file in self.PIECE_MAP.items():
            path=os.path.join("assets","pieces",file)
            img=pygame.image.load(path).convert_alpha()
            images[key]=pygame.transform.scale(img,(TILE,TILE))
        return images

    def draw_board(self):
        for r in range(8):
            for c in range(8):
                color=WHITE if (r+c)%2==0 else GREEN
                pygame.draw.rect(self.screen,color,(c*TILE,r*TILE,TILE,TILE))
                piece=self.board.board[r][c]
                if piece:
                    self.screen.blit(self.images[piece],(c*TILE,r*TILE))
        for r,c in self.legal_moves:
            pygame.draw.circle(self.screen,BLUE,(c*TILE+TILE//2,r*TILE+TILE//2),10)

    def handle_click(self,pos):
        r,c=pos[1]//TILE,pos[0]//TILE
        if self.selected:
            if (r,c) in self.legal_moves:
                self.board.move_piece(self.selected,(r,c))
            self.selected=None
            self.legal_moves=[]
        else:
            piece=self.board.board[r][c]
            if piece and piece[1]==self.board.turn:
                self.selected=(r,c)
                self.legal_moves=get_legal_moves(self.board,(r,c))

    def run(self):
        clock=pygame.time.Clock()
        running=True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    self.handle_click(pygame.mouse.get_pos())
            self.draw_board()
            pygame.display.flip()
        pygame.quit()

