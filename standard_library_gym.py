# Enumeration
people = ['Alice', 'Bob', 'John', 'You', 'Cant', 'See', 'Me', 'Cena']

for index, name in enumerate(people, start=1):
    print(index, name)
    
# zip

people = ['Alice', 'Bob', 'John']
age = [56, 78, 99]
for age, name in zip(age, people):
    print(i)



"""itertools
functools
operator
collections
statistics"""

## Itertools
"""First Iteration"""
people = [
    ("Alice", "developer"),
    ("Bob", "developer"),
    ("John", "designer"),
    ("Mike", "designer"),
    ("Sarah", "developer"),
]

apex = []

for i in people:
    if i[1] in apex:
        continue
    apex.append(i[1])
    
by_career = {}
for i in apex:
    by_career[i] = []
    
for i in people:
    for j in by_career.keys():
        if i[1] == j:
            by_career[j].append(i[0])
print(by_career)


"""Second Iteration"""
"""Returns a group though"""
from itertools import groupby

people = [
    ("Alice", "developer"),
    ("Bob", "developer"),
    ("John", "designer"),
    ("Mike", "designer"),
    ("Sarah", "developer"),
]

people = sorted(people, key=lambda x: x[1])

for career, group in groupby(people, key=lambda x: x[1]):
    print(career, list(group))


