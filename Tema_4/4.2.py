list1 = [5, 10, 15, 20, 25, 50, 20]
for i, n in enumerate(list1):
    if n == 20:
        list1[i] = 200
print(list1)