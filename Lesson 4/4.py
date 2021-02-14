given_set = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_set = [el for el in given_set if given_set.count(el) == 1]

print(f"New list: {new_set}")