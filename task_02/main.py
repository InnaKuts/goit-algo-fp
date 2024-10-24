import sys
import matplotlib.pyplot as plt
import matplotlib.collections as mc
import numpy as np


def pythagoras_tree(p1, p2, level, angle=np.pi/6, scale=1.0/np.sqrt(2)):
    sin = scale * np.sin(angle)
    cos = scale * np.cos(angle)

    l_transform = np.array([
        [cos, -sin],
        [sin, cos]
    ])
    r_transform = np.array([
        [cos, sin],
        [-sin, cos]
    ])

    points = []

    def build_level(a, b, lvl):
        if lvl <= 0:
            return
        delta = b - a
        c = b + np.dot(l_transform, delta)
        d = b + np.dot(r_transform, delta)
        points.append([a, b])
        build_level(b, c, lvl - 1)
        build_level(b, d, lvl - 1)

    build_level(p1, p2, level)
    return points


def draw_pythagoras_tree(level):
    p1 = np.array([0, 0])
    p2 = np.array([0, 1])

    lines = pythagoras_tree(p1, p2, level)

    lc = mc.LineCollection(lines, linewidths=2)
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_title(f'Pythagoras Tree: {level}')
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)

    plt.axis('off')
    plt.show()


def safe(func, default):
    try:
        return func()
    except:
        return default


def main():
    level = safe(lambda: int(sys.argv[1]), None)
    if level is None:
        level = safe(lambda: int(input('Enter recursion level (default = 10): ')), 10)
    draw_pythagoras_tree(level)


if __name__ == '__main__':
    main()
