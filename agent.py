#!/usr/local/bin/python2.7

import sys
import math
from direction import Direction
from cell import Cell


class Agent:
    '''
    Represents the agent acting on the environment.
    heuristic_number is a number referring to the heuristics outlined in the
    project description which is in range(1, 7)
    '''

    def __init__(self, pos, direction, heuristic_num, world):
        self.pos = pos
        self.dir = direction
        self.heuristic_num = heuristic_num
        self.world = world

    def estimate(self, start, end):
        ''' Estimate is a method that runs the appropriate heuristic '''
        try:
            if self.heuristic_num > 6 or self.heuristic_num < 1:
                raise IndexError("No heuristic {0}".format(self.heuristic_num))

            # Run the appropriate heuristic function
            heuristic_name = "_heuristic_{0}".format(self.heuristic_num)
            return getattr(self, heuristic_name)(start, end)
        except Exception as err:
            print str(err)
            sys.exit(1)

    def get_possible_moves(self, world):
        moves = self._moves_from_state()
        moves = self._sanitize_moves(moves, world)
        moves_functions = []
        for m in moves:
            moves_functions.append(getattr(self, m))
        return moves_functions

    def _heuristic_1(self, start, end):
        '''
        A heuristic of 0. A solution for a relaxed problem where the robot can
        teleport to the goal. This value also provides a baseline of how
        uninformed search would perform.
        '''
        return 0

    def _heuristic_2(self, start, end):
        '''
        Min(vertical, horizontal). Use whichever difference is smaller. This
        heuristic should dominate  # 1.
        '''
        x_diff = abs(start[0] - end[0])
        y_diff = abs(start[1] - end[1])
        return min(x_diff, y_diff)

    def _heuristic_3(self, start, end):
        '''
        Max(vertical, horizontal). Use whichever difference is larger. This
        heuristic should dominate  # 2.
        '''
        x_diff = abs(start[0] - end[0])
        y_diff = abs(start[1] - end[1])
        return max(x_diff, y_diff)

    def _heuristic_4(self, start, end):
        '''
        Vertical + horizontal. Sum the differences together. This heuristic
        should dominate  # 3.
        '''
        x_diff = abs(start[0] - end[0])
        y_diff = abs(start[1] - end[1])
        return x_diff + y_diff

    def _heuristic_5(self, start, end):
        '''
        Find an admissable heuristic that dominates  # 4. A small tweak of #4 will
        work here.
        If the robot is not in the same row or column as the goal, it will need
        to turn with a cost of at least 1.
        '''
        x_diff = abs(start[0] - end[0])
        y_diff = abs(start[1] - end[1])
        heuristic = x_diff + y_diff
        if x_diff == 0 or y_diff == 0:
            return heuristic
        return heuristic + 1

    def _heuristic_6(self, start, end):
        '''
        Create a non - admissable heuristic by multiplying  # 5 by 3. See the lecture
        notes on heuristics for why we might want to do such a thing.
        '''
        return 3 * self._heuristic_5(start, end)

    def bash(self, pos):
        ''' Returns the cost of bashing over the current position'''
        bash_cost = 3
        return bash_cost + self.forward(pos)

    def forward(self, pos):
        ''' Returns the cost of moving forward to the given position '''
        return self.world.get_cell(pos)

    def turn(self, pos):
        ''' Cost of turning to face the given position '''
        single_turn_cost = math.ceil(self.world.get_cell(self.pos) / 3.0)
        turns_needed = self.dir.count_turns_needed(self.pos, pos)
        return single_turn_cost * turns_needed

    def direction(self):
        ''' Returns the direction of the agent '''
        return self.dir.direction()

    def demolish(self, world):
        '''
        The robot uses high-powered explosives to simplify the task. The
        explosives clear all 8 of the adjacent squares (excluding the square
        inhibited by the robot, fortunately) and replaces their terrain
        complexity with 3 due to residual rubble. Time required: 4. Note: this
        action can increase terrain complexity if the initial complexity of the
        square is less than 3. Also note that if the agent considers using
        Demolish, but the search backtracks, you must ensure that correct terrain
        complexity is restored to the map.
        '''
        return 0
