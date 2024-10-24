from algos import bfs_traverse, dfs_traverse
from node import build_tree_from_heap, draw_tree, Node
import matplotlib.pyplot as plt


def colorize(path: list[Node], sb=0.3, r=18 / 255, g=150 / 255, b=240 / 255):
    if len(path) <= 0:
        return
    sk = (1 - sb) / len(path)

    for idx, n in enumerate(path):
        c = sk * (idx + 1) + sb
        n.color = (c * r, c * g, c * b)


def main():
    root = build_tree_from_heap([1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 39, 41, 43])

    bfs_path = bfs_traverse(root)
    print('BFS:' + ', '.join([str(b.val) for b in bfs_path]))

    dfs_path = dfs_traverse(root)
    print('DFS:' + ', '.join([str(b.val) for b in dfs_path]))

    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    colorize(bfs_path)
    ax[0].set_title('BFS Traverse Order')
    draw_tree(ax[0], root)

    colorize(dfs_path)
    ax[1].set_title('DFS Traverse Order')
    draw_tree(ax[1], root)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
