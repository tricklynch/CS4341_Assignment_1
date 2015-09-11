"""
The FSM
States  Next states Description
0:      0, 1, 2     You just moved forward
1:      0           You just bashed
2:      0, 1, 3     You just turned
3:      0, 1        You just turned a second consecutive time

Possible moves from states
States  Moves
0       forward, bash, turn
1       forward
2       forward, bash, turn
3       forward, bash
"""

class FSM:
    def __init__(self, state):
        self.current_state = state
        self.next_states = self._get_next_states()

    def _get_next_states(self):
        state = self.current_state
        if state is 0:
            return [0, 1, 2]
        elif state is 1:
            return [0]
        elif state is 2:
            return [0, 1, 3]
        elif state is 3:
            return [0, 1]
        else:
            # Error check later
            return []
