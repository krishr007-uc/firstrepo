x = input("What's x?")
y = input("What's y?")
if float(y) == 0:
    print("Error: cannot divide by zero")
else:
    z = round(float(x) / float(y), 3)
    print(f"{z:.2f}")