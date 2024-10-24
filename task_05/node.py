import uuid

import networkx as nx


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left = x - 1 / 2 ** layer
            pos[node.left.id] = (left, y - 1)
            add_edges(graph, node.left, pos, x=left, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right = x + 1 / 2 ** layer
            pos[node.right.id] = (right, y - 1)
            add_edges(graph, node.right, pos, x=right, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(ax, tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    nx.draw(tree, ax=ax, pos=pos, labels=labels, arrows=False, node_size=1500, node_color=colors, font_color="whitesmoke")


def build_tree_from_heap(heap):
    if not heap:
        return None

    root = Node(heap[0])
    nodes = [root]

    for i in range(1, len(heap)):
        new_node = Node(heap[i])
        parent = nodes[(i - 1) // 2]

        if parent.left is None:
            parent.left = new_node
        else:
            parent.right = new_node

        nodes.append(new_node)

    return root
