from cell import Cell

class Direction():
    ''' The direction class is used to keep track of the agent's Forward position '''
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def __init__(self, index=1):
        self.index = index
        self._dirs = [self.WEST, self.NORTH, self.EAST, self.SOUTH]

    def count_turns_needed(self, otherdir):
        ''' Returns the number of turns needed to face the given other direction '''
        dist = abs(self._dirs.index(otherdir) - self.index)
        return 2 if dist >= 3 else dist

    def __getitem__(self, val):
        return self._dirs[val % len(self._dirs)]

    def turnLeft(self):
        self.index -= 1
        return self[self.index]

    def turnRight(self):
        self.index += 1
        return self[self.index]

    def direction(self):
        return self._dirs[self.index]

    @staticmethod
    def vector(first, other):
        ''' Returns the offset of a point compared to the agent's position '''
        return Cell.sub_positions(other, first)

    def set_dir(self, other_dir):
        if other_dir in self._dirs:
            self.index = self._dirs.index(other_dir)
        return self
