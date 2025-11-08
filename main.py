import pygame
from utils import *
from grid import Grid
from searching_algorithms import *
from button import Button  

pygame.init()

SIDEBAR_WIDTH = 180
WIN = pygame.display.set_mode((WIDTH + SIDEBAR_WIDTH, HEIGHT))
pygame.display.set_caption("Searching Algorithms")

GRID_SURFACE = pygame.Surface((WIDTH, HEIGHT))

ROWS = 50
COLS = 50
grid = Grid(GRID_SURFACE, ROWS, COLS, WIDTH, HEIGHT)

start = None
end = None
run = True

def draw_all():
    grid.draw()
    WIN.blit(GRID_SURFACE, (0, 0))
    for b in buttons:
        b.draw()
    pygame.display.update()

def clear():
    global start, end
    start = None
    end = None
    grid.reset()
    draw_all()


buttons = [
    Button(WIDTH + 20, 30, 140, 35, "BFS", lambda: bfs(lambda: draw_all(), grid, start, end), WIN),
    Button(WIDTH + 20, 80, 140, 35, "DFS", lambda: dfs(lambda: draw_all(), grid, start, end), WIN),
    Button(WIDTH + 20, 130, 140, 35, "DLS", lambda: dls(lambda: draw_all(), grid, start, end, 12), WIN),
    Button(WIDTH + 20, 180, 140, 35, "A*", lambda: astar(lambda: draw_all(), grid, start, end), WIN),
    Button(WIDTH + 20, 230, 140, 35, "UCS", lambda: ucs(lambda: draw_all(), grid, start, end), WIN),
    Button(WIDTH + 20, 280, 140, 35, "Greedy", lambda: greedy_search(lambda: draw_all(), grid, start, end), WIN),
    Button(WIDTH + 20, 330, 140, 35, "IDS", lambda: ids(lambda: draw_all(), grid, start, end, 50), WIN),
    Button(WIDTH + 20, 380, 140, 35, "IDA*", lambda: ida_star(lambda: draw_all(), grid, start, end), WIN),
    Button(WIDTH + 20, 450, 140, 35, "CLEAR", lambda: clear(), WIN)
]


while run:
    draw_all()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:  # Left click
            pos = pygame.mouse.get_pos()

            # Button Click Handling
            for b in buttons:
                if b.clicked(pos):
                    for row in grid.grid:
                        for spot in row:
                            spot.update_neighbors(grid.grid)
                    b.action()
                    break

            # Clicking inside grid
            if pos[0] < WIDTH:
                row, col = grid.get_clicked_pos(pos)
                if 0 <= row < ROWS and 0 <= col < COLS:
                    spot = grid.grid[row][col]
                    if not start and spot != end:
                        start = spot
                        start.make_start()
                    elif not end and spot != start:
                        end = spot
                        end.make_end()
                    elif spot != end and spot != start:
                        spot.make_barrier()

        elif pygame.mouse.get_pressed()[2]:  # Right click
            pos = pygame.mouse.get_pos()
            if pos[0] < WIDTH:
                row, col = grid.get_clicked_pos(pos)
                if 0 <= row < ROWS and 0 <= col < COLS:
                    spot = grid.grid[row][col]
                    spot.reset()
                    if spot == start:
                        start = None
                    elif spot == end:
                        end = None

pygame.quit()
