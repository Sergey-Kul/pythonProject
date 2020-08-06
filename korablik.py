from matplotlib.patches import Path, PathPatch, Polygon
import matplotlib.pyplot as plt


def kor(ax):
    poly = [(1, 3), (7, 2), (6, 1), (3, 1)]
    polygon = Polygon(poly, fc="blue", ec="black", lw=4)
    ax.add_patch(polygon)
    poly = [(4, 2.5), (4, 6), (7, 3)]
    polygon = Polygon(poly, fc="blue", ec="black", lw=4)
    ax.add_patch(polygon)
    ax.add_patch(path_patch)


vertices = [(1, 3), (7, 2), (6, 1), (3, 1), (1, 3),
            (4, 2.5), (4, 6), (7, 3), (4, 2.5)]

codes = [1, 2, 2, 2, 2, 1, 2, 2, 2]

path = Path(vertices, codes)
path_patch = PathPatch(path, lw=3)

n = 8
m = 7
plt.xlim(0, n)
plt.ylim(0, m)
ax = plt.gca()

kor(ax)
plt.show()
