import pygame
import sys
import os
from pygame.locals import *

# определение файловой директории для изображений
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')


# класс с общими для всех фигур функциями
class Chess():
    def __init__(self):
        pass

    # функция загрузки спрайта изображения
    def set_sprite(self, image_name, color):
        self.color_type = color
        self.image_name = image_name
        self.image = pygame.image.load(os.path.join(img_folder, self.image_name)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (game.cell_size, game.cell_size))
        self.rect = self.image.get_rect()
        return self.rect

    # функция загрузки изображения фигуры на поле
    def load_unit(self, cell, rect):
        self.size = game.cell_size
        self.x = cell[0]
        self.y = cell[1]
        self.rect = rect
        self.rect.topleft = (70 + self.size * (self.x - 1), 70 + self.size * self.y)
        self.rect.bottomleft = (70 + self.size * (self.x), 70 + self.size * (self.y + 1))


# классы отдельных фигур (определение изображения и создания обьекта изображения)
class Pawn(pygame.sprite.Sprite):
    def __init__(self, color, ch=None):
        pygame.sprite.Sprite.__init__(self)
        self.ch = ch
        self.description = color + " " + "Pawn"
        self.color_type = color

        if self.color_type == "black":
            self.image_name = "pawn_b.png"
        elif self.color_type == "white":
            self.image_name = "pawn_w.png"
        else:
            raise ValueError("No color")
        self.rect = Chess.set_sprite(self, self.image_name, self.color_type)
        self.previous_move = None

class Pawn_2(pygame.sprite.Sprite):
    def __init__(self, color, ch=None):
        pygame.sprite.Sprite.__init__(self)
        self.ch = ch
        self.description = color + " " + "Pawn"
        self.color_type = color

        if self.color_type == "black":
            self.image_name = "pawn_b_2.png"
        elif self.color_type == "white":
            self.image_name = "pawn_w_2.png"
        else:
            raise ValueError("No color")
        self.rect = Chess.set_sprite(self, self.image_name, self.color_type)
        self.previous_move = None

class Pawn_3(pygame.sprite.Sprite):
    def __init__(self, color, ch=None):
        pygame.sprite.Sprite.__init__(self)
        self.ch = ch
        self.description = color + " " + "Pawn"
        self.color_type = color

        if self.color_type == "black":
            self.image_name = "pawn_b_3.png"
        elif self.color_type == "white":
            self.image_name = "pawn_w_3.png"
        else:
            raise ValueError("No color")
        self.rect = Chess.set_sprite(self, self.image_name, self.color_type)
        self.previous_move = None

class Pawn_4(pygame.sprite.Sprite):
    def __init__(self, color, ch=None):
        pygame.sprite.Sprite.__init__(self)
        self.ch = ch
        self.description = color + " " + "Pawn"
        self.color_type = color

        if self.color_type == "black":
            self.image_name = "pawn_b_4.png"
        elif self.color_type == "white":
            self.image_name = "pawn_w_4.png"
        else:
            raise ValueError("No color")
        self.rect = Chess.set_sprite(self, self.image_name, self.color_type)
        self.previous_move = None

