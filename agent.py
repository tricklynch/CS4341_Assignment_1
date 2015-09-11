#!/usr/local/bin/python2.7

import sys
import math
from cell import Cell
from direction import Direction
from fsm import FSM


class Agent:
    '''
    Represents the agent acting on the environment.
    heuristic_number is a number referring to the heuristics outlined in the
    project description which is in range(1, 7)
    '''

    def __init__(self, pos, direction, heuristic_num, state, world):
        self.pos = pos
        self.dir = direction
        self.heuristic_num = heuristic_num
        self.fsm = FSM(state)
        self.world = world

    def estimate(self, end):
        ''' Estimate is a method that runs the appropriate heuristic '''
        try:
            if self.heuristic_num > 6 or self.heuristic_num < 1:
                raise IndexError("No heuristic {0}".format(self.heuristic_num))

            # Run the appropriate heuristic function
            heuristic_name = "_heuristic_{0}".format(self.heuristic_num)
            return getattr(self, heuristic_name)(end)
        except Exception as err:
            print str(err)
            sys.exit(1)

    def get_possible_moves(self, world):
        moves = self._moves_from_state()
        moves = self._sanitize_moves(moves, world)
        moves_functions = []
        for m in moves:
            moves_functions.append(getattr(self, m))
        return moves_functions

    # Return a list of possible moves based off of the state
    def _moves_from_state(self):
        state = self.fsm.current_state
        if state is 0:
            moves = ["forward", "bash", "turn"]
        elif state is 1:
            moves = ["forward"]
        elif states is 2:
            moves = ["forward", "bash", "turn"]
        elif states is 3:
            moves = ["forward", "bash"]
        else:
            # Do some error checking later maybe
            return []
        return moves

    # Remove moves that are not possible based on position
    def _sanitize_moves(self, moves, world):
        length = world.length() - 1
        width = world.width() - 1
        if self.dir is 0:
            if "forward" in moves:
                if self.pos[0] == 0:
                    moves.remove("forward")
            if "bash" in moves:
                if self.pos[0] <= 1:
                    moves.remove("bash")
        elif self.dir is 1:
            if "forward" in moves:
                if self.pos[1] == 0:
                    moves.remove("forward")
            if "bash" in moves:
                if self.pos[1] <= 1:
                    moves.remove("bash")
        elif self.dir is 2:
            if "forward" in moves:
                if self.pos[0] == width:
                    moves.remove("forward")
            if "bash" in moves:
                if self.pos[0] >= width - 1:
                    moves.remove("bash")
        elif self.dir is 3:
            if "forward" in moves:
                if self.pos[1] == length:
                    moves.remove("forward")
            if "bash" in moves:
                if self.pos[1] >= length - 1:
                    moves.remove("bash")
        return moves

    def _heuristic_1(self, end):
        '''
        A heuristic of 0. A solution for a relaxed problem where the robot can
        teleport to the goal. This value also provides a baseline of how
        uninformed search would perform.
        '''
        return 0

    def _heuristic_2(self, end):
        '''
        Min(vertical, horizontal). Use whichever difference is smaller. This
        heuristic should dominate  # 1.
        '''
        x_diff = abs(self.pos[0] - end[0])
        y_diff = abs(self.pos[1] - end[1])
        return min(x_diff, y_diff)

    def _heuristic_3(self, end):
        '''
        Max(vertical, horizontal). Use whichever difference is larger. This
        heuristic should dominate  # 2.
        '''
        x_diff = abs(self.pos[0] - end[0])
        y_diff = abs(self.pos[1] - end[1])
        return max(x_diff, y_diff)

    def _heuristic_4(self, end):
        '''
        Vertical + horizontal. Sum the differences together. This heuristic
        should dominate  # 3.
        '''
        x_diff = abs(self.pos[0] - end[0])
        y_diff = abs(self.pos[1] - end[1])
        return x_diff + y_diff

    def _heuristic_5(self, end):
        '''
        Find an admissable heuristic that dominates  # 4. A small tweak of #4 will
        work here.
        If the robot is not in the same row or column as the goal, it will need
        to turn with a cost of at least 1.
        '''
        x_diff = abs(self.pos[0] - end[0])
        y_diff = abs(self.pos[1] - end[1])
        heuristic = x_diff + y_diff
        if x_diff == 0 or y_diff == 0:
            return heuristic
        return heuristic + 1

    def _heuristic_6(self, end):
        '''
        Create a non - admissable heuristic by multiplying  # 5 by 3. See the lecture
        notes on heuristics for why we might want to do such a thing.
        '''
        return 3 * self._heuristic_5(end)

    def bash(self, pos):
        ''' Returns the cost of bashing over the current position'''
        offset = self.vector(pos)
        offset_pos = Cell.add_positions(self.pos, offset)
        two_offset_pos = Cell.add_positions(offset_pos, offset)
        bash_cost = 3
        return bash_cost + self.world.get_cell(two_offset_pos)

    def forward(self, pos):
        ''' Returns the cost of moving forward to the given position '''
        forward_position = Cell.add_positions(self.pos, self.direction())
        return self.world.get_cell(forward_position)

    def turn(self, pos):
        ''' Cost of turning to face the given position '''
        single_turn_cost = math.ceil(self.world.get_cell(self.pos) / 3)
        other_dir = self.vector(pos)
        turns_needed = self.dir.count_turns_needed(other_dir)
        return single_turn_cost * turns_needed

    def vector(self, other):
        ''' Returns the offset of a point compared to the agent's position '''
        return Cell.sub_positions(other, self.pos)

    def direction(self):
        ''' Returns the direction of the agent '''
        return self.dir.direction()

    def demolish(self, world):
        '''
        The robot uses high-powered explosives to simplify the task. The
        explosives clear all 8 of the adjacent squares (excluding the square
        inhibited by the robot, fortunately) and replaces their terrain
        complexity with 3 due to residual rubble. Time required: 4. Note: this
        action can increase terrain complexity if the initial complexity of the
        square is less than 3. Also note that if the agent considers using
        Demolish, but the search backtracks, you must ensure that correct terrain
        complexity is restored to the map.
        '''
        return 0
