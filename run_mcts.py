from mcts import MonteCarloTreeSearch
from utilities.env_wrapper import EnvWrapper
import random

def main():
    random.seed(2)
    env = EnvWrapper()
    monteCarloTreeSearch = MonteCarloTreeSearch(env)
    steps = 10000
    for _ in range(0, steps):
        node = monteCarloTreeSearch.tree_policy()
        reward = monteCarloTreeSearch.default_policy(node.state)
        monteCarloTreeSearch.backward(node, reward)

    monteCarloTreeSearch.tree.show()
    monteCarloTreeSearch.forward()

if __name__ == "__main__":
    main()