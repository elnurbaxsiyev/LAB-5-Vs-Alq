def f(x):
    return x**3 - 9 * x**2 + 5 * x - 6

def x(a, b, e):
    if f(a) * f(b) >= 0:
        print("Verilen araliqda kök yoxdur.")
        return None

    while (b - a) >= e:
        c = (a + b) / 2 
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

a = 8.0
b = 9.0
e = 0.01  # Hassasiyet

kok = x(a, b, e)

if kok is not None:
    print("Kök:", kok)