class Knight(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.description = color + " " + "Knight"
        self.color_type = color
        if self.color_type == "black":
            self.image_name = "knight_b.png"
        elif self.color_type == "white":
            self.image_name = "knight_w.png"
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


# класс отдельных ячеек с текцщим состоянием и хранением в памяти двух фигур (текущей и предыдущей)
class Cell:
    def __init__(self, position_x=0, position_y=0, piece="None", state=None, previous="None", state_piece=None, state_check=None):
        self.position_x = position_x
        self.position_y = position_y
        self.piece = piece
        self.previous = previous
        self.state = state
        self.state_check = state_check
        self.state_piece = state_piece
        # if self.piece != "None":
        # self.desribtion = (str(self.position_x) + " " + str(self.position_y) + " " + self.piece.description)
        # else: self.desribtion = (str(self.position_x) + " " + str(self.position_y) + " " + self.piece)

    # возвращает позицию клетки
    def position(self):
        return (70 + self.position_x * game.cell_size + game.cell_size // 3,
                70 + self.position_y * game.cell_size + game.cell_size // 3)

    # def update(self, new_piece):
    # self.previous = self.piece
    # self.piece = new_piece
    # Chess.load_unit(self, (self.position_x, self.position_y), self.piece.rect)

    # def load_previous(self):
    # if self.previous != "None":
    # self.piece = self.previous
    # self.previous = "None"
    # Chess.load_unit(self, (self.position_x, self.position_y), self.piece.rect)
    # else: print("Ошибка")

    # функция, определяющая возможные ходы для фигуры
    def show_variants(self, current_list):
        def calc(res, x=0, y=0):
            d1 = 1
            lst = list(range(0, 8))
            while self.position_x + (d1 * x) in lst and self.position_y + (d1 * y) in lst and \
                    current_list[self.position_x + (d1 * x)][
                        self.position_y + (d1 * y)].piece == "None":
                res += [[self.position_x + d1 * x, self.position_y + (d1 * y)]]
                d1 += 1
            else:
                try:
                    if current_list[self.position_x + (d1 * x)][
                        self.position_y + (d1 * y)].piece.color_type != self.piece.color_type:
                        res += [[self.position_x + (d1 * x), self.position_y + (d1 * y)]]
                except (IndexError, AttributeError):
                    pass
            return res

        # подфункция для ходов слона
        def bishop():
            res = []
            res = calc(res, x=1, y=1)
            res = calc(res, x=1, y=-1)
            res = calc(res, x=-1, y=1)
            res = calc(res, x=-1, y=-1)
            return res

        # подфунцкия для ходов ладьи
        def rook():
            res = []
            res = calc(res, x=1, y=0)
            res = calc(res, x=-1, y=0)
            res = calc(res, x=0, y=1)
            res = calc(res, x=0, y=-1)

            return res

        def pawn_attack(x,y):
            try:
                lst = ([[self.position_x + x, self.position_y + y]] if
                       current_list[self.position_x + x][self.position_y + y].piece.color_type != self.piece.color_type else [])
            except Exception:
                lst = []
            # Проверка на взятие на проходе
            try:
                if type(current_list[self.position_x + x][self.position_y].piece) == Pawn and \
                        current_list[self.position_x + x][self.position_y].piece.color_type != self.piece.color_type and \
                        current_list[self.position_x + x][self.position_y].piece.previous_move == 2:
                    lst += [[self.position_x + x, self.position_y + y]]
            except Exception:
                pass
            return lst


        if isinstance(self.piece, Pawn):
            if (self.position_y == 1 and self.piece.color_type == "black" and
                current_list[self.position_x][self.position_y + 1].piece == "None") or (
                    self.position_y == 6 and self.piece.color_type == "white" and
                    current_list[self.position_x][self.position_y - 1].piece == "None"):
                selected_list = ([[self.position_x, self.position_y - 1], [self.position_x, self.position_y - 2]]
                                 if self.piece.color_type == 'white' else
                                 [[self.position_x, self.position_y + 1], [self.position_x, self.position_y + 2]])
            else:
                selected_list = ([[self.position_x, self.position_y - 1]]
                                 if self.piece.color_type == 'white' else
                                 [[self.position_x, self.position_y + 1]])

            for i in reversed(selected_list):
                if current_list[i[0]][i[1]].piece != "None":
                    selected_list.remove(i)

            if self.piece.color_type == "white":
                selected_list += pawn_attack(1, -1)
                selected_list += pawn_attack(-1, -1)
            elif self.piece.color_type == "black":
                selected_list += pawn_attack(1, 1)
                selected_list += pawn_attack(-1, 1)

        if isinstance(self.piece, Pawn_2):
            if (self.position_y == 1 and self.piece.color_type == "black" and
                current_list[self.position_x][self.position_y + 1].piece == "None") or (
                    self.position_y == 6 and self.piece.color_type == "white" and
                    current_list[self.position_x][self.position_y - 1].piece == "None"):
                selected_list = ([[self.position_x, self.position_y - 1], [self.position_x, self.position_y - 2]]
                                 if self.piece.color_type == 'white' else
                                 [[self.position_x, self.position_y + 1], [self.position_x, self.position_y + 2]])
            else:
                selected_list = ([[self.position_x, self.position_y - 1]]
                                 if self.piece.color_type == 'white' else
                                 [[self.position_x, self.position_y + 1]])

            for i in reversed(selected_list):
                if current_list[i[0]][i[1]].piece != "None":
                    selected_list.remove(i)

            if self.piece.color_type == "white":
                selected_list += pawn_attack(1, -1)
                selected_list += pawn_attack(-1, -1)
            elif self.piece.color_type == "black":
                selected_list += pawn_attack(1, 1)
                selected_list += pawn_attack(-1, 1)

        if isinstance(self.piece, Pawn_3):
            if (self.position_y == 1 and self.piece.color_type == "black" and
                current_list[self.position_x][self.position_y + 1].piece == "None") or (
                    self.position_y == 6 and self.piece.color_type == "white" and
                    current_list[self.position_x][self.position_y - 1].piece == "None"):
                selected_list = ([[self.position_x, self.position_y - 1], [self.position_x, self.position_y - 2]]
                                 if self.piece.color_type == 'white' else
                                 [[self.position_x, self.position_y + 1], [self.position_x, self.position_y + 2]])
            else:
                selected_list = ([[self.position_x, self.position_y - 1]]
                                 if self.piece.color_type == 'white' else
                                 [[self.position_x, self.position_y + 1]])

            for i in reversed(selected_list):
                if current_list[i[0]][i[1]].piece != "None":
                    selected_list.remove(i)

            if self.piece.color_type == "white":
                selected_list += pawn_attack(1, -1)
                selected_list += pawn_attack(-1, -1)
            elif self.piece.color_type == "black":
                selected_list += pawn_attack(1, 1)
                selected_list += pawn_attack(-1, 1)

        if isinstance(self.piece, Pawn_4):
            if (self.position_y == 1 and self.piece.color_type == "black" and
                current_list[self.position_x][self.position_y + 1].piece == "None") or (
                    self.position_y == 6 and self.piece.color_type == "white" and
                    current_list[self.position_x][self.position_y - 1].piece == "None"):
                selected_list = ([[self.position_x, self.position_y - 1], [self.position_x, self.position_y - 2]]
                                 if self.piece.color_type == 'white' else
                                 [[self.position_x, self.position_y + 1], [self.position_x, self.position_y + 2]])
            else:
                selected_list = ([[self.position_x, self.position_y - 1]]
                                 if self.piece.color_type == 'white' else
                                 [[self.position_x, self.position_y + 1]])

            for i in reversed(selected_list):
                if current_list[i[0]][i[1]].piece != "None":
                    selected_list.remove(i)

            if self.piece.color_type == "white":
                selected_list += pawn_attack(1, -1)
                selected_list += pawn_attack(-1, -1)
            elif self.piece.color_type == "black":
                selected_list += pawn_attack(1, 1)
                selected_list += pawn_attack(-1, 1)

        if isinstance(self.piece, Pawn):
            if (self.position_y == 1 and self.piece.color_type == "black" and
                current_list[self.position_x][self.position_y + 1].piece == "None") or (
                    self.position_y == 6 and self.piece.color_type == "white" and
                    current_list[self.position_x][self.position_y - 1].piece == "None"):
                selected_list = ([[self.position_x, self.position_y - 1], [self.position_x, self.position_y - 2]]
                                 if self.piece.color_type == 'white' else
                                 [[self.position_x, self.position_y + 1], [self.position_x, self.position_y + 2]])
            else:
                selected_list = ([[self.position_x, self.position_y - 1]]
                                 if self.piece.color_type == 'white' else
                                 [[self.position_x, self.position_y + 1]])

            for i in reversed(selected_list):
                if current_list[i[0]][i[1]].piece != "None":
                    selected_list.remove(i)

            if self.piece.color_type == "white":
                selected_list += pawn_attack(1, -1)
                selected_list += pawn_attack(-1, -1)
            elif self.piece.color_type == "black":
                selected_list += pawn_attack(1, 1)
                selected_list += pawn_attack(-1, 1)

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
            selected_list = rook()
            selected_list += bishop()

        elif isinstance(self.piece, Rook):
            selected_list = rook()

        elif isinstance(self.piece, Bishop):
            selected_list = bishop()

        # проверка выхода подсвеченных клеток за границы поля
        selected_list[:] = [i for i in selected_list if (all(item in list(range(0, 8)) for item in i))]
        # проверка на заполнение клеток с фигурами того же цвета
        for i in reversed(selected_list):
            try:
                if current_list[i[0]][i[1]].piece.color_type == self.piece.color_type:
                    selected_list.remove(i)
            except AttributeError:
                pass

        return selected_list

    # def delete(self):
    # self.previous = self.piece
    # self.piece == "None"


# класс списка всех ячеек
class CellList:
    def __init__(self, surface, cell_size, nrows, ncolumns):
        self.surface = surface
        self.cell_size = cell_size
        self.nrows = nrows
        self.ncolumns = ncolumns
        self.list = self.make()
        self.check = None

    def make(self):
        cell_list = [[Cell(column * self.cell_size + 70, row * self.cell_size + 70)
                      for column in range(self.ncolumns)] for row in range(self.nrows)]
        return cell_list

    # функция закрашивания клеток возможного хода
    def draw(self):
        cell_list = self.list
        for row in range(len(cell_list)):
            for column in range(len(cell_list[row])):
                if cell_list[row][column].state == 'Selected' and cell_list[row][column].piece != 'None':
                    selected_list = cell_list[row][column].show_variants(cell_list)
                    for i in selected_list:
                        cell_list[i[0]][i[1]], cell_list[row][column] = cell_list[row][column], cell_list[i[0]][i[1]]
                        if cell_list[i[0]][i[1]].piece != "None":
                            new_cel = Cell()
                            cell_list[row][column], new_cel = new_cel, cell_list[row][column]
                        d = self.chess_check(cell_list, get_color=True)
                        if cell_list[i[0]][i[1]].piece != "None":
                            cell_list[row][column], new_cel = new_cel, cell_list[row][column]
                        cell_list[i[0]][i[1]], cell_list[row][column] = cell_list[row][column], cell_list[i[0]][i[1]]
                        if not(d[0]) or (d[0] and cell_list[row][column].piece.color_type != d[1]):
                            pygame.draw.rect(self.surface, (161, 211, 134) if (i[0] + i[1]) % 2 == 0 else (24, 63, 33),
                                             (i[0] * self.cell_size + 71, i[1] * self.cell_size + 71,
                                              self.cell_size - 1, self.cell_size - 1))
                        else:
                            cell_list[i[0]][i[1]].state = None
                if cell_list[row][column].state == 'Unselected' and cell_list[row][column].piece != 'None':
                    unselected_list = cell_list[row][column].show_variants(cell_list)
                    for i in unselected_list:
                        pygame.draw.rect(self.surface, (192, 192, 192) if (i[0] + i[1]) % 2 == 0 else (21, 34, 45),
                                         (i[0] * self.cell_size + 71, i[1] * self.cell_size + 71,
                                          self.cell_size - 1, self.cell_size - 1))
                    cell_list[row][column].state = None
                if cell_list[row][column].state == 'Unselected' and cell_list[row][column].piece == 'None':
                    cell_list[row][column].state = None

    #функция проверки шаха
    def chess_check(self, cell_list, draw=False, get_color=False):
        color = None
        W = False
        #cell_list = self.list
        for row in range(len(cell_list)):
            for column in range(len(cell_list[row])):
                if cell_list[row][column].piece != 'None':
                    selected_list = cell_list[row][column].show_variants(cell_list)
                    for i in selected_list:
                        if type(cell_list[i[0]][i[1]].piece) == King:
                            if draw:
                                cell_list[i[0]][i[1]].state_check = "Check"
                                cell_list[row][column].state_check = "Check"
                                self.check = cell_list[i[0]][i[1]].piece.color_type
                            if get_color:
                                color = cell_list[i[0]][i[1]].piece.color_type
                            W = True
        if get_color:
            return (W, color)
        else:
            return W

    # функция закрашивания клеток в случае шаха
    def draw_check(self):
        cell_list = self.list
        for row in range(len(cell_list)):
            for column in range(len(cell_list[row])):
                if cell_list[row][column].state_check == 'Delete':
                    pygame.draw.rect(self.surface, (192, 192, 192) if (row + column) % 2 == 0 else (21, 34, 45),
                                     (row *
                                      self.cell_size + 71, column * self.cell_size + 71,
                                      self.cell_size - 1, self.cell_size - 1))
                    cell_list[row][column].state_check = None

                if cell_list[row][column].state_check == 'Check':
                    pygame.draw.rect(self.surface, (250, 158, 124) if (row + column) % 2 == 0 else (102, 21, 23),
                                     (row * self.cell_size + 71, column * self.cell_size + 71,
                                      self.cell_size - 1, self.cell_size - 1))
                    cell_list[row][column].state_check = 'Delete'

    # функция проверки возможности хода и самого хода
    def check_and_move(self, piece, now):
        self.x_pr = piece[0]
        self.y_pr = piece[1]
        self.x_n = now[0]
        self.y_n = now[1]
        self.pawn_choose = False
        cell_list = self.list
        self.move_not = True

        for row in range(len(cell_list)):
            for column in range(len(cell_list[row])):
                if cell_list[row][column].state == 'Move' and cell_list[self.x_pr][self.y_pr].piece != 'None':
                    selected_list = cell_list[self.x_pr][self.y_pr].show_variants(cell_list)
                    for i in selected_list[:]:
                        cell_list[i[0]][i[1]], cell_list[row][column] = cell_list[row][column], cell_list[i[0]][i[1]]
                        if cell_list[i[0]][i[1]].piece != "None":
                            new_cel = Cell()
                            cell_list[row][column], new_cel = new_cel, cell_list[row][column]
                        d = self.chess_check(cell_list, get_color=True)
                        if cell_list[i[0]][i[1]].piece != "None":
                            cell_list[row][column], new_cel = new_cel, cell_list[row][column]
                        cell_list[i[0]][i[1]], cell_list[row][column] = cell_list[row][column], cell_list[i[0]][i[1]]
                        if (d[0]) and not(d[0] and cell_list[row][column].piece.color_type != d[1]):
                            selected_list.remove(i)

                    for i in selected_list:
                        # если ход возможен, фигура ходит
                        if i[0] == self.x_n and i[1] == self.y_n:

                            # уничтожение атакованной фигуры
                            if cell_list[self.x_n][self.y_n].piece != 'None':
                                cell_list[self.x_n][self.y_n].piece.kill()
                            # взятие на проходе
                            if type(cell_list[self.x_pr][self.y_pr].piece) == Pawn and \
                                    cell_list[self.x_n][self.y_n].piece == 'None' and \
                                    (self.x_n != self.x_pr):
                                cell_list[self.x_n][self.y_pr].piece.kill()
                                cell_list[self.x_n][self.y_pr] = Cell(self.x_n, self.y_pr, 'None', 'Unselected')

                            Chess.load_unit(self, (self.x_n, self.y_n), cell_list[self.x_pr][self.y_pr].piece.rect)
                            cell_list[self.x_n][self.y_n] = Cell(self.x_n, self.y_n,
                                                                 cell_list[self.x_pr][self.y_pr].piece, 'Unselected')
                            self.move_not = False
                            if type(cell_list[self.x_n][self.y_n].piece == Pawn):
                                #Запоминание на сколько клеток сделала пешка ход (для взятия на проходе)
                                self.list[self.x_n][self.y_n].piece.previous_move = abs(self.y_n - self.y_pr)
                                if (self.y_n == 0 or self.y_n == 7):
                                    cell_list[self.x_n][self.y_n].piece.ch = (self.x_n, self.y_n)

                            return True
                    # если ход не возможен, убирается выделение клеток
                    if self.move_not:
                        cell_list[self.x_pr][self.y_pr].state = 'Unselected'
                        return False

                if cell_list[row][column].state == 'Move' and cell_list[self.x_pr][self.y_pr].piece == 'None':
                    return False

    # функция удаления выделения для клетки, в которой находится фигура
    def undraw_now(self, x, y):
        i = (x, y)
        pygame.draw.rect(self.surface, (192, 192, 192) if (i[0] + i[1]) % 2 == 0 else (21, 34, 45),
                         (i[0] * self.cell_size + 71, i[1] * self.cell_size + 71,
                          self.cell_size - 1, self.cell_size - 1))


# класс игры
class Life:
    def __init__(self, width=200, height=400, cell_size=20, fps=5):
        # определение размеров и игровых поверхностей
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
        # создание списка ячеек
        self.cell_table = CellList(self.surface1, self.cell_size, 8, 8)
        self.surface2 = pygame.display.set_mode(self.screen_size)

    # функция прорисовки линий внутри поля
    def make_lines(self):

        for x in range(70, 71 + self.cell_size * 8, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 70), (x, 70 + self.cell_size * 8), 4)

        for y in range(70, 71 + self.cell_size * 8, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (70, y), (70 + self.cell_size * 8, y), 4)


    # функция создания клеток доски
    def make_board(self, number_of_moves):
        numbers_list = ['8', '7', '6', '5', '4', '3', '2', '1']
        letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        # self.cell_table = []
        # self.cell_list = []
        self.number_of_moves_def = number_of_moves //2
        for x in range(8):
            for y in range(8):
                # self.cell_list.append(Cell(x, y))
                pygame.draw.rect(self.screen, (192, 192, 192) if (x + y) % 2 == 0 else (21, 34, 45),
                                 (70 + self.cell_size * x, 70 + self.cell_size * y, self.cell_size, self.cell_size))
            # self.cell_table.append(self.cell_list)
            # self.cell_list=[]
        # добавление текста
        pygame.font.init()
        font = pygame.font.Font('GorgeousPixel.ttf', 30)
        counter_x = 0
        for x in range(70, 71 + self.cell_size * 8, self.cell_size):
            try:
                text_1 = font.render(letters_list[counter_x], True, (0, 0, 0))
                text_2 = pygame.transform.flip(text_1, True, True)
            except IndexError:
                break
            text_1_pos = (x + self.cell_size // 2.55, 79 + self.cell_size * 8)
            text_2_pos = (x + self.cell_size // 2.55, 70 - self.cell_size // 1.6)
            self.screen.blit(text_1, text_1_pos)
            self.screen.blit(text_2, text_2_pos)
            counter_x += 1
        counter_y = 0
        for y in range(70, 71 + self.cell_size * 8, self.cell_size):
            try:
                text_1 = font.render(numbers_list[counter_y], True, (0, 0, 0))
                text_2 = pygame.transform.flip(text_1, True, True)
            except IndexError:
                break
            text_1_pos = (70 - self.cell_size // 1.6, y + self.cell_size // 3.7)
            text_2_pos = (97 + self.cell_size * 8, y + self.cell_size // 3.7)
            self.screen.blit(text_1, text_1_pos)
            self.screen.blit(text_2, text_2_pos)
            counter_y += 1
        # добавление кнопок опций
        if number_of_moves == 0:
            options = ['new_game.png', 'new_pieces.png']
            for name in options:
                option_img = pygame.image.load(os.path.join(img_folder, name)).convert_alpha()
                option_img = pygame.transform.scale(option_img, (game.cell_size // 1.2, game.cell_size // 1.2))
                option_rect = option_img.get_rect()
                if name == 'new_game.png':
                    option_rect.topleft = (6, 8)
                elif name == 'new_pieces.png':
                    option_rect.topleft = (self.width - 2 - game.cell_size // 1.2, 8)
                self.screen.blit(option_img, option_rect)

        else:
            options = ['new_game.png', 'new_pieces_na.png']
            for name in options:


                option_img = pygame.image.load(os.path.join(img_folder, name)).convert_alpha()
                option_img = pygame.transform.scale(option_img, (game.cell_size // 1.2, game.cell_size // 1.2))
                option_rect = option_img.get_rect()

                pygame.draw.rect(self.screen, (121, 121, 121),(self.width - 9 - game.cell_size // 1.2, 0, self.cell_size, self.cell_size))

                if name == 'new_game.png':
                    option_rect.topleft = (6, 8)
                elif name == 'new_pieces_na.png':
                    option_rect.topleft = (self.width - 2 - game.cell_size // 1.2, 8)
                self.screen.blit(option_img, option_rect)
        #обновление количества ходов
        number_txt = str(self.number_of_moves_def)
        text_number = font.render(number_txt, True, (255, 255, 255))
        if self.number_of_moves_def < 10:
            text_number_pos = (70 - self.cell_size // 1.6, 79 + self.cell_size * 8)
        elif 10 <= self.number_of_moves_def < 100:
            text_number_pos = (70 - self.cell_size // 1.47, 79 + self.cell_size * 8)
        elif self.number_of_moves_def >= 100:
            text_number_pos = (70 - self.cell_size // 1.25, 79 + self.cell_size * 8)
        pygame.draw.rect(self.screen, (121, 121, 121),
                         (70 - self.cell_size // 1.6,
                          79 + self.cell_size * 8, self.cell_size,
                          self.cell_size), )
        self.screen.blit(text_number, text_number_pos)




    # функция проверки пешки на краю доски
    def choose(self):
        W = False
        for piece in self.all_sprites:
            if type(piece) == Pawn:
                if piece.ch != None:
                    self.color = piece.color_type
                    pygame.draw.rect(self.screen, (121, 121, 121),
                                     (self.width // 2 - 2 * self.cell_size + 1,
                                      self.height // 2 - 0.48 * self.cell_size - 5, self.cell_size * 4,
                                      self.cell_size * 2))
                    pygame.draw.rect(self.screen, (0, 0, 0),
                                     (self.width // 2 - 2 * self.cell_size + 1,
                                      self.height // 2 - 0.48 * self.cell_size - 5,
                                      self.cell_size * 4, self.cell_size * 2), 4)
                    pygame.font.init()
                    font = pygame.font.Font('GorgeousPixel.ttf', 60)
                    text_choose = 'Choose:'
                    text_chose_f = font.render(text_choose, True, (0, 0, 0))
                    text_choose_pos = (self.width // 2 - self.cell_size * 1.5, self.height // 2 - self.cell_size * 0.5)
                    self.screen.blit(text_chose_f, text_choose_pos)
                    if self.color == 'black':
                        options = ['queen_b.png', 'bishop_b.png', 'rook_b.png', 'knight_b.png']
                    else:
                        options = ['queen_w.png', 'bishop_w.png', 'rook_w.png', 'knight_w.png']
                    i = 2
                    for name in options:
                        option_img = pygame.image.load(os.path.join(img_folder, name)).convert_alpha()
                        option_img = pygame.transform.scale(option_img, (self.cell_size, self.cell_size))
                        option_rect = option_img.get_rect()
                        option_rect.bottomleft = (
                            self.width // 2 - i * self.cell_size, self.height // 2 + self.cell_size * 1.35)
                        self.screen.blit(option_img, option_rect)
                        i -= 1
                    W = piece
        return W

    def new_items(self):
        self.color = 'white' if self.number_of_moves % 2 == 0 else 'black'

        pygame.draw.rect(self.screen, (121, 121, 121),
                         (self.width // 2 - 2 * self.cell_size + 1,
                          self.height // 2 - 0.48 * self.cell_size - 5, self.cell_size * 4,
                          self.cell_size * 2))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (self.width // 2 - 2 * self.cell_size + 1,
                          self.height // 2 - 0.48 * self.cell_size - 5,
                          self.cell_size * 4, self.cell_size * 2), 4)
        pygame.font.init()
        font = pygame.font.Font('GorgeousPixel.ttf', 60)
        text_choose = 'Pawns:'
        text_chose_f = font.render(text_choose, True, (0, 0, 0))
        text_choose_pos = (self.width // 2 - self.cell_size * 1.5, self.height // 2 - self.cell_size * 0.5)
        self.screen.blit(text_chose_f, text_choose_pos)
        if self.color == 'black':
            options = ['pawn_b.png', 'pawn_b_2.png', 'pawn_b_3.png', 'pawn_b_4.png']
        else:
            options = ['pawn_w.png', 'pawn_w_2.png', 'pawn_w_3.png', 'pawn_w_4.png']
        i = 2
        for name in options:
            option_img = pygame.image.load(os.path.join(img_folder, name)).convert_alpha()
            option_img = pygame.transform.scale(option_img, (self.cell_size, self.cell_size))
            option_rect = option_img.get_rect()
            option_rect.bottomleft = (
                self.width // 2 - i * self.cell_size, self.height // 2 + self.cell_size * 1.35)
            self.screen.blit(option_img, option_rect)
            i -= 1

    # функция первоначального размещения фигур на доске
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


    # запуск иггры
    def run_game(self):
        pygame.init()
        new = False
        Touch = False
        # clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        pygame.display.set_caption('Chess')
        self.screen.fill((121, 121, 121))
        press_key = (None, None)
        game = True
        pawn_choose = False
        self.number_of_moves = 0
        self.make_units()
        mouse_click = True
        turn = "white"
        while game:
            # обработка нажатий мышкой в игре
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_click = True
                    x_pos = (pygame.mouse.get_pos()[0] - 70) // self.cell_size
                    y_pos = (pygame.mouse.get_pos()[1] - 70) // self.cell_size

                    # выбор фигуры для пешки на краю доски
                    if self.choose():
                        piece = self.choose()
                        new_piece = None
                        if y_pos == 4:
                            if x_pos == 2:
                                new_piece = Queen(self.color)
                            if x_pos == 3:
                                new_piece = Bishop(self.color)
                            if x_pos == 4:
                                new_piece = Rook(self.color)
                            if x_pos == 5:
                                new_piece = Knight(self.color)
                        if new_piece != None:
                            self.cell_table.list[piece.ch[0]][piece.ch[1]] = Cell(piece.ch[0], piece.ch[1], new_piece)
                            Chess.load_unit(self, piece.ch, new_piece.rect)
                            piece.kill()
                            self.all_sprites.add(new_piece)

                    if x_pos == 8 and y_pos == -1 and self.number_of_moves == 0 and press_key == (None, None):
                        Touch = True

                    else:
                        if Touch:
                            if 2 <= x_pos <= 5 and y_pos == 4:
                                new_piece_b = None
                                new_piece_w = None
                                for x in range(8):
                                    if x_pos == 2:
                                        new_piece_b = Pawn('black')
                                        new_piece_w = Pawn('white')
                                    if x_pos == 3:
                                        new_piece_b = Pawn_2('black')
                                        new_piece_w = Pawn_2('white')
                                    if x_pos == 4:
                                        new_piece_b = Pawn_3('black')
                                        new_piece_w = Pawn_3('white')
                                    if x_pos == 5:
                                        new_piece_b = Pawn_4('black')
                                        new_piece_w = Pawn_4('white')


                                    self.cell_table.list[x][1].piece.kill()
                                    self.cell_table.list[x][1] = Cell(x, 1, new_piece_b)

                                    Chess.load_unit(self, (x, 1), new_piece_b.rect)

                                    self.all_sprites.add(new_piece_b)

                                    self.cell_table.list[x][6].piece.kill()
                                    self.cell_table.list[x][6] = Cell(x, 6, new_piece_w)
                                    Chess.load_unit(self, (x, 6), new_piece_w.rect)

                                    self.all_sprites.add(new_piece_w)

                                    new_piece_b = None
                                    new_piece_w = None

                                    Touch = False
                                    press_key = (None, None)
                            else:
                                pass

                        # нажатия на клетки поля
                        elif 0 <= x_pos <= 7 and 0 <= y_pos <= 7:
                            if press_key[0] == x_pos and press_key[1] == y_pos:

                                self.cell_table.list[x_pos][y_pos].state = 'Unselected'
                                press_key = (None, None)

                            else:

                                if press_key != (None, None):

                                    self.cell_table.undraw_now(press_key[0], press_key[1])

                                    self.cell_table.list[press_key[0]][press_key[1]].state = 'Move'
                                    if (self.cell_table.check_and_move(press_key, (x_pos, y_pos))):
                                        self.cell_table.list[press_key[0]][press_key[1]].state = 'Unselected'
                                        self.cell_table.draw()
                                        self.cell_table.list[press_key[0]][press_key[1]] = Cell(press_key[0],
                                                                                                press_key[1], 'None',
                                                                                                'Unselected')


                                        self.cell_table.undraw_now(x_pos, y_pos)

                                        press_key = (None, None)
                                        self.number_of_moves += 1
                                        # !!!!!!!!!!!!!!!!!!!!turn = ("white" if turn =="black" else "black")
                                    else:
                                        #!!!!!!!!!!!!!!!if self.cell_table.list[x_pos][y_pos].piece.color_type == turn:
                                        self.cell_table.list[press_key[0]][press_key[1]].state = 'Unselected'
                                        self.cell_table.draw()
                                        self.cell_table.list[x_pos][y_pos].state = 'Selected'

                                        press_key = (x_pos, y_pos)


                                else:
                                    #!!!!!!!!!!!!!!!!!if self.cell_table.list[x_pos][y_pos].piece.color_type == turn:
                                        self.cell_table.list[x_pos][y_pos].state = 'Selected'
                                        press_key = (x_pos, y_pos)

                        # нажатия за границы поля
                        elif  x_pos == -1 and y_pos == -1:
                            game = False
                            new = True

                        else:
                            if press_key != (None, None):
                                self.cell_table.list[press_key[0]][press_key[1]].state = 'Unselected'
                            press_key = (None, None)

            # self.all_sprites.update()

            # проверка на пешку в последнем ряду
            if mouse_click:
                if self.choose():
                    pass
                elif Touch:
                    self.new_items()
                else:
                    self.make_board(self.number_of_moves)
                    self.cell_table.draw_check()
                    self.cell_table.draw()
                    self.cell_table.chess_check(self.cell_table.list, draw=True)
                    self.screen.blit(self.surface1, (0, 0))
                    self.all_sprites.draw(self.screen)

                    self.make_lines()
                # self.choose('black')
                # self.choose('white')
                pygame.display.flip()
                mouse_click = False
            # clock.tick(self.fps)
        #pygame.quit()
        return new


# запуск игры
if __name__ == '__main__':
    game = Life(700, 700, 70, 5)
    new = True
    while new:
        new = game.run_game()
