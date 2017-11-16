from statistics import easy, hard
import matplotlib.pyplot as plt

l1 = []
l1.append(easy)
l1.append(hard)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

# rectangular box plot
bplot1 = axes[0].boxplot(l1, vert=True, patch_artist=True, showfliers=False)

bplot2 = axes[1].boxplot(l1, vert=True, patch_artist=True)

# fill with colors
colors = ['lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

print(bplot1.get('boxes'))

# adding horizontal grid lines
for ax in axes:
    ax.yaxis.grid(True)
    ax.set_xticks([y+1 for y in range(len(l1))], )
    ax.set_xlabel('Sudoku Difficulty')
    ax.set_ylabel('Time to Solve (s)')

# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(len(l1))],
         xticklabels=['easy', 'hard'])
plt.suptitle('Boxplots Comparing Time to Solve a set of Easy and Hard Sudokus')

plt.show()
