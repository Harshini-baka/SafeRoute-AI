from src.environment.building import Building
from src.environment.hazard import HazardSimulator


def test_fire_spreads_to_adjacent_cells():

    layout = [
        [1, 1, 1, 1, 1],
        [1, 0, 5, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]

    building = Building(layout)

    hazard = HazardSimulator(building)

    hazard.spread_fire()

    assert building.layout[1][1] == Building.FIRE
    assert building.layout[1][3] == Building.FIRE
    assert building.layout[2][2] == Building.FIRE