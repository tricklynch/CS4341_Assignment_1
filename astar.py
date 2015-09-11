#!/usr/local/bin/python2.7

import world
from agent import Agent
from queue import CellQueue
from direction import Direction

class AStar:

    def __init__(self, world, heuristic_num):
        self.world = world

        self.heuristic_num = heuristic_num

        # Total cost to get to a given node
        self.cost_so_far = {}
        self.cost_so_far[self.world.start] = 0
        self.facing = {}
        self.facing[self.world.start] = Direction()

        # Openset is a priorityQueue where best options are first
        self.open_set = CellQueue()
        self.open_set.put(self.world.start, 0)

        # cameFrom is a dictionary of the traversed path
        self.came_from = {}
        self.came_from[self.world.start] = None

    def output():
        # The score of the path found
        # The number of actions required to reach the goal
        # The number of nodes expanded
        # The series of actions (e.g., forward, turn, forward, forward, forward,
        #   ...) taken to get to the goal, with each action separated by a newline
        pass

    def start(self):
        ''' Start the A star algorithm '''
        while not self.open_set.empty():
            current = self.open_set.get()
            print "Expanding node {0}".format(current)

            # If we reached the goal, stop
            if current == self.world.goal:
                break

            # For each adjacent cell
            for next in self.world.get_adjacent_cells(current):
                # Tally total cost
                evaluator = Agent(current, self.facing[current], self.heuristic_num, 0, self.world)
                new_cost = self.cost_so_far[current] \
                    + self.world.get_cell(next) + evaluator.turn(next)
                new_dir = Direction().set_dir(Direction.vector(current, next))
                
                # Consider the adjacent node, 'next'...
                if next not in self.cost_so_far or new_cost < self.cost_so_far[next]:
                    # TODO: Replace the 0 with a variable. This is the state of
                    # the agent at the time of evaluation. The state is
                    # dependant on the previous moves and at this time I am not
                    # certain how to determine that.
                    self.cost_so_far[next] = new_cost
                    priority = new_cost + \
                        evaluator.estimate(self.world.goal)
                    self.open_set.put(next, priority)
                    self.facing[next] = new_dir
                    self.came_from[next] = current
        self.trace_path()

    def draw_solution(self, path, costs):
        ''' Draws the board and highlights the spaces that the agent took '''
        green = '\033[92m'
        reset = '\033[0m'
        bold = '\033[1m'

        for y, row in enumerate(self.world.rows):
            print "\n"
            for x, cell in enumerate(row):
                if tuple([x, y]) in path:
                    print "{0}{1}{2}{3}\t".format(bold, green, cell, reset),
                else:
                    print "{0}\t".format(cell),
        print "\n"

        print "Path\tCost"
        for x in range(len(path)):
            print "{0}\t{1}".format(path[x], costs[x])


    def trace_path(self):
        '''Using the came_from dictionary, reconstruct the correct path to the goal '''
        current = self.world.goal
        path = [current]
        costs = [current]

        while True:
            path.append(current)
            costs.append(self.cost_so_far[current])
            current = self.came_from[current]

            if current == self.world.start:
                path.append(current)
                costs.append(self.cost_so_far[current])
                current = self.came_from[current]
                break

        path.reverse()
        costs.reverse()

        self.draw_solution(path, costs)
