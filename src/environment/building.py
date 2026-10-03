class Building:
    EMPTY = 0
    WALL = 1
    EXIT = 2
    PERSON = 3
    SMOKE = 4
    FIRE = 5

    CELL_COSTS = {
        EMPTY: 1,
        EXIT: 1,
        PERSON: 1,
        SMOKE: 5,
        FIRE: float("inf")
    }

    def __init__(self, layout):
        self.layout = layout

    def get_cell(self, row, col):
        return self.layout[row][col]

    def set_cell(self, row, col, value):
        self.layout[row][col] = value

    def is_walkable(self, row, col):
        return self.layout[row][col] != self.WALL

    def get_cost(self, row, col):
        cell_type = self.layout[row][col]
        return self.CELL_COSTS.get(cell_type, 1)

    def get_position(self, cell_type):
        for row in range(len(self.layout)):
            for col in range(len(self.layout[row])):
                if self.layout[row][col] == cell_type:
                    return row, col

        return None