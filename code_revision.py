# Collatz Conjecture
"""First Iteration"""
def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    count = 0
    while number != 1:
        if number % 2 == 0:
            count += 1
            number = number // 2
            continue
        if number % 2:
            count += 1
            number = number * 3 +1
    return count

"""Second Iteration"""
def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    count = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        count += 1
    return count

"""Third Iteration"""
"""With Recurison"""
def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    if number == 1:
        return 0

    if number % 2 == 0:
        return 1 + steps(number // 2)

    return 1 + steps(number * 3 + 1)

## using aall and takewhile
print(all(False if i < 0 else True for i in [1, -2, 3]))

numbers = [50, 5, 6, -7]

from itertools import takewhile

result = all(i >= 0 for i in takewhile(lambda x: x >= 0, numbers))
print(result)
