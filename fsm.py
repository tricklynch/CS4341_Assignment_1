"""
0:  0, 1, 2, 3  You just moved forward
1:  0           You just bashed
2:  0, 1, 4     You just turned left
3:  0, 1, 4     You just turned right
4:  0, 1        You just turned left or right for a second, consecutive time
"""

class FSM:
    def __init__(self, state):
        self.current_state = state
        self.next_states = self._get_next_states()

    def _get_next_states(self):
        state = self.current_state
        if state is 0:
            return [0, 1, 2, 3]
        elif state is 1:
            return [0]
        elif state is 2:
            return [0, 1, 4]
        elif state is 3:
            return [0, 1, 4]
        elif state is 4:
            return [0, 1]
