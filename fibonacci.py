def fibonacci(n):
    if n==0:
        yield [0]
    elif n==1:
        yield [0, 1]
    else:
        fib_object=fibonacci(n-1)
        num1 = next(fib_object)
        x=num1.pop()

        y=num1.pop()
        yield num1 + [y, x, x+y]


for i in fibonacci(5):
    print(i)