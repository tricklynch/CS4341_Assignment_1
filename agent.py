#!/usr/local/bin/python2.7

import sys
from direction import Direction
from fsm import FSM

class Agent:
    '''
    Represents the agent acting on the environment.
    heuristic_number is a number referring to the heuristics outlined in the
    project description which is in range(1, 7)
    '''

    def __init__(self):
        self.pos = ()
        self.dir = Direction()
        self.fsm = FSM()

    def bash(self, pos):
        ''' Returns the cost of bashing over the current position'''
        offset = self.vector(pos)
        offset_pos = Cell.add_positions(self.pos, offset)
        two_offset_pos = Cell.add_positions(offset_pos, offset)
        bash_cost = 3
        return bash_cost + self.world.get_cell(two_offset_pos)

    def forward(self, pos):
        ''' Returns the cost of moving forward to the given position '''
        forward_position = Cell.add_positions(self.pos, self.direction())
        return self.world.get_cell(forward_position)

    def turn(self, pos):
        ''' Cost of turning to face the given position '''
        single_turn_cost = math.ceil(self.world.get_cell(self.pos) / 3)
        turns_needed = self.dir.count_turns_needed(pos)
        return single_turn_cost * turns_needed

    def vector(self, other):
        ''' Returns the offset of a point compared to the agent's position '''
        return Cell.sub_positions(other, self.pos)

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
