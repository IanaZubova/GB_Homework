from itertools import cycle

condition = 0
for el in cycle("HappyMonday"):
    if condition > 21:
        break
    print(el)
    condition += 1