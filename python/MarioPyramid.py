"""
    rows = 6
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')
        print(" ")
    print(" ")
    for i in range(rows + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")
"""

while True:
    h = int(input("Height: "))
    if h > 0 and h < 30000:
        break
for i in range(h):
    print(" " * (h-1-i), end="")
    print("#" * (i+1), end="  ")
    print("#" * (i+1), end="")
    print(" " * (h-1-i))
