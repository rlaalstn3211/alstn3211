def calculate_y(a, b, max_x):

    for x in range(max_x + 1):
        y = a ** 2 * x + b
        print(f'{a} x {a} x {x} + {b} = {y}')

a = float(input("a: "))
b = float(input("b: "))
max_x = int(input("Max: "))

calculate_y(a, b, max_x)