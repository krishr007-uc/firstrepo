def newfib(n):
    if n==0:
        yield 0
    elif n==1:
        yield 1
    else:
        g = newfib(n-1)
        h = newfib(n-2)
        yield next(g)+next(h)

n=int(input("Enter a number: "))

for i in range(n):
    k = newfib(i)
    print(next(k))
