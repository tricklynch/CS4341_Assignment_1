#!/usr/local/bin/python2.7
from operator import sub, add


class World:
    '''The world structure is a class that is used to represent '''

    def __init__(self, filepath, agent):
        self.rows = []
        self.start = ()
        self.goal = ()
        self.load(filepath)

        agent.pos = self.start
        self.agent = agent

    def __str__(self):
        return str(self.rows)

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
        if pos_x < 0 or pos_x > self.width:
            return True
        if pos_y < 0 or pos_y > self.length:
            return True
        return False

    def get_cell_complexity(self, pos):
        ''' Returns the complexity of the cell at the given position tuple '''
        pos_x = pos[0]
        pos_y = pos[1]
        return self.rows[pos_x][pos_y]

    def _add_positions(self, pos, other):
        '''
        A helper function that adds two positions together and returns the result.
        For example, given (1,1) and (1,0), (2,1) will be returned.
        '''
        return tuple(map(add, pos, other))

    def _sub_positions(self, pos, other):
        '''
        A helper function that subtracts two positions together and returns the result.
        For example, given (1,1) and (1,0), (0,1) will be returned.
        '''
        return tuple(map(sub, pos, other))

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
            cell = self._add_positions(pos, offset)
            if self.pos_off_board(cell):
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
                try:
                    complexity = int(strippedVal)
                    row.append(complexity)
                except ValueError as err:
                    # This exception is caught if we try to parse a non integer ValueError
                    # This happens when we parse the Goal or start location.
                    row.append(1)
                    if strippedVal == "G":
                        self.goal = (x, y)
                    elif strippedVal == "S":
                        self.start = (x, y)
                    else:
                        print "ERROR: Read an invalid character in the world file: {0}".format(strippedVal)
            self.rows.append(row)

    def _read_world_file(self, filename):
        ''' Reads the world file from the filepath and returns the contents of the file '''
        try:
            world_file = open(filename, 'r')
        except:
            print('The file probably does not exist or something')
            sys.exit(1)
        return world_file
