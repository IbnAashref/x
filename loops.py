
n = 5
i = 1
x = 1
for i in range(n):
    for x in range(n-1):
        print(" * ")
    print(" * ")
    print("\n")


i = 1
while i < 5:
    print("   ")
    for x in range(i):
        print("* ")
        i += 1
