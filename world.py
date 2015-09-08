class World:
    '''The world structure is a class that is used to represent '''
    def __init__(self, filepath):
        self.start = ()
        self.goal = ()
        self.rows = []
        self.load(filepath)

    def __str__(self):
        return str(self.rows)

    def load(self, filename):
        ''' Parses the world file from the given filename'''
        world_file = self._read_world_file(filename)

        #Parse through the rows file
        for y, world_row in enumerate(world_file):
            row = []
            for x, world_element in enumerate(world_row.split("\t")):
                strippedVal = world_element.rstrip("\n")
                try:
                    complexity = int(strippedVal)
                    row.append(complexity)
                except ValueError as err:
                    #This exception is caught if we try to parse a non integer ValueError
                    #This happens when we parse the Goal or start location.
                    row.append(1)
                    if strippedVal == "G":
                        self.goal = (x, y)
                    elif strippedVal == "S":
                        self.start = (x, y)
                    else:
                        print "ERROR: Read an invalid character in the world file: {0}".format(strippedVal)
            self.rows.append(row)

    def _read_world_file(self, filename):
        ''' Reads the world file from the filepath and returns the contents of the file '''
        try:
            world_file = open(filename, 'r')
        except:
            print('The file probably does not exist or something')
            sys.exit(1)
        return world_file
