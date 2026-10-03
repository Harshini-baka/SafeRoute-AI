import random

class HazardSimulator:

    def __init__(self, building):
        self.building = building
        self.fire_spread_rate = 0.5
        self.smoke_spread_rate = 0.7

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
              if random.random() < self.fire_spread_rate:
                 new_fire.append((new_row, new_col))

      for row, col in new_fire:
        self.building.layout[row][col] = self.building.FIRE
    
    
    def create_smoke_from_fire(self):

      current_fire = []

      for row in range(len(self.building.layout)):
        for col in range(len(self.building.layout[row])):

            if self.building.layout[row][col] == self.building.FIRE:
                current_fire.append((row, col))

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
                self.building.layout[new_row][new_col] = self.building.SMOKE
    
    
    def spread_smoke(self):
        current_smoke = []

        for row in range(len(self.building.layout)):
            for col in range(len(self.building.layout[row])):

                if self.building.layout[row][col] == self.building.SMOKE:
                    current_smoke.append((row, col))

        new_smoke = []

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for row, col in current_smoke:

            for row_change, col_change in directions:

                new_row = row + row_change
                new_col = col + col_change

                if new_row < 0 or new_row >= len(self.building.layout):
                    continue

                if new_col < 0 or new_col >= len(self.building.layout[new_row]):
                    continue

                cell = self.building.layout[new_row][new_col]

                if cell == self.building.EMPTY:
                    if random.random() < self.smoke_spread_rate:
                        new_smoke.append((new_row, new_col))

        for row, col in new_smoke:
            self.building.layout[row][col] = self.building.SMOKE

    def update(self):
        self.create_smoke_from_fire()
        self.spread_smoke()
        self.spread_fire()