#!/usr/local/bin/python2.7

import sys
import world


def output():
    # The score of the path found
    # The number of actions required to reach the goal
    # The number of nodes expanded
    # The series of actions (e.g., forward, turn, forward, forward, forward,
    #   ...) taken to get to the goal, with each action separated by a newline
    pass


def main():
    newWorld = world.World("world0.txt")
    print newWorld

if __name__ == "__main__":
    main()

 

class Astar:
    def __init__(self, agent, world):
        self.agent = agent
        self.world = world
        self.score = 0
        self.actionNum = 0
        self.nodeNum = 0
        self.actionList= []
        
        def astar(self):
            closedSet = []
            
            cameFrom = []
