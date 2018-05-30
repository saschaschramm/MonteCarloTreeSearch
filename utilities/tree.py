def vertical_lines(last_node_flags):
    vertical_lines = []
    vertical_line = '\u2502'
    for last_node_flag in last_node_flags[0:-1]:
        if last_node_flag == False:
            vertical_lines.append(vertical_line + ' ' * 3)
        else:
            # space between vertical lines
            vertical_lines.append(' ' * 4)
    return ''.join(vertical_lines)

def horizontal_line(last_node_flags):
    horizontal_line = '\u251c\u2500\u2500 '
    horizontal_line_end = '\u2514\u2500\u2500 '
    if last_node_flags[-1]:
        return horizontal_line_end
    else:
        return horizontal_line

class Tree:

    def __init__(self):
        self.nodes = {}
        self.root = None

    def is_expandable(self, node):
        if node.terminal:
            return False
        if len(node.untried_actions) > 0:
            return True
        return False

    def iter(self, identifier, depth, last_node_flags):
        if identifier is None:
            node = self.root
        else:
            node = self.nodes[identifier]

        if depth == 0:
            yield "", node
        else:
            yield vertical_lines(last_node_flags) + horizontal_line(last_node_flags), node

        children = [self.nodes[identifier] for identifier in node.children_identifiers]
        last_index = len(children) - 1

        depth += 1
        for index, child in enumerate(children):
            last_node_flags.append(index == last_index)
            for edge, node in self.iter(child.identifier, depth, last_node_flags):
                yield edge, node
            last_node_flags.pop()

    def add_node(self, node, parent=None):
        self.nodes.update({node.identifier: node})

        if parent is None:
            self.root = node
            self.nodes[node.identifier].parent = None
        else:
            self.nodes[parent.identifier].children_identifiers.append(node.identifier)
            self.nodes[node.identifier].parent_identifier=parent.identifier

    def children(self, node):
        children = []
        for identifier in self.nodes[node.identifier].children_identifiers:
            children.append(self.nodes[identifier])
        return children

    def parent(self, node):
        parent_identifier = self.nodes[node.identifier].parent_identifier
        if parent_identifier is None:
            return None
        else:
            return self.nodes[parent_identifier]

    def show(self):
        lines = ""
        for edge, node in self.iter(identifier=None, depth=0, last_node_flags=[]):
            lines += "{}{}\n".format(edge, node)
        print(lines)