class GridManager:
    grille_size = 3
    grille = [["black" for _ in range(3)] for _ in range(3)]

    @staticmethod
    def display_grid():
        """
        Displays the current state of the grid.
        """
        for row in GridManager.grille:
            print(row)

    @staticmethod
    def get_cell(row, col):
        """
        Gets the color of the cell at the specified row and column.

        :param row: Row index.
        :param col: Column index.
        :return: Color of the cell.
        """
        if 0 <= row < GridManager.grille_size and 0 <= col < GridManager.grille_size:
            return GridManager.grille[row][col]
        else:
            raise IndexError("Cell index out of range")

    @staticmethod
    def set_cell(row, col, color):
        """
        Sets the color of the cell at the specified row and column.

        :param row: Row index.
        :param col: Column index.
        :param color: Color to set.
        """
        if 0 <= row < GridManager.grille_size and 0 <= col < GridManager.grille_size:
            GridManager.grille[row][col] = color
        else:
            raise IndexError("Cell index out of range")

    @staticmethod
    def clear_grid():
        """
        Clears the grid by resetting all cells to "black".
        """
        GridManager.grille = [["black" for _ in range(GridManager.grille_size)] for _ in range(GridManager.grille_size)]

# Exemple d'utilisation :
# GridManager.display_grid()

# print("Setting cell at (1, 1) to 'red'")
# GridManager.set_cell(1, 1, "red")
# GridManager.display_grid()

# print("Getting cell at (1, 1)")
# print(GridManager.get_cell(1, 1))

# print("Clearing the grid")
# GridManager.clear_grid()
# GridManager.display_grid()
