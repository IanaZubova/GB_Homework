from math import factorial

n = int(input('Insert value: '))

def generator():
    for el in range(1, n + 1):
        yield el

g = generator()

for el in g:
    print(el)

print(f"Factorial is: {factorial(n)}")