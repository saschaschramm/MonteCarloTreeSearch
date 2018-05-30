from model import MonteCarloTreeSearch
import random
from gym.envs.registration import register
import gym
from utilities.tree import Tree

def init_env():
    register(
        id='FrozenLakeNotSlippery-v0',
        entry_point='gym.envs.toy_text:FrozenLakeEnv',
        kwargs={'map_name': '4x4', 'is_slippery': False}
    )
    return gym.make('FrozenLakeNotSlippery-v0')

def main():
    random.seed(2)
    env = init_env()
    tree = Tree()
    monteCarloTreeSearch = MonteCarloTreeSearch(env=env, tree=tree)
    steps = 10000

    for _ in range(0, steps):
        env.reset()
        node = monteCarloTreeSearch.tree_policy()
        reward = monteCarloTreeSearch.default_policy(node)
        monteCarloTreeSearch.backward(node, reward)

    monteCarloTreeSearch.tree.show()
    monteCarloTreeSearch.forward()

if __name__ == "__main__":
   main()
