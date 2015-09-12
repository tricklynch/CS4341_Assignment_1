from cell import Cell
from operator import div
import math

class Direction():
    ''' The direction class is used to keep track of the agent's Forward position '''
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def __init__(self, index=1):
        self.index = index
        self._direction = self.NORTH
        self._dirs = {self.WEST:-1, self.NORTH:-1, self.EAST:1, self.SOUTH:1}


    def count_turns_needed(self, from_pos, to_pos):
        ''' Returns the number of turns needed to face the given other direction '''
        print "Current direction {0}, from_pos {1}, to_pos {2}".format(self._direction, from_pos, to_pos)
        vector = self.vector(from_pos, to_pos)
        if vector == self.direction():
            return 0

        if vector == self.NORTH:
            if self.direction() == self.SOUTH:
                return 2
            return 1
        if vector == self.SOUTH:
            if self.direction() == self.NORTH:
                return 2
            return 1
        if vector == self.EAST:
            if self.direction() == self.WEST:
                return 2
            return 1
        if vector == self.WEST:
            if self.direction() == self.EAST:
                return 2
            return 1
        return 1


    def direction(self):
        return self._direction

    @staticmethod
    def vector(first, other):
        ''' Returns the offset of a point compared to the agent's position '''
        offset = Cell.sub_positions(other, first)
        abs_offset = map(abs,offset)
        max_val = max(abs_offset)
        vector = tuple(map(div,offset,(max_val,max_val)))
        return vector

    def set_dir(self, other_dir):
        if other_dir in self._dirs:
            self._direction = other_dir
        return self
