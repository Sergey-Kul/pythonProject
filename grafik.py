import matplotlib.pyplot as plt

line = plt.plot([1, 5, -3, -0.5], [1, 25, 9, 0.25])

plt.setp(line, color='black', linewidth=2, marker='o')

plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.show()
