import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_small(self):
        num_cols = 3
        num_rows = 3
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 50
        num_rows = 40
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m3._cells),
            num_cols,
        )
        self.assertEqual(
            len(m3._cells[0]),
            num_rows,
        )

    def test_reset_cells_visited(self):
        num_cols = 3
        num_rows = 3
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        # Set some cells as visited
        m._cells[0][0].visited = True
        m._cells[1][1].visited = True
        m._cells[2][2].visited = True
        
        # Reset all cells
        m._reset_cells_visited()
        
        # Verify all cells are not visited
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(m._cells[i][j].visited)

if __name__ == "__main__":
    unittest.main()
