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

def test_smoke_spreads_to_adjacent_cells():

    layout = [
        [1, 1, 1, 1, 1],
        [1, 0, 4, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]

    building = Building(layout)

    hazard = HazardSimulator(building)

    hazard.spread_smoke()

    assert building.layout[1][1] == Building.SMOKE
    assert building.layout[1][3] == Building.SMOKE
    assert building.layout[2][2] == Building.SMOKE


def test_fire_creates_smoke():

    layout = [
        [1, 1, 1, 1, 1],
        [1, 0, 5, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]

    building = Building(layout)

    hazard = HazardSimulator(building)

    hazard.create_smoke_from_fire()

    assert building.layout[1][1] == Building.SMOKE
    assert building.layout[1][3] == Building.SMOKE
    assert building.layout[2][2] == Building.SMOKE

def test_hazard_update():

    layout = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 5, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]

    building = Building(layout)

    hazard = HazardSimulator(building)

    hazard.update()

    assert building.layout[2][3] == Building.FIRE

    assert building.layout[1][3] == Building.SMOKE
    assert building.layout[3][3] == Building.SMOKE
    assert building.layout[2][2] == Building.SMOKE
    assert building.layout[2][4] == Building.SMOKE