import heapq


def dijkstra(building, start, goal):

    priority_queue = [(0, start)]

    distances = {
        start: 0
    }

    parent = {
        start: None
    }

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    while priority_queue:

        current_cost, current = heapq.heappop(priority_queue)

        if current == goal:
            return reconstruct_path(parent, goal)

        if current_cost > distances[current]:
            continue

        row, col = current

        for row_change, col_change in directions:

            new_row = row + row_change
            new_col = col + col_change

            neighbor = (new_row, new_col)

            if not is_valid_cell(building, new_row, new_col):
                continue

            movement_cost = building.get_cost(new_row, new_col)

            if movement_cost == float("inf"):
                continue

            new_cost = current_cost + movement_cost

            if neighbor not in distances or new_cost < distances[neighbor]:

                distances[neighbor] = new_cost

                parent[neighbor] = current

                heapq.heappush(
                    priority_queue,
                    (new_cost, neighbor)
                )

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