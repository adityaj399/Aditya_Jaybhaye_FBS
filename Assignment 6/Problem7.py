n = 5   # number of rows

for i in range(n):
    print(" "*(n-i), end="")   # spaces for triangle shape
    val = 1   # first number of row is always 1
    for j in range(i+1):
        print(val, end=" ")
        val = val * (i-j) // (j+1)   # get next number
    print()