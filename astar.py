#!/usr/local/bin/python2.7

import sys
import world
import agent
from Queue import PriorityQueue

class Heuristic:

    def __init__(self, heuristic_num):
        self.heuristic_num = heuristic_num

    def estimate(self, start, end):
        ''' Estimate is a method that runs the appropriate heuristic '''
        try:
            if self.heuristic_num > 6 or self.heuristic_num < 1:
                raise IndexError("No heuristic {0}".format(self.heuristic_num))

            # Run the appropriate heuristic function
            heuristic_name = "_heuristic_{0}".format(self.heuristic_num)
            return getattr(self, heuristic_name)(start, end)
        except Exception as err:
            print str(err)
            sys.exit(1)

    def _heuristic_1(self, start, end):
        '''
        A heuristic of 0. A solution for a relaxed problem where the robot can
        teleport to the goal. This value also provides a baseline of how
        uninformed search would perform.
        '''
        return 0

    def _heuristic_2(self, start, end):
        '''
        Min(vertical, horizontal). Use whichever difference is smaller. This
        heuristic should dominate  # 1.
        '''
        x_diff = abs(start[0] - end[0])
        y_diff = abs(start[1] - end[1])
        return min(x_diff, y_diff)

    def _heuristic_3(self, start, end):
        '''
        Max(vertical, horizontal). Use whichever difference is larger. This
        heuristic should dominate  # 2.
        '''
        x_diff = abs(start[0] - end[0])
        y_diff = abs(start[1] - end[1])
        return max(x_diff, y_diff)

    def _heuristic_4(self, start, end):
        '''
        Vertical + horizontal. Sum the differences together. This heuristic
        should dominate  # 3.
        '''
        x_diff = abs(start[0] - end[0])
        y_diff = abs(start[1] - end[1])
        return x_diff + y_diff

    def _heuristic_5(self, start, end):
        '''
        Find an admissable heuristic that dominates  # 4. A small tweak of #4 will
        work here.
        If the robot is not in the same row or column as the goal, it will need
        to turn with a cost of at least 1.
        '''
        x_diff = abs(start[0] - end[0])
        y_diff = abs(start[1] - end[1])
        heuristic = x_diff + y_diff
        if x_diff == 0 or y_diff == 0:
            return heuristic
        return heuristic + 1

    def _heuristic_6(self, start, end):
        '''
        Create a non - admissable heuristic by multiplying  # 5 by 3. See the lecture
        notes on heuristics for why we might want to do such a thing.
        '''
        return 3 * heuristic_5(start, end)


class AStar:

    def __init__(self, agent, world, heuristic_num):
        self.world = world

        self.h = Heuristic(heuristic_num)

        # Total cost to get to a given node
        self.cost_so_far = {}
        self.cost_so_far[self.world.start] = 0

        # Openset is a priorityQueue where best options are first
        self.open_set = PriorityQueue()
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

    def agent(self):
        ''' A getter for the world agent '''
        return self.world.agent

    def start(self):
        ''' Start the A star algorithm '''
        while not self.open_set.empty():
            current = self.open_set.get()
            if current == self.world.goal:
                break

            for next in self.world.get_adjacent_cells(current):
                new_cost = self.cost_so_far[current] \
                    + self.world.get_cell(next)
                if next not in self.cost_so_far or new_cost < self.cost_so_far[next]:
                    self.cost_so_far[next] = new_cost
                    priority = new_cost + \
                        self.h.estimate(next, self.world.goal)
                    self.open_set.put(next, priority)
                    self.came_from[next] = current
        self.trace_path()

    def draw_solution(self, path):
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
        print path

    def trace_path(self):
        '''Using the came_from dictionary, reconstruct the correct path to the goal '''
        current = self.world.goal
        path = [current]
        while current != self.world.start:
            current = self.came_from[current]
            path.append(current)
        path.reverse()
        self.draw_solution(path)


def main():
    worldFile = "test1.world.txt"
    if(len(sys.argv) == 2):
        worldFile = sys.argv[1]
    newAgent = agent.Agent()
    newWorld = world.World(worldFile, newAgent)
    astar = AStar(newAgent, newWorld, 5)
    astar.start()

if __name__ == "__main__":
    main()
