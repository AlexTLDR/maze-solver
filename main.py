from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 10, 50, 50, win)
    maze._reset_cells_visited()  
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
