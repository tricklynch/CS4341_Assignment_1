#!/usr/local/bin/python2.7
from cell import Cell
import sys
import random

class World:
    '''The world structure is a class that is used to represent '''

    def __init__(self, filepath=None, height=0, width=0):
        self.rows = []
        self.start = ()
        self.goal = ()
        if filepath is None:
            self.gen_rand_world(height, width)
        else:
            self.load(filepath)
        

    def __str__(self):
        return "\n".join(str(row) for row in self.rows)

    def width(self):
        '''Returns the width of the board '''
        return max(len(x) for x in self.rows)

    def length(self):
        ''' Returns the length, or height of the board '''
        return len(self.rows)

    def is_at_goal(self, pos):
        ''' Returns True if the given position is the goal square '''
        return pos == self.goal

    def pos_off_board(self, pos):
        ''' Returns True if the position is off of the board, or false otherwise '''
        pos_x = pos[0]
        pos_y = pos[1]
        if pos_x < 0 or pos_x >= self.width():
            return True
        if pos_y < 0 or pos_y >= self.length():
            return True
        return False

    def get_cell(self, pos):
        ''' Returns the complexity of the cell at the given position tuple '''
        try:
            pos_x = pos[0]
            pos_y = pos[1]
            return int(self.rows[pos_y][pos_x])
        except IndexError as err:
            print "ERROR getting cell {0}: {1}".format(pos, err)
            print self
            sys.exit(1)

    def get_adjacent_cells(self, pos):
        ''' Returns all cells adjacent to the given position tuple. Diagonals are not considered adjacent. '''
        adjacent_offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        return self._get_cells_from_offsets(pos, adjacent_offsets)

    def get_surrounding_cells(self, pos):
        ''' Returns all 8 cells that surround the given position tuple, including diagonals'''
        surrounding_offsets = [(-1, 0), (0, 1), (1, 0), (0, -1),
                               (-1, 1), (1, 1), (1, -1), (-1, -1)]
        return self._get_cells_from_offsets(pos, surrounding_offsets)

    def _get_cells_from_offsets(self, pos, offsets):
        '''
        A helper function that is used to retrieve the coordinates of the cells
        that are 'offset' units away from the given position. For instance, giving
        a position of (0,1) and an offset of [(1,1),(1,0)] would return the cells
        [(1,2),(1,1)].
        '''
        result = []
        for offset in offsets:
            cell = Cell.add_positions(pos, offset)
            if self.pos_off_board(cell) == True:
                continue
            result.append(cell)
        return result

    def load(self, filename):
        ''' Parses the world file from the given filename'''
        world_file = self._read_world_file(filename)

        # Parse through the rows file
        for y, world_row in enumerate(world_file):
            row = []
            for x, world_element in enumerate(world_row.split("\t")):
                strippedVal = world_element.rstrip("\n")
                newCell = Cell(strippedVal)
                if newCell.is_goal:
                    self.goal = (x, y)
                if newCell.is_start:
                    self.start = (x, y)
                row.append(newCell)
            self.rows.append(row)

    def _read_world_file(self, filename):
        ''' Reads the world file from the filepath and returns the contents of the file '''
        try:
            world_file = open(filename, 'r')
        except:
            print('The file probably does not exist or something')
            sys.exit(1)
        return world_file

    def gen_rand_world(self, height, width):
        for i in range(height):
            world_row = []
            for j in range(width):
                newCell = Cell(random.randrange(1, 10))
                world_row.append(newCell)
            self.rows.append(world_row)
        start_x = 0
        start_y = 0
        goal_x = 0
        goal_y = 0
        while((start_x == goal_x) and (start_y == goal_y)):
            start_x = random.randrange(width)
            start_y = random.randrange(height)
            goal_x = random.randrange(width)
            goal_y = random.randrange(height)
        self.start = (start_x, start_y)
        self.goal = (goal_x, goal_y)
        self.rows[start_y][start_x] = Cell("S")
        self.rows[goal_y][goal_x] = Cell("G")
