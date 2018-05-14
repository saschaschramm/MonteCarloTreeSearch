from utilities.tree import Tree
from utilities.env_wrapper import EnvWrapper
import random
from math import sqrt, log
from utilities.node import Node

class MonteCarloTreeSearch():

    def __init__(self):
        self.env = EnvWrapper()
        self.tree = Tree()
        self.tree.add_node(Node(state = 0))
        random.seed(1)

    def expand(self, parent):
        step = self.env.step_with_state(parent.state, parent.action())
        child = Node(state = step.state)
        self.tree.add_node(child, parent)
        return child

    def default_policy(self, state):

        if state == 15:
            return 1.0

        while True:
            action = random.randint(0, 3)
            step = self.env.step_with_state(state, action)
            if step.done:
                return step.reward
            state = step.state

    def compute_value(self, parent, child, exploration_constant):
        return child.total_simulation_reward / child.num_visits + exploration_constant * \
        sqrt(2 * log(parent.num_visits) / child.num_visits)

    def best_child(self, node, exploration_constant):
        best_child = self.tree.children(node)[0]
        best_value = self.compute_value(node, best_child, exploration_constant)
        iter_children = iter(self.tree.children(node))
        next(iter_children)
        for child in iter_children:
            value = self.compute_value(node, child, exploration_constant)
            if value > best_value:
                best_child = child
                best_value = value

        return best_child

    def tree_policy(self):
        node = self.tree.root
        while not node.is_terminal():
            if node.is_expandable():
                return self.expand(node)
            else:
                node = self.best_child(node, exploration_constant=1.0/sqrt(2.0))
        return node

    def backward(self, node, value):
        while node:
            node.num_visits += 1
            node.total_simulation_reward += value
            node.performance = node.total_simulation_reward/node.num_visits
            node = self.tree.parent(node)

    def forward(self):
        self._forward(self.tree.root)

    def _forward(self,node):
        best_child = self.best_child(node, exploration_constant=0)
        print("******** state ", best_child.state)

        for child in self.tree.children(best_child):
            print("{} -> {}".format(child.state, child.performance))

        if len(self.tree.children(best_child)) > 0:
            self._forward(best_child)