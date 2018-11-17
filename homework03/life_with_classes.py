import pygame
from pygame.locals import *
import random
from copy import deepcopy


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
        cell = CellList(self.cell_width, self.cell_height, randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            # Отрисовка списка клеток
            for i in range(self.cell_height):
                for k in range(self.cell_width):
                    x, y = k * self.cell_size - 1, i * self.cell_size - 1
                    if clist[i][k]:
                        pygame.draw.rect(self.screen, pygame.Color('green'), (x, y,
                                                                              self.cell_size, self.cell_size))
                    else:
                        pygame.draw.rect(self.screen, pygame.Color('white'), (x, y,
                                                                              self.cell_size, self.cell_size))
            # Выполнение одного шага игры (обновление состояния ячеек)
            cell.update(self.clist)


            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


class Cell:

    def __init__(self, row, col, state=False):
        self.row = row
        self.col = col
        self.state = state

    def is_alive(self):
        return self.state


class CellList:

    def __init__(self, nrows, ncols, randomize=False):
        self.nrows = nrows
        self.ncols = ncols

    def get_neighbours(self, cell):
        neighbours = []
        row, col = cell
        neighbours = [self.clist[r][c] for r in range(row - 1, row + 2) for c in range(col - 1, col + 2) if
                      (0 <= r <= (self.cell_height - 1)) and (0 <= c <= (self.cell_width - 1))
                      and ((r != row) or (c != col))]
        return neighbours

    def update(self):
        new_clist = deepcopy(self)
        # PUT YOUR CODE HERE
        return self

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __str__(self):
        pass

    @classmethod
    def from_file(cls, filename):
        pass
