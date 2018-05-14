import gym
from gym.envs.registration import register

import collections
Step = collections.namedtuple('Step', 'state reward done')

class EnvWrapper():

    def __init__(self):
        register(
            id='FrozenLakeNotSlippery-v0',
            entry_point='gym.envs.toy_text:FrozenLakeEnv',
            kwargs={'map_name': '4x4', 'is_slippery': False}
        )

        env = gym.make('FrozenLakeNotSlippery-v0')
        self.transitions = env.P

    def step_with_state(self, state, action):
        transition = self.transitions[state][action][0]
        state = transition[1]
        reward = transition[2]
        done = transition[3]
        return Step(state, reward, done)