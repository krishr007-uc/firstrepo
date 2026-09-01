def scramble(s):
    for i in range(len(s)):
        yield s[i:]+s[:i]


x = scramble("hello")

for l in x:
    print(l)

    