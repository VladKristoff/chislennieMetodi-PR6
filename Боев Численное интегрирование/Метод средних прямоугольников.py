def f(x):
    return x**4*(1+x**2)**-1

def integral(f, x1, x2, n):
    dx, integ = (x2-x1) / n, 0
    for i in range(n):
        integ += dx * f(x1 + dx / 2)
        x1 += dx
    return integ

print("При делении отрезка на 10: ", integral(f, 1, 2, 10))
print("При делении отрезка на 20: ", integral(f, 1, 2, 20))