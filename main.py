import pygame
import os
from pygame.locals import *

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

class Pawn(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.color_type = color
        if self.color_type == "black":
            image_name = "pawn_b.png"
        elif self.color_type == "white":
            image_name = "pawn_w.png"
        else: raise ValueError("No color")

        self.image = pygame.image.load(os.path.join(img_folder, image_name)).convert()
        self.image = pygame.transform.scale(self.image, (game.return_arg("cell_size"), game.return_arg("cell_size")))
        if self.color_type == "black":
            self.image.set_colorkey((255, 255, 255))
        elif self.color_type == "white":
            self.image.set_colorkey((0, 0, 0))
        else: raise ValueError("No color")
        self.rect = self.image.get_rect()

    def load_unit(self, cell):
        size = game.return_arg("cell_size")
        x = cell[0]
        y = cell[1]
        self.rect.topleft = (70 + size * (x-1), 70 + size * y)
        self.rect.bottomleft = (70 + size * (x), 70 + size * (y+1))

class Knight(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.color_type = color
        if self.color_type == "black":
            image_name = "knight_b.png"
        elif self.color_type == "white":
            image_name = "khight_w.png"
        else:
            raise ValueError("No color")

        self.image = pygame.image.load(os.path.join(img_folder, image_name)).convert()
        self.image = pygame.transform.scale(self.image, (game.return_arg("cell_size"), game.return_arg("cell_size")))
        if self.color_type == "black":
            self.image.set_colorkey((255, 255, 255))
        elif self.color_type == "white":
            self.image.set_colorkey((0, 0, 0))
        else:
            raise ValueError("No color")
        self.rect = self.image.get_rect()
    def load_unit(self, cell):
        size = game.return_arg("cell_size")
        x = cell[0]
        y = cell[1]
        self.rect.topleft = (70 + size * (x-1), 70 + size * y)
        self.rect.bottomleft = (70 + size * (x), 70 + size * (y+1))

class Queen(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.color_type = color
        if self.color_type == "black":
            image_name = "queen_b.png"
        elif self.color_type == "white":
            image_name = "queen_w.png"
        else:
            raise ValueError("No color")

        self.image = pygame.image.load(os.path.join(img_folder, image_name)).convert()
        self.image = pygame.transform.scale(self.image, (game.return_arg("cell_size"), game.return_arg("cell_size")))
        if self.color_type == "black":
            self.image.set_colorkey((255, 255, 255))
        elif self.color_type == "white":
            self.image.set_colorkey((0, 0, 0))
        else:
            raise ValueError("No color")
        self.rect = self.image.get_rect()
    def load_unit(self, cell):
        size = game.return_arg("cell_size")
        x = cell[0]
        y = cell[1]
        self.rect.topleft = (70 + size * (x-1), 70 + size * y)
        self.rect.bottomleft = (70 + size * (x), 70 + size * (y+1))

class King(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.color_type = color
        if self.color_type == "black":
            image_name = "king_b.png"
        elif self.color_type == "white":
            image_name = "king_w.png"
        else:
            raise ValueError("No color")

        self.image = pygame.image.load(os.path.join(img_folder, image_name)).convert()
        self.image = pygame.transform.scale(self.image, (game.return_arg("cell_size"), game.return_arg("cell_size")))
        if self.color_type == "black":
            self.image.set_colorkey((255, 255, 255))
        elif self.color_type == "white":
            self.image.set_colorkey((0, 0, 0))
        else:
            raise ValueError("No color")
        self.rect = self.image.get_rect()
    def load_unit(self, cell):
        size = game.return_arg("cell_size")
        x = cell[0]
        y = cell[1]
        self.rect.topleft = (70 + size * (x-1), 70 + size * y)
        self.rect.bottomleft = (70 + size * (x), 70 + size * (y+1))

class Bishop(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.color_type = color
        if self.color_type == "black":
            image_name = "bishop_b.png"
        elif self.color_type == "white":
            image_name = "bishop_w.png"
        else:
            raise ValueError("No color")

        self.image = pygame.image.load(os.path.join(img_folder, image_name)).convert()
        self.image = pygame.transform.scale(self.image, (game.return_arg("cell_size"), game.return_arg("cell_size")))
        if self.color_type == "black":
            self.image.set_colorkey((255, 255, 255))
        elif self.color_type == "white":
            self.image.set_colorkey((0, 0, 0))
        else:
            raise ValueError("No color")
        self.rect = self.image.get_rect()
    def load_unit(self, cell):
        size = game.return_arg("cell_size")
        x = cell[0]
        y = cell[1]
        self.rect.topleft = (70 + size * (x-1), 70 + size * y)
        self.rect.bottomleft = (70 + size * (x), 70 + size * (y+1))

class Rook(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.color_type = color
        if self.color_type == "black":
            image_name = "rook_b.png"
        elif self.color_type == "white":
            image_name = "rook_w.png"
        else:
            raise ValueError("No color")

        self.image = pygame.image.load(os.path.join(img_folder, image_name)).convert()
        self.image = pygame.transform.scale(self.image, (game.return_arg("cell_size"), game.return_arg("cell_size")))
        if self.color_type == "black":
            self.image.set_colorkey((255, 255, 255))
        elif self.color_type == "white":
            self.image.set_colorkey((0, 0, 0))
        else:
            raise ValueError("No color")
        self.rect = self.image.get_rect()
    def load_unit(self, cell):
        size = game.return_arg("cell_size")
        x = cell[0]
        y = cell[1]
        self.rect.topleft = (70 + size * (x-1), 70 + size * y)
        self.rect.bottomleft = (70 + size * (x), 70 + size * (y+1))

class Cell:
    def __init__(self, position_x = 0, position_y = 0, piece_type = "None", color_type = "None"):
        self.position_x = position_x
        self.position_y = position_y
        self.piece_type = piece_type
        self.color_type = color_type

    def position(self):
        return (70 + self.position_x * game.return_arg("cell_size") +game.return_arg("cell_size")//3,
                70 + self.position_y * game.return_arg("cell_size") +game.return_arg("cell_size")//3)

    def highlite(self, type):
        self.type = type
        if type == "Attack":
            color = (255, 0, 0, 128)
        elif type == "Cell selection":
            color = (255, 255, 0, 128)
        pygame.draw.rect(game.return_arg("surface1"), color, (70 + self.position_x * game.return_arg("cell_size"),
            70 + self.position_y * game.return_arg("cell_size"), game.return_arg("cell_size"), game.return_arg("cell_size")))
        screen = game.return_arg("screen")
        screen.screen.blit(game.return_arg("surface1"), (0, 0) )

class Life:
    def __init__(self, width=200, height=400, cell_size=20, fps=5):
        self.width = width
        self.height = height - 59

        self.cell_size = cell_size
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        self.fps = fps

        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)

        self.surface1 = self.screen.convert_alpha()
        self.surface1.fill([0, 0, 0, 0])

        self.surface2 = pygame.display.set_mode(self.screen_size)

    def return_arg(self, name):

        if name == "surface1":
            return self.surface1
        elif name == "cell_size":
            return self.cell_size
        elif name == "screen":
            return self.screen
        elif name == "surface2":
            return self.surface2

    def make_board(self):
        numbers_list = ['8', '7', '6', '5', '4', '3', '2', '1']
        letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(self.screen, (207, 177, 157) if (x+y) % 2 == 0 else (128, 0, 0),
                                (70 + self.cell_size * x, 70 + self.cell_size * y, self.cell_size, self.cell_size))
        font = pygame.font.Font(None, 30)
        counter_x = 0
        for x in range(70, 71 + self.cell_size * 8, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 70), (x, 70 + self.cell_size * 8))
            try:
                text_1 = font.render(letters_list[counter_x], True, (0, 0, 0))
                text_2 = pygame.transform.flip(text_1, True, True)
            except IndexError:
                break
            text_1_pos = (x + self.cell_size // 3, 80 + self.cell_size * 8)
            text_2_pos = (x + self.cell_size // 3, 70 - self.cell_size // 1.5 )
            self.screen.blit(text_1, text_1_pos)
            self.screen.blit(text_2, text_2_pos)
            counter_x += 1
        counter_y = 0
        for y in range(70, 71 + self.cell_size * 8, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (70, y), (70 + self.cell_size * 8, y))
            try:
                text_1 = font.render(numbers_list[counter_y], True, (0, 0, 0))
                text_2 = pygame.transform.flip(text_1, True, True)
            except IndexError:
                break
            text_1_pos = (70 - self.cell_size // 1.5 , y + self.cell_size // 3)
            text_2_pos = (80 + self.cell_size * 8, y + self.cell_size // 3)
            self.screen.blit(text_1, text_1_pos)
            self.screen.blit(text_2, text_2_pos)
            counter_y += 1

    def make_units(self):
        for x in range(8):
            for y in range(8):
                if y == 1:
                    pawn = Pawn("black")
                    cell = Cell(x, y, "Pawn", "black")
                    Pawn.load_unit(pawn, (x, y))
                    self.all_sprites.add(pawn)
                elif y == 6:
                    pawn = Pawn("white")
                    cell = Cell(x, y, "Pawn", "white")
                    Pawn.load_unit(pawn, (x,y))
                    self.all_sprites.add(pawn)
                elif y == 0:
                    if x == 0 or x == 7:
                        rook = Rook("black")
                        cell = Cell(x, y, "Rook", "black")
                        Rook.load_unit(rook, (x, y))
                        self.all_sprites.add(rook)
                    if x == 1 or x == 6:
                        knight = Knight("black")
                        cell = Cell(x, y, "Knight", "black")
                        Knight.load_unit(knight, (x, y))
                        self.all_sprites.add(knight)
                    if x == 2 or x == 5:
                        bishop = Bishop("black")
                        cell = Cell(x, y, "Bishop", "black")
                        Bishop.load_unit(bishop, (x, y))
                        self.all_sprites.add(bishop)
                    if x == 3:
                        queen = Queen("black")
                        cell = Cell(x, y, "Queen", "black")
                        Queen.load_unit(queen, (x, y))
                        self.all_sprites.add(queen)
                    if x == 4:
                        king = King("black")
                        cell = Cell(x, y, "King", "black")
                        King.load_unit(king, (x, y))
                        self.all_sprites.add(king)
                elif y == 7:
                    if x == 0 or x == 7:
                        rook = Rook("white")
                        cell = Cell(x, y, "Rook", "white")
                        Rook.load_unit(rook, (x, y))
                        self.all_sprites.add(rook)
                    if x == 1 or x == 6:
                        knight = Knight("white")
                        cell = Cell(x, y, "Knight", "white")
                        Knight.load_unit(knight, (x, y))
                        self.all_sprites.add(knight)
                    if x == 2 or x == 5:
                        bishop = Bishop("white")
                        cell = Cell(x, y, "Bishop", "white")
                        Bishop.load_unit(bishop, (x, y))
                        self.all_sprites.add(bishop)
                    if x == 3:
                        queen = Queen("white")
                        cell = Cell(x, y, "Queen", "white")
                        Queen.load_unit(queen, (x, y))
                        self.all_sprites.add(queen)
                    if x == 4:
                        king = King("white")
                        cell = Cell(x, y, "King", "white")
                        King.load_unit(king, (x, y))
                        self.all_sprites.add(king)



    def run_game(self):
        pygame.init()
        #clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        pygame.display.set_caption('Chess')
        self.screen.fill(pygame.Color('white'))

        game = True
        while game:



            for event in pygame.event.get():
                if event.type == QUIT:
                    game = False

            self.all_sprites.update()

            self.make_board()
            self.make_units()
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            #clock.tick(self.fps)
        pygame.quit()

if __name__ == '__main__':
    game = Life(500, 500, 40, 5)
    game.run_game()
