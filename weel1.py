def lower_triangle(n):
    print("Lower Triangle:")
    for i in range(1, n + 1):
        print('* ' * i)

def upper_triangle(n):
    print("\nUpper Triangle:")
    for i in range(n, 0, -1):
        print('* ' * i)

def pyramid(n):
    print("\nPyramid:")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '* ' * i
        print(spaces + stars.strip())

n = 5

lower_triangle(n)
upper_triangle(n)
pyramid(n)
