from node import build_tree_from_heap, draw_tree


def main():
    root = build_tree_from_heap([1, 3, 5, 7, 11, 13, 17, 19])
    #           1
    #     3          5
    #   7   11    13   17
    # 19
    draw_tree(root)


if __name__ == "__main__":
    main()
