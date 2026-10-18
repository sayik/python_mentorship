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

------------------------------------------------------------------------------------------------------------------------------------

## using aall and takewhile
- takewhile stops completely the moment it encounters the first element that evaluates to False.
print(all(False if i < 0 else True for i in [1, -2, 3]))

numbers = [50, 5, 6, -7]

from itertools import takewhile

result = all(i >= 0 for i in takewhile(lambda x: x >= 0, numbers))
print(result)


"""Using Sorted"""

users = [{"name":"Alice", "age":8}, {"name":"Bob", "age":75}, {"name":"John", "age":55}]

result = sorted(users, key=lambda user: user["age"], reverse=True)

print(result)
-------------------------------------------------------------------------------------------------------------------
## Reverse and iteration 

price = [10, 20, 30]

# after_tax = list(map(lambda price: price + price * 0.18, price))
# print(after_tax)

for i in price[::-1]:
    print(i)

## with reversed built in 
for item in reversed(price):
    print(item)

--------------------------------------------------------------------------------------------------------------------
## Transforamtion with map
price = [10, 20, 30]

after_tax = list(map(lambda price: price + price * 0.18, price))
print(after_tax)

-------------------------------------------------------------------------------------------------------------------------

## Accessing attribute dynamically
### Before 
class User:
    name = "Alice"

user = User()

def get_value(object_to_look, item):
    return object_to_look.__class__.__dict__[item]

print(get_value(user, "name"))  # Alice
class User:
    name = "Alice"
    
### After    
user = User()

def get_value(object_to_look, item):
    return getattr(object_to_look, item)
    
setattr(user, "age", 55)
print(get_value(user, "name"))
print(getattr(user, "age"))
print(hasattr(user, "mat"))

----------------------------------------------------------------------------------------------------------------------------
## strict parallel iteration. 

words = ["pythion", "is", "really", "fun"]
meow = [1, 2, 3]

for i, j in zip(words, meow, strict=True):
    print(i, j)

### Error handled 
words = ["pythion", "is", "really", "fun"]
meow = [1, 2, 3]

try:
    for i, j in zip(words, meow, strict=True):
        print(i, j)
except ValueError as e:
    print(f"Length mismatch: {e}")
