import random
import time
from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        if seed is not None:
            random.seed(seed)
            
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
        time.sleep(1)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        
        self._cells[i][j].draw(x1, y1, x2, y2)
        if self._win is not None:
            self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        
        while True:
            possible_directions = []
            
            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append((i-1, j, "left"))
            if i < self._num_cols-1 and not self._cells[i+1][j].visited:
                possible_directions.append((i+1, j, "right"))
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i, j-1, "up"))
            if j < self._num_rows-1 and not self._cells[i][j+1].visited:
                possible_directions.append((i, j+1, "down"))
            
            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
            
            next_cell = random.choice(possible_directions)
            next_i, next_j, direction = next_cell
            
            if direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            elif direction == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif direction == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
                
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        time.sleep(1)
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
            
        if (i > 0 and 
            not self._cells[i-1][j].visited and 
            not self._cells[i][j].has_left_wall):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], True)
        
        if (i < self._num_cols-1 and 
            not self._cells[i+1][j].visited and 
            not self._cells[i][j].has_right_wall):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], True)
        
        if (j > 0 and 
            not self._cells[i][j-1].visited and 
            not self._cells[i][j].has_top_wall):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], True)
        
        if (j < self._num_rows-1 and 
            not self._cells[i][j+1].visited and 
            not self._cells[i][j].has_bottom_wall):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], True)
        
        return False
