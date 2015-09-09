#!/usr/local/bin/python2.7

import sys
import world
import agent
import heapq


class AStar:

    def __init__(self, agent, world):
        self.world = world
        self.score = 0
        self.actionNum = 0
        self.nodeNum = 0
        self.actionList = []
        self.cameFrom = []
        self.openSet = [self.world.start]
        heapq.heapify(self.openSet)
        self.closedSet = []

    def output():
        # The score of the path found
        # The number of actions required to reach the goal
        # The number of nodes expanded
        # The series of actions (e.g., forward, turn, forward, forward, forward,
        #   ...) taken to get to the goal, with each action separated by a newline
        pass

    def agent(self):
        ''' A getter for the world agent '''
        return self.world.agent

    def start(self):
        ''' Start the A star algorithm '''


def main():
    newAgent = agent.Agent(5)
    newWorld = world.World("test1.world.txt", newAgent)
    astar = AStar(newAgent, newWorld)
    astar.start()

if __name__ == "__main__":
    main()
