import pygame
import os
from pygame.locals import *

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

class Chess():
    def __init__(self):
        pass

    def set_sprite(self, image_name, color):
        self.color_type = color
        self.image_name = image_name
        self.image = pygame.image.load(os.path.join(img_folder, self.image_name)).convert()
        self.image = pygame.transform.scale(self.image, (game.cell_size, game.cell_size))
        if self.color_type == "black":
            self.image.set_colorkey((0, 0, 0))
        elif self.color_type == "white":
            self.image.set_colorkey((0, 0, 0))
        else:
            raise ValueError("No color")
        self.rect = self.image.get_rect()
        return self.rect

    def load_unit(self, cell, rect):
        self.size = game.cell_size
        self.x = cell[0]
        self.y = cell[1]
        self.rect = rect
        self.rect.topleft = (70 + self.size * (self.x - 1), 70 + self.size * self.y)
        self.rect.bottomleft = (70 + self.size * (self.x), 70 + self.size * (self.y + 1))


class Pawn(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.description = color + " " + "Pawn"
        self.color_type = color
        if self.color_type == "black":
            self.image_name = "pawn_b.png"
        elif self.color_type == "white":
            self.image_name = "pawn_w.png"
        else: raise ValueError("No color")
        self.rect = Chess.set_sprite(self, self.image_name, self.color_type)

class Knight(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.description = color + " " + "Knight"
        self.color_type = color
        if self.color_type == "black":
            self.image_name = "knight_b.png"
        elif self.color_type == "white":
            self.image_name = "khight_w.png"
        else:
            raise ValueError("No color")
        self.rect = Chess.set_sprite(self, self.image_name, self.color_type)

class Queen(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.description = color + " " + "Queen"
        self.color_type = color
        if self.color_type == "black":
            self.image_name = "queen_b.png"
        elif self.color_type == "white":
            self.image_name = "queen_w.png"
        else:
            raise ValueError("No color")
        self.rect = Chess.set_sprite(self, self.image_name, self.color_type)

class King(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.description = color + " " + "King"
        self.color_type = color
        if self.color_type == "black":
            self.image_name = "king_b.png"
        elif self.color_type == "white":
            self.image_name = "king_w.png"
        else:
            raise ValueError("No color")
        self.rect = Chess.set_sprite(self, self.image_name, self.color_type)

class Bishop(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.description = color + " " + "Bishop"
        self.color_type = color
        if self.color_type == "black":
            self.image_name = "bishop_b.png"
        elif self.color_type == "white":
            self.image_name = "bishop_w.png"
        else:
            raise ValueError("No color")
        self.rect = Chess.set_sprite(self, self.image_name, self.color_type)

class Rook(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.description = color + " " + "Rook"
        self.color_type = color
        if self.color_type == "black":
            self.image_name = "rook_b.png"
        elif self.color_type == "white":
            self.image_name = "rook_w.png"
        else:
            raise ValueError("No color")
        self.rect = Chess.set_sprite(self, self.image_name, self.color_type)

class Cell:
    def __init__(self, position_x=0, position_y=0, piece="None", previous="None", state=None):
        self.position_x = position_x
        self.position_y = position_y
        self.piece = piece
        self.previous = previous
        self.state = state
        if self.piece != "None":
            self.desribtion = (str(self.position_x) + " " + str(self.position_y) + " " + self.piece.description)
        else: self.desribtion = (str(self.position_x) + " " + str(self.position_y) + " " + self.piece)

    def position(self):
        return (70 + self.position_x * game.cell_size + game.cell_size//3,
                70 + self.position_y * game.cell_size + game.cell_size//3)
    def update(self, new_piece):
        self.previous = self.piece
        if self.piece != "None":
            self.piece.kill()
        self.piece = new_piece
        Chess.load_unit(self, (self.position_x, self.position_y), self.piece.rect)

    def load_previous(self):
        if self.previous != "None":
            self.piece = self.previous
            self.previous = "None"
            Chess.load_unit(self, (self.position_x, self.position_y), self.piece.rect)
        else: print("Ошибка")

    def show_variants(self):
        def bishop():
            lst = list(range(0, 8))
            res = []
            d1 = 1
            while self.position_x + d1 in lst and self.position_y + d1 in lst:
                res += [[self.position_x + d1, self.position_y + d1]]
                d1 += 1
            d2 = 1
            while self.position_x + d2 in lst and self.position_y - d2 in lst:
                res += [[self.position_x + d2, self.position_y - d2]]
                d2 += 1
            d3 = 1
            while self.position_x - d3 in lst and self.position_y + d3 in lst:
                res += [[self.position_x - d3, self.position_y + d3]]
                d3 += 1
            d4 = 1
            while self.position_x - d4 in lst and self.position_y - d4 in lst:
                res += [[self.position_x - d4, self.position_y - d4]]
                d4 += 1
            return res

        if isinstance(self.piece, Pawn):
            selected_list = ([[self.position_x, self.position_y - 1],[self.position_x , self.position_y - 2]]
                    if self.piece.color_type == 'white' else
                    [[self.position_x, self.position_y + 1],[self.position_x, self.position_y + 2]])
        elif isinstance(self.piece, Knight):
            selected_list = [[self.position_x + 2, self.position_y - 1], [self.position_x + 2, self.position_y + 1],
                    [self.position_x - 2, self.position_y - 1], [self.position_x - 2, self.position_y + 1],
                    [self.position_x + 1, self.position_y + 2], [self.position_x - 1, self.position_y + 2],
                    [self.position_x + 1, self.position_y - 2], [self.position_x - 1, self.position_y - 2]]
        elif isinstance(self.piece, King):
            selected_list = [[self.position_x + 1, self.position_y], [self.position_x - 1, self.position_y],
                    [self.position_x, self.position_y - 1], [self.position_x, self.position_y + 1],
                    [self.position_x + 1, self.position_y + 1], [self.position_x - 1, self.position_y - 1],
                    [self.position_x + 1, self.position_y - 1], [self.position_x - 1, self.position_y + 1]]

        elif isinstance(self.piece, Queen):
            selected_list = [[i, self.position_y] for i in range(8)] + [[self.position_x, i] for i in range(8)]
            selected_list += bishop()

        elif isinstance(self.piece, Rook):
            selected_list = [[i, self.position_y] for i in range(8)] + [[self.position_x, i] for i in range(8)]

        elif isinstance(self.piece, Bishop):
            selected_list = bishop()

        #проверка выхода подсвеченных клеток за границы поля
        selected_list[:] = [i for i in selected_list if all(item in list(range(0, 8)) for item in i)]

        return selected_list


        '''if self.piece.color_type == 'black':
                return 'Yes'
            elif self.piece:
                return 'No'''''

    '''def highlite(self, type):
        self.type = type
        if type == "Attack":
            color = (255, 0, 0, 128)
        elif type == "Cell selection":
            color = (255, 255, 0, 128)
        pygame.draw.rect(game.surface1, color, (70 + self.position_x * game.cell_size,
            70 + self.position_y * game.cell_size, game.cell_size, game.cell_size))
        screen = game.screen
        screen.blit(game.surface1, (0, 0) )'''

    def delete(self):
        self.previous = self.piece
        self.piece == "None"

class CellList:
    def __init__(self, surface, cell_size, nrows, ncolumns):
        self.surface = surface
        self.cell_size = cell_size
        self.nrows = nrows
        self.ncolumns = ncolumns
        self.list = self.make()
    def make(self):
        cell_list = [[Cell(column * self.cell_size + 70, row * self.cell_size + 70)
                          for column in range(self.ncolumns)] for row in range(self.nrows)]
        return cell_list
    def draw(self):
        cell_list = self.list
        for row in range(len(cell_list)):
            for column in range(len(cell_list[row])):
                if cell_list[row][column].state == 'Selected' and cell_list[row][column].piece != 'None':
                    selected_list = cell_list[row][column].show_variants()
                    for i in selected_list:
                        pygame.draw.rect(self.surface, pygame.Color('green'), (i[0] * self.cell_size + 71, i[1] * self.cell_size + 71,
                                                                               self.cell_size - 1, self.cell_size - 1))

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
        self.cell_table = CellList(self.surface1, self.cell_size, 8, 8)
        self.surface2 = pygame.display.set_mode(self.screen_size)

    def make_board(self):
        numbers_list = ['8', '7', '6', '5', '4', '3', '2', '1']
        letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        #self.cell_table = []
        #self.cell_list = []
        for x in range(8):
            for y in range(8):
                #self.cell_list.append(Cell(x, y))
                pygame.draw.rect(self.screen, (207, 177, 157) if (x+y) % 2 == 0 else (128, 0, 0),
                                (70 + self.cell_size * x, 70 + self.cell_size * y, self.cell_size, self.cell_size))
            #self.cell_table.append(self.cell_list)
            #self.cell_list=[]
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
                    pawn = Pawn('black')
                    self.cell_table.list[x][y] = Cell(x, y, pawn)
                    Chess.load_unit(self, (x, y), pawn.rect)
                    self.all_sprites.add(pawn)
                elif y == 6:
                    pawn = Pawn("white")
                    self.cell_table.list[x][y] = Cell(x, y, pawn)
                    Chess.load_unit(self, (x, y), pawn.rect)
                    self.all_sprites.add(pawn)
                elif y == 0:
                    if x == 0 or x == 7:
                        rook = Rook("black")
                        self.cell_table.list[x][y] = Cell(x, y, rook)
                        Chess.load_unit(self, (x, y), rook.rect)
                        self.all_sprites.add(rook)
                    if x == 1 or x == 6:
                        knight = Knight("black")
                        self.cell_table.list[x][y] = Cell(x, y, knight)
                        Chess.load_unit(self, (x, y), knight.rect)
                        self.all_sprites.add(knight)
                    if x == 2 or x == 5:
                        bishop = Bishop("black")
                        self.cell_table.list[x][y] = Cell(x, y, bishop)
                        Chess.load_unit(self, (x, y), bishop.rect)
                        self.all_sprites.add(bishop)
                    if x == 3:
                        queen = Queen("black")
                        self.cell_table.list[x][y] = Cell(x, y, queen)
                        Chess.load_unit(self, (x, y), queen.rect)
                        self.all_sprites.add(queen)
                    if x == 4:
                        king = King("black")
                        self.cell_table.list[x][y] = Cell(x, y, king)
                        Chess.load_unit(self, (x, y), king.rect)
                        self.all_sprites.add(king)
                elif y == 7:
                    if x == 0 or x == 7:
                        rook = Rook("white")
                        self.cell_table.list[x][y] = Cell(x, y, rook)
                        Chess.load_unit(self, (x, y), rook.rect)
                        self.all_sprites.add(rook)
                    if x == 1 or x == 6:
                        knight = Knight("white")
                        self.cell_table.list[x][y] = Cell(x, y, knight)
                        Chess.load_unit(self, (x, y), knight.rect)
                        self.all_sprites.add(knight)
                    if x == 2 or x == 5:
                        bishop = Bishop("white")
                        self.cell_table.list[x][y] = Cell(x, y, bishop)
                        Chess.load_unit(self, (x, y), bishop.rect)
                        self.all_sprites.add(bishop)
                    if x == 3:
                        queen = Queen("white")
                        self.cell_table.list[x][y] = Cell(x, y, queen)
                        Chess.load_unit(self, (x, y), queen.rect)
                        self.all_sprites.add(queen)
                    if x == 4:
                        king = King("white")
                        self.cell_table.list[x][y] = Cell(x, y, king)
                        Chess.load_unit(self, (x, y), king.rect)
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
                elif event.type == MOUSEBUTTONDOWN:
                    x_pos = (pygame.mouse.get_pos()[0] - 70) // self.cell_size
                    y_pos = (pygame.mouse.get_pos()[1] - 70) // self.cell_size

                    self.cell_table.list[x_pos][y_pos].state = 'Selected'

            self.all_sprites.update()
            self.make_board()
            self.cell_table.draw()
            self.screen.blit(self.surface1, (0, 0))
            self.make_units()
            self.all_sprites.draw(self.screen)

            pygame.display.flip()
            #clock.tick(self.fps)
        pygame.quit()

if __name__ == '__main__':
    game = Life(500, 500, 40, 5)
    game.run_game()
