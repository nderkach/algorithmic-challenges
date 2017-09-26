class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

    def color_graph(graph, colors):
        for node in graph:

            # get the node's neighbors' colors, as a set so we
            # can check if a color is illegal in constant time
            illegal_colors = \
                set([neighbor.color for neighbor in node.neighbors if neighbor.color])
            legal_colors = \
                [color for color in colors if color not in illegal_colors]

            # assign the first legal color
            node.color = legal_colors[0]

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]
