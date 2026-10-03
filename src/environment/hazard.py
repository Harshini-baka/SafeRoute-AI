class HazardSimulator:

    def __init__(self, building):
        self.building = building

    def spread_fire(self):
        current_fire = []

        for row in range(len(self.building.layout)):
            for col in range(len(self.building.layout[row])):

                if self.building.layout[row][col] == self.building.FIRE:
                    current_fire.append((row, col))

        new_fire = []

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for row, col in current_fire:

            for row_change, col_change in directions:

                new_row = row + row_change
                new_col = col + col_change

                if new_row < 0 or new_row >= len(self.building.layout):
                    continue

                if new_col < 0 or new_col >= len(self.building.layout[new_row]):
                    continue

                cell = self.building.layout[new_row][new_col]

                if cell == self.building.EMPTY:
                    new_fire.append((new_row, new_col))

        for row, col in new_fire:
            self.building.layout[row][col] = self.building.FIRE