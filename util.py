from settings import CELL_SIZE
import pygame as pg

def load_piece_image(piece):

    piece_surface = pg.image.load(f'images/{piece}.png').convert_alpha()
    piece_surface = pg.transform.scale(piece_surface,(CELL_SIZE, CELL_SIZE))
    return piece_surface

def load_piece_images():
    
    pieces = {
            'w-p' : load_piece_image('white-pawn'),
            'w-r' : load_piece_image('white-rook'),
            'w-b' : load_piece_image('white-bishop'),
            'w-n' : load_piece_image('white-knight'),
            'w-k' : load_piece_image('white-king'),
            'w-q' : load_piece_image('white-queen'),
            'b-p' : load_piece_image('black-pawn'),
            'b-r' : load_piece_image('black-rook'),
            'b-b' : load_piece_image('black-bishop'),
            'b-n' : load_piece_image('black-knight'),
            'b-k' : load_piece_image('black-king'),
            'b-q' : load_piece_image('black-queen'),
            }
    
    return pieces

    