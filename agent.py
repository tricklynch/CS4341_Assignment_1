#!/usr/local/bin/python2.7

import sys


class Agent:
    # start_pos is a tuple for the initial x, y coordinates of the agent
    # heuristic_number is a number referring to the heuristics outlined in the
    #   project description which is in range(6)

    def __init__(self, start_pos, heuristic_number):
        self.pos = start_pos
        # heuristic is a string that should be the name of a function in the
        #   Agent class
        heuristic = "heuristic_" + str(heuristic_number)
        try:
           # heuristic_func is a function to represent the heuristic
            self.heuristic_func = getattr(self, heuristic)
        except:
            print("Your heuristic_number is out of range probably")
            sys.exit(1)

    def heuristic_0(self, world):
        return 0

    def heuristic_1(self, world):
        pass

    def heuristic_2(self, world):
        pass

    def heuristic_3(self, world):
        pass

    def heuristic_4(self, world):
        pass

    def heuristic_5(self, world):
        pass
