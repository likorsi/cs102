import copy
import pygame
from pygame.locals import *
import random


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        self.clist = self.cell_list()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            # Отрисовка списка клеток
            self.draw_cell_list(self.clist)
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.update_cell_list(self.clist)

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=True) -> list:
        """ Создание списка клеток.
        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        self.clist = []
        if randomize == True:
                for i in range(self.cell_width):
                    self.clist.append([random.randint(0, 1) for _ in range(self.cell_height)])
        else:
            self.clist = [[0] * self.cell_width for _ in range(self.cell_height)]
        return self.clist

    def draw_cell_list(self, clist):
        """ Отображение списка клеток
        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        for i in range(self.cell_height):
            for k in range(self.cell_width):
                x, y = k * self.cell_size-1, i * self.cell_size-1
                if clist[i][k]:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (x, y,
                                        self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (x, y,
                                        self.cell_size, self.cell_size))


    def get_neighbours(self, cell) -> list:
        """ Вернуть список соседей для указанной ячейки
        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        row, col = cell
        neighbours = [self.clist[r][c] for r in range(row - 1, row + 2) for c in range(col - 1, col + 2) if
                      (0 <= r <= (self.cell_height - 1)) and (0 <= c <= (self.cell_width - 1))
                      and ((r != row) or (c != col))]
        return neighbours


    def update_cell_list(self, cell_list) -> list:
        """ Выполнить один шаг игры.
        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.
        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = copy.deepcopy(self.clist)
        for i in range(self.cell_height):
            for k in range(self.cell_width):
                all_neighbours = sum(self.get_neighbours((i, k)))
                if self.clist[i][k] == 1:
                    if (all_neighbours <= 1) or (all_neighbours >= 4):
                        new_clist[i][k] = 0
                else:
                    if all_neighbours == 3:
                        new_clist[i][k] = 1
        self.clist = new_clist
        return self.clist
