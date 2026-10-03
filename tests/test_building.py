from src.environment.building import Building


def test_cell_costs():

    layout = [
        [1, 1, 1, 1, 1],
        [1, 3, 0, 4, 2],
        [1, 0, 0, 5, 1],
        [1, 1, 1, 1, 1]
    ]

    building = Building(layout)

    assert building.get_cost(1, 2) == 1
    assert building.get_cost(1, 3) == 5
    assert building.get_cost(2, 3) == float("inf")