from src.environment.building import Building
from src.pathfinding.bfs import bfs


def test_bfs_finds_path():

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

    path = bfs(building, start, goal)

    assert path is not None
    assert path[0] == start
    assert path[-1] == goal


def test_bfs_returns_none_when_no_path():

    layout = [
        [1, 1, 1, 1, 1],
        [1, 3, 1, 2, 1],
        [1, 1, 1, 1, 1],
    ]

    building = Building(layout)

    start = building.get_position(Building.PERSON)
    goal = building.get_position(Building.EXIT)

    path = bfs(building, start, goal)

    assert path is None