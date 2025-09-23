#6. Python Program to Multiply All the Items in a Dictionary

d = {"a": 10, "b": 20, "c": 30}
res = 1
for i in d.values():
    res*=i
print("Multiplication of values:", res)