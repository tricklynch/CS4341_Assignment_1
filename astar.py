#!/usr/local/bin/python2.7

import sys
import world
import agent


def output():
    # The score of the path found
    # The number of actions required to reach the goal
    # The number of nodes expanded
    # The series of actions (e.g., forward, turn, forward, forward, forward,
    #   ...) taken to get to the goal, with each action separated by a newline
    pass


def main():
    newWorld = world.World("world0.txt")
    newAgent = agent.Agent(newWorld.start, 20)
    print newWorld

if __name__ == "__main__":
    main()
