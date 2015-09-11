#!/usr/local/bin/python2.7

from operator import sub, add

class Cell:
    '''The Cell class represents a tile on the board'''

    def __init__(self, complexity):
        self.is_start = False
        self.is_goal = False
        self.parse(complexity)

    def __int__(self):
        return self.complexity

    def __repr__(self):
        if self.is_start:
            return "S"
        elif self.is_goal:
            return "G"
        return str(self.complexity)

    def set_complexity(self, complexity):
        ''' Sets the complexity of the cell'''
        self.complexity = complexity

    def parse(self, complexity):
        ''' Given a value, 1-9, or an S or G, set the complexity, start, and goal'''
        try:
            c = int(complexity)
            self.complexity = c
        except ValueError as err:
            # This exception is caught if we try to parse a non integer ValueError
            # This happens when we parse the Goal or start location.
            if complexity == "G":
                self.complexity = 1
                self.is_goal = True
            elif complexity == "S":
                self.complexity = 1
                self.is_start = True
            else:
                print "ERROR: Read an invalid character in the world file: {0}".format(strippedVal)
                sys.exit(1)

    @staticmethod
    def add_positions(pos, other):
        '''
        A static utility method that adds two positions together and returns the result.
        For example, given (1,1) and (1,0), (2,1) will be returned.
        '''
        return tuple(map(add, pos, other))

    @staticmethod
    def sub_positions(pos, other):
        '''
        A static utility method that subtracts two positions together and returns the result.
        For example, given (1,1) and (1,0), (0,1) will be returned.
        '''
        return tuple(map(sub, pos, other))
