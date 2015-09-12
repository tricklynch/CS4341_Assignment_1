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

    def output(self, score, expanded):
        # The score of the path found
        # The number of actions required to reach the goal
        # The number of nodes expanded
        # The series of actions (e.g., forward, turn, forward, forward, forward,
        #   ...) taken to get to the goal, with each action separated by a newline
        print "Nodes Expanded = {0}\nScore = {1}".format(expanded, score); 

    def start(self):
        ''' Start the A star algorithm '''
        expansion_count = 0
        while not self.open_set.empty():
            current = self.open_set.get()
           # print "Expanding node {0}".format(current)
            expansion_count += 1
            # If we reached the goal, stop
            if current == self.world.goal:
                break

            evaluator = Agent(current, self.facing[current], self.heuristic_num, self.world)
            for next in self.world.get_adjacent_cells(current):
                # Tally total cost
                g_score = self.cost_so_far[current] \
                    + evaluator.forward(next) + evaluator.turn(next)

                # Consider the adjacent node, 'next'...
                if next not in self.cost_so_far or g_score < self.cost_so_far[next]:
                    self.cost_so_far[next] = g_score
                    h_score = evaluator.estimate(next, self.world.goal)
                    f_score = g_score + h_score

                    #Add the node to the priority queue
                    self.open_set.put(next, f_score)
                    #Save the direction the node is facing
                    new_dir = Direction().set_dir(Direction.vector(current, next))
                    self.facing[next] = new_dir
                    #Add the node to the path of traversed nodes
                    self.came_from[next] = current

            for bash_cell in self.world.get_bashable_cells(current):
                g_score = self.cost_so_far[current] \
                    + evaluator.bash(bash_cell) + evaluator.turn(bash_cell)

                #Consider the bash node, next
                if bash_cell not in self.cost_so_far or g_score < self.cost_so_far[bash_cell]:
                    self.cost_so_far[bash_cell] = g_score
                    h_score = evaluator.estimate(bash_cell, self.world.goal)
                    f_score = g_score + h_score

                    self.open_set.put(bash_cell, f_score)
                    new_dir = Direction().set_dir(Direction.vector(current, bash_cell))
                    self.facing[bash_cell] = new_dir
                    self.came_from[bash_cell] = current
        score = 100 - self.cost_so_far[self.world.goal]
        self.trace_path()
        self.output(score, expansion_count)

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
        path.pop(0)
        costs.pop(0)

        path.reverse()
        costs.reverse()
        self.draw_solution(path, costs)
