def simpleGeneratorfun():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
x=simpleGeneratorfun()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))