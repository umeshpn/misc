# A class to find a Hamiltonian path and an example for illustration.

from abc import abstractmethod

# Set this to true to print the graph and each backtracking step.
debug = False


# A graph representing non-cyclic Hamiltonian path.
class Graph:
    def __init__(self, n_nodes):
        self.graph = [[0 for column in range(n_nodes)] for row in range(n_nodes)]
        self.n_nodes = n_nodes
        self.n_sol = 0
        self.define_connections() # To be defined by child classes.

    @abstractmethod
    def define_connections(self):
        # When overriding, use the connect() method to connect nodes.
        # Do not connect 0 and self.n_nodes - 1.
        pass

    @staticmethod
    def node_name(node_num):
        # Specify how each node is named.
        # Override to have customized names.
        return str(node_num)

    def connect(self, a, b):
        """Connects nodes a and b."""
        self.graph[a][b] = 1
        self.graph[b][a] = 1

    def are_adjacent(self, a, b):
        """True iff there is an edge between the two nodes."""
        return self.graph[a][b] == 1
        
    def can_add(self, node, path, index):
        """Returns True of the node can be added to path[index]."""
        return node not in path and self.are_adjacent(path[index - 1], node)

    def print_path(self, path, is_ok):
        """Prints the path for final result and debugging.  Retracting info is printed only in debug mode."""
        if is_ok:
            self.n_sol += 1
            print('Solution %d: ' % self.n_sol , end='')
        elif debug:
            print('RETRACT:', end='')
        else:
            return

        # Print nodes in path.
        for node in path:
            if node == -1:
                break
            print(self.node_name(node) + " ==> ", end='')
        print()

    def solve(self):
        """Solve a hamiltonian path from node 0 to node (self.n_nodes - 1)."""
        path = [-1] * self.n_nodes

        # Start at node 0.
        path[0] = 0

        self.solve_recursively(path, 1)
        if self.n_sol == 0:
            print('No solution!')

    def solve_recursively(self, path, index):
        """Finds a path from index to self.n_nodes - 1.  Returns True if found, and false is needs to backtrack."""
        if index == self.n_nodes:
            # Found a path covering all nodes.
            self.print_path(path, True)
            return True

        if path[index-1] == self.n_nodes - 1:
            # Reached the end node prematurely.  Backtrack.
            return False

        for node in range(1, self.n_nodes):
            if self.can_add(node, path, index):
                path[index] = node

                if not self.solve_recursively(path, index + 1):
                    path[index] = -1
                    self.print_path(path, False)

        self.print_path(path, False)

        # Haven't found full path.  Backtrack.
        return False

    def print_graph(self):
        """Prints each node and its neighbors."""
        for i in range(self.n_nodes):
            print('%s: [' % self.node_name(i), end='')
            for j in range(self.n_nodes):
                if self.graph[i][j] == 1:
                    print(self.node_name(j) + " ", end='')
            print(' ]')


# Particular problem.
class YasarGraph(Graph):
    def __init__(self):
        super().__init__(23)
        
    def node_name(self, k):
        if k == 0:
            return "Start"
        elif k == self.n_nodes - 1:
            return "End"
        else:
            return chr(ord("A") + k-1)

    def define_connections(self):
        self.connect(0, 15)
        self.connect(0, 2)
        self.connect(0, 14)
        self.connect(0, 17)
        self.connect(0, 20)

        self.connect(22, 2)
        self.connect(22, 3)
        self.connect(22, 4)
        self.connect(22, 6)
        self.connect(22, 5)

        self.connect(1, 2)
        self.connect(1, 3)
        self.connect(1, 7)
        self.connect(2, 8)
        self.connect(4, 6)
        self.connect(4, 7)
        self.connect(4, 9)
        self.connect(5, 13)
        self.connect(5, 9)
        self.connect(5, 6)
        self.connect(5, 18)
        self.connect(7, 8)
        self.connect(7, 11)
        self.connect(8, 15)
        self.connect(9, 10)
        self.connect(9, 11)
        self.connect(10, 11)
        self.connect(10, 13)
        self.connect(10, 14)
        self.connect(10, 16)
        self.connect(11, 12)
        self.connect(11, 14)
        self.connect(12, 15)
        self.connect(13, 18)
        self.connect(14, 15)
        self.connect(14, 17)
        self.connect(16, 17)
        self.connect(16, 18)
        self.connect(16, 20)
        self.connect(17, 21)
        self.connect(18, 19)
        self.connect(18, 20)
        self.connect(19, 20)
        self.connect(20, 21)


# Entry point.
if __name__ == '__main__':
    yasar = YasarGraph()
    if debug:
        yasar.print_graph()
    yasar.solve()

