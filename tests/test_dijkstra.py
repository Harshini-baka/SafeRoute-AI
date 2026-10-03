from src.environment.building import Building
from src.pathfinding.dijkstra import dijkstra


def test_dijkstra_finds_path():

    layout = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 3, 0, 0, 0, 2, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]

    building = Building(layout)

    start = building.get_position(Building.PERSON)
    goal = building.get_position(Building.EXIT)

    costs = {
        (1, 2): 10,
        (1, 3): 10,
        (1, 4): 10
    }

    path = dijkstra(
        building,
        start,
        goal,
        costs
    )

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal