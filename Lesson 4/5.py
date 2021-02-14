from functools import reduce

my_list = [el for el in range(100, 1000+1) if el % 2 == 0]

print(reduce(lambda el_1, el_2: el_1 * el_2, my_list))