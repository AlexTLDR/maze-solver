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

def test_break_entrance_and_exit(self):
    num_cols = 3
    num_rows = 3
    m = Maze(0, 0, num_rows, num_cols, 10, 10)
    m._break_entrance_and_exit()
    
    # Check entrance (top-left cell)
    self.assertFalse(m._cells[0][0].has_top_wall)
    
    # Check exit (bottom-right cell)
    self.assertFalse(m._cells[num_cols-1][num_rows-1].has_bottom_wall)
    
    # Verify other walls are still intact
    self.assertTrue(m._cells[0][0].has_left_wall)
    self.assertTrue(m._cells[0][0].has_right_wall)
    self.assertTrue(m._cells[0][0].has_bottom_wall)
    
    self.assertTrue(m._cells[num_cols-1][num_rows-1].has_left_wall)
    self.assertTrue(m._cells[num_cols-1][num_rows-1].has_right_wall)
    self.assertTrue(m._cells[num_cols-1][num_rows-1].has_top_wall)


if __name__ == "__main__":
    unittest.main()
