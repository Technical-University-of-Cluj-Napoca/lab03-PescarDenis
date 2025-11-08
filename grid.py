from utils import *
from spot import Spot

class Grid:
    def __init__(self, win: pygame.Surface, rows: int, cols: int, width: int, height: int):
        """
        Initialize a grid with the given number of rows and columns, of the width and height of the window.
        Args:
            win (pygame.Surface): The Pygame surface (window) where the grid will be drawn.
            rows (int): Number of rows in the grid.
            cols (int): Number of columns in the grid.
            width (int): Width of the window in pixels.
            height (int): Height of the window in pixels.
        """
        self.win: pygame.Surface = win
        self.rows: int = rows
        self.cols: int = cols
        self.width: int = width
        self.height: int = height
        self.grid: list[list[Spot]] = self._make_grid()

    def _make_grid(self) -> list[list[Spot]]:
        """
        Create a grid of Spot objects.
        Returns:
            list[list[Spot]]: A 2D list (matrix) representing the grid of Spot objects.
        """
        grid = []
        spot_width = self.width // self.rows  # width of each spot
        spot_height = self.height // self.cols  # height of each spot
        for i in range(self.rows):
            grid.append([])
            for j in range(self.cols):
                spot = Spot(i, j, spot_width, spot_height, self.rows)
                grid[i].append(spot)
        return grid

    def draw_grid_lines(self) -> None:
        spot_width = self.width // self.cols
        spot_height = self.height // self.rows

        for i in range(self.rows):
            pygame.draw.line(self.win, GRID_LINE_COLOR, (0, i * spot_height), (self.width, i * spot_height))

        for j in range(self.cols):
            pygame.draw.line(self.win, GRID_LINE_COLOR, (j * spot_width, 0), (j * spot_width, self.height))


    def draw(self) -> None:
        self.win.fill(BACKGROUND_COLOR)

        for row in self.grid:
            for spot in row:
                spot.draw(self.win)

        self.draw_grid_lines()
        pygame.display.update()


    def get_clicked_pos(self, pos: tuple[int, int]) -> tuple[int, int]:
        """
        Get the row and column of the grid based on the mouse position.
        Args:
            pos (tuple[int, int]): The (x, y) position of the mouse click.
        Returns:
            tuple[int, int]: The (row, col) position of the clicked spot in the grid.
        """
        spot_width = self.width // self.cols
        spot_height = self.height // self.rows
        x, y = pos
        col = x // spot_width
        row = y // spot_height
        return col, row
    
    def reset(self) -> None:
        """
        Reset the grid to its initial state.
        Returns:
            None
        """
        for row in self.grid:
            for spot in row:
                spot.reset()