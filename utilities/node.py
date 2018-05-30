import uuid
import random

class Node:

    def __init__(self, state, action, action_space, reward, terminal):
        self.identifier = str(uuid.uuid1())
        self.parent_identifier = None
        self.children_identifiers = []
        self.untried_actions = list(range(action_space))
        self.state = state
        self.total_simulation_reward = 0
        self.num_visits = 0
        self.performance = 0
        self.action = action
        self.reward = reward
        self.terminal = terminal

    def __str__(self):
        return "{}: (action={}, visits={}, reward={:d}, ratio={:0.4f})".format(
                                                  self.state,
                                                  self.action,
                                                  self.num_visits,
                                                  int(self.total_simulation_reward),
                                                  self.performance)

    def untried_action(self):
        action = random.choice(self.untried_actions)
        self.untried_actions.remove(action)
        return action