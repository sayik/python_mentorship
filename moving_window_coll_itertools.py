from itertools import pairwise
from collections import deque

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

window = deque(maxlen=3)

for i in numbers:
    window.append(i)
    if len(window) == 3:
        print(window)
