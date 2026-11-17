from itertools import pairwise
from collections import deque


## With deque
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

window = deque(maxlen=3)

for i in numbers:
    window.append(i)
    if len(window) == 3:
        print(window)


## Manually with two variables using while loop
start, end = 0, 3

while end <= len(numbers):
    print(numbers[start: end])
    start += 1
    end += 1


## Manually using for loop
start, end = 0, 3

for _ in range(len(numbers)):
    print(numbers[start: end])
    
    if end == len(numbers):
        break
    start += 1
    end += 1
    
