import uuid

class Node:

    def __init__(self, state=None):
        self.identifier = str(uuid.uuid1())
        self.parent_identifier = None
        self.children_identifiers = []
        self.untried_actions = [0, 1, 2, 3]
        self.state = state
        self.total_simulation_reward = 0
        self.num_visits = 0
        self.performance = 0
        self.terminal_states = [5, 7, 11, 12, 15]

    def __str__(self):
        return "{}: ({} | {:d} | {:0.4f})".format(self.state,
                                                  self.num_visits,
                                                  int(self.total_simulation_reward),
                                                  self.performance)

    def is_terminal(self):
        if self.state in self.terminal_states:
            return True
        else:
            return False

    def is_expandable(self):
        if self.state in self.terminal_states:
            return False
        if len(self.untried_actions) > 0:
            return True
        return False

    def action(self):
        action = self.untried_actions[0]
        self.untried_actions.remove(action)
        return action