def function2 (p):
    a = 0
    b = 1
    if p < a:
        return a
    else:
        while p >= b:
            a, b = b, a + b
        return b