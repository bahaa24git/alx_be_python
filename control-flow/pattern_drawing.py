size = int(input("Enter the size of the pattern:"))
current = 1
while current <= size:
    for i in range(1, size + 1):
        print('*', end="")
        i += 1
    print()       
    current += 1