lst = [12, 12, 90, 45]
n = len(lst)
count = i = 0
while i < n :
    count += (lst[i] + 1) % 2
    i += 1
print(count)