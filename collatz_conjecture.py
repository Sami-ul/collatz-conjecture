import matplotlib.pyplot as plt
import numpy as np

def collatz(start):
    num_list = [start]
    while start != 1:
        if start % 2 == 1:
            start = (start * 3) + 1
        elif start % 2 == 0:
            start = start / 2
        num_list.append(start)
    return num_list

num_list = collatz(27)

num_arr = np.array(num_list)
y = np.arange(1, len(num_list)+1)

plt.plot(y, num_arr, color="red")
plt.show()
