my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = []

for el in range(len(my_list) - 1):
    if my_list[el] < my_list[el + 1]:
        new_list.append(my_list[el + 1])

print(f"Original list: {my_list}")
print(f"New list: {new_list}")