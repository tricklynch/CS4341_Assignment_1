#!/usr/local/bin/python2.7

import sys
from direction import Direction

class Agent:
    # start_pos is a tuple for the initial x, y coordinates of the agent
    # heuristic_number is a number referring to the heuristics outlined in the
    # project description which is in range(1, 7)
    def __init__(self, heuristic_number):
        # heuristic is a string that should be the name of a function in the
        # Agent class
        try:
            heuristic = "_heuristic_" + str(heuristic_number)
            if heuristic_number > 6 or heuristic_number < 1:
                raise IndexError(
                    "Your heuristic_number is out of range. Choose between 1 and 6")
            # heuristic_func is a function to represent the heuristic
            self.heuristic_func = getattr(self, heuristic)
        except Exception as err:
            print str(err)
            sys.exit(1)

        self.pos = ()
        self.dir = Direction()

    # A heuristic of 0. A solution for a relaxed problem where the robot can
    # teleport to the goal. This value also provides a baseline of how
    # uninformed search would perform.
    def _heuristic_1(self, world):
        return 0

    # Min(vertical, horizontal). Use whichever difference is smaller. This
    # heuristic should dominate #1.
    def _heuristic_2(self, world):
        x_diff = abs(self.pos[0] - world.goal[0])
        y_diff = abs(self.pos[1] - world.goal[1])
        return min(x_diff, y_diff)

    # Max(vertical, horizontal). Use whichever difference is larger. This
    # heuristic should dominate #2.
    def _heuristic_3(self, world):
        x_diff = abs(self.pos[0] - world.goal[0])
        y_diff = abs(self.pos[1] - world.goal[1])
        return max(x_diff, y_diff)

    # Vertical + horizontal. Sum the differences together. This heuristic
    # should dominate #3.
    def _heuristic_4(self, world):
        x_diff = abs(self.pos[0] - world.goal[0])
        y_diff = abs(self.pos[1] - world.goal[1])
        return x_diff + y_diff

    # Find an admissable heuristic that dominates #4. A small tweak of #4 will
    # work here.
    # If the robot is not in the same row or column as the goal, it will need
    # to turn with a cost of at least 1.
    def _heuristic_5(self, world):
        x_diff = abs(self.pos[0] - world.goal[0])
        y_diff = abs(self.pos[1] - world.goal[1])
        heuristic = x_diff + y_diff
        if x_diff == 0 or y_diff == 0:
            return heuristic
        return heuristic + 1

    # Create a non-admissable heuristic by multiplying #5 by 3. See the lecture
    # notes on heuristics for why we might want to do such a thing.
    def _heuristic_6(self, world):
        return 3 * heuristic_5(world)

    # Moves the agent 1 unit forward on the map without changing its facing
    # direction. Time required: the terrain complexity of the square being
    # moved into.
    def forward(self, world):
        Cell.add_positions(self.pos, self.dir)

    # The robot powers up, and charges forward crashing through obstacles in
    # its path. The effect is to move the agent 1 unit forward on the map
    # without changing its facing direction. Time required: 3 (ignores terrain
    # complexity), and the next action taken by the agent must be Forward.
    # I.e., the after Bashing, the agent cannot turn, Demolish, or Bash; it
    # must first move Forward at least once to recover its balance.
    def bash(self, world):
        Cell.add_positions(self.pos, self.dir)
        Cell.add_positions(self.pos, self.dir)

    # Turns the agent 90 degrees, either left or right. Time required: 1/3 of
    # the numeric value of the square currently occupied (rounded up).
    def turn(self, world, direction):
        if direction is "right":
            self.dir.turnRight()
        elif direction is "left":
            self.dir.turnLeft()


    # The robot uses high-powered explosives to simplify the task. The
    # explosives clear all 8 of the adjacent squares (excluding the square
    # inhibited by the robot, fortunately) and replaces their terrain
    # complexity with 3 due to residual rubble. Time required: 4. Note: this
    # action can increase terrain complexity if the initial complexity of the
    # square is less than 3. Also note that if the agent considers using
    # Demolish, but the search backtracks, you must ensure that correct terrain
    # complexity is restored to the map.
    def demolish(self, world):
        pass
