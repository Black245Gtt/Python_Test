lambda x: len(x)
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]
print(list(filter(lambda x: len(x), list1)))