
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# Function to draw the towers and disks
def draw(A, B, C, n):
    plt.clf()

    colors = ['red', 'green', 'blue', 'orange',
              'purple', 'cyan', 'yellow', 'pink']

    positions = [0, 3, 6]

    for x, tower in zip(positions, [A, B, C]):
        plt.plot([x, x], [0, n+1], 'k', linewidth=3)

        for j, disk in enumerate(tower):
            w = disk * 0.3
            color = colors[(disk-1) % len(colors)]

            rect = patches.Rectangle(
                (x-w/2, j+0.1), w, 0.4,
                color=color
            )
            plt.gca().add_patch(rect)

    plt.xlim(-2, 8)
    plt.ylim(0, n+2)
    plt.xticks([0, 3, 6], ['A', 'B', 'C'])
    plt.pause(0.5)


# Recursive Tower of Hanoi function
def hanoi(n, A, B, C, towers):
    if n == 1:
        towers[C].append(towers[A].pop())
        draw(*towers, total)
        return

    hanoi(n-1, A, C, B, towers)

    towers[C].append(towers[A].pop())
    draw(*towers, total)

    hanoi(n-1, B, A, C, towers)


# Main program
total = 4
towers = [list(range(total, 0, -1)), [], []]

plt.ion()
draw(*towers, total)

hanoi(total, 0, 1, 2, towers)

plt.ioff()
plt.show()

print("Total moves:", 2**total - 1)
