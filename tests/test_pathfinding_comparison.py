from src.environment.building import Building
from src.pathfinding.bfs import bfs
from src.pathfinding.dijkstra import dijkstra


def test_bfs_and_dijkstra_choose_different_routes():

    layout = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 3, 4, 4, 4, 2, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]
    building = Building(layout)

    start = building.get_position(Building.PERSON)
    goal = building.get_position(Building.EXIT)

    bfs_path = bfs(
        building,
        start,
        goal
    )

    dijkstra_path = dijkstra(
        building,
        start,
        goal
    )

    assert bfs_path is not None
    assert dijkstra_path is not None

    print("\nBFS path:")
    print(bfs_path)

    print("\nDijkstra path:")
    print(dijkstra_path)


    dangerous_cells = {
        (1, 2),
        (1, 3),
        (1, 4)
    }

    assert not any(
        cell in dangerous_cells
        for cell in dijkstra_path
    )