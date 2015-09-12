CS4341 Assignment 1
Alec Benson     abenson
Leo Bowen-Biggs pcbiggs
Keenan Gray     krgray
Patrick Lynch   pelynch

To run the program under certain conditions, run

./astar

To run the program in a way that you can specify the heuristic, run

python2.7 main.py heuristic

Where heuristic is a number between 1 and 6 inclusive. This will run a randomly
generated 10 x 10 board with the heuristic you specify. There are flags
available in order to specify the world to run or the size of a random world to
generate. Additionally, you may write a world to a file so that you may re-test
the world later. The flag for specifying the size of a random world is -s
followed by a number. The flag for specifying the world to run is a -w followed
by a filename to read from. The flag for writing the world to a file is -f
followed by a filename to write to. In order to see the documentation for these
flags, run

python2.7 main.py -h

When running our program with extra flags, do not forget to include the
heuristic number at the end.
