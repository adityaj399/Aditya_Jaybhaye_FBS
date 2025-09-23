#3. Python Program to Check if a Given Key Exists in a Dictionary or Not

d = {1: 100, 2: 200, 3: 300}
key = 2
if key in d:
    print(f"Key {key} exists with value {d[key]}")
else:
    print(f"Key {key} does not exist")