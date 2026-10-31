
## Before
### Counter
list_to_count = ["major", "general", "it's", "major", "general", "major", "general","major", "general", "major"]

new_dict = dict(zip(set(list_to_count), [0 for _ in range(len(set(list_to_count)))]))

print(new_dict)

print(dict.fromkeys(set(list_to_count), 0))


## After
from **collections import Counter**

list_to_count = ["major", "general", "it's", "major", "general", "major", "general","major", "general", "major"]

print(Counter(list_to_count))
