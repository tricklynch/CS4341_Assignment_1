#!/usr/local/bin/python2.7

import argparse
from world import World
from astar import AStar

def main():
    parser = argparse.ArgumentParser(
        description="Compute the optimal path using A*"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-w", "--world", help="The filename of the world to load",
    )
    group.add_argument(
        "-s", "--size", type=int, help="Size of the random board to be generated"
    )
    parser.add_argument(
        "heuristic", type=int,
        help="The heuristic number to run (in range(1, 7))"
    )
    args = parser.parse_args()
    if args.world:
        newWorld = World(filepath=args.world)
    elif args.size:
        newWorld = World(height=args.size, width=args.size)
    else:
        newWorld = World(height=10, width=10)
    astar = AStar(newWorld, 5)
    astar.start()

if __name__ == "__main__":
    main()
