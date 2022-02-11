import pygame
from pygame.locals import *


class Life:
    def __init__(self, width=200, height=400, cell_size=20, fps=5):
        # инициализация параметров игры
        self.width = width
        self.height = height - 59

        self.cell_size = cell_size
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        self.fps = fps

        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)


    def make_board(self):
        numbers_list = ['8', '7', '6', '5', '4', '3', '2', '1']
        letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        # отрисовка квадратов 8 на 8, чередуя белый и коричневый цвета
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(self.screen, pygame.Color('white') if (x+y) % 2 == 0 else (128, 0, 0),
                                (70 + self.cell_size * x, 70 + self.cell_size * y, self.cell_size, self.cell_size))

        font = pygame.font.Font(None, 30)
        counter_x = 0
        for x in range(70, 71 + self.cell_size * 8, self.cell_size):
            # отрисовка контуров "игральной доски" и пространства между квадратами
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 70), (x, 70 + self.cell_size * 8))
            try:
                # определение соответствующей надписи-подсказки квадрата по оси x
                text_1 = font.render(letters_list[counter_x], True, (0, 0, 0))
                # отражение этой надписи-подсказки по горизонтали и вертикали для 2-го игрока
                text_2 = pygame.transform.flip(text_1, True, True)
            except IndexError:
                break
            # расчёт координаты для надписи-подсказки для обоих игроков 
            text_1_pos = (x + self.cell_size // 3, 80 + self.cell_size * 8)
            text_2_pos = (x + self.cell_size // 3, 70 - self.cell_size // 1.5 )
            # размещение надписей на экране
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
            text_2_pos = (80  + self.cell_size * 8, y + self.cell_size // 3)
            self.screen.blit(text_1, text_1_pos)
            self.screen.blit(text_2, text_2_pos)
            counter_y += 1


    def run_game(self):
        pygame.init()
        #clock = pygame.time.Clock()
        pygame.display.set_caption('Life')
        # заполнение фона белым цветом
        self.screen.fill(pygame.Color('white'))
        game = True
        # главный цикл игры с проверкой действий игроков
        while game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    game = False
            #отрисовка игральной доски 
            self.make_board()
            # обновление состояния всего поля
            pygame.display.flip()
            #clock.tick(self.fps)
        pygame.quit()

#начальная точка всей программы с созданием экземпляра класса "игра" и её запуском       
if __name__ == '__main__':
    game = Life(500, 500, 40, 5)
    game.run_game()

