import pygame
from src.environment.building import Building
from src.pathfinding.bfs import bfs
from src.pathfinding.dijkstra import dijkstra

# Size of each grid cell
CELL_SIZE = 40

# Building layout
BUILDING = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 4, 4, 4, 4, 4, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Grid dimensions
ROWS = len(BUILDING)
COLS = len(BUILDING[0])

building = Building(BUILDING)
start = building.get_position(Building.PERSON)
goal = building.get_position(Building.EXIT)

path = dijkstra(building, start, goal)

print("Start:", start)
print("Goal:", goal)
print("Dijkstra path:", path)

def draw_grid(screen, path):
    for row in range(ROWS):
        for col in range(COLS):

            cell = BUILDING[row][col]
            position = (row, col)

            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if cell == Building.WALL:
                color = (40, 40, 40)

            elif cell == Building.EXIT:
                color = (0, 180, 0)

            elif cell == Building.PERSON:
                color = (0, 100, 255)

            elif cell == Building.SMOKE:
                color=(120,120,120)

            elif cell==Building.FIRE:
                color=(255, 80, 0)

            elif path is not None and position in path:
                color = (255, 220, 100)

            else:
                color = (230, 230, 230)

            pygame.draw.rect(
                screen,
                color,
                (x, y, CELL_SIZE, CELL_SIZE)
            )

            pygame.draw.rect(
                screen,
                (180, 180, 180),
                (x, y, CELL_SIZE, CELL_SIZE),
                1
            )


def main():

    pygame.init()

    width = COLS * CELL_SIZE
    height = ROWS * CELL_SIZE

    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption("SafeRoute AI - Building Environment")

    clock = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        draw_grid(screen,path)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()