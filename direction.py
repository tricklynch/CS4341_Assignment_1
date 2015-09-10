class Direction():
    ''' The direction class is used to keep track of the agent's Forward position '''
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def __init__(self):
        self.index = 0
        self._dirs = [self.NORTH, self.EAST, self.SOUTH, self.WEST]

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