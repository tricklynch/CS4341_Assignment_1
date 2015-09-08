#!/usr/local/bin/python2.7

import sys


class Agent:
    # start_pos is a tuple for the initial x, y coordinates of the agent
    # heuristic_number is a number referring to the heuristics outlined in the
    #   project description which is in range(1, 7)

    def __init__(self, start_pos, heuristic_number):
        self.pos = start_pos
        # heuristic is a string that should be the name of a function in the
        #   Agent class
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
    def _heuristic_5(self, world):
        pass

    # Create a non-admissable heuristic by multiplying #5 by 3. See the lecture
    # notes on heuristics for why we might want to do such a thing.
    def _heuristic_6(self, world):
        return 3 * heuristic_5(world)
