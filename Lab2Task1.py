import math

def function1 (x):
    if x > 45:
        z = -(x ** 0.5)
    else:
        z = math.sin(2 * x)
    return z

def function2 (p):
    a = 0
    b = 1
    if p < a:
        return a
    else:
        while p >= b:
            a, b = b, a + b
        return b

def main():
    x = float(input("Введіть значення x: "))
    z = function1 (x)
    print(f"Значення z = {z}")

    p = float(input("Введіть значення p: "))
    fib = function2 (p)
    print(f"Перше число з послідовності Фібоначі більше за p = {fib}")

if __name__ == "__main__":
    main()
