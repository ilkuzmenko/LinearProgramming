import numpy as np
from graphviz import Source


class MarkovChains:

    def __init__(self, initial_distribution, stochastic_matrix):

        self.B = np.array(initial_distribution)
        self.P = np.array(stochastic_matrix)

    def chains(self):

        b = self.B

        for k in range(10000):
            b = np.dot(b, self.P)
            if (np.round(b, 8) == np.round(np.dot(b, self.P), 8)).all():
                print(f"Number of steps: { k + 1 }")
                break
            print(np.round(b, 7))

    def visualize(self):

        digraph = 'digraph finite_state_machine { size="8,8" node [shape = circle];'

        for enj, j in enumerate(self.P):
            for eni, i in enumerate(j):
                if i != 0:
                    digraph += f"{enj + 1} -> {eni + 1} [label = {i}];"

        digraph += "}"

        s = Source(digraph, filename="markov_chains_graph.gv", format="png")
        s.view()


if __name__ == '__main__':

    b0 = [0.2, 0.4, 0.1, 0.3]
    P = [[0.2, 0.8, 0.0, 0.0],
         [0.3, 0.2, 0.2, 0.3],
         [0.0, 0.0, 0.2, 0.8],
         [0.5, 0.3, 0.0, 0.2]]

    markov_chain = MarkovChains(b0, P)
    MarkovChains.chains(markov_chain)
    MarkovChains.visualize(markov_chain)
