#!/usr/local/bin/python2.7

import sys
from direction import Direction


class Agent:
    '''
    Represents the agent acting on the environment.
    heuristic_number is a number referring to the heuristics outlined in the
    project description which is in range(1, 7)
    '''

    def __init__(self):
        self.pos = ()
        self.dir = Direction()

    def forward(self, world):
        '''
        Moves the agent 1 unit forward on the map without changing its facing
        direction. Time required: the terrain complexity of the square being
        moved into.
        '''
        self.pos = Cell.add_positions(self.pos, self.direction())

    def bash(self, world):
        '''
        The robot powers up, and charges forward crashing through obstacles in
        its path. The effect is to move the agent 1 unit forward on the map
        without changing its facing direction. Time required: 3 (ignores terrain
        complexity), and the next action taken by the agent must be Forward.
        I.e., the after Bashing, the agent cannot turn, Demolish, or Bash; it
        must first move Forward at least once to recover its balance.
        '''
        Cell.add_positions(self.pos, self.dir)
        Cell.add_positions(self.pos, self.dir)

    def direction(self):
        ''' Returns the direction of the agent '''
        return self.dir.direction()

    def turn(self, world, direction):
        '''
        Turns the agent 90 degrees, either left or right. Time required: 1/3 of
        the numeric value of the square currently occupied (rounded up).
        '''
        if direction is "right":
            self.dir.turnRight()
            return self.direction()
        elif direction is "left":
            self.dir.turnLeft()
            return self.direction()

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
        pass
