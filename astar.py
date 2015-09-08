#!/usr/local/bin/python2.7

import sys

class Location:
    def __init__(self, complexity, type):
        self.complexity = complexity
        # type represents either start, goal, or a normal location
        self.type = type

def load_world(filename):
    try:
        world_file = open(filename, 'r')
    except:
        print('The file probably does not exist or something')
        sys.exit(1)
    world = []
    for world_row in world_file:
        row = []
        for world_element in world_row.split("\t"):
            row.append(int(world_element.rstrip("\n")))
        world.append(row)
    return world

def output():
    # The score of the path found
    # The number of actions required to reach the goal
    # The number of nodes expanded
    # The series of actions (e.g., forward, turn, forward, forward, forward,
    #   ...) taken to get to the goal, with each action separated by a newline
    pass

def main():
    load_world("test")

if __name__ == "__main__":
    main()
