from mcts import MonteCarloTreeSearch

def main():
    monteCarloTreeSearch = MonteCarloTreeSearch()
    steps = 10000
    for _ in range(0, steps):
        node = monteCarloTreeSearch.tree_policy()
        reward = monteCarloTreeSearch.default_policy(node.state)
        monteCarloTreeSearch.backward(node, reward)

    monteCarloTreeSearch.tree.show()
    monteCarloTreeSearch.forward()

if __name__ == "__main__":
    main()



"""
******** state  14
13 -> 0.29411764705882354
14 -> 0.982648057336854
15 -> 1.0
10 -> 0.391304347826087
******** state  15

"""