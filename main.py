#!/usr/local/bin/python2.7

import argparse
from world import World
from astar import AStar

def main():
    parser = argparse.ArgumentParser(
        description="Compute the optimal path using A*"
    )
    parser.add_argument(
        "world", help="The filename of the world to load",
    )
    parser.add_argument(
        "heuristic", type=int,
        help="The heuristic number to run (in range(1, 7))"
    )
    args = parser.parse_args()
    newWorld = World(args.world)
    astar = AStar(newWorld, 5)
    astar.start()

if __name__ == "__main__":
    main()
