import pygame
from pygame.locals import *
import random
from copy import deepcopy


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10) -> None:
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

    def draw_grid(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        clist = CellList(self.cell_height, self.cell_width, randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            # Отрисовка списка клеток
            x, y = 1, 1
            for cell in clist:
                size = self.cell_size - 1
                if cell.is_alive():
                    pygame.draw.rect(self.screen, pygame.Color('green'),
                                     [x, y, size, size])
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                                     [x, y, size, size])
                x += size + 1
                if x >= self.width:
                    y += self.cell_size
                    x = 1
            # Выполнение одного шага игры (обновление состояния ячеек)
            clist.update()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


class Cell:

    def __init__(self, row: int, col: int, state=False) -> None:
        self.row = row
        self.col = col
        self.state = state

    def is_alive(self) -> int:
        return int(self.state)


class CellList:

    def __init__(self, nrows: int, ncols: int, randomize=False) -> None:
        self.nrows = nrows
        self.ncols = ncols
        self.grid: list = []
        for row in range(nrows):
            self.grid.append([])
            for col in range(ncols):
                if randomize:
                    self.grid[row].append(Cell(row, col, random.randint(0, 1)))
                else:
                    self.grid[row].append(Cell(row, col, False))


    def get_neighbours(self, cell: Cell) -> list:
        row, col = cell.row, cell.col
        neighbours = []
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r in range(0, self.nrows) and c in range(self.ncols) and (r != row or c != col):
                    neighbours.append(self.grid[r][c])
        return neighbours

    def update(self) -> object:
        new_clist = deepcopy(self.grid)
        for cell in self:
            all_neighbours = sum(c.is_alive() for c in self.get_neighbours(cell))
            if all_neighbours <= 1 or all_neighbours >= 4:
                new_clist[cell.row][cell.col].state = 0
            elif all_neighbours == 3:
                new_clist[cell.row][cell.col].state = 1
        self.grid = new_clist
        return self

    def __iter__(self):
        self.row, self.col = 0, 0
        return self

    def __next__(self):
        if self.row < self.nrows:
            cell = self.grid[self.row][self.col]
            self.col += 1
            if self.col == self.ncols:
                self.row += 1
                self.col = 0
            return cell
        else:
            raise StopIteration


    def __str__(self) -> str:
        str = ''
        for r in range(self.nrows):
            for c in range(self.ncols):
                if self.grid[r][c].state:
                    str += '1'
                else:
                    str += '0'
            str += '\n'
        return str

    @classmethod
    def from_file(cls, filename: str) -> 'CellList':
     grid = []
     with open(filename) as file:
         for row, line in enumerate(file):
             grid.append([Cell(row, col, state)
                          for col, state in enumerate(line)
                          if state != '\n' and (int(state) == 0 or int(state) == 1)])
     clist = cls(len(grid), len(grid[0]), randomize=False)
     clist.grid = grid
     return clist

if __name__ == '__main__':
    game = GameOfLife(600, 540, 20)
    game.run()