from collections import deque


def bfs(building, start, goal):
    queue = deque([start])

    visited = {start}

    parent = {
        start: None
    }

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    while queue:

        current = queue.popleft()

        if current == goal:
            return reconstruct_path(parent, goal)

        row, col = current

        for row_change, col_change in directions:

            new_row = row + row_change
            new_col = col + col_change

            neighbor = (new_row, new_col)

            if not is_valid_cell(building, new_row, new_col):
                continue

            if neighbor in visited:
                continue

            visited.add(neighbor)

            parent[neighbor] = current

            queue.append(neighbor)

    return None


def is_valid_cell(building, row, col):

    if row < 0 or row >= len(building.layout):
        return False

    if col < 0 or col >= len(building.layout[row]):
        return False

    return building.is_walkable(row, col)


def reconstruct_path(parent, goal):

    path = []

    current = goal

    while current is not None:

        path.append(current)

        current = parent[current]

    path.reverse()

    return path


if __name__ == "__main__":

    from src.environment.building import Building
    
    layout = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 3, 0, 0, 0, 0, 0, 0, 2, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    building = Building(layout)

    start = building.get_position(Building.PERSON)
    goal = building.get_position(Building.EXIT)

    path = bfs(building, start, goal)

    print("Start:", start)
    print("Goal:", goal)
    print("Path:", path)