import pygame as pg 
from settings import *
from util import load_piece_images

class ChessBoard:

    def __init__(self, game) -> None:
        self.game = game
        self.board = [
            ['b-r','b-n','b-b','b-q','b-k','b-b','b-n','b-r'],
            ['b-p','b-p','b-p','b-p','b-p','b-p','b-p','b-p'],
            ['','','','','','','','',''],
            ['','','','','','','','',''],
            ['','','','','','','','',''],
            ['','','','','','','','',''],
            ['w-p','w-p','w-p','w-p','w-p','w-p','w-p','w-p'],
            ['w-r','w-n','w-b','w-q','w-k','w-b','w-n','w-r'],

        ]
    
    def draw(self):

        self.game.screen.fill((0, 0, 0))

        for row in range(0, 8):
            for col in range(0, 8):
                if (row + col) % 2 == 0:
                    rect = pg.Rect(col * CELL_SIZE, row * CELL_SIZE ,CELL_SIZE, CELL_SIZE)
                    pg.draw.rect(self.game.screen, 'white', rect)
                else:
                    rect = pg.Rect(col * CELL_SIZE, row * CELL_SIZE ,CELL_SIZE, CELL_SIZE)
                    pg.draw.rect(self.game.screen, (255,153,0), rect)
                
                if self.board[row][col] != '':
                    self.game.screen.blit(self.game.chess_piece_images[self.board[row][col]],(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def check_inputs(self):

        for event in pg.event.get():

            pass

class Game:


    def __init__(self) -> None:
        
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pg.display.set_caption('Shess')
        self.chess_board = ChessBoard(self)
        self.chess_piece_images = load_piece_images()


    def run(self):
        
        running = True 
        current_player = 'white'
        holding_mouse = (None, False, None)
        while running:
            self.chess_board.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False


                elif event.type == pg.MOUSEBUTTONDOWN:

                    screen_mouse_x, screen_mouse_y = event.pos
                    x, y = event.pos
                    x, y = int(x // CELL_SIZE), int(y // CELL_SIZE)

                    if self.chess_board.board[y][x] != '':
                        print(self.chess_board.board[y][x])

                        # Check if it's the current player's move then move the current board while highlighting the available positions from the 
                        # current location
                        holding_mouse = ((y, x), True, self.chess_board.board[y][x])
                        self.chess_board.board[y][x] = ''
                    
                    elif self.chess_board.board[y][x] == '' and holding_mouse[1]:
                            print('Current pos: ', holding_mouse[2])
                            self.chess_board.board[y][x] = holding_mouse[2]
                            # self.chess_board.board[holding_mouse[0][0]][holding_mouse[0][1]] = ''
                            holding_mouse = (None, False, None)

            if (holding_mouse[1]):
                screen_mouse_x, screen_mouse_y = pg.mouse.get_pos()
                self.screen.blit(self.chess_piece_images[holding_mouse[2]],(screen_mouse_x - CELL_SIZE//2, screen_mouse_y - CELL_SIZE//2))

                # for event in pg.event.get():

                #     if event.type == pg.MOUSEBUTTONDOWN:
                        
                #         x, y = event.pos
                #         x, y = int(x // CELL_SIZE), int(y // CELL_SIZE)
                #         print(x, y)

                        







            
            pg.display.flip()
            

game = Game()

game.run()

        

        


    