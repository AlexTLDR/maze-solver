from graphics import Window, Cell


def main():
    win = Window(800, 600)

    # Create and draw cells with different wall configurations
    cell1 = Cell(win)
    cell1.draw(50, 50, 150, 150)  # All walls

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.has_top_wall = False
    cell2.draw(200, 50, 300, 150)  # Missing left and top walls

    cell3 = Cell(win)
    cell3.has_right_wall = False
    cell3.has_bottom_wall = False
    cell3.draw(350, 50, 450, 150)  # Missing right and bottom walls

    cell4 = Cell(win)
    cell4.has_left_wall = False
    cell4.has_right_wall = False
    cell4.has_top_wall = False
    cell4.has_bottom_wall = False
    cell4.draw(500, 50, 600, 150)  # No walls

    win.wait_for_close()


if __name__ == "__main__":
    main()
