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