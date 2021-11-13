import numpy as np
from graphviz import Source


class MarkovChains:

    def __init__(self, b0, P):

        self.initial_distribution = np.array(b0)
        self.transition_matrix = np.array(P)

    def ergodic_distribution(self):

        b = self.initial_distribution

        for k in range(10000):
            b = np.dot(b, self.transition_matrix)
            if (np.round(b, 8) == np.round(np.dot(b, self.transition_matrix), 8)).all():
                print(f"\nb(k): { k + 1 }\n"
                      f"{np.round(b, 8)}")
                break
            print(np.round(b, 8))

    def visualize(self):

        digraph = 'digraph finite_state_machine { size="8,8" node [shape = circle];'

        for enj, j in enumerate(self.transition_matrix):
            for eni, i in enumerate(j):
                if i != 0:
                    digraph += f"{enj + 1} -> {eni + 1} [label = {i}];"

        digraph += "}"

        s = Source(digraph, filename="markov_chains_graph.gv", format="png")
        s.render(filename='graph')
        # s.view()


if __name__ == '__main__':

    initial_state = [0.2, 0.4, 0.1, 0.2, 0.1]
    transition_matrix = [[0.2, 0.7, 0.0, 0.0, 0.1],
                         [0.3, 0.2, 0.2, 0.3, 0.0],
                         [0.0, 0.0, 0.2, 0.5, 0.3],
                         [0.4, 0.3, 0.0, 0.2, 0.1],
                         [0.5, 0.3, 0.0, 0.2, 0.0]]

    markov_chain = MarkovChains(initial_state, transition_matrix)
    MarkovChains.ergodic_distribution(markov_chain)
    MarkovChains.visualize(markov_chain)
